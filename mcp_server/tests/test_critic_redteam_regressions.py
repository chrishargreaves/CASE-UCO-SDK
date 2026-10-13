"""Regressions for critic issues #38, #40, #41, #44, #45, #46, #47, #48."""

from __future__ import annotations

import json
import math
from pathlib import Path

import pytest

import graph_validator
from critic import CriticArtifactRequest, analyze_artifact
from critic.canonical import load_canonical_graph
from critic.deterministic import _validation_findings
from critic.graph_heuristics import run_graph_heuristics
from critic.graph_integrity import analyze_graph_integrity
from critic.models import ValidationSummary
from critic.response_parser import CriticResponseError, parse_critic_model_response
from critic.serializer_python import SerializerTooComplexError, analyze_python_serializer
from critic.sessions import (
    CriticSessionError,
    _atomic_write_json,
    finalize_critic_review,
    start_critic_review,
    submit_critic_revision,
)

CTX = {
    "kb": "http://example.org/kb/",
    "uco-core": "https://ontology.unifiedcyberontology.org/uco/core/",
    "uco-action": "https://ontology.unifiedcyberontology.org/uco/action/",
    "uco-observable": "https://ontology.unifiedcyberontology.org/uco/observable/",
    "uco-identity": "https://ontology.unifiedcyberontology.org/uco/identity/",
    "uco-types": "https://ontology.unifiedcyberontology.org/uco/types/",
    "uco-marking": "https://ontology.unifiedcyberontology.org/uco/marking/",
    "case-investigation": "https://ontology.caseontology.org/case/investigation/",
}


def _view(tmp_path: Path, graph: list[dict]):
    path = tmp_path / "g.jsonld"
    path.write_text(json.dumps({"@context": CTX, "@graph": graph}), encoding="utf-8")
    return load_canonical_graph(path)


def _rule_ids(findings) -> set[str]:
    return {f.rule_id for f in findings}


def test_bare_reference_is_dangling(tmp_path):
    view = _view(
        tmp_path,
        [
            {
                "@id": "urn:example:a",
                "@type": "uco-core:Grouping",
                "uco-core:object": [{"@id": "urn:example:MISSING"}],
            }
        ],
    )
    assert "urn:example:MISSING" not in view.nodes
    _view_out, findings, _ = analyze_graph_integrity(
        tmp_path / "g.jsonld", artifact_hash="x"
    )
    dangling = [f for f in findings if f.rule_id == "CRIT-G-DANGLING-REF"]
    assert [f.target.node_id for f in dangling] == ["urn:example:MISSING"]


def test_expanded_kb_reference_is_dangling(tmp_path):
    view = _view(
        tmp_path,
        [
            {
                "@id": "kb:a",
                "@type": "uco-core:Grouping",
                "uco-core:object": [{"@id": "kb:MISSING"}],
            }
        ],
    )
    _view_out, findings, _ = analyze_graph_integrity(
        tmp_path / "g.jsonld", artifact_hash="x"
    )
    assert "http://example.org/kb/MISSING" in {
        f.target.node_id for f in findings if f.rule_id == "CRIT-G-DANGLING-REF"
    }


@pytest.mark.parametrize(
    "name",
    ["Add ledger entry", "Embedded thumbnail image", "Holiday photo IMG_0042.raw"],
)
def test_raster_picture_without_forensic_image_tokens(tmp_path, name):
    view = _view(
        tmp_path,
        [{"@id": "kb:pic", "@type": "uco-observable:RasterPicture", "uco-core:name": name}],
    )
    findings, _ = run_graph_heuristics(view, artifact_hash="x")
    assert "CRIT-H-IMAGE-CONTAINER-MISMATCH" not in _rule_ids(findings)


@pytest.mark.parametrize("name", ["laptop.E01", "Disk image of laptop", "sdcard.dd"])
def test_raster_picture_with_forensic_image_tokens(tmp_path, name):
    view = _view(
        tmp_path,
        [{"@id": "kb:pic", "@type": "uco-observable:RasterPicture", "uco-core:name": name}],
    )
    findings, _ = run_graph_heuristics(view, artifact_hash="x")
    assert "CRIT-H-IMAGE-CONTAINER-MISMATCH" in _rule_ids(findings)


@pytest.mark.parametrize(
    ("performer_name", "flagged"),
    [
        ("Radio Operator Lee", False),
        ("Apterix Corp", False),
        ("APT28", True),
        ("Unknown threat actor", True),
    ],
)
def test_role_contradiction_needs_threat_actor_wording(tmp_path, performer_name, flagged):
    view = _view(
        tmp_path,
        [
            {
                "@id": "kb:act",
                "@type": "uco-action:Action",
                "uco-core:name": "User opens attachment",
                "uco-action:performer": {"@id": "kb:who"},
            },
            {"@id": "kb:who", "@type": "uco-identity:Identity", "uco-core:name": performer_name},
        ],
    )
    findings, _ = run_graph_heuristics(view, artifact_hash="x")
    assert ("CRIT-H-ACTION-ROLE-CONTRADICTION" in _rule_ids(findings)) is flagged


@pytest.mark.parametrize(
    ("action_name", "flagged"),
    [
        ("Examine disk image of the seized laptop", False),
        ("Analyze image for steganography", False),
        ("Image the seized laptop", True),
        ("Acquire the seized laptop", True),
        ("Export chat logs from the phone", True),
        ("COC-004 — Discord logical export custody (ART-004)", False),
        ("Transfer of the extracted image to the lab", False),
    ],
)
def test_acquisition_inversion_needs_acquisition_verb(tmp_path, action_name, flagged):
    view = _view(
        tmp_path,
        [
            {
                "@id": "kb:act",
                "@type": "case-investigation:InvestigativeAction",
                "uco-core:name": action_name,
                "uco-action:object": {"@id": "kb:img"},
            },
            {"@id": "kb:img", "@type": "uco-observable:File"},
        ],
    )
    findings, _ = run_graph_heuristics(view, artifact_hash="x")
    assert ("CRIT-H-ACQ-INPUT-RESULT-INVERSION" in _rule_ids(findings)) is flagged


def test_observable_relationship_counts_as_relationship(tmp_path):
    view = _view(
        tmp_path,
        [
            {
                "@id": "kb:inv",
                "@type": "case-investigation:Investigation",
                "uco-core:object": [{"@id": "kb:a"}],
            },
            {"@id": "kb:a", "@type": "uco-observable:File"},
            {"@id": "kb:b", "@type": "uco-observable:File"},
            {
                "@id": "kb:rel",
                "@type": "uco-observable:ObservableRelationship",
                "uco-core:source": {"@id": "kb:b"},
                "uco-core:target": {"@id": "kb:a"},
                "uco-core:kindOfRelationship": "Contained_Within",
                "uco-core:isDirectional": True,
            },
        ],
    )
    assert view.get("http://example.org/kb/rel").is_a(
        "https://ontology.unifiedcyberontology.org/uco/core/Relationship"
    )
    findings, _ = run_graph_heuristics(view, artifact_hash="x")
    orphans = {f.target.node_id for f in findings if f.rule_id == "CRIT-H-ORPHAN-TOP-LEVEL"}
    assert "http://example.org/kb/rel" not in orphans
    assert "http://example.org/kb/b" not in orphans


def test_orphan_walk_follows_facets_markings_and_creators(tmp_path):
    view = _view(
        tmp_path,
        [
            {
                "@id": "kb:inv",
                "@type": "case-investigation:Investigation",
                "uco-core:object": [{"@id": "kb:msg"}],
            },
            {
                "@id": "kb:msg",
                "@type": "uco-observable:ObservableObject",
                "uco-core:createdBy": {"@id": "kb:author"},
                "uco-core:objectMarking": [{"@id": "kb:marking"}],
                "uco-core:hasFacet": [
                    {
                        "@type": "uco-observable:EmailMessageFacet",
                        "uco-observable:from": {"@id": "kb:sender"},
                    },
                    {
                        "@type": "uco-observable:ContentDataFacet",
                        "uco-observable:hash": [{"@id": "kb:hash"}],
                    },
                ],
            },
            {"@id": "kb:author", "@type": "uco-identity:Identity"},
            {"@id": "kb:marking", "@type": "uco-marking:MarkingDefinition"},
            {"@id": "kb:sender", "@type": "uco-observable:ObservableObject"},
            {
                "@id": "kb:hash",
                "@type": "uco-types:Hash",
                "uco-types:hashMethod": "SHA256",
                "uco-types:hashValue": "00" * 32,
            },
            {"@id": "kb:stray", "@type": "uco-observable:ObservableObject"},
        ],
    )
    findings, _ = run_graph_heuristics(view, artifact_hash="x")
    orphans = {f.target.node_id for f in findings if f.rule_id == "CRIT-H-ORPHAN-TOP-LEVEL"}
    assert orphans == {"http://example.org/kb/stray"}


def test_profile_not_selected_names_the_iri():
    validation = ValidationSummary(
        conforms=True,
        verification_status="complete",
        profile_not_selected=[
            {
                "iri": "http://www.w3.org/2006/time#Instant",
                "required_profile": "time",
                "used_as": "class",
                "selected_profiles": [],
            },
            {"term": "http://www.w3.org/2006/time#inXSDDateTimeStamp"},
        ],
    )
    node_ids = [
        f.target.node_id
        for f in _validation_findings(validation)
        if f.rule_id == "CRIT-V-PROFILE-NOT-SELECTED"
    ]
    assert node_ids == [
        "http://www.w3.org/2006/time#Instant",
        "http://www.w3.org/2006/time#inXSDDateTimeStamp",
    ]


@pytest.mark.parametrize(
    "source",
    ["x = a" + ".b" * 20000 + "\n", "x = " + "+".join(["1"] * 20000) + "\n"],
    ids=["attribute-chain", "binop-chain"],
)
def test_deep_serializer_ast_is_typed_error(source):
    with pytest.raises(SerializerTooComplexError):
        analyze_python_serializer(Path("/tmp/deep.py"), source, artifact_hash="ab" * 32)


def test_oversized_serializer_is_not_read(tmp_path, monkeypatch):
    graph = tmp_path / "g.jsonld"
    graph.write_text(
        json.dumps({"@context": CTX, "@graph": [{"@id": "kb:a", "@type": "uco-core:Grouping"}]}),
        encoding="utf-8",
    )
    serializer = tmp_path / "big.py"
    serializer.write_text("x = 1\n" * 50000, encoding="utf-8")
    monkeypatch.setenv("CASE_UCO_MCP_READ_ROOTS", str(tmp_path))
    monkeypatch.setattr(graph_validator, "validator_available", lambda: False)

    original = Path.read_bytes

    def guarded(self: Path) -> bytes:
        assert self.name != "big.py", "oversized serializer was read in full"
        return original(self)

    monkeypatch.setattr(Path, "read_bytes", guarded)
    review = analyze_artifact(
        CriticArtifactRequest(
            graph_path=str(graph),
            serializer_path=str(serializer),
            critic_scope="both",
        )
    )
    assert "critic_serializer_too_large" in review.errors


def _response(confidence: float, score: object = None) -> dict:
    payload = {
        "schema_version": "1.2.0",
        "graph_sha256": "a" * 64,
        "prompt_package_hash": "b" * 64,
        "findings": [
            {
                "severity": "low",
                "category": "investigation_structure",
                "confidence": confidence,
                "claim_type": "missing_object_link",
                "target": {"node_id": "urn:example:x"},
                "evidence": ["e"],
                "rationale": "r",
                "recommended_change": "c",
                "verification_method": "v",
            }
        ],
        "finding_assessments": [],
        "scorecard": {},
    }
    if score is not None:
        payload["findings"][0]["confidence"] = 0.5
        payload["scorecard"] = {"source_fidelity": {"score": score, "evidence": []}}
    return payload


@pytest.mark.parametrize(
    "payload",
    [_response(math.nan), _response(math.inf), _response(0.5, score=math.nan)],
    ids=["nan-confidence", "inf-confidence", "nan-score"],
)
def test_non_finite_numbers_rejected(payload):
    with pytest.raises(CriticResponseError) as exc:
        parse_critic_model_response(
            payload,
            expected_graph_sha256="a" * 64,
            expected_prompt_package_hash="b" * 64,
        )
    # Infinity is already outside the schema's 0..1 confidence range.
    assert exc.value.code in {
        "critic_response_non_finite_number",
        "critic_response_schema_mismatch",
    }
    if math.isnan(payload["findings"][0]["confidence"]) or payload["scorecard"]:
        assert exc.value.code == "critic_response_non_finite_number"


def test_session_json_refuses_nan(tmp_path):
    with pytest.raises(CriticSessionError) as exc:
        _atomic_write_json(tmp_path / "x.json", {"confidence": math.nan})
    assert exc.value.code == "critic_session_non_finite_number"
    assert not (tmp_path / "x.json").exists()


@pytest.fixture
def split_roots(tmp_path, monkeypatch):
    read = tmp_path / "read"
    write = tmp_path / "write"
    read.mkdir()
    write.mkdir()
    monkeypatch.setenv("CASE_UCO_MCP_READ_ROOTS", str(read))
    monkeypatch.setenv("CASE_UCO_MCP_WRITE_ROOTS", str(write))
    monkeypatch.setenv("CASE_UCO_CRITIC_SESSION_ROOT", str(write / "critic-sessions"))
    monkeypatch.setenv("CASE_UCO_MCP_ALLOW_OVERWRITE", "1")
    monkeypatch.setattr(graph_validator, "validator_available", lambda: True)
    monkeypatch.setattr(
        graph_validator,
        "validate_graph_file",
        lambda *a, **k: graph_validator.GraphValidationReport(
            conforms=True,
            warning_count=0,
            violation_count=0,
            exit_code=0,
            validator_name="case_validate",
            safe_summary="conforms",
            verification_status="complete",
        ),
    )
    return read, write


def test_failed_start_leaves_no_session_directory(split_roots):
    read, write = split_roots
    with pytest.raises(CriticSessionError):
        start_critic_review(
            graph_path=str(read / "missing.jsonld"),
            critic_scope="graph",
            model_policy="disabled",
        )
    sessions = write / "critic-sessions"
    assert not sessions.exists() or not any(sessions.glob("critsess-*"))


def test_write_root_source_can_be_finalized(split_roots):
    read, write = split_roots
    fixtures = Path(__file__).resolve().parent / "fixtures" / "critic"
    graph = read / "gold.jsonld"
    graph.write_text(
        (fixtures / "gold-charged-with.jsonld").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    evidence = write / "evidence.txt"
    evidence.write_text("evidence\n", encoding="utf-8")
    started = start_critic_review(
        graph_path=str(graph),
        source_paths=[str(evidence)],
        critic_scope="graph",
        model_policy="disabled",
    )
    sid = started["session_id"]
    graph.write_text(graph.read_text(encoding="utf-8") + "\n", encoding="utf-8")
    submit_critic_revision(sid, graph_path=str(graph), change_summary="confirm")
    try:
        finalize_critic_review(sid)
    except CriticSessionError as exc:
        assert exc.code != "critic_session_artifact_path_denied", str(exc)

