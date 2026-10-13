# SOSA/SSN Sensor Observations

> See [Recipe Index](INDEX.md) for all recipes.

Model readings that a sensor made about something (vehicle telemetry, wearable heart rate, a phone's barometer) with the [W3C Semantic Sensor Network Ontology](https://www.w3.org/TR/2017/REC-vocab-ssn-20171019/) (SOSA core plus SSN and SSN-System), and carry each value with its unit using [QUDT](qudt-quantities-and-units.md). The device stays a UCO `Device`; SOSA adds the sensor role, the observation, and what was observed.

Issues: [#148](https://github.com/vulnmaster/CASE-UCO-SDK/issues/148); upstream discussion in [ucoProject/UCO#404](https://github.com/ucoProject/UCO/issues/404) and [ucoProject/UCO#567](https://github.com/ucoProject/UCO/issues/567).

## Scope

- When a reading is a SOSA observation and when it is just a quantity
- Hosting a `sosa:Sensor` on a `sosa:Platform`, both typed as UCO devices
- `sosa:Observation` with a `qudt:QuantityValue` result, result time, and phenomenon time
- SSN-System capabilities such as a sensor's stated accuracy
- Runnable exemplars: `examples/upper-ontology/sosa-qudt/build_vehicle_telemetry.py` and `build_wearable_health.py`

## When to use SOSA

SOSA is for the Sensor-Observation-Sampling-Actuator pattern: a sensor, a property it observes, the thing that property belongs to, and a result at a time. Use it when the evidence records what a sensor reported. Do not wrap every number in an observation.

| Evidence | Approach |
|---|---|
| Vehicle speed and heading logged by the infotainment GNSS receiver | `sosa:Observation` per reading, result is a `qudt:QuantityValue` |
| Daily step count and heart rate from a fitness band | `sosa:Observation`; a daily total also gets `sosa:phenomenonTime` (an OWL-Time interval) |
| A sensor's published accuracy or range | SSN-System `ssn-system:SystemCapability` with an `ssn-system:Accuracy` property |
| A phone was unlocked at 14:02 | An event or `InvestigativeAction` with native times, not an observation ([event.md](event.md)) |
| A wallet's USD value from an exchange rate | A `qudt:Quantity` and the lookup action ([qudt-quantities-and-units.md](qudt-quantities-and-units.md)) |
| File size, duration, byte counts | Native UCO properties (`size_in_bytes`, `start_time`/`end_time`) |

## Pattern

| Node | Types | Key links |
|---|---|---|
| Vehicle, wearer, room | UCO object (`ObservableObject`, `Person`) + `sosa:FeatureOfInterest` | target of `sosa:hasFeatureOfInterest` |
| Head unit, wristband | `Device` / `WearableDevice` + `sosa:Platform` | `sosa:hosts` the sensors |
| GNSS receiver, accelerometer | `Device` + `sosa:Sensor` | `sosa:isHostedBy`, `sosa:observes` |
| Speed, heart rate | `sosa:ObservableProperty` with `rdfs:label` | `qudt:hasQuantityKind` (`quantitykind:Speed`, `quantitykind:HeartRate`) |
| One reading | `sosa:Observation` | `sosa:madeBySensor`, `sosa:hasFeatureOfInterest`, `sosa:observedProperty`, `sosa:hasResult`, `sosa:resultTime` |
| The reading's value | `qudt:QuantityValue` | `qudt:value` (numeric), `qudt:hasUnit` |
| Where the reading came from | the extracted file (`ObservableObject` + `FileFacet`) | `prov:wasDerivedFrom` on the observation |

`sosa:resultTime` is when the result was produced (an `xsd:dateTime`). `sosa:phenomenonTime` is when the observed property had that value; use it when that differs, for example a daily total over a calendar day.

SOSA, SSN, and QUDT classes are not SDK dataclasses. Create UCO objects with `graph.create()`, then add the SOSA role with `graph.add_type()` and SOSA nodes with `graph.upsert_node()`.

## Python skeleton

<details open><summary>Python</summary>

```python
from case_uco import CASEGraph
from case_uco.uco.observable import Device, DeviceFacet, ObservableObject

graph = CASEGraph(extra_context={
    "sosa": "http://www.w3.org/ns/sosa/",
    "qudt": "http://qudt.org/schema/qudt/",
    "unit": "http://qudt.org/vocab/unit/",
    "quantitykind": "http://qudt.org/vocab/quantitykind/",
    "prov": "http://www.w3.org/ns/prov#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
})

graph.create(ObservableObject, id="kb:vehicle-1", name="Seized vehicle")
graph.add_type("kb:vehicle-1", "sosa:FeatureOfInterest")
graph.create(Device, id="kb:gnss-1", name="Infotainment GNSS receiver",
             has_facet=[DeviceFacet(device_type="GNSS receiver")])
graph.add_type("kb:gnss-1", "sosa:Sensor")

graph.upsert_node("kb:vehicle-speed", types=["sosa:ObservableProperty"], properties={
    "rdfs:label": "Vehicle speed",
    "qudt:hasQuantityKind": {"@id": "quantitykind:Speed"},
})
graph.upsert_node("kb:speed-value-1", types=["qudt:QuantityValue"], properties={
    "qudt:value": {"@type": "xsd:decimal", "@value": "50"},
    "qudt:hasUnit": {"@id": "unit:KiloM-PER-HR"},
})
graph.upsert_node("kb:speed-observation-1", types=["sosa:Observation"], properties={
    "sosa:madeBySensor": {"@id": "kb:gnss-1"},
    "sosa:hasFeatureOfInterest": {"@id": "kb:vehicle-1"},
    "sosa:observedProperty": {"@id": "kb:vehicle-speed"},
    "sosa:hasResult": {"@id": "kb:speed-value-1"},
    "sosa:resultTime": {"@type": "xsd:dateTime", "@value": "2023-11-22T15:30:00Z"},
    "prov:wasDerivedFrom": {"@id": "kb:telemetry-log-1"},
})
graph.write("vehicle-telemetry.jsonld")
```

</details>

```bash
python examples/upper-ontology/sosa-qudt/build_vehicle_telemetry.py
python examples/upper-ontology/sosa-qudt/build_wearable_health.py
```

### Sensor capability (SSN-System)

```python
graph.upsert_node("kb:hr-accuracy", types=["ssn-system:Accuracy", "qudt:Quantity"], properties={
    "qudt:hasQuantityKind": {"@id": "quantitykind:HeartRate"},
    "qudt:quantityValue": {"@id": "kb:hr-accuracy-value"},  # 5 unit:BEAT-PER-MIN
})
graph.upsert_node("kb:hr-capability", types=["ssn-system:SystemCapability"], properties={
    "ssn-system:hasSystemProperty": {"@id": "kb:hr-accuracy"},
})
graph.link("kb:heart-rate-sensor-1", "ssn-system:hasSystemCapability", "kb:hr-capability")
```

Record where a stated capability came from (a specification sheet, a test report) in `rdfs:comment` or with `prov:wasDerivedFrom`. Never infer one.

## Finding units

Look up unit IRIs instead of guessing them. The MCP tool `lookup_qudt_units` searches the pinned QUDT units vocabulary by symbol, label, UCUM code, or quantity kind:

```text
lookup_qudt_units(query="km/h")             -> unit:KiloM-PER-HR
lookup_qudt_units(query="bpm")              -> unit:BEAT-PER-MIN
lookup_qudt_units(quantity_kind="Speed")    -> every speed unit
```

QUDT 3.5.2 has no bearing or heading quantity kind. Use `quantitykind:PlaneAngle` with `unit:DEG` and say in the property's `rdfs:label` which reference direction applies (true north, magnetic north).

## Validation

Select `sosa` for SOSA-only graphs. Selecting `ssn` adds SSN and SSN-System and pulls in `sosa`. Add `qudt` for values and `time` when you use OWL-Time intervals.

```bash
validate_graph("vehicle-telemetry.jsonld", profiles=["sosa", "qudt", "prov-o"], strict_concepts=True)
validate_graph("wearable-health.jsonld", profiles=["ssn", "qudt", "time", "prov-o"], strict_concepts=True)

case_validate --built-version case-1.5.0 \
  --ontology-graph ontology/upper/sosa.ttl \
  --ontology-graph ontology/upper/qudt-schema.ttl \
  --ontology-graph ontology/upper/prov-o.ttl \
  --ontology-graph ontology/upper/sdk-shapes/sh-sosa-sdk.ttl \
  --ontology-graph ontology/upper/sdk-shapes/sh-qudt-sdk.ttl \
  --inference rdfs --allow-info vehicle-telemetry.jsonld
```

The W3C does not publish SHACL shapes for SOSA or SSN, and CDO-Shapes has no SOSA, SSN, or QUDT profile yet. The SDK ships shapes in `ontology/upper/sdk-shapes/`: every observation needs a result; the sensor, feature of interest, observed property, phenomenon time, and result time each appear at most once; `sosa:resultTime` is an `xsd:dateTime`. They are deliberately weaker than the SSN 2017 OWL axioms (exactly one of each). Strict concept coverage rejects terms the pinned W3C release does not declare.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| A `sosa:Observation` for a device unlock or a login | Model the event or action with native times |
| A `sosa:Observation` for a looked-up value (a wallet's fiat value) | Use a `qudt:Quantity` and record the lookup ([qudt-quantities-and-units.md](qudt-quantities-and-units.md)) |
| An observation with no `sosa:hasResult` or `sosa:hasSimpleResult` | Attach the reading; the SDK shape rejects an empty observation |
| `sosa:hasSimpleResult "50 km/h"` | A `qudt:QuantityValue` with `qudt:value` 50 and `qudt:hasUnit unit:KiloM-PER-HR` |
| `qudt:unit` / `qudt:numericValue` (QUDT 2 pattern) | `qudt:hasUnit` / `qudt:value` |
| Guessed unit IRIs such as `unit:KM-PER-HR` | `lookup_qudt_units`; strict coverage rejects undeclared units |
| `sosa:resultTime` as a plain string | `xsd:dateTime` literal |
| Replacing the UCO `Device` with a bare `sosa:Sensor` | Keep the UCO type and add the SOSA role |
| Treating UCO's `observable:Observation` as a SOSA observation | UCO's class is an `action:Action` for the act of observing; it is not aligned with SOSA |

## Related

- [qudt-quantities-and-units.md](qudt-quantities-and-units.md): quantities and units outside the sensor pattern
- [owl-time-temporal-evidence.md](owl-time-temporal-evidence.md): intervals for `sosa:phenomenonTime`
- [prov-o-evidence-lineage.md](prov-o-evidence-lineage.md): tying readings to the extracted source
- [geosparql-geospatial-evidence.md](geosparql-geospatial-evidence.md): locations that go with GNSS readings
