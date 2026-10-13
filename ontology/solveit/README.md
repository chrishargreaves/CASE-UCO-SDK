# SOLVE-IT Extension (bundled)

Pinned, sync-managed snapshot of [SOLVE-IT](https://solveit-df.org) — the
Systematic Objective-based Listing of Various Established digital
Investigation Techniques — comprising the upstream
[solve-it-ontology](https://github.com/SOLVE-IT-DF/solve-it-ontology)
CASE/UCO extension ontology and the compiled RDF knowledge base from
[SOLVE-IT-DF/solve-it](https://github.com/SOLVE-IT-DF/solve-it) (MIT
licensed). Exact pinned versions are recorded in the `provenance` block of
`manifest.json`.

SOLVE-IT organizes digital forensic practice as **objectives** (what the
investigation needs to achieve) → **techniques** (how to achieve it) →
**weaknesses** (what can go wrong, classified per ASTM E3016-18) →
**mitigations** (what reduces the risk), enabling systematic Error
Mitigation Analysis alongside CASE/UCO evidence modeling.

## Contents

| File | Role |
| --- | --- |
| `solve_it_core.ttl` | Objective/Technique/Weakness/Mitigation/Citation classes; `SolveitInvestigativeAction` (subclass of `case-investigation:InvestigativeAction`) with `appliedMitigation`; `usedTechnique` is `owl:deprecated` |
| `solve_it_core_shapes.ttl` | SHACL for the core: a `Technique` must be an `owl:Class` with an `rdfs:subClassOf` and exactly one `techniqueID` |
| `solve_it_observable*.ttl` (4 files) | ~60 forensic observable classes (image containers, bitstreams, timelines, keyword search artifacts, acquisition records, ...) |
| `solve_it_observable_shapes.ttl` | SHACL shapes constraining the observables |
| `solve_it_analysis.ttl` | Hypothesis classes (subclasses of `uco-analysis` types), including `HypothesisedRecord`, `HypothesisedConfiguration`, `HypothesisedTableAttribution` |
| `solve_it_analysis_shapes.ttl` | SHACL for the hypothesis classes |
| `solve_it_sqlite.ttl` | SQLite internals observables |
| `solve_it_tool_profile.ttl` | Tool capability profiles |
| `solve_it_weakness_assessment.ttl` | `WeaknessEvaluation`/`WeaknessEvaluationSet` risk-rating classes |
| `solve-it-kb.ttl` | Compiled knowledge base: 24 objectives, 200 techniques, 441 weaknesses, 336 mitigations, 164 citations. Each technique is an `owl:Class` subclass of `SolveitInvestigativeAction` |
| `solveit-technique-catalog.ttl` | **Generated** UCO bridge: types each knowledge-base technique `uco-action:Technique` with `action:techniqueID`, label and comment, so SOLVE-IT techniques sit under the same UCO metaclass as MITRE ATT&CK and ATLAS; regenerate with `make sync-solveit-offline` |
| `solveit-local-anchors.ttl` | SDK-local bridge anchoring three upstream enumeration classes to `owl:Thing` |
| `solveit-exemplar.ttl` | Validated exemplar (disk imaging with mitigations + weakness evaluation) |
| `solveit-invalid-exemplar.ttl` | Expected-invalid fixture proving the shapes constrain |
| `queries/*.sparql` | Competency queries run by the lifecycle gates |

## Modeling a performed technique

Since SOLVE-IT 0.2.x a technique is a class, and the action that performed
it is an instance of that class (the `uco-action:Technique` metaclass
pattern from UCO 1.5.0):

```turtle
<urn:uuid:...> a solveit-core:SolveitInvestigativeAction , solveit-data:techniqueDFT-1002 ;
    uco-core:name "acquire-laptop-image" ;
    solveit-core:appliedMitigation solveit-data:mitigationDFM-1004 ;
    uco-action:performer <urn:uuid:...> ;
    uco-action:result <urn:uuid:...> .
```

A plain `uco-action:Action` typed with a technique class works too, and
becomes a `SolveitInvestigativeAction` under RDFS inference.

**When a technique is a value** (for example
`solveit-wa:scopedToTechnique`), restate its minimal catalogue entry in
the case graph, as upstream's examples do: `owl:Class`,
`solveit-core:Technique`, `rdfs:subClassOf
solveit-core:SolveitInvestigativeAction`, `rdfs:label`, and
`solveit-core:techniqueID`. The reason is that `case_validate` passes the
knowledge base as an ontology graph, and pySHACL copies only the
class-level triples of `owl:Class` nodes into the data graph, so
`TechniqueShape` can't see the KB's `techniqueID`.
`get_solveit_details` returns the entry as `catalog_entry_jsonld`;
builders can call `solveit_index.technique_catalog_entry("DFT-1002")`.
The same interaction is why the deprecated `usedTechnique` now fails
validation.

The `uco-action:Technique` metaclass ships in UCO 1.5.0, so the manifest
has no dependencies. The MITRE ATT&CK catalog (`attack-technique`) is a
separate vocabulary; request it alongside `solveit` only when a graph also
records observed hacking techniques.

## Usage

```bash
# validate a graph that uses SOLVE-IT terms (KB individuals included)
# via the MCP tool: validate_graph(path, extensions=["solveit"])

# query the knowledge base via MCP
#   search_solveit("disk imaging")
#   get_solveit_details("DFT-1002")
#   plan_solveit_workflow("image the seized laptop and verify integrity")

# load the class registry into discovery tools
CASE_UCO_EXTENSIONS=solveit  # search_classes(scope="solveit")
```

Recipe: `docs/recipes/solve-it-investigation-planning.md`.

## Keeping pace with upstream

Upstream releases monthly (knowledge base) and continuously (ontology).
Refresh the snapshot with:

```bash
make sync-solveit             # pin current upstream main
make sync-solveit REF=<sha>   # pin a specific solve-it-ontology commit
```

The sync tool re-vendors every file, regenerates the technique catalog
bridge, and rewrites manifest provenance (commits, release tag, and
SHA-256 digests of every vendored file). A weekly GitHub Actions check
(`.github/workflows/upstream-freshness.yml`) fails when the pinned snapshot
falls behind the newest upstream release.

There is intentionally no `validation-subset.json`: subset mode skips RDFS
inference, which SOLVE-IT needs so core CASE/UCO shapes apply to its
subclasses. Plain `extensions=["solveit"]` therefore loads the full
manifest (ontology + shapes + catalog + knowledge base).
