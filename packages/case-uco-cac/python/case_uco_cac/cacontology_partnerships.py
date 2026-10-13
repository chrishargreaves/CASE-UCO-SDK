"""CAC Ontology - Crimes Against Children — cacontology-partnerships module."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AICooperation:
    """Cooperation in developing AI-based solutions for detection, analysis, and prevention of child exploitation. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#AICooperation"


@dataclass
class AcademicPartner:
    """Academic institution participating in partnership with research and training capabilities. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#AcademicPartner"
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
class AcademicPartnership:
    """Partnership with academic institutions for research, training, and technology development in child protection. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#AcademicPartnership"
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
class ActiveCooperationPhase:
    """Phase of active cooperation with joint operations and information sharing. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#ActiveCooperationPhase"


@dataclass
class CivilSocietyEngagement:
    """Framework for engaging civil society, volunteers, and public participation in child protection initiatives. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#CivilSocietyEngagement"
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
class CivilSocietyPartner:
    """Civil society organization participating in partnership with community engagement capabilities. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#CivilSocietyPartner"
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
class CollaborativeInvestigationSituation:
    """Complex situation involving multiple partners working together on investigations. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#CollaborativeInvestigationSituation"


@dataclass
class CommunityAnalysis:
    """Analysis performed by volunteer researchers and civil society organizations using open source intelligence methods. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#CommunityAnalysis"


@dataclass
class ContentDetectionCooperation:
    """Cooperation in developing and improving automated content detection systems. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#ContentDetectionCooperation"


@dataclass
class CoordinationMechanism:
    """Mechanism for coordinating activities and sharing information between partners. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#CoordinationMechanism"


@dataclass
class CrowdsourcingInvestigation:
    """Investigation leveraging public participation for object identification, geolocation, and evidence analysis. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#CrowdsourcingInvestigation"


@dataclass
class DataSharingAgreement:
    """Legal agreement governing data sharing between partners, including scope, limitations, and privacy protections. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#DataSharingAgreement"
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


@dataclass
class EmergencyCoordination:
    """Rapid coordination mechanism for urgent situations requiring immediate partner response. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#EmergencyCoordination"


@dataclass
class EvaluationPhase:
    """Phase of partnership evaluation and effectiveness assessment. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#EvaluationPhase"


@dataclass
class GeolocationRequest:
    """Request for public assistance in identifying geographic locations from visual evidence. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#GeolocationRequest"


@dataclass
class HashSharingProtocol:
    """Protocol for sharing cryptographic hashes of illegal content between partners for detection and prevention. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#HashSharingProtocol"
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


@dataclass
class InformationSharingFramework:
    """Framework governing how information is shared between public and private partners while protecting privacy and investigation integrity. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#InformationSharingFramework"
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


@dataclass
class InformationSharingSituation:
    """Situation involving active information sharing between partnership entities. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#InformationSharingSituation"


@dataclass
class IntelligenceSharing:
    """Sharing of actionable intelligence between partners while maintaining operational security. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#IntelligenceSharing"
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


@dataclass
class JointOperation:
    """Operation conducted jointly by multiple partners with shared resources and coordination. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#JointOperation"


@dataclass
class LawEnforcementPartner:
    """Law enforcement agency participating in partnership with investigative and enforcement responsibilities. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#LawEnforcementPartner"
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
class MultiStakeholderInitiative:
    """Initiative involving multiple types of organizations including law enforcement, technology companies, NGOs, and civil society groups. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#MultiStakeholderInitiative"
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
class NGOCoordination:
    """Coordination framework with non-governmental organizations specializing in child protection and victim advocacy. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#NGOCoordination"
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
class NGOPartner:
    """Non-governmental organization participating in partnership with advocacy and support capabilities. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#NGOPartner"
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
class OSINTInvestigation:
    """Open source intelligence investigation conducted by skilled volunteers and researchers. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#OSINTInvestigation"


@dataclass
class ObjectIdentificationRequest:
    """Request for public assistance in identifying objects, locations, or other evidence from case materials. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#ObjectIdentificationRequest"


@dataclass
class PartnerRole:
    """Role played by an organization within a public-private partnership framework. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#PartnerRole"
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
class PartnershipFormationPhase:
    """Phase of partnership formation including agreement negotiation and framework establishment. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#PartnershipFormationPhase"


@dataclass
class PlatformMonitoring:
    """Cooperative monitoring of platforms and services for illegal content and activities. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#PlatformMonitoring"


@dataclass
class PublicPrivatePartnership:
    """Formal partnership between government/law enforcement agencies and private sector organizations for child protection initiatives. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#PublicPrivatePartnership"
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
class PublicTip:
    """Information provided by members of the public in response to crowdsourcing requests. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#PublicTip"
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


@dataclass
class RegularMeeting:
    """Regular meetings between partners for coordination, information sharing, and strategic planning. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#RegularMeeting"


@dataclass
class RenewalPhase:
    """Phase of partnership renewal or renegotiation. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#RenewalPhase"


@dataclass
class TaskForceCoordination:
    """Coordination through multi-partner task forces with representatives from different organizations. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#TaskForceCoordination"


@dataclass
class TechIndustryCooperation:
    """Cooperation framework between law enforcement and technology companies for content detection, platform monitoring, and data sharing. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#TechIndustryCooperation"
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
class TechnicalIntegration:
    """Technical integration between partner systems for automated information sharing and analysis. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#TechnicalIntegration"
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


@dataclass
class TechnologyCooperation:
    """Cooperation in developing and deploying technology solutions for child protection. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#TechnologyCooperation"


@dataclass
class TechnologyPartner:
    """Technology company or provider participating in partnership with technical capabilities and platform access. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#TechnologyPartner"
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
class ToolDevelopment:
    """Joint development of investigative tools and technologies for law enforcement use. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/partnerships#ToolDevelopment"

