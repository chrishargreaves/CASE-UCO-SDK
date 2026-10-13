"""ATT&CK and ATLAS technique catalogs: sync tools, committed catalogs, index."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest
import rdflib
from rdflib.namespace import OWL, RDF, RDFS

MCP_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = MCP_DIR.parent
sys.path.insert(0, str(MCP_DIR))
sys.path.insert(0, str(MCP_DIR / "tools"))

import adversary_technique_index  # noqa: E402
import sync_atlas_catalog  # noqa: E402
import sync_attack_catalog  # noqa: E402

ACTION = rdflib.Namespace("https://ontology.unifiedcyberontology.org/uco/action/")
DCTERMS = rdflib.Namespace("http://purl.org/dc/terms/")
ATTACK = rdflib.Namespace("https://attack.mitre.org/techniques/")
ATLAS = rdflib.Namespace("https://atlas.mitre.org/techniques/")


def _pattern(stix_id, ext_id, name, *, kill_chain="mitre-attack", phases=(), **extra):
    obj = {
        "type": "attack-pattern",
        "id": stix_id,
        "name": name,
        "description": f"{name} description. (Citation: Somebody 2020) Second sentence.",
        "modified": "2026-05-12T00:00:00.000Z",
        "external_references": [
            {
                "source_name": "mitre-attack",
                "external_id": ext_id,
                "url": f"https://attack.mitre.org/techniques/{ext_id.replace('.', '/')}",
            }
        ],
        "kill_chain_phases": [
            {"kill_chain_name": kill_chain, "phase_name": p} for p in phases
        ],
    }
    obj.update(extra)
    return obj


def _bundle(version, objects, tactics):
    return {
        "type": "bundle",
        "objects": [
            {"type": "x-mitre-collection", "x_mitre_version": version, "modified": "2026-08-05T00:00:00Z"},
            *[
                {
                    "type": "x-mitre-tactic",
                    "id": f"x-mitre-tactic--{tid}",
                    "name": name,
                    "x_mitre_shortname": short,
                    "description": f"The adversary is trying to {short}.",
                    "external_references": [
                        {"source_name": "mitre-attack", "external_id": tid,
                         "url": f"https://attack.mitre.org/tactics/{tid}"}
                    ],
                }
                for tid, name, short in tactics
            ],
            *objects,
        ],
    }


@pytest.fixture()
def attack_bundles():
    enterprise = _bundle(
        "19.2",
        [
            _pattern("attack-pattern--1", "T1027", "Obfuscated Files or Information",
                     phases=["stealth"], x_mitre_platforms=["Windows", "Linux"]),
            _pattern("attack-pattern--2", "T1027.002", "Software Packing",
                     phases=["stealth"], x_mitre_is_subtechnique=True,
                     x_mitre_platforms=["Windows"]),
            _pattern("attack-pattern--3", "T1086", "PowerShell", phases=["execution"],
                     revoked=True),
            _pattern("attack-pattern--4", "T1059.001", "PowerShell", phases=["execution"],
                     x_mitre_is_subtechnique=True),
            _pattern("attack-pattern--5", "T1059", "Command and Scripting Interpreter",
                     phases=["execution"]),
            _pattern("attack-pattern--6", "T1050", "Old Technique", x_mitre_deprecated=True),
            {"type": "relationship", "relationship_type": "subtechnique-of",
             "source_ref": "attack-pattern--2", "target_ref": "attack-pattern--1"},
            {"type": "relationship", "relationship_type": "subtechnique-of",
             "source_ref": "attack-pattern--4", "target_ref": "attack-pattern--5"},
            {"type": "relationship", "relationship_type": "revoked-by",
             "source_ref": "attack-pattern--3", "target_ref": "attack-pattern--4"},
        ],
        [("TA0005", "Stealth", "stealth"), ("TA0002", "Execution", "execution")],
    )
    ics = _bundle(
        "19.2",
        [
            _pattern("attack-pattern--9", "T0800", "Activate Firmware Update Mode",
                     kill_chain="mitre-ics-attack", phases=["inhibit-response-function"],
                     x_mitre_platforms=["None"]),
        ],
        [("TA0107", "Inhibit Response Function", "inhibit-response-function")],
    )
    return {
        "enterprise": (enterprise, {"source": "fixture", "sha256": "0" * 64}),
        "ics": (ics, {"source": "fixture", "sha256": "1" * 64}),
    }


def _attack_graph(bundles) -> rdflib.Graph:
    techniques, tactics = sync_attack_catalog.build_catalog(bundles)
    ttl = sync_attack_catalog.render_catalog(
        techniques, tactics, attack_version="19.2", bundles=bundles
    )
    graph = rdflib.Graph()
    graph.parse(data=ttl, format="turtle")
    return graph


class TestAttackSync:
    def test_every_technique_is_a_punned_technique_class(self, attack_bundles):
        g = _attack_graph(attack_bundles)
        ids = {str(o) for o in g.objects(None, ACTION.techniqueID)}
        assert ids == {"T1027", "T1027.002", "T1086", "T1059", "T1059.001", "T1050", "T0800"}
        for tid in ids:
            node = ATTACK[tid]
            assert (node, RDF.type, OWL.Class) in g
            assert (node, RDF.type, ACTION.Technique) in g

    def test_subtechnique_specializes_parent_not_action(self, attack_bundles):
        g = _attack_graph(attack_bundles)
        assert set(g.objects(ATTACK["T1027.002"], RDFS.subClassOf)) == {ATTACK.T1027}
        assert set(g.objects(ATTACK.T1027, RDFS.subClassOf)) == {ACTION.Action}
        label = str(g.value(ATTACK["T1027.002"], RDFS.label))
        assert label == "Obfuscated Files or Information: Software Packing"

    def test_tactics_and_platforms_are_annotations(self, attack_bundles):
        g = _attack_graph(attack_bundles)
        assert (DCTERMS.subject, RDF.type, OWL.AnnotationProperty) in g
        tactic = rdflib.URIRef("https://attack.mitre.org/tactics/TA0005")
        assert (ATTACK.T1027, DCTERMS.subject, tactic) in g
        assert {str(o) for o in g.objects(ATTACK.T1027, DCTERMS.coverage)} == {"Linux", "Windows"}
        assert list(g.objects(ATTACK.T0800, DCTERMS.coverage)) == []
        ics = rdflib.URIRef("https://attack.mitre.org/matrices/ics/")
        assert (ATTACK.T0800, DCTERMS.isPartOf, ics) in g

    def test_revoked_and_deprecated_are_kept_and_marked(self, attack_bundles):
        g = _attack_graph(attack_bundles)
        assert (ATTACK.T1086, OWL.deprecated, rdflib.Literal(True)) in g
        assert (ATTACK.T1086, DCTERMS.isReplacedBy, ATTACK["T1059.001"]) in g
        assert (ATTACK.T1050, OWL.deprecated, rdflib.Literal(True)) in g
        assert (ATTACK.T1027, OWL.deprecated, None) not in g

    def test_description_is_cleaned(self, attack_bundles):
        g = _attack_graph(attack_bundles)
        comment = str(g.value(ATTACK.T1027, RDFS.comment))
        assert "Citation" not in comment
        assert comment.startswith("Obfuscated Files or Information description.")

    def test_bundle_version_mismatch_is_rejected(self, tmp_path):
        bundle = _bundle("19.1", [], [])
        (tmp_path / "enterprise-attack-19.2.json").write_text(json.dumps(bundle))
        with pytest.raises(SystemExit):
            sync_attack_catalog.load_bundles("19.2", tmp_path, ["enterprise"])


@pytest.fixture()
def atlas_data():
    return {
        "format-version": "6.0.0",
        "collection": {"version": "2026.09", "modified-date": "2026-09-15"},
        "tactics": {
            "AML.TA0005": {"name": "Execution", "description": "Run code.",
                           "attack-reference": {"id": "TA0002"}},
        },
        "techniques": {
            "AML.T0051": {"name": "LLM Prompt Injection", "description": "Craft prompts.",
                          "platforms": ["Generative AI"], "maturity": "Realized",
                          "modified-date": "2026-05-27"},
            "AML.T0051.000": {"name": "Direct", "description": "Inject directly.",
                              "platforms": ["Generative AI"], "maturity": "Realized"},
            "AML.T0000": {"name": "Search Open Technical Databases", "description": "Search.",
                          "platforms": ["Enterprise"], "maturity": "Realized",
                          "attack-reference": {"id": "T1596",
                                               "url": "https://attack.mitre.org/techniques/T1596/"}},
        },
        "relationships": {
            "AML.T0051": {"achieves": [{"target": "AML.TA0005"}]},
            "AML.T0051.000": {"achieves": [{"target": "AML.TA0005"}],
                              "specializes": [{"target": "AML.T0051"}]},
        },
    }


class TestAtlasSync:
    def _graph(self, data) -> rdflib.Graph:
        techniques, tactics = sync_atlas_catalog.build_catalog(data)
        ttl = sync_atlas_catalog.render_catalog(
            techniques, tactics, release="2026.09",
            provenance={"source": "fixture", "sha256": "0" * 64}, data=data,
        )
        g = rdflib.Graph()
        g.parse(data=ttl, format="turtle")
        return g

    def test_atlas_techniques_use_the_uco_metaclass(self, atlas_data):
        g = self._graph(atlas_data)
        for tid in ("AML.T0051", "AML.T0051.000", "AML.T0000"):
            assert (ATLAS[tid], RDF.type, ACTION.Technique) in g
            assert (ATLAS[tid], ACTION.techniqueID, rdflib.Literal(tid)) in g
        assert set(g.objects(ATLAS["AML.T0051.000"], RDFS.subClassOf)) == {ATLAS["AML.T0051"]}
        assert str(g.value(ATLAS["AML.T0051.000"], RDFS.label)) == "LLM Prompt Injection: Direct"

    def test_attack_links_are_see_also_not_imports(self, atlas_data):
        g = self._graph(atlas_data)
        assert (ATLAS["AML.T0000"], RDFS.seeAlso, ATTACK.T1596) in g
        assert (ATTACK.T1596, None, None) not in g
        assert (None, OWL.imports, None) not in g

    def test_unsupported_format_is_rejected(self, tmp_path):
        path = tmp_path / "ATLAS.yaml"
        path.write_text("format-version: 5.6.0\ntechniques: {}\n")
        with pytest.raises(SystemExit):
            sync_atlas_catalog.load_atlas("2026.09", path)


def _committed(ext: str, filename: str) -> tuple[rdflib.Graph, dict]:
    ext_dir = PROJECT_ROOT / "extensions" / ext
    graph = rdflib.Graph()
    graph.parse(str(ext_dir / filename), format="turtle")
    manifest = json.loads((ext_dir / "manifest.json").read_text(encoding="utf-8"))
    return graph, manifest


@pytest.mark.parametrize(
    ("ext", "filename"),
    [
        ("attack-technique", "mitre-attack-catalog.ttl"),
        ("atlas-technique", "mitre-atlas-catalog.ttl"),
    ],
)
def test_committed_catalog_is_complete_and_well_formed(ext, filename):
    g, manifest = _committed(ext, filename)
    techniques = set(g.subjects(RDF.type, ACTION.Technique))
    assert len(techniques) == manifest["provenance"]["technique_count"]
    assert manifest["owl_files"] == [filename]
    assert not manifest.get("depends_on")
    for node in techniques:
        assert (node, RDF.type, OWL.Class) in g, node
        assert g.value(node, ACTION.techniqueID) is not None, node
        assert g.value(node, RDFS.label) is not None, node
        assert g.value(node, RDFS.comment) is not None, node
        parents = set(g.objects(node, RDFS.subClassOf))
        assert len(parents) == 1, node
        parent = next(iter(parents))
        assert parent == ACTION.Action or parent in techniques, (node, parent)
    subs = sum(1 for n in techniques if g.value(n, RDFS.subClassOf) != ACTION.Action)
    assert subs == manifest["provenance"]["subtechnique_count"]


def test_attack_catalog_covers_all_three_domains():
    g, manifest = _committed("attack-technique", "mitre-attack-catalog.ttl")
    assert manifest["provenance"]["attack_version"] == "19.2"
    assert set(manifest["provenance"]["domains"]) == {"enterprise", "mobile", "ics"}
    matrices = {str(o) for o in g.objects(None, DCTERMS.isPartOf)}
    for domain in ("enterprise", "mobile", "ics"):
        assert f"https://attack.mitre.org/matrices/{domain}/" in matrices
    for path in ("attack-technique.ttl", "attack-technique-shapes.ttl"):
        assert not (PROJECT_ROOT / "extensions/attack-technique" / path).exists(), (
            "UCO 1.5.0 ships the Technique metaclass; the local copy must stay retired"
        )


class TestIndex:
    def test_search_spans_both_catalogs(self):
        result = adversary_technique_index.search("prompt injection")
        assert result["results"][0]["id"] == "AML.T0051"
        assert set(result["catalog_versions"]) == {"MITRE ATT&CK", "MITRE ATLAS"}
        assert "evidence" in result["evidence_gate"]

    def test_exact_id_and_catalog_filter(self):
        result = adversary_technique_index.search("T1059.001", catalog="ATT&CK")
        assert result["results"][0]["id"] == "T1059.001"
        assert all(r["catalog"] == "MITRE ATT&CK" for r in result["results"])
        with pytest.raises(ValueError):
            adversary_technique_index.search("x", catalog="engage")

    def test_deprecated_hidden_unless_requested(self):
        default = adversary_technique_index.search("PowerShell", catalog="attack", limit=50)
        assert "T1086" not in {r["id"] for r in default["results"]}
        exact = adversary_technique_index.search("T1086")
        assert exact["results"][0]["deprecated"] is True

    def test_details_gives_hierarchy_replacement_and_guidance(self):
        revoked = adversary_technique_index.details("T1086")
        assert [r["id"] for r in revoked["replaced_by"]] == ["T1059.001"]
        assert "deprecation" in revoked["modeling_guidance"]
        parent = adversary_technique_index.details("T1027")
        assert "T1027.002" in {s["id"] for s in parent["subtechniques"]}
        sub = adversary_technique_index.details("T1027.002")
        assert sub["parent"]["id"] == "T1027"
        atlas = adversary_technique_index.details("AML.T0051")
        guidance = atlas["modeling_guidance"]
        assert guidance["validate_with"] == {"extensions": ["atlas-technique"]}
        assert atlas["iri"] in guidance["example_jsonld"]["@type"]
        assert (PROJECT_ROOT / guidance["recipe"]).is_file()

    def test_unknown_id_raises_key_error(self):
        with pytest.raises(KeyError):
            adversary_technique_index.details("T9999")
