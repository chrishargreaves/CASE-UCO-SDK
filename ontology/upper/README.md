# Vendored Upper-Ontology Sources

Pinned source files for every upper/external ontology that UCO maintains a
[CDO-Shapes](https://github.com/ucoProject) conformance profile for. These
snapshots exist so the SDK works **fully offline**:

- `mcp_server/tools/build_upper_ontology_registry.py` rebuilds the strict
  concept-coverage registry (`mcp_server/upper_ontology_registry.json`)
  from these files by default — no network access required.
- Developers on air-gapped investigation networks can inspect the exact
  upper-ontology text the registry was derived from.

| File | Ontology | Upstream source |
| --- | --- | --- |
| `bfo.owl` | Basic Formal Ontology (BFO) 2.0 / ISO 21838-2 | <http://purl.obolibrary.org/obo/bfo.owl> |
| `gufo.ttl` | gentle Unified Foundational Ontology (gUFO) | <https://nemo-ufes.github.io/gufo/gufo.ttl> |
| `prov-o.ttl` | W3C Provenance Ontology (PROV-O) | <http://www.w3.org/ns/prov-o.ttl> |
| `time.ttl` | W3C OWL-Time | <https://www.w3.org/2006/time.ttl> |
| `geo.ttl` | OGC GeoSPARQL 1.1 (core) | <https://opengeospatial.github.io/ogc-geosparql/geosparql11/geo.ttl> |
| `sf.ttl` | OGC Simple Features geometries | <https://opengeospatial.github.io/ogc-geosparql/geosparql11/sf_geometries.ttl> |
| `foaf.rdf` | Friend of a Friend (FOAF) 0.99 | <http://xmlns.com/foaf/spec/index.rdf> |
| `org.ttl` | W3C Organization Ontology (ORG) | <https://www.w3.org/ns/org.ttl> |
| `prof.ttl` | W3C Profiles Vocabulary (PROF) | <https://www.w3.org/ns/dx/prof/> |
| `prof-roles.ttl` | W3C PROF Resource Roles vocabulary | <https://www.w3.org/ns/dx/prof/role/> |
| `qudt-schema.ttl` | QUDT 3.5.2 schema | `schema/SCHEMA_QUDT.ttl` in the [v3.5.2 release](https://github.com/qudt/qudt-public-repo/releases/tag/v3.5.2) |
| `qudt-units.ttl` | QUDT 3.5.2 units | `vocab/unit/VOCAB_QUDT-UNITS-ALL.ttl` in the same release |
| `qudt-quantitykinds.ttl` | QUDT 3.5.2 quantity kinds | `vocab/quantitykinds/VOCAB_QUDT-QUANTITY-KINDS-ALL.ttl` in the same release |
| `qudt-prefixes.ttl` | QUDT 3.5.2 unit prefixes | `vocab/prefixes/VOCAB_QUDT-PREFIXES.ttl` in the same release |
| `sosa.ttl` | W3C SOSA (2017 Recommendation) | <https://www.w3.org/ns/sosa/> |
| `ssn.ttl` | W3C SSN (2017 Recommendation) | <https://www.w3.org/ns/ssn/> |
| `ssn-systems.ttl` | W3C SSN System Capabilities | <https://www.w3.org/ns/ssn/systems/> |

`provenance.json` records the source URL, SHA-256, and fetch timestamp of
each file.

## CDO-Shapes conformance profiles (`shapes/`)

The `shapes/` subdirectory vendors the SHACL conformance profiles published
by the [Cyber Domain Ontology project](https://github.com/Cyber-Domain-Ontology)
for each profiled ontology (`sh-bfo.ttl`, `sh-gufo.ttl`, `sh-prov-o.ttl`,
`sh-time.ttl`, `sh-geo.ttl`, `sh-foaf.ttl`, `sh-org.ttl`, `sh-prof.ttl`),
pinned to a specific upstream commit recorded in `provenance.json`. They can
be passed to `case_validate` for offline profile conformance checks:

```bash
case_validate --built-version case-1.5.0 \
  --ontology-graph ontology/upper/shapes/sh-prov-o.ttl \
  --allow-info output.jsonld
```

The `get_uco_profiles` MCP tool reports these vendored paths as
`local_source` / `local_shapes` for each profile.

## SDK-pinned profiles and shapes (`sdk-shapes/`)

UCO has no CDO-Shapes profile for QUDT, SOSA, or SSN yet (see
[ucoProject/UCO#404](https://github.com/ucoProject/UCO/issues/404)), so the
SDK pins them itself as the `qudt`, `sosa`, and `ssn` validation profiles.
The W3C publishes no SHACL for SOSA/SSN, and the SDK does not load QUDT's own
SHACL (it imports SKOS by an unversioned IRI). `sdk-shapes/sh-qudt-sdk.ttl`
and `sdk-shapes/sh-sosa-sdk.ttl` hold the minimal shapes the SDK enforces:
one numeric `qudt:value` and one `qudt:hasUnit` per `qudt:QuantityValue`,
a result on every `sosa:Observation`, and at most one sensor, feature of
interest, observed property, phenomenon time, and result time per
observation. The QUDT unit vocabulary also feeds
`mcp_server/qudt_unit_index.json`, the index behind the `lookup_qudt_units`
MCP tool.

## Licensing

Each file remains under its upstream license and is vendored unmodified for
interoperability: BFO and gUFO are published under Creative Commons
Attribution 4.0; the W3C vocabularies (PROV-O, OWL-Time, ORG, PROF) under
the W3C Software and Document License; GeoSPARQL under the OGC document
license; FOAF under Creative Commons Attribution; SOSA and SSN under the
W3C Software and Document License and the OGC Software License; QUDT under
Creative Commons Attribution 4.0, with the UCUM notice from the Regenstrief
Institute that the QUDT schema carries. Consult the ontology
headers inside each file for the authoritative license statement.

## Refreshing the snapshot

```bash
# Re-download all pinned sources and rebuild the registry (network required)
python3 mcp_server/tools/build_upper_ontology_registry.py --fetch

# Offline rebuild from this snapshot (default)
python3 mcp_server/tools/build_upper_ontology_registry.py
```

Review the resulting registry diff before committing — term additions or
removals change what strict concept coverage accepts.
