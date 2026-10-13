#!/usr/bin/env python3
"""Synchronize the pinned MITRE ATLAS technique catalog.

Writes ``extensions/atlas-technique/mitre-atlas-catalog.ttl``: every
technique and sub-technique of one ATLAS data release (Adversarial Threat
Landscape for AI Systems, https://atlas.mitre.org), in the same UCO 1.5.0
``uco-action:Technique`` metaclass pattern as the ATT&CK catalog:

* each technique is a punned ``owl:Class`` that is also an instance of
  ``uco-action:Technique`` and carries ``uco-action:techniqueID``;
* a technique ``rdfs:subClassOf uco-action:Action``; a sub-technique
  ``rdfs:subClassOf`` the technique it ``specializes``;
* tactics (``achieves``), platforms and matrix membership are annotations;
* an ATLAS technique adapted from ATT&CK links to it with ``rdfs:seeAlso``
  (an annotation, so the ATT&CK catalog is not a dependency).

Source: ``mitre-atlas/atlas-data`` ``dist/v6/ATLAS-<release>.yaml`` at tag
``v<release>`` (format 6.x). The release and SHA-256 are recorded in
``extensions/atlas-technique/manifest.json``.

Usage:
    python3 mcp_server/tools/sync_atlas_catalog.py --atlas-release 2026.09
    python3 mcp_server/tools/sync_atlas_catalog.py --atlas-file /path/to/ATLAS-2026.09.yaml
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

EXT_DIR = extension_dir("atlas-technique", PROJECT_ROOT)
CATALOG_FILE = "mitre-atlas-catalog.ttl"
MANIFEST_FILE = "manifest.json"

ATLAS_REPO = "mitre-atlas/atlas-data"
DEFAULT_ATLAS_RELEASE = "2026.09"
TECHNIQUE_NS = "https://atlas.mitre.org/techniques/"
TACTIC_NS = "https://atlas.mitre.org/tactics/"
MATRIX_IRI = "https://atlas.mitre.org/matrices/ATLAS"
ATTACK_TECHNIQUE_NS = "https://attack.mitre.org/techniques/"
ATTACK_TACTIC_NS = "https://attack.mitre.org/tactics/"
TECHNIQUE_ID_RE = re.compile(r"^AML\.T[0-9]{4}(?:\.[0-9]{3})?$")
TACTIC_ID_RE = re.compile(r"^AML\.TA[0-9]{4}$")
ATTACK_ID_RE = re.compile(r"^(T[0-9]{4}(?:\.[0-9]{3})?|TA[0-9]{4})$")
CATALOG_ID_RE = re.compile(r"^atlas:(AML\.T[0-9]{4}(?:\.[0-9]{3})?)$", re.MULTILINE)
SUPPORTED_FORMAT_MAJOR = "6"


def _fetch(url: str, timeout: int = 180) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": "case-uco-sdk-sync"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def atlas_url_for_release(release: str) -> str:
    return (
        f"https://raw.githubusercontent.com/{ATLAS_REPO}/v{release}/"
        f"dist/v6/ATLAS-{release}.yaml"
    )


def load_atlas(release: str, path: Path | None) -> tuple[dict, dict[str, str]]:
    try:
        import yaml
    except ImportError as exc:
        raise SystemExit("sync-atlas needs PyYAML: pip install pyyaml") from exc

    url = atlas_url_for_release(release)
    if path is not None:
        raw = path.read_bytes()
        source = f"{url} (local copy)"
    else:
        print(f"fetching {url}")
        raw = _fetch(url)
        source = url
    data = yaml.safe_load(raw.decode("utf-8"))
    if not isinstance(data, dict) or "techniques" not in data:
        raise SystemExit("not an ATLAS v6 data file (no top-level 'techniques')")
    fmt = str(data.get("format-version") or "")
    if fmt.split(".")[0] != SUPPORTED_FORMAT_MAJOR:
        raise SystemExit(f"unsupported ATLAS format-version {fmt!r}; expected 6.x")
    file_release = str((data.get("collection") or {}).get("version") or "")
    if file_release and file_release != release:
        raise SystemExit(f"file is ATLAS release {file_release}, expected {release}")
    return data, {"source": source, "sha256": hashlib.sha256(raw).hexdigest()}


def _relationships(data: dict) -> dict[str, dict[str, list[str]]]:
    """source id -> relationship-type -> [target ids]."""

    out: dict[str, dict[str, list[str]]] = {}
    for source, by_type in (data.get("relationships") or {}).items():
        for rel_type, rels in (by_type or {}).items():
            for rel in rels or []:
                target = rel.get("target")
                if target:
                    out.setdefault(str(source), {}).setdefault(str(rel_type), []).append(
                        str(target)
                    )
    return out


def _attack_iri(ref: dict | None, namespace: str) -> str | None:
    if not isinstance(ref, dict):
        return None
    attack_id = str(ref.get("id") or "")
    return f"{namespace}{attack_id}" if ATTACK_ID_RE.match(attack_id) else None


def build_catalog(data: dict) -> tuple[dict[str, TechniqueEntry], dict[str, TacticEntry]]:
    rels = _relationships(data)

    tactics: dict[str, TacticEntry] = {}
    for tactic_id, obj in (data.get("tactics") or {}).items():
        if not TACTIC_ID_RE.match(str(tactic_id)):
            continue
        attack_ref = _attack_iri(obj.get("attack-reference") or obj.get("ATT&CK-reference"), ATTACK_TACTIC_NS)
        tactics[tactic_id] = TacticEntry(
            tactic_id=tactic_id,
            curie=f"atlas-tactic:{tactic_id}",
            name=str(obj.get("name") or tactic_id),
            description=summarize_description(str(obj.get("description") or ""), 300),
            matrix_iri=MATRIX_IRI,
            see_also=attack_ref,
        )

    techniques: dict[str, TechniqueEntry] = {}
    raw_techniques = data.get("techniques") or {}
    for technique_id, obj in raw_techniques.items():
        if not TECHNIQUE_ID_RE.match(str(technique_id)):
            continue
        own = rels.get(technique_id, {})
        parents = [p for p in own.get("specializes", []) if p in raw_techniques]
        parent = parents[0] if parents else None
        if parent is None and technique_id.count(".") == 2:
            candidate = technique_id.rsplit(".", 1)[0]
            parent = candidate if candidate in raw_techniques else None
        tactic_ids = sorted(
            {t for t in own.get("achieves", []) if t in tactics}, key=technique_sort_key
        )
        see_also = []
        attack_ref = _attack_iri(obj.get("attack-reference"), ATTACK_TECHNIQUE_NS)
        if attack_ref:
            see_also.append(attack_ref)
        maturity = str(obj.get("maturity") or "").strip()
        modified = str(obj.get("modified-date") or "")[:10] or None
        techniques[technique_id] = TechniqueEntry(
            technique_id=technique_id,
            curie=f"atlas:{technique_id}",
            name=str(obj.get("name") or technique_id),
            description=summarize_description(str(obj.get("description") or "")),
            parent_curie=f"atlas:{parent}" if parent else None,
            tactic_curies=[f"atlas-tactic:{t}" for t in tactic_ids],
            platforms=sorted({str(p) for p in obj.get("platforms") or [] if p}),
            matrix_iris=[MATRIX_IRI],
            see_also=see_also,
            modified=modified,
            comment_suffix=f"ATLAS maturity: {maturity}." if maturity else "",
        )
    qualify_subtechnique_labels(techniques)
    return techniques, tactics


def render_catalog(
    techniques: dict[str, TechniqueEntry],
    tactics: dict[str, TacticEntry],
    *,
    release: str,
    provenance: dict[str, str],
    data: dict,
) -> str:
    year = str((data.get("collection") or {}).get("modified-date") or release)[:4]
    header = (
        ANNOTATION_PREFIXES
        + f"@prefix atlas: <{TECHNIQUE_NS}> .\n"
        + f"@prefix atlas-tactic: <{TACTIC_NS}> .\n"
        + "\n"
        "#\n"
        f"# MITRE ATLAS {release} technique catalog (Adversarial Threat Landscape\n"
        "# for AI Systems), expressed with the UCO 1.5.0 uco-action:Technique\n"
        "# metaclass (ucoProject/UCO PR #676).\n"
        "#\n"
        "# GENERATED FILE - do not edit by hand. Regenerate with:\n"
        f"#   make sync-atlas ATLAS_RELEASE={release}\n"
        "#\n"
        "# Each technique is a punned class: an instance of the metaclass and an\n"
        "# owl:Class. Sub-techniques specialize their parent technique. Concrete\n"
        "# behaviors are typed with the technique class. Links to MITRE ATT&CK\n"
        "# are rdfs:seeAlso annotations; the ATT&CK catalog is not imported.\n"
        "#\n"
        f"# Source: {provenance['source']}\n"
        f"#   sha256 {provenance['sha256']}\n"
        f"#   format-version {data.get('format-version')}\n"
        "#\n"
        f"# Copyright {year} MITRE. ATLAS data is licensed under the Apache\n"
        "# License, Version 2.0: https://github.com/mitre-atlas/atlas-data/blob/main/LICENSE\n"
        "#\n"
        "\n"
        + ANNOTATION_DECLARATIONS
        + "\n"
    )
    matrix = render_matrix(
        MATRIX_IRI, "MITRE ATLAS", release, see_also="https://atlas.mitre.org/"
    )
    tactic_blocks = "\n".join(
        render_tactic(tactics[t]) for t in sorted(tactics, key=technique_sort_key)
    )
    technique_blocks = "\n".join(
        render_technique(techniques[t], "MITRE ATLAS")
        for t in sorted(techniques, key=technique_sort_key)
    )
    return (
        header
        + "#\n# Matrix\n#\n\n"
        + matrix
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


def update_manifest_provenance(
    *, release: str, provenance: dict[str, str], data: dict, counts: dict[str, int]
) -> None:
    manifest_path = EXT_DIR / MANIFEST_FILE
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["provenance"] = {
        "atlas_data_repo": f"https://github.com/{ATLAS_REPO}",
        "atlas_release": release,
        "atlas_format_version": str(data.get("format-version")),
        "atlas_source": provenance["source"],
        "sha256": provenance["sha256"],
        **counts,
        "synced": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "sync_tool": "mcp_server/tools/sync_atlas_catalog.py",
        "license": "Apache-2.0 (https://github.com/mitre-atlas/atlas-data/blob/main/LICENSE)",
    }
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(
        f"updated manifest provenance (ATLAS {release}, "
        f"{counts['technique_count']} techniques)"
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--atlas-release",
        default=None,
        help=f"ATLAS data release tag without the leading v (default: manifest pin, else {DEFAULT_ATLAS_RELEASE})",
    )
    parser.add_argument(
        "--atlas-file",
        type=Path,
        default=None,
        help="Local dist/v6/ATLAS-<release>.yaml (offline)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit non-zero when the committed catalog differs from upstream membership",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print counts only")
    args = parser.parse_args(argv)

    release = args.atlas_release
    if release is None:
        manifest = json.loads((EXT_DIR / MANIFEST_FILE).read_text(encoding="utf-8"))
        release = (manifest.get("provenance") or {}).get(
            "atlas_release"
        ) or DEFAULT_ATLAS_RELEASE

    data, provenance = load_atlas(release, args.atlas_file)
    techniques, tactics = build_catalog(data)
    counts = {
        "technique_count": len(techniques),
        "subtechnique_count": sum(1 for e in techniques.values() if e.parent_curie),
        "tactic_count": len(tactics),
    }
    print(
        f"ATLAS {release}: {counts['technique_count']} techniques "
        f"({counts['subtechnique_count']} sub-techniques), {len(tactics)} tactics"
    )

    if args.check:
        committed = catalog_technique_ids()
        if committed != set(techniques):
            print(
                f"catalog drift: {len(set(techniques) - committed)} missing, "
                f"{len(committed - set(techniques))} extra"
            )
            return 1
        print("catalog membership matches upstream")
        return 0
    if args.dry_run:
        return 0

    ttl = render_catalog(
        techniques, tactics, release=release, provenance=provenance, data=data
    )
    out = EXT_DIR / CATALOG_FILE
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ttl, encoding="utf-8")

    import rdflib

    rdflib.Graph().parse(str(out), format="turtle")
    update_manifest_provenance(
        release=release, provenance=provenance, data=data, counts=counts
    )
    print(f"wrote {out.relative_to(PROJECT_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
