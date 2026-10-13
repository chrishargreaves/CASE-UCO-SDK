"""CAC Ontology - Crimes Against Children — cacontology-sex-trafficking module."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AdultTraffickingVictimRole:
    """Role of adult being sex trafficked through force, fraud, or coercion. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#AdultTraffickingVictimRole"
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
class AgingOutVictimProfile:
    """Vulnerability profile for youth aging out of foster care system."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#AgingOutVictimProfile"
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
class AssociateTraffickerRole:
    """Supporting role in trafficking operation, assisting primary traffickers. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#AssociateTraffickerRole"
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
class CommercialSexualExploitation:
    """Forced engagement in commercial sexual activities for the traffickers' profit. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#CommercialSexualExploitation"


@dataclass
class CrossJurisdictionalControl:
    """Maintenance of victim control across multiple jurisdictions through coordinated trafficking network. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#CrossJurisdictionalControl"


@dataclass
class DisruptionPhase:
    """Phase when trafficking enterprise faces law enforcement intervention."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#DisruptionPhase"


@dataclass
class EarningsCollection:
    """Collection of money earned through victim exploitation by trafficking operation. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#EarningsCollection"


@dataclass
class EstablishmentPhase:
    """Initial phase of trafficking enterprise formation and recruitment setup."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#EstablishmentPhase"


@dataclass
class ExpansionPhase:
    """Phase of trafficking enterprise growth, adding victims and locations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#ExpansionPhase"


@dataclass
class FinancialFacilitatorRole:
    """Role managing financial aspects including collecting earnings and money laundering. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#FinancialFacilitatorRole"
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
class InterstateVictimTransport:
    """Transportation of trafficking victims across state lines for commercial sexual exploitation. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#InterstateVictimTransport"


@dataclass
class MinorTraffickingVictimRole:
    """Role of minor (under 18) being sex trafficked. Modeled as anti-rigid gUFO Role. Concrete victim age at specific trafficking operations SHOULD be represented using cacontology-temporal:AgeAtTimeSituati"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#MinorTraffickingVictimRole"
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
class MultiJurisdictionalSituation:
    """Complex situation involving trafficking operations across multiple jurisdictions requiring coordinated law enforcement response."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#MultiJurisdictionalSituation"


@dataclass
class MultiStateTraffickingConspiracy:
    """Criminal conspiracy spanning multiple states for trafficking operations (e.g., Brooklyn-North Carolina network). Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#MultiStateTraffickingConspiracy"


@dataclass
class OngoingDangerResponse:
    """Response to situations where victims are identified as being in ongoing danger from traffickers. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#OngoingDangerResponse"
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
    action_count: Optional[int] = field(default=None)
    action_status: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    environment: Optional[UcoObject] = field(default=None)
    error: list[UcoObject] = field(default_factory=list)
    instrument: list[UcoObject] = field(default_factory=list)
    location: list[Location] = field(default_factory=list)
    object: list[UcoObject] = field(default_factory=list)
    participant: list[UcoObject] = field(default_factory=list)
    performer: Optional[UcoObject] = field(default=None)
    result: list[UcoObject] = field(default_factory=list)
    start_time: Optional[datetime] = field(default=None)
    subaction: list[Action] = field(default_factory=list)
    was_informed_by: list[InvestigativeAction] = field(default_factory=list)


@dataclass
class OperationalPhase:
    """Active operational phase of trafficking enterprise with established victim control."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#OperationalPhase"


@dataclass
class PrimaryTraffickerRole:
    """Leading role in trafficking operation, often controlling multiple victims and coordinating activities. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#PrimaryTraffickerRole"
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
class RecruitmentFacilitatorRole:
    """Role focused on recruiting and grooming new victims for trafficking. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#RecruitmentFacilitatorRole"
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
class RunawayVictimProfile:
    """Vulnerability profile for runaway or homeless youth targeted by traffickers."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#RunawayVictimProfile"
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
class TraffickerRole:
    """Role of individual involved in sex trafficking operations. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#TraffickerRole"
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
class TraffickingCell:
    """Smaller operational unit within trafficking ring, often controlling specific victims or geographic areas. Modeled as specialized gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#TraffickingCell"
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
class TraffickingEnterprise:
    """Criminal organization engaged in systematic sex trafficking operations with multiple defendants and coordinated activities. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#TraffickingEnterprise"
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
class TraffickingHierarchy:
    """Organizational structure within trafficking enterprise defining roles and authority levels."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#TraffickingHierarchy"
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
class TraffickingNetworkSituation:
    """Complex situation encompassing active trafficking network operations across multiple jurisdictions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#TraffickingNetworkSituation"


@dataclass
class TraffickingOperation:
    """Coordinated trafficking activity involving multiple perpetrators, victims, and locations. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#TraffickingOperation"


@dataclass
class TraffickingRing:
    """Coordinated group of traffickers operating across multiple jurisdictions with shared victims and resources (e.g., 8-defendant Brooklyn case). Modeled as specialized gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#TraffickingRing"
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
class TraffickingVictimRescue:
    """Specialized rescue operation for trafficking victims involving multiple agencies and victim services. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#TraffickingVictimRescue"
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
    action_count: Optional[int] = field(default=None)
    action_status: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    environment: Optional[UcoObject] = field(default=None)
    error: list[UcoObject] = field(default_factory=list)
    instrument: list[UcoObject] = field(default_factory=list)
    location: list[Location] = field(default_factory=list)
    object: list[UcoObject] = field(default_factory=list)
    participant: list[UcoObject] = field(default_factory=list)
    performer: Optional[UcoObject] = field(default=None)
    result: list[UcoObject] = field(default_factory=list)
    start_time: Optional[datetime] = field(default=None)
    subaction: list[Action] = field(default_factory=list)
    was_informed_by: list[InvestigativeAction] = field(default_factory=list)


@dataclass
class TraffickingVictimRole:
    """Role of person being exploited through sex trafficking. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#TraffickingVictimRole"
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
class TransportationFacilitatorRole:
    """Role focused on transporting victims between locations for trafficking purposes. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#TransportationFacilitatorRole"
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
class VictimControl:
    """Methods used to maintain psychological and physical control over trafficking victims. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#VictimControl"


@dataclass
class VictimControlSituation:
    """Ongoing situation of psychological and physical control maintained over trafficking victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#VictimControlSituation"


@dataclass
class VictimEmergencyResponse:
    """Emergency response to 911 calls from trafficking victims seeking help. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#VictimEmergencyResponse"
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
    action_count: Optional[int] = field(default=None)
    action_status: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    environment: Optional[UcoObject] = field(default=None)
    error: list[UcoObject] = field(default_factory=list)
    instrument: list[UcoObject] = field(default_factory=list)
    location: list[Location] = field(default_factory=list)
    object: list[UcoObject] = field(default_factory=list)
    participant: list[UcoObject] = field(default_factory=list)
    performer: Optional[UcoObject] = field(default=None)
    result: list[UcoObject] = field(default_factory=list)
    start_time: Optional[datetime] = field(default=None)
    subaction: list[Action] = field(default_factory=list)
    was_informed_by: list[InvestigativeAction] = field(default_factory=list)


@dataclass
class VictimRecruitment:
    """Process of identifying, targeting, and acquiring new victims for trafficking operations. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#VictimRecruitment"


@dataclass
class VictimRotation:
    """Systematic movement of victims between different locations to avoid detection and maintain control. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#VictimRotation"


@dataclass
class VictimSafetyAssessment:
    """Assessment of victim safety and ongoing threats from trafficking network. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#VictimSafetyAssessment"
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
    action_count: Optional[int] = field(default=None)
    action_status: Optional[str] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    environment: Optional[UcoObject] = field(default=None)
    error: list[UcoObject] = field(default_factory=list)
    instrument: list[UcoObject] = field(default_factory=list)
    location: list[Location] = field(default_factory=list)
    object: list[UcoObject] = field(default_factory=list)
    participant: list[UcoObject] = field(default_factory=list)
    performer: Optional[UcoObject] = field(default=None)
    result: list[UcoObject] = field(default_factory=list)
    start_time: Optional[datetime] = field(default=None)
    subaction: list[Action] = field(default_factory=list)
    was_informed_by: list[InvestigativeAction] = field(default_factory=list)


@dataclass
class VictimTransportation:
    """Transportation of trafficking victims between locations for commercial sexual exploitation. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#VictimTransportation"


@dataclass
class VictimVulnerabilityProfile:
    """Profile of factors that make individuals vulnerable to trafficking recruitment. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#VictimVulnerabilityProfile"
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

