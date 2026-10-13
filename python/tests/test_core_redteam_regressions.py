"""Regressions for core issues #34, #37, #52, #54, #55, #59."""

from __future__ import annotations

import json
import warnings
from datetime import date, datetime, timedelta, timezone

import pytest

from case_uco import CASEGraph
from case_uco.graph import parse_xsd_datetime
from case_uco.uco.observable import FileFacet, ObservableObject


def _load(doc: dict) -> tuple[CASEGraph, list]:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", UserWarning)
        return CASEGraph.from_jsonld(json.dumps(doc))


def _sized_doc(size_literal: dict) -> dict:
    g = CASEGraph()
    g.create(ObservableObject, name="good-node")
    g.create(
        ObservableObject,
        name="sized",
        has_facet=[FileFacet(file_name="evidence.dd", size_in_bytes=4096)],
    )
    doc = json.loads(g.serialize())
    for node in doc["@graph"]:
        for facet in node.get("uco-core:hasFacet") or []:
            if "uco-observable:sizeInBytes" in facet:
                facet["uco-observable:sizeInBytes"] = size_literal
    return doc


def test_bad_literal_keeps_good_nodes_and_warns():
    graph, objects = _load(_sized_doc({"@type": "xsd:integer", "@value": "4096.0"}))
    names = {getattr(o, "name", None) for o in objects}
    assert {"good-node", "sized"} <= names
    reasons = [w.reason for w in graph.deserialization_warnings]
    assert "coercion_failed" in reasons
    detail = next(w.detail for w in graph.deserialization_warnings if w.reason == "coercion_failed")
    assert "size_in_bytes" in detail


@pytest.mark.parametrize(
    "datatype",
    ["xsd:nonNegativeInteger", "xsd:positiveInteger", "xsd:long", "xsd:unsignedInt"],
)
def test_integer_subtypes_coerce_to_int(datatype):
    _graph, objects = _load(_sized_doc({"@type": datatype, "@value": "42"}))
    facets = [f for o in objects for f in (getattr(o, "has_facet", None) or [])]
    sizes = [f.size_in_bytes for f in facets if isinstance(f, FileFacet)]
    assert sizes == [42]
    assert isinstance(sizes[0], int)


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("2024-01-01T00:00Z", datetime(2024, 1, 1, tzinfo=timezone.utc)),
        ("2024-01-01T00:00:00Z", datetime(2024, 1, 1, tzinfo=timezone.utc)),
        (
            "2024-01-01T00:00:00.123456700Z",
            datetime(2024, 1, 1, 0, 0, 0, 123456, tzinfo=timezone.utc),
        ),
        ("2024-01-01T00:00Z[UTC]", datetime(2024, 1, 1, tzinfo=timezone.utc)),
        (
            "2024-01-01T05:30:00.5+05:30",
            datetime(2024, 1, 1, 5, 30, 0, 500000, tzinfo=timezone(timedelta(hours=5, minutes=30))),
        ),
    ],
)
def test_parse_xsd_datetime_forms(text, expected):
    assert parse_xsd_datetime(text) == expected


def test_zone_id_datetime_does_not_abort_document():
    g = CASEGraph()
    g.create(FileFacet, file_name="good")
    g.create(FileFacet, file_name="zoned", modified_time=datetime(2024, 1, 1, tzinfo=timezone.utc))
    doc = json.loads(g.serialize())
    for node in doc["@graph"]:
        if "uco-observable:modifiedTime" in node:
            node["uco-observable:modifiedTime"]["@value"] = "2024-01-01T00:00Z[UTC]"
    graph, objects = _load(doc)
    assert {o.file_name for o in objects} == {"good", "zoned"}
    assert not graph.deserialization_warnings


def test_date_on_datetime_field_is_midnight():
    g = CASEGraph()
    g.create(FileFacet, file_name="x", modified_time=date(2024, 12, 31))
    node = json.loads(g.serialize())["@graph"][0]
    assert node["uco-observable:modifiedTime"] == {
        "@type": "xsd:dateTime",
        "@value": "2024-12-31T00:00:00",
    }


def test_bytes_on_integer_field_is_rejected():
    g = CASEGraph()
    with pytest.raises(TypeError):
        g.create(FileFacet, file_name="x.bin", size_in_bytes=b"\x00\x01ABC")
        g.serialize()


def test_partitions_do_not_share_nested_lists():
    g = CASEGraph()
    g.create(ObservableObject, name="p", has_facet=[FileFacet(file_name="a.txt")])
    src = g._objects[0]
    part = g.partition_by(lambda obj: "only")["only"]._objects[0]
    part["uco-core:hasFacet"].append({"@id": "kb:alias"})
    assert len(src["uco-core:hasFacet"]) == 1

    g2 = CASEGraph()
    g2.create(ObservableObject, name="rootish", has_facet=[FileFacet(file_name="b.txt")])
    src2 = g2._objects[0]
    for pg in g2.partition_by_roots([src2["@id"]]).values():
        for obj in pg._objects:
            if obj.get("@id") == src2["@id"]:
                obj["uco-core:hasFacet"].append({"@id": "kb:alias2"})
    assert len(src2["uco-core:hasFacet"]) == 1
