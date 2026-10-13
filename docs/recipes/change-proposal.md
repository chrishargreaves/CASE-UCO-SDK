# Proposing Changes to CASE/UCO

> See [Recipe Index](INDEX.md) for all recipes.

When the CASE/UCO ontology doesn't have a class, facet, or property for the concept you need to model, you can draft a **change proposal** — a structured request for the ontology committees to consider adding or modifying a concept in a future specification release.

This recipe covers the full workflow: confirming the gap, checking for existing proposals, choosing the target tracker and release, drafting a competency-question proposal that marks where each statement came from, testing optional draft classes, and creating a local extension to unblock your work.

## When to use this recipe

- **Explicit request**: You know you need a concept that doesn't exist (e.g., "there's no facet for drone telemetry data")
- **Gap detected during modeling**: `search_classes` and `find_classes_for_domain` return no adequate match for what you're trying to model
- **Agent-suggested**: While helping model data, the agent identifies that no existing class covers the concept and proactively suggests drafting a proposal
- **Rejected by concept coverage**: `validate_graph` returned `conforms: False` with an `undeclared_concepts` list — the graph uses a class or property that no supported ontology declares. Do not invent terms or disable the check; file a proposal (this recipe) and/or declare the term in an extension ontology ([extensions recipe](extensions.md)) so validation passes.

## Which tracker?

| Concept namespace | Target repository |
|---|---|
| `uco-*` (general cyber-domain) | [ucoProject/UCO](https://github.com/ucoProject/UCO/issues) |
| `case-*` (investigation-specific) | [casework/CASE](https://github.com/casework/CASE/issues) |
| `cacontology*` (crimes against children) | [Project-VIC-International/CAC-Ontology](https://github.com/Project-VIC-International/CAC-Ontology/issues) |

`check_existing_proposals` searches all three by default. Precedent CAC proposals filed from this SDK: [#40](https://github.com/Project-VIC-International/CAC-Ontology/issues/40) (legal-outcomes charging/sentencing properties) and [#41](https://github.com/Project-VIC-International/CAC-Ontology/issues/41) (core case-identification properties) — both backed locally by `ontology/cac/local/cacontology-sdk-pending.ttl` until they land upstream.

## Key tools

| Tool | Role |
|---|---|
| `search_classes` | Verify the gap — search by keyword to confirm no existing class fits |
| `get_class_details` | Inspect near-matches to confirm they don't cover the concept |
| `find_classes_for_domain` | Check if the concept is already mapped under a different name |
| `check_existing_proposals` | Search open GitHub issues in UCO, CASE, and the CAC Ontology for prior proposals |
| `draft_change_proposal` | Draft the competency-question proposal, its review notes, and optional companion test files |

---

## Step 1: Confirm the gap

Before drafting a proposal, thoroughly verify that no existing class covers the concept. Near-misses are common — the ontology may model the concept under a different name or as a property on an existing class.

<details open><summary>Python — confirming a gap</summary>

```python
from case_uco.registry import search, get_class

# Search by several keywords related to the concept
results = search("drone")
print(f"Found {len(results)} results for 'drone'")
for r in results:
    print(f"  {r['name']:30s} {r['module']}")

# Try related terms
for term in ["uav", "unmanned", "aerial", "flight", "telemetry"]:
    hits = search(term)
    if hits:
        print(f"\n'{term}' matched:")
        for h in hits:
            print(f"  {h['name']:30s} {h['module']}")

# Inspect near-matches in detail
info = get_class("DeviceFacet")
print(f"\nDeviceFacet properties:")
for prop in info["properties"]:
    print(f"  {prop['name']:20s} {prop['type']}")
```

</details>

<details><summary>MCP — confirming a gap</summary>

```
1. search_classes("drone")          → no results
2. search_classes("uav")            → no results
3. search_classes("telemetry")      → no results
4. find_classes_for_domain("drone forensics")  → no task templates
5. get_class_details("DeviceFacet") → review properties, confirm none cover flight data
```

The gap is confirmed: no existing class models UAV/drone-specific telemetry data.

</details>

---

## Step 2: Check existing proposals

**This step is critical for proposal quality.** Before drafting a new proposal, search the open issues in the UCO, CASE, and CAC Ontology repositories. Someone may have already proposed the concept, or a related proposal may be in progress. Finding related issues provides essential context — for example, discovering a prerequisite proposal (like UCO #535 "Add Qualities") can change the entire design of your proposal.

<details open><summary>MCP — checking existing proposals</summary>

```
check_existing_proposals("drone telemetry")
```

Possible outcomes:

- **Exact match found**: "UCO Issue #700 proposes a DroneTelemetryFacet — consider commenting on that issue instead of creating a duplicate."
- **Partial match found**: "CASE Issue #190 discusses aerial surveillance evidence, which overlaps with drone telemetry. Your proposal should reference it."
- **No match found**: Proceed to Step 3.
- **GitHub unavailable**: Proceed with local drafting, but search the issue trackers manually before submitting: [UCO issues](https://github.com/ucoProject/UCO/issues), [CASE issues](https://github.com/casework/CASE/issues), [CAC Ontology issues](https://github.com/Project-VIC-International/CAC-Ontology/issues).

</details>

---

## Step 3: Determine the target tracker and release

### Target repository

The concept's scope determines which tracker receives the proposal:

| Scope | Target | Repository | Examples |
|---|---|---|---|
| General cyber-observable, identity, action, or data structure with utility beyond investigation | **UCO** | [ucoProject/UCO](https://github.com/ucoProject/UCO/issues/new) | New device facet, new observable type, new action property |
| Specific to the investigation process itself | **CASE** | [casework/CASE](https://github.com/casework/CASE/issues/new) | New investigator role, new case metadata, investigation workflow concepts |
| Specific to crimes-against-children investigations | **CAC** | [Project-VIC-International/CAC-Ontology](https://github.com/Project-VIC-International/CAC-Ontology/issues/new) | Grooming stages, NCMEC CyberTip fields, CSAM provenance |

**Decision logic:**

1. Is the concept specific to crimes-against-children investigations? **CAC**, unless it is useful outside that domain.
2. Is it specific to the process of conducting an investigation (roles, exhibits, authorization, case metadata, investigative workflows)? **CASE**.
3. Is it a general cyber-observable, identity, tool, action, location, or data structure with utility across the cyber domain? **UCO**.
4. **Unsure?** Ask the developer. `draft_change_proposal` triages from the concept and description, and reports `target_repo_unresolved` when it cannot tell.

### Target release

Every change proposal names a suggested release. Check the current state of the CASE/UCO branches:

| Branch | Version | When to target |
|--------|---------|----------------|
| `main` | 1.5.0 | Released. CASE and UCO 1.5.0 both shipped; nothing new targets this. |
| `develop` | next backward-compatible release | Default for most proposals. Changes that are backward-compatible additions. |
| `develop-2.0.0` | 2.0.0 | For proposals that require breaking changes or major restructuring. |

If unsure, target `develop`. Read the version off the branch rather than
assuming it — after the 1.5.0 release `develop` still carried
`owl:versionIRI core:1.5.0`, so the next minor had not been opened yet:

```bash
git -C ontology/UCO show origin/develop:ontology/uco/core/core.ttl | grep versionIRI
```

The CAC Ontology versions independently; without a `target_release`, a CAC
proposal suggests "the next CAC Ontology release". The committee may
reassign any proposal to a different milestone during review.

---

## Step 4: Draft the proposal

A proposal is a **discussion draft built around competency questions**. It
asks what a graph should be able to answer, cites where each idea came from,
and leaves the ontology design to the committee. This keeps it short and
easy for ontologists to respond to. The format follows the
[change proposal template](../templates/change-proposal-template.md):

- **Header**: title and target repository as HTML comments, then a visible
  suggested release and a contributor line that discloses the AI assistance
  and names the model.
- **Background**: why the change is needed.
- **Competency questions**: a concrete scenario, then each question with its
  expected answer.
- **Requirements**: the terms the questions need, each with a sourced
  definition and what it might connect to.
- **Open questions**: where input is most wanted.
- **Related issues and references**.
- A collapsed **Committee section** (benefits and risks, proposed ontology
  changes, CQ queries and example data, review checklist) left for review.

### Mark where every statement came from

Each statement is one of three kinds, and the proposal shows which:

| Provenance | Rendered | Use for |
|---|---|---|
| `contributor` | unmarked | Text the contributor wrote or approved in the conversation |
| `cited` | `*[from [label](url)]*` | A quote or paraphrase of a person or publication. The URL must be the exact comment or page quoted; for a GitHub comment, its `#issuecomment-` link |
| `ai` | `*[AI-drafted]*` | Text an AI assistant wrote. Plain strings default to this |

An agent must never mark its own text as the contributor's. When the
contributor rewrites or approves an AI-drafted statement, redraft with
`provenance="contributor"`.

<details open><summary>MCP — drafting a proposal</summary>

```
draft_change_proposal(
    concept="Drone telemetry",
    title="Representing drone flight telemetry",
    target_repo="UCO",
    contributor="Jane Examiner (@jexaminer)",
    ai_model="<the model drafting with you>",
    description=[
        {"text": "Our lab extracts DJI flight logs in most drone cases and has "
                 "nowhere to put altitude, speed, and home point.",
         "provenance": "contributor"},
    ],
    scenario="A drone seized near a prison holds a flight log with 412 points "
             "over 18 minutes, including a hover over the yard.",
    competency_questions=[
        {"question": "Where was the drone, and at what altitude, at a given time?",
         "expected_answer": "The logged point nearest that time, with its "
                            "latitude, longitude, and altitude above takeoff."},
        {"question": "Which flights hovered over a given area for over a minute?",
         "expected_answer": "The one flight with the 74-second hover over the yard."},
    ],
    terms=[
        {"name": "Observation", "vocabulary": "SOSA",
         "concept_url": "https://www.w3.org/TR/vocab-ssn/#SOSAObservation",
         "definition": {"text": "\"Act of carrying out an (Observation) Procedure "
                                "to estimate or calculate a value of a property "
                                "of a FeatureOfInterest.\"",
                        "source_label": "W3C SOSA/SSN",
                        "source_url": "https://www.w3.org/TR/vocab-ssn/#SOSAObservation"},
         "might_connect_to": "One telemetry point in the flight log"},
    ],
    open_questions=[
        "Should UCO reuse SOSA observations through a profile, or define its own "
        "telemetry facet aligned to them?",
    ],
    references=[{"label": "W3C SOSA/SSN", "url": "https://www.w3.org/TR/vocab-ssn/"}],
)
```

The tool writes to `change_proposals/` (or `output_dir`):

- `<slug>.md`: the issue body.
- `<slug>.review.md`: lint findings and a hand-check list for the
  contributor. Not filed.
- Companion test files, only when `proposed_classes` or
  `proposed_properties` are given (Step 5).

</details>

### Lint and the review notes

The result carries `lint` findings and `ready_to_file` (no errors). The
review notes list the same findings plus the checks a person has to make.

| Code | Severity | What it catches |
|---|---|---|
| `contributor_missing` | error | No contributor; a person must own the proposal |
| `ai_model_unspecified` | warning | The AI disclosure does not name the model |
| `no_competency_questions`, `cq_missing_expected_answer` | error | The proposal has nothing testable for the committee to respond to |
| `citation_missing_url` | error | A `*[from …]*` tag that does not link what it quotes |
| `citation_link_not_comment` | info | A person is cited with an issue link rather than the comment quoted |
| `vocabulary_claim_unlinked` | error | A term attributed to an outside vocabulary with no `concept_url` |
| `vocabulary_term_unlinked` | warning | Text names a backticked term from an outside vocabulary without a link |
| `ontology_term_not_found` | error | A CASE/UCO (or CAC) term that the pinned ontology does not declare, the usual sign of a hallucinated term |
| `parent_class_undeclared` | error | A draft class whose parent does not exist |
| `avoid_standard_wording` | warning | "Standard", which implies a standards development organization |
| `exclusionary_phrasing` | warning | Statements about who is or is not in the community; describe who drafted the proposal instead ("This proposal was not posted or drafted by a lawyer.") |
| `endorsement_wording` | warning | "Lead", "endorse", and similar wording that ranks sources |

Wording rules skip `cited` statements, since a quote cannot be reworded.

<!-- recipe-lint: ignore-start anti-pattern -- The terms below are examples of hallucinated CASE/UCO terms that ontology_term_not_found rejects. -->
For example, a draft that says an action is `uco-core:initiatedBy` its actor, or
gives a person a `uco-core:role`, fails with `ontology_term_not_found`: neither
term exists in UCO 1.5.0.
<!-- recipe-lint: ignore-end anti-pattern -->

The hand checks cannot be automated. They ask the contributor to:

- open every outside link and confirm it resolves and says what the
  statement claims;
- confirm each `*[from …]*` tag links the exact comment or page quoted;
- read every AI-drafted statement and keep, rewrite, or delete it;
- check that no single jurisdiction or locale is treated as the default;
- check that things that should be objects (statutes, people, roles) are not
  stood in for by strings, and that roles are kept distinct from the people
  who hold them;
- check that sources are not circular;
- check that existing vocabularies (SOSA/SSN, PROV-O, schema.org) were
  considered before new terms.

`verify_links=True` fetches each outside link and reports whether a quoted
definition appears on the page. It helps, but a page can resolve and still
say something different, so the hand checks stand.

---

## Step 5: Companion test files (optional)

The issue body leaves the design to the committee. A contributor who already
has draft classes passes them as `proposed_classes` (`name`, `parent`,
`description`, `properties: [{name, type, description}]`) or
`proposed_properties` (`name`, `target_class`, `type`). The tool writes local
files for testing:

| File | Contents |
|---|---|
| `<slug>.ttl` | `owl:Class` with `rdfs:subClassOf`, label, and comment for each class; `owl:DatatypeProperty` or `owl:ObjectProperty` with `rdfs:range` |
| `<slug>-shapes.ttl` | SHACL node shapes for the proposed properties, kept apart from the OWL |
| `<slug>.jsonld` | Example data. A Facet subclass hangs off an `ObservableObject` through `uco-core:hasFacet`; any other class is a top-level node. Every node has an `@id`, and object-range properties point at a typed node |
| `<slug>.sparql` | The competency questions' `sparql` when given, otherwise one query per draft class |

With `run_tests=True` (the default), the tool validates the example with
`case_validate` (RDFS inference, the companion ontology and shapes loaded,
strict concept coverage) and runs the SPARQL. The results go in the review
notes. Set `include_design_sketch=True` to list the draft classes in the
committee section as an AI-drafted sketch; by default it stays a placeholder.

Expand the example with realistic data that exercises every draft class and
property and supports the competency questions.

---

## Step 6: Test

```bash
make test-proposal PROPOSAL=drone-telemetry
```

This runs two checks:

1. **Graph validation** — validates the example `.jsonld` against CASE/UCO 1.5.0 using `case_validate` with `--inference rdfs --allow-info`. The companion `.ttl` and `-shapes.ttl` are included via `--ontology-graph` when present.
2. **SPARQL query testing** — executes each query in the `.sparql` file against the example graph and reports whether results were returned.

### Understanding validation flags

- **`--inference rdfs`** — Required when proposed classes are `rdfs:subClassOf` existing UCO/CASE classes (e.g., Facet, UcoObject). Without this, SHACL cannot infer that the proposed facet satisfies the `sh:class uco-core:Facet` constraint.
- **`--allow-info`** — Allows informational results (UUID IRI suggestions, vocabulary hints) without causing a non-zero exit code.
- **`--ontology-graph <slug>.ttl`** — Declares the proposed classes so the validator knows their type hierarchy.

### Common validation failures and fixes

| Failure | Cause | Fix |
|---------|-------|-----|
| `NodeKindConstraintComponent: Value is not of Node Kind sh:IRI` | Facet objects are blank nodes (missing `@id`) | Give each facet an `@id` |
| `ClassConstraintComponent: Value does not have class uco-core:Facet` | No `.ttl` declaring `rdfs:subClassOf` | Keep the generated `<slug>.ttl` beside the `.jsonld` |
| A required property is missing | The parent class's SHACL shape requires it (for example `uco-core:Relationship`) | Add the property to the example |

### Test extensions against multiple CASE/UCO branches

```bash
# Test against all three branches: main (v1.5.0), develop, develop-2.0.0 (v2.0.0)
make test-extension-compat \
  EXT_TTL=change_proposals/drone-telemetry.ttl \
  EXT_SHAPES=change_proposals/drone-telemetry-shapes.ttl \
  EXT_DATA=change_proposals/drone-telemetry.jsonld
```

---

## Step 7: Create a local extension (optional)

If you need typed classes immediately rather than raw JSON-LD, create a local extension ontology and scaffold typed classes. See the [Working with Extensions](extensions.md) recipe for the full workflow.

```bash
# After defining your extension TTL files:
case-uco-generate scaffold \
  --extension extensions/proposed/proposed.ttl extensions/proposed/proposed-shapes.ttl \
  --output-dir my_project/
```

When the concept is officially added to CASE/UCO in a future release, retire the local extension and switch to the SDK's built-in class.

---

## Submitting the proposal

Only the contributor files the proposal. Before filing:

1. `ready_to_file` is true: no lint errors remain.
2. The contributor has worked through every hand check in `<slug>.review.md`.
3. Every *[AI-drafted]* statement has been kept, rewritten, or deleted by the contributor.
4. If companion files exist, `make test-proposal PROPOSAL=<slug>` passes.

Then open a new issue in the target tracker and paste the body of `<slug>.md`:

- **UCO**: https://github.com/ucoProject/UCO/issues/new
- **CASE**: https://github.com/casework/CASE/issues/new
- **CAC**: https://github.com/Project-VIC-International/CAC-Ontology/issues/new

Use the title from the first HTML comment. Do not paste the review notes. Offer
the companion files in the discussion if the committee asks for a design.

## Proposal file conventions

```
change_proposals/
├── <slug>.md              # The issue body
├── <slug>.review.md       # Lint findings and hand checks (not filed)
├── <slug>.ttl             # Draft OWL (only with draft classes or properties)
├── <slug>-shapes.ttl      # Draft SHACL shapes
├── <slug>.jsonld          # Example instance data
└── <slug>.sparql          # SPARQL competency queries
```

The Makefile `test-proposal` target looks for these by convention. Only the
`.md` is filed.

## Related

- [extensions.md](extensions.md) — local extension playground while a proposal is pending
- [recipe-authoring.md](recipe-authoring.md) — turn a validated modeling pattern into a catalog recipe
- [otics-scada-intrusion.md](otics-scada-intrusion.md) — ICS/SCADA recipe whose ontology gaps motivate `IndustrialControlDeviceFacet`
