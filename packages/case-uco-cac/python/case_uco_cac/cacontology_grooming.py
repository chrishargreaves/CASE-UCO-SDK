"""CAC Ontology - Crimes Against Children — cacontology_grooming module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional, Union

import case_uco.uco.core as _uco_core
import case_uco.uco.identity as _uco_identity
import case_uco.uco.observable as _uco_observable
import case_uco.uco.pattern as _uco_pattern
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AcceleratedTrustExploitation", "AccountReplacementEvent", "AlcoholFacilitatedGrooming", "AnonymousInitiation", "AnonymousPlatformContact", "BluntRecruitmentGrooming", "ChildVictim", "ConditioningBehavior", "ConditioningPhase", "CrossInstitutionalGrooming", "DirectTraffickingPropositionGrooming", "EconomicIncentiveGrooming", "EducatorGrooming", "EliteInstitutionTargeting", "Enticement", "EscalationPattern", "ExplicitCommercialOfferGrooming", "ExploitationPhase", "FabricatedPersona", "GraphicConversationGrooming", "GroomingBehavior", "GroomingMessage", "GroomingPattern", "GroomingPhase", "ImmediateExploitationAttempt", "ImmediateMonetizationGrooming", "ImpairmentBasedGrooming", "InappropriateGift", "InitialContactPhase", "InitiatorContentSending", "InterstateTransportPlan", "IsolationBasedGrooming", "IsolationBehavior", "IsolationPhase", "IsolationTactics", "LocationSpecificGrooming", "MaintenancePhase", "ManipulationPattern", "MarijuanaFacilitatedGrooming", "MultipleAccountGrooming", "NormalizationBehavior", "NormalizationGrooming", "OfflineControlEstablishment", "OnlineGrooming", "OnlineGroomingSituation", "OnlinePredationSituation", "OnlinePredator", "OnlineToOfflineProgression", "OpportunisticGrooming", "PeerPersonaGrooming", "PhysicalMeetingArrangement", "PhysicalSpaceGrooming", "PlatformAnonymityFeature", "PositionOfTrustGrooming", "PreyBehaviorPattern", "PrivilegedVictimTargeting", "PublicToPrivateGrooming", "RapidEscalationGrooming", "ReciprocityGrooming", "ReputationBasedSilencing", "SameDayProgression", "SecrecyRequest", "SexualConsequenceGameGrooming", "SexualContentExchangeGrooming", "SexualExploitation", "SexualSolicitation", "SexualizationPhase", "SkippedGroomingPhases", "StreetBasedGrooming", "SubstanceFacilitatedGrooming", "SubstanceInducedVulnerabilityGrooming", "TeenageImpersonationGrooming", "TravelArrangement", "TrustBuilding", "TrustBuildingBehavior", "TrustBuildingPhase", "TrustThroughAnonymity", "UnverifiedUserProfile", "VehicleBasedGrooming", "VictimComplianceInPhysicalMeeting", "VictimResponse", "VictimTargeting", "VictimVulnerability", "VictimVulnerabilitySituation"]


@dataclass
class GroomingBehavior(_cac_core.ExploitationEvent):
    """Predatory behavior designed to prepare a child for abuse by building trust, isolating them, and normalizing inappropriate contact."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#GroomingBehavior"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_end_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasEndPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    comment: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:comment', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    analysis_completeness: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:analysisCompleteness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    behavior_frequency: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:behaviorFrequency', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    behavior_intensity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:behaviorIntensity', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    behavior_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:behaviorType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    data_confidence: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:dataConfidence', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    grooming_effectiveness: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:groomingEffectiveness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    grooming_stage: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:groomingStage', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    manipulation_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:manipulationLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    end_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:endTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class RapidEscalationGrooming(GroomingBehavior):
    """Grooming with accelerated timeline from initial contact to exploitation attempt, bypassing traditional relationship-building phases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#RapidEscalationGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AcceleratedTrustExploitation(RapidEscalationGrooming):
    """Rapid exploitation of minimal trust established through pretexts or assistance offers."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#AcceleratedTrustExploitation"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AccountReplacementEvent(_cac_core.ExploitationEvent):
    """Pattern where an offender whose account is banned or blocked creates a new account and returns to an earlier offense phase (typically initial contact). The lifecycle resets rather than terminates — st"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#AccountReplacementEvent"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    original_account_id: Optional[Account] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:originalAccountId', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/observable/Account', 'alternate_range_iris': []})
    replacement_account_id: Optional[Account] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:replacementAccountId', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/observable/Account', 'alternate_range_iris': []})
    resumes_at: Optional[Phase] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:resumesAt', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://cacontology.projectvic.org/core#Phase', 'alternate_range_iris': []})
    triggered_by: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:triggeredBy', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SubstanceFacilitatedGrooming(GroomingBehavior):
    """Grooming that uses alcohol or drugs to reduce victim resistance and facilitate exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#SubstanceFacilitatedGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AlcoholFacilitatedGrooming(SubstanceFacilitatedGrooming):
    """Grooming using alcohol to impair victim judgment and reduce resistance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#AlcoholFacilitatedGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AnonymousPlatformContact(GroomingBehavior):
    """Initial contact made through platforms that allow anonymous messaging or minimal user verification."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#AnonymousPlatformContact"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AnonymousInitiation(AnonymousPlatformContact):
    """Starting contact without revealing true identity or personal information."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#AnonymousInitiation"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SexualExploitation(GroomingBehavior):
    """Direct exploitation of child for sexual purposes including solicitation of images or performances."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#SexualExploitation"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DirectTraffickingPropositionGrooming(SexualExploitation):
    """Grooming involving explicit, immediate propositions for commercial sexual activity without gradual normalization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#DirectTraffickingPropositionGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class BluntRecruitmentGrooming(DirectTraffickingPropositionGrooming):
    """Direct, unsubtle recruitment for trafficking without gradual persuasion techniques."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#BluntRecruitmentGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ChildVictim(_uco_identity.Person):
    """Minor child who is the target of grooming behavior. When analysis depends on the victim’s exact age at specific grooming events (e.g., 13-or-younger online grooming in 2025), that age SHOULD be repres"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#ChildVictim"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ConditioningBehavior(GroomingBehavior):
    """Offender behavior that shapes victim readiness, compliance, dependency, or situational constraints preparatory to direct exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#ConditioningBehavior"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ConditioningPhase(_cac_core.ConditioningPhase):
    """Grooming-process phase in which the offender conditions the victim or situation for exploitation — including rapport, isolation, normalization, and compliance shaping prior to the primary exploitation"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#ConditioningPhase"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    conditioning_mode: Optional[str] = field(default=None, metadata={'jsonld_key': 'cac-core:conditioningMode', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_grooming_phase_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:hasGroomingPhaseBeginPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_grooming_phase_end_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:hasGroomingPhaseEndPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class OnlineGrooming(GroomingBehavior):
    """Grooming behavior conducted through online platforms and digital communication channels."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#OnlineGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EducatorGrooming(OnlineGrooming):
    """Grooming behavior by educational personnel leveraging position of trust and authority."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#EducatorGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CrossInstitutionalGrooming(EducatorGrooming):
    """Grooming targeting students from multiple educational institutions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#CrossInstitutionalGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EconomicIncentiveGrooming(DirectTraffickingPropositionGrooming):
    """Grooming that emphasizes financial benefits of commercial sexual activity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#EconomicIncentiveGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimTargeting(_cac_core.ExploitationEvent):
    """The process by which an offender identifies and selects a potential victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#VictimTargeting"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EliteInstitutionTargeting(VictimTargeting):
    """Targeting of students from elite or prestigious educational institutions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#EliteInstitutionTargeting"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Enticement(GroomingBehavior):
    """Direct solicitation of a child to engage in illegal sexual activity or meet for such purposes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#Enticement"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class GroomingPattern(_uco_pattern.Pattern):
    """Identifiable pattern of behavior across multiple communications or interactions that indicates grooming."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#GroomingPattern"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class EscalationPattern(GroomingPattern):
    """Progressive increase in inappropriate content or requests over time."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#EscalationPattern"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_end_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasEndPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    escalation_duration: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:escalationDuration', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    escalation_predictability: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:escalationPredictability', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    escalation_speed: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:escalationSpeed', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    escalation_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:escalationType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    pattern_confidence: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:patternConfidence', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class ExplicitCommercialOfferGrooming(DirectTraffickingPropositionGrooming):
    """Grooming involving direct offers of money in exchange for sexual services."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#ExplicitCommercialOfferGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class GroomingPhase(_cac_core.Phase):
    """A temporal phase within the grooming process."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#GroomingPhase"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ExploitationPhase(GroomingPhase):
    """Final phase involving direct sexual exploitation and abuse."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#ExploitationPhase"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FabricatedPersona(_uco_identity.Identity):
    """A fabricated identity (e.g., a fictitious minor peer) created and controlled by an offender to contact, groom, lure, or coerce victims. The same persona may be reused across victims and platforms. Com"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#FabricatedPersona"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    claimed_age: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:claimedAge', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    claimed_display_name: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:claimedDisplayName', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    claimed_gender: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:claimedGender', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SexualContentExchangeGrooming(OnlineGrooming):
    """Grooming involving exchange of sexual content to normalize sexual behavior."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#SexualContentExchangeGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class GraphicConversationGrooming(SexualContentExchangeGrooming):
    """Grooming involving progressively graphic sexual conversations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#GraphicConversationGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class GroomingMessage(_uco_observable.Message):
    """Communication containing grooming behavior or inappropriate content directed at a child."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#GroomingMessage"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ImmediateExploitationAttempt(RapidEscalationGrooming):
    """Attempt to immediately exploit victim without extended grooming or relationship building."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#ImmediateExploitationAttempt"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ImmediateMonetizationGrooming(DirectTraffickingPropositionGrooming):
    """Grooming focused on immediate monetization of victim's sexuality."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#ImmediateMonetizationGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ImpairmentBasedGrooming(SubstanceFacilitatedGrooming):
    """Grooming that exploits victim impairment from substances to reduce resistance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#ImpairmentBasedGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InappropriateGift(_uco_observable.ObservableObject):
    """Offer or provision of gifts, money, or favors as part of grooming process."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#InappropriateGift"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class InitialContactPhase(GroomingPhase):
    """First phase of grooming involving initial contact and relationship establishment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#InitialContactPhase"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InitiatorContentSending(SexualContentExchangeGrooming):
    """Grooming phase where perpetrator sends sexual content to victim first."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#InitiatorContentSending"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PhysicalMeetingArrangement(Enticement):
    """Coordination of in-person meeting between predator and victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#PhysicalMeetingArrangement"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TravelArrangement(PhysicalMeetingArrangement):
    """Planning or facilitating travel for victim to meet predator."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#TravelArrangement"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InterstateTransportPlan(TravelArrangement):
    """Planning to transport victim across state lines for illegal purposes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#InterstateTransportPlan"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PhysicalSpaceGrooming(GroomingBehavior):
    """Grooming that occurs in physical spaces rather than digital platforms."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#PhysicalSpaceGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class IsolationBasedGrooming(PhysicalSpaceGrooming):
    """Grooming that relies on physical isolation to reduce victim resistance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#IsolationBasedGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class IsolationBehavior(ConditioningBehavior):
    """Attempts to separate child from parents, friends, or other support systems."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#IsolationBehavior"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class IsolationPhase(ConditioningPhase):
    """Phase aimed at separating victim from support systems and creating dependency."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#IsolationPhase"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class IsolationTactics(ConditioningBehavior):
    """Isolation conditioning behavior separating the victim from support systems."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#IsolationTactics"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    isolation_effectiveness: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:isolationEffectiveness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    isolation_method: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:isolationMethod', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    isolation_progress_rate: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:isolationProgressRate', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})


@dataclass
class LocationSpecificGrooming(GroomingBehavior):
    """Grooming that references or prepares for specific physical locations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#LocationSpecificGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MaintenancePhase(GroomingPhase):
    """Ongoing phase to maintain control and continue exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#MaintenancePhase"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ManipulationPattern(GroomingPattern):
    """Systematic use of psychological manipulation techniques to control victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#ManipulationPattern"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MarijuanaFacilitatedGrooming(SubstanceFacilitatedGrooming):
    """Grooming using marijuana to reduce victim inhibitions and facilitate exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#MarijuanaFacilitatedGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MultipleAccountGrooming(EducatorGrooming):
    """Grooming using multiple fake accounts to maintain deceptive identity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#MultipleAccountGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class NormalizationBehavior(ConditioningBehavior):
    """Gradual introduction of sexual topics to normalize inappropriate behavior."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#NormalizationBehavior"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class NormalizationGrooming(SexualContentExchangeGrooming):
    """Grooming technique to normalize sexual conversations and content sharing."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#NormalizationGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OfflineControlEstablishment(ManipulationPattern):
    """Establishing control over victim in preparation for physical contact."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#OfflineControlEstablishment"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OnlineGroomingSituation(_cac_core.Situation):
    """Overall situation encompassing the grooming relationship and interactions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#OnlineGroomingSituation"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OnlinePredationSituation(_cac_core.Situation):
    """Active situation where predator is engaging with potential victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#OnlinePredationSituation"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OnlinePredator(_uco_identity.Person):
    """Individual who engages in grooming behavior toward children online. Age-at-time for this offender MAY be captured via cacontology-temporal:AgeAtTimeSituation instances when age-gap and legal-capacity """

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#OnlinePredator"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class OnlineToOfflineProgression(EscalationPattern):
    """Escalation from online grooming to arranging physical meetings or contact."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#OnlineToOfflineProgression"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    progression_duration: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:progressionDuration', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    progression_stages: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:progressionStages', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    transition_likelihood: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:transitionLikelihood', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})


@dataclass
class OpportunisticGrooming(RapidEscalationGrooming):
    """Grooming that exploits immediate opportunities rather than planned relationship development."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#OpportunisticGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PeerPersonaGrooming(EducatorGrooming):
    """Grooming using false peer identity to establish rapport with victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#PeerPersonaGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PlatformAnonymityFeature:
    """Platform features that enable anonymous communication (guest messaging, temporary accounts, no profile requirements)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#PlatformAnonymityFeature"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PositionOfTrustGrooming(EducatorGrooming):
    """Grooming that exploits educator's position of trust and authority over students."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#PositionOfTrustGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PreyBehaviorPattern(GroomingPattern):
    """Pattern of targeting vulnerable children or specific victim characteristics."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#PreyBehaviorPattern"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PrivilegedVictimTargeting(EliteInstitutionTargeting):
    """Targeting of victims from privileged backgrounds who may be less likely to report."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#PrivilegedVictimTargeting"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PublicToPrivateGrooming(PhysicalSpaceGrooming):
    """Grooming that transitions from public contact to private exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#PublicToPrivateGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ReciprocityGrooming(SexualContentExchangeGrooming):
    """Grooming technique encouraging victim to reciprocate with sexual content."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#ReciprocityGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ReputationBasedSilencing(EliteInstitutionTargeting):
    """Exploitation of institutional reputation to discourage victim reporting."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#ReputationBasedSilencing"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SameDayProgression(RapidEscalationGrooming):
    """Grooming progression from initial contact to sexual exploitation within the same day."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#SameDayProgression"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SecrecyRequest(GroomingMessage):
    """Instruction to keep communication or relationship secret from parents or authorities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#SecrecyRequest"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SexualConsequenceGameGrooming(PhysicalSpaceGrooming):
    """Physical-space grooming pattern where the perpetrator frames sexualized contact as part of a game with consequences, typically involving multiple juveniles in a group context (e.g., sleepovers, peer g"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#SexualConsequenceGameGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    game_context: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:gameContext', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    participant_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:participantCount', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    rule_structure_description: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:ruleStructureDescription', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SexualSolicitation(GroomingMessage):
    """Message explicitly requesting sexual activity, images, or meetings from a child."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#SexualSolicitation"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SexualizationPhase(ConditioningPhase):
    """Phase involving introduction of sexual content and normalization of inappropriate behavior."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#SexualizationPhase"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SkippedGroomingPhases(RapidEscalationGrooming):
    """Grooming that bypasses traditional conditioning phases such as trust building, isolation, and normalization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#SkippedGroomingPhases"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StreetBasedGrooming(PhysicalSpaceGrooming):
    """Grooming that begins with street-based contact and recruitment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#StreetBasedGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SubstanceInducedVulnerabilityGrooming(SubstanceFacilitatedGrooming):
    """Grooming that creates vulnerability through substance administration."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#SubstanceInducedVulnerabilityGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TeenageImpersonationGrooming(PeerPersonaGrooming):
    """Grooming involving impersonation of teenage peer to gain victim trust."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#TeenageImpersonationGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TrustBuilding(ConditioningBehavior):
    """Trust-rapport conditioning behavior establishing emotional connection with the child victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#TrustBuilding"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    trust_building_method: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:trustBuildingMethod', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    trust_development_rate: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:trustDevelopmentRate', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    trust_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:trustLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class TrustBuildingBehavior(ConditioningBehavior):
    """Early grooming stage focused on establishing emotional connection with the child victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#TrustBuildingBehavior"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TrustBuildingPhase(ConditioningPhase):
    """Phase focused on building emotional connection and trust with victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#TrustBuildingPhase"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TrustThroughAnonymity(TrustBuildingBehavior):
    """Building trust by appearing less threatening through anonymous contact."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#TrustThroughAnonymity"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class UnverifiedUserProfile(_uco_observable.Account):
    """User account with minimal or no identity verification enabling anonymous contact."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#UnverifiedUserProfile"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class VehicleBasedGrooming(PhysicalSpaceGrooming):
    """Grooming that uses vehicles for isolation and exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#VehicleBasedGrooming"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimResponse(_uco_observable.Message):
    """Child's response to grooming behavior, indicating compliance, resistance, or confusion."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#VictimResponse"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class VictimComplianceInPhysicalMeeting(VictimResponse):
    """Victim's agreement or compliance with arranged physical meeting."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#VictimComplianceInPhysicalMeeting"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimVulnerability(_uco_core.UcoObject):
    """Characteristics or circumstances that make a child more susceptible to grooming."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#VictimVulnerability"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    exploitability_score: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:exploitabilityScore', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    vulnerability_duration: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:vulnerabilityDuration', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    vulnerability_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:vulnerabilityLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    vulnerability_stability: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:vulnerabilityStability', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    vulnerability_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-grooming:vulnerabilityType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class VictimVulnerabilitySituation(_cac_core.Situation):
    """Circumstances that make a child more susceptible to grooming."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#VictimVulnerabilitySituation"
    NAMESPACE_PREFIX: str = "cacontology-grooming"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
