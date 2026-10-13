"""CAC Ontology - Crimes Against Children — cacontology_prevention module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional, Union

import case_uco.uco.core as _uco_core
import case_uco.uco.identity as _uco_identity
import case_uco.uco.role as _uco_role
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AffiliateCoordination", "AffiliateResourceSharing", "AgeTargetedEducation", "ArchivePublicationSystem", "BehavioralPrevention", "BullyingPrevention", "ChildAbusePreventionMonth", "ChildSafetyEducation", "CommunityEducation", "CommunityEducator", "CommunityEmailList", "CommunityEngagement", "CommunityEngagementMetrics", "CommunityNewsletterSystem", "CommunityOutreach", "CommunityOutreachEffectiveness", "CommunityPartnershipInitiative", "CourseCompletionTracking", "DigitalLiteracy", "DigitalSafety", "DisclosureBarrierReduction", "DisclosureEncouragementStrategy", "DiscreetAccessSystem", "EducationPlatformIntegration", "EducationPortal", "EducationalPosterCampaign", "EducationalResource", "EducatorTraining", "EmailListEngagementMetrics", "EnvironmentalPrevention", "FAQKnowledgeBase", "FAQUsageMetrics", "HealthcareProviderTraining", "ICACAffiliateNetwork", "InformationPoster", "InteractiveCourseMetrics", "InteractiveCourseSystem", "MultimediaEducationContent", "NationwideAwarenessInitiative", "OnlineSafetyEducation", "OutreachTriggeredInvestigation", "ParentCommunityEmailList", "ParentEducation", "ParentalControl", "ParentalVigilanceProgram", "PlatformSafety", "PodcastEducationSeries", "PodcastEngagementMetrics", "PostPresentationDisclosure", "PosterDistributionMetrics", "PreventionAdvocate", "PreventionCurriculum", "PreventionEffectiveness", "PreventionMaterial", "PreventionMetrics", "PreventionProgram", "PreventionSpecialist", "PrimaryPrevention", "PublicAwareness", "QRCodeEngagementMetrics", "QRCodeIntegration", "RapidResponseDisclosureWorkflow", "RiskAssessmentTool", "RiskPrevention", "RiskReduction", "SafeDisclosureEnvironment", "SafetyCoordinator", "SafetyGuideline", "SafetyProtocol", "SchoolAllegationProtocol", "SchoolCounselorTraining", "SchoolDistribution", "SchoolPolicy", "SchoolPresentationProgram", "SchoolSafetyProgram", "SecondaryPrevention", "SextortionAwareness", "SextortionEducation", "SextortionResponse", "SextortionWarningSign", "StatewideCampaignMetrics", "StudentEducation", "TeacherTraining", "TertiaryPrevention", "TrustedAdultIdentification", "TwelvePlusEducation", "VictimDisclosureTriggering"]


@dataclass
class AffiliateCoordination(_cac_core.SupportEvent):
    """Coordination activities between CAC affiliate organizations for unified prevention efforts."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#AffiliateCoordination"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AffiliateResourceSharing(_cac_core.SupportEvent):
    """Coordinated sharing of educational resources and prevention materials among CAC affiliates."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#AffiliateResourceSharing"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ChildSafetyEducation(_cac_core.SupportEvent):
    """Education programs teaching children about safety."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#ChildSafetyEducation"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    age_group: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-prevention:ageGroup', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    name: Optional[str] = field(default=None, metadata={'jsonld_key': 'uco-core:name', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class AgeTargetedEducation(ChildSafetyEducation):
    """Education programs targeted to specific age groups."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#AgeTargetedEducation"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ArchivePublicationSystem(_uco_core.UcoObject):
    """Knowledge repository system providing access to archived educational publications and historical safety information."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#ArchivePublicationSystem"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PreventionProgram(_cac_core.SupportEvent):
    """Structured program designed to prevent child abuse and exploitation. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#PreventionProgram"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    participant_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-prevention:participantCount', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    program_duration: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-prevention:programDuration', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    end_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:endTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    modified_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:modifiedTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    name: Optional[str] = field(default=None, metadata={'jsonld_key': 'uco-core:name', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class BehavioralPrevention(PreventionProgram):
    """Prevention strategies focused on behavioral changes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#BehavioralPrevention"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class BullyingPrevention(PreventionProgram):
    """Prevention programs focused on reducing bullying and shaming."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#BullyingPrevention"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ChildAbusePreventionMonth:
    """National Child Abuse Prevention Month coordinated awareness activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#ChildAbusePreventionMonth"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CommunityEducation(_cac_core.SupportEvent):
    """Education programs for community members."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#CommunityEducation"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    name: Optional[str] = field(default=None, metadata={'jsonld_key': 'uco-core:name', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class CommunityEducator(_uco_role.Role):
    """Educator working in community prevention programs."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#CommunityEducator"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CommunityEmailList(_uco_core.UcoObject):
    """Organized email communication system for ongoing safety updates to parents and community members."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#CommunityEmailList"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PreventionMetrics(_uco_core.UcoObject):
    """Metrics for measuring prevention program effectiveness."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#PreventionMetrics"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class CommunityEngagement(PreventionMetrics):
    """Measurement of community engagement in prevention."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#CommunityEngagement"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    community_participation: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-prevention:communityParticipation', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class CommunityEngagementMetrics(PreventionMetrics):
    """Comprehensive metrics for measuring community engagement across multiple communication channels."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#CommunityEngagementMetrics"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CommunityNewsletterSystem(CommunityEmailList):
    """Regular newsletter communication system for ongoing community engagement and safety updates."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#CommunityNewsletterSystem"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CommunityOutreach(_cac_core.SupportEvent):
    """Outreach programs to engage communities in child protection. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#CommunityOutreach"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    name: Optional[str] = field(default=None, metadata={'jsonld_key': 'uco-core:name', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class CommunityOutreachEffectiveness(PreventionMetrics):
    """Measurement of community outreach program effectiveness in generating victim disclosures and arrests."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#CommunityOutreachEffectiveness"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CommunityPartnershipInitiative(CommunityOutreach):
    """Initiative building partnerships with community organizations for child protection."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#CommunityPartnershipInitiative"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CourseCompletionTracking(_uco_core.UcoObject):
    """System for tracking participant progress and completion rates in interactive safety courses."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#CourseCompletionTracking"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class DigitalLiteracy(ChildSafetyEducation):
    """Education on digital literacy and safe technology use."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#DigitalLiteracy"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DigitalSafety(PreventionProgram):
    """Prevention programs focused on digital safety."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#DigitalSafety"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SafetyProtocol(_uco_core.UcoObject):
    """Protocol designed to ensure child safety in various settings."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#SafetyProtocol"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    implementation_status: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-prevention:implementationStatus', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class DisclosureEncouragementStrategy(SafetyProtocol):
    """Strategy for encouraging victims to disclose abuse through education and support."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#DisclosureEncouragementStrategy"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DisclosureBarrierReduction(DisclosureEncouragementStrategy):
    """Strategies to reduce barriers preventing victim disclosure."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#DisclosureBarrierReduction"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DiscreetAccessSystem(DigitalSafety):
    """System allowing discreet access to safety information to reduce bullying and shaming."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#DiscreetAccessSystem"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EducationPlatformIntegration(_uco_core.UcoObject):
    """Integration capabilities between different educational delivery platforms and content management systems."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#EducationPlatformIntegration"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class EducationPortal(_cac_core.DigitalSystemEntity):
    """Online portal providing educational resources for child protection. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#EducationPortal"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    education_portal_reach: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-prevention:educationPortalReach', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class EducationalPosterCampaign(PreventionProgram):
    """School-based poster distribution campaign for prevention education."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#EducationalPosterCampaign"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EducationalResource(_uco_core.UcoObject):
    """Resource designed for educational purposes in child protection."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#EducationalResource"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    language_availability: list[str] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-prevention:languageAvailability', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    target_audience: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-prevention:targetAudience', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class EducatorTraining(_cac_core.SupportEvent):
    """Training programs specifically designed for educators."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#EducatorTraining"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    name: Optional[str] = field(default=None, metadata={'jsonld_key': 'uco-core:name', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class EmailListEngagementMetrics(CommunityEngagementMetrics):
    """Metrics tracking email list subscription rates, open rates, and engagement patterns."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#EmailListEngagementMetrics"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EnvironmentalPrevention(PreventionProgram):
    """Prevention strategies focused on environmental factors."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#EnvironmentalPrevention"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FAQKnowledgeBase(_uco_core.UcoObject):
    """Structured question and answer system for Internet Crimes Against Children frequently asked questions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#FAQKnowledgeBase"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class FAQUsageMetrics(CommunityEngagementMetrics):
    """Metrics tracking FAQ access patterns, most searched questions, and help-seeking behaviors."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#FAQUsageMetrics"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HealthcareProviderTraining(_cac_core.SupportEvent):
    """Training for healthcare providers on child protection."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#HealthcareProviderTraining"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    name: Optional[str] = field(default=None, metadata={'jsonld_key': 'uco-core:name', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class ICACAffiliateNetwork(_uco_identity.Organization):
    """Network of formally affiliated CAC organizations for coordinated child protection efforts."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#ICACAffiliateNetwork"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class InformationPoster(EducationalResource):
    """Physical poster containing educational information and QR codes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#InformationPoster"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InteractiveCourseMetrics(CommunityEngagementMetrics):
    """Metrics tracking course enrollment, completion rates, and learning effectiveness."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#InteractiveCourseMetrics"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OnlineSafetyEducation(ChildSafetyEducation):
    """Education about staying safe online."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#OnlineSafetyEducation"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InteractiveCourseSystem(OnlineSafetyEducation):
    """Interactive online safety course platform with progression tracking and engagement features."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#InteractiveCourseSystem"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MultimediaEducationContent(EducationalResource):
    """Educational content incorporating multiple media types including audio, video, and interactive elements."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#MultimediaEducationContent"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class NationwideAwarenessInitiative:
    """Nationwide coordinated awareness campaign involving multiple agencies and communities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#NationwideAwarenessInitiative"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class OutreachTriggeredInvestigation(_cac_core.InvestigativeAction):
    """Investigation initiated as direct result of community outreach presentation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#OutreachTriggeredInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ParentCommunityEmailList(CommunityEmailList):
    """Specialized email list for parent and community safety updates and archived publication access."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#ParentCommunityEmailList"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ParentEducation(_cac_core.SupportEvent):
    """Education programs for parents and caregivers."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#ParentEducation"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    name: Optional[str] = field(default=None, metadata={'jsonld_key': 'uco-core:name', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class ParentalControl(SafetyProtocol):
    """Technology tools for parental oversight."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#ParentalControl"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ParentalVigilanceProgram(CommunityOutreach):
    """Program educating parents on recognizing signs of child exploitation and reporting."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#ParentalVigilanceProgram"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PlatformSafety(SafetyProtocol):
    """Safety measures implemented by technology platforms."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#PlatformSafety"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PodcastEducationSeries(ChildSafetyEducation):
    """Audio-based educational content delivery system, such as the Protect Kids Online (PKO) Podcast."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#PodcastEducationSeries"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PodcastEngagementMetrics(CommunityEngagementMetrics):
    """Metrics tracking podcast download rates, completion rates, and listener engagement."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#PodcastEngagementMetrics"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PostPresentationDisclosure(_cac_core.SupportEvent):
    """Victim disclosure that occurs following a safety presentation or educational event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#PostPresentationDisclosure"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PosterDistributionMetrics(PreventionMetrics):
    """Metrics tracking poster distribution and reach."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#PosterDistributionMetrics"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PreventionAdvocate(_uco_role.Role):
    """Advocate promoting prevention initiatives."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#PreventionAdvocate"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PreventionCurriculum(_uco_core.UcoObject):
    """Structured curriculum for prevention education."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#PreventionCurriculum"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PreventionEffectiveness(PreventionMetrics):
    """Assessment of prevention program effectiveness."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#PreventionEffectiveness"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    prevention_effectiveness: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-prevention:preventionEffectiveness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class PreventionMaterial(EducationalResource):
    """Educational material focused on prevention strategies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#PreventionMaterial"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PreventionSpecialist(_uco_role.Role):
    """Professional specializing in prevention programs."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#PreventionSpecialist"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PrimaryPrevention(PreventionProgram):
    """Prevention strategies that stop abuse before it occurs."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#PrimaryPrevention"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PublicAwareness(_cac_core.SupportEvent):
    """Campaigns to raise public awareness about child protection. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#PublicAwareness"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    name: Optional[str] = field(default=None, metadata={'jsonld_key': 'uco-core:name', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class QRCodeEngagementMetrics(PreventionMetrics):
    """Metrics tracking QR code usage and engagement."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#QRCodeEngagementMetrics"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class QRCodeIntegration(_uco_core.UcoObject):
    """QR code system for discreet access to prevention information."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#QRCodeIntegration"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class RapidResponseDisclosureWorkflow(_cac_core.SupportEvent):
    """Workflow enabling rapid response from victim disclosure to arrest (e.g., 8-hour timeline)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#RapidResponseDisclosureWorkflow"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RiskAssessmentTool(_uco_core.UcoObject):
    """Tool for assessing risks to child safety."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#RiskAssessmentTool"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class RiskPrevention(PreventionProgram):
    """Programs focused on preventing risk factors for child abuse. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#RiskPrevention"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RiskReduction(PreventionMetrics):
    """Measurement of risk reduction achieved."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#RiskReduction"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    risk_reduction_level: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-prevention:riskReductionLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class SafeDisclosureEnvironment(SafetyProtocol):
    """Creation of safe environment where victims feel comfortable disclosing abuse."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#SafeDisclosureEnvironment"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SafetyCoordinator(_uco_role.Role):
    """Coordinator responsible for safety programs."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#SafetyCoordinator"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SafetyGuideline(EducationalResource):
    """Guidelines for maintaining child safety."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#SafetyGuideline"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SchoolAllegationProtocol(_cac_core.Artifact):
    """Protocol for managing allegations of abuse in school settings. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#SchoolAllegationProtocol"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SchoolCounselorTraining(EducatorTraining):
    """Training program for school counselors."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#SchoolCounselorTraining"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SchoolDistribution(_cac_core.SupportEvent):
    """Distribution of educational materials to schools."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#SchoolDistribution"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SchoolPolicy(_uco_core.UcoObject):
    """Policy governing child protection in schools."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#SchoolPolicy"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SchoolPresentationProgram:
    """FBI school presentation program for child safety education and disclosure encouragement."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#SchoolPresentationProgram"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SchoolSafetyProgram(PreventionProgram):
    """Safety program implemented in school settings."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#SchoolSafetyProgram"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SecondaryPrevention(PreventionProgram):
    """Early intervention strategies to prevent escalation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#SecondaryPrevention"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SextortionAwareness(PreventionProgram):
    """Prevention program focused on sextortion education and awareness."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#SextortionAwareness"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SextortionEducation(ChildSafetyEducation):
    """Educational content specifically addressing sextortion risks and prevention."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#SextortionEducation"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SextortionResponse(SafetyProtocol):
    """Response protocol for sextortion incidents."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#SextortionResponse"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SextortionWarningSign(_uco_core.UcoObject):
    """Identifiable warning signs of sextortion activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#SextortionWarningSign"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class StatewideCampaignMetrics(PreventionMetrics):
    """Metrics for measuring statewide prevention campaign effectiveness."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#StatewideCampaignMetrics"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StudentEducation(ChildSafetyEducation):
    """Safety education program for students."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#StudentEducation"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TeacherTraining(EducatorTraining):
    """Training program specifically for teachers."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#TeacherTraining"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TertiaryPrevention(PreventionProgram):
    """Prevention of re-victimization and recurrence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#TertiaryPrevention"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TrustedAdultIdentification(DisclosureEncouragementStrategy):
    """Education helping children identify trusted adults for disclosure."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#TrustedAdultIdentification"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TwelvePlusEducation(AgeTargetedEducation):
    """Safety education targeted specifically for students 12 years and older."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#TwelvePlusEducation"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimDisclosureTriggering:
    """Safety education event that triggers victim disclosure of ongoing abuse."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/prevention#VictimDisclosureTriggering"
    NAMESPACE_PREFIX: str = "cacontology-prevention"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
