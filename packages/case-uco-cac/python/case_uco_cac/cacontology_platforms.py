"""CAC Ontology - Crimes Against Children — cacontology_platforms module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar, Optional, Union

import case_uco.uco.action as _uco_action
import case_uco.uco.core as _uco_core
import case_uco.uco.identity as _uco_identity
import case_uco.uco.observable as _uco_observable
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AccountMetadata", "AccountSuspensionAction", "AffordanceMisuse", "Anonymity", "AnonymityProtectionLevel", "AnonymousChatPlatform", "AnonymousContactOpportunity", "ChannelMigrationEvent", "CoercionLeverage", "ContactDiscovery", "ContentHashingAction", "ContentModerationAction", "ContentModerationCapability", "ContentModerationQueue", "Coordination", "CrossPlatformEvidence", "CryptocurrencyService", "DarkWebService", "DataPreservationAction", "DataRetentionPolicy", "DeviceSocialMediaCorrelation", "DigitalEvidenceCorrelation", "DistributionInfrastructure", "ElectronicDeviceEvidence", "ElectronicServiceProvider", "EmergencyDisclosureRequest", "Ephemerality", "FileHostingService", "GamePlatform", "GenerativeSynthesis", "GuestChatFeature", "IdentityDisclosurePolicy", "LargeScalePlatformTakedown", "LegalComplianceCapability", "LegalDataDisclosureAction", "MassUserBehaviorAnalysis", "MassUserDatabase", "MassivePlatformSituation", "MessagingService", "MinimalVerificationRequirement", "ModerationThroughputMetrics", "MultiPlatformSituation", "OnlineDatingPlatform", "OpenChatRooms", "PlatformAffordance", "PlatformCooperationSituation", "PlatformDeploymentPhase", "PlatformGrowthPhase", "PlatformInvestigationCoordination", "PlatformInvestigationPhase", "PlatformModerationPhase", "PlatformOperation", "PlatformTakedownPhase", "PrivateMessage", "ProfileBrowsingAnonymous", "RandomUserMatching", "ReviewBacklogSituation", "SimultaneousSearchWarrant", "SocialMediaAccount", "SocialMediaAppData", "SocialMediaEvidence", "SocialMediaPlatform", "SocialMediaPost", "StoredSocialMediaContent", "TechnicalServiceProvider", "TemporaryAccountSystem", "UnmonitoredCommunication", "UserRiskClassification", "UserScaleClassification", "UserVerificationSystem", "VideoStreamingPlatform"]


@dataclass
class SocialMediaEvidence(_uco_observable.ObservableObject):
    """Digital evidence collected from social media platforms, including posts, messages, and account information."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#SocialMediaEvidence"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class AccountMetadata(SocialMediaEvidence):
    """Account-level metadata including creation date, profile information, and activity patterns."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#AccountMetadata"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AccountSuspensionAction(_cac_core.DetectionEvent):
    """An action to suspend or terminate a user account due to policy violations. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#AccountSuspensionAction"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    suspension_duration: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:suspensionDuration', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#integer', 'alternate_range_iris': []})
    suspension_reason: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:suspensionReason', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class AffordanceMisuse(_uco_core.Relationship):
    """Annotation linking a platform affordance to the phase transition it enabled — affordances on offense trajectory edges rather than platform nodes alone."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#AffordanceMisuse"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    affordance_class: Optional[PlatformAffordance] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:affordanceClass', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://cacontology.projectvic.org/platforms#PlatformAffordance', 'alternate_range_iris': []})
    enables_transition_from: Optional[Phase] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:enablesTransitionFrom', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://cacontology.projectvic.org/core#Phase', 'alternate_range_iris': []})
    enables_transition_to: Optional[Phase] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:enablesTransitionTo', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://cacontology.projectvic.org/core#Phase', 'alternate_range_iris': []})
    misuse_description: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:misuseDescription', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    platform: Optional[DigitalService] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:platform', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/observable/DigitalService', 'alternate_range_iris': []})


@dataclass
class PlatformAffordance(_cac_core.DigitalSystemEntity):
    """A platform capability that offenders may misuse to advance an offense trajectory (anonymity, ephemerality, unmonitored communication, etc.)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#PlatformAffordance"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Anonymity(PlatformAffordance):
    """Platform affordance enabling pseudonymous or minimally verified contact."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#Anonymity"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AnonymityProtectionLevel(_cac_core.EnduringEntity):
    """Level of anonymity protection provided by platform features and policies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#AnonymityProtectionLevel"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MessagingService(_uco_observable.ObservableObject):
    """A digital service for real-time communication and messaging (e.g., WhatsApp, Telegram, Signal, Discord, Kik). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#MessagingService"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    allows_anonymous_chat: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:allowsAnonymousChat', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    conversation_logging: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:conversationLogging', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    encryption_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:encryptionLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class AnonymousChatPlatform(MessagingService):
    """Platform that allows anonymous or minimally verified communication, enabling contact without identity verification."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#AnonymousChatPlatform"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AnonymousContactOpportunity(_cac_core.EnduringEntity):
    """Opportunities provided by platform for anonymous users to initiate contact with other users."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#AnonymousContactOpportunity"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ChannelMigrationEvent(_cac_core.ExploitationEvent):
    """Documented offense pattern where contact is initiated on one platform and deliberately moved to a second platform before escalation, to access more capable channels and/or sever the evidence trail on """

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#ChannelMigrationEvent"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    from_platform: Optional[DigitalService] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:fromPlatform', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/observable/DigitalService', 'alternate_range_iris': []})
    migration_rationale: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:migrationRationale', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    occurs_between: list[Phase] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-platforms:occursBetween', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org/core#Phase', 'alternate_range_iris': []})
    to_platform: Optional[DigitalService] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:toPlatform', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/observable/DigitalService', 'alternate_range_iris': []})


@dataclass
class CoercionLeverage(PlatformAffordance):
    """Platform affordance that amplifies coercive leverage (screenshots, forwarding, contact export, payment rails)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#CoercionLeverage"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ContactDiscovery(PlatformAffordance):
    """Platform affordance for finding or matching with new contacts (search, suggestions, random matching)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#ContactDiscovery"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ContentHashingAction(_cac_core.DetectionEvent):
    """An action by a platform to generate hashes of content for detection and matching. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#ContentHashingAction"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ContentModerationAction(_cac_core.DetectionEvent):
    """An action taken by a platform to moderate content (review, remove, restrict, etc.). Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#ContentModerationAction"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    moderation_decision: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:moderationDecision', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class ContentModerationCapability(_cac_core.DigitalSystemEntity):
    """The ability and methods a platform uses to detect, review, and remove inappropriate content. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#ContentModerationCapability"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    csai_detection_enabled: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:csaiDetectionEnabled', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    hash_matching_enabled: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:hashMatchingEnabled', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    moderation_method: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:moderationMethod', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    moderation_presence: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:moderationPresence', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ContentModerationQueue(_cac_core.DigitalSystemEntity):
    """A queue/backlog of content items awaiting moderation review and operational handling at scale (e.g., large volumes of flagged CSAM candidates)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#ContentModerationQueue"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    queue_size: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:queueSize', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class Coordination(PlatformAffordance):
    """Platform affordance for group coordination, encrypted channels, or multi-party planning."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#Coordination"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CrossPlatformEvidence(SocialMediaEvidence):
    """Evidence found across multiple social media platforms by the same user."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#CrossPlatformEvidence"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CryptocurrencyService(_uco_observable.ObservableObject):
    """A service for cryptocurrency transactions and exchanges (e.g., Bitcoin, Coinbase, Binance). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#CryptocurrencyService"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class DarkWebService(_uco_observable.ObservableObject):
    """A service accessible through anonymizing networks like Tor, often used for illegal activities. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#DarkWebService"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class DataPreservationAction(_cac_core.InvestigativeAction):
    """An action to preserve user data in response to legal requests. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#DataPreservationAction"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    preservation_period: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:preservationPeriod', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#integer', 'alternate_range_iris': []})
    start_time_uco_core: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class DataRetentionPolicy(_cac_core.Artifact):
    """A platform's policy for how long they retain user data and content. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#DataRetentionPolicy"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    anonymous_user_data_retention: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:anonymousUserDataRetention', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#integer', 'alternate_range_iris': []})
    content_retention_period: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:contentRetentionPeriod', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#integer', 'alternate_range_iris': []})
    log_retention_period: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:logRetentionPeriod', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#integer', 'alternate_range_iris': []})
    user_data_retention_period: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:userDataRetentionPeriod', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#integer', 'alternate_range_iris': []})


@dataclass
class DeviceSocialMediaCorrelation(_cac_core.AssessmentResult):
    """Correlation between evidence found on devices and social media accounts."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#DeviceSocialMediaCorrelation"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DigitalEvidenceCorrelation(_uco_action.Action):
    """Process of correlating evidence found across devices and platforms."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#DigitalEvidenceCorrelation"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class DistributionInfrastructure(PlatformAffordance):
    """Platform affordance for sharing or broadcasting content to audiences beyond direct dyadic chat."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#DistributionInfrastructure"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ElectronicDeviceEvidence(_uco_observable.ObservableObject):
    """Digital evidence found on electronic devices including computers, phones, and storage media."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#ElectronicDeviceEvidence"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ElectronicServiceProvider(_uco_identity.Organization):
    """An organization that provides digital services and platforms, with responsibilities for content moderation and law enforcement cooperation. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#ElectronicServiceProvider"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    accepts_legal_process: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:acceptsLegalProcess', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    emergency_disclosure_capable: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:emergencyDisclosureCapable', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    headquartered_in: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:headquarteredIn', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    operates_in_jurisdiction: list[str] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-platforms:operatesInJurisdiction', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class EmergencyDisclosureRequest(_cac_core.InvestigativeAction):
    """Time-sensitive request by law enforcement/investigators to an electronic service provider for immediate disclosure of information based on an asserted emergency involving imminent danger (e.g., danger"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#EmergencyDisclosureRequest"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    start_time_uco_core: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class Ephemerality(PlatformAffordance):
    """Platform affordance where messages or media auto-delete, reducing forensic retention on the platform."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#Ephemerality"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FileHostingService(_uco_observable.ObservableObject):
    """A service for storing and sharing files online (e.g., Google Drive, Dropbox, OneDrive, MEGA). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#FileHostingService"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class GamePlatform(_uco_observable.ObservableObject):
    """A digital platform for gaming with communication features (e.g., Xbox Live, PlayStation Network, Steam, Roblox, Minecraft). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#GamePlatform"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    contact_initiation_method: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:contactInitiationMethod', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    guest_accounts_allowed: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:guestAccountsAllowed', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})


@dataclass
class GenerativeSynthesis(PlatformAffordance):
    """Platform affordance for AI-generated or synthetic media creation and manipulation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#GenerativeSynthesis"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class GuestChatFeature:
    """Platform feature allowing users to chat without creating accounts or verifying identity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#GuestChatFeature"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class IdentityDisclosurePolicy(_cac_core.Artifact):
    """Platform policy regarding when and how user identities may be disclosed to other users or authorities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#IdentityDisclosurePolicy"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LargeScalePlatformTakedown(_cac_core.InvestigativeAction):
    """Coordinated takedown of major exploitation platforms with user bases exceeding 1 million accounts, requiring specialized international coordination and mass forensic processing. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#LargeScalePlatformTakedown"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    countries_involved: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:countriesInvolved', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    evidence_volume_terabytes: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:evidenceVolumeTerabytes', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    operation_scale: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:operationScale', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    start_time_uco_core: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class LegalComplianceCapability(_cac_core.EnduringEntity):
    """A platform's ability to respond to legal requests and cooperate with law enforcement. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#LegalComplianceCapability"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegalDataDisclosureAction(_cac_core.InvestigativeAction):
    """An action to disclose user data to law enforcement in response to legal process. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#LegalDataDisclosureAction"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    legal_process_used: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:legalProcessUsed', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    response_time_frame: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:responseTimeFrame', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#integer', 'alternate_range_iris': []})
    start_time_uco_core: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class MassUserBehaviorAnalysis(_cac_core.InvestigativeAction):
    """Analysis of user behavior patterns across massive user bases for investigation prioritization and automated threat assessment. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#MassUserBehaviorAnalysis"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    automated_processing_percentage: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:automatedProcessingPercentage', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    start_time_uco_core: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class MassUserDatabase(_uco_observable.ObservableObject):
    """User database analysis for platforms with massive user bases requiring specialized processing techniques and automated analysis tools. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#MassUserDatabase"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    processing_timeframe_days: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:processingTimeframeDays', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    user_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:userCount', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class MassivePlatformSituation(_cac_core.Situation):
    """Situation involving platforms with massive user bases requiring specialized investigation approaches. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#MassivePlatformSituation"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MinimalVerificationRequirement(_cac_core.EnduringEntity):
    """Verification requirements that are easily bypassed or minimal (email only, no identity check)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#MinimalVerificationRequirement"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ModerationThroughputMetrics(_cac_core.AssessmentResult):
    """Operational metrics describing moderation throughput and latency (e.g., queue size, review latency, flagged volume)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#ModerationThroughputMetrics"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    flag_volume_per_month: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:flagVolumePerMonth', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    review_latency_hours: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:reviewLatencyHours', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    throughput_per_day: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:throughputPerDay', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class MultiPlatformSituation(_cac_core.Situation):
    """Situation involving coordination across multiple platforms and service providers. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#MultiPlatformSituation"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OnlineDatingPlatform(_uco_observable.ObservableObject):
    """A platform for meeting and dating online (e.g., Tinder, Bumble, Grindr, dating websites). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#OnlineDatingPlatform"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class OpenChatRooms(AnonymousContactOpportunity):
    """Chat rooms open to anonymous users without verification or moderation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#OpenChatRooms"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PlatformCooperationSituation(_cac_core.Situation):
    """Situation involving cooperative efforts between platforms and law enforcement. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#PlatformCooperationSituation"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PlatformDeploymentPhase(_cac_core.Phase):
    """Phase when platform is deployed and becomes operational. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#PlatformDeploymentPhase"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PlatformGrowthPhase(_cac_core.Phase):
    """Phase of platform expansion and user base growth. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#PlatformGrowthPhase"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PlatformInvestigationCoordination(_uco_action.Action):
    """Coordinated investigation across multiple platforms and devices."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#PlatformInvestigationCoordination"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PlatformInvestigationPhase(_cac_core.Phase):
    """Phase when platform is under law enforcement investigation. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#PlatformInvestigationPhase"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PlatformModerationPhase(_cac_core.Phase):
    """Phase of active content moderation and policy enforcement. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#PlatformModerationPhase"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PlatformOperation(_cac_core.InvestigativeAction):
    """Coordinated law enforcement operation targeting specific platforms or services. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#PlatformOperation"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PlatformTakedownPhase(_cac_core.Phase):
    """Phase of platform takedown and shutdown operations. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#PlatformTakedownPhase"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PrivateMessage(SocialMediaEvidence):
    """Private messages or direct communications on social media platforms."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#PrivateMessage"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProfileBrowsingAnonymous(AnonymousContactOpportunity):
    """Ability to browse and contact user profiles anonymously without revealing identity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#ProfileBrowsingAnonymous"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RandomUserMatching(AnonymousContactOpportunity):
    """Platform feature that randomly matches users for anonymous conversations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#RandomUserMatching"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ReviewBacklogSituation(_cac_core.Situation):
    """Situation in which moderation review demand exceeds capacity, producing review backlog/latency risks."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#ReviewBacklogSituation"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SimultaneousSearchWarrant(_uco_action.Action):
    """Coordinated search warrant execution on devices and platform accounts."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#SimultaneousSearchWarrant"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SocialMediaAccount(_uco_observable.Account):
    """User account on a social media platform potentially containing evidence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#SocialMediaAccount"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SocialMediaAppData(ElectronicDeviceEvidence):
    """Application data from social media apps stored on devices."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#SocialMediaAppData"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SocialMediaPlatform(_uco_observable.ObservableObject):
    """A digital platform for social networking and content sharing (e.g., Facebook, Instagram, TikTok, Twitter, LinkedIn). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#SocialMediaPlatform"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    platform_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:platformType', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    primary_user_base: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:primaryUserBase', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    requires_registration: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:requiresRegistration', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})


@dataclass
class SocialMediaPost(SocialMediaEvidence):
    """Individual posts, updates, or content shared on social media platforms."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#SocialMediaPost"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StoredSocialMediaContent(ElectronicDeviceEvidence):
    """Social media content downloaded and stored on electronic devices."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#StoredSocialMediaContent"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TechnicalServiceProvider(_uco_identity.Organization):
    """Organizations providing technical infrastructure (hosting, CDN, DNS, etc.) that may be involved in content distribution. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#TechnicalServiceProvider"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class TemporaryAccountSystem:
    """System allowing creation of temporary accounts with minimal verification requirements."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#TemporaryAccountSystem"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class UnmonitoredCommunication(PlatformAffordance):
    """Platform affordance for private channels with limited proactive moderation or parental visibility."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#UnmonitoredCommunication"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class UserRiskClassification(_cac_core.AssessmentResult):
    """Automated classification of user risk levels based on platform activity patterns, content sharing, and behavioral indicators. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#UserRiskClassification"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    user_risk_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:userRiskLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class UserScaleClassification(_cac_core.AssessmentResult):
    """Classification system for platform size based on user base: small (<1K), medium (1K-100K), large (100K-1M), massive (1M+). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#UserScaleClassification"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    million_plus_users: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:millionPlusUsers', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    platform_scale: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:platformScale', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class UserVerificationSystem(_cac_core.DigitalSystemEntity):
    """Systems used by platforms to verify user identity and age. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#UserVerificationSystem"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    age_verification_method: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:ageVerificationMethod', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    identity_verification_required: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:identityVerificationRequired', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    verification_strength: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:verificationStrength', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class VideoStreamingPlatform(_uco_observable.ObservableObject):
    """A platform for video content streaming and sharing (e.g., YouTube, Twitch, OnlyFans, Periscope). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/platforms#VideoStreamingPlatform"
    NAMESPACE_PREFIX: str = "cacontology-platforms"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    age_verification_required: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-platforms:ageVerificationRequired', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
