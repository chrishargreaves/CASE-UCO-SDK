"""scope="core" returns CASE/UCO classes and labels extensions by name (#43)."""

from __future__ import annotations

import pytest


@pytest.mark.parametrize(
    ("name", "iri"),
    [
        ("Subject", "https://ontology.caseontology.org/case/investigation/Subject"),
        ("Technique", "https://ontology.unifiedcyberontology.org/uco/action/Technique"),
    ],
)
def test_core_scope_never_reports_extension_classes(name, iri):
    from server import get_class_details, search_classes

    details = get_class_details(name, scope="core")
    assert details["iri"] == iri
    assert details["source"] == "core"
    core_hits = search_classes(name, scope="core")
    assert core_hits and all(not h["module"].startswith("ext.") for h in core_hits)
    all_hits = search_classes(name, scope="all")
    ext_hits = [h for h in all_hits if h["module"].startswith("ext.")]
    assert ext_hits and all(h["source"] != "core" for h in ext_hits)
