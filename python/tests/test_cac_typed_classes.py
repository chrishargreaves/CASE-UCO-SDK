"""Typed CAC classes from the generated case-uco-cac package."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

from case_uco import CASEGraph
from case_uco.graph import unregister_extension_source

PACKAGE_ROOT = Path(__file__).resolve().parents[2] / "packages" / "case-uco-cac" / "python"


@pytest.fixture(scope="module")
def cac():
    sys.path.insert(0, str(PACKAGE_ROOT))
    try:
        import case_uco_cac

        yield case_uco_cac
    finally:
        sys.path.remove(str(PACKAGE_ROOT))


def test_typed_cac_objects_use_cac_prefixes(cac) -> None:
    from case_uco_cac.cacontology_prevention import EducationalResource
    from case_uco_cac.cacontology_training import CapacityBuildingProgram, TrainingInstitution
    from case_uco_cac.cacontology_victim_impact import VictimSupport
    from case_uco.uco.identity import Organization

    assert issubclass(TrainingInstitution, Organization)
    graph = CASEGraph()
    institution = graph.create(TrainingInstitution, name="Example Training Center", label="Example Training Center")
    graph.create(EducationalResource, name="Example guide", target_audience="parents")
    graph.create(CapacityBuildingProgram, name="Example program", capacity_level="basic")
    graph.create(VictimSupport, label="Referral", service_type="family_support")
    with pytest.raises(ValueError, match="service_type is required"):
        graph.create(VictimSupport, label="No service type")

    doc = json.loads(graph.serialize())
    nodes = {node["@type"]: node for node in doc["@graph"]}
    assert nodes["cacontology-victim-impact:VictimSupport"]["cacontology-victim-impact:serviceType"] == "family_support"
    assert nodes["cacontology-prevention:EducationalResource"]["cacontology-prevention:targetAudience"] == "parents"
    assert nodes["cacontology-training:CapacityBuildingProgram"]["cacontology-training:capacityLevel"] == "basic"
    assert nodes["cacontology-training:TrainingInstitution"]["rdfs:label"] == "Example Training Center"
    assert not any(key.startswith("uco-core:service") for node in doc["@graph"] for key in node)
    assert doc["@context"]["cacontology-victim-impact"] == "https://cacontology.projectvic.org/victim-impact#"
    assert graph.get_id(institution) in {node["@id"] for node in doc["@graph"]}


def test_registered_cac_classes_rehydrate(cac) -> None:
    from case_uco_cac.cacontology_victim_impact import VictimSupport

    graph = CASEGraph()
    graph.create(VictimSupport, label="Referral", service_type="family_support")
    cac.register()
    try:
        _, objects = CASEGraph.from_jsonld(graph.serialize())
    finally:
        unregister_extension_source("cac")
    assert isinstance(objects[0], VictimSupport)
    assert objects[0].service_type == "family_support"


def test_registry_points_at_generated_class(cac) -> None:
    registry = json.loads((PACKAGE_ROOT.parent / "_registry.json").read_text(encoding="utf-8"))
    entry = registry["classes"]["VictimSupport"]
    module_name, _, class_name = entry["python_class"].rpartition(".")
    module = __import__(module_name, fromlist=[class_name])
    assert getattr(module, class_name).CLASS_IRI == entry["iri"]
