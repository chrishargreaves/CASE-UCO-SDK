"""CAC Ontology - Crimes Against Children — cac-core module."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Artifact:
    """An enduring entity that is inspectable, storable, transferable, or evidentiary. Aligned to UCO ObservableObject for digital evidence interoperability."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#Artifact"
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
class AssessmentResult:
    """An output or conclusion of some evaluative, analytic, classification, or decision-making process. Intentionally not subclassed from uco-observable:ObservableObject because the semantic identity of a r"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#AssessmentResult"
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
class ConditioningPhase:
    """Temporal phase in which an offender shapes victim readiness, situational constraints, or compliance preparatory to the primary exploitation act — through rapport, deception, isolation, normalization, """

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#ConditioningPhase"


@dataclass
class CoordinationEvent:
    """An event representing coordination, information sharing, or collaborative activity among stakeholders."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#CoordinationEvent"


@dataclass
class DetectionEvent:
    """An event representing the detection, identification, or flagging of content, behavior, or indicators relevant to child exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#DetectionEvent"


@dataclass
class DigitalSystemEntity:
    """An enduring entity representing a software or system-level resource such as an online service platform, moderation system, or digital environment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#DigitalSystemEntity"
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
class EnduringEntity:
    """A thing that persists through time while potentially changing state. This is the CAC-facing root for all object-like entities including people, organizations, devices, artifacts, places, and assessmen"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#EnduringEntity"
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
class Entity:
    """The most general class in the CAC semantic spine. All CAC domain concepts should anchor to one of its subclasses."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#Entity"


@dataclass
class Event:
    """Something that happens or unfolds in time — an action, interaction, incident, hearing, or process step."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#Event"


@dataclass
class ExploitationEvent:
    """An event representing an act of exploitation, abuse, or victimization of a child."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#ExploitationEvent"


@dataclass
class InvestigativeAction:
    """An event that is specifically an investigative action within a CAC investigation. Aligned to both CASE InvestigativeAction and UCO Action for investigation interoperability."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#InvestigativeAction"
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
class LegalEvent:
    """An event representing a legal proceeding, judicial action, sentencing hearing, or other court-related occurrence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#LegalEvent"


@dataclass
class Occurrent:
    """A CAC organizing superclass for things that happen or unfold in time. This is a CAC-layer abstraction not directly mapped to a gUFO superclass in the base spine."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#Occurrent"


@dataclass
class OrganizationLikeEntity:
    """An enduring entity that represents an organization, institution, team, agency, or other collectively organized actor."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#OrganizationLikeEntity"
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
class PersonLikeEntity:
    """An enduring entity that is person-like in the domain model. Use for natural persons and person-profile abstractions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#PersonLikeEntity"
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
class Phase:
    """A temporal stage of some enduring entity, process, or situation. The bearer remains the same entity while changing phase. Aligned to gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#Phase"


@dataclass
class PlaceLikeEntity:
    """An enduring entity used to represent places, venues, virtual environments treated as locatable contexts, or place-like reference points."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#PlaceLikeEntity"
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
class Role:
    """A non-rigid role borne by an enduring entity in a certain relational or contextual setting. A bearer can gain or lose a role without ceasing to exist. Aligned to both gUFO Role and UCO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#Role"
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
class Situation:
    """A context, state, or configuration that holds at a time and may involve multiple participants. Aligned to gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#Situation"


@dataclass
class SupportEvent:
    """An event representing victim support, advocacy, training, or welfare-related activity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#SupportEvent"

