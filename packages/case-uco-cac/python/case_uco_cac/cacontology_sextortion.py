"""CAC Ontology - Crimes Against Children — cacontology_sextortion module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional, Union

import case_uco.uco.observable as _uco_observable
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac import cacontology as _cacontology
from case_uco_cac._context import NAMESPACES

__all__ = ["AdditionalContentDemand", "AgeDeceptionSextortion", "AgeDeceptionTactic", "CoercionCycle", "ComplianceResponse", "ContactListThreat", "ConversationReconstruction", "DemandMessage", "DeviceForensicAnalysis", "DisappearingMessageFeature", "DoxxingThreat", "EmotionalManipulation", "ExtortionDemand", "ExtortionPhase", "FalseProfileCreation", "GiftCardDemand", "IdentityImpersonation", "ImageAcquisitionPhase", "ImageLeakThreat", "ImageSharingFeature", "ImageSolicitationMessage", "InitialDeceptionPhase", "InstantMessagingPlatform", "InstantMessagingSextortion", "ManipulationTactic", "MonetaryDemand", "PeerImpersonation", "PersonalMeetingDemand", "PrivateMessagingFeature", "ProgressiveEscalation", "PropertyDestructionThreat", "RefusalResponse", "ReportingResponse", "SadisticSextortion", "ScreenshotThreat", "SelfHarmThreat", "SextortionCommunication", "SextortionIncident", "SextortionInvestigation", "SextortionProgression", "SexualSolicitationPhase", "SexuallyExplicitConversation", "SharingThreat", "SilentVictimization", "SocialMediaSextortion", "SocialMediaSharingThreat", "SwattingThreat", "ThreatMechanism", "ThreatMessage", "TrustBuildingPhase", "VictimIdentification", "VictimIsolation", "VictimResponse", "ViolenceThreat"]


@dataclass
class ExtortionDemand(_uco_observable.ObservableObject):
    """Specific demand made by sextortion offender using threat leverage."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#ExtortionDemand"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class AdditionalContentDemand(ExtortionDemand):
    """Demand for more graphic content or additional intimate images."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#AdditionalContentDemand"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SextortionIncident(_cacontology.Sextortion):
    """Online blackmail incident where offender tricks or coerces someone into sending sexual images, then threatens to share unless demands are met. May involve demands for money, gift cards, or more graphi"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#SextortionIncident"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    comment: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:comment', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    incident_duration: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:incidentDuration', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    incident_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:incidentType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    severity_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:severityLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    victim_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:victimCount', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    end_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:endTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class AgeDeceptionSextortion(SextortionIncident):
    """Sextortion incident involving offender lying about their age when interacting with children (e.g., posing as juvenile)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#AgeDeceptionSextortion"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AgeDeceptionTactic(_cac_core.ExploitationEvent):
    """Tactic of lying about age when interacting with children (e.g., adult posing as juvenile)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#AgeDeceptionTactic"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CoercionCycle(_cac_core.ExploitationEvent):
    """Self-sustaining sextortion loop in which retained imagery becomes perpetual leverage: the offender redeploys the same retained material to demand new content, extending leverage further without acquir"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#CoercionCycle"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    coercion_cycle_demand_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:coercionCycleDemandType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    cycles_between: list[Phase] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-sextortion:cyclesBetween', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org/core#Phase', 'alternate_range_iris': []})
    sustained_by: list[Artifact] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-sextortion:sustainedBy', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org/core#Artifact', 'alternate_range_iris': []})
    termination_condition: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:terminationCondition', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class VictimResponse(_uco_observable.ObservableObject):
    """Pattern of victim response to sextortion attempts."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#VictimResponse"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    emotional_impact: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:emotionalImpact', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    response_speed: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:responseSpeed', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    response_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:responseType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ComplianceResponse(VictimResponse):
    """Victim complies with initial requests before recognizing threat."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#ComplianceResponse"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    compliance_duration: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:complianceDuration', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    compliance_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:complianceLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ThreatMechanism(_cac_core.ExploitationEvent):
    """Specific method of threatening or coercing victims using obtained material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#ThreatMechanism"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SharingThreat(ThreatMechanism):
    """Threat to share intimate images with contacts, family, or publicly."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#SharingThreat"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ContactListThreat(SharingThreat):
    """Threat to send intimate images to victim's contact list."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#ContactListThreat"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SextortionInvestigation(_cac_core.InvestigativeAction):
    """Investigation specifically focused on sextortion incidents."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#SextortionInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ConversationReconstruction(SextortionInvestigation):
    """Reconstruction of conversation patterns and progression timelines."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#ConversationReconstruction"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SextortionCommunication(_uco_observable.Message):
    """Communication patterns specific to sextortion incidents."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#SextortionCommunication"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class DemandMessage(SextortionCommunication):
    """Message making specific demands backed by threats."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#DemandMessage"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DeviceForensicAnalysis(SextortionInvestigation):
    """Forensic examination of seized devices for sextortion evidence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#DeviceForensicAnalysis"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DisappearingMessageFeature(_uco_observable.ObservableObject):
    """Platform feature where messages automatically delete after viewing."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#DisappearingMessageFeature"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class DoxxingThreat(ThreatMechanism):
    """Threat mechanism involving doxxing (threatened release of identifying/personal information) to intimidate or coerce a victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#DoxxingThreat"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    threat_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:threatType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ManipulationTactic(_cac_core.ExploitationEvent):
    """Psychological manipulation technique used to control and exploit victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#ManipulationTactic"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EmotionalManipulation(ManipulationTactic):
    """Use of emotional tactics (false love, friendship, etc.) to control victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#EmotionalManipulation"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ExtortionPhase(_cac_core.Phase):
    """Final phase involving threats and blackmail using obtained images."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#ExtortionPhase"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class IdentityImpersonation(AgeDeceptionTactic):
    """Creating false identity or persona to deceive victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#IdentityImpersonation"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FalseProfileCreation(IdentityImpersonation):
    """Creating fake profiles on platforms with false age and personal information."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#FalseProfileCreation"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class GiftCardDemand(ExtortionDemand):
    """Demand for gift cards as form of payment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#GiftCardDemand"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ImageAcquisitionPhase(_cac_core.Phase):
    """Phase where intimate images are obtained from victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#ImageAcquisitionPhase"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ImageLeakThreat(ThreatMechanism):
    """Threat mechanism involving threatened release of the victim's sexual imagery to family, friends, school, or the public to compel compliance (Issue #36). Provides typed coercion semantics beyond boolea"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#ImageLeakThreat"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ImageSharingFeature(_uco_observable.ObservableObject):
    """Platform feature enabling image sharing in private conversations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#ImageSharingFeature"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ImageSolicitationMessage(SextortionCommunication):
    """Message requesting intimate images from victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#ImageSolicitationMessage"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InitialDeceptionPhase(_cac_core.Phase):
    """First phase involving age deception and false identity establishment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#InitialDeceptionPhase"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InstantMessagingPlatform:
    """Digital platform used for instant messaging in sextortion incidents."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#InstantMessagingPlatform"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class InstantMessagingSextortion(SextortionIncident):
    """Sextortion conducted through instant messaging platforms with direct private communication."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#InstantMessagingSextortion"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MonetaryDemand(ExtortionDemand):
    """Demand for money or financial payment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#MonetaryDemand"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PeerImpersonation(IdentityImpersonation):
    """Posing as age-appropriate peer to gain victim trust."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#PeerImpersonation"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    impersonation_method: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:impersonationMethod', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    target_age_group: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:targetAgeGroup', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PersonalMeetingDemand(ExtortionDemand):
    """Demand for in-person meeting or physical contact."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#PersonalMeetingDemand"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PrivateMessagingFeature(_uco_observable.ObservableObject):
    """Platform feature enabling private direct communication."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#PrivateMessagingFeature"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ProgressiveEscalation(ManipulationTactic):
    """Gradual increase in sexual content and requests to avoid triggering victim resistance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#ProgressiveEscalation"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    escalation_stages: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:escalationStages', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    stage_progression: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:stageProgression', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PropertyDestructionThreat(ThreatMechanism):
    """Threat mechanism involving destruction of property to compel compliance (e.g., 'destruction' threats in sadistic sextortion framing)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#PropertyDestructionThreat"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    threat_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:threatType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class RefusalResponse(VictimResponse):
    """Victim refuses demands triggering threat escalation (as in WA case)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#RefusalResponse"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ReportingResponse(VictimResponse):
    """Victim reports incident to authorities or trusted adults."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#ReportingResponse"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SadisticSextortion(SextortionIncident):
    """Sextortion incident in which the coercive leverage includes threats compelling suffering, submission, or harm (e.g., violence, coerced self-harm, or destruction), often coordinated through organized n"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#SadisticSextortion"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    employs_threat: list[ThreatMechanism] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-sextortion:employsThreat', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org/sextortion#ThreatMechanism', 'alternate_range_iris': []})


@dataclass
class ScreenshotThreat(ThreatMechanism):
    """Threat to screenshot images when victim refuses demands (specific to WA case)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#ScreenshotThreat"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    screenshot_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:screenshotCount', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    screenshot_evidence: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:screenshotEvidence', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})


@dataclass
class SelfHarmThreat(ThreatMechanism):
    """Threat mechanism involving threats that compel or pressure the victim to engage in self-harm as a condition of compliance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#SelfHarmThreat"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    threat_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:threatType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SextortionProgression(_cac_core.ExploitationEvent):
    """Sequential phases of sextortion from initial contact through exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#SextortionProgression"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SexualSolicitationPhase(_cac_core.Phase):
    """Phase involving sexually explicit conversations and image solicitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#SexualSolicitationPhase"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SexuallyExplicitConversation(SextortionCommunication):
    """Conversation containing sexually explicit content directed at children."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#SexuallyExplicitConversation"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SilentVictimization(VictimResponse):
    """Victim does not report due to shame, fear, or manipulation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#SilentVictimization"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SocialMediaSextortion(SextortionIncident):
    """Sextortion conducted through social media platforms and networks."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#SocialMediaSextortion"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SocialMediaSharingThreat(SharingThreat):
    """Threat to post intimate images on social media platforms."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#SocialMediaSharingThreat"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    contact_list_access: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:contactListAccess', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    target_platforms: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:targetPlatforms', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SwattingThreat(ThreatMechanism):
    """Threat mechanism involving swatting (threatened or induced false emergency report leading to armed law enforcement response) to intimidate or coerce a victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#SwattingThreat"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    threat_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:threatType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ThreatMessage(SextortionCommunication):
    """Message containing explicit threats about sharing images."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#ThreatMessage"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TrustBuildingPhase(_cac_core.ConditioningPhase):
    """Phase focused on building trust and rapport with victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#TrustBuildingPhase"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimIdentification(SextortionInvestigation):
    """Process of identifying and locating sextortion victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#VictimIdentification"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimIsolation(ManipulationTactic):
    """Tactics to isolate victim from support systems and reporting mechanisms."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#VictimIsolation"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ViolenceThreat(ThreatMechanism):
    """Threat mechanism involving threatened physical violence to compel compliance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sextortion#ViolenceThreat"
    NAMESPACE_PREFIX: str = "cacontology-sextortion"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    threat_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sextortion:threatType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
