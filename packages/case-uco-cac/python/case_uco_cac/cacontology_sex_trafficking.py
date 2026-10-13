"""CAC Ontology - Crimes Against Children — cacontology_sex_trafficking module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar, Optional

import case_uco.uco.identity as _uco_identity
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AdultTraffickingVictimRole", "AgingOutVictimProfile", "AssociateTraffickerRole", "CommercialSexualExploitation", "CrossJurisdictionalControl", "DisruptionPhase", "EarningsCollection", "EstablishmentPhase", "ExpansionPhase", "FinancialFacilitatorRole", "InterstateVictimTransport", "MinorTraffickingVictimRole", "MultiJurisdictionalSituation", "MultiStateTraffickingConspiracy", "OngoingDangerResponse", "OperationalPhase", "PrimaryTraffickerRole", "RecruitmentFacilitatorRole", "RunawayVictimProfile", "TraffickerRole", "TraffickingCell", "TraffickingEnterprise", "TraffickingHierarchy", "TraffickingNetworkSituation", "TraffickingOperation", "TraffickingRing", "TraffickingVictimRescue", "TraffickingVictimRole", "TransportationFacilitatorRole", "VictimControl", "VictimControlSituation", "VictimEmergencyResponse", "VictimRecruitment", "VictimRotation", "VictimSafetyAssessment", "VictimTransportation", "VictimVulnerabilityProfile"]


@dataclass
class TraffickingVictimRole(_cac_core.Role):
    """Role of person being exploited through sex trafficking. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#TraffickingVictimRole"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AdultTraffickingVictimRole(TraffickingVictimRole):
    """Role of adult being sex trafficked through force, fraud, or coercion. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#AdultTraffickingVictimRole"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimVulnerabilityProfile(_cac_core.PersonLikeEntity):
    """Profile of factors that make individuals vulnerable to trafficking recruitment. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#VictimVulnerabilityProfile"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AgingOutVictimProfile(VictimVulnerabilityProfile):
    """Vulnerability profile for youth aging out of foster care system."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#AgingOutVictimProfile"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TraffickerRole(_cac_core.Role):
    """Role of individual involved in sex trafficking operations. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#TraffickerRole"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AssociateTraffickerRole(TraffickerRole):
    """Supporting role in trafficking operation, assisting primary traffickers. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#AssociateTraffickerRole"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TraffickingOperation(_cac_core.ExploitationEvent):
    """Coordinated trafficking activity involving multiple perpetrators, victims, and locations. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#TraffickingOperation"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CommercialSexualExploitation(TraffickingOperation):
    """Forced engagement in commercial sexual activities for the traffickers' profit. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#CommercialSexualExploitation"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimControl(TraffickingOperation):
    """Methods used to maintain psychological and physical control over trafficking victims. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#VictimControl"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CrossJurisdictionalControl(VictimControl):
    """Maintenance of victim control across multiple jurisdictions through coordinated trafficking network. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#CrossJurisdictionalControl"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DisruptionPhase(_cac_core.Phase):
    """Phase when trafficking enterprise faces law enforcement intervention."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#DisruptionPhase"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EarningsCollection(TraffickingOperation):
    """Collection of money earned through victim exploitation by trafficking operation. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#EarningsCollection"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EstablishmentPhase(_cac_core.Phase):
    """Initial phase of trafficking enterprise formation and recruitment setup."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#EstablishmentPhase"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ExpansionPhase(_cac_core.Phase):
    """Phase of trafficking enterprise growth, adding victims and locations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#ExpansionPhase"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FinancialFacilitatorRole(TraffickerRole):
    """Role managing financial aspects including collecting earnings and money laundering. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#FinancialFacilitatorRole"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimTransportation(TraffickingOperation):
    """Transportation of trafficking victims between locations for commercial sexual exploitation. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#VictimTransportation"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InterstateVictimTransport(VictimTransportation):
    """Transportation of trafficking victims across state lines for commercial sexual exploitation. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#InterstateVictimTransport"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MinorTraffickingVictimRole(TraffickingVictimRole):
    """Role of minor (under 18) being sex trafficked. Modeled as anti-rigid gUFO Role. Concrete victim age at specific trafficking operations SHOULD be represented using cacontology-temporal:AgeAtTimeSituati"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#MinorTraffickingVictimRole"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MultiJurisdictionalSituation(_cac_core.Situation):
    """Complex situation involving trafficking operations across multiple jurisdictions requiring coordinated law enforcement response."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#MultiJurisdictionalSituation"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MultiStateTraffickingConspiracy(TraffickingOperation):
    """Criminal conspiracy spanning multiple states for trafficking operations (e.g., Brooklyn-North Carolina network). Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#MultiStateTraffickingConspiracy"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TraffickingVictimRescue(_cac_core.InvestigativeAction):
    """Specialized rescue operation for trafficking victims involving multiple agencies and victim services. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#TraffickingVictimRescue"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OngoingDangerResponse(TraffickingVictimRescue):
    """Response to situations where victims are identified as being in ongoing danger from traffickers. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#OngoingDangerResponse"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OperationalPhase(_cac_core.Phase):
    """Active operational phase of trafficking enterprise with established victim control."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#OperationalPhase"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PrimaryTraffickerRole(TraffickerRole):
    """Leading role in trafficking operation, often controlling multiple victims and coordinating activities. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#PrimaryTraffickerRole"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RecruitmentFacilitatorRole(TraffickerRole):
    """Role focused on recruiting and grooming new victims for trafficking. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#RecruitmentFacilitatorRole"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RunawayVictimProfile(VictimVulnerabilityProfile):
    """Vulnerability profile for runaway or homeless youth targeted by traffickers."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#RunawayVictimProfile"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TraffickingEnterprise(_uco_identity.Organization):
    """Criminal organization engaged in systematic sex trafficking operations with multiple defendants and coordinated activities. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#TraffickingEnterprise"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class TraffickingCell(TraffickingEnterprise):
    """Smaller operational unit within trafficking ring, often controlling specific victims or geographic areas. Modeled as specialized gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#TraffickingCell"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TraffickingHierarchy(_cac_core.EnduringEntity):
    """Organizational structure within trafficking enterprise defining roles and authority levels."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#TraffickingHierarchy"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TraffickingNetworkSituation(_cac_core.Situation):
    """Complex situation encompassing active trafficking network operations across multiple jurisdictions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#TraffickingNetworkSituation"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TraffickingRing(TraffickingEnterprise):
    """Coordinated group of traffickers operating across multiple jurisdictions with shared victims and resources (e.g., 8-defendant Brooklyn case). Modeled as specialized gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#TraffickingRing"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TransportationFacilitatorRole(TraffickerRole):
    """Role focused on transporting victims between locations for trafficking purposes. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#TransportationFacilitatorRole"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimControlSituation(_cac_core.Situation):
    """Ongoing situation of psychological and physical control maintained over trafficking victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#VictimControlSituation"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimEmergencyResponse(TraffickingVictimRescue):
    """Emergency response to 911 calls from trafficking victims seeking help. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#VictimEmergencyResponse"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimRecruitment(TraffickingOperation):
    """Process of identifying, targeting, and acquiring new victims for trafficking operations. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#VictimRecruitment"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimRotation(VictimTransportation):
    """Systematic movement of victims between different locations to avoid detection and maintain control. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#VictimRotation"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimSafetyAssessment(_cac_core.InvestigativeAction):
    """Assessment of victim safety and ongoing threats from trafficking network. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/trafficking#VictimSafetyAssessment"
    NAMESPACE_PREFIX: str = "cacontology-sex-trafficking"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
