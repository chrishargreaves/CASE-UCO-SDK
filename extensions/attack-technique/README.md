# MITRE ATT&CK Technique Catalog (`attack-technique`)

The complete [MITRE ATT&CK](https://attack.mitre.org) v19.2 technique set —
Enterprise, Mobile and ICS, 1,166 techniques and sub-techniques — expressed
with the UCO 1.5.0 `uco-action:Technique` metaclass
([ucoProject/UCO PR #676](https://github.com/ucoProject/UCO/pull/676),
resolving [issue #666](https://github.com/ucoProject/UCO/issues/666)).

ATT&CK describes **adversary tradecraft against computer systems**. It is a
separate vocabulary from SOLVE-IT (forensic practice), the offense-conduct
extensions (`trafficking`, `elder-fraud`, `extortion`, `trajectories`) and
CAC, and no extension depends on it. Load it only for graphs whose evidence
shows intrusion behavior; see
[cross-ontology-composition.md](../../docs/recipes/cross-ontology-composition.md)
principle 6. Attacks on AI systems use the sibling
[`atlas-technique`](../atlas-technique/) catalog.

## The model

`uco-action:Technique` is a metaclass. Verbatim from UCO: *"A technique is a
class of actions joined by some common characteristics.
`uco-action:Technique` itself is a metaclass. A Technique instance is an
`owl:Class` that is a subclass of `uco-action:Action`."* UCO 1.5.0 defines it,
`uco-core:UcoType`, and `uco-action:techniqueID` natively. This extension no
longer carries a local copy of those terms (it did while `case_validate` was
pinned to CASE 1.4.0); it contributes only the catalog.

```turtle
# In the catalog: a technique is a class.
attack:T1543.003
    a owl:Class, uco-action:Technique ;
    rdfs:subClassOf attack:T1543 ;
    rdfs:label "Create or Modify System Process: Windows Service"@en ;
    uco-action:techniqueID "T1543.003" ;
    dcterms:subject attack-tactic:TA0003 , attack-tactic:TA0004 ;
    dcterms:coverage "Windows" ;
    dcterms:isPartOf <https://attack.mitre.org/matrices/enterprise/> .

# In the case graph: the behavior the evidence shows is an instance of it.
kb:action-install-service
    a uco-action:Action, attack:T1543.003 ;
    uco-action:performer kb:lotus-blossom .
```

| Catalog content | Representation |
|---|---|
| Technique | `owl:Class`, `a uco-action:Technique`, `rdfs:subClassOf uco-action:Action`, `uco-action:techniqueID` |
| Sub-technique | Same, but `rdfs:subClassOf` its parent technique (`subtechnique-of`); label "Parent: Sub-technique" |
| Tactic | `dcterms:subject` → `https://attack.mitre.org/tactics/TA…` (labelled, per matrix) |
| Platform | `dcterms:coverage` literal |
| Matrix | `dcterms:isPartOf` → `https://attack.mitre.org/matrices/{enterprise,mobile,ics}/` |
| Deprecated / revoked | Kept, `owl:deprecated true`; a revoked technique has `dcterms:isReplacedBy` its successor (`revoked-by`) |
| Description | First paragraph of the ATT&CK description (citations stripped), plus `rdfs:seeAlso` the ATT&CK page |

Tactics, platforms and matrices are OWL annotations, never class axioms,
because the released UCO model keeps `uco-action:Technique` minimal (it has
no framework, tactic, or platform properties). The Dublin Core properties are
declared `owl:AnnotationProperty` in the catalog; no new vocabulary is minted.

## Discovery

- `search_adversary_techniques("registry run keys", catalog="attack")`
- `get_adversary_technique("T1547.001")` — tactics, platforms, parent and
  sub-techniques, replacement for a revoked ID, and a typing example

## Validation

```bash
case_validate --built-version case-1.5.0 \
  --ontology-graph extensions/attack-technique/mitre-attack-catalog.ttl \
  --inference rdfs --allow-info \
  path/to/graph.jsonld
```

Or `validate_graph(path, extensions=["attack-technique"])` (strict concept
coverage included).

## Refreshing the catalog

```bash
make sync-attack                          # ATT&CK v19.2 (or the manifest pin)
make sync-attack ATTACK_VERSION=19.2
make sync-attack-offline STIX_DIR=/path/to/stix ATTACK_VERSION=19.2
```

`mcp_server/tools/sync_attack_catalog.py` reads the three STIX 2.1 bundles
from [mitre-attack/attack-stix-data](https://github.com/mitre-attack/attack-stix-data),
regenerates `mitre-attack-catalog.ttl`, and records the release, per-bundle
SHA-256, and counts in `manifest.json`. `--check` reports drift without
writing. Do not edit the catalog by hand.

## Files

| File | What it is |
|---|---|
| `mitre-attack-catalog.ttl` | Generated catalog (techniques, sub-techniques, tactics, matrices) |
| `manifest.json` | Extension manifest and sync provenance |
| `_registry.json` | Discovery pointer; the metaclass is in the core registry |

## License

ATT&CK content: © 2026 The MITRE Corporation. This work is reproduced and
distributed with the permission of The MITRE Corporation, under the
[ATT&CK Terms of Use](https://attack.mitre.org/resources/legal-and-branding/terms-of-use/).
SDK tooling: Apache-2.0.

## Used by

- [`examples/cti/lotus_blossom_2025/`](../../examples/cti/lotus_blossom_2025/) and
  [`examples/cti/darkwatchman_2021/`](../../examples/cti/darkwatchman_2021/)
- Recipe: [`docs/recipes/cyber-threat-intelligence.md`](../../docs/recipes/cyber-threat-intelligence.md)
