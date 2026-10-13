# Resource Catalogs, Desk References, and Training Directories

> See [Recipe Index](INDEX.md) for all recipes.

Model a document that *lists* resources — an investigator quick-reference
guide, a hotline directory, a training catalog, a tool list — as the document
plus the organizations, tools, training, and educational material it names.
A catalog records no investigation, so this recipe creates no case nodes.

## When to use this recipe

- `route_investigation_content` or `route_cac_content` returns
  `document_genre` (`resource-catalog` or `training-material`) and puts this
  recipe first. The topical families it shows in `topic_families` (for
  example CAC, legal, or forensics) are vocabulary hints only.
- The source has task headers ("Need to:"), access badges ("Login Required",
  "Paid"), "Name | Resource" entries, and a link per entry, and it has no
  case artifacts: no docket or case numbers, hashes of evidence, IP
  addresses, timestamps of events, or charging language.

When a case file *contains* a resource appendix, route the case evidence
with its case recipe and add the appendix with this pattern in the same
graph.

## Key classes

| Class | Use for |
|---|---|
| `uco-observable:ObservableObject` with `uco-observable:FileFacet` and `uco-observable:ContentDataFacet` | The catalog document, with its SHA-256 |
| `uco-core:Grouping` | One catalog section ("Hotlines", "Training") whose `uco-core:object` lists the section's entries |
| `uco-core:Relationship` (`Contained_Within`) | Section to document |
| `uco-core:ExternalReference` | The link printed for an entry (`uco-core:referenceURL`) and its access note (`uco-core:definingContext`) |
| `uco-identity:Organization` | Task forces, nonprofits, helplines, portals |
| `uco-tool:Tool` | Software and online tools (imagers, hash libraries, legal-process builders) |
| `cacontology-hotlines:HotlineOrganization` | Organizations that operate a reporting hotline (CAC extension) |
| `cacontology-training:TrainingInstitution` | Organizations that provide training (CAC extension; a `uco-identity:Organization` subclass) |
| `cacontology-prevention:EducationalResource` | Parent, school, and reference material; `cacontology-prevention:targetAudience` takes the CAC allowed values (`parents`, `children`, `educators`, `professionals`, ...) |

## Canonical pattern

```
catalog document (ObservableObject + FileFacet + ContentDataFacet/SHA-256)
  ^  Contained_Within
Grouping "Hotlines" --uco-core:object--> HotlineOrganization --uco-core:externalReference--> ExternalReference
Grouping "Training" --uco-core:object--> TrainingInstitution --uco-core:externalReference--> ExternalReference
Grouping "Prevention" --uco-core:object--> Organization, EducationalResource --uco-core:createdBy--> Organization
```

## Python skeleton

The typed CAC classes come from `case-uco-cac`
(`pip install case-uco-cac`); validate with the `cac:catalog` profile.

```python
import hashlib
from pathlib import Path

from case_uco import CASEGraph
from case_uco.uco.core import ExternalReference, Grouping, Relationship
from case_uco.uco.observable import ContentDataFacet, FileFacet, ObservableObject
from case_uco.uco.tool import Tool
from case_uco.uco.types import Hash
from case_uco_cac.cacontology_hotlines import HotlineOrganization
from case_uco_cac.cacontology_training import TrainingInstitution

data = Path("resource-catalog-sample.txt").read_bytes()
graph = CASEGraph()
guide = graph.create(ObservableObject, has_facet=[
    FileFacet(file_name="resource-catalog-sample.txt", size_in_bytes=len(data)),
    ContentDataFacet(
        hash=[Hash(hash_method="SHA256", hash_value=hashlib.sha256(data).hexdigest().upper())],
        size_in_bytes=len(data), mime_type="text/plain",
    ),
])
hotline = graph.create(
    HotlineOrganization, name="Example Hotline Network", label="Example Hotline Network",
    external_reference=[ExternalReference(reference_url="https://hotline.example.org/report",
                                          defining_context="Listed in the catalog")],
)
academy = graph.create(
    TrainingInstitution, name="Example Forensics Academy", label="Example Forensics Academy",
    external_reference=[ExternalReference(reference_url="https://academy.example.net",
                                          defining_context="Listed in the catalog; access: paid")],
)
imager = graph.create(Tool, name="Example Imaging Tool")
for title, members in (("Hotlines", [hotline]), ("Training", [academy]), ("Digital forensics", [imager])):
    section = graph.create(Grouping, name=title, context=["Resource catalog section"], object=members)
    graph.create(Relationship, source=[section], target=guide,
                 kind_of_relationship="Contained_Within", is_directional=True)
graph.write("resource-catalog.jsonld")
```

The full builder is
[`examples/recipes/build_resource_catalog.py`](../../examples/recipes/build_resource_catalog.py)
(output `examples/recipes/resource-catalog.jsonld`, synthetic source
`examples/recipes/resource-catalog-sample.txt`).

## Modeling rules

- Record what the catalog prints. Keep its access notes ("login required",
  "paid", "free download") in `uco-core:definingContext`, and do not add
  languages, audiences, or dates it does not state.
- Every CAC class needs `label` (`rdfs:label`); the CAC spine shapes
  require it.
- Use the CAC allowed values for `targetAudience`. The
  `community_members` audience also expects several languages, so choose it
  only when the catalog lists them.
- One graph per catalog. Sections become `uco-core:Grouping` nodes, so
  entries that appear in two sections are one node referenced twice.

## Anti-patterns

- Creating `case-investigation:Investigation`, suspects, victims, offenses,
  or warrants because the catalog mentions them as topics.
- Typing a listed service as an event: `cacontology-victim-impact:VictimSupport`,
  `cacontology-prevention:PreventionProgram`, and the CAC training classes
  are gUFO events that need a begin time. A listing is not something that
  happened.
- `cacontology-institutional-exploitation:CharitableOrganization` for an
  ordinary nonprofit: its shapes expect institutional component parts. Use
  `uco-identity:Organization`.

## Validation

```bash
# SDK / MCP
# validate_graph("resource-catalog.jsonld", extensions=["cac:catalog"])
case_validate --built-version case-1.5.0 \
  --ontology-graph ontology/cac/ontology/ontology/cacontology-core-spine.ttl \
  --ontology-graph ontology/cac/ontology/ontology/cacontology-hotlines.ttl \
  --ontology-graph ontology/cac/ontology/ontology/cacontology-training.ttl \
  --ontology-graph ontology/cac/ontology/ontology/cacontology-prevention.ttl \
  --inference rdfs --allow-info \
  examples/recipes/resource-catalog.jsonld
```

`cac:catalog` (`ontology/cac/validation-subset-catalog.json`) loads the CAC
core spine with the hotline, training, and prevention modules and their
shapes. Without the CAC extension, keep the core classes above and drop the
`cacontology-*` types.

## Related recipes

- [cross-ontology-composition.md](cross-ontology-composition.md) — when a case file carries a resource appendix
- [cac-hotline-intake-lifecycle.md](cac-hotline-intake-lifecycle.md) — hotline *reports* (case evidence), not hotline listings
- [configured-tool.md](configured-tool.md) — tools that were actually used in an examination
