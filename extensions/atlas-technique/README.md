# MITRE ATLAS Technique Catalog (`atlas-technique`)

The complete [MITRE ATLAS](https://atlas.mitre.org) (Adversarial Threat
Landscape for AI Systems) technique set from data release 2026.09 — 208
techniques and sub-techniques across 16 tactics — expressed with the UCO
1.5.0 `uco-action:Technique` metaclass, the same pattern as the
[`attack-technique`](../attack-technique/) ATT&CK catalog.

ATLAS describes **adversary tradecraft against AI systems**: prompt
injection, jailbreaks, model evasion, poisoning, model extraction and theft,
and abuse of AI agents and their tools. Load it for graphs whose evidence
shows an attack *on* an AI system. A case that only involves AI (an offender
using a chatbot, AI-generated media) is not an ATLAS case. The extension has
no dependencies; ATT&CK is added to a graph only when the evidence also shows
conventional intrusion (see
[cross-ontology-composition.md](../../docs/recipes/cross-ontology-composition.md)
principle 6).

## The model

```turtle
# In the catalog: a technique is a class; a sub-technique specializes its parent.
atlas:AML.T0051.001
    a owl:Class, uco-action:Technique ;
    rdfs:subClassOf atlas:AML.T0051 ;
    rdfs:label "LLM Prompt Injection: Indirect"@en ;
    uco-action:techniqueID "AML.T0051.001" ;
    dcterms:subject atlas-tactic:AML.TA0005 ;
    dcterms:coverage "Agentic AI" , "Generative AI" ;
    dcterms:isPartOf <https://atlas.mitre.org/matrices/ATLAS> .

# In the case graph: the evidenced behavior is an instance of it.
kb:action-prompt-injection
    a uco-action:Action, atlas:AML.T0051.001 ;
    uco-action:instrument kb:injected-email .
```

| Catalog content | Representation |
|---|---|
| Technique | `owl:Class`, `a uco-action:Technique`, `rdfs:subClassOf uco-action:Action`, `uco-action:techniqueID` (`AML.T…`) |
| Sub-technique | `rdfs:subClassOf` the technique it `specializes`; label "Parent: Sub-technique" |
| Tactic (`achieves`) | `dcterms:subject` → `https://atlas.mitre.org/tactics/AML.TA…` |
| Platform | `dcterms:coverage` (*Generative AI*, *Agentic AI*, *Predictive AI*, *Enterprise*) |
| Maturity | Appended to `rdfs:comment` ("ATLAS maturity: Realized / Demonstrated / Feasible.") |
| Adapted ATT&CK technique / tactic | `rdfs:seeAlso` → the ATT&CK IRI (a reference only; ATT&CK is not imported) |

ATLAS mitigations and case studies are not vendored; the catalog covers what
a case graph types actions with.

## Discovery

- `search_adversary_techniques("prompt injection", catalog="atlas")`
- `get_adversary_technique("AML.T0051.001")`

## Validation

```bash
case_validate --built-version case-1.5.0 \
  --ontology-graph extensions/atlas-technique/mitre-atlas-catalog.ttl \
  --inference rdfs --allow-info \
  path/to/graph.jsonld
```

Or `validate_graph(path, extensions=["atlas-technique"])`.

## Refreshing the catalog

```bash
make sync-atlas                           # ATLAS 2026.09 (or the manifest pin)
make sync-atlas ATLAS_RELEASE=2026.10
make sync-atlas-offline ATLAS_FILE=/path/to/ATLAS-2026.09.yaml ATLAS_RELEASE=2026.09
```

`mcp_server/tools/sync_atlas_catalog.py` reads `dist/v6/ATLAS-<release>.yaml`
(format 6.x) from the `v<release>` tag of
[mitre-atlas/atlas-data](https://github.com/mitre-atlas/atlas-data) —
`dist/ATLAS.yaml` is the deprecated 5.x format — regenerates
`mitre-atlas-catalog.ttl`, and records the release, SHA-256, and counts in
`manifest.json`. ATLAS publishes monthly; `--check` reports drift without
writing. Needs PyYAML.

## Files

| File | What it is |
|---|---|
| `mitre-atlas-catalog.ttl` | Generated catalog (techniques, sub-techniques, tactics, matrix) |
| `manifest.json` | Extension manifest and sync provenance |
| `_registry.json` | Discovery pointer; the metaclass is in the core registry |

## License

ATLAS data: Copyright 2021-2026 MITRE, licensed under the
[Apache License 2.0](https://github.com/mitre-atlas/atlas-data/blob/main/LICENSE).

## Used by

- [`examples/ai-system-attacks/`](../../examples/ai-system-attacks/)
- Recipe: [`docs/recipes/ai-system-attacks.md`](../../docs/recipes/ai-system-attacks.md)
