"""CAC Ontology - Crimes Against Children — cacontology-extremist-enterprises module."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AccelerationistGroup:
    """Extremist group with accelerationist goals seeking to hasten societal collapse through criminal activities including child exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#AccelerationistGroup"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    has_network_component: list[EnduringEntity] = field(default_factory=list)
    has_network_notoriety_quality: Optional[Quality] = field(default=None)
    ideological_framework: Optional[str] = field(default=None)
    network_notoriety: Optional[str] = field(default=None)
    network_size: Optional[int] = field(default=None)
    operational_scope: Optional[str] = field(default=None)


@dataclass
class AccessControlSystem:
    """System controlling access to enterprise channels and resources based on member status and content contributions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#AccessControlSystem"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    uses_as_currency: list[Lorebook] = field(default_factory=list)


@dataclass
class AlternateAccountSystem:
    """System of alternate accounts (alts) used to evade platform restrictions and maintain operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#AlternateAccountSystem"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    alt_account_count: Optional[int] = field(default=None)


@dataclass
class AnimalAbuseCoercion:
    """Coercion of victims to abuse pets or animals as part of exploitation and control."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#AnimalAbuseCoercion"
    degradation_level: Optional[str] = field(default=None)


@dataclass
class ChildExploitationEnterprise:
    """Criminal enterprise as defined in 18 U.S.C. § 2252A(g) engaging in coordinated child exploitation activities with multiple participants and systematic operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#ChildExploitationEnterprise"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    has_exploitation_relation: list[Relator] = field(default_factory=list)
    has_hierarchy: Optional[EnterpriseHierarchy] = field(default=None)
    has_leadership_relation: list[Relator] = field(default_factory=list)
    has_member: list[Person] = field(default_factory=list)
    has_operational_begin_date: Optional[TypedLiteral] = field(default=None)
    has_operational_end_date: Optional[TypedLiteral] = field(default=None)
    leadership_count: Optional[int] = field(default=None)
    membership_requirements: Optional[str] = field(default=None)
    operates_in_situation: list[Situation] = field(default_factory=list)


@dataclass
class ContentBasedRecruitment:
    """Recruitment of new members based on quality and notoriety of content they produce."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#ContentBasedRecruitment"


@dataclass
class ContentCompilationSystem:
    """System for compiling, editing, and organizing exploitative content within criminal enterprise."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#ContentCompilationSystem"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)


@dataclass
class ContentCurationAction:
    """Action of curating and organizing exploitative content for enterprise purposes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#ContentCurationAction"


@dataclass
class ContentCurrencySystem:
    """System using exploitative content as valuable currency within criminal enterprise for advancement and access."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#ContentCurrencySystem"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    uses_as_currency: list[Lorebook] = field(default_factory=list)


@dataclass
class ContentEditingProcess:
    """Process of editing and organizing victim content into compilations for enterprise distribution."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#ContentEditingProcess"
    editing_quality: Optional[str] = field(default=None)


@dataclass
class ContentProducerRole:
    """Role focused on producing high-quality exploitative content for enterprise operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#ContentProducerRole"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)


@dataclass
class ContentValueAssessment:
    """Assessment of content value based on quality, notoriety, and enterprise utility."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#ContentValueAssessment"
    content_value: Optional[float] = field(default=None)


@dataclass
class CoordinatorRole:
    """Role coordinating activities across different platforms and channels within enterprise."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#CoordinatorRole"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)


@dataclass
class CovertEmployeeOperation:
    """Operation using online covert employees (OCE) to infiltrate and monitor extremist networks."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#CovertEmployeeOperation"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    action_count: Optional[int] = field(default=None)
    action_status: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    environment: Optional[UcoObject] = field(default=None)
    error: list[UcoObject] = field(default_factory=list)
    instrument: list[UcoObject] = field(default_factory=list)
    location: list[Location] = field(default_factory=list)
    object: list[UcoObject] = field(default_factory=list)
    participant: list[UcoObject] = field(default_factory=list)
    performer: Optional[UcoObject] = field(default=None)
    result: list[UcoObject] = field(default_factory=list)
    start_time: Optional[datetime] = field(default=None)
    subaction: list[Action] = field(default_factory=list)
    was_informed_by: list[InvestigativeAction] = field(default_factory=list)
    evidence_quality: Optional[str] = field(default=None)


@dataclass
class CrossPlatformCoordination:
    """Coordination of enterprise activities across multiple internet platforms and channels."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#CrossPlatformCoordination"
    platform_count: Optional[int] = field(default=None)


@dataclass
class CrossPlatformEvidenceCorrelation:
    """Correlation of evidence across multiple platforms to establish identity and network connections."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#CrossPlatformEvidenceCorrelation"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    action_count: Optional[int] = field(default=None)
    action_status: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    environment: Optional[UcoObject] = field(default=None)
    error: list[UcoObject] = field(default_factory=list)
    instrument: list[UcoObject] = field(default_factory=list)
    location: list[Location] = field(default_factory=list)
    object: list[UcoObject] = field(default_factory=list)
    participant: list[UcoObject] = field(default_factory=list)
    performer: Optional[UcoObject] = field(default=None)
    result: list[UcoObject] = field(default_factory=list)
    start_time: Optional[datetime] = field(default=None)
    subaction: list[Action] = field(default_factory=list)
    was_informed_by: list[InvestigativeAction] = field(default_factory=list)


@dataclass
class CyberExtremistNetwork:
    """Extremist network operating primarily through digital platforms and encrypted communications."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#CyberExtremistNetwork"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    has_network_component: list[EnduringEntity] = field(default_factory=list)
    has_network_notoriety_quality: Optional[Quality] = field(default=None)
    ideological_framework: Optional[str] = field(default=None)
    network_notoriety: Optional[str] = field(default=None)
    network_size: Optional[int] = field(default=None)
    operational_scope: Optional[str] = field(default=None)


@dataclass
class EncryptedChannelInfiltration:
    """Infiltration of encrypted channels used by extremist networks for evidence collection."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#EncryptedChannelInfiltration"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    action_count: Optional[int] = field(default=None)
    action_status: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    environment: Optional[UcoObject] = field(default=None)
    error: list[UcoObject] = field(default_factory=list)
    instrument: list[UcoObject] = field(default_factory=list)
    location: list[Location] = field(default_factory=list)
    object: list[UcoObject] = field(default_factory=list)
    participant: list[UcoObject] = field(default_factory=list)
    performer: Optional[UcoObject] = field(default=None)
    result: list[UcoObject] = field(default_factory=list)
    start_time: Optional[datetime] = field(default=None)
    subaction: list[Action] = field(default_factory=list)
    was_informed_by: list[InvestigativeAction] = field(default_factory=list)
    evidence_quality: Optional[str] = field(default=None)
    infiltration_duration: Optional[float] = field(default=None)


@dataclass
class EncryptedChannelNetwork:
    """Network of encrypted messaging channels used for enterprise coordination and content sharing."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#EncryptedChannelNetwork"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    has_changed: Optional[bool] = field(default=None)
    state: Optional[str] = field(default=None)
    channel_count: Optional[int] = field(default=None)
    encryption_level: Optional[str] = field(default=None)
    has_encryption_capability: Optional[IntrinsicMode] = field(default=None)


@dataclass
class EnterpriseHierarchy:
    """Organizational hierarchy within child exploitation enterprise defining leadership and member roles."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#EnterpriseHierarchy"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    hierarchy_complexity: Optional[str] = field(default=None)


@dataclass
class EnterpriseLeaderRole:
    """Leadership role within child exploitation enterprise, directing and coordinating activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#EnterpriseLeaderRole"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)


@dataclass
class EnterpriseRole:
    """Role within child exploitation enterprise structure."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#EnterpriseRole"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)


@dataclass
class ExtremeDegradationCoercion:
    """Coercion of victims to engage in extreme degrading activities beyond typical exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#ExtremeDegradationCoercion"
    degradation_level: Optional[str] = field(default=None)


@dataclass
class ExtremistNetworkCell:
    """Operational cell within larger extremist network conducting specialized activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#ExtremistNetworkCell"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    has_network_component: list[EnduringEntity] = field(default_factory=list)
    has_network_notoriety_quality: Optional[Quality] = field(default=None)
    ideological_framework: Optional[str] = field(default=None)
    network_notoriety: Optional[str] = field(default=None)
    network_size: Optional[int] = field(default=None)
    operational_scope: Optional[str] = field(default=None)


@dataclass
class IdentityCorrelationAnalysis:
    """Analysis correlating multiple accounts and identities across platforms to establish single individual control."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#IdentityCorrelationAnalysis"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    action_count: Optional[int] = field(default=None)
    action_status: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    environment: Optional[UcoObject] = field(default=None)
    error: list[UcoObject] = field(default_factory=list)
    instrument: list[UcoObject] = field(default_factory=list)
    location: list[Location] = field(default_factory=list)
    object: list[UcoObject] = field(default_factory=list)
    participant: list[UcoObject] = field(default_factory=list)
    performer: Optional[UcoObject] = field(default=None)
    result: list[UcoObject] = field(default_factory=list)
    start_time: Optional[datetime] = field(default=None)
    subaction: list[Action] = field(default_factory=list)
    was_informed_by: list[InvestigativeAction] = field(default_factory=list)
    identity_correlation_accuracy: Optional[float] = field(default=None)


@dataclass
class InnerCore:
    """Elite inner core of enterprise members with access to restricted channels and advanced activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#InnerCore"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    hierarchy_complexity: Optional[str] = field(default=None)
    inner_core_size: Optional[int] = field(default=None)


@dataclass
class InnerCoreMemberRole:
    """Role of member within enterprise inner core with access to restricted channels and advanced operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#InnerCoreMemberRole"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)


@dataclass
class LeadershipStructure:
    """Leadership structure of enterprise including multiple leaders and their areas of control."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#LeadershipStructure"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    hierarchy_complexity: Optional[str] = field(default=None)


@dataclass
class Lorebook:
    """Edited compilation of victim content including images, videos, and personal information organized by enterprise members."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#Lorebook"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    has_changed: Optional[bool] = field(default=None)
    state: Optional[str] = field(default=None)
    compilation_complexity: Optional[str] = field(default=None)
    contains_victim_content: list[ObservableObject] = field(default_factory=list)
    content_notoriety: Optional[str] = field(default=None)
    content_volume_items: Optional[int] = field(default=None)


@dataclass
class MembershipAdvancementSystem:
    """System governing member advancement within enterprise based on content contributions and activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#MembershipAdvancementSystem"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    uses_as_currency: list[Lorebook] = field(default_factory=list)
    advancement_criteria: Optional[str] = field(default=None)


@dataclass
class MembershipTier:
    """Membership tier within enterprise hierarchy determining access and privileges."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#MembershipTier"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    hierarchy_complexity: Optional[str] = field(default=None)
    access_level: Optional[str] = field(default=None)
    membership_level: Optional[str] = field(default=None)


@dataclass
class MentalHealthVulnerabilityTargeting:
    """Targeting of minors with mental health challenges and psychological vulnerabilities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#MentalHealthVulnerabilityTargeting"
    targeting_precision: Optional[str] = field(default=None)
    vulnerability_type: Optional[str] = field(default=None)


@dataclass
class NameCuttingCoercion:
    """Coercion of victims to cut enterprise member names into their bodies as ownership marking."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#NameCuttingCoercion"
    coercion_effectiveness: Optional[float] = field(default=None)
    coercion_severity: Optional[str] = field(default=None)
    creates_victimization_situation: list[Situation] = field(default_factory=list)
    has_coercion_event_begin_date: Optional[TypedLiteral] = field(default=None)
    self_harm_type: Optional[str] = field(default=None)


@dataclass
class NetworkMappingInvestigation:
    """Investigation mapping the structure and relationships within extremist child exploitation networks."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#NetworkMappingInvestigation"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    action_count: Optional[int] = field(default=None)
    action_status: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    environment: Optional[UcoObject] = field(default=None)
    error: list[UcoObject] = field(default_factory=list)
    instrument: list[UcoObject] = field(default_factory=list)
    location: list[Location] = field(default_factory=list)
    object: list[UcoObject] = field(default_factory=list)
    participant: list[UcoObject] = field(default_factory=list)
    performer: Optional[UcoObject] = field(default=None)
    result: list[UcoObject] = field(default_factory=list)
    start_time: Optional[datetime] = field(default=None)
    subaction: list[Action] = field(default_factory=list)
    was_informed_by: list[InvestigativeAction] = field(default_factory=list)
    network_mapping_completeness: Optional[float] = field(default=None)


@dataclass
class NihilisticViolentExtremismNetwork:
    """Criminal network engaging in child exploitation as part of broader nihilistic violent extremism goals including social unrest and downfall of current world order (e.g., 764 network)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#NihilisticViolentExtremismNetwork"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    has_network_component: list[EnduringEntity] = field(default_factory=list)
    has_network_notoriety_quality: Optional[Quality] = field(default=None)
    ideological_framework: Optional[str] = field(default=None)
    network_notoriety: Optional[str] = field(default=None)
    network_size: Optional[int] = field(default=None)
    operational_scope: Optional[str] = field(default=None)


@dataclass
class PlatformMigrationStrategy:
    """Strategy for migrating operations between platforms when accounts are terminated or restricted."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#PlatformMigrationStrategy"


@dataclass
class PrivateGroupManagement:
    """Management of private groups and channels with restricted access for enterprise operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#PrivateGroupManagement"


@dataclass
class RecruitmentHierarchy:
    """Hierarchy governing recruitment of new members based on content quality and notoriety."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#RecruitmentHierarchy"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    hierarchy_complexity: Optional[str] = field(default=None)


@dataclass
class RecruitmentSpecialistRole:
    """Role specializing in recruiting new members based on content quality and enterprise needs."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#RecruitmentSpecialistRole"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)


@dataclass
class SelfHarmCoercion:
    """Coercion of victims to engage in self-harm activities including cutting, burning, and extreme degradation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#SelfHarmCoercion"
    coercion_effectiveness: Optional[float] = field(default=None)
    coercion_severity: Optional[str] = field(default=None)
    creates_victimization_situation: list[Situation] = field(default_factory=list)
    has_coercion_event_begin_date: Optional[TypedLiteral] = field(default=None)
    self_harm_type: Optional[str] = field(default=None)


@dataclass
class SelfImmolationCoercion:
    """Coercion of victims to set themselves on fire or engage in burning activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#SelfImmolationCoercion"
    coercion_effectiveness: Optional[float] = field(default=None)
    coercion_severity: Optional[str] = field(default=None)
    creates_victimization_situation: list[Situation] = field(default_factory=list)
    has_coercion_event_begin_date: Optional[TypedLiteral] = field(default=None)
    self_harm_type: Optional[str] = field(default=None)


@dataclass
class SiblingAbuseCoercion:
    """Coercion of victims to abuse siblings or family members as part of exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#SiblingAbuseCoercion"
    degradation_level: Optional[str] = field(default=None)


@dataclass
class SocialEngineeringCampaign:
    """Systematic social engineering campaign to gain victim trust and facilitate exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#SocialEngineeringCampaign"
    social_engineering_complexity: Optional[str] = field(default=None)


@dataclass
class SuicideCoercion:
    """Coercion of victims toward suicide as ultimate form of exploitation and control."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#SuicideCoercion"
    degradation_level: Optional[str] = field(default=None)


@dataclass
class TrustBuildingProcess:
    """Process of building trust with vulnerable victims before exploitation begins."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#TrustBuildingProcess"
    social_engineering_complexity: Optional[str] = field(default=None)
    trust_building_duration: Optional[float] = field(default=None)


@dataclass
class VictimContentCompilation:
    """Organized compilation of content obtained from specific victim through exploitation and coercion."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#VictimContentCompilation"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    has_changed: Optional[bool] = field(default=None)
    state: Optional[str] = field(default=None)
    compilation_complexity: Optional[str] = field(default=None)
    contains_victim_content: list[ObservableObject] = field(default_factory=list)
    content_notoriety: Optional[str] = field(default=None)
    content_volume_items: Optional[int] = field(default=None)


@dataclass
class VictimProfileDevelopment:
    """Development of detailed victim profiles including vulnerabilities and exploitation opportunities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#VictimProfileDevelopment"


@dataclass
class VulnerablePopulationTargeting:
    """Systematic targeting of vulnerable populations including minors with mental health challenges."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#VulnerablePopulationTargeting"
    targeting_precision: Optional[str] = field(default=None)
    vulnerability_type: Optional[str] = field(default=None)

