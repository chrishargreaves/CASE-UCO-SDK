"""CAC Ontology - Crimes Against Children — cac_core module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar, Optional

import case_uco.case.investigation as _case_investigation
import case_uco.uco.core as _uco_core
import case_uco.uco.observable as _uco_observable
import case_uco.uco.role as _uco_role
from case_uco_cac._context import NAMESPACES

__all__ = ["Artifact", "AssessmentResult", "ConditioningPhase", "CoordinationEvent", "DetectionEvent", "DigitalSystemEntity", "EnduringEntity", "Entity", "Event", "ExploitationEvent", "InvestigativeAction", "LegalEvent", "Occurrent", "OrganizationLikeEntity", "PersonLikeEntity", "Phase", "PlaceLikeEntity", "Role", "Situation", "SupportEvent"]


@dataclass
class Artifact(_uco_observable.ObservableObject):
    """An enduring entity that is inspectable, storable, transferable, or evidentiary. Aligned to UCO ObservableObject for digital evidence interoperability."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#Artifact"
    NAMESPACE_PREFIX: str = "cac-core"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class EnduringEntity(_uco_core.UcoObject):
    """A thing that persists through time while potentially changing state. This is the CAC-facing root for all object-like entities including people, organizations, devices, artifacts, places, and assessmen"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#EnduringEntity"
    NAMESPACE_PREFIX: str = "cac-core"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class AssessmentResult(EnduringEntity):
    """An output or conclusion of some evaluative, analytic, classification, or decision-making process. Intentionally not subclassed from uco-observable:ObservableObject because the semantic identity of a r"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#AssessmentResult"
    NAMESPACE_PREFIX: str = "cac-core"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Entity:
    """The most general class in the CAC semantic spine. All CAC domain concepts should anchor to one of its subclasses."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#Entity"
    NAMESPACE_PREFIX: str = "cac-core"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class Phase(Entity):
    """A temporal stage of some enduring entity, process, or situation. The bearer remains the same entity while changing phase. Aligned to gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#Phase"
    NAMESPACE_PREFIX: str = "cac-core"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ConditioningPhase(Phase):
    """Temporal phase in which an offender shapes victim readiness, situational constraints, or compliance preparatory to the primary exploitation act — through rapport, deception, isolation, normalization, """

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#ConditioningPhase"
    NAMESPACE_PREFIX: str = "cac-core"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Occurrent(Entity):
    """A CAC organizing superclass for things that happen or unfold in time. This is a CAC-layer abstraction not directly mapped to a gUFO superclass in the base spine."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#Occurrent"
    NAMESPACE_PREFIX: str = "cac-core"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Event(Occurrent):
    """Something that happens or unfolds in time — an action, interaction, incident, hearing, or process step."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#Event"
    NAMESPACE_PREFIX: str = "cac-core"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CoordinationEvent(Event):
    """An event representing coordination, information sharing, or collaborative activity among stakeholders."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#CoordinationEvent"
    NAMESPACE_PREFIX: str = "cac-core"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DetectionEvent(Event):
    """An event representing the detection, identification, or flagging of content, behavior, or indicators relevant to child exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#DetectionEvent"
    NAMESPACE_PREFIX: str = "cac-core"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DigitalSystemEntity(EnduringEntity):
    """An enduring entity representing a software or system-level resource such as an online service platform, moderation system, or digital environment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#DigitalSystemEntity"
    NAMESPACE_PREFIX: str = "cac-core"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ExploitationEvent(Event):
    """An event representing an act of exploitation, abuse, or victimization of a child."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#ExploitationEvent"
    NAMESPACE_PREFIX: str = "cac-core"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InvestigativeAction(_case_investigation.InvestigativeAction):
    """An event that is specifically an investigative action within a CAC investigation. Aligned to both CASE InvestigativeAction and UCO Action for investigation interoperability."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#InvestigativeAction"
    NAMESPACE_PREFIX: str = "cac-core"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class LegalEvent(Event):
    """An event representing a legal proceeding, judicial action, sentencing hearing, or other court-related occurrence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#LegalEvent"
    NAMESPACE_PREFIX: str = "cac-core"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OrganizationLikeEntity(EnduringEntity):
    """An enduring entity that represents an organization, institution, team, agency, or other collectively organized actor."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#OrganizationLikeEntity"
    NAMESPACE_PREFIX: str = "cac-core"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PersonLikeEntity(EnduringEntity):
    """An enduring entity that is person-like in the domain model. Use for natural persons and person-profile abstractions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#PersonLikeEntity"
    NAMESPACE_PREFIX: str = "cac-core"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PlaceLikeEntity(EnduringEntity):
    """An enduring entity used to represent places, venues, virtual environments treated as locatable contexts, or place-like reference points."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#PlaceLikeEntity"
    NAMESPACE_PREFIX: str = "cac-core"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Role(_uco_role.Role):
    """A non-rigid role borne by an enduring entity in a certain relational or contextual setting. A bearer can gain or lose a role without ceasing to exist. Aligned to both gUFO Role and UCO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#Role"
    NAMESPACE_PREFIX: str = "cac-core"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class Situation(Entity):
    """A context, state, or configuration that holds at a time and may involve multiple participants. Aligned to gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#Situation"
    NAMESPACE_PREFIX: str = "cac-core"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SupportEvent(Event):
    """An event representing victim support, advocacy, training, or welfare-related activity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/core#SupportEvent"
    NAMESPACE_PREFIX: str = "cac-core"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
