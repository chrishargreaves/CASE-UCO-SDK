#!/usr/bin/env python3
"""Synchronize the pinned MITRE ATT&CK technique catalog from STIX 2.1.

Writes ``extensions/attack-technique/mitre-attack-catalog.ttl``: the complete
Enterprise, Mobile and ICS ATT&CK technique set of one release, in the UCO
1.5.0 ``uco-action:Technique`` metaclass pattern (ucoProject/UCO PR #676):

* every technique and sub-technique is a punned ``owl:Class`` that is also an
  instance of ``uco-action:Technique`` and carries ``uco-action:techniqueID``;
* a technique ``rdfs:subClassOf uco-action:Action``; a sub-technique
  ``rdfs:subClassOf`` its parent technique (``subtechnique-of``);
* tactics (``dcterms:subject``), platforms (``dcterms:coverage``) and matrix
  membership (``dcterms:isPartOf``) are annotations, never class axioms;
* deprecated and revoked techniques stay in the catalog with
  ``owl:deprecated true`` so older graphs keep validating; a revoked technique
  points at its successor with ``dcterms:isReplacedBy`` (``revoked-by``).

Default source: ``mitre-attack/attack-stix-data``, pinned release recorded in
``extensions/attack-technique/manifest.json`` with a SHA-256 per bundle.

Usage:
    # Refresh from a pinned ATT&CK release (network)
    python3 mcp_server/tools/sync_attack_catalog.py --attack-version 19.2

    # Regenerate from local STIX bundles (air-gapped); the directory holds
    # enterprise-attack-<v>.json, mobile-attack-<v>.json, ics-attack-<v>.json
    python3 mcp_server/tools/sync_attack_catalog.py --stix-dir /path/to/stix --attack-version 19.2

    # Check the committed catalog against upstream without writing
    python3 mcp_server/tools/sync_attack_catalog.py --attack-version 19.2 --check
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

sys.path.insert(0, str(PROJECT_ROOT / "mcp_server"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from extension_paths import extension_dir  # noqa: E402
from technique_catalog_ttl import (  # noqa: E402
    ANNOTATION_DECLARATIONS,
    ANNOTATION_PREFIXES,
    TacticEntry,
    TechniqueEntry,
    qualify_subtechnique_labels,
    render_matrix,
    render_tactic,
    render_technique,
    summarize_description,
    technique_sort_key,
)

EXT_DIR = extension_dir("attack-technique", PROJECT_ROOT)
CATALOG_FILE = "mitre-attack-catalog.ttl"
MANIFEST_FILE = "manifest.json"

STIX_REPO = "mitre-attack/attack-stix-data"
DEFAULT_ATTACK_VERSION = "19.2"
TECHNIQUE_NS = "https://attack.mitre.org/techniques/"
TACTIC_NS = "https://attack.mitre.org/tactics/"

# domain key -> (STIX directory/file stem, kill_chain_name, matrix IRI, label)
DOMAINS: dict[str, tuple[str, str, str, str]] = {
    "enterprise": (
        "enterprise-attack",
        "mitre-attack",
        "https://attack.mitre.org/matrices/enterprise/",
        "Enterprise ATT&CK",
    ),
    "mobile": (
        "mobile-attack",
        "mitre-mobile-attack",
        "https://attack.mitre.org/matrices/mobile/",
        "Mobile ATT&CK",
    ),
    "ics": (
        "ics-attack",
        "mitre-ics-attack",
        "https://attack.mitre.org/matrices/ics/",
        "ICS ATT&CK",
    ),
}
ATTACK_SOURCE_NAMES = {"mitre-attack", "mitre-mobile-attack", "mitre-ics-attack"}
TECHNIQUE_ID_RE = re.compile(r"^T[0-9]{4}(?:\.[0-9]{3})?$")
CATALOG_ID_RE = re.compile(r"^attack:(T[0-9]{4}(?:\.[0-9]{3})?)$", re.MULTILINE)


def _fetch(url: str, timeout: int = 300) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "case-uco-sdk-sync"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def stix_url_for(domain: str, version: str) -> str:
    stem = DOMAINS[domain][0]
    return (
        f"https://raw.githubusercontent.com/{STIX_REPO}/master/"
        f"{stem}/{stem}-{version}.json"
    )


def load_bundles(
    version: str, stix_dir: Path | None, domains: list[str]
) -> dict[str, tuple[dict, dict[str, str]]]:
    """Return domain -> (bundle, provenance{source, sha256})."""

    loaded: dict[str, tuple[dict, dict[str, str]]] = {}
    for domain in domains:
        stem = DOMAINS[domain][0]
        if stix_dir is not None:
            path = stix_dir / f"{stem}-{version}.json"
            if not path.is_file():
                raise SystemExit(f"missing STIX bundle: {path}")
            raw = path.read_bytes()
            source = f"{stix_url_for(domain, version)} (local copy)"
        else:
            source = stix_url_for(domain, version)
            print(f"fetching {source}")
            raw = _fetch(source)
        bundle = json.loads(raw.decode("utf-8"))
        bundle_version = _version_from_bundle(bundle)
        if bundle_version and bundle_version != version:
            raise SystemExit(
                f"{stem} bundle reports ATT&CK v{bundle_version}, expected v{version}"
            )
        loaded[domain] = (
            bundle,
            {"source": source, "sha256": hashlib.sha256(raw).hexdigest()},
        )
    return loaded


def _version_from_bundle(bundle: dict) -> str | None:
    for obj in bundle.get("objects") or []:
        if obj.get("type") == "x-mitre-collection" and obj.get("x_mitre_version"):
            return str(obj["x_mitre_version"])
    return None


def _attack_ref(obj: dict) -> tuple[str | None, str | None]:
    for ref in obj.get("external_references") or []:
        if ref.get("source_name") in ATTACK_SOURCE_NAMES and ref.get("external_id"):
            return str(ref["external_id"]), ref.get("url")
    return None, None


def parse_domain(
    domain: str, bundle: dict
) -> tuple[dict[str, TechniqueEntry], dict[str, TacticEntry]]:
    """Parse one STIX bundle into technique and tactic entries."""

    _, kill_chain, matrix_iri, _ = DOMAINS[domain]
    objects = bundle.get("objects") or []

    tactics: dict[str, TacticEntry] = {}
    tactic_by_shortname: dict[str, str] = {}
    for obj in objects:
        if obj.get("type") != "x-mitre-tactic" or obj.get("revoked"):
            continue
        tactic_id, url = _attack_ref(obj)
        if not tactic_id:
            continue
        tactic_by_shortname[str(obj.get("x_mitre_shortname"))] = tactic_id
        tactics[tactic_id] = TacticEntry(
            tactic_id=tactic_id,
            curie=f"attack-tactic:{tactic_id}",
            name=str(obj.get("name") or tactic_id),
            description=summarize_description(str(obj.get("description") or ""), 300),
            matrix_iri=matrix_iri,
            see_also=url,
        )

    stix_to_id: dict[str, str] = {}
    for obj in objects:
        if obj.get("type") == "attack-pattern":
            ext_id, _ = _attack_ref(obj)
            if ext_id:
                stix_to_id[str(obj["id"])] = ext_id

    parent_of: dict[str, str] = {}
    replaced_by: dict[str, list[str]] = {}
    for obj in objects:
        if obj.get("type") != "relationship":
            continue
        src = stix_to_id.get(str(obj.get("source_ref")))
        dst = stix_to_id.get(str(obj.get("target_ref")))
        if not src or not dst:
            continue
        if obj.get("relationship_type") == "subtechnique-of":
            parent_of[src] = dst
        elif obj.get("relationship_type") == "revoked-by":
            replaced_by.setdefault(src, []).append(dst)

    techniques: dict[str, TechniqueEntry] = {}
    for obj in objects:
        if obj.get("type") != "attack-pattern":
            continue
        ext_id, url = _attack_ref(obj)
        if not ext_id or not TECHNIQUE_ID_RE.match(ext_id):
            continue
        revoked = bool(obj.get("revoked"))
        deprecated = bool(obj.get("x_mitre_deprecated"))
        tactic_ids: list[str] = []
        for phase in obj.get("kill_chain_phases") or []:
            if phase.get("kill_chain_name") != kill_chain:
                continue
            tid = tactic_by_shortname.get(str(phase.get("phase_name")))
            if tid and tid not in tactic_ids:
                tactic_ids.append(tid)
        parent = parent_of.get(ext_id)
        if parent is None and "." in ext_id:
            parent = ext_id.split(".")[0]
        status = ""
        if revoked:
            successors = sorted(set(replaced_by.get(ext_id, [])), key=technique_sort_key)
            status = "Revoked by MITRE ATT&CK" + (
                f"; superseded by {', '.join(successors)}." if successors else "."
            )
        elif deprecated:
            status = "Deprecated by MITRE ATT&CK."
        modified = str(obj.get("modified") or "")[:10] or None
        techniques[ext_id] = TechniqueEntry(
            technique_id=ext_id,
            curie=f"attack:{ext_id}",
            name=str(obj.get("name") or ext_id),
            description=summarize_description(str(obj.get("description") or "")),
            parent_curie=f"attack:{parent}" if parent else None,
            tactic_curies=[f"attack-tactic:{t}" for t in tactic_ids],
            platforms=sorted(
                {str(p) for p in obj.get("x_mitre_platforms") or [] if p and p != "None"}
            ),
            matrix_iris=[matrix_iri],
            see_also=[url] if url else [],
            replaced_by_curies=[
                f"attack:{t}"
                for t in sorted(set(replaced_by.get(ext_id, [])), key=technique_sort_key)
            ],
            deprecated=revoked or deprecated,
            modified=modified,
            comment_suffix=status,
        )
    return techniques, tactics


def build_catalog(
    bundles: dict[str, tuple[dict, dict[str, str]]],
) -> tuple[dict[str, TechniqueEntry], dict[str, TacticEntry]]:
    techniques: dict[str, TechniqueEntry] = {}
    tactics: dict[str, TacticEntry] = {}
    for domain, (bundle, _) in bundles.items():
        dom_techniques, dom_tactics = parse_domain(domain, bundle)
        for tid, entry in dom_techniques.items():
            existing = techniques.get(tid)
            if existing is None:
                techniques[tid] = entry
                continue
            # An ID present in several domains is one technique; merge the
            # domain-specific annotations rather than emitting two classes.
            for attr in ("tactic_curies", "matrix_iris", "see_also"):
                merged = getattr(existing, attr)
                merged.extend(v for v in getattr(entry, attr) if v not in merged)
            existing.platforms = sorted(set(existing.platforms) | set(entry.platforms))
        tactics.update(dom_tactics)

    # A parent missing from the release (should not happen upstream) would
    # leave a sub-technique outside uco-action:Action; fall back to Action.
    for entry in techniques.values():
        if entry.parent_curie and entry.parent_curie[len("attack:"):] not in techniques:
            entry.parent_curie = None
    qualify_subtechnique_labels(techniques)
    return techniques, tactics


def render_catalog(
    techniques: dict[str, TechniqueEntry],
    tactics: dict[str, TacticEntry],
    *,
    attack_version: str,
    bundles: dict[str, tuple[dict, dict[str, str]]],
) -> str:
    sources = "".join(
        f"#   {DOMAINS[d][3]}: {prov['source']}\n#     sha256 {prov['sha256']}\n"
        for d, (_, prov) in bundles.items()
    )
    year = max(
        (
            str(obj.get("modified") or "")[:4]
            for bundle, _ in bundles.values()
            for obj in bundle.get("objects") or []
            if obj.get("type") == "x-mitre-collection"
        ),
        default=str(datetime.now(timezone.utc).year),
    )
    header = (
        ANNOTATION_PREFIXES
        + f"@prefix attack: <{TECHNIQUE_NS}> .\n"
        + f"@prefix attack-tactic: <{TACTIC_NS}> .\n"
        + "\n"
        "#\n"
        f"# MITRE ATT&CK v{attack_version} technique catalog (Enterprise, Mobile, ICS),\n"
        "# expressed with the UCO 1.5.0 uco-action:Technique metaclass\n"
        "# (ucoProject/UCO PR #676).\n"
        "#\n"
        "# GENERATED FILE - do not edit by hand. Regenerate with:\n"
        f"#   make sync-attack ATTACK_VERSION={attack_version}\n"
        "#\n"
        "# \"A Technique instance is an owl:Class that is a subclass of\n"
        "# uco-action:Action.\" Each technique is a punned class: an instance of\n"
        "# the metaclass and an owl:Class. Sub-techniques specialize their parent\n"
        "# technique. Concrete behaviors are typed with the technique class.\n"
        "#\n"
        "# Sources:\n"
        f"{sources}"
        "#\n"
        f"# \u00a9 {year} The MITRE Corporation. This work is reproduced and\n"
        "# distributed with the permission of The MITRE Corporation.\n"
        "# ATT&CK terms of use: https://attack.mitre.org/resources/legal-and-branding/terms-of-use/\n"
        "#\n"
        "\n"
        + ANNOTATION_DECLARATIONS
        + "\n"
    )
    matrices = "\n".join(
        render_matrix(
            DOMAINS[d][2],
            DOMAINS[d][3],
            attack_version,
            see_also="https://attack.mitre.org/",
        )
        for d in bundles
    )
    tactic_blocks = "\n".join(
        render_tactic(tactics[t]) for t in sorted(tactics, key=technique_sort_key)
    )
    technique_blocks = "\n".join(
        render_technique(techniques[t], "MITRE ATT&CK")
        for t in sorted(techniques, key=technique_sort_key)
    )
    return (
        header
        + "#\n# Matrices\n#\n\n"
        + matrices
        + "\n#\n# Tactics (annotation values)\n#\n\n"
        + tactic_blocks
        + "\n#\n# Techniques and sub-techniques\n#\n\n"
        + technique_blocks
    )


def catalog_technique_ids(path: Path | None = None) -> set[str]:
    path = path or EXT_DIR / CATALOG_FILE
    if not path.is_file():
        return set()
    return set(CATALOG_ID_RE.findall(path.read_text(encoding="utf-8")))


def catalog_counts(techniques: dict[str, TechniqueEntry]) -> dict[str, int]:
    return {
        "technique_count": len(techniques),
        "subtechnique_count": sum(1 for e in techniques.values() if e.parent_curie),
        "deprecated_count": sum(1 for e in techniques.values() if e.deprecated),
    }


def update_manifest_provenance(
    *,
    attack_version: str,
    bundles: dict[str, tuple[dict, dict[str, str]]],
    counts: dict[str, int],
) -> None:
    manifest_path = EXT_DIR / MANIFEST_FILE
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    provenance: dict = {
        "attack_stix_repo": f"https://github.com/{STIX_REPO}",
        "attack_version": attack_version,
        "domains": {
            d: {"source": prov["source"], "sha256": prov["sha256"]}
            for d, (_, prov) in bundles.items()
        },
        **counts,
        "synced": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "sync_tool": "mcp_server/tools/sync_attack_catalog.py",
        "license": "MITRE ATT&CK Terms of Use "
        "(https://attack.mitre.org/resources/legal-and-branding/terms-of-use/)",
    }
    manifest["provenance"] = provenance
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(
        f"updated manifest provenance (ATT&CK v{attack_version}, "
        f"{counts['technique_count']} techniques)"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--attack-version",
        default=None,
        help=f"ATT&CK release to fetch (default: manifest pin, else {DEFAULT_ATTACK_VERSION})",
    )
    parser.add_argument(
        "--stix-dir",
        type=Path,
        default=None,
        help="Directory with <domain>-attack-<version>.json bundles (offline)",
    )
    parser.add_argument(
        "--domains",
        default=",".join(DOMAINS),
        help="Comma-separated domains to include (default: enterprise,mobile,ics)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit non-zero when the committed catalog differs from upstream membership",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print counts and exit without writing files",
    )
    args = parser.parse_args(argv)

    version = args.attack_version
    if version is None:
        manifest = json.loads((EXT_DIR / MANIFEST_FILE).read_text(encoding="utf-8"))
        version = (manifest.get("provenance") or {}).get(
            "attack_version"
        ) or DEFAULT_ATTACK_VERSION
    domains = [d.strip() for d in args.domains.split(",") if d.strip()]
    unknown = [d for d in domains if d not in DOMAINS]
    if unknown:
        raise SystemExit(f"unknown domain(s): {', '.join(unknown)}")

    bundles = load_bundles(version, args.stix_dir, domains)
    techniques, tactics = build_catalog(bundles)
    counts = catalog_counts(techniques)
    print(
        f"ATT&CK v{version}: {counts['technique_count']} techniques "
        f"({counts['subtechnique_count']} sub-techniques, "
        f"{counts['deprecated_count']} deprecated/revoked), {len(tactics)} tactics"
    )

    if args.check:
        committed = catalog_technique_ids()
        missing = sorted(set(techniques) - committed, key=technique_sort_key)
        extra = sorted(committed - set(techniques), key=technique_sort_key)
        if missing or extra:
            print(f"catalog drift: {len(missing)} missing, {len(extra)} extra")
            return 1
        print("catalog membership matches upstream")
        return 0
    if args.dry_run:
        return 0

    ttl = render_catalog(techniques, tactics, attack_version=version, bundles=bundles)
    out = EXT_DIR / CATALOG_FILE
    out.write_text(ttl, encoding="utf-8")

    try:
        import rdflib

        rdflib.Graph().parse(str(out), format="turtle")
    except ImportError:
        print("warning: rdflib not installed; skipped TTL parse check")

    update_manifest_provenance(attack_version=version, bundles=bundles, counts=counts)
    print(f"wrote {out.relative_to(PROJECT_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
