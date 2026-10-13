# Missing Child Investigations

> See [Recipe Index](INDEX.md) for all recipes.

Model missing-child cases including AMBER alerts, stranger abduction investigations, runaway tracking, and recovery operations using CAC abduction and investigation-coordination classes.

## Scope

**Layer 3 — Institutional workflow** with location and communications evidence support.

## Key classes

| Class | Role |
|---|---|
| `uco-observable:Observation` | Initial missing-person report observation |
| `cacontology-stranger-abduction:StrangerAbductionInvestigation` | Stranger-abduction investigation type |
| `case-investigation:InvestigativeAction` with a descriptive name | AMBER alert issuance when no dedicated CAC class exists |
| `case-investigation:InvestigativeAction` | Cell-site / GPS tracking steps |
| `cacontology-stranger-abduction:VictimRecovery` | Successful victim recovery process |
| `CACInvestigation` | Investigation container |
| `CellSiteFacet` / `LatLongCoordinatesFacet` | Location evidence |

## Canonical pattern

```
uco-observable:Observation (missing-person report)
  └── Related_To ──▶ CACInvestigation
        ├── cacontology:hasStep ──▶ InvestigativeAction (CDR / cell-site / GPS)
        ├── cacontology:hasStep ──▶ InvestigativeAction (AMBER alert activation)
        └── cacontology:hasStep ──▶ cacontology-stranger-abduction:VictimRecovery
```

## Modeling rules

- Separate **report**, **alert**, **tracking**, and **recovery** into distinct actions.
- Link location evidence via `CellSiteFacet` or `LatLongCoordinatesFacet` — see [cell-site.md](cell-site.md).
- When rescue involves extraction from ongoing danger, chain to [cac-victim-rescue-extraction.md](cac-victim-rescue-extraction.md).

## Python skeleton

```python
from case_uco import CASEGraph

graph = CASEGraph()
report = graph.add_node("kb:missing-1", "uco-observable:Observation", {
    "uco-core:name": "Missing-child report observation",
})
graph.write("missing-child.jsonld")
```

## Validation

Use the named missing-child profile so abduction, case-management, and
temporal terms are in the SHACL closure. The default `cac` press-release
subset will reject those terms as a **subset miss**, not as a missing
ontology concept.

```bash
# SDK / MCP
# validate_graph(..., extensions=["cac:missing-child"])
# CASE_UCO_EXTENSIONS=cac

case_validate --built-version case-1.5.0 \
  --ontology-graph ontology/cac/ontology/ontology/cacontology-core-spine.ttl \
  --ontology-graph ontology/cac/ontology/ontology/cacontology-stranger-abduction.ttl \
  examples/cac/t0-missing-child.jsonld
```

The T0 fixture `examples/cac/t0-missing-child.jsonld` is the conformance
target for `cac:missing-child`. Use `extensions=['cac:full']` only when
the complete CAC SPARQL shapes are safe for the installed case-utils.

## Related recipes

- [cell-site.md](cell-site.md)
- [location.md](location.md)
- [cac-victim-rescue-extraction.md](cac-victim-rescue-extraction.md)
