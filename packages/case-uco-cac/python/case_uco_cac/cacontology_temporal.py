"""CAC Ontology - Crimes Against Children — cacontology_temporal module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar, Optional

from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["Age", "AgeAtTimeSituation", "AnalysisTransitionEvent", "ClosureEvent", "CompletedPhase", "ConcurrentInvestigationSituation", "EventSequence", "EvidenceTransitionEvent", "InitiationEvent", "InvestigationLifecycle", "LegalProcessTransitionEvent", "MultiJurisdictionCoordinationSituation", "ParallelEventCluster", "ParallelEvidenceCollectionSituation", "PhaseTransitionEvent", "ResolutionPhase", "ResolutionTransitionEvent", "ResumptionEvent", "RoleConflictSituation", "RoleEscalation", "RoleReassignment", "RoleTransition", "SimultaneousRoleSituation", "SuspendedSituation", "SuspensionEvent", "UrgentRescueLifecycle"]


@dataclass
class Age:
    """Age of a person modeled as a gUFO Quality whose concrete value is attributed in time-bounded situations. Intended for age-of-consent, Romeo-and-Juliet, and other age-dependent legal reasoning."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#Age"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class AgeAtTimeSituation(_cac_core.Situation):
    """gUFO QualityValueAttributionSituation specializing in attribution of an Age quality value to a specific person over a time-bounded interval (e.g., the victim was 13 years old during a 2025 grooming ev"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#AgeAtTimeSituation"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PhaseTransitionEvent(_cac_core.Event):
    """Event marking transition between investigation phases. Modeled as gUFO Event with temporal boundaries and phase change effects."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#PhaseTransitionEvent"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AnalysisTransitionEvent(PhaseTransitionEvent):
    """Event transitioning investigation from Initial to Analysis Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#AnalysisTransitionEvent"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ClosureEvent(PhaseTransitionEvent):
    """Event transitioning investigation from Resolution to Completed Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#ClosureEvent"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CompletedPhase(_cac_core.Phase):
    """Terminal phase indicating investigation has been fully concluded with all actions finalized."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#CompletedPhase"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ConcurrentInvestigationSituation(_cac_core.Situation):
    """Situation where multiple investigations run simultaneously, potentially sharing resources or evidence. Modeled as gUFO Situation with temporal overlap constraints."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#ConcurrentInvestigationSituation"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EventSequence(_cac_core.Event):
    """Ordered sequence of investigation events with temporal dependencies. Modeled as gUFO structured event pattern."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#EventSequence"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EvidenceTransitionEvent(PhaseTransitionEvent):
    """Event transitioning investigation from Legal Process to Evidence Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#EvidenceTransitionEvent"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InitiationEvent(PhaseTransitionEvent):
    """Event transitioning investigation from non-existence to Initial Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#InitiationEvent"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InvestigationLifecycle:
    """Complete temporal structure of CAC investigation from initiation to closure. Modeled as gUFO Kind with definite phase sequence and temporal constraints."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#InvestigationLifecycle"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class LegalProcessTransitionEvent(PhaseTransitionEvent):
    """Event transitioning investigation from Analysis to Legal Process Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#LegalProcessTransitionEvent"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MultiJurisdictionCoordinationSituation(_cac_core.Situation):
    """Situation where investigation requires coordination across multiple jurisdictions with timing synchronization. Modeled as gUFO Situation with coordination constraints."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#MultiJurisdictionCoordinationSituation"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ParallelEventCluster(_cac_core.Event):
    """Set of investigation events occurring simultaneously or with temporal overlap. Modeled as gUFO composite event pattern."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#ParallelEventCluster"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ParallelEvidenceCollectionSituation(_cac_core.Situation):
    """Situation where multiple evidence collection activities occur simultaneously across different phases. Modeled as gUFO Situation allowing phase overlap."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#ParallelEvidenceCollectionSituation"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ResolutionPhase(_cac_core.Phase):
    """Phase focused on resolution of investigation outcomes such as plea agreements, sentencing, and restitution orders."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#ResolutionPhase"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ResolutionTransitionEvent(PhaseTransitionEvent):
    """Event transitioning investigation from Evidence to Resolution Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#ResolutionTransitionEvent"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ResumptionEvent(_cac_core.Event):
    """Event causing investigation to exit suspended state and resume active phase. Modeled as gUFO Event terminating suspension situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#ResumptionEvent"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RoleConflictSituation(_cac_core.Situation):
    """Situation where person's multiple roles create potential conflict of interest. Modeled as gUFO Situation requiring resolution."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#RoleConflictSituation"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RoleTransition(_cac_core.Event):
    """Event representing change in person's role within investigation. Modeled as gUFO Event with role change effects."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#RoleTransition"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RoleEscalation(RoleTransition):
    """Role transition involving increased responsibility or authority (e.g., analyst to lead investigator)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#RoleEscalation"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RoleReassignment(RoleTransition):
    """Role transition involving change in assignment without authority change (e.g., different investigator)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#RoleReassignment"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SimultaneousRoleSituation(_cac_core.Situation):
    """Situation where person plays multiple roles simultaneously in investigation context. Modeled as gUFO Situation with role overlap."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#SimultaneousRoleSituation"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SuspendedSituation(_cac_core.Situation):
    """Situation where investigation is temporarily suspended pending resources, legal decisions, or external factors. Modeled as gUFO Situation with temporal duration."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#SuspendedSituation"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SuspensionEvent(_cac_core.Event):
    """Event causing investigation to enter suspended state. Modeled as gUFO Event creating suspension situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#SuspensionEvent"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class UrgentRescueLifecycle(InvestigationLifecycle):
    """Accelerated investigation lifecycle for urgent child rescue situations. Compressed phase durations with parallel processing."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/temporal#UrgentRescueLifecycle"
    NAMESPACE_PREFIX: str = "cacontology-temporal"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
