"""CAC Ontology - Crimes Against Children — cacontology_hotlines module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional, Union

import case_uco.uco.identity as _uco_identity
import case_uco.uco.observable as _uco_observable
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["ActionPhase", "AutomatedReporterAgent", "ClosurePhase", "ESPReport", "EvidenceItem", "ForensicsSpecialistRole", "ForwardToLEAction", "HashFeedbackAction", "HashSubmissionAction", "HotlineAction", "HotlineAnalystRole", "HotlineOrganization", "HotlineReport", "ImageEvidence", "IntakeChannel", "IntakePhase", "InternationalCoordination", "LiaisonRole", "MultiAgencyCoordination", "PublicReport", "ReportReviewAction", "ReporterRole", "ReviewPhase", "TakedownRequestAction", "URLReference", "VideoEvidence"]


@dataclass
class ActionPhase(_cac_core.Phase):
    """The phase during which responsive actions are taken (forwarding, takedown requests, etc.)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#ActionPhase"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AutomatedReporterAgent(_cac_core.DigitalSystemEntity):
    """A software agent that automatically reports content to hotlines. Enhanced as gUFO Object for comprehensive software entity modeling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#AutomatedReporterAgent"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ClosurePhase(_cac_core.Phase):
    """The phase during which reports are finalized and closed."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#ClosurePhase"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HotlineReport(_uco_observable.Observation):
    """A report submitted to a hotline about potential child sexual abuse material. Enhanced as gUFO Situation representing complex multi-party coordination contexts involving reporters, hotline organization"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#HotlineReport"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    current_phase: list[Phase] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-hotlines:currentPhase', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org/core#Phase', 'alternate_range_iris': []})
    has_evidence: list[EvidenceItem] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-hotlines:hasEvidence', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org/hotlines#EvidenceItem', 'alternate_range_iris': []})
    intake_channel: list[IntakeChannel] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-hotlines:intakeChannel', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org/hotlines#IntakeChannel', 'alternate_range_iris': []})
    involves_coordination: list[MultiAgencyCoordination] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-hotlines:involvesCoordination', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'https://cacontology.projectvic.org/hotlines#MultiAgencyCoordination', 'alternate_range_iris': []})
    received_by: list[HotlineOrganization] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-hotlines:receivedBy', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org/hotlines#HotlineOrganization', 'alternate_range_iris': []})


@dataclass
class ESPReport(HotlineReport):
    """A report submitted by an electronic service provider."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#ESPReport"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EvidenceItem(_cac_core.Artifact):
    """A piece of evidence associated with a hotline report. Enhanced as gUFO Object for comprehensive digital artifact modeling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#EvidenceItem"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    first_seen: list[datetime] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-hotlines:firstSeen', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class ForensicsSpecialistRole(_cac_core.Role):
    """The role of a specialist who performs forensic analysis of evidence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#ForensicsSpecialistRole"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HotlineAction(_cac_core.CoordinationEvent):
    """An action taken as part of processing a hotline report. Enhanced as gUFO Event for comprehensive temporal process modeling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#HotlineAction"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    end_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:endTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    start_time: list[Union[str, TypedLiteral]] = field(default_factory=list, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class ForwardToLEAction(HotlineAction):
    """The action of forwarding a report to law enforcement. Enhanced as gUFO Event for inter-agency coordination modeling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#ForwardToLEAction"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    forwards_to: list[Organization] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-hotlines:forwardsTo', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/identity/Organization', 'alternate_range_iris': []})


@dataclass
class HashFeedbackAction(HotlineAction):
    """The action of providing feedback about a hash submission. Enhanced as gUFO Event for collaborative evidence assessment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#HashFeedbackAction"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    references_hash: list[Hash] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-hotlines:referencesHash', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/observable/Hash', 'alternate_range_iris': []})


@dataclass
class HashSubmissionAction(HotlineAction):
    """The action of submitting a hash to a hash-sharing service. Enhanced as gUFO Event for digital forensics coordination."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#HashSubmissionAction"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    produces_hash: list[Hash] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-hotlines:producesHash', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/observable/Hash', 'alternate_range_iris': []})


@dataclass
class HotlineAnalystRole(_cac_core.Role):
    """The role of a specialist who analyzes hotline reports."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#HotlineAnalystRole"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HotlineOrganization(_uco_identity.Organization):
    """An organization that operates a hotline for receiving and processing reports of child sexual abuse material. Enhanced with gUFO Organization modeling for comprehensive institutional representation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#HotlineOrganization"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ImageEvidence(EvidenceItem):
    """An image submitted as evidence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#ImageEvidence"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class IntakeChannel(_cac_core.EnduringEntity):
    """A channel through which reports are received (web form, API, phone, etc.). Enhanced as gUFO Object for comprehensive communication infrastructure modeling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#IntakeChannel"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class IntakePhase(_cac_core.Phase):
    """The phase during which reports are initially received and logged."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#IntakePhase"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MultiAgencyCoordination(_cac_core.Situation):
    """A complex situation involving coordination between hotlines, law enforcement, and service providers."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#MultiAgencyCoordination"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    coordination_begin_time: list[datetime] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-hotlines:coordinationBeginTime', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class InternationalCoordination(MultiAgencyCoordination):
    """A coordination situation involving multiple countries or international organizations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#InternationalCoordination"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LiaisonRole(_cac_core.Role):
    """The role of a specialist who coordinates with law enforcement agencies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#LiaisonRole"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PublicReport(HotlineReport):
    """A report submitted by a member of the public."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#PublicReport"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ReportReviewAction(HotlineAction):
    """The action of reviewing and triaging a hotline report. Enhanced as gUFO Event with comprehensive temporal modeling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#ReportReviewAction"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ReporterRole(_cac_core.Role):
    """The role of a person or organization submitting a report to a hotline. Enhanced as anti-rigid gUFO Role supporting dynamic role assignment and temporal constraints."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#ReporterRole"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    is_anonymous: list[bool] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-hotlines:isAnonymous', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    role_assignment_time: list[datetime] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-hotlines:roleAssignmentTime', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class ReviewPhase(_cac_core.Phase):
    """The phase during which reports undergo detailed analysis and classification."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#ReviewPhase"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TakedownRequestAction(HotlineAction):
    """The action of requesting content takedown from a hosting provider. Enhanced as gUFO Event for content removal coordination."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#TakedownRequestAction"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    target: list[Organization] = field(default_factory=list, metadata={'jsonld_key': 'uco-action:target', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/identity/Organization', 'alternate_range_iris': []})


@dataclass
class URLReference(EvidenceItem):
    """A URL submitted as evidence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#URLReference"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VideoEvidence(EvidenceItem):
    """A video submitted as evidence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/hotlines#VideoEvidence"
    NAMESPACE_PREFIX: str = "cacontology-hotlines"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
