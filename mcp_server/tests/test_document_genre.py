"""Document-genre gate: catalogs and training documents are not case evidence (#77)."""

from __future__ import annotations

from pathlib import Path

from cac_content_router import route_cac_content
from document_genre import CATALOG_RECIPE, detect_document_genre
from investigation_router import route_investigation_content

ROOT = Path(__file__).resolve().parents[2]
CATALOG = (ROOT / "examples/recipes/resource-catalog-sample.txt").read_text(encoding="utf-8")

CASE_WITH_RESOURCES = """
United States v. Example, Case No. 1:26-cr-00412. The defendant was arrested on
2026-03-14 14:05 after an ICAC task force investigation. The affiant states that
probable cause exists: the CyberTipline report listed IP address 203.0.113.24 and
SHA-256 9F86D081884C7D659A2FEADE0B4C1D5E2E0E7B2E5D1F3A4B6C8D0E1F2A3B4C5D.
Victim services: help.example.org, hotline.example.org/report, parents.example.org.
"""

TRAINING = """
Course outline — Module 1: Introduction to undercover chat investigations.
Learning objectives: participants will be able to document online solicitation.
Module 2: Preserving platform evidence. Lesson 3: Writing the report.
Knowledge check at the end of each module.
"""


def test_catalog_sample_is_a_resource_catalog() -> None:
    genre = detect_document_genre(CATALOG)
    assert genre is not None
    assert genre["genre"] == "resource-catalog"
    assert genre["case_evidence_signals"] == []
    assert {"catalog-disclaimer", "task-headers", "access-badges"} <= set(genre["genre_signals"])
    assert genre["recommended_recipe"] == CATALOG_RECIPE


def test_case_evidence_overrides_catalog_wording() -> None:
    assert detect_document_genre(CASE_WITH_RESOURCES) is None
    assert detect_document_genre(CATALOG + CASE_WITH_RESOURCES) is None


def test_training_material_is_detected() -> None:
    genre = detect_document_genre(TRAINING)
    assert genre is not None and genre["genre"] == "training-material"


def test_investigation_router_prefers_catalog_recipe() -> None:
    result = route_investigation_content(ROOT, content_text=CATALOG)
    assert result["document_genre"]["genre"] == "resource-catalog"
    assert [f["family_id"] for f in result["matched_families"]] == ["resource-catalog"]
    assert result["matched_families"][0]["recipes"] == [CATALOG_RECIPE]
    assert result["ordered_recommendations"]["primary_composition_recipe"] == CATALOG_RECIPE
    topics = {f["family_id"]: f for f in result["topic_families"]}
    assert "docs/recipes/cac-pacer-document-ingestion.md" in topics["cac-child-exploitation"]["deferred_case_recipes"]
    assert result["routing_confidence"]["level"] != "abstain"


def test_investigation_router_keeps_case_routing_for_case_evidence() -> None:
    result = route_investigation_content(ROOT, content_text=CASE_WITH_RESOURCES)
    assert "document_genre" not in result
    assert "resource-catalog" not in [f["family_id"] for f in result["matched_families"]]


def test_cac_router_leads_with_catalog_domain() -> None:
    result = route_cac_content(ROOT, content_text=CATALOG, include_recipe_content=False)
    assert result["document_genre"]["genre"] == "resource-catalog"
    assert result["matched_domains"][0]["domain_id"] == "resource-catalog"
    assert result["matched_domains"][0]["recipe_file"] == CATALOG_RECIPE
    assert all("genre_caveat" in d for d in result["matched_domains"][1:])
    assert result["modeling_checklist"][0]["id"] == "catalog-document-provenance"
    assert result["recommended_workflow"][0] == result["document_genre"]["guidance"]
