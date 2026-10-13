"""Generated bindings honor inherited SHACL bounds (#32, #53) and core registry names (#43)."""

from __future__ import annotations

from datetime import datetime

import pytest

from case_uco import CASEGraph
from case_uco.registry import get_class, list_classes, search
from case_uco.uco.action import Action, ActionLifecycle, ArrayOfAction
from case_uco.uco.observable import ObservableObject, ObservableRelationship


def test_observable_relationship_requires_endpoints():
    with pytest.raises(ValueError, match="source"):
        CASEGraph().create(
            ObservableRelationship,
            kind_of_relationship="Contained_Within",
            is_directional=True,
        )


def test_observable_relationship_with_endpoints():
    g = CASEGraph()
    a = g.create(ObservableObject)
    b = g.create(ObservableObject)
    g.create(
        ObservableRelationship,
        source=[a],
        target=[b],
        kind_of_relationship="Contained_Within",
        is_directional=True,
    )


def test_action_lifecycle_rejects_end_time():
    with pytest.raises(ValueError, match="maxCount 0"):
        CASEGraph().create(
            ActionLifecycle,
            phase=ArrayOfAction(action=[Action(name="phase-step")]),
            end_time=[datetime(2024, 1, 1)],
        )


def test_action_lifecycle_registry_omits_forbidden_properties():
    props = {p["name"] for p in get_class("ActionLifecycle")["properties"]}
    assert "phase" in props
    assert not props & {"endTime", "startTime", "error", "actionCount", "actionStatus"}


@pytest.mark.parametrize(
    ("name", "module"),
    [
        ("Subject", "case.investigation"),
        ("Technique", "uco.action"),
        ("VictimTargeting", "uco.victim"),
    ],
)
def test_core_class_wins_name_collisions(name, module):
    assert get_class(name)["module"] == module
    assert get_class(name, core_only=True)["module"] == module
    modules = {c["module"] for c in search(name) if c["name"] == name}
    assert module in modules
    assert any(m.startswith("ext.") for m in modules)
    assert list_classes().count(name) == 1
