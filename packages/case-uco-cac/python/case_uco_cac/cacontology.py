"""CAC Ontology - Crimes Against Children — cacontology module."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AnalysisPhase:
    """Phase focused on detailed analysis of evidence and cybertip information."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#AnalysisPhase"


@dataclass
class AnalystRole:
    """Role of professional analyzing cybertips and digital evidence. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#AnalystRole"
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
class CACInvestigation:
    """A child-protection investigation that follows a standard action lifecycle that commonly begins with the discovery of CSAM, the receipt of a cybertip, or a call to a hotline. This class extends the CAS"""

    CLASS_IRI: str = "https://cacontology.projectvic.org#CACInvestigation"
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
    object: list[UcoObject] = field(default_factory=list)
    focus: list[str] = field(default_factory=list)
    investigation_form: Optional[str] = field(default=None)
    investigation_status: Optional[str] = field(default=None)
    relevant_authorization: list[Authorization] = field(default_factory=list)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)
    current_phase: Optional[Phase] = field(default=None)
    has_role: list[Role] = field(default_factory=list)


@dataclass
class CSAMCurationAction:
    """The action of curating and classifying child sexual abuse material using standard classification systems."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#CSAMCurationAction"
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
class CSAMIncident:
    """Incidents involving possession, manufacture, or distribution of child sexual abuse material. This replaces the deprecated 'ChildPornographyIncident' term."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#CSAMIncident"


@dataclass
class ChildSexualAbuseEvent:
    """A class representing any event involving child sexual abuse or exploitation. This is the base class for all CAC incidents modeled as gUFO Event. Victim and offender ages at the time of the event SHOUL"""

    CLASS_IRI: str = "https://cacontology.projectvic.org#ChildSexualAbuseEvent"


@dataclass
class ConclusionPhase:
    """Final phase involving case closure or prosecution referral."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#ConclusionPhase"


@dataclass
class ConspiracyLeaderRole:
    """Leadership role within criminal conspiracy, directing and coordinating activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#ConspiracyLeaderRole"
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
class ConspiracyMemberRole:
    """Member role within criminal conspiracy, participating in coordinated activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#ConspiracyMemberRole"
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
class ConspiracyRole:
    """Role of individual within criminal conspiracy."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#ConspiracyRole"
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
class ConspiracyToCommitCSA:
    """Criminal conspiracy involving multiple defendants coordinating child sexual abuse or exploitation activities (e.g., 8-defendant Brooklyn trafficking ring)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#ConspiracyToCommitCSA"


@dataclass
class CoordinatedOffensePattern:
    """Pattern of coordinated criminal activities involving multiple perpetrators working together across time and locations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#CoordinatedOffensePattern"
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


@dataclass
class CriminalEnterprise:
    """Organized criminal group conducting systematic child exploitation activities with defined roles and structure."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#CriminalEnterprise"
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
class DigitallyGeneratedCSAMIncident:
    """Incidents involving digitally generated or manipulated child sexual abuse material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#DigitallyGeneratedCSAMIncident"


@dataclass
class EvidencePhase:
    """Phase focused on evidence collection, analysis, and curation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#EvidencePhase"


@dataclass
class EvidenceReviewAction:
    """The action of reviewing and analyzing digital evidence using forensic tools."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#EvidenceReviewAction"
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
class GroomingSolicitation:
    """Incidents involving grooming or solicitation of children for sexual purposes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#GroomingSolicitation"


@dataclass
class InitialPhase:
    """Initial phase of CAC investigation involving cybertip receipt and preliminary review."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#InitialPhase"


@dataclass
class InvestigationLifecycleSituation:
    """Overall situation encompassing the complete CAC investigation lifecycle."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#InvestigationLifecycleSituation"


@dataclass
class InvestigatorRole:
    """Role of law enforcement officer or analyst conducting CAC investigation. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#InvestigatorRole"
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
class LegalProcessAction:
    """The action of initiating legal processes such as search warrants, subpoenas, or MLAT requests."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#LegalProcessAction"
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
class LegalProcessPhase:
    """Phase involving legal processes such as search warrants and subpoenas."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#LegalProcessPhase"


@dataclass
class LiveStreamingCSA:
    """Incidents involving live streaming of child sexual abuse."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#LiveStreamingCSA"


@dataclass
class MultiDefendantIndictment:
    """Legal indictment involving multiple defendants in coordinated criminal enterprise (e.g., 19-count superseding indictment)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#MultiDefendantIndictment"
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
    charging_instrument_counts: Optional[int] = field(default=None)
    filed_date: Optional[TypedLiteral] = field(default=None)


@dataclass
class OffenderRole:
    """Role of a person who commits child sexual abuse or exploitation. Modeled as anti-rigid gUFO Role. When offender age or age-gap reasoning is relevant (e.g., Romeo-and-Juliet scenarios), age SHOULD be r"""

    CLASS_IRI: str = "https://cacontology.projectvic.org#OffenderRole"
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
class ReceiveCybertipAction:
    """The initial action of receiving a cybertip report from a reporting entity (e.g., NCMEC, INHOPE)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#ReceiveCybertipAction"
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
    occurs_in_situation: list[InvestigationPendingSituation] = field(default_factory=list)


@dataclass
class RescuerRole:
    """Role of a person involved in rescuing or protecting victims (e.g., law enforcement, NGO worker). Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#RescuerRole"
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
class ReviewCybertipAction:
    """The action of reviewing and analyzing a cybertip report by an analyst."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#ReviewCybertipAction"
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
class Sextortion:
    """Incidents involving sexual extortion of children."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#Sextortion"


@dataclass
class Subject:
    """Continuity alias for the investigation-subject role. Deprecated in favor of case-investigation:Subject (a uco-role:Role whose conduct is within the scope of an investigation); new graphs should use th"""

    CLASS_IRI: str = "https://cacontology.projectvic.org#Subject"


@dataclass
class UnknownVictimSubmission:
    """The action of submitting information about unidentified victims to relevant databases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#UnknownVictimSubmission"
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
class VictimPhase:
    """Phase focused on victim identification, rescue, and support. Deprecated: consider using the more specific VictimIdentificationPhase, VictimRescuePhase, VictimSupportPhase, or VictimRecoveryPhase class"""

    CLASS_IRI: str = "https://cacontology.projectvic.org#VictimPhase"


@dataclass
class VictimRescueAction:
    """The action of rescuing and providing support to identified victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org#VictimRescueAction"
    creates_situation: list[Situation] = field(default_factory=list)
    performer: list[RescuerRole] = field(default_factory=list)


@dataclass
class VictimRole:
    """Role of a person who is a victim of child sexual abuse or exploitation. Modeled as anti-rigid gUFO Role. When the victim's age is known at the time of a specific event or phase, it SHOULD be captured """

    CLASS_IRI: str = "https://cacontology.projectvic.org#VictimRole"
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

