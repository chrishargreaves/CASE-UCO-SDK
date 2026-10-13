# QUDT Quantities and Units

> See [Recipe Index](INDEX.md) for all recipes.

Attach a number to its unit and quantity kind with [QUDT](https://qudt.org/) when CASE/UCO has no native property for the value: a wallet balance in BTC, its USD valuation, a speed, a heart rate, a battery capacity. The SDK pins [QUDT 3.5.2](https://github.com/qudt/qudt-public-repo/releases/tag/v3.5.2) (schema, units, quantity kinds, and prefixes).

Issues: [#148](https://github.com/vulnmaster/CASE-UCO-SDK/issues/148); upstream discussion in [ucoProject/UCO#404](https://github.com/ucoProject/UCO/issues/404).

## Scope

- `qudt:QuantityValue` (a number and a unit) and `qudt:Quantity` (a quantity of some kind, with one or more values)
- Finding unit IRIs with `lookup_qudt_units`
- Recording where a derived value came from
- Runnable exemplar: `examples/upper-ontology/sosa-qudt/build_wallet_valuation.py`

## When to use QUDT

| Value | Approach |
|---|---|
| File size, byte counts, durations, timestamps | Native UCO properties (`size_in_bytes`, `start_time`/`end_time`); no QUDT |
| A number with a unit that UCO has no property for | `qudt:QuantityValue` |
| A sensor's reading | A [SOSA observation](sosa-sensor-observations.md) whose result is a `qudt:QuantityValue` |
| A computed or looked-up value (fiat valuation, a total) | `qudt:Quantity` + `qudt:QuantityValue`, with the lookup recorded as an `InvestigativeAction` |

A lookup is not an observation: no sensor made it. Record the rate source, the time, and the action that computed the value instead.

## Pattern

| Node | Types | Key properties |
|---|---|---|
| The value | `qudt:QuantityValue` | exactly one `qudt:value` (numeric literal), exactly one `qudt:hasUnit` (unit IRI) |
| The quantity | `qudt:Quantity` | `qudt:hasQuantityKind` (`quantitykind:Currency`), `qudt:quantityValue` |
| Its origin | the source object or the computing action | `prov:wasDerivedFrom`, `prov:wasGeneratedBy` |

QUDT 3 renamed the core properties: use `qudt:hasUnit` and `qudt:value`, not the QUDT 2 forms listed under Anti-patterns. Write numbers as typed literals (`xsd:decimal` for measured or monetary values, `xsd:integer` for counts) and keep the lexical form from the source (`0.41250000`).

## Finding units

Unit IRIs follow QUDT's own naming (km/h is `unit:KiloM-PER-HR`), so look them up instead of guessing. The MCP tool `lookup_qudt_units` searches the pinned vocabulary by symbol, English label, UCUM code, ISO 4217 currency code, or quantity kind:

```text
lookup_qudt_units(query="USD")                  -> unit:CCY_USD
lookup_qudt_units(query="bitcoin")              -> unit:CCY_BTC
lookup_qudt_units(query="mAh")                  -> unit:MilliA-HR
lookup_qudt_units(quantity_kind="Count")       -> every count unit, including unit:NUM
```

Common choices: counts use `unit:NUM` with `quantitykind:Count`, ratios use `unit:UNITLESS` or `unit:PERCENT`, angles use `unit:DEG` with `quantitykind:PlaneAngle`. QUDT has no bearing or heading quantity kind.

## Python skeleton

<details open><summary>Python</summary>

```python
from case_uco import CASEGraph

graph = CASEGraph(extra_context={
    "qudt": "http://qudt.org/schema/qudt/",
    "unit": "http://qudt.org/vocab/unit/",
    "quantitykind": "http://qudt.org/vocab/quantitykind/",
    "prov": "http://www.w3.org/ns/prov#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
})

graph.upsert_node("kb:wallet-valuation-1-value", types=["qudt:QuantityValue"], properties={
    "qudt:value": {"@type": "xsd:decimal", "@value": "24537.83"},
    "qudt:hasUnit": {"@id": "unit:CCY_USD"},
})
graph.upsert_node("kb:wallet-valuation-1", types=["qudt:Quantity"], properties={
    "rdfs:label": "Wallet balance valued in USD at 2024-08-14T16:00:00Z",
    "qudt:hasQuantityKind": {"@id": "quantitykind:Currency"},
    "qudt:quantityValue": {"@id": "kb:wallet-valuation-1-value"},
})
graph.link("kb:wallet-valuation-1", "prov:wasGeneratedBy", "kb:valuation-action-1")
graph.link("kb:wallet-valuation-1", "prov:wasDerivedFrom", "kb:rate-source-1")
graph.write("wallet-valuation.jsonld")
```

</details>

```bash
python examples/upper-ontology/sosa-qudt/build_wallet_valuation.py
```

## Validation

```bash
validate_graph("wallet-valuation.jsonld", profiles=["qudt", "prov-o"], strict_concepts=True)

case_validate --built-version case-1.5.0 \
  --ontology-graph ontology/upper/qudt-schema.ttl \
  --ontology-graph ontology/upper/prov-o.ttl \
  --ontology-graph ontology/upper/sdk-shapes/sh-qudt-sdk.ttl \
  --inference rdfs --allow-info wallet-valuation.jsonld
```

The `qudt` profile loads the QUDT schema and the SDK shape `ontology/upper/sdk-shapes/sh-qudt-sdk.ttl`, which requires exactly one numeric `qudt:value` and exactly one `qudt:hasUnit` IRI on every `qudt:QuantityValue`. The SDK does not load QUDT's own SHACL. Its import of SKOS by an unversioned IRI makes it unsuitable for OWL 2 DL review ([ucoProject/UCO#404](https://github.com/ucoProject/UCO/issues/404)). Strict concept coverage checks unit and quantity-kind IRIs against the pinned vocabularies, so a mistyped unit fails validation.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| `qudt:unit` | `qudt:hasUnit` (QUDT 3) |
| `qudt:numericValue` | `qudt:value` |
| Guessed unit IRIs such as `unit:KM-PER-HR` or `unit:USD` | `lookup_qudt_units`; use `unit:KiloM-PER-HR`, `unit:CCY_USD` |
| Value and unit in one string (`"50 km/h"`) | Separate `qudt:value` and `qudt:hasUnit` |
| Two values or two units on one `qudt:QuantityValue` | One node per value |
| A `sosa:Observation` for a looked-up value | `qudt:Quantity` plus the lookup action |
| QUDT for file sizes or timestamps | Native UCO properties |
| A valuation with no rate source or time | Record the rate source and the action that computed it |

## Related

- [sosa-sensor-observations.md](sosa-sensor-observations.md): sensor readings whose results are QUDT values
- [prov-o-evidence-lineage.md](prov-o-evidence-lineage.md): derivation of computed values
- [fraud-crypto-laundering.md](fraud-crypto-laundering.md): wallets, addresses, and transactions
