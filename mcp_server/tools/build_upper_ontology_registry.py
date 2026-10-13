#!/usr/bin/env python3
"""Build the pinned upper-ontology term registry used by concept coverage.

Strict concept coverage historically accepted *any* IRI under a profiled
upper-ontology namespace (BFO, gUFO, PROV-O, OWL-Time, GeoSPARQL, FOAF, ORG,
PROF, and since v1.31.0 QUDT and SOSA/SSN), which let fabricated terms such
as ``prov:CompletelyImaginaryProperty`` pass validation. This script
downloads pinned releases of each profiled ontology, extracts the exact
declared terms with their RDF roles (class, property, individual, datatype),
and writes a compact JSON registry to
``mcp_server/upper_ontology_registry.json``. The registry is committed to the
repository so validation works offline; re-run this script to refresh it when
a profiled ontology publishes a new supported release. It also writes
``mcp_server/qudt_unit_index.json``, the QUDT unit table behind the
``lookup_qudt_units`` MCP tool.

The pinned source files themselves are vendored under ``ontology/upper/``
(v1.19.0) so registry rebuilds are fully offline by default — no network
access is required unless you explicitly refresh the vendored snapshot.

Usage:
    # Offline rebuild from the vendored sources in ontology/upper/ (default)
    python3 mcp_server/tools/build_upper_ontology_registry.py

    # Refresh the vendored sources from upstream, then rebuild the registry
    python3 mcp_server/tools/build_upper_ontology_registry.py --fetch

    # Refresh only some sources (e.g. after bumping QUDT_VERSION)
    python3 mcp_server/tools/build_upper_ontology_registry.py --fetch \
        --only qudt,qudt-units,qudt-quantitykinds,qudt-prefixes

    # Rebuild from an alternate directory of downloaded files
    python3 mcp_server/tools/build_upper_ontology_registry.py --source-dir /path/to/downloaded
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import sys
import urllib.request
import zipfile
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
REGISTRY_PATH = PROJECT_ROOT / "mcp_server" / "upper_ontology_registry.json"
VENDORED_SOURCE_DIR = PROJECT_ROOT / "ontology" / "upper"
VENDORED_PROVENANCE = VENDORED_SOURCE_DIR / "provenance.json"
QUDT_UNIT_INDEX_PATH = PROJECT_ROOT / "mcp_server" / "qudt_unit_index.json"

QUDT_VERSION = "3.5.2"
QUDT_RELEASE_URL = (
    "https://github.com/qudt/qudt-public-repo/releases/download/"
    f"v{QUDT_VERSION}/qudt-public-repo-{QUDT_VERSION}.zip"
)

# Pinned sources for every ontology that UCO maintains a CDO-Shapes profile
# for. ``namespace_prefixes`` filters extracted terms so annotation vocabulary
# defined in the same file under other namespaces is not registered.
ONTOLOGY_SOURCES: dict[str, dict] = {
    "bfo": {
        "title": "Basic Formal Ontology (BFO) 2.0 / ISO 21838-2",
        "profile": "CDO-Shapes-BFO",
        "namespace_prefixes": ["http://purl.obolibrary.org/obo/BFO_"],
        "source_url": "http://purl.obolibrary.org/obo/bfo.owl",
        "local_file": "bfo.owl",
        "format": "xml",
    },
    "gufo": {
        "title": "gentle Unified Foundational Ontology (gUFO)",
        "profile": "CDO-Shapes-gufo",
        "namespace_prefixes": ["http://purl.org/nemo/gufo#"],
        "source_url": "https://nemo-ufes.github.io/gufo/gufo.ttl",
        "local_file": "gufo.ttl",
        "format": "turtle",
    },
    "prov-o": {
        "title": "W3C Provenance Ontology (PROV-O)",
        "profile": "CDO-Shapes-PROV-O",
        "namespace_prefixes": ["http://www.w3.org/ns/prov#"],
        "source_url": "http://www.w3.org/ns/prov-o.ttl",
        "local_file": "prov-o.ttl",
        "format": "turtle",
    },
    "owl-time": {
        "title": "W3C OWL-Time",
        "profile": "CDO-Shapes-Time",
        "namespace_prefixes": ["http://www.w3.org/2006/time#"],
        "source_url": "https://www.w3.org/2006/time.ttl",
        "local_file": "time.ttl",
        "format": "turtle",
    },
    "geosparql": {
        "title": "OGC GeoSPARQL 1.1 (core)",
        "profile": "CDO-Shapes-GeoSPARQL",
        "namespace_prefixes": ["http://www.opengis.net/ont/geosparql#"],
        "source_url": "https://opengeospatial.github.io/ogc-geosparql/geosparql11/geo.ttl",
        "local_file": "geo.ttl",
        "format": "turtle",
    },
    "geosparql-sf": {
        "title": "OGC Simple Features geometries (GeoSPARQL 1.1)",
        "profile": "CDO-Shapes-GeoSPARQL",
        "namespace_prefixes": ["http://www.opengis.net/ont/sf#"],
        "source_url": "https://opengeospatial.github.io/ogc-geosparql/geosparql11/sf_geometries.ttl",
        "local_file": "sf.ttl",
        "format": "turtle",
    },
    "foaf": {
        "title": "Friend of a Friend (FOAF) vocabulary",
        "profile": "CDO-Shapes-FOAF",
        "namespace_prefixes": ["http://xmlns.com/foaf/0.1/"],
        "source_url": "http://xmlns.com/foaf/spec/index.rdf",
        "local_file": "foaf.rdf",
        "format": "xml",
        # FOAF's RDF carries no owl:versionIRI/versionInfo; pin the spec
        # version manually so the fail-closed provenance check passes.
        "version_info": "0.99 (Paddington Edition, 2014-01-14)",
    },
    "org": {
        "title": "W3C Organization Ontology (ORG)",
        "profile": "CDO-Shapes-ORG",
        "namespace_prefixes": ["http://www.w3.org/ns/org#"],
        "source_url": "https://www.w3.org/ns/org.ttl",
        "local_file": "org.ttl",
        "format": "turtle",
    },
    "prof": {
        "title": "W3C Profiles Vocabulary (PROF)",
        "profile": "CDO-Shapes-PROF",
        "namespace_prefixes": ["http://www.w3.org/ns/dx/prof/"],
        "source_url": "https://www.w3.org/ns/dx/prof/",
        "local_file": "prof.ttl",
        "format": "turtle",
        "accept": "text/turtle",
        "exclude_prefixes": ["http://www.w3.org/ns/dx/prof/role/"],
    },
    "prof-roles": {
        "title": "W3C PROF Resource Roles vocabulary",
        "profile": "CDO-Shapes-PROF",
        "namespace_prefixes": ["http://www.w3.org/ns/dx/prof/role/"],
        "source_url": "https://www.w3.org/ns/dx/prof/role/",
        "local_file": "prof-roles.ttl",
        "format": "turtle",
        "accept": "text/turtle",
        # Roles are prof:ResourceRole / skos:Concept individuals.
        "typed_members_are_individuals": True,
        "version_info": "W3C Working Group Note 2019-12-18 (https://www.w3.org/TR/2019/NOTE-dx-prof-20191218/)",
    },
    # QUDT and SOSA/SSN have no CDO-Shapes profile; the SDK pins them
    # (issue #60, ucoProject/UCO#404) and ships minimal shapes under
    # ontology/upper/sdk-shapes/.
    "qudt": {
        "title": "QUDT schema (Quantities, Units, Dimensions and Types)",
        "profile": "SDK-pinned QUDT",
        "namespace_prefixes": ["http://qudt.org/schema/qudt/"],
        "source_url": QUDT_RELEASE_URL,
        "archive_member": "schema/SCHEMA_QUDT.ttl",
        "local_file": "qudt-schema.ttl",
        "format": "turtle",
    },
    "qudt-units": {
        "title": "QUDT units vocabulary",
        "profile": "SDK-pinned QUDT",
        "namespace_prefixes": ["http://qudt.org/vocab/unit/"],
        "source_url": QUDT_RELEASE_URL,
        "archive_member": "vocab/unit/VOCAB_QUDT-UNITS-ALL.ttl",
        "local_file": "qudt-units.ttl",
        "format": "turtle",
        # Units are typed qudt:Unit, a class outside this namespace.
        "typed_members_are_individuals": True,
    },
    "qudt-quantitykinds": {
        "title": "QUDT quantity kinds vocabulary",
        "profile": "SDK-pinned QUDT",
        "namespace_prefixes": ["http://qudt.org/vocab/quantitykind/"],
        "source_url": QUDT_RELEASE_URL,
        "archive_member": "vocab/quantitykinds/VOCAB_QUDT-QUANTITY-KINDS-ALL.ttl",
        "local_file": "qudt-quantitykinds.ttl",
        "format": "turtle",
        "typed_members_are_individuals": True,
    },
    "qudt-prefixes": {
        "title": "QUDT unit prefixes vocabulary",
        "profile": "SDK-pinned QUDT",
        "namespace_prefixes": ["http://qudt.org/vocab/prefix/"],
        "source_url": QUDT_RELEASE_URL,
        "archive_member": "vocab/prefixes/VOCAB_QUDT-PREFIXES.ttl",
        "local_file": "qudt-prefixes.ttl",
        "format": "turtle",
        "typed_members_are_individuals": True,
    },
    "sosa": {
        "title": "W3C Sensor, Observation, Sample, and Actuator (SOSA)",
        "profile": "SDK-pinned SOSA/SSN",
        "namespace_prefixes": ["http://www.w3.org/ns/sosa/"],
        "source_url": "https://www.w3.org/ns/sosa/",
        "local_file": "sosa.ttl",
        "format": "turtle",
        "accept": "text/turtle",
        # The W3C files carry no owl:versionIRI; pin the Recommendation.
        "version_info": "W3C Recommendation 2017-10-19 (https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/)",
    },
    "ssn": {
        "title": "W3C Semantic Sensor Network (SSN)",
        "profile": "SDK-pinned SOSA/SSN",
        "namespace_prefixes": ["http://www.w3.org/ns/ssn/"],
        "exclude_prefixes": ["http://www.w3.org/ns/ssn/systems/"],
        "source_url": "https://www.w3.org/ns/ssn/",
        "local_file": "ssn.ttl",
        "format": "turtle",
        "accept": "text/turtle",
        "version_info": "W3C Recommendation 2017-10-19 (https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/)",
    },
    "ssn-systems": {
        "title": "W3C SSN System Capabilities (SSN-System)",
        "profile": "SDK-pinned SOSA/SSN",
        "namespace_prefixes": ["http://www.w3.org/ns/ssn/systems/"],
        "source_url": "https://www.w3.org/ns/ssn/systems/",
        "local_file": "ssn-systems.ttl",
        "format": "turtle",
        "accept": "text/turtle",
        "version_info": "W3C Recommendation 2017-10-19 (https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/)",
    },
}


# CDO-Shapes conformance profiles (SHACL) published by the Cyber Domain
# Ontology project — vendored alongside the upper-ontology sources so
# profile conformance checks run offline:
#   case_validate --ontology-graph ontology/upper/shapes/sh-prov-o.ttl ...
SHAPES_SOURCES: dict[str, dict] = {
    "bfo": {"repo": "Cyber-Domain-Ontology/CDO-Shapes-BFO", "path": "shapes/sh-bfo.ttl"},
    "gufo": {"repo": "Cyber-Domain-Ontology/CDO-Shapes-gufo", "path": "shapes/sh-gufo.ttl"},
    "prov-o": {"repo": "Cyber-Domain-Ontology/CDO-Shapes-PROV-O", "path": "shapes/sh-prov-o.ttl"},
    "owl-time": {"repo": "Cyber-Domain-Ontology/CDO-Shapes-Time", "path": "shapes/sh-time.ttl"},
    "geosparql": {"repo": "Cyber-Domain-Ontology/CDO-Shapes-GeoSPARQL", "path": "shapes/sh-geo.ttl"},
    "foaf": {"repo": "Cyber-Domain-Ontology/CDO-Shapes-FOAF", "path": "shapes/sh-foaf.ttl"},
    "org": {"repo": "Cyber-Domain-Ontology/CDO-Shapes-ORG", "path": "shapes/sh-org.ttl"},
    "prof": {"repo": "Cyber-Domain-Ontology/CDO-Shapes-PROF", "path": "shapes/sh-prof.ttl"},
}


def _fetch(url: str, accept: str | None) -> bytes:
    request = urllib.request.Request(url, headers={"Accept": accept or "text/turtle, application/rdf+xml"})
    with urllib.request.urlopen(request, timeout=180) as response:
        return response.read()


_ARCHIVES: dict[str, bytes] = {}


def _fetch_source(spec: dict) -> bytes:
    """Download one pinned source, extracting it from a release archive if needed."""

    member = spec.get("archive_member")
    if not member:
        return _fetch(spec["source_url"], spec.get("accept"))
    url = spec["source_url"]
    if url not in _ARCHIVES:
        _ARCHIVES[url] = _fetch(url, "application/zip")
    with zipfile.ZipFile(io.BytesIO(_ARCHIVES[url])) as archive:
        return archive.read(member)


def _github_default_branch_sha(repo: str) -> str:
    """Resolve the current commit SHA of a repo's default branch."""

    data = json.loads(
        _fetch(f"https://api.github.com/repos/{repo}", "application/vnd.github+json")
    )
    branch = data.get("default_branch", "main")
    commit = json.loads(
        _fetch(
            f"https://api.github.com/repos/{repo}/commits/{branch}",
            "application/vnd.github+json",
        )
    )
    return commit["sha"]


def _extract_terms(
    graph,
    prefixes: tuple[str, ...],
    excludes: tuple[str, ...] = (),
    typed_members_are_individuals: bool = False,
) -> dict[str, list[str]]:
    """Categorize declared terms by RDF role within the target namespaces."""

    from rdflib import OWL, RDF, RDFS, URIRef

    classes: set[str] = set()
    properties: set[str] = set()
    individuals: set[str] = set()
    datatypes: set[str] = set()

    class_types = {OWL.Class, RDFS.Class}
    property_types = {
        OWL.ObjectProperty,
        OWL.DatatypeProperty,
        OWL.AnnotationProperty,
        OWL.FunctionalProperty,
        OWL.InverseFunctionalProperty,
        OWL.TransitiveProperty,
        OWL.SymmetricProperty,
        RDF.Property,
    }

    def in_scope(term) -> bool:
        return (
            isinstance(term, URIRef)
            and str(term).startswith(prefixes)
            and not (excludes and str(term).startswith(excludes))
        )

    for subject, rdf_type in graph.subject_objects(RDF.type):
        if not in_scope(subject):
            continue
        iri = str(subject)
        if rdf_type in class_types:
            classes.add(iri)
        elif rdf_type in property_types:
            properties.add(iri)
        elif rdf_type == RDFS.Datatype:
            datatypes.add(iri)
        elif rdf_type == OWL.NamedIndividual:
            individuals.add(iri)

    # Role inference for terms declared only structurally.
    for subject in graph.subjects(RDFS.subClassOf):
        if in_scope(subject):
            classes.add(str(subject))
    for pred in (RDFS.subPropertyOf, RDFS.domain, RDFS.range):
        for subject in graph.subjects(pred):
            if in_scope(subject) and str(subject) not in classes:
                properties.add(str(subject))
    for obj in graph.objects(None, RDFS.subClassOf):
        if in_scope(obj):
            classes.add(str(obj))
    for pred in (RDFS.domain, RDFS.range):
        for obj in graph.objects(None, pred):
            if in_scope(obj) and str(obj) not in properties:
                classes.add(str(obj))

    # Vocabulary members typed by an in-scope class (e.g. time:Friday a
    # time:DayOfWeek) count as individuals.
    # With typed_members_are_individuals, members typed by a class in another
    # namespace count too (e.g. unit:KiloM-PER-HR a qudt:Unit).
    for subject, rdf_type in graph.subject_objects(RDF.type):
        if not in_scope(subject):
            continue
        if in_scope(rdf_type) or (
            typed_members_are_individuals
            and isinstance(rdf_type, URIRef)
            and rdf_type not in class_types
            and rdf_type not in property_types
            and rdf_type not in (RDFS.Datatype, OWL.Ontology)
        ):
            iri = str(subject)
            if iri not in classes and iri not in properties:
                individuals.add(iri)

    properties -= classes  # punned terms count as classes for rdf:type use
    return {
        "classes": sorted(classes),
        "properties": sorted(properties),
        "individuals": sorted(individuals - classes - properties),
        "datatypes": sorted(datatypes),
    }


def _version_metadata(graph) -> dict[str, str]:
    from rdflib import OWL, RDF

    meta: dict[str, str] = {}
    for ontology in graph.subjects(RDF.type, OWL.Ontology):
        version_iri = graph.value(ontology, OWL.versionIRI)
        version_info = graph.value(ontology, OWL.versionInfo)
        if version_iri:
            meta["version_iri"] = str(version_iri)
        if version_info:
            meta["version_info"] = str(version_info)
        if meta:
            break
    return meta


def fetch_vendored_sources(
    target_dir: Path = VENDORED_SOURCE_DIR, only: set[str] | None = None
) -> None:
    """Download pinned upper ontologies into ``ontology/upper/``.

    Writes a ``provenance.json`` next to the files recording source URL,
    SHA-256, and fetch time for each so the vendored snapshot is auditable.
    ``only`` limits the refresh to those ontology keys and their shapes.
    """

    target_dir.mkdir(parents=True, exist_ok=True)
    provenance: dict[str, dict] = {}
    if VENDORED_PROVENANCE.is_file():
        provenance = json.loads(VENDORED_PROVENANCE.read_text(encoding="utf-8")).get("files", {})
    for key, spec in ONTOLOGY_SOURCES.items():
        if only and key not in only:
            continue
        data = _fetch_source(spec)
        (target_dir / spec["local_file"]).write_bytes(data)
        record = {
            "ontology": key,
            "source_url": spec["source_url"],
            "sha256": hashlib.sha256(data).hexdigest(),
            "fetched": datetime.now(timezone.utc).isoformat(),
        }
        if spec.get("archive_member"):
            record["archive_member"] = spec["archive_member"]
        provenance[spec["local_file"]] = record
        print(f"fetched {key} -> ontology/upper/{spec['local_file']} ({len(data)} bytes)")
    shapes_dir = target_dir / "shapes"
    shapes_dir.mkdir(parents=True, exist_ok=True)
    for key, spec in SHAPES_SOURCES.items():
        if only and key not in only:
            continue
        sha = _github_default_branch_sha(spec["repo"])
        raw_url = f"https://raw.githubusercontent.com/{spec['repo']}/{sha}/{spec['path']}"
        data = _fetch(raw_url, "text/turtle")
        local_name = Path(spec["path"]).name
        (shapes_dir / local_name).write_bytes(data)
        provenance[f"shapes/{local_name}"] = {
            "ontology": key,
            "source_repo": f"https://github.com/{spec['repo']}",
            "source_commit": sha,
            "sha256": hashlib.sha256(data).hexdigest(),
            "fetched": datetime.now(timezone.utc).isoformat(),
        }
        print(f"fetched CDO-Shapes {key} -> ontology/upper/shapes/{local_name} ({len(data)} bytes)")
    VENDORED_PROVENANCE.write_text(
        json.dumps(
            {
                "description": (
                    "Pinned upper-ontology source files and CDO-Shapes profiles "
                    "vendored for offline registry rebuilds and profile "
                    "conformance checks. Refresh with "
                    "build_upper_ontology_registry.py --fetch."
                ),
                "files": provenance,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def build_registry(source_dir: Path | None) -> dict:
    import rdflib

    ontologies: dict[str, dict] = {}
    for key, spec in ONTOLOGY_SOURCES.items():
        prefixes = tuple(spec["namespace_prefixes"])
        graph = rdflib.Graph()
        if source_dir is not None:
            data = (source_dir / spec["local_file"]).read_bytes()
        else:
            data = _fetch_source(spec)
        graph.parse(data=data, format=spec["format"])
        terms = _extract_terms(
            graph,
            prefixes,
            tuple(spec.get("exclude_prefixes", ())),
            bool(spec.get("typed_members_are_individuals")),
        )
        version_meta = _version_metadata(graph)
        # Manual pin for ontologies whose RDF omits a usable version
        # (fail-closed provenance check requires version_iri or version_info).
        if "version_info" in spec:
            version_meta["version_info"] = spec["version_info"]
        entry = {
            "title": spec["title"],
            "profile": spec["profile"],
            "namespace_prefixes": spec["namespace_prefixes"],
            "source_url": spec["source_url"],
            **({"archive_member": spec["archive_member"]} if spec.get("archive_member") else {}),
            **version_meta,
            "term_counts": {k: len(v) for k, v in terms.items()},
            **terms,
        }
        ontologies[key] = entry
        print(
            f"{key}: {entry['term_counts']['classes']} classes, "
            f"{entry['term_counts']['properties']} properties, "
            f"{entry['term_counts']['individuals']} individuals, "
            f"{entry['term_counts']['datatypes']} datatypes"
        )

    return {
        "registry_version": "1.0",
        "generated": datetime.now(timezone.utc).isoformat(),
        "generator": "mcp_server/tools/build_upper_ontology_registry.py",
        "description": (
            "Exact declared terms of upper/external ontologies that UCO "
            "maintains CDO-Shapes profiles for. Strict concept coverage "
            "accepts only these terms inside the profiled namespaces."
        ),
        "ontologies": ontologies,
    }


def build_qudt_unit_index(source_dir: Path) -> dict:
    """Compact lookup table of QUDT units for the ``lookup_qudt_units`` tool."""

    import rdflib
    from rdflib import RDF, RDFS, Literal, Namespace

    qudt = Namespace("http://qudt.org/schema/qudt/")
    graph = rdflib.Graph()
    graph.parse(source_dir / ONTOLOGY_SOURCES["qudt-units"]["local_file"], format="turtle")
    unit_prefix = "http://qudt.org/vocab/unit/"
    quantitykind_prefix = "http://qudt.org/vocab/quantitykind/"

    def texts(subject, predicate, english_only: bool = False) -> list[str]:
        values = []
        for obj in graph.objects(subject, predicate):
            if not isinstance(obj, Literal):
                continue
            if english_only and obj.language not in (None, "en", "en-us"):
                continue
            values.append(str(obj))
        return sorted(set(values))

    units = []
    for unit in sorted(set(graph.subjects(RDF.type, qudt.Unit))):
        iri = str(unit)
        if not iri.startswith(unit_prefix):
            continue
        deprecated = any(str(v).lower() == "true" for v in graph.objects(unit, rdflib.OWL.deprecated))
        multiplier = graph.value(unit, qudt.conversionMultiplier)
        units.append(
            {
                "id": "unit:" + iri[len(unit_prefix):],
                "labels": texts(unit, RDFS.label, english_only=True),
                "symbol": (texts(unit, qudt.symbol) or [None])[0],
                "alt_symbols": texts(unit, qudt.altSymbol),
                "ucum": texts(unit, qudt.ucumCode),
                "quantity_kinds": sorted(
                    "quantitykind:" + str(qk)[len(quantitykind_prefix):]
                    for qk in graph.objects(unit, qudt.hasQuantityKind)
                    if str(qk).startswith(quantitykind_prefix)
                ),
                "conversion_multiplier": str(multiplier) if multiplier is not None else None,
                **({"deprecated": True} if deprecated else {}),
            }
        )
    return {
        "generator": "mcp_server/tools/build_upper_ontology_registry.py",
        "qudt_version": QUDT_VERSION,
        "source_url": QUDT_RELEASE_URL,
        "prefixes": {"unit": unit_prefix, "quantitykind": quantitykind_prefix},
        "units": units,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--source-dir",
        type=Path,
        default=None,
        help=(
            "Read ontology files from this directory. Default: the vendored "
            f"snapshot at {VENDORED_SOURCE_DIR} when present (offline rebuild)."
        ),
    )
    parser.add_argument(
        "--fetch",
        action="store_true",
        help=(
            "Refresh the vendored snapshot in ontology/upper/ from upstream "
            "before rebuilding the registry (requires network access)."
        ),
    )
    parser.add_argument(
        "--only",
        default="",
        help=(
            "With --fetch, refresh only these comma-separated ontology keys "
            f"(choices: {', '.join(ONTOLOGY_SOURCES)})."
        ),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=REGISTRY_PATH,
        help=f"Registry output path (default: {REGISTRY_PATH})",
    )
    args = parser.parse_args()

    source_dir = args.source_dir
    only = {key.strip() for key in args.only.split(",") if key.strip()}
    unknown = only - set(ONTOLOGY_SOURCES)
    if unknown:
        print(f"error: unknown ontology keys: {', '.join(sorted(unknown))}", file=sys.stderr)
        return 1
    if args.fetch:
        fetch_vendored_sources(only=only or None)
        source_dir = source_dir or VENDORED_SOURCE_DIR
    elif source_dir is None:
        if not VENDORED_SOURCE_DIR.is_dir():
            print(
                f"error: no vendored snapshot at {VENDORED_SOURCE_DIR}; run with "
                "--fetch (network) or pass --source-dir",
                file=sys.stderr,
            )
            return 1
        source_dir = VENDORED_SOURCE_DIR

    registry = build_registry(source_dir)
    args.output.write_text(json.dumps(registry, indent=2, sort_keys=False) + "\n", encoding="utf-8")
    total = sum(
        sum(entry["term_counts"].values()) for entry in registry["ontologies"].values()
    )
    print(f"Wrote {args.output} ({total} terms across {len(registry['ontologies'])} ontologies).")
    unit_index = build_qudt_unit_index(source_dir)
    QUDT_UNIT_INDEX_PATH.write_text(
        json.dumps(unit_index, indent=1, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"Wrote {QUDT_UNIT_INDEX_PATH} ({len(unit_index['units'])} QUDT units).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
