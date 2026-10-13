"""CAC Ontology - Crimes Against Children — cacontology_extremist_enterprises module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar, Optional, Union

import case_uco.uco.core as _uco_core
import case_uco.uco.identity as _uco_identity
import case_uco.uco.observable as _uco_observable
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AccelerationistGroup", "AccessControlSystem", "AlternateAccountSystem", "AnimalAbuseCoercion", "ChildExploitationEnterprise", "ContentBasedRecruitment", "ContentCompilationSystem", "ContentCurationAction", "ContentCurrencySystem", "ContentEditingProcess", "ContentProducerRole", "ContentValueAssessment", "CoordinatorRole", "CovertEmployeeOperation", "CrossPlatformCoordination", "CrossPlatformEvidenceCorrelation", "CyberExtremistNetwork", "EncryptedChannelInfiltration", "EncryptedChannelNetwork", "EnterpriseHierarchy", "EnterpriseLeaderRole", "EnterpriseRole", "ExtremeDegradationCoercion", "ExtremistNetworkCell", "IdentityCorrelationAnalysis", "InnerCore", "InnerCoreMemberRole", "LeadershipStructure", "Lorebook", "MembershipAdvancementSystem", "MembershipTier", "MentalHealthVulnerabilityTargeting", "NameCuttingCoercion", "NetworkMappingInvestigation", "NihilisticViolentExtremismNetwork", "PlatformMigrationStrategy", "PrivateGroupManagement", "RecruitmentHierarchy", "RecruitmentSpecialistRole", "SelfHarmCoercion", "SelfImmolationCoercion", "SiblingAbuseCoercion", "SocialEngineeringCampaign", "SuicideCoercion", "TrustBuildingProcess", "VictimContentCompilation", "VictimProfileDevelopment", "VulnerablePopulationTargeting"]


@dataclass
class NihilisticViolentExtremismNetwork(_uco_identity.Organization):
    """Criminal network engaging in child exploitation as part of broader nihilistic violent extremism goals including social unrest and downfall of current world order (e.g., 764 network)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#NihilisticViolentExtremismNetwork"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_network_component: list[EnduringEntity] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-extremist-enterprises:hasNetworkComponent', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'https://cacontology.projectvic.org/core#EnduringEntity', 'alternate_range_iris': []})
    has_network_notoriety_quality: Optional[Quality] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:hasNetworkNotorietyQuality', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://purl.org/nemo/gufo#Quality', 'alternate_range_iris': []})
    ideological_framework: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:ideologicalFramework', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    network_notoriety: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:networkNotoriety', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    network_size: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:networkSize', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    operational_scope: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:operationalScope', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class AccelerationistGroup(NihilisticViolentExtremismNetwork):
    """Extremist group with accelerationist goals seeking to hasten societal collapse through criminal activities including child exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#AccelerationistGroup"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ContentCurrencySystem(_uco_core.UcoObject):
    """System using exploitative content as valuable currency within criminal enterprise for advancement and access."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#ContentCurrencySystem"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    uses_as_currency: list[Lorebook] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-extremist-enterprises:usesAsCurrency', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org/extremist-enterprises#Lorebook', 'alternate_range_iris': []})


@dataclass
class AccessControlSystem(ContentCurrencySystem):
    """System controlling access to enterprise channels and resources based on member status and content contributions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#AccessControlSystem"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AlternateAccountSystem(_uco_core.UcoObject):
    """System of alternate accounts (alts) used to evade platform restrictions and maintain operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#AlternateAccountSystem"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    alt_account_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:altAccountCount', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class AnimalAbuseCoercion(_cac_core.Event):
    """Coercion of victims to abuse pets or animals as part of exploitation and control."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#AnimalAbuseCoercion"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ChildExploitationEnterprise(_uco_identity.Organization):
    """Criminal enterprise as defined in 18 U.S.C. § 2252A(g) engaging in coordinated child exploitation activities with multiple participants and systematic operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#ChildExploitationEnterprise"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_exploitation_relation: list[Relator] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-extremist-enterprises:hasExploitationRelation', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://purl.org/nemo/gufo#Relator', 'alternate_range_iris': []})
    has_hierarchy: Optional[EnterpriseHierarchy] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:hasHierarchy', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://cacontology.projectvic.org/extremist-enterprises#EnterpriseHierarchy', 'alternate_range_iris': []})
    has_leadership_relation: list[Relator] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-extremist-enterprises:hasLeadershipRelation', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://purl.org/nemo/gufo#Relator', 'alternate_range_iris': []})
    has_member: list[Person] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-extremist-enterprises:hasMember', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/identity/Person', 'alternate_range_iris': []})
    has_operational_begin_date: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:hasOperationalBeginDate', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_operational_end_date: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:hasOperationalEndDate', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    leadership_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:leadershipCount', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    membership_requirements: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:membershipRequirements', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    operates_in_situation: list[Situation] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-extremist-enterprises:operatesInSituation', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'https://cacontology.projectvic.org/core#Situation', 'alternate_range_iris': []})


@dataclass
class ContentBasedRecruitment(_cac_core.ExploitationEvent):
    """Recruitment of new members based on quality and notoriety of content they produce."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#ContentBasedRecruitment"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ContentCompilationSystem(_uco_core.UcoObject):
    """System for compiling, editing, and organizing exploitative content within criminal enterprise."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#ContentCompilationSystem"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ContentCurationAction(_cac_core.ExploitationEvent):
    """Action of curating and organizing exploitative content for enterprise purposes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#ContentCurationAction"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ContentEditingProcess(_cac_core.ExploitationEvent):
    """Process of editing and organizing victim content into compilations for enterprise distribution."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#ContentEditingProcess"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    editing_quality: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:editingQuality', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class EnterpriseRole(_cac_core.Role):
    """Role within child exploitation enterprise structure."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#EnterpriseRole"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ContentProducerRole(EnterpriseRole):
    """Role focused on producing high-quality exploitative content for enterprise operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#ContentProducerRole"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ContentValueAssessment(_cac_core.ExploitationEvent):
    """Assessment of content value based on quality, notoriety, and enterprise utility."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#ContentValueAssessment"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    content_value: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:contentValue', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class CoordinatorRole(EnterpriseRole):
    """Role coordinating activities across different platforms and channels within enterprise."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#CoordinatorRole"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CovertEmployeeOperation(_cac_core.InvestigativeAction):
    """Operation using online covert employees (OCE) to infiltrate and monitor extremist networks."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#CovertEmployeeOperation"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    evidence_quality: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:evidenceQuality', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CrossPlatformCoordination(_cac_core.ExploitationEvent):
    """Coordination of enterprise activities across multiple internet platforms and channels."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#CrossPlatformCoordination"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    platform_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:platformCount', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class CrossPlatformEvidenceCorrelation(_cac_core.InvestigativeAction):
    """Correlation of evidence across multiple platforms to establish identity and network connections."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#CrossPlatformEvidenceCorrelation"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CyberExtremistNetwork(NihilisticViolentExtremismNetwork):
    """Extremist network operating primarily through digital platforms and encrypted communications."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#CyberExtremistNetwork"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EncryptedChannelInfiltration(CovertEmployeeOperation):
    """Infiltration of encrypted channels used by extremist networks for evidence collection."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#EncryptedChannelInfiltration"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    infiltration_duration: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:infiltrationDuration', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class EncryptedChannelNetwork(_uco_observable.ObservableObject):
    """Network of encrypted messaging channels used for enterprise coordination and content sharing."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#EncryptedChannelNetwork"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    channel_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:channelCount', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    encryption_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:encryptionLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_encryption_capability: Optional[IntrinsicMode] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:hasEncryptionCapability', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://purl.org/nemo/gufo#IntrinsicMode', 'alternate_range_iris': []})


@dataclass
class EnterpriseHierarchy(_uco_core.UcoObject):
    """Organizational hierarchy within child exploitation enterprise defining leadership and member roles."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#EnterpriseHierarchy"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    hierarchy_complexity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:hierarchyComplexity', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class EnterpriseLeaderRole(EnterpriseRole):
    """Leadership role within child exploitation enterprise, directing and coordinating activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#EnterpriseLeaderRole"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ExtremeDegradationCoercion(_cac_core.Event):
    """Coercion of victims to engage in extreme degrading activities beyond typical exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#ExtremeDegradationCoercion"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    degradation_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:degradationLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ExtremistNetworkCell(NihilisticViolentExtremismNetwork):
    """Operational cell within larger extremist network conducting specialized activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#ExtremistNetworkCell"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class IdentityCorrelationAnalysis(CrossPlatformEvidenceCorrelation):
    """Analysis correlating multiple accounts and identities across platforms to establish single individual control."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#IdentityCorrelationAnalysis"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    identity_correlation_accuracy: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:identityCorrelationAccuracy', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class InnerCore(EnterpriseHierarchy):
    """Elite inner core of enterprise members with access to restricted channels and advanced activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#InnerCore"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    inner_core_size: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:innerCoreSize', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class InnerCoreMemberRole(EnterpriseRole):
    """Role of member within enterprise inner core with access to restricted channels and advanced operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#InnerCoreMemberRole"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LeadershipStructure(EnterpriseHierarchy):
    """Leadership structure of enterprise including multiple leaders and their areas of control."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#LeadershipStructure"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Lorebook(_uco_observable.ObservableObject):
    """Edited compilation of victim content including images, videos, and personal information organized by enterprise members."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#Lorebook"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    compilation_complexity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:compilationComplexity', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    contains_victim_content: list[ObservableObject] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-extremist-enterprises:containsVictimContent', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/observable/ObservableObject', 'alternate_range_iris': []})
    content_notoriety: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:contentNotoriety', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    content_volume_items: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:contentVolumeItems', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class MembershipAdvancementSystem(ContentCurrencySystem):
    """System governing member advancement within enterprise based on content contributions and activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#MembershipAdvancementSystem"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    advancement_criteria: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:advancementCriteria', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class MembershipTier(EnterpriseHierarchy):
    """Membership tier within enterprise hierarchy determining access and privileges."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#MembershipTier"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    access_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:accessLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    membership_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:membershipLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class MentalHealthVulnerabilityTargeting(_cac_core.Event):
    """Targeting of minors with mental health challenges and psychological vulnerabilities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#MentalHealthVulnerabilityTargeting"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class NameCuttingCoercion(_cac_core.Event):
    """Coercion of victims to cut enterprise member names into their bodies as ownership marking."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#NameCuttingCoercion"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class NetworkMappingInvestigation(_cac_core.InvestigativeAction):
    """Investigation mapping the structure and relationships within extremist child exploitation networks."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#NetworkMappingInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    network_mapping_completeness: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:networkMappingCompleteness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class PlatformMigrationStrategy(_cac_core.ExploitationEvent):
    """Strategy for migrating operations between platforms when accounts are terminated or restricted."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#PlatformMigrationStrategy"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PrivateGroupManagement(_cac_core.ExploitationEvent):
    """Management of private groups and channels with restricted access for enterprise operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#PrivateGroupManagement"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RecruitmentHierarchy(EnterpriseHierarchy):
    """Hierarchy governing recruitment of new members based on content quality and notoriety."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#RecruitmentHierarchy"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RecruitmentSpecialistRole(EnterpriseRole):
    """Role specializing in recruiting new members based on content quality and enterprise needs."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#RecruitmentSpecialistRole"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SelfHarmCoercion(_cac_core.ExploitationEvent):
    """Coercion of victims to engage in self-harm activities including cutting, burning, and extreme degradation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#SelfHarmCoercion"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    coercion_effectiveness: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:coercionEffectiveness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    coercion_severity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:coercionSeverity', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    creates_victimization_situation: list[Situation] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-extremist-enterprises:createsVictimizationSituation', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org/core#Situation', 'alternate_range_iris': []})
    has_coercion_event_begin_date: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:hasCoercionEventBeginDate', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    self_harm_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:selfHarmType', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SelfImmolationCoercion(_cac_core.Event):
    """Coercion of victims to set themselves on fire or engage in burning activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#SelfImmolationCoercion"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SiblingAbuseCoercion(_cac_core.Event):
    """Coercion of victims to abuse siblings or family members as part of exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#SiblingAbuseCoercion"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SocialEngineeringCampaign(_cac_core.ExploitationEvent):
    """Systematic social engineering campaign to gain victim trust and facilitate exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#SocialEngineeringCampaign"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    social_engineering_complexity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:socialEngineeringComplexity', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SuicideCoercion(_cac_core.Event):
    """Coercion of victims toward suicide as ultimate form of exploitation and control."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#SuicideCoercion"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TrustBuildingProcess(_cac_core.Event):
    """Process of building trust with vulnerable victims before exploitation begins."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#TrustBuildingProcess"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    trust_building_duration: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:trustBuildingDuration', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class VictimContentCompilation(Lorebook):
    """Organized compilation of content obtained from specific victim through exploitation and coercion."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#VictimContentCompilation"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimProfileDevelopment(_cac_core.ExploitationEvent):
    """Development of detailed victim profiles including vulnerabilities and exploitation opportunities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#VictimProfileDevelopment"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VulnerablePopulationTargeting(_cac_core.ExploitationEvent):
    """Systematic targeting of vulnerable populations including minors with mental health challenges."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/extremist-enterprises#VulnerablePopulationTargeting"
    NAMESPACE_PREFIX: str = "cacontology-extremist-enterprises"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    targeting_precision: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:targetingPrecision', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    vulnerability_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-extremist-enterprises:vulnerabilityType', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
