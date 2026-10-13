# Upper-Ontology Exemplars

Runnable builders that produce JSON-LD graphs aligned with the upper-ontology recipe catalog. Each script uses the public `CASEGraph` API (`create`, `upsert_node`, `add_type`, `add_property`, `create_relationship`) and writes output next to the script.

Validate these graphs locally with vendored CDO-Shapes profiles under `ontology/upper/shapes/` and the SDK shapes for QUDT and SOSA under `ontology/upper/sdk-shapes/` (via `mcp_server/tools/run_recipe_examples.py --validate` or `validate_graph(..., profiles=[...])`).

CI job `recipe-validation` runs every entry in [`docs/recipes/recipe-execution.json`](../../docs/recipes/recipe-execution.json) (`run_recipe_examples.py --all --validate`), including these exemplars. CI uploads the machine-readable report as a workflow artifact (do not commit workstation-local reports with absolute paths).

## Index

| Recipe | Builder | Output |
|---|---|---|
| [foundational-typing-bfo-gufo.md](../../docs/recipes/foundational-typing-bfo-gufo.md) | `foundational-typing/build_bfo_variant.py` | `foundational-typing-bfo.jsonld` |
| [foundational-typing-bfo-gufo.md](../../docs/recipes/foundational-typing-bfo-gufo.md) | `foundational-typing/build_gufo_variant.py` | `foundational-typing-gufo.jsonld` |
| [foundational-typing-bfo-gufo.md](../../docs/recipes/foundational-typing-bfo-gufo.md) | *(static anti-pattern)* | `foundational-typing/invalid_category_mistake.jsonld` |
| [prov-o-evidence-lineage.md](../../docs/recipes/prov-o-evidence-lineage.md) | `prov-o-lineage/build_exemplar.py` | `prov-o-lineage.jsonld` |
| [owl-time-temporal-evidence.md](../../docs/recipes/owl-time-temporal-evidence.md) | `owl-time/build_exemplar.py` | `owl-time-temporal.jsonld` |
| [geosparql-geospatial-evidence.md](../../docs/recipes/geosparql-geospatial-evidence.md) | `geosparql/build_exemplar.py` | `geosparql-geospatial.jsonld` |
| [foaf-org-identity-roles.md](../../docs/recipes/foaf-org-identity-roles.md) | `foaf-org/build_exemplar.py` | `foaf-org-identity.jsonld` |
| [prof-validation-profile-metadata.md](../../docs/recipes/prof-validation-profile-metadata.md) | `prof-metadata/build_exemplar.py` | `prof-metadata.jsonld` |
| [solveit-plan-execution-provenance.md](../../docs/recipes/solveit-plan-execution-provenance.md) | `solveit-plan-execution/build_exemplar.py` | `solveit-plan-execution.jsonld` |
| [sosa-sensor-observations.md](../../docs/recipes/sosa-sensor-observations.md) | `sosa-qudt/build_vehicle_telemetry.py` | `vehicle-telemetry.jsonld` |
| [sosa-sensor-observations.md](../../docs/recipes/sosa-sensor-observations.md) | `sosa-qudt/build_wearable_health.py` | `wearable-health.jsonld` |
| [sosa-sensor-observations.md](../../docs/recipes/sosa-sensor-observations.md) | *(static anti-pattern)* | `sosa-qudt/invalid_qudt2_pattern.jsonld` |
| [qudt-quantities-and-units.md](../../docs/recipes/qudt-quantities-and-units.md) | `sosa-qudt/build_wallet_valuation.py` | `wallet-valuation.jsonld` |
| [cross-ontology-composition.md](../../docs/recipes/cross-ontology-composition.md) | `composition/build_composite.py` | `cross-ontology-composite.jsonld` |

## Run all

```bash
for script in \
  foundational-typing/build_bfo_variant.py \
  foundational-typing/build_gufo_variant.py \
  prov-o-lineage/build_exemplar.py \
  owl-time/build_exemplar.py \
  geosparql/build_exemplar.py \
  foaf-org/build_exemplar.py \
  prof-metadata/build_exemplar.py \
  solveit-plan-execution/build_exemplar.py \
  sosa-qudt/build_vehicle_telemetry.py \
  sosa-qudt/build_wearable_health.py \
  sosa-qudt/build_wallet_valuation.py \
  composition/build_composite.py
do
  python "examples/upper-ontology/$script"
done
```

Or run the gate (builders + optional validation):

```bash
python mcp_server/tools/run_recipe_examples.py --category upper-ontology --validate
```

## Prerequisites

```bash
pip install -e python/   # CASEGraph from this repo
pip install case-utils   # for --validate / case_validate
```

Builders do not invoke `case_validate` directly — validate outputs with profile shapes from `ontology/upper/shapes/` via `run_recipe_examples.py --validate` or `validate_graph(..., profiles=[...])`.

## Related

- [docs/recipes/INDEX.md](../../docs/recipes/INDEX.md) — full recipe catalog
- [docs/recipes/recipe-execution.json](../../docs/recipes/recipe-execution.json) — nine-entry upper-ontology exemplar gate (#69)
- [docs/recipes/cross-ontology-composition.md](../../docs/recipes/cross-ontology-composition.md) — composition policy
- [ontology/upper/provenance.json](../../ontology/upper/provenance.json) — pinned upper-ontology sources
