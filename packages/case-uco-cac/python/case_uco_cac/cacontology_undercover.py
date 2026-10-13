"""CAC Ontology - Crimes Against Children — cacontology_undercover module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional, Union

import case_uco.uco.identity as _uco_identity
import case_uco.uco.location as _uco_location
import case_uco.uco.observable as _uco_observable
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AdvertisementPhotographyEvidence", "AgeAcknowledgment", "ApartmentStingOperation", "BathroomViolationEvidence", "ChatInvestigationAgent", "ChatRoomInfiltration", "ChildPersona", "ClientCommunicationInterception", "ClientResponseInterception", "ControlledMeeting", "CriminalItemAgreementAction", "CriminalSolicitation", "DisguiseRequestAction", "EvidenceGatheringPhase", "ExplicitMessageRequestAction", "ExtractionPhase", "Hotel", "InPersonMeetingSolicitation", "IncriminatingStatement", "InfiltrationPhase", "LiveAdvertisementMonitoring", "MeetingLocation", "MeetingLocationArrangement", "MinorPersonaAgent", "MinorPersonaOperation", "Motel", "MultiPlatformUndercoverOperation", "MultiplePersonaOperation", "OnlinePlatformSurveillance", "OperationHandler", "OperationalEvidence", "ParentPersona", "PhoneInstructionMonitoring", "PhysicalLocationSting", "PlatformAccount", "PredatorTargetingOperation", "PreparationPhase", "PrivacyViolationInvestigation", "ResidentialStingLocation", "SexualIntentStatement", "ShortTermRental", "SiblingPersonaOperation", "SocialMediaAgent", "SocialMediaUndercoverOperation", "StingOperation", "SurveillancePosition", "SuspectCommunicationAction", "TechnicalSupport", "TransportArrangementAction", "UndercoverAgent", "UndercoverChatInvestigation", "UndercoverCommunication", "UndercoverEvidence", "UndercoverIdentity", "UndercoverOperation", "VictimInstructionEvidence", "VideoCallRequestAction", "WebsiteAdvertisementResponse"]


@dataclass
class UndercoverEvidence(_cac_core.Artifact):
    """Evidence obtained through undercover operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#UndercoverEvidence"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    chain_of_custody_maintained: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:chainOfCustodyMaintained', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    collection_date: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:collectionDate', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    collection_method: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:collectionMethod', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    evidence_authenticity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:evidenceAuthenticity', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    evidence_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:evidenceType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class OperationalEvidence(UndercoverEvidence):
    """Evidence collected during undercover operations including recordings, communications, and observations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#OperationalEvidence"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AdvertisementPhotographyEvidence(OperationalEvidence):
    """Photographic evidence of minor victims posted in trafficking advertisements."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#AdvertisementPhotographyEvidence"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SuspectCommunicationAction(_cac_core.ExploitationEvent):
    """Base class for criminal communication actions initiated by suspect during undercover operation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#SuspectCommunicationAction"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    occurred_during_operation: Optional[UndercoverOperation] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:occurredDuringOperation', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'https://cacontology.projectvic.org/undercover#UndercoverOperation', 'alternate_range_iris': []})


@dataclass
class AgeAcknowledgment(SuspectCommunicationAction):
    """Suspect explicitly acknowledging the stated age of the minor persona during communication."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#AgeAcknowledgment"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    acknowledged_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:acknowledgedCount', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    age_stated_to_suspect: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:ageStatedToSuspect', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class UndercoverOperation(_cac_core.InvestigativeAction):
    """A law enforcement operation using false identities or covert methods to investigate crimes and gather evidence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#UndercoverOperation"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    operation_duration: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:operationDuration', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    operation_status: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:operationStatus', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    operation_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:operationType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    risk_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:riskLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    end_time_uco_core: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:endTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    start_time_uco_core: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class PhysicalLocationSting(UndercoverOperation):
    """Undercover operation conducted at physical location to apprehend suspects responding to trafficking advertisements."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#PhysicalLocationSting"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ApartmentStingOperation(PhysicalLocationSting):
    """Undercover operation using residential apartment as location for sting operation targeting trafficking clients."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#ApartmentStingOperation"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class BathroomViolationEvidence(OperationalEvidence):
    """Evidence of traffickers forcing victims to undress in bathrooms or other private areas."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#BathroomViolationEvidence"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class UndercoverAgent(_cac_core.Role):
    """Law enforcement officer or authorized civilian operating under false identity in an investigation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#UndercoverAgent"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SocialMediaAgent(UndercoverAgent):
    """Agent specialized in social media platform undercover operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#SocialMediaAgent"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ChatInvestigationAgent(SocialMediaAgent):
    """Agent specialized in chat-based undercover investigations for predator identification."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#ChatInvestigationAgent"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ChatRoomInfiltration(UndercoverOperation):
    """Undercover operation involving infiltration of online chat rooms or messaging platforms to investigate criminal activity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#ChatRoomInfiltration"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class UndercoverIdentity(_uco_identity.Identity):
    """A fictitious identity created and maintained by law enforcement for undercover operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#UndercoverIdentity"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    backstory_depth: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:backstoryDepth', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    documentation_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:documentationLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    identity_complexity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:identityComplexity', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    identity_lifespan: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:identityLifespan', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    identity_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:identityType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ChildPersona(UndercoverIdentity):
    """Undercover identity portraying a minor child for investigative purposes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#ChildPersona"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PhoneInstructionMonitoring(UndercoverOperation):
    """Monitoring and interception of phone communications used to instruct victims in trafficking operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#PhoneInstructionMonitoring"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ClientCommunicationInterception(PhoneInstructionMonitoring):
    """Interception of phone communications between traffickers, victims, and clients."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#ClientCommunicationInterception"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class WebsiteAdvertisementResponse(UndercoverOperation):
    """Undercover operation responding to existing trafficking advertisements posted by suspects."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#WebsiteAdvertisementResponse"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ClientResponseInterception(WebsiteAdvertisementResponse):
    """Undercover response to trafficking advertisement posing as potential client to gather evidence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#ClientResponseInterception"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ControlledMeeting(UndercoverOperation):
    """Planned in-person meeting between undercover agents and suspects under controlled conditions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#ControlledMeeting"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CriminalItemAgreementAction(SuspectCommunicationAction):
    """Suspect agreeing to bring items for abuse (condoms, vape, alcohol, etc.)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#CriminalItemAgreementAction"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    items_agreed_to_bring: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:itemsAgreedToBring', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CriminalSolicitation(_uco_observable.Message):
    """Request or instruction from suspect to undercover agent to commit illegal acts."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#CriminalSolicitation"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class DisguiseRequestAction(SuspectCommunicationAction):
    """Suspect requesting alleged minor wear disguise items (sunglasses, etc.) to avoid detection."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#DisguiseRequestAction"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    disguise_item_requested: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:disguiseItemRequested', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    disguise_purpose: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:disguisePurpose', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class EvidenceGatheringPhase(_cac_core.Phase):
    """Phase focused on collecting criminal evidence through undercover interactions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#EvidenceGatheringPhase"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ExplicitMessageRequestAction(SuspectCommunicationAction):
    """Suspect requesting explicit pictures or content from undercover persona."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#ExplicitMessageRequestAction"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    request_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:requestType', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ExtractionPhase(_cac_core.Phase):
    """Phase involving safe withdrawal from undercover operation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#ExtractionPhase"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MeetingLocation(_uco_location.Location):
    """Physical location arranged for meeting with alleged minor. Extends uco-location:Location as this represents a physical place."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#MeetingLocation"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    arranged_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:arrangedTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    location_name: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:locationName', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    room_number: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:roomNumber', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class Hotel(MeetingLocation):
    """Hotel used or intended for sexual exploitation of minors. Physical location."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#Hotel"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class UndercoverChatInvestigation(ChatRoomInfiltration):
    """Investigation using chat communications on various platforms with agents posing as minors."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#UndercoverChatInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InPersonMeetingSolicitation(UndercoverChatInvestigation):
    """Targeting individuals who seek to arrange in-person meetings with minors for illegal purposes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#InPersonMeetingSolicitation"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class IncriminatingStatement(_uco_observable.Message):
    """Statement made by suspect that provides evidence of criminal intent or past crimes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#IncriminatingStatement"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class InfiltrationPhase(_cac_core.Phase):
    """Phase involving initial contact and establishment of undercover presence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#InfiltrationPhase"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LiveAdvertisementMonitoring(WebsiteAdvertisementResponse):
    """Real-time monitoring of trafficking advertisements to identify and respond to active postings."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#LiveAdvertisementMonitoring"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MeetingLocationArrangement(SuspectCommunicationAction):
    """Suspect arranging specific meeting location (motel, hotel, other private location)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#MeetingLocationArrangement"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    arranged_for_meeting: Optional[MeetingLocation] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:arrangedForMeeting', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'https://cacontology.projectvic.org/undercover#MeetingLocation', 'alternate_range_iris': []})
    meeting_location_name: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:meetingLocationName', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    meeting_location_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:meetingLocationType', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class MinorPersonaAgent(UndercoverAgent):
    """Undercover agent operating with minor persona identity on social media platforms."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#MinorPersonaAgent"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SocialMediaUndercoverOperation(UndercoverOperation):
    """Undercover operation conducted on social media platforms to identify predators seeking to meet children."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#SocialMediaUndercoverOperation"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MinorPersonaOperation(SocialMediaUndercoverOperation):
    """Undercover operation where agents pose as minors to identify individuals seeking inappropriate contact."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#MinorPersonaOperation"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Motel(MeetingLocation):
    """Motel used or intended for sexual exploitation of minors (e.g., 'Princess Motel'). Physical location."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#Motel"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MultiPlatformUndercoverOperation(SocialMediaUndercoverOperation):
    """Undercover operation conducted across multiple social media platforms simultaneously."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#MultiPlatformUndercoverOperation"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MultiplePersonaOperation(MinorPersonaOperation):
    """Undercover operation where agent poses as multiple fictitious minors (e.g., 14-year-old and 12-year-old sisters). Extends MinorPersonaOperation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#MultiplePersonaOperation"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    persona_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:personaCount', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    primary_persona_age: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:primaryPersonaAge', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    secondary_persona_age: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:secondaryPersonaAge', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class OnlinePlatformSurveillance(UndercoverOperation):
    """Covert monitoring of online platforms for criminal activity without direct participation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#OnlinePlatformSurveillance"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OperationHandler(_cac_core.Role):
    """Supervising officer responsible for managing undercover operations and agent safety."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#OperationHandler"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ParentPersona(UndercoverIdentity):
    """Undercover identity portraying a parent or guardian of a child victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#ParentPersona"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PlatformAccount(_uco_observable.DigitalAccount):
    """Account created on digital platforms for undercover operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#PlatformAccount"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PredatorTargetingOperation(UndercoverOperation):
    """Undercover operation specifically targeting online predators who seek contact with children."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#PredatorTargetingOperation"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PreparationPhase(_cac_core.Phase):
    """Phase involving setup of undercover identities and operational planning."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#PreparationPhase"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PrivacyViolationInvestigation(UndercoverOperation):
    """Investigation of trafficking activities involving forced undressing and privacy violations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#PrivacyViolationInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ResidentialStingLocation(_uco_location.Location):
    """Residential property (apartment, house, etc.) used as staging area for undercover sting operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#ResidentialStingLocation"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SexualIntentStatement(SuspectCommunicationAction):
    """Explicit statement by suspect expressing intent to engage in sexual acts with alleged minor."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#SexualIntentStatement"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    sexual_acts_intended: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:sexualActsIntended', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    targeted_both_personas: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:targetedBothPersonas', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})


@dataclass
class ShortTermRental(MeetingLocation):
    """Short-term rental property (Airbnb, VRBO, etc.) used for sexual exploitation. Physical location."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#ShortTermRental"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SiblingPersonaOperation(MultiplePersonaOperation):
    """Undercover operation where agent creates related minor personas (siblings)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#SiblingPersonaOperation"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    sibling_relationship: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:siblingRelationship', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class StingOperation(UndercoverOperation):
    """Coordinated undercover operation designed to catch suspects in the act of committing crimes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#StingOperation"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SurveillancePosition(_uco_location.Location):
    """Position maintained by backup officers for observation and safety during physical sting operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#SurveillancePosition"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class TechnicalSupport(_cac_core.Role):
    """Personnel providing technical infrastructure and monitoring for undercover operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#TechnicalSupport"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TransportArrangementAction(SuspectCommunicationAction):
    """Suspect arranging to pick up and transport alleged minor to meeting location."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#TransportArrangementAction"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    destination_location: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:destinationLocation', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    pickup_location: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:pickupLocation', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class UndercoverCommunication(_uco_observable.MessageThread):
    """Communication conducted while using an undercover identity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#UndercoverCommunication"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class VictimInstructionEvidence(OperationalEvidence):
    """Evidence of traffickers providing phones and instructions to victims for client communication."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#VictimInstructionEvidence"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VideoCallRequestAction(SuspectCommunicationAction):
    """Suspect requesting video call with undercover persona, often to confirm alone or for explicit purposes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/undercover#VideoCallRequestAction"
    NAMESPACE_PREFIX: str = "cacontology-undercover"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    when_parent_absent: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-undercover:whenParentAbsent', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
