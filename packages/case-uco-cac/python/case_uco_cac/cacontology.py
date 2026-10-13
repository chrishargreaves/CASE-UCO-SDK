"""CAC Ontology - Crimes Against Children — cacontology module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar, Optional

import case_uco.case.investigation as _case_investigation
import case_uco.uco.action as _uco_action
import case_uco.uco.identity as _uco_identity
import case_uco.uco.observable as _uco_observable
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AnalysisPhase", "AnalystRole", "CACInvestigation", "CSAMCurationAction", "CSAMIncident", "ChildSexualAbuseEvent", "ConclusionPhase", "ConspiracyLeaderRole", "ConspiracyMemberRole", "ConspiracyRole", "ConspiracyToCommitCSA", "CoordinatedOffensePattern", "CriminalEnterprise", "DigitallyGeneratedCSAMIncident", "EvidencePhase", "EvidenceReviewAction", "GroomingSolicitation", "InitialPhase", "InvestigationLifecycleSituation", "InvestigatorRole", "LegalProcessAction", "LegalProcessPhase", "LiveStreamingCSA", "MultiDefendantIndictment", "OffenderRole", "ReceiveCybertipAction", "RescuerRole", "ReviewCybertipAction", "Sextortion", "Subject", "UnknownVictimSubmission", "VictimPhase", "VictimRescueAction", "VictimRole"]


@dataclass
class AnalysisPhase(_cac_core.Phase):
    """Phase focused on detailed analysis of evidence and cybertip information."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#AnalysisPhase"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AnalystRole(_cac_core.Role):
    """Role of professional analyzing cybertips and digital evidence. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#AnalystRole"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CACInvestigation(_case_investigation.Investigation):
    """A child-protection investigation that follows a standard action lifecycle that commonly begins with the discovery of CSAM, the receipt of a cybertip, or a call to a hotline. This class extends the CAS"""

    CLASS_IRI: str = "https://cacontology.projectvic.org#CACInvestigation"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    current_phase: Optional[Phase] = field(default=None, metadata={'jsonld_key': 'cacontology:currentPhase', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'https://cacontology.projectvic.org/core#Phase', 'alternate_range_iris': []})
    has_role: list[Role] = field(default_factory=list, metadata={'jsonld_key': 'cacontology:hasRole', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'https://cacontology.projectvic.org/core#Role', 'alternate_range_iris': []})


@dataclass
class CSAMCurationAction(_cac_core.InvestigativeAction):
    """The action of curating and classifying child sexual abuse material using standard classification systems."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#CSAMCurationAction"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ChildSexualAbuseEvent(_cac_core.ExploitationEvent):
    """A class representing any event involving child sexual abuse or exploitation. This is the base class for all CAC incidents modeled as gUFO Event. Victim and offender ages at the time of the event SHOUL"""

    CLASS_IRI: str = "https://cacontology.projectvic.org#ChildSexualAbuseEvent"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CSAMIncident(ChildSexualAbuseEvent):
    """Incidents involving possession, manufacture, or distribution of child sexual abuse material. This replaces the deprecated 'ChildPornographyIncident' term."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#CSAMIncident"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ConclusionPhase(_cac_core.Phase):
    """Final phase involving case closure or prosecution referral."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#ConclusionPhase"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ConspiracyRole(_cac_core.Role):
    """Role of individual within criminal conspiracy."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#ConspiracyRole"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ConspiracyLeaderRole(ConspiracyRole):
    """Leadership role within criminal conspiracy, directing and coordinating activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#ConspiracyLeaderRole"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ConspiracyMemberRole(ConspiracyRole):
    """Member role within criminal conspiracy, participating in coordinated activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#ConspiracyMemberRole"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ConspiracyToCommitCSA(ChildSexualAbuseEvent):
    """Criminal conspiracy involving multiple defendants coordinating child sexual abuse or exploitation activities (e.g., 8-defendant Brooklyn trafficking ring)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#ConspiracyToCommitCSA"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CoordinatedOffensePattern(_uco_action.Action):
    """Pattern of coordinated criminal activities involving multiple perpetrators working together across time and locations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#CoordinatedOffensePattern"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CriminalEnterprise(_uco_identity.Organization):
    """Organized criminal group conducting systematic child exploitation activities with defined roles and structure."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#CriminalEnterprise"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class DigitallyGeneratedCSAMIncident(CSAMIncident):
    """Incidents involving digitally generated or manipulated child sexual abuse material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#DigitallyGeneratedCSAMIncident"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EvidencePhase(_cac_core.Phase):
    """Phase focused on evidence collection, analysis, and curation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#EvidencePhase"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EvidenceReviewAction(_cac_core.InvestigativeAction):
    """The action of reviewing and analyzing digital evidence using forensic tools."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#EvidenceReviewAction"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class GroomingSolicitation(ChildSexualAbuseEvent):
    """Incidents involving grooming or solicitation of children for sexual purposes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#GroomingSolicitation"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InitialPhase(_cac_core.Phase):
    """Initial phase of CAC investigation involving cybertip receipt and preliminary review."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#InitialPhase"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InvestigationLifecycleSituation(_cac_core.Situation):
    """Overall situation encompassing the complete CAC investigation lifecycle."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#InvestigationLifecycleSituation"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InvestigatorRole(_cac_core.Role):
    """Role of law enforcement officer or analyst conducting CAC investigation. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#InvestigatorRole"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegalProcessAction(_cac_core.InvestigativeAction):
    """The action of initiating legal processes such as search warrants, subpoenas, or MLAT requests."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#LegalProcessAction"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegalProcessPhase(_cac_core.Phase):
    """Phase involving legal processes such as search warrants and subpoenas."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#LegalProcessPhase"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LiveStreamingCSA(ChildSexualAbuseEvent):
    """Incidents involving live streaming of child sexual abuse."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#LiveStreamingCSA"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MultiDefendantIndictment(_uco_observable.ObservableObject):
    """Legal indictment involving multiple defendants in coordinated criminal enterprise (e.g., 19-count superseding indictment)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#MultiDefendantIndictment"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class OffenderRole(_cac_core.Role):
    """Role of a person who commits child sexual abuse or exploitation. Modeled as anti-rigid gUFO Role. When offender age or age-gap reasoning is relevant (e.g., Romeo-and-Juliet scenarios), age SHOULD be r"""

    CLASS_IRI: str = "https://cacontology.projectvic.org#OffenderRole"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ReceiveCybertipAction(_cac_core.InvestigativeAction):
    """The initial action of receiving a cybertip report from a reporting entity (e.g., NCMEC, INHOPE)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#ReceiveCybertipAction"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    occurs_in_situation: list[InvestigationPendingSituation] = field(default_factory=list, metadata={'jsonld_key': 'cacontology:occursInSituation', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'https://cacontology.projectvic.org#InvestigationPendingSituation', 'alternate_range_iris': []})


@dataclass
class RescuerRole(_cac_core.Role):
    """Role of a person involved in rescuing or protecting victims (e.g., law enforcement, NGO worker). Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#RescuerRole"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ReviewCybertipAction(_cac_core.InvestigativeAction):
    """The action of reviewing and analyzing a cybertip report by an analyst."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#ReviewCybertipAction"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Sextortion(ChildSexualAbuseEvent):
    """Incidents involving sexual extortion of children."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#Sextortion"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Subject:
    """Continuity alias for the investigation-subject role. Deprecated in favor of case-investigation:Subject (a uco-role:Role whose conduct is within the scope of an investigation); new graphs should use th"""

    CLASS_IRI: str = "https://cacontology.projectvic.org#Subject"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class UnknownVictimSubmission(_cac_core.InvestigativeAction):
    """The action of submitting information about unidentified victims to relevant databases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#UnknownVictimSubmission"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimPhase(_cac_core.Phase):
    """Phase focused on victim identification, rescue, and support. Deprecated: consider using the more specific VictimIdentificationPhase, VictimRescuePhase, VictimSupportPhase, or VictimRecoveryPhase class"""

    CLASS_IRI: str = "https://cacontology.projectvic.org#VictimPhase"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimRescueAction(_cac_core.SupportEvent):
    """The action of rescuing and providing support to identified victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#VictimRescueAction"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    creates_situation: list[Situation] = field(default_factory=list, metadata={'jsonld_key': 'cacontology:createsSituation', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'https://cacontology.projectvic.org/core#Situation', 'alternate_range_iris': []})
    performer: list[RescuerRole] = field(default_factory=list, metadata={'jsonld_key': 'uco-action:performer', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org#RescuerRole', 'alternate_range_iris': []})


@dataclass
class VictimRole(_cac_core.Role):
    """Role of a person who is a victim of child sexual abuse or exploitation. Modeled as anti-rigid gUFO Role. When the victim's age is known at the time of a specific event or phase, it SHOULD be captured """

    CLASS_IRI: str = "https://cacontology.projectvic.org#VictimRole"
    NAMESPACE_PREFIX: str = "cacontology"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
