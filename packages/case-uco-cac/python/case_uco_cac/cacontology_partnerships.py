"""CAC Ontology - Crimes Against Children — cacontology_partnerships module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar, Optional

import case_uco.uco.observable as _uco_observable
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AICooperation", "AcademicPartner", "AcademicPartnership", "ActiveCooperationPhase", "CivilSocietyEngagement", "CivilSocietyPartner", "CollaborativeInvestigationSituation", "CommunityAnalysis", "ContentDetectionCooperation", "CoordinationMechanism", "CrowdsourcingInvestigation", "DataSharingAgreement", "EmergencyCoordination", "EvaluationPhase", "GeolocationRequest", "HashSharingProtocol", "InformationSharingFramework", "InformationSharingSituation", "IntelligenceSharing", "JointOperation", "LawEnforcementPartner", "MultiStakeholderInitiative", "NGOCoordination", "NGOPartner", "OSINTInvestigation", "ObjectIdentificationRequest", "PartnerRole", "PartnershipFormationPhase", "PlatformMonitoring", "PublicPrivatePartnership", "PublicTip", "RegularMeeting", "RenewalPhase", "TaskForceCoordination", "TechIndustryCooperation", "TechnicalIntegration", "TechnologyCooperation", "TechnologyPartner", "ToolDevelopment"]


@dataclass
class TechnologyCooperation(_cac_core.CoordinationEvent):
    """Cooperation in developing and deploying technology solutions for child protection. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#TechnologyCooperation"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AICooperation(TechnologyCooperation):
    """Cooperation in developing AI-based solutions for detection, analysis, and prevention of child exploitation. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#AICooperation"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PartnerRole(_cac_core.Role):
    """Role played by an organization within a public-private partnership framework. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#PartnerRole"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AcademicPartner(PartnerRole):
    """Academic institution participating in partnership with research and training capabilities. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#AcademicPartner"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PublicPrivatePartnership(_cac_core.OrganizationLikeEntity):
    """Formal partnership between government/law enforcement agencies and private sector organizations for child protection initiatives. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#PublicPrivatePartnership"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AcademicPartnership(PublicPrivatePartnership):
    """Partnership with academic institutions for research, training, and technology development in child protection. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#AcademicPartnership"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ActiveCooperationPhase(_cac_core.Phase):
    """Phase of active cooperation with joint operations and information sharing. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#ActiveCooperationPhase"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CivilSocietyEngagement(PublicPrivatePartnership):
    """Framework for engaging civil society, volunteers, and public participation in child protection initiatives. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#CivilSocietyEngagement"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CivilSocietyPartner(PartnerRole):
    """Civil society organization participating in partnership with community engagement capabilities. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#CivilSocietyPartner"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CollaborativeInvestigationSituation(_cac_core.Situation):
    """Complex situation involving multiple partners working together on investigations. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#CollaborativeInvestigationSituation"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CommunityAnalysis(_cac_core.CoordinationEvent):
    """Analysis performed by volunteer researchers and civil society organizations using open source intelligence methods. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#CommunityAnalysis"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ContentDetectionCooperation(TechnologyCooperation):
    """Cooperation in developing and improving automated content detection systems. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#ContentDetectionCooperation"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CoordinationMechanism(_cac_core.CoordinationEvent):
    """Mechanism for coordinating activities and sharing information between partners. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#CoordinationMechanism"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CrowdsourcingInvestigation(_cac_core.CoordinationEvent):
    """Investigation leveraging public participation for object identification, geolocation, and evidence analysis. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#CrowdsourcingInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InformationSharingFramework(_cac_core.Artifact):
    """Framework governing how information is shared between public and private partners while protecting privacy and investigation integrity. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#InformationSharingFramework"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DataSharingAgreement(InformationSharingFramework):
    """Legal agreement governing data sharing between partners, including scope, limitations, and privacy protections. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#DataSharingAgreement"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EmergencyCoordination(CoordinationMechanism):
    """Rapid coordination mechanism for urgent situations requiring immediate partner response. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#EmergencyCoordination"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EvaluationPhase(_cac_core.Phase):
    """Phase of partnership evaluation and effectiveness assessment. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#EvaluationPhase"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class GeolocationRequest(CrowdsourcingInvestigation):
    """Request for public assistance in identifying geographic locations from visual evidence. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#GeolocationRequest"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TechnicalIntegration(InformationSharingFramework):
    """Technical integration between partner systems for automated information sharing and analysis. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#TechnicalIntegration"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HashSharingProtocol(TechnicalIntegration):
    """Protocol for sharing cryptographic hashes of illegal content between partners for detection and prevention. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#HashSharingProtocol"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InformationSharingSituation(_cac_core.Situation):
    """Situation involving active information sharing between partnership entities. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#InformationSharingSituation"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class IntelligenceSharing(InformationSharingFramework):
    """Sharing of actionable intelligence between partners while maintaining operational security. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#IntelligenceSharing"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class JointOperation(CoordinationMechanism):
    """Operation conducted jointly by multiple partners with shared resources and coordination. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#JointOperation"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LawEnforcementPartner(PartnerRole):
    """Law enforcement agency participating in partnership with investigative and enforcement responsibilities. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#LawEnforcementPartner"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MultiStakeholderInitiative(PublicPrivatePartnership):
    """Initiative involving multiple types of organizations including law enforcement, technology companies, NGOs, and civil society groups. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#MultiStakeholderInitiative"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class NGOCoordination(PublicPrivatePartnership):
    """Coordination framework with non-governmental organizations specializing in child protection and victim advocacy. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#NGOCoordination"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class NGOPartner(PartnerRole):
    """Non-governmental organization participating in partnership with advocacy and support capabilities. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#NGOPartner"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OSINTInvestigation(CommunityAnalysis):
    """Open source intelligence investigation conducted by skilled volunteers and researchers. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#OSINTInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ObjectIdentificationRequest(CrowdsourcingInvestigation):
    """Request for public assistance in identifying objects, locations, or other evidence from case materials. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#ObjectIdentificationRequest"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PartnershipFormationPhase(_cac_core.Phase):
    """Phase of partnership formation including agreement negotiation and framework establishment. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#PartnershipFormationPhase"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PlatformMonitoring(TechnologyCooperation):
    """Cooperative monitoring of platforms and services for illegal content and activities. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#PlatformMonitoring"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PublicTip(_uco_observable.ObservableObject):
    """Information provided by members of the public in response to crowdsourcing requests. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#PublicTip"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class RegularMeeting(CoordinationMechanism):
    """Regular meetings between partners for coordination, information sharing, and strategic planning. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#RegularMeeting"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RenewalPhase(_cac_core.Phase):
    """Phase of partnership renewal or renegotiation. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#RenewalPhase"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TaskForceCoordination(CoordinationMechanism):
    """Coordination through multi-partner task forces with representatives from different organizations. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#TaskForceCoordination"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TechIndustryCooperation(PublicPrivatePartnership):
    """Cooperation framework between law enforcement and technology companies for content detection, platform monitoring, and data sharing. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#TechIndustryCooperation"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TechnologyPartner(PartnerRole):
    """Technology company or provider participating in partnership with technical capabilities and platform access. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#TechnologyPartner"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ToolDevelopment(TechnologyCooperation):
    """Joint development of investigative tools and technologies for law enforcement use. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#ToolDevelopment"
    NAMESPACE_PREFIX: str = "cacontology-partnerships"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
