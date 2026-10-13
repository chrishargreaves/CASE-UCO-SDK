"""CAC Ontology - Crimes Against Children — cacontology-grooming module."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AcceleratedTrustExploitation:
    """Rapid exploitation of minimal trust established through pretexts or assistance offers."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#AcceleratedTrustExploitation"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class AccountReplacementEvent:
    """Pattern where an offender whose account is banned or blocked creates a new account and returns to an earlier offense phase (typically initial contact). The lifecycle resets rather than terminates — st"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#AccountReplacementEvent"
    original_account_id: Optional[Account] = field(default=None)
    replacement_account_id: Optional[Account] = field(default=None)
    resumes_at: Optional[Phase] = field(default=None)
    triggered_by: Optional[str] = field(default=None)


@dataclass
class AlcoholFacilitatedGrooming:
    """Grooming using alcohol to impair victim judgment and reduce resistance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#AlcoholFacilitatedGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class AnonymousInitiation:
    """Starting contact without revealing true identity or personal information."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#AnonymousInitiation"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class AnonymousPlatformContact:
    """Initial contact made through platforms that allow anonymous messaging or minimal user verification."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#AnonymousPlatformContact"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class BluntRecruitmentGrooming:
    """Direct, unsubtle recruitment for trafficking without gradual persuasion techniques."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#BluntRecruitmentGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class ChildVictim:
    """Minor child who is the target of grooming behavior. When analysis depends on the victim’s exact age at specific grooming events (e.g., 13-or-younger online grooming in 2025), that age SHOULD be repres"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#ChildVictim"
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
class ConditioningBehavior:
    """Offender behavior that shapes victim readiness, compliance, dependency, or situational constraints preparatory to direct exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#ConditioningBehavior"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class ConditioningPhase:
    """Grooming-process phase in which the offender conditions the victim or situation for exploitation — including rapport, isolation, normalization, and compliance shaping prior to the primary exploitation"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#ConditioningPhase"
    conditioning_mode: Optional[str] = field(default=None)
    has_grooming_phase_begin_point: Optional[TypedLiteral] = field(default=None)
    has_grooming_phase_end_point: Optional[TypedLiteral] = field(default=None)


@dataclass
class CrossInstitutionalGrooming:
    """Grooming targeting students from multiple educational institutions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#CrossInstitutionalGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class DirectTraffickingPropositionGrooming:
    """Grooming involving explicit, immediate propositions for commercial sexual activity without gradual normalization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#DirectTraffickingPropositionGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class EconomicIncentiveGrooming:
    """Grooming that emphasizes financial benefits of commercial sexual activity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#EconomicIncentiveGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class EducatorGrooming:
    """Grooming behavior by educational personnel leveraging position of trust and authority."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#EducatorGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class EliteInstitutionTargeting:
    """Targeting of students from elite or prestigious educational institutions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#EliteInstitutionTargeting"


@dataclass
class Enticement:
    """Direct solicitation of a child to engage in illegal sexual activity or meet for such purposes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#Enticement"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class EscalationPattern:
    """Progressive increase in inappropriate content or requests over time."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#EscalationPattern"
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
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    escalation_duration: Optional[float] = field(default=None)
    escalation_predictability: Optional[float] = field(default=None)
    escalation_speed: Optional[str] = field(default=None)
    escalation_type: Optional[str] = field(default=None)
    pattern_confidence: Optional[float] = field(default=None)


@dataclass
class ExplicitCommercialOfferGrooming:
    """Grooming involving direct offers of money in exchange for sexual services."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#ExplicitCommercialOfferGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class ExploitationPhase:
    """Final phase involving direct sexual exploitation and abuse."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#ExploitationPhase"


@dataclass
class FabricatedPersona:
    """A fabricated identity (e.g., a fictitious minor peer) created and controlled by an offender to contact, groom, lure, or coerce victims. The same persona may be reused across victims and platforms. Com"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#FabricatedPersona"
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
    claimed_age: Optional[str] = field(default=None)
    claimed_display_name: Optional[str] = field(default=None)
    claimed_gender: Optional[str] = field(default=None)


@dataclass
class GraphicConversationGrooming:
    """Grooming involving progressively graphic sexual conversations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#GraphicConversationGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class GroomingBehavior:
    """Predatory behavior designed to prepare a child for abuse by building trust, isolating them, and normalizing inappropriate contact."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#GroomingBehavior"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class GroomingMessage:
    """Communication containing grooming behavior or inappropriate content directed at a child."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#GroomingMessage"
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
class GroomingPattern:
    """Identifiable pattern of behavior across multiple communications or interactions that indicates grooming."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#GroomingPattern"
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
class GroomingPhase:
    """A temporal phase within the grooming process."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#GroomingPhase"


@dataclass
class ImmediateExploitationAttempt:
    """Attempt to immediately exploit victim without extended grooming or relationship building."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#ImmediateExploitationAttempt"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class ImmediateMonetizationGrooming:
    """Grooming focused on immediate monetization of victim's sexuality."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#ImmediateMonetizationGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class ImpairmentBasedGrooming:
    """Grooming that exploits victim impairment from substances to reduce resistance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#ImpairmentBasedGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class InappropriateGift:
    """Offer or provision of gifts, money, or favors as part of grooming process."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#InappropriateGift"
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
class InitialContactPhase:
    """First phase of grooming involving initial contact and relationship establishment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#InitialContactPhase"


@dataclass
class InitiatorContentSending:
    """Grooming phase where perpetrator sends sexual content to victim first."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#InitiatorContentSending"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class InterstateTransportPlan:
    """Planning to transport victim across state lines for illegal purposes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#InterstateTransportPlan"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class IsolationBasedGrooming:
    """Grooming that relies on physical isolation to reduce victim resistance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#IsolationBasedGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class IsolationBehavior:
    """Attempts to separate child from parents, friends, or other support systems."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#IsolationBehavior"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class IsolationPhase:
    """Phase aimed at separating victim from support systems and creating dependency."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#IsolationPhase"
    conditioning_mode: Optional[str] = field(default=None)
    has_grooming_phase_begin_point: Optional[TypedLiteral] = field(default=None)
    has_grooming_phase_end_point: Optional[TypedLiteral] = field(default=None)


@dataclass
class IsolationTactics:
    """Isolation conditioning behavior separating the victim from support systems."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#IsolationTactics"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)
    isolation_effectiveness: Optional[str] = field(default=None)
    isolation_method: Optional[str] = field(default=None)
    isolation_progress_rate: Optional[float] = field(default=None)


@dataclass
class LocationSpecificGrooming:
    """Grooming that references or prepares for specific physical locations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#LocationSpecificGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class MaintenancePhase:
    """Ongoing phase to maintain control and continue exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#MaintenancePhase"


@dataclass
class ManipulationPattern:
    """Systematic use of psychological manipulation techniques to control victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#ManipulationPattern"
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
class MarijuanaFacilitatedGrooming:
    """Grooming using marijuana to reduce victim inhibitions and facilitate exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#MarijuanaFacilitatedGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class MultipleAccountGrooming:
    """Grooming using multiple fake accounts to maintain deceptive identity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#MultipleAccountGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class NormalizationBehavior:
    """Gradual introduction of sexual topics to normalize inappropriate behavior."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#NormalizationBehavior"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class NormalizationGrooming:
    """Grooming technique to normalize sexual conversations and content sharing."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#NormalizationGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class OfflineControlEstablishment:
    """Establishing control over victim in preparation for physical contact."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#OfflineControlEstablishment"
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
class OnlineGrooming:
    """Grooming behavior conducted through online platforms and digital communication channels."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#OnlineGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class OnlineGroomingSituation:
    """Overall situation encompassing the grooming relationship and interactions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#OnlineGroomingSituation"


@dataclass
class OnlinePredationSituation:
    """Active situation where predator is engaging with potential victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#OnlinePredationSituation"


@dataclass
class OnlinePredator:
    """Individual who engages in grooming behavior toward children online. Age-at-time for this offender MAY be captured via cacontology-temporal:AgeAtTimeSituation instances when age-gap and legal-capacity """

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#OnlinePredator"
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
class OnlineToOfflineProgression:
    """Escalation from online grooming to arranging physical meetings or contact."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#OnlineToOfflineProgression"
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
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    escalation_duration: Optional[float] = field(default=None)
    escalation_predictability: Optional[float] = field(default=None)
    escalation_speed: Optional[str] = field(default=None)
    escalation_type: Optional[str] = field(default=None)
    pattern_confidence: Optional[float] = field(default=None)
    progression_duration: Optional[int] = field(default=None)
    progression_stages: Optional[int] = field(default=None)
    transition_likelihood: Optional[float] = field(default=None)


@dataclass
class OpportunisticGrooming:
    """Grooming that exploits immediate opportunities rather than planned relationship development."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#OpportunisticGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class PeerPersonaGrooming:
    """Grooming using false peer identity to establish rapport with victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#PeerPersonaGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class PhysicalMeetingArrangement:
    """Coordination of in-person meeting between predator and victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#PhysicalMeetingArrangement"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class PhysicalSpaceGrooming:
    """Grooming that occurs in physical spaces rather than digital platforms."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#PhysicalSpaceGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class PlatformAnonymityFeature:
    """Platform features that enable anonymous communication (guest messaging, temporary accounts, no profile requirements)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#PlatformAnonymityFeature"


@dataclass
class PositionOfTrustGrooming:
    """Grooming that exploits educator's position of trust and authority over students."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#PositionOfTrustGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class PreyBehaviorPattern:
    """Pattern of targeting vulnerable children or specific victim characteristics."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#PreyBehaviorPattern"
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
class PrivilegedVictimTargeting:
    """Targeting of victims from privileged backgrounds who may be less likely to report."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#PrivilegedVictimTargeting"


@dataclass
class PublicToPrivateGrooming:
    """Grooming that transitions from public contact to private exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#PublicToPrivateGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class RapidEscalationGrooming:
    """Grooming with accelerated timeline from initial contact to exploitation attempt, bypassing traditional relationship-building phases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#RapidEscalationGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class ReciprocityGrooming:
    """Grooming technique encouraging victim to reciprocate with sexual content."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#ReciprocityGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class ReputationBasedSilencing:
    """Exploitation of institutional reputation to discourage victim reporting."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#ReputationBasedSilencing"


@dataclass
class SameDayProgression:
    """Grooming progression from initial contact to sexual exploitation within the same day."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#SameDayProgression"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class SecrecyRequest:
    """Instruction to keep communication or relationship secret from parents or authorities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#SecrecyRequest"
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
class SexualConsequenceGameGrooming:
    """Physical-space grooming pattern where the perpetrator frames sexualized contact as part of a game with consequences, typically involving multiple juveniles in a group context (e.g., sleepovers, peer g"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#SexualConsequenceGameGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)
    game_context: Optional[str] = field(default=None)
    participant_count: Optional[int] = field(default=None)
    rule_structure_description: Optional[str] = field(default=None)


@dataclass
class SexualContentExchangeGrooming:
    """Grooming involving exchange of sexual content to normalize sexual behavior."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#SexualContentExchangeGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class SexualExploitation:
    """Direct exploitation of child for sexual purposes including solicitation of images or performances."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#SexualExploitation"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class SexualSolicitation:
    """Message explicitly requesting sexual activity, images, or meetings from a child."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#SexualSolicitation"
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
class SexualizationPhase:
    """Phase involving introduction of sexual content and normalization of inappropriate behavior."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#SexualizationPhase"
    conditioning_mode: Optional[str] = field(default=None)
    has_grooming_phase_begin_point: Optional[TypedLiteral] = field(default=None)
    has_grooming_phase_end_point: Optional[TypedLiteral] = field(default=None)


@dataclass
class SkippedGroomingPhases:
    """Grooming that bypasses traditional conditioning phases such as trust building, isolation, and normalization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#SkippedGroomingPhases"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class StreetBasedGrooming:
    """Grooming that begins with street-based contact and recruitment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#StreetBasedGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class SubstanceFacilitatedGrooming:
    """Grooming that uses alcohol or drugs to reduce victim resistance and facilitate exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#SubstanceFacilitatedGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class SubstanceInducedVulnerabilityGrooming:
    """Grooming that creates vulnerability through substance administration."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#SubstanceInducedVulnerabilityGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class TeenageImpersonationGrooming:
    """Grooming involving impersonation of teenage peer to gain victim trust."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#TeenageImpersonationGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class TravelArrangement:
    """Planning or facilitating travel for victim to meet predator."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#TravelArrangement"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class TrustBuilding:
    """Trust-rapport conditioning behavior establishing emotional connection with the child victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#TrustBuilding"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)
    trust_building_method: Optional[str] = field(default=None)
    trust_development_rate: Optional[float] = field(default=None)
    trust_level: Optional[str] = field(default=None)


@dataclass
class TrustBuildingBehavior:
    """Early grooming stage focused on establishing emotional connection with the child victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#TrustBuildingBehavior"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class TrustBuildingPhase:
    """Phase focused on building emotional connection and trust with victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#TrustBuildingPhase"
    conditioning_mode: Optional[str] = field(default=None)
    has_grooming_phase_begin_point: Optional[TypedLiteral] = field(default=None)
    has_grooming_phase_end_point: Optional[TypedLiteral] = field(default=None)


@dataclass
class TrustThroughAnonymity:
    """Building trust by appearing less threatening through anonymous contact."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#TrustThroughAnonymity"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class UnverifiedUserProfile:
    """User account with minimal or no identity verification enabling anonymous contact."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#UnverifiedUserProfile"
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
class VehicleBasedGrooming:
    """Grooming that uses vehicles for isolation and exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#VehicleBasedGrooming"
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    has_end_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    analysis_completeness: Optional[float] = field(default=None)
    behavior_frequency: Optional[str] = field(default=None)
    behavior_intensity: Optional[str] = field(default=None)
    behavior_type: Optional[str] = field(default=None)
    data_confidence: Optional[float] = field(default=None)
    grooming_effectiveness: Optional[float] = field(default=None)
    grooming_stage: Optional[str] = field(default=None)
    manipulation_level: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class VictimComplianceInPhysicalMeeting:
    """Victim's agreement or compliance with arranged physical meeting."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#VictimComplianceInPhysicalMeeting"
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
class VictimResponse:
    """Child's response to grooming behavior, indicating compliance, resistance, or confusion."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#VictimResponse"
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
class VictimTargeting:
    """The process by which an offender identifies and selects a potential victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#VictimTargeting"


@dataclass
class VictimVulnerability:
    """Characteristics or circumstances that make a child more susceptible to grooming."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#VictimVulnerability"
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
    has_begin_point_in_xsd_date_time_stamp: Optional[TypedLiteral] = field(default=None)
    exploitability_score: Optional[float] = field(default=None)
    vulnerability_duration: Optional[float] = field(default=None)
    vulnerability_level: Optional[str] = field(default=None)
    vulnerability_stability: Optional[str] = field(default=None)
    vulnerability_type: Optional[str] = field(default=None)


@dataclass
class VictimVulnerabilitySituation:
    """Circumstances that make a child more susceptible to grooming."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/grooming#VictimVulnerabilitySituation"

