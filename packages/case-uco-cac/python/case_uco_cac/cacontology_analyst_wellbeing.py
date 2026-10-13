"""CAC Ontology - Crimes Against Children — cacontology_analyst_wellbeing module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar, Optional

from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["ExposureMitigationMeasure", "OccupationalHarm", "SecondaryTraumaticStress", "VicariousTrauma"]


@dataclass
class ExposureMitigationMeasure(_cac_core.EnduringEntity):
    """A measure, control, or workflow technique used to reduce human exposure to traumatic content while enabling effective review and classification (e.g., blur/previews, hash-only review, progressive reve"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/analyst-wellbeing#ExposureMitigationMeasure"
    NAMESPACE_PREFIX: str = "cacontology-analyst-wellbeing"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    mitigation_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-analyst-wellbeing:mitigationType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class OccupationalHarm(_cac_core.Situation):
    """Occupational harm experienced by investigators or content analysts arising from exposure to traumatic materials or sustained operational stressors."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/analyst-wellbeing#OccupationalHarm"
    NAMESPACE_PREFIX: str = "cacontology-analyst-wellbeing"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    harm_severity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-analyst-wellbeing:harmSeverity', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SecondaryTraumaticStress(OccupationalHarm):
    """Occupational stress reactions arising from indirect exposure to others' trauma, including exposure through content review and investigative materials."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/analyst-wellbeing#SecondaryTraumaticStress"
    NAMESPACE_PREFIX: str = "cacontology-analyst-wellbeing"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VicariousTrauma(OccupationalHarm):
    """A form of occupational harm in which repeated exposure to traumatic material produces trauma-like impacts in the reviewer."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/analyst-wellbeing#VicariousTrauma"
    NAMESPACE_PREFIX: str = "cacontology-analyst-wellbeing"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
