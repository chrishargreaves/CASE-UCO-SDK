"""CAC Ontology - Crimes Against Children — cacontology_street_recruitment module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar, Optional

import case_uco.uco.core as _uco_core
import case_uco.uco.location as _uco_location
from case_uco_cac import cac_core as _cac_core
from case_uco_cac import cacontology_grooming as _cacontology_grooming
from case_uco_cac import cacontology_sex_trafficking as _cacontology_sex_trafficking
from case_uco_cac._context import NAMESPACES

__all__ = ["AgeVulnerabilityIndicator", "AlcoholFacilitation", "BehavioralVulnerabilityIndicator", "BodySellingProposition", "CasualConversationApproach", "CommercialDistrict", "DelayedReporting", "DemographicTargeting", "DigitalFollowUp", "DigitalToPhysicalBridge", "DirectSolicitationApproach", "DirectTraffickingProposition", "DisclosureToAuthorities", "DrugFacilitatedVulnerability", "EconomicIncentivePresentation", "EscapeAttempt", "ExplicitCommercialOffer", "FoodOfferApproach", "HelpOfferApproach", "HelpSeekingBehavior", "HighTrafficArea", "HighwayLocation", "ImmediateExploitationAttempt", "ImmediateIsolation", "ImmediateReporting", "ImpairmentExploitation", "InitialStreetContact", "IsolatedLocation", "IsolationVulnerabilityIndicator", "LocationTransition", "MarijuanaFacilitation", "NeighborhoodTargeting", "NextDayFollowUp", "OpportunisticExploitation", "PersistenceAfterRejection", "PhoneChargingOffer", "PhysicalVulnerabilityIndicator", "PostContactReinforcement", "PretextBasedApproach", "ProstitutionProposition", "PublicSpaceTargeting", "RapidEscalationRecruitment", "ResidentialArea", "SameDayProgression", "SecondaryLocationExploitation", "SocioeconomicVulnerabilityIndicator", "StreetBasedRecruitment", "StreetRecruitmentLocation", "StreetVulnerabilityAssessment", "StrippingProposition", "SubstanceBasedControl", "SubstanceFacilitatedRecruitment", "TextMessageFollowUp", "TraffickingPropositionReinforcement", "TraffickingPropositionRejection", "TransitArea", "TransportationOfferApproach", "VehicleBasedIsolation", "VehicleLocation", "VictimReporting", "VictimResistance", "VictimStreetResponse", "VulnerabilityIndicator", "VulnerableNeighborhood"]


@dataclass
class VulnerabilityIndicator(_uco_core.UcoObject):
    """Observable characteristic or behavior indicating potential trafficking vulnerability."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#VulnerabilityIndicator"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PhysicalVulnerabilityIndicator(VulnerabilityIndicator):
    """Physical appearance or condition indicating vulnerability (youth, fatigue, distress)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#PhysicalVulnerabilityIndicator"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AgeVulnerabilityIndicator(PhysicalVulnerabilityIndicator):
    """Apparent youth or minor status making individual vulnerable to exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#AgeVulnerabilityIndicator"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    apparent_age: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:apparentAge', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class StreetBasedRecruitment(_cacontology_sex_trafficking.VictimRecruitment):
    """Trafficking recruitment occurring in public spaces through direct physical approach and opportunistic exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#StreetBasedRecruitment"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    comment: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:comment', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SubstanceFacilitatedRecruitment(StreetBasedRecruitment):
    """Use of alcohol or drugs to facilitate trafficking recruitment and reduce victim resistance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#SubstanceFacilitatedRecruitment"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    substance_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:substanceType', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class DrugFacilitatedVulnerability(SubstanceFacilitatedRecruitment):
    """Creation or exploitation of vulnerability through substance administration."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#DrugFacilitatedVulnerability"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    administration_method: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:administrationMethod', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class AlcoholFacilitation(DrugFacilitatedVulnerability):
    """Use of alcohol to impair victim judgment and facilitate exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#AlcoholFacilitation"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class BehavioralVulnerabilityIndicator(VulnerabilityIndicator):
    """Behavioral patterns indicating vulnerability (isolation, confusion, seeking help)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#BehavioralVulnerabilityIndicator"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    distress_indicators: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:distressIndicators', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class DirectTraffickingProposition(_cacontology_grooming.SexualExploitation):
    """Explicit, immediate proposition for victim to engage in commercial sexual activity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#DirectTraffickingProposition"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    explicitness_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:explicitnessLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    proposition_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:propositionType', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ExplicitCommercialOffer(DirectTraffickingProposition):
    """Direct offer of money in exchange for sexual services or performances."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#ExplicitCommercialOffer"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    money_amount_mentioned: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:moneyAmountMentioned', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class ProstitutionProposition(ExplicitCommercialOffer):
    """Direct proposition to engage in prostitution or selling sexual services."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#ProstitutionProposition"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class BodySellingProposition(ProstitutionProposition):
    """Explicit suggestion that victim can make money by 'selling their body'."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#BodySellingProposition"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InitialStreetContact(_cac_core.ExploitationEvent):
    """First contact between trafficker and victim occurring in public space."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#InitialStreetContact"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    approach_method: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:approachMethod', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    contact_duration: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:contactDuration', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    initial_contact_location: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:initialContactLocation', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CasualConversationApproach(InitialStreetContact):
    """Approach through seemingly innocent casual conversation to assess vulnerability."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#CasualConversationApproach"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    conversation_topic: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:conversationTopic', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class StreetRecruitmentLocation(_uco_location.Location):
    """Specific location where street-based trafficking recruitment occurs."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#StreetRecruitmentLocation"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class HighTrafficArea(StreetRecruitmentLocation):
    """Public area with high pedestrian traffic used for victim identification."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#HighTrafficArea"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CommercialDistrict(HighTrafficArea):
    """Commercial areas with restaurants, shops, and businesses used for recruitment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#CommercialDistrict"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimStreetResponse(_cac_core.Event):
    """Victim's response to street-based recruitment attempts and trafficking propositions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#VictimStreetResponse"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    response_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:responseType', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class HelpSeekingBehavior(VictimStreetResponse):
    """Victim's attempts to seek help or report trafficking recruitment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#HelpSeekingBehavior"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimReporting(HelpSeekingBehavior):
    """Victim's decision to report trafficking recruitment or assault to authorities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#VictimReporting"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    reporting_delay: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:reportingDelay', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    reporting_method: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:reportingMethod', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class DelayedReporting(VictimReporting):
    """Victim reporting that occurs days or weeks after initial incident."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#DelayedReporting"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PublicSpaceTargeting(StreetBasedRecruitment):
    """Systematic targeting of vulnerable individuals in specific public locations for trafficking recruitment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#PublicSpaceTargeting"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DemographicTargeting(PublicSpaceTargeting):
    """Targeting individuals based on specific demographic characteristics indicating vulnerability."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#DemographicTargeting"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PostContactReinforcement(_cac_core.ExploitationEvent):
    """Follow-up contact after initial encounter to reinforce trafficking proposition."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#PostContactReinforcement"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    follow_up_delay: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:followUpDelay', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    follow_up_method: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:followUpMethod', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class DigitalFollowUp(PostContactReinforcement):
    """Follow-up through digital communication channels (text, social media, calls)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#DigitalFollowUp"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DigitalToPhysicalBridge(DigitalFollowUp):
    """Use of digital communication to maintain connection after physical encounter."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#DigitalToPhysicalBridge"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DirectSolicitationApproach(InitialStreetContact):
    """Direct approach with immediate commercial sexual proposition."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#DirectSolicitationApproach"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DisclosureToAuthorities(VictimReporting):
    """Victim's disclosure of trafficking recruitment or exploitation to law enforcement."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#DisclosureToAuthorities"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EconomicIncentivePresentation(DirectTraffickingProposition):
    """Presentation of financial benefits and earning potential from commercial sexual activity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#EconomicIncentivePresentation"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    economic_incentive: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:economicIncentive', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class VictimResistance(VictimStreetResponse):
    """Active resistance to trafficking recruitment attempts or exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#VictimResistance"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    resistance_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:resistanceLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class EscapeAttempt(VictimResistance):
    """Victim's attempt to escape from trafficking situation or recruitment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#EscapeAttempt"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PretextBasedApproach(InitialStreetContact):
    """Initial approach using false pretext or offer of assistance to establish contact."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#PretextBasedApproach"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    pretext_used: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:pretextUsed', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class HelpOfferApproach(PretextBasedApproach):
    """Approach offering assistance such as phone charging, food, transportation, or shelter."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#HelpOfferApproach"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    help_offer_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:helpOfferType', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class FoodOfferApproach(HelpOfferApproach):
    """Approach offering food or meals to establish trust and create obligation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#FoodOfferApproach"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class IsolatedLocation(_uco_location.Location):
    """Secluded location used for exploitation away from public view."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#IsolatedLocation"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class HighwayLocation(IsolatedLocation):
    """Location near or alongside highways used for isolated exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#HighwayLocation"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ImmediateExploitationAttempt(DirectTraffickingProposition):
    """Attempt to immediately engage victim in commercial sexual activity without extended grooming."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#ImmediateExploitationAttempt"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RapidEscalationRecruitment(StreetBasedRecruitment):
    """Trafficking recruitment with accelerated timeline from initial contact to exploitation attempt."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#RapidEscalationRecruitment"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    escalation_timeframe: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:escalationTimeframe', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class ImmediateIsolation(RapidEscalationRecruitment):
    """Rapid removal of victim from public space to isolated location for exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#ImmediateIsolation"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ImmediateReporting(VictimReporting):
    """Victim reporting that occurs immediately or within hours of incident."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#ImmediateReporting"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SubstanceBasedControl(SubstanceFacilitatedRecruitment):
    """Use of substance dependency or impairment to maintain control over victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#SubstanceBasedControl"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ImpairmentExploitation(SubstanceBasedControl):
    """Exploitation of victim while impaired by substances to reduce resistance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#ImpairmentExploitation"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    impairment_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:impairmentLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class IsolationVulnerabilityIndicator(VulnerabilityIndicator):
    """Indicators that individual is alone or lacks social support (walking alone, no companions)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#IsolationVulnerabilityIndicator"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    isolation_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:isolationLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class LocationTransition(_cac_core.ExploitationEvent):
    """Movement of victim from initial contact location to exploitation location."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#LocationTransition"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    transportation_method: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:transportationMethod', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class MarijuanaFacilitation(DrugFacilitatedVulnerability):
    """Use of marijuana to reduce victim inhibitions and facilitate exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#MarijuanaFacilitation"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class NeighborhoodTargeting(PublicSpaceTargeting):
    """Targeting specific neighborhoods or geographic areas known for vulnerable populations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#NeighborhoodTargeting"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class NextDayFollowUp(PostContactReinforcement):
    """Follow-up contact occurring the day after initial encounter."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#NextDayFollowUp"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OpportunisticExploitation(StreetBasedRecruitment):
    """Exploitation of vulnerable individuals encountered in public spaces without prior planning or relationship."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#OpportunisticExploitation"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TraffickingPropositionReinforcement(PostContactReinforcement):
    """Repeated presentation of trafficking proposition to overcome initial resistance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#TraffickingPropositionReinforcement"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    reinforcement_attempts: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:reinforcementAttempts', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class PersistenceAfterRejection(TraffickingPropositionReinforcement):
    """Continued recruitment attempts after initial rejection of trafficking proposition."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#PersistenceAfterRejection"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    persistence_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:persistenceLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PhoneChargingOffer(HelpOfferApproach):
    """Specific pretext offering to charge victim's phone in vehicle or location."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#PhoneChargingOffer"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ResidentialArea(StreetRecruitmentLocation):
    """Residential neighborhoods where victims may be walking or living."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#ResidentialArea"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SameDayProgression(RapidEscalationRecruitment):
    """Progression from initial contact to sexual assault and trafficking proposition within same day."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#SameDayProgression"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    same_day_progression: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:sameDayProgression', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})


@dataclass
class SecondaryLocationExploitation(LocationTransition):
    """Exploitation occurring at secondary location away from initial contact point."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#SecondaryLocationExploitation"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    distance_from_contact: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:distanceFromContact', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    exploitation_location: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:exploitationLocation', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SocioeconomicVulnerabilityIndicator(VulnerabilityIndicator):
    """Indicators of economic hardship or social disadvantage (clothing, possessions, location)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#SocioeconomicVulnerabilityIndicator"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StreetVulnerabilityAssessment(_cac_core.ExploitationEvent):
    """Rapid assessment of individual vulnerability factors in public space encounters."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#StreetVulnerabilityAssessment"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    vulnerability_indicators: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-street-recruitment:vulnerabilityIndicators', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class StrippingProposition(ExplicitCommercialOffer):
    """Specific proposition to engage in stripping or exotic dancing for money."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#StrippingProposition"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TextMessageFollowUp(DigitalFollowUp):
    """Follow-up through text messaging to reinforce trafficking proposition."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#TextMessageFollowUp"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TraffickingPropositionRejection(VictimStreetResponse):
    """Victim's rejection of trafficking proposition or commercial sexual offer."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#TraffickingPropositionRejection"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TransitArea(HighTrafficArea):
    """Transportation hubs or transit areas where vulnerable individuals may be targeted."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#TransitArea"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TransportationOfferApproach(HelpOfferApproach):
    """Offer of rides or transportation to isolated locations for exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#TransportationOfferApproach"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VehicleBasedIsolation(ImmediateIsolation):
    """Use of vehicle to isolate victim and transport to exploitation location."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#VehicleBasedIsolation"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VehicleLocation(IsolatedLocation):
    """Vehicle used as location for exploitation or transportation to exploitation site."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#VehicleLocation"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VulnerableNeighborhood(ResidentialArea):
    """Neighborhood with high poverty, crime, or social vulnerability targeted by traffickers."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/street#VulnerableNeighborhood"
    NAMESPACE_PREFIX: str = "cacontology-street-recruitment"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
