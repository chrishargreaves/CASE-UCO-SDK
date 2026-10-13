#!/usr/bin/env python3
"""Vehicle telemetry exemplar for docs/recipes/sosa-sensor-observations.md.

Scenario from ucoProject/UCO#567: an infotainment unit logged the vehicle's
bearing and speed in the minutes before a collision. Each log row becomes a
pair of SOSA observations whose results are QUDT quantity values. The sensor
and its host are the same nodes as the UCO devices, and every observation
records which extracted file it came from.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from case_uco import CASEGraph
from case_uco.case.investigation import Investigation, InvestigativeAction
from case_uco.uco.observable import Device, DeviceFacet, FileFacet, ObservableObject
from case_uco.uco.tool import Tool

HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "vehicle-telemetry.jsonld"

EXTRA_CONTEXT = {
    "sosa": "http://www.w3.org/ns/sosa/",
    "qudt": "http://qudt.org/schema/qudt/",
    "unit": "http://qudt.org/vocab/unit/",
    "quantitykind": "http://qudt.org/vocab/quantitykind/",
    "prov": "http://www.w3.org/ns/prov#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
}

# (timestamp, bearing in degrees, speed in km/h) from the synthetic log.
LOG_ROWS = [
    ("2023-11-22T15:30:00Z", "90", "50"),
    ("2023-11-22T15:32:00Z", "135", "70"),
    ("2023-11-22T15:33:30Z", "180", "30"),
]


def _decimal(value: str) -> dict:
    return {"@type": "xsd:decimal", "@value": value}


def _datetime(value: str) -> dict:
    return {"@type": "xsd:dateTime", "@value": value}


def build() -> CASEGraph:
    graph = CASEGraph(extra_context=EXTRA_CONTEXT)
    tz = timezone.utc

    # The vehicle is the feature of interest. UCO has no vehicle class, so it
    # is a plain observable object.
    vehicle_id = "kb:vehicle-1"
    vehicle = graph.create(
        ObservableObject,
        id=vehicle_id,
        name="Suspect vehicle (synthetic)",
        description=["2021 sedan involved in the collision under investigation."],
    )
    graph.add_type(vehicle_id, "sosa:FeatureOfInterest")

    # The infotainment unit is a UCO device and the SOSA platform hosting the
    # GNSS receiver; the receiver is a UCO device and the SOSA sensor.
    infotainment_id = "kb:infotainment-1"
    infotainment = graph.create(
        Device,
        id=infotainment_id,
        name="Vehicle infotainment unit",
        has_facet=[DeviceFacet(model="IVI-9", serial_number="IVI9-000123")],
    )
    graph.add_type(infotainment_id, "sosa:Platform")

    gnss_id = "kb:gnss-receiver-1"
    graph.create(
        Device,
        id=gnss_id,
        name="Infotainment GNSS receiver",
        has_facet=[DeviceFacet(device_type="GNSS receiver")],
    )
    graph.add_type(gnss_id, "sosa:Sensor")
    graph.link(gnss_id, "sosa:isHostedBy", infotainment_id)
    graph.link(infotainment_id, "sosa:hosts", gnss_id)

    speed_property = "kb:vehicle-speed"
    graph.upsert_node(
        speed_property,
        types=["sosa:ObservableProperty"],
        properties={
            "rdfs:label": "Vehicle speed over ground",
            "qudt:hasQuantityKind": {"@id": "quantitykind:Speed"},
        },
    )
    bearing_property = "kb:vehicle-bearing"
    graph.upsert_node(
        bearing_property,
        types=["sosa:ObservableProperty"],
        properties={
            # QUDT has no bearing or heading quantity kind; bearing is a plane
            # angle measured clockwise from true north.
            "rdfs:label": "Vehicle bearing (degrees clockwise from true north)",
            "qudt:hasQuantityKind": {"@id": "quantitykind:PlaneAngle"},
        },
    )
    graph.link(gnss_id, "sosa:observes", speed_property)
    graph.link(gnss_id, "sosa:observes", bearing_property)

    # The extracted log the observations were parsed from.
    log_id = "kb:telemetry-log-1"
    log_file = graph.create(
        ObservableObject,
        id=log_id,
        name="navigation_trace.db",
        has_facet=[FileFacet(file_name="navigation_trace.db", size_in_bytes=40960)],
    )

    tool = graph.create(Tool, name="Example vehicle extraction tool", version="5.2")
    graph.create(
        InvestigativeAction,
        name="Extract infotainment navigation log",
        start_time=datetime(2023, 11, 23, 9, 0, tzinfo=tz),
        end_time=datetime(2023, 11, 23, 9, 40, tzinfo=tz),
        instrument=[tool],
        object=[infotainment],
        result=[log_file],
    )

    for index, (timestamp, bearing, speed) in enumerate(LOG_ROWS, start=1):
        for prop_id, value, unit, label in (
            (speed_property, speed, "unit:KiloM-PER-HR", "speed"),
            (bearing_property, bearing, "unit:DEG", "bearing"),
        ):
            value_id = f"kb:{label}-value-{index}"
            graph.upsert_node(
                value_id,
                types=["qudt:QuantityValue"],
                properties={
                    "qudt:value": _decimal(value),
                    "qudt:hasUnit": {"@id": unit},
                },
            )
            observation_id = f"kb:{label}-observation-{index}"
            graph.upsert_node(
                observation_id,
                types=["sosa:Observation"],
                properties={
                    "sosa:madeBySensor": {"@id": gnss_id},
                    "sosa:hasFeatureOfInterest": {"@id": vehicle_id},
                    "sosa:observedProperty": {"@id": prop_id},
                    "sosa:hasResult": {"@id": value_id},
                    "sosa:resultTime": _datetime(timestamp),
                    "prov:wasDerivedFrom": {"@id": log_id},
                },
            )

    graph.create(
        Investigation,
        name="Synthetic case 2023-TRAFFIC-014",
        description=["Collision reconstruction from infotainment bearing and speed telemetry."],
        object=[vehicle, infotainment, log_file],
    )
    return graph


def main() -> None:
    graph = build()
    graph.write(str(OUTPUT))
    print(f"wrote {OUTPUT} ({len(graph)} nodes)")


if __name__ == "__main__":
    main()
