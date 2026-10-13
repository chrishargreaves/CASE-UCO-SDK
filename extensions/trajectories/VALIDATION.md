# Trajectories extension — validation log

Date: 2026-10-12 (v1.31.0; re-validated after porting
[PR #135](https://github.com/vulnmaster/CASE-UCO-SDK/pull/135):
`PhaseAssertion ⊆ uco-core:Assertion`, `StateMachineModel ⊆
uco-analysis:AnalyticResult`, five single-rule invalid fixtures, three
competency queries). Sections not re-run keep their recorded date.
Status: `candidate`

True green paths below. Upper shapes (`sh-time`, `sh-prov-o`, optional `sh-gufo`) load via the SDK profile bundle when `profiles` is set — not via ad-hoc TTL alone.

`trajectories-exemplar.ttl` uses neither `traj:enactsAction` nor `traj:initialState` (0 / 0). `trajectories-elder-fraud-exemplar.ttl` is now **synthetic** (fictional Victim V and Courier C; it replaced an exemplar built from a real federal case) and exercises each once (1 / 1). The three ESM domain exemplars (`elder-fraud`, `extortion`, `trafficking`) exercise v0.3.0 most fully and are included in this log.

---

## Primary: SDK `case_uco.validation` (strict coverage)

Public API since v1.22.1 (`python/case_uco/validation/`). The
`mcp_server/graph_validator` module remains a thin re-export for MCP/critic
compatibility, but extension docs should import the package.

```bash
export PATH="$PWD/.venv/bin:$PATH"
export PYTHONPATH="$PWD/python${PYTHONPATH:+:$PYTHONPATH}"
python3 <<'PY'
from case_uco.validation import validate_graph_file

def check(path, extensions, profiles=("time", "prov-o")):
    r = validate_graph_file(
        path,
        extensions=extensions,
        profiles=list(profiles),
        strict_concepts=True,
        force_rdfs_inference=True,
    )
    stages = dict(r.stage_status)
    print(path.split("/")[-1], "conforms=", r.conforms,
          "coverage=", stages.get("coverage_conformance"),
          "shacl=", stages.get("shacl_conformance"),
          "viol=", r.violation_count)

for p in (
    "extensions/trajectories/trajectories-exemplar.ttl",
    "extensions/trajectories/trajectories-elder-fraud-exemplar.ttl",
):
    check(p, ["trajectories"])
    check(p, ["trajectories"], profiles=("time", "prov-o", "gufo"))

check("extensions/trajectories/trajectories-invalid-exemplar.ttl", ["trajectories"])

for p, ext in (
    ("extensions/elder-fraud/elder-fraud-exemplar.ttl", "elder-fraud"),
    ("extensions/extortion/extortion-exemplar.ttl", "extortion"),
    ("extensions/trafficking/trafficking-exemplar.ttl", "trafficking"),
):
    check(p, [ext])
    check(p, [ext], profiles=("time", "prov-o", "gufo"))
PY
```

### Recorded results (re-verified 2026-10-12, case-utils 0.18.0, UCO/CASE 1.5.0)

| Artifact | profiles | Conforms | coverage | SHACL | `enactsAction`/`initialState` uses |
|---|---|---|---|---|---|
| `trajectories-exemplar.ttl` | time, prov-o | **True** | ok | conforms | 0 / 0 — does not exercise v0.3.0 |
| `trajectories-exemplar.ttl` | time, prov-o, gufo | **True** | ok | conforms | 0 / 0 |
| `trajectories-elder-fraud-exemplar.ttl` | time, prov-o | **True** | ok | conforms | 1 / 1 |
| `trajectories-elder-fraud-exemplar.ttl` | time, prov-o, gufo | **True** | ok | conforms | 1 / 1 |
| `trajectories-invalid-exemplar.ttl` | time, prov-o (and + gufo) | **False** | ok | nonconformant | firewall/missing-prop fixture |
| `trajectories-invalid-{probability,interval,sequence-index,terminal,estimate-membership}.ttl` | time, prov-o (and + gufo) | **False** | ok | nonconformant | one rule each; see Invalid fixtures |
| `elder-fraud-exemplar.ttl` | time, prov-o | **True** | ok | conforms | 8 / 1 |
| `elder-fraud-exemplar.ttl` | time, prov-o, gufo | **True** | ok | conforms | 8 / 1 |
| `extortion-exemplar.ttl` | time, prov-o | **True** | ok | conforms | 2 / 1 |
| `extortion-exemplar.ttl` | time, prov-o, gufo | **True** | ok | conforms | 2 / 1 |
| `trafficking-exemplar.ttl` | time, prov-o | **True** | ok | conforms | 3 / 1 |
| `trafficking-exemplar.ttl` | time, prov-o, gufo | **True** | ok | conforms | 3 / 1 |

Invalid exemplar expected messages include:

- `Every PhaseAssertion MUST cite >=1 evidence node via prov:wasDerivedFrom.`
- Missing `assertsState` / `atInterval` / `sequenceIndex` on dual-typed model
- Missing `uco-core:ConfidenceFacet` via `hasFacet`
- `traj:StateMachineModel is an INFERRED analytic artifact.`

Without `profiles=['time','prov-o']`, coverage fails closed on `profile_not_selected` for `time:*` / `prov:*` even if SHACL alone would pass.

---

## Critic: deterministic pass (offline)

```bash
export PATH="$PWD/.venv/bin:$PATH"
python3 <<'PY'
import sys
from pathlib import Path
sys.path.insert(0, "mcp_server")
from critic.models import CriticArtifactRequest
from critic.deterministic import analyze_artifact

for label, path, exts in [
    ("cac", "extensions/trajectories/trajectories-exemplar.ttl", ["trajectories"]),
    ("elder-base", "extensions/trajectories/trajectories-elder-fraud-exemplar.ttl", ["trajectories"]),
    ("elder-fraud-ext", "extensions/elder-fraud/elder-fraud-exemplar.ttl", ["elder-fraud"]),
    ("extortion-ext", "extensions/extortion/extortion-exemplar.ttl", ["extortion"]),
    ("trafficking-ext", "extensions/trafficking/trafficking-exemplar.ttl", ["trafficking"]),
]:
    req = CriticArtifactRequest(
        graph_path=str(Path(path).resolve()),
        critic_scope="graph",
        extensions=exts,
        profiles=["time", "prov-o"],
        force_rdfs_inference=True,
    )
    review = analyze_artifact(req)
    print(label, "status=", review.status,
          "findings=", len(review.deterministic_findings or []))
PY
```

### Recorded results

| Exemplar | status | deterministic findings |
|---|---|---|
| CAC grooming (base) | `deterministic_clean` | `[]` |
| Elder-fraud (base, non-CAC) | `deterministic_clean` | `[]` |
| `elder-fraud` extension | `deterministic_clean` | `[]` |
| `extortion` extension | `deterministic_clean` | `[]` |
| `trafficking` extension | `deterministic_clean` | `[]` |

---

## Secondary: `case_validate` CLI (caveat)

```bash
.venv/bin/case_validate --built-version case-1.5.0 \
  --ontology-graph extensions/trajectories/trajectories.ttl \
  --ontology-graph extensions/trajectories/trajectories-shapes.ttl \
  --ontology-graph ontology/upper/time.ttl \
  --ontology-graph ontology/upper/prov-o.ttl \
  --inference rdfs --allow-info \
  extensions/trajectories/<exemplar>.ttl
```

**What this loads**

| Layer | Loaded? |
|---|---|
| traj OWL + SHACL | Yes (`--ontology-graph`) |
| UCO/CASE shapes | Yes (`--built-version case-1.5.0`) |
| `ontology/upper/shapes/sh-time.ttl`, `sh-prov-o.ttl` | **No** |
| Strict concept coverage / profile selection | **No** |

Use the SDK primary path above for PR-grade "green." CLI alone can report SHACL conformant while the SDK still fails coverage.

---

## Mutations (a–d) — base observed/inferred firewall

Mutations written under `/tmp`, validated with the same CLI base as above (`rdfs` ON). Against the base CAC exemplar; unrelated to v0.3.0. All must fail.

| Mutation | Change | Result |
|---|---|---|
| (a) | Drop `prov:wasDerivedFrom` on first `PhaseAssertion` | Conforms **False** — missing evidence provenance |
| (b) | Drop `uco-core:hasFacet` ConfidenceFacet link | Conforms **False** — missing ConfidenceFacet |
| (c) | Dual-type `StateMachineModel` as also `PhaseAssertion` | Conforms **False** — firewall / missing required props |
| (d) | `Trajectory hasPhaseAssertion` → a `TransitionEstimate` | Conforms **False** — `sh:class` on hasPhaseAssertion |

## Mutations (e–g) — v0.3.0 `enactsAction` / `initialState` (new)

Mutations written under the scratch dir, validated via the SDK primary path
(`extensions=["elder-fraud"]`, `profiles=["time","prov-o"]`,
`force_rdfs_inference=True`) against `elder-fraud-exemplar.ttl`.

| Mutation | Change | Expected | Actual | Result |
|---|---|---|---|---|
| (e) | `transition-1 traj:enactsAction` retargeted from `cg:action-spoofed-opener-call` to `cg:person-castanos-garcia` (a `Person`, not an `Action`) | Conforms **False** (`sh:class uco-action:Action`) | Conforms **False**, 1 violation | Fails as expected (fixed in v1.24.0 — see below) |
| (f) | `transition-4` given an `enactsAction` value that is a `Person` (`cg:person-nunez-nunez`) in addition to its two valid Action values | Conforms **False** (`sh:class` rejects the Person value); cardinality no longer rejects multi-valued `enactsAction` | Conforms **False**, 1 violation | Fails on the bad value only — multi-action edges remain first-class |
| (g) | `cg:model` given two `traj:initialState` values (`ef:InitialContact` and `ef:Conditioning`) | Conforms **False** (`sh:maxCount 1`) | Conforms **False**, 1 violation | Fails as expected |

**Note on (f) history:** Prior to allowing multi-valued `traj:enactsAction`, mutation (f) was "two `enactsAction` on `transition-4`" and was expected to fail `sh:maxCount 1`. That constraint was lifted so ESM multi-action edges (`a_spoof`+`a_script`+`a_secrecy`, `a_fakeid`+`a_deposit`) validate.

**History of (e) and (f) — fixed in v1.24.0.** Both mutations previously
passed validation when they should have failed. `traj:enactsAction` carried
`rdfs:range uco-action:Action`, and under `force_rdfs_inference=True` RDFS
range entailment infers `?o a uco-action:Action` for *any* value of an
`enactsAction` triple, whatever its asserted type. The `sh:class` check was
therefore satisfied by construction and could not reject anything.

The range was removed. `sh:class uco-action:Action` is now the only type
constraint on the property and it evaluates against asserted types, so both
mutations fail as intended. Three sibling properties — `hasPhaseAssertion`,
`learnedFrom`, `hasTransitionEstimate` — had the same defect and were fixed
the same way.

`fromState`, `toState`, `assertsState` and `initialState` deliberately keep
their ranges: their values are phase-vocabulary individuals declared in a
domain extension's *ontology* graph, and `case_validate` does not merge
`--ontology-graph` type assertions into the data graph, so removing the range
makes `sh:class` fail on every valid exemplar. Constraining those usefully
needs a vocabulary-membership check (`sh:in`, or `skos:inScheme`) rather than
`sh:class`. See the commentary at the head of the object-property section in
`trajectories.ttl`.

Mutation (g) exercises `sh:maxCount 1` on `traj:initialState` and has always
caught that cardinality violation correctly.

---

## Focus-node non-vacuity (all valid exemplars, current working tree)

| Shape target | CAC (base) | Elder (base, non-CAC) | Invalid | `elder-fraud` ext | `extortion` ext | `trafficking` ext |
|---|---|---|---|---|---|---|
| PhaseAssertion | 4 | 4 | 2 | 8 | 4 | 4 |
| Trajectory | 1 | 1 | 1 | 2 | 1 | 1 |
| Transition | 3 | 3 | 1 | 5 | 3 | 3 |
| StateMachineModel | 1 | 1 | 1 | 1 | 1 | 1 |
| TransitionEstimate | 3 | 2 | 1 | 5 | 3 | 3 |

All nonzero on the valid exemplars.

`traj:enactsAction` / `traj:initialState` triple counts (direct count, not
shape-target count — confirms which artifacts actually exercise v0.3.0):

| Artifact | `enactsAction` uses | `initialState` uses |
|---|---|---|
| `trajectories-exemplar.ttl` (base) | 0 | 0 |
| `trajectories-elder-fraud-exemplar.ttl` (base) | 0 | 0 |
| `trajectories-invalid-exemplar.ttl` | 0 | 0 |
| `elder-fraud-exemplar.ttl` | 8 | 1 |
| `extortion-exemplar.ttl` | 2 | 1 |
| `trafficking-exemplar.ttl` | 3 | 1 |

(`elder-fraud` has five transitions and eight `enactsAction` triples:
`InitialContact -> Conditioning` has three (`a_spoof`/`a_script`/`a_secrecy`);
`Conditioning -> ExtractionInstruction` has one (`a_direct`);
`ExtractionInstruction -> ProceedsCollection` has one (`a_coopt`);
`ProceedsCollection -> Laundering` has two (`a_fakeid`/`a_deposit`);
`Laundering -> Completed` has one (`a_transmit`) — 3+1+1+2+1 = 8.
`extortion` omits `enactsAction` on one transition by design. See each
domain's README.)

---

## Regression: existing SDK test suite

```bash
export PATH="$PWD/.venv/bin:$PATH"
export PYTHONPATH="$PWD/python:$PWD/mcp_server${PYTHONPATH:+:$PYTHONPATH}"
.venv/bin/python -m pytest -q \
  mcp_server/tests/test_extension_paths.py \
  python/tests/test_extension_bundle_contract.py \
  python/tests/test_validation_api.py \
  python/tests/test_darkwatchman_release.py \
  python/tests/test_attack_catalog_coverage.py
```

Result (2026-07-19): **16 passed**, 0 failed.

---

## `make validate-extension` — standard gate (2026-10-12)

`scripts/validate_extension.py` runs `case_validate` with the manifest's
OWL/SHACL/bridge files and no extra flags. Both shipped exemplars use
`urn:uuid:…` instance IRIs.

| DATA | Result |
|---|---|
| `trajectories-exemplar.ttl` | `Conforms: True`, exit 0 |
| `trajectories-elder-fraud-exemplar.ttl` | `Conforms: True`, exit 0 |

---

## Invalid fixtures

`mcp_server/tests/test_trajectories.py` runs every fixture with `pyshacl`
(`inference=rdfs`, ontology `trajectories.ttl`, shapes
`trajectories-shapes.ttl`); the SDK path above fails each one too.

| Fixture | Rule under test | Why it fails |
|---|---|---|
| `trajectories-invalid-exemplar.ttl` | Observed≠inferred firewall + required observed-layer props | Dual-typed model/assertion; missing `wasDerivedFrom`, `ConfidenceFacet`, `assertsState`, `atInterval`, `sequenceIndex` |
| `trajectories-invalid-probability.ttl` | `traj:transitionProbability` in `[0, 1]` | `sh:maxInclusive` — value `1.5` |
| `trajectories-invalid-interval.ttl` | `traj:atInterval` is a `time:ProperInterval` | `sh:class` — value is a `uco-identity:Person` |
| `trajectories-invalid-sequence-index.ttl` | Unique `sequenceIndex` per Trajectory | SPARQL — two assertions share index `0` |
| `trajectories-invalid-terminal.ttl` | At most one `isTerminal true` per Trajectory | SPARQL "at most one terminal" (also "terminal has the max `sequenceIndex`") |
| `trajectories-invalid-estimate-membership.ttl` | Estimate `ofTransition` is among the model's `hasTransition` | SPARQL — estimate points at an undeclared transition |

Two rules stay advisory and are not enforced: dense/consecutive
`sequenceIndex` numbering (the OWL comment allows zero- or one-based
numbering) and exactly one terminal (marking a terminal is optional).

---

## Competency SPARQL queries

Declared in `manifest.json` `competency_queries`; run as raw A-Box (no
inference). Row counts recorded 2026-10-12:

| Query | Proves | CAC | Elder |
|---|---|---|---|
| `queries/observed-occupancy-chain.sparql` | Trajectory → PhaseAssertion → state + interval + `prov:wasDerivedFrom` | 4 rows | 4 rows |
| `queries/inference-provenance.sparql` | `StateMachineModel` (an `AnalyticResult`) `learnedFrom` a Trajectory, `wasGeneratedBy` an `Analysis` whose `instrument` is a `Tool` | 4 rows | 4 rows |
| `queries/observed-inferred-firewall.sparql` | No PhaseAssertion typed `AnalyticResult`; every `StateMachineModel` typed `AnalyticResult`; no dual-typed node | 0 rows (expected empty) | 0 rows (expected empty) |

---

## Deferred

- Language bindings under `packages/case-uco-trajectories/`
- Init of `ontology/aeo/ontology` (git submodule not checked out in this
  working environment — confirmed unrelated to this branch: `ONTOLOGY_REFERENCE.md`
  entries for `trajectories`/`elder-fraud`/`extortion`/`trafficking` were
  added via targeted splice rather than a full `case-uco-generate generate`
  run, specifically to avoid dropping the existing `ext.aeo.*` sections that
  a full regen in this environment would silently lose)
