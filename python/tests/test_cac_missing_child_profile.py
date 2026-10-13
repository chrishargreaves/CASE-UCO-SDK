"""Named CAC validation subset ``cac:missing-child`` (issue #18)."""

from __future__ import annotations

from pathlib import Path

import pytest

from case_uco.validation import (
    DEFAULT_BUILT_VERSION,
    parse_extension_token,
    report_to_dict,
    validate_graph_file,
    validator_available,
)
from case_uco.validation.graph import load_extension_ontology_paths

ROOT = Path(__file__).resolve().parents[2]
T0 = ROOT / "examples/cac/t0-missing-child.jsonld"
INVENTED = ROOT / "examples/cac/t0-missing-child-invented-term.jsonld"
ABDUCTION_IRI = "https://cacontology.projectvic.org/abduction#StrangerAbductionInvestigation"
CASE_PHASE_IRI = "https://cacontology.projectvic.org/case-management#CaseInitiationPhase"
URGENCY_IRI = "https://cacontology.projectvic.org/temporal#urgencyLevel"
INVENTED_IRI = "https://cacontology.projectvic.org#InventedMediaAuthScore"


def test_parse_extension_token_named_subset():
    assert parse_extension_token("cac") == ("cac", "subset")
    assert parse_extension_token("cac:full") == ("cac", "full")
    assert parse_extension_token("cac:missing-child") == ("cac", "missing-child")
    with pytest.raises(ValueError, match="extension_unknown"):
        parse_extension_token("cac:")


def test_unknown_named_subset_fails_closed():
    with pytest.raises(ValueError, match="extension_unknown"):
        load_extension_ontology_paths(
            "cac", mode="does-not-exist", project_root=ROOT
        )


def test_missing_child_subset_loads_abduction_modules():
    paths = load_extension_ontology_paths(
        "cac", mode="missing-child", project_root=ROOT
    )
    names = {p.name for p in paths}
    assert "cacontology-stranger-abduction.ttl" in names
    assert "cacontology-case-management.ttl" in names
    assert "cacontology-temporal.ttl" in names
    press = load_extension_ontology_paths("cac", mode="subset", project_root=ROOT)
    press_names = {p.name for p in press}
    assert "cacontology-stranger-abduction.ttl" not in press_names


@pytest.mark.skipif(not validator_available(), reason="case_validate not installed")
def test_t0_missing_child_profile_conforms():
    report = validate_graph_file(
        T0,
        extensions=["cac:missing-child"],
        project_root=ROOT,
        strict_concepts=True,
    )
    payload = report_to_dict(report)
    assert payload["built_version"] == "case-1.5.0"
    assert payload["ontology_identity"]["case"] == "1.5.0"
    assert payload["ontology_identity"]["cac"] == "3.1.0"
    assert DEFAULT_BUILT_VERSION == "case-1.5.0"
    assert report.conforms is True
    assert report.verification_status == "complete"
    assert not report.undeclared_concepts


@pytest.mark.skipif(not validator_available(), reason="case_validate not installed")
def test_invented_term_fails_as_nonexistent():
    report = validate_graph_file(
        INVENTED,
        extensions=["cac:missing-child"],
        project_root=ROOT,
        strict_concepts=True,
    )
    assert report.conforms is not True
    assert INVENTED_IRI in report.undeclared_concepts
    assert "Do not mint" in report.concept_guidance


@pytest.mark.skipif(not validator_available(), reason="case_validate not installed")
def test_subset_miss_is_not_a_missing_ontology_concept():
    report = validate_graph_file(
        T0,
        extensions=["cac"],
        project_root=ROOT,
        strict_concepts=True,
    )
    undeclared = set(report.undeclared_concepts)
    assert undeclared.intersection({ABDUCTION_IRI, CASE_PHASE_IRI, URGENCY_IRI})
    assert report.conforms is not True
    assert "outside the selected validation subset" in report.concept_guidance
    assert "cac:missing-child" in report.concept_guidance
