"""Generated Python extension classes subclass core classes and serialize with extension prefixes."""

from __future__ import annotations

import ast
import importlib
import json
import sys
from pathlib import Path

import pytest

from case_uco_generator.cli import _gen_python_extension
from case_uco_generator.schema_model import (
    Cardinality,
    OntologyClass,
    OntologyProperty,
    OntologySchema,
)

CORE = "https://ontology.unifiedcyberontology.org/uco/core/"
IDENTITY = "https://ontology.unifiedcyberontology.org/uco/identity/"
SPINE = "https://example.org/spine#"
TRAINING = "https://example.org/training#"
XSD_STRING = "http://www.w3.org/2001/XMLSchema#string"


def _prop(iri: str, name: str, cardinality: Cardinality = Cardinality.ZERO_OR_ONE) -> OntologyProperty:
    return OntologyProperty(
        iri=iri, name=name, range_iri=XSD_STRING, range_is_class=False, cardinality=cardinality
    )


def _schemas() -> tuple[OntologySchema, OntologySchema]:
    uco_object = OntologyClass(
        iri=f"{CORE}UcoObject", name="UcoObject", namespace_prefix="uco-core", module="uco.core",
        properties=[_prop(f"{CORE}name", "name")],
    )
    identity = OntologyClass(
        iri=f"{IDENTITY}Identity", name="Identity", namespace_prefix="uco-identity",
        module="uco.identity", parent_iris=[uco_object.iri],
    )
    organization = OntologyClass(
        iri=f"{IDENTITY}Organization", name="Organization", namespace_prefix="uco-identity",
        module="uco.identity", parent_iris=[identity.iri],
    )
    support_event = OntologyClass(
        iri=f"{SPINE}SupportEvent", name="SupportEvent", namespace_prefix="ext.demo-spine",
        module="ext.demo.spine", parent_iris=[uco_object.iri],
        properties=[_prop(f"{CORE}name", "name"), _prop(f"{SPINE}eventCode", "eventCode")],
    )
    org_like = OntologyClass(
        iri=f"{SPINE}OrganizationLikeEntity", name="OrganizationLikeEntity",
        namespace_prefix="ext.demo-spine", module="ext.demo.spine", parent_iris=[uco_object.iri],
    )
    victim_support = OntologyClass(
        iri=f"{TRAINING}VictimSupport", name="VictimSupport", namespace_prefix="ext.demo-training",
        module="ext.demo.training", parent_iris=[support_event.iri],
        properties=[_prop(f"{TRAINING}serviceType", "serviceType", Cardinality.EXACTLY_ONE)],
    )
    institution = OntologyClass(
        iri=f"{TRAINING}TrainingInstitution", name="TrainingInstitution",
        namespace_prefix="ext.demo-training", module="ext.demo.training",
        parent_iris=[org_like.iri, organization.iri],
    )
    core = [uco_object, identity, organization]
    ext = [support_event, org_like, victim_support, institution]
    modules = {
        "ext.demo.spine": [support_event.iri, org_like.iri],
        "ext.demo.training": [victim_support.iri, institution.iri],
    }
    full = OntologySchema(
        classes={c.iri: c for c in core + ext},
        modules={"uco.core": [uco_object.iri], "uco.identity": [identity.iri, organization.iri], **modules},
    )
    return full, OntologySchema(classes={c.iri: c for c in ext}, modules=modules)


MANIFEST = {"namespaces": {"demo-spine": SPINE, "demo-training": TRAINING}}


@pytest.fixture()
def generated(tmp_path: Path):
    full, ext = _schemas()
    _gen_python_extension(ext, full, tmp_path, "demo", "0.0.1", "Demo", "case_uco_demo_ext", ">=1.5.0", MANIFEST)
    return tmp_path / "python"


def test_extension_classes_subclass_core_and_skip_restated_fields(generated: Path) -> None:
    source = (generated / "case_uco_demo_ext" / "spine.py").read_text(encoding="utf-8")
    tree = ast.parse(source)
    support = next(n for n in tree.body if isinstance(n, ast.ClassDef) and n.name == "SupportEvent")
    assert ast.unparse(support.bases[0]) == "_uco_core.UcoObject"
    fields = [n.target.id for n in support.body if isinstance(n, ast.AnnAssign)]
    assert "name" not in fields
    assert {"event_code", "label"} <= set(fields)
    assert "'jsonld_key': 'demo-spine:eventCode'" in source

    training = (generated / "case_uco_demo_ext" / "training.py").read_text(encoding="utf-8")
    assert "class VictimSupport(_spine.SupportEvent):" in training
    assert "class TrainingInstitution(_uco_identity.Organization):" in training

    pyproject = (generated / "pyproject.toml").read_text(encoding="utf-8")
    assert '[project.entry-points."case_uco.class_registry"]' in pyproject
    assert 'demo = "case_uco_demo_ext:classes"' in pyproject


def test_extension_classes_serialize_with_extension_prefixes(generated: Path) -> None:
    pytest.importorskip("case_uco")
    from case_uco import CASEGraph

    sys.path.insert(0, str(generated))
    try:
        package = importlib.import_module("case_uco_demo_ext")
        training = importlib.import_module("case_uco_demo_ext.training")
        assert {c.__name__ for c in package.classes()} == {
            "SupportEvent", "OrganizationLikeEntity", "VictimSupport", "TrainingInstitution",
        }
        graph = CASEGraph()
        graph.create(training.VictimSupport, name="Referral", label="Referral", service_type="family_support")
        with pytest.raises(ValueError, match="service_type is required"):
            graph.create(training.VictimSupport, name="Missing type")
        doc = json.loads(graph.serialize())
    finally:
        sys.path.remove(str(generated))
        for name in [m for m in sys.modules if m.startswith("case_uco_demo_ext")]:
            del sys.modules[name]

    node = doc["@graph"][0]
    assert node["@type"] == "demo-training:VictimSupport"
    assert node["uco-core:name"] == "Referral"
    assert node["rdfs:label"] == "Referral"
    assert node["demo-training:serviceType"] == "family_support"
    assert doc["@context"]["demo-training"] == TRAINING
    assert doc["@context"]["rdfs"] == "http://www.w3.org/2000/01/rdf-schema#"
