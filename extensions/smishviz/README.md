# SmishViz Campaign and Social-Engineering Annotation Extension (`smish`)

Candidate local extension for analytic campaign clusters, BERTopic topic
keywords, and psychological-factor / persuasion-technique annotations on
SMS phishing (smishing) messages, as produced by the
[SmishViz CASE/UCO](https://github.com/varnicm/smishviz-case-uco) research
pipeline.

This extension intentionally does **not** re-declare message text, URL
strings, domain names, or impersonation links. Those use canonical CASE/UCO
facets and `uco-core:Relationship`.

## Contents

| File | Purpose |
|---|---|
| `smishviz.ttl` | OWL T-Box: `CampaignCluster`, `CampaignSubcluster`, `Keyword`, `PsychologicalFactor`, `PersuasionTechnique`, and six object properties |
| `smishviz-shapes.ttl` | SHACL shapes (names, IRI node kinds, cluster hierarchy, max three keywords) |
| `smishviz-exemplar.ttl` | A-Box exemplar: SMS + MessageFacet + URL/Domain facets + Relationships + SmishViz annotations |
| `manifest.json` | Extension registration for the CASE-UCO-SDK generator and validator |

## Design

- Every class subclasses `uco-core:UcoObject`.
- `CampaignCluster` / `CampaignSubcluster` are **ML-derived analytic partitions**, not confirmed adversary operations.
- `PersuasionTechnique` is a vocabulary label, not a subclass of `uco-action:Technique`.
- Message content uses `MessageFacet.messageText` / `messageID`.
- URLs use `URLFacet.fullValue` and `URLFacet.host` → `DomainName`.
- Domains use `DomainNameFacet.value`.
- Message→URL / Message→Domain / Message→Organization use
  `uco-core:Relationship` with `kindOfRelationship` `Contains`,
  `References`, and `Impersonates`.

## Mapping from the current SmishViz repository vocabulary

| Current SmishViz term | Target |
|---|---|
| `smish:CampaignCluster` | Keep (now `rdfs:subClassOf uco-core:UcoObject`) |
| `smish:CampaignSubcluster` | Keep (now subclass + required `partOfCluster`) |
| `smish:Keyword` | Keep |
| `smish:PsychologicalFactor` | Keep |
| `smish:PersuasionTechnique` | Keep |
| `smish:belongsToCluster` / `belongsToSubcluster` / `partOfCluster` | Keep |
| `smish:hasKeyword` / `hasPsychologicalFactor` / `hasPersuasionTechnique` | Keep |
| `smish:messageText` / `messageIdentifier` | `MessageFacet.messageText` / `messageID` |
| `smish:fullText` | `uco-core:description` |
| `smish:urlValue` | `URLFacet.fullValue` |
| `smish:domainValue` | `DomainNameFacet.value` |
| `smish:hasDomain` | `URLFacet.host` |
| `smish:containsURL` | `Relationship` `Contains` |
| `smish:referencesDomain` | `Relationship` `References` |
| `smish:impersonates` | `Relationship` `Impersonates` |

## Validation

```bash
case_validate --built-version case-1.5.0 \
  --ontology-graph extensions/smishviz/smishviz.ttl \
  --ontology-graph extensions/smishviz/smishviz-shapes.ttl \
  --inference rdfs --allow-info \
  extensions/smishviz/smishviz-exemplar.ttl
```

Or via the MCP tool: `validate_graph(path, extensions=["smishviz"])`.

Compatibility / playground:

```bash
make test-extension-compat \
  EXT_TTL=extensions/smishviz/smishviz.ttl \
  EXT_SHAPES=extensions/smishviz/smishviz-shapes.ttl \
  EXT_DATA=extensions/smishviz/smishviz-exemplar.ttl

# Note: the SDK playground-test target currently injects OWL + SHACL only.
# After clone, also copy the exemplar before `make -j check`:
#   cp extensions/smishviz/smishviz-exemplar.ttl \
#      .playground-test/tests/exemplars.ttl
make playground-test \
  EXT_OWL=extensions/smishviz/smishviz.ttl \
  EXT_SHAPES=extensions/smishviz/smishviz-shapes.ttl
```

## Status

Candidate local extension authored for adoption by
[varnicm/smishviz-case-uco](https://github.com/varnicm/smishviz-case-uco).
Namespace `https://reactlab.org/smishviz/ontology/` matches the upstream
SmishViz repository. Not yet proposed as a core CASE/UCO change — these
concepts are research-corpus-specific and belong in an extension.
