"""QUDT and SOSA/SSN profiles (issue #60): bundle composition, object-IRI
coverage for unit vocabularies, and the unit lookup tool.

All fixtures are Tier T0 public-safe synthetic data.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import concept_coverage
import qudt_units
from validation_bundle import resolve_validation_bundle

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

QUDT = "http://qudt.org/schema/qudt/"
UNIT = "http://qudt.org/vocab/unit/"
SOSA = "http://www.w3.org/ns/sosa/"
XSD_DECIMAL = "http://www.w3.org/2001/XMLSchema#decimal"
PROF_ROLE = "http://www.w3.org/ns/dx/prof/role/"

pytestmark = pytest.mark.skipif(
    not concept_coverage._core_ontology_paths(PROJECT_ROOT),
    reason="core ontology submodules not present",
)


def _write(tmp_path: Path, nodes: list[dict]) -> Path:
    target = tmp_path / "graph.jsonld"
    target.write_text(
        json.dumps({"@context": {"kb": "http://example.org/kb/"}, "@graph": nodes}),
        encoding="utf-8",
    )
    return target


def _quantity_value(unit_iri: str, unit_predicate: str = QUDT + "hasUnit") -> dict:
    return {
        "@id": "kb:value-1",
        "@type": QUDT + "QuantityValue",
        QUDT + "value": {"@type": XSD_DECIMAL, "@value": "50"},
        unit_predicate: {"@id": unit_iri},
    }


def _check(path: Path, profiles: list[str]):
    return concept_coverage.check_graph_concepts(
        path, project_root=PROJECT_ROOT, selected_profiles=profiles
    )


def test_ssn_profile_pulls_in_sosa_and_sdk_shapes():
    bundle = resolve_validation_bundle(profiles=["ssn", "qudt"], project_root=PROJECT_ROOT)
    assert set(bundle.profiles) == {"ssn", "sosa", "qudt"}
    names = {Path(p).name for p in bundle.ontology_graph_paths()}
    assert {"sosa.ttl", "ssn.ttl", "ssn-systems.ttl", "qudt-schema.ttl"} <= names
    assert {"sh-sosa-sdk.ttl", "sh-qudt-sdk.ttl"} <= names


def test_declared_unit_iri_passes_under_qudt(tmp_path):
    report = _check(_write(tmp_path, [_quantity_value(UNIT + "KiloM-PER-HR")]), ["qudt"])
    assert report.ok is True, report.unknown_upper_ontology_terms


def test_guessed_unit_iri_fails(tmp_path):
    report = _check(_write(tmp_path, [_quantity_value(UNIT + "KM-PER-HR")]), ["qudt"])
    assert report.ok is False
    assert UNIT + "KM-PER-HR" in report.unknown_upper_ontology_terms


def test_qudt2_unit_predicate_fails(tmp_path):
    graph = _write(tmp_path, [_quantity_value(UNIT + "KiloM-PER-HR", QUDT + "unit")])
    report = _check(graph, ["qudt"])
    assert report.ok is False
    assert QUDT + "unit" in report.unknown_upper_ontology_terms


def test_unit_iri_without_qudt_profile_is_profile_not_selected(tmp_path):
    graph = _write(
        tmp_path,
        [
            {
                "@id": "kb:observation-1",
                "@type": SOSA + "Observation",
                SOSA + "hasResult": {"@id": UNIT + "KiloM-PER-HR"},
            }
        ],
    )
    report = _check(graph, ["sosa"])
    assert report.ok is False
    assert any(
        item.iri == UNIT + "KiloM-PER-HR"
        and item.required_profile == "qudt"
        and item.used_as == "value"
        for item in report.profile_not_selected
    )


@pytest.mark.parametrize(
    ("role", "ok"),
    [("validation", True), ("ValidationRole", False)],
)
def test_prof_resource_roles_are_checked(tmp_path, role, ok):
    graph = _write(
        tmp_path,
        [
            {
                "@id": "kb:descriptor-1",
                "@type": "http://www.w3.org/ns/dx/prof/ResourceDescriptor",
                "http://www.w3.org/ns/dx/prof/hasRole": {"@id": PROF_ROLE + role},
            }
        ],
    )
    report = _check(graph, ["prof"])
    assert report.ok is ok
    assert (PROF_ROLE + role in report.unknown_upper_ontology_terms) is not ok


@pytest.mark.parametrize(
    ("query", "expected"),
    [
        ("km/h", "unit:KiloM-PER-HR"),
        ("mph", "unit:MI-PER-HR"),
        ("degrees", "unit:DEG"),
        ("bpm", "unit:BEAT-PER-MIN"),
        ("USD", "unit:CCY_USD"),
        ("EUR", "unit:CCY_EUR"),
        ("mAh", "unit:MilliA-HR"),
        ("meters", "unit:M"),
        ("liters", "unit:L"),
    ],
)
def test_lookup_ranks_expected_unit_first(query, expected):
    result = qudt_units.lookup_units(query, limit=3)
    assert result["units"][0]["id"] == expected


def test_lookup_rejects_guessed_iri_with_hint():
    result = qudt_units.lookup_units("KM-PER-HR")
    assert result["units"] == []
    assert "Do not invent" in result["hint"]


def test_lookup_filters_by_quantity_kind_and_clamps_limit():
    result = qudt_units.lookup_units("", quantity_kind="Speed", limit=500)
    assert 0 < len(result["units"]) <= 50
    assert all("quantitykind:Speed" in u["quantity_kinds"] for u in result["units"])
    assert all(u["iri"].startswith(UNIT) for u in result["units"])
