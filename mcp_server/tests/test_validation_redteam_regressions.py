"""Regressions for validation and document-processor issues #49, #50, #51, #58."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import pytest

import document_processor as dp
import server
from case_uco.validation.coverage import check_graph_concepts
from case_uco.validation.graph import (
    required_extensions_for_graph,
    validate_graph_file,
    validator_available,
)

needs_validator = pytest.mark.skipif(
    not validator_available(), reason="case_validate not installed"
)

WALLET_CSV = "wallet,amount\n1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa,1\n"


def _write_thread(path: Path) -> Path:
    path.write_text(
        json.dumps(
            {
                "@context": {
                    "kb": "http://example.org/kb/",
                    "uco-types": "https://ontology.unifiedcyberontology.org/uco/types/",
                    "co": "http://purl.org/co/",
                    "xsd": "http://www.w3.org/2001/XMLSchema#",
                },
                "@graph": [
                    {
                        "@id": "kb:thread-1",
                        "@type": "uco-types:Thread",
                        "co:size": {"@type": "xsd:nonNegativeInteger", "@value": "1"},
                        "co:index": {"@type": "xsd:positiveInteger", "@value": "1"},
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    return path


# --- #50: vendored Collections Ontology terms are declared --------------------


def test_coverage_accepts_collections_ontology_terms(tmp_path: Path) -> None:
    coverage = check_graph_concepts(_write_thread(tmp_path / "thread.jsonld"))
    assert "http://purl.org/co/size" not in coverage.undeclared_properties
    assert "http://purl.org/co/index" not in coverage.undeclared_properties
    assert coverage.ok


@needs_validator
def test_validate_graph_file_conforms_for_collections_terms(tmp_path: Path) -> None:
    report = validate_graph_file(_write_thread(tmp_path / "thread.jsonld"))
    assert report.conforms is True
    assert not report.undeclared_concepts


# --- #51: extra_ontology_graphs alone feeds coverage --------------------------


@needs_validator
def test_extra_ontology_graphs_alone_share_bundle_with_coverage(tmp_path: Path) -> None:
    ontology = tmp_path / "widget.ttl"
    ontology.write_text(
        "@prefix ex: <http://example.org/ont/> .\n"
        "@prefix owl: <http://www.w3.org/2002/07/owl#> .\n"
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
        "@prefix sh: <http://www.w3.org/ns/shacl#> .\n"
        "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n"
        'ex:Widget a owl:Class, sh:NodeShape ; rdfs:label "Widget"@en ;\n'
        "  sh:property [ sh:path ex:label ; sh:datatype xsd:string ; sh:minCount 1 ] .\n"
        'ex:label a owl:DatatypeProperty ; rdfs:label "label"@en .\n',
        encoding="utf-8",
    )
    graph = tmp_path / "widget.jsonld"
    graph.write_text(
        json.dumps(
            {
                "@context": {"kb": "http://example.org/kb/", "ex": "http://example.org/ont/"},
                "@graph": [{"@id": "kb:w1", "@type": "ex:Widget", "ex:label": "ok"}],
            }
        ),
        encoding="utf-8",
    )
    report = validate_graph_file(graph, extra_ontology_graphs=[ontology], strict_concepts=True)
    assert dict(report.stage_status)["bundle_resolution"] == "complete"
    assert not report.undeclared_concepts
    assert report.conforms is True


# --- #49: required-extension handoff ------------------------------------------


def test_required_extensions_names_extension_namespaces_only() -> None:
    document = {
        "@context": {
            "uco-action": "https://ontology.unifiedcyberontology.org/uco/action/",
            "cryptoinv": "http://example.org/ontology/cryptoinv/",
        },
        "@graph": [
            {"@id": "kb:a", "@type": "uco-action:Action"},
            {
                "@id": "kb:f",
                "@type": ["cryptoinv:CryptocurrencyAddressFacet"],
                "cryptoinv:addressValue": "x",
            },
        ],
    }
    assert required_extensions_for_graph(document) == ["cryptoinv"]
    assert required_extensions_for_graph({"@graph": [document["@graph"][0]], "@context": document["@context"]}) == []


def test_processed_csv_reports_cryptoinv_and_validates_with_it(tmp_path: Path) -> None:
    source = tmp_path / "wallets.csv"
    source.write_text(WALLET_CSV, encoding="utf-8")
    output = tmp_path / "out" / "wallets.jsonld"
    doc = dp.process_document_file(source, output)
    assert doc.required_extensions == ("cryptoinv",)
    if validator_available():
        report = validate_graph_file(
            output, extensions=list(doc.required_extensions), strict_concepts=False
        )
        assert report.conforms is True


def test_mcp_tool_payload_carries_required_extensions(tmp_path: Path) -> None:
    source = tmp_path / "wallets.csv"
    source.write_text(WALLET_CSV, encoding="utf-8")
    tool = getattr(server.process_document_file, "fn", server.process_document_file)
    payload = tool(str(source), str(tmp_path / "out" / "wallets.jsonld"))
    assert payload["ok"] is True
    assert payload["required_extensions"] == ["cryptoinv"]
    assert "extensions=['cryptoinv']" in payload["safe_summary"]


# --- #58: the hashed bytes are the extracted bytes ----------------------------


def test_source_changed_during_extraction_keeps_hash_and_rows_consistent(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    source = tmp_path / "rows.csv"
    original = "name,amount\nalice,1\n"
    source.write_text(original, encoding="utf-8")
    real_extract = dp.extract_content

    def extract_after_concurrent_write(path: Path, *args, **kwargs):
        source.write_text("name,amount\nmallory,999\n", encoding="utf-8")
        return real_extract(path, *args, **kwargs)

    monkeypatch.setattr(dp, "extract_content", extract_after_concurrent_write)
    doc = dp.process_document_file(source, tmp_path / "out" / "rows.jsonld")

    assert doc.sha256 == hashlib.sha256(original.encode("utf-8")).hexdigest()
    assert doc.byte_size == len(original.encode("utf-8"))
    serialized = json.dumps(doc.graph)
    assert "alice" in serialized
    assert "mallory" not in serialized


def test_source_is_not_reread_for_hashing(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    source = tmp_path / "rows.csv"
    source.write_text("name,amount\nalice,1\n", encoding="utf-8")
    real_read_bytes = Path.read_bytes
    reads: list[Path] = []

    def counting_read_bytes(self: Path) -> bytes:
        if self == source:
            reads.append(self)
        return real_read_bytes(self)

    monkeypatch.setattr(Path, "read_bytes", counting_read_bytes)
    dp.process_document_file(source, tmp_path / "out" / "rows.jsonld")
    assert reads == []
