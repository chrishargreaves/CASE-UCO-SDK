#!/usr/bin/env python3
"""Wearable health-data exemplar for docs/recipes/sosa-sensor-observations.md.

A fitness band's step counter and optical heart-rate sensor produced the
records recovered from the paired phone's health database. The exemplar
shows SSN system capabilities (the heart-rate sensor's published accuracy),
an observation over an interval (a daily step count, OWL-Time), a point
observation (heart rate), and provenance back to the extracted file.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from case_uco import CASEGraph
from case_uco.case.investigation import Investigation, InvestigativeAction
from case_uco.uco.identity import Person
from case_uco.uco.observable import Device, DeviceFacet, FileFacet, ObservableObject, WearableDevice
from case_uco.uco.tool import Tool

HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "wearable-health.jsonld"

EXTRA_CONTEXT = {
    "sosa": "http://www.w3.org/ns/sosa/",
    "ssn-system": "http://www.w3.org/ns/ssn/systems/",
    "qudt": "http://qudt.org/schema/qudt/",
    "unit": "http://qudt.org/vocab/unit/",
    "quantitykind": "http://qudt.org/vocab/quantitykind/",
    "time": "http://www.w3.org/2006/time#",
    "prov": "http://www.w3.org/ns/prov#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
}


def _typed(datatype: str, value: str) -> dict:
    return {"@type": datatype, "@value": value}


def _quantity_value(graph: CASEGraph, node_id: str, value: str, unit: str, datatype: str = "xsd:decimal") -> str:
    graph.upsert_node(
        node_id,
        types=["qudt:QuantityValue"],
        properties={"qudt:value": _typed(datatype, value), "qudt:hasUnit": {"@id": unit}},
    )
    return node_id


def build() -> CASEGraph:
    graph = CASEGraph(extra_context=EXTRA_CONTEXT)
    tz = timezone.utc

    # The wearer is the feature of interest of both observations.
    wearer_id = "kb:wearer-1"
    wearer = graph.create(Person, id=wearer_id, name="Device owner (synthetic)")
    graph.add_type(wearer_id, "sosa:FeatureOfInterest")

    band_id = "kb:fitness-band-1"
    band = graph.create(
        WearableDevice,
        id=band_id,
        name="Fitness band",
        has_facet=[DeviceFacet(model="Band 7", serial_number="FB7-55821")],
    )
    graph.add_type(band_id, "sosa:Platform")

    step_counter_id = "kb:step-counter-1"
    graph.create(Device, id=step_counter_id, name="Fitness band accelerometer step counter",
                 has_facet=[DeviceFacet(device_type="accelerometer")])
    heart_sensor_id = "kb:heart-rate-sensor-1"
    graph.create(Device, id=heart_sensor_id, name="Fitness band optical heart-rate sensor",
                 has_facet=[DeviceFacet(device_type="photoplethysmography sensor")])
    for sensor_id in (step_counter_id, heart_sensor_id):
        graph.add_type(sensor_id, "sosa:Sensor")
        graph.link(sensor_id, "sosa:isHostedBy", band_id)
        graph.link(band_id, "sosa:hosts", sensor_id)

    step_count = "kb:daily-step-count"
    graph.upsert_node(step_count, types=["sosa:ObservableProperty"], properties={
        "rdfs:label": "Steps taken per calendar day",
        "qudt:hasQuantityKind": {"@id": "quantitykind:Count"},
    })
    heart_rate = "kb:heart-rate"
    graph.upsert_node(heart_rate, types=["sosa:ObservableProperty"], properties={
        "rdfs:label": "Heart rate",
        "qudt:hasQuantityKind": {"@id": "quantitykind:HeartRate"},
    })
    graph.link(step_counter_id, "sosa:observes", step_count)
    graph.link(heart_sensor_id, "sosa:observes", heart_rate)

    # Published accuracy of the heart-rate sensor (SSN-System capability).
    accuracy_id = "kb:heart-rate-accuracy"
    graph.upsert_node(accuracy_id, types=["ssn-system:Accuracy", "qudt:Quantity"], properties={
        "rdfs:comment": "Manufacturer-stated accuracy at rest (synthetic specification).",
        "qudt:hasQuantityKind": {"@id": "quantitykind:HeartRate"},
        "qudt:quantityValue": {"@id": _quantity_value(graph, "kb:heart-rate-accuracy-value", "5", "unit:BEAT-PER-MIN")},
    })
    capability_id = "kb:heart-rate-capability"
    graph.upsert_node(capability_id, types=["ssn-system:SystemCapability"], properties={
        "ssn-system:hasSystemProperty": {"@id": accuracy_id},
    })
    graph.link(heart_sensor_id, "ssn-system:hasSystemCapability", capability_id)

    health_db_id = "kb:health-db-1"
    health_db = graph.create(
        ObservableObject,
        id=health_db_id,
        name="healthdb_secure.sqlite",
        has_facet=[FileFacet(file_name="healthdb_secure.sqlite", size_in_bytes=2097152)],
    )
    tool = graph.create(Tool, name="Example mobile extraction tool", version="7.1")
    graph.create(
        InvestigativeAction,
        name="Parse paired phone health database",
        start_time=datetime(2024, 5, 3, 13, 0, tzinfo=tz),
        end_time=datetime(2024, 5, 3, 13, 20, tzinfo=tz),
        instrument=[tool],
        object=[health_db],
    )

    # A daily step count describes an interval (phenomenonTime) and was
    # computed when the day closed (resultTime).
    day_id = "kb:day-2024-04-30"
    for edge, stamp in (("begin", "2024-04-30T00:00:00-04:00"), ("end", "2024-05-01T00:00:00-04:00")):
        graph.upsert_node(f"{day_id}-{edge}", types=["time:Instant"], properties={
            "time:inXSDDateTimeStamp": _typed("xsd:dateTimeStamp", stamp),
        })
    graph.upsert_node(day_id, types=["time:Interval"], properties={
        "time:hasBeginning": {"@id": f"{day_id}-begin"},
        "time:hasEnd": {"@id": f"{day_id}-end"},
    })
    graph.upsert_node("kb:step-observation-1", types=["sosa:Observation"], properties={
        "sosa:madeBySensor": {"@id": step_counter_id},
        "sosa:hasFeatureOfInterest": {"@id": wearer_id},
        "sosa:observedProperty": {"@id": step_count},
        "sosa:phenomenonTime": {"@id": day_id},
        "sosa:resultTime": _typed("xsd:dateTime", "2024-05-01T00:00:05-04:00"),
        "sosa:hasResult": {"@id": _quantity_value(graph, "kb:step-count-value-1", "8432", "unit:NUM", "xsd:integer")},
        "prov:wasDerivedFrom": {"@id": health_db_id},
    })
    graph.upsert_node("kb:heart-rate-observation-1", types=["sosa:Observation"], properties={
        "sosa:madeBySensor": {"@id": heart_sensor_id},
        "sosa:hasFeatureOfInterest": {"@id": wearer_id},
        "sosa:observedProperty": {"@id": heart_rate},
        "sosa:resultTime": _typed("xsd:dateTime", "2024-04-30T21:47:12-04:00"),
        "sosa:hasResult": {"@id": _quantity_value(graph, "kb:heart-rate-value-1", "142", "unit:BEAT-PER-MIN")},
        "prov:wasDerivedFrom": {"@id": health_db_id},
    })

    graph.create(
        Investigation,
        name="Synthetic case 2024-WEAR-007",
        description=["Activity timeline from a fitness band's step and heart-rate records."],
        object=[wearer, band, health_db],
    )
    return graph


def main() -> None:
    graph = build()
    graph.write(str(OUTPUT))
    print(f"wrote {OUTPUT} ({len(graph)} nodes)")


if __name__ == "__main__":
    main()
