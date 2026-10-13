"""Extension packages and scaffolds must emit valid identifiers for punned classes."""

from __future__ import annotations

import ast
from pathlib import Path

from case_uco_generator.cli import _gen_python_extension
from case_uco_generator.scaffold import scaffold_python
from case_uco_generator.schema_model import OntologyClass, OntologySchema

IRI = "https://ontology.solveit-df.org/solveit/data/techniqueDFT-1001"


def _schema() -> OntologySchema:
    cls = OntologyClass(
        iri=IRI,
        name="techniqueDFT-1001",
        namespace_prefix="solveit-data",
        module="ext.solveit.solveit-data",
    )
    return OntologySchema(
        classes={IRI: cls},
        modules={"ext.solveit.solveit-data": [IRI]},
    )


def test_extension_package_sanitizes_hyphenated_class_names(tmp_path: Path) -> None:
    schema = _schema()
    _gen_python_extension(
        schema, schema, tmp_path, "solveit", "0.0.1", "SOLVE-IT", "case_uco_solveit", ">=1.5.0", {}
    )
    source = (tmp_path / "python" / "case_uco_solveit" / "solveit_data.py").read_text(encoding="utf-8")
    tree = ast.parse(source)
    names = [node.name for node in tree.body if isinstance(node, ast.ClassDef)]
    assert names == ["techniqueDFT_1001"]
    assert f'CLASS_IRI: str = "{IRI}"' in source


def test_registry_keeps_canonical_class_on_local_name_collision(tmp_path: Path) -> None:
    import json

    from case_uco_generator.cli import _emit_extension_registry

    canonical_iri = "https://example.org/usa-federal-law#FederalProsecution"
    alias_iri = "https://example.org/legal-outcomes#FederalProsecution"
    canonical = OntologyClass(
        iri=canonical_iri, name="FederalProsecution",
        namespace_prefix="ext-usa-federal-law", module="ext.cac.usa-federal-law",
    )
    alias = OntologyClass(
        iri=alias_iri, name="FederalProsecution",
        namespace_prefix="ext-legal-outcomes", module="ext.cac.legal-outcomes",
        equivalent_iris=[canonical_iri],
    )
    schema = OntologySchema(
        classes={alias_iri: alias, canonical_iri: canonical},
        modules={"ext.cac.legal-outcomes": [alias_iri], "ext.cac.usa-federal-law": [canonical_iri]},
    )
    registry = json.loads(_emit_extension_registry(schema, schema, tmp_path, "cac").read_text(encoding="utf-8"))
    assert registry["classes"]["FederalProsecution"]["iri"] == canonical_iri
    assert registry["classes"]["ext-legal-outcomes:FederalProsecution"]["iri"] == alias_iri


def test_scaffold_sanitizes_hyphenated_class_names() -> None:
    tree = ast.parse(scaffold_python(_schema(), "solveit-data", "https://ontology.solveit-df.org/solveit/data/"))
    assert [node.name for node in tree.body if isinstance(node, ast.ClassDef)] == ["techniqueDFT_1001"]
