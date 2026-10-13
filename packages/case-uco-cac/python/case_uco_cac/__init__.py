"""CAC Ontology - Crimes Against Children — CASE/UCO SDK extension bindings.

Each module holds typed dataclasses that work with ``CASEGraph.create``.
Call :func:`register` (or ``case_uco.graph.discover_extension_class_providers()``)
so ``CASEGraph.from_jsonld`` rehydrates these types.
"""

from __future__ import annotations

import importlib

from case_uco_cac._context import NAMESPACES

__version__ = "3.1.0"

MODULES: tuple[str, ...] = (
    "cac_core",
    "cacontology",
    "cacontology_ai_csam",
    "cacontology_analyst_wellbeing",
    "cacontology_asset_forfeiture",
    "cacontology_athletic_exploitation",
    "cacontology_case_management",
    "cacontology_custodial",
    "cacontology_detection",
    "cacontology_educational_exploitation",
    "cacontology_extremist_enterprises",
    "cacontology_forensics",
    "cacontology_grooming",
    "cacontology_hotlines",
    "cacontology_institutional_exploitation",
    "cacontology_integration_patterns",
    "cacontology_international",
    "cacontology_investigation_coordination",
    "cacontology_law_enforcement_corruption",
    "cacontology_legal_harmonization",
    "cacontology_legal_outcomes",
    "cacontology_multi_jurisdiction",
    "cacontology_partnerships",
    "cacontology_physical_evidence",
    "cacontology_platform_infrastructure",
    "cacontology_platforms",
    "cacontology_prevention",
    "cacontology_production",
    "cacontology_recantation",
    "cacontology_recruitment_networks",
    "cacontology_sadistic_online_exploitation",
    "cacontology_sex_offender_registry",
    "cacontology_sex_trafficking",
    "cacontology_sextortion",
    "cacontology_specialized_units",
    "cacontology_stranger_abduction",
    "cacontology_street_recruitment",
    "cacontology_synthesis",
    "cacontology_tactical",
    "cacontology_taskforce",
    "cacontology_temporal",
    "cacontology_training",
    "cacontology_undercover",
    "cacontology_us_ncmec",
    "cacontology_usa_federal_law",
    "cacontology_usa_legislative",
    "cacontology_victim_impact",
)

# Public so the case_uco.extensions entry point (and static analysis)
# can reference it: the SDK registry loader resolves this at runtime.
REGISTRY_PATH = __file__.replace("__init__.py", "_registry.json")


def classes() -> list[type]:
    """Every generated class; the ``case_uco.class_registry`` provider."""
    found: list[type] = []
    for name in MODULES:
        module = importlib.import_module(f"{__name__}.{name}")
        found.extend(getattr(module, cls_name) for cls_name in module.__all__)
    return found


def register() -> int:
    """Register the classes for typed ``CASEGraph.from_jsonld`` loading."""
    from case_uco.graph import register_extension_classes

    return register_extension_classes(classes(), source="cac", context=NAMESPACES)


__all__ = ["MODULES", "NAMESPACES", "REGISTRY_PATH", "__version__", "classes", "register"]
