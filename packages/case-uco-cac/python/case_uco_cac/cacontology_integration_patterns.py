"""CAC Ontology - Crimes Against Children — cacontology_integration_patterns module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar, Optional

from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AIGenerationPattern", "CapabilityPattern", "CompliancePattern", "CoordinationSituationPattern", "CriminalOrganizationPattern", "CrossBorderPattern", "EducationalPattern", "EvidenceObjectPattern", "ForensicsLifecyclePattern", "HighPriorityModule", "IdeologyPattern", "InstitutionalRolePattern", "JudicialPhasePattern", "LegalEventPattern", "LowPriorityModule", "MediumPriorityModule", "ModuleIntegrationStrategy", "OntologicalConsistency", "OrganizationalPattern", "Phase3Wave1", "Phase3Wave2", "Phase3Wave3", "PhaseConsistency", "PreventiveActionPattern", "RegistrationPattern", "RoleConsistency", "SpecializedRolePattern", "SyntheticArtifactPattern", "TaskforceRolePattern", "TemporalConsistency", "TotalPhase3Implementation", "TreatyPattern", "ValidationStrategy"]


@dataclass
class AIGenerationPattern:
    """gUFO pattern for modeling AI generation processes creating synthetic CSAM with algorithmic characteristics."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#AIGenerationPattern"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CapabilityPattern:
    """gUFO pattern for modeling specialized capabilities as intrinsic properties of organizations or individuals."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#CapabilityPattern"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CompliancePattern(_cac_core.Situation):
    """gUFO pattern for modeling compliance with registration requirements as temporal situation with monitoring."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#CompliancePattern"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CoordinationSituationPattern(_cac_core.Situation):
    """gUFO pattern for modeling multi-jurisdiction coordination situations with participating organizations and temporal constraints."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#CoordinationSituationPattern"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CriminalOrganizationPattern(_cac_core.OrganizationLikeEntity):
    """gUFO pattern for modeling criminal enterprises with hierarchical structure and operational patterns."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#CriminalOrganizationPattern"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CrossBorderPattern(_cac_core.Situation):
    """gUFO pattern for modeling cross-border investigations as complex situations spanning multiple jurisdictions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#CrossBorderPattern"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EducationalPattern:
    """gUFO pattern for modeling educational interventions as processes with learning outcomes and effectiveness measures."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#EducationalPattern"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class EvidenceObjectPattern(_cac_core.Artifact):
    """gUFO pattern for modeling digital evidence as Objects with intrinsic properties and forensic lifecycle phases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#EvidenceObjectPattern"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ForensicsLifecyclePattern:
    """gUFO pattern for modeling forensics process lifecycle with acquisition, analysis, and presentation phases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#ForensicsLifecyclePattern"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ModuleIntegrationStrategy:
    """Framework for systematically integrating gUFO concepts into CAC ontology modules. Defines patterns, priorities, and validation approaches."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#ModuleIntegrationStrategy"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class HighPriorityModule(ModuleIntegrationStrategy):
    """CAC module requiring immediate gUFO integration due to core investigation role or external dependency."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#HighPriorityModule"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class IdeologyPattern:
    """gUFO pattern for modeling extremist ideologies as belief systems influencing criminal behavior."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#IdeologyPattern"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class InstitutionalRolePattern(_cac_core.Role):
    """gUFO pattern for modeling institutional roles in multi-jurisdiction contexts with authority and responsibility boundaries."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#InstitutionalRolePattern"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class JudicialPhasePattern(_cac_core.Phase):
    """gUFO pattern for modeling judicial process phases (pre-trial, trial, sentencing, appeals) with legal constraints."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#JudicialPhasePattern"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegalEventPattern(_cac_core.LegalEvent):
    """gUFO pattern for modeling legal events (hearings, sentencing, appeals) with temporal boundaries and legal effects."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#LegalEventPattern"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LowPriorityModule(ModuleIntegrationStrategy):
    """CAC module requiring gUFO integration in final wave, with specialized or advanced features."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#LowPriorityModule"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MediumPriorityModule(ModuleIntegrationStrategy):
    """CAC module requiring gUFO integration in second wave, building on high-priority foundation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#MediumPriorityModule"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ValidationStrategy:
    """Framework for validating gUFO integration across CAC modules ensuring consistency and correctness."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#ValidationStrategy"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class OntologicalConsistency(ValidationStrategy):
    """Validation ensuring proper use of gUFO meta-ontological categories and constraints across modules."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#OntologicalConsistency"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OrganizationalPattern(_cac_core.OrganizationLikeEntity):
    """gUFO pattern for modeling CAC taskforces and law enforcement organizations with structure and capabilities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#OrganizationalPattern"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Phase3Wave1:
    """First wave implementing high-priority modules (forensics, multi-jurisdiction, legal outcomes, taskforce)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#Phase3Wave1"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class Phase3Wave2:
    """Second wave implementing medium-priority modules (specialized units, registry, prevention, international)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#Phase3Wave2"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class Phase3Wave3:
    """Third wave implementing low-priority modules (AI CSAM, extremist enterprises, advanced features)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#Phase3Wave3"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PhaseConsistency(ValidationStrategy):
    """Validation ensuring phase modeling follows gUFO intrinsic constraints and proper transition semantics."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#PhaseConsistency"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PreventiveActionPattern(_cac_core.SupportEvent):
    """gUFO pattern for modeling prevention activities as actions with preventive intent and outcome measurement."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#PreventiveActionPattern"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RegistrationPattern(_cac_core.Situation):
    """gUFO pattern for modeling sex offender registration as ongoing situation with compliance requirements."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#RegistrationPattern"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RoleConsistency(ValidationStrategy):
    """Validation ensuring role modeling follows gUFO anti-rigidity constraints and proper inheritance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#RoleConsistency"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SpecializedRolePattern(_cac_core.Role):
    """gUFO pattern for modeling specialized investigative roles with specific capabilities and training requirements."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#SpecializedRolePattern"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SyntheticArtifactPattern(_cac_core.Artifact):
    """gUFO pattern for modeling AI-generated artifacts with synthetic properties and detection characteristics."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#SyntheticArtifactPattern"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TaskforceRolePattern(_cac_core.Role):
    """gUFO pattern for modeling roles within CAC taskforces with specialization and coordination relationships."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#TaskforceRolePattern"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TemporalConsistency(ValidationStrategy):
    """Validation ensuring temporal relationships and constraints are properly modeled across modules."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#TemporalConsistency"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TotalPhase3Implementation:
    """Complete Phase 3 implementation across all CAC modules with validation and testing."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#TotalPhase3Implementation"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class TreatyPattern:
    """gUFO pattern for modeling international treaties and agreements as normative frameworks governing cooperation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/integration-patterns#TreatyPattern"
    NAMESPACE_PREFIX: str = "cacontology-integration-patterns"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
