"""CAC Ontology - Crimes Against Children — cacontology_synthesis module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar, Optional

import case_uco.uco.core as _uco_core
import case_uco.uco.observable as _uco_observable
from case_uco_cac._context import NAMESPACES

__all__ = ["Claim", "DistributionObservation", "EvidenceGap", "InterventionLocus", "InterventionObjective", "InterventionOperation", "InterventionType", "KeyFinding", "MethodologyStatement", "OffendingChain", "OffendingChainStage", "Recommendation", "Report", "ReportArtifact", "ReportFigure", "ReportSection", "ResearchQuestion", "ScopeConstraint", "TextEvidencePointer"]


@dataclass
class Claim(_uco_core.UcoObject):
    """A first-class, queryable claim extracted from a report (finding, recommendation, distribution, gap, or scope constraint)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/synthesis#Claim"
    NAMESPACE_PREFIX: str = "cacontology-synthesis"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class DistributionObservation(Claim):
    """A structured observation about a distribution (count/denominator and/or rank) reported by a report."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/synthesis#DistributionObservation"
    NAMESPACE_PREFIX: str = "cacontology-synthesis"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EvidenceGap(Claim):
    """A stated gap, limitation, or missing intervention area identified by a report."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/synthesis#EvidenceGap"
    NAMESPACE_PREFIX: str = "cacontology-synthesis"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InterventionLocus(_uco_core.UcoObject):
    """A locus within the TF-CSEA ecosystem/offending chain that an intervention targets (e.g., grooming, payment systems)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/synthesis#InterventionLocus"
    NAMESPACE_PREFIX: str = "cacontology-synthesis"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class InterventionObjective(_uco_core.UcoObject):
    """An objective an intervention serves (e.g., CSAM detection, improve policing effectiveness)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/synthesis#InterventionObjective"
    NAMESPACE_PREFIX: str = "cacontology-synthesis"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class InterventionOperation(_uco_core.UcoObject):
    """A domain of operation for an intervention (e.g., online, hybrid)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/synthesis#InterventionOperation"
    NAMESPACE_PREFIX: str = "cacontology-synthesis"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class InterventionType(_uco_core.UcoObject):
    """A category of TF-CSEA intervention (e.g., technological tools and protocols)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/synthesis#InterventionType"
    NAMESPACE_PREFIX: str = "cacontology-synthesis"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class KeyFinding(Claim):
    """A numbered key finding stated by a report."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/synthesis#KeyFinding"
    NAMESPACE_PREFIX: str = "cacontology-synthesis"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MethodologyStatement(Claim):
    """A structured statement about methodology (e.g., PRISMA, date range, databases, inclusion criteria)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/synthesis#MethodologyStatement"
    NAMESPACE_PREFIX: str = "cacontology-synthesis"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OffendingChain(_uco_core.UcoObject):
    """A conceptual chain of activities in TF-CSEA used to locate interventions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/synthesis#OffendingChain"
    NAMESPACE_PREFIX: str = "cacontology-synthesis"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class OffendingChainStage(_uco_core.UcoObject):
    """A stage within an offending chain."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/synthesis#OffendingChainStage"
    NAMESPACE_PREFIX: str = "cacontology-synthesis"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class Recommendation(Claim):
    """A numbered recommendation stated by a report."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/synthesis#Recommendation"
    NAMESPACE_PREFIX: str = "cacontology-synthesis"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Report(_uco_core.UcoObject):
    """A report or publication treated as a collected source document (an intellectual work), distinct from the concrete artifact(s) that realize it."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/synthesis#Report"
    NAMESPACE_PREFIX: str = "cacontology-synthesis"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ReportArtifact(_uco_observable.ObservableObject):
    """A concrete artifact that realizes a Report (e.g., a PDF file). Use this when you want a report-as-file node that is separate from the report-as-intellectual-work."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/synthesis#ReportArtifact"
    NAMESPACE_PREFIX: str = "cacontology-synthesis"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ReportFigure(_uco_core.UcoObject):
    """A figure within a report (e.g., PRISMA diagram, distribution charts)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/synthesis#ReportFigure"
    NAMESPACE_PREFIX: str = "cacontology-synthesis"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ReportSection(_uco_core.UcoObject):
    """A logical section of a report (e.g., Synopsis, Methods, Findings)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/synthesis#ReportSection"
    NAMESPACE_PREFIX: str = "cacontology-synthesis"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ResearchQuestion(Claim):
    """A research question posed by a report."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/synthesis#ResearchQuestion"
    NAMESPACE_PREFIX: str = "cacontology-synthesis"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ScopeConstraint(Claim):
    """A stated boundary on what the report includes/excludes (e.g., out-of-scope topics)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/synthesis#ScopeConstraint"
    NAMESPACE_PREFIX: str = "cacontology-synthesis"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TextEvidencePointer(_uco_core.UcoObject):
    """A resolvable pointer to a location in a text artifact (e.g., normalized.txt lines), optionally with quote and quote hash."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/synthesis#TextEvidencePointer"
    NAMESPACE_PREFIX: str = "cacontology-synthesis"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
