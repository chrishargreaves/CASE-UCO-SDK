# Attacks on AI Systems (MITRE ATLAS)

> See [Recipe Index](INDEX.md) for all recipes.

Model an incident or report in which an **AI system is the target**: prompt
injection against an LLM application, a jailbreak, evasion of a detection
model, poisoned training or retrieval data, model extraction or theft, or an
AI agent abused into calling its own tools. Techniques come from
[MITRE ATLAS](https://atlas.mitre.org) (Adversarial Threat Landscape for AI
Systems), vendored complete by the
[`atlas-technique`](../../extensions/atlas-technique/) extension (ATLAS data
release 2026.09: 208 techniques and sub-techniques, 16 tactics).

**Not this recipe:** a case that merely *involves* AI — an offender who uses a
chatbot to write scam messages, AI-generated images, a deepfake voice in an
impersonation call. Those are model-of-the-offense questions; route them by
the offense (for example
[elder-fraud-impersonation.md](elder-fraud-impersonation.md) or the CAC
recipes) and do not add ATLAS techniques unless the evidence shows an attack
*on* an AI system.

Validated against `examples/ai-system-attacks/build_ai_system_attack.py`
(synthetic indirect prompt injection against an LLM email assistant).

## 1. The model: the UCO 1.5.0 Technique metaclass

ATLAS uses the same pattern as MITRE ATT&CK in
[cyber-threat-intelligence.md](cyber-threat-intelligence.md) §5.
`uco-action:Technique` is a metaclass (UCO 1.5.0, from
[ucoProject/UCO PR #676](https://github.com/ucoProject/UCO/pull/676)): *"A
Technique instance is an `owl:Class` that is a subclass of
`uco-action:Action`."* In the catalog:

- each ATLAS technique is an `owl:Class` that is `a uco-action:Technique`,
  carries `uco-action:techniqueID` (`AML.T0051`), and lives under its
  canonical `https://atlas.mitre.org/techniques/<id>` IRI;
- a sub-technique `rdfs:subClassOf` the technique it specializes
  (`AML.T0051.001` *LLM Prompt Injection: Indirect* under `AML.T0051`), and a
  top-level technique `rdfs:subClassOf uco-action:Action`;
- tactics (`dcterms:subject`), platforms such as *Generative AI* or *Agentic
  AI* (`dcterms:coverage`) and the ATLAS matrix (`dcterms:isPartOf`) are
  annotations; the comment ends with ATLAS's maturity rating;
- an ATLAS technique adapted from ATT&CK points at it with `rdfs:seeAlso`.
  That link is a reference, not an import: the ATT&CK catalog is not loaded.

A behavior that exhibits a technique is a `uco-action:Action` **typed with
the technique class**. The `rdf:type` edge is the association; do not create a
technique instance node or a relationship to the technique.

```json
{
  "@id": "kb:action-prompt-injection-<uuid>",
  "@type": ["uco-action:Action", "https://atlas.mitre.org/techniques/AML.T0051.001"],
  "uco-core:name": "Hidden instructions in an inbound email reach the assistant",
  "uco-action:instrument": [{"@id": "kb:email-<uuid>"}],
  "uco-action:object": [{"@id": "kb:assistant-<uuid>"}]
}
```

Find techniques with `search_adversary_techniques("prompt injection",
catalog="atlas")` and read one with `get_adversary_technique("AML.T0051.001")`
(tactics, platforms, parent and sub-techniques, related ATT&CK techniques,
and a typing example).

## 2. Evidence decides every technique type

A technique type is a claim that the evidence shows that tradecraft. Attach
one to the `Action` an artifact supports — an application or agent log, the
injected document or message, a poisoned dataset, model-serving request
logs — and keep the artifact in the graph as the action's `instrument`,
`object`, or `result`. Name the most specific sub-technique the evidence
supports, and only that class (the parent follows by subclassing).

Do not bring ATT&CK in by association. Add `attack-technique` only when the
evidence also shows conventional intrusion — for example, host evidence that
the stolen model weights were staged and exfiltrated over a C2 channel — and
type only the actions that evidence shows (see
[cross-ontology-composition.md](cross-ontology-composition.md) principle 6).
The `rdfs:seeAlso` link from an ATLAS technique to ATT&CK is MITRE's
cross-reference, not evidence about your case.

## 3. Common AI attacks

| What the evidence shows | ATLAS technique |
|---|---|
| Instructions hidden in content the model ingests (email, web page, document, retrieved chunk) | `AML.T0051.001` LLM Prompt Injection: Indirect |
| A user typing instructions that override the system prompt | `AML.T0051.000` LLM Prompt Injection: Direct |
| Prompts that bypass the model's safety controls | `AML.T0054` LLM Jailbreak |
| The system prompt recovered by the adversary | `AML.T0056` Extract LLM System Prompt |
| An agent's own tool call carrying data out | `AML.T0086` Exfiltration via AI Agent Tool Invocation |
| An agent coerced into calling a tool | `AML.T0053` AI Agent Tool Invocation |
| Inputs crafted so a classifier or detector misses them | `AML.T0015` Evade AI Model |
| Tampered training data | `AML.T0020` Training Data Poisoning |
| Tampered retrieval (RAG) corpus | `AML.T0070` RAG Poisoning |
| Model functionality copied through its inference API | `AML.T0024.002` Exfiltration via AI Inference API: Extract AI Model |
| A malicious model file or artifact a user loaded | `AML.T0011.000` User Execution: Unsafe AI Artifacts |
| A compromised model, dataset, or AI dependency in the supply chain | `AML.T0010` AI Supply Chain Compromise |

Confirm each mapping with `get_adversary_technique` before using it; ATLAS
releases monthly and the SDK pins one release (`make sync-atlas`).

## 4. Python skeleton

```python
from case_uco import CASEGraph
from case_uco.uco.action import Action
from case_uco.uco.observable import ObservableObject, EmailMessageFacet

ATLAS = "https://atlas.mitre.org/techniques/"

graph = CASEGraph()
email = graph.create(
    ObservableObject,
    has_facet=[EmailMessageFacet(subject="Q3 vendor schedule")],
)
assistant = graph.create(ObservableObject, description="LLM email assistant")
injection = graph.create(
    Action,
    name="Hidden instructions in an inbound email reach the assistant",
    instrument=[email],
    object=[assistant],
)
graph.add_type(graph.get_id(injection), ATLAS + "AML.T0051.001")
graph.write("ai-system-attack.jsonld")
```

## Validation

```bash
case_validate --built-version case-1.5.0 \
  --ontology-graph extensions/atlas-technique/mitre-atlas-catalog.ttl \
  --inference rdfs --allow-info \
  ai-system-attack.jsonld
```

Or `validate_graph(path, extensions=["atlas-technique"])`, which adds strict
concept coverage. An ATLAS IRI that is not in the pinned catalog fails
coverage; look it up instead of guessing the ID.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Adding ATLAS techniques because the case involves an AI tool | ATLAS describes attacks *on* AI systems; model AI-assisted offenses by the offense |
| Typing an action with both `AML.T0051` and `AML.T0051.001` | Keep only the most specific class; the sub-technique already specializes its parent |
| Loading `attack-technique` because an ATLAS technique has an ATT&CK `rdfs:seeAlso` | Add ATT&CK only for intrusion behavior the evidence shows |
| A technique-typed action with no artifact behind it | Link the log, message, dataset, or request that shows it as `instrument` / `object` / `result` |
| Minting `AML.*` classes that are not in the pinned catalog | Use `search_adversary_techniques`; if ATLAS has moved on, run `make sync-atlas` |
| Naming a performer for an unattributed adversary | Leave `performer` off until the evidence attributes the behavior |

## Checklist

1. Confirm the target is an AI system (section "Not this recipe").
2. Capture the evidence first: the injected content, model or agent logs,
   datasets, requests, each as a hashed `ObservableObject`.
3. Model each adversary behavior as a `uco-action:Action` linked to those
   artifacts; leave `performer` off unless attributed.
4. Type each behavior with the most specific ATLAS technique the evidence
   supports (`search_adversary_techniques(..., catalog="atlas")`).
5. Add ATT&CK techniques only for conventional intrusion that the evidence
   shows, on those actions only.
6. Record the examiner's review as a `case-investigation:InvestigativeAction`
   whose `result` is the behavior actions.
7. Validate with `extensions=["atlas-technique"]` (plus `attack-technique`
   only if step 5 applied); `Conforms: True` before presenting.

## Related

- [cyber-threat-intelligence.md](cyber-threat-intelligence.md) — ATT&CK techniques for intrusion tradecraft, same metaclass pattern
- [cross-ontology-composition.md](cross-ontology-composition.md) — when two vocabularies belong on one graph
- [spear-phishing.md](spear-phishing.md) — the email delivery chain when the injected content arrives by phishing
- [analysis.md](analysis.md) — attribution and confidence for the adversary behind the attack
