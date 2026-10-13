"""CAC Ontology - Crimes Against Children — cacontology-specialized-units module."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AnalystRole:
    """Role of analyst supporting specialized unit operations. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#AnalystRole"
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
class CollegeParkBarrack:
    """Maryland State Police College Park Barrack supporting computer crimes investigations. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#CollegeParkBarrack"
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
class CommunityEngagementK9:
    """K9 utilized for community outreach and educational programs. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#CommunityEngagementK9"
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
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)


@dataclass
class CoordinatedArrest:
    """Arrest coordinated as part of larger operation. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#CoordinatedArrest"
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
class CountyPoliceSupport:
    """County-level police department providing support to state computer crimes investigations. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#CountyPoliceSupport"
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
class CriticalIncidentDebriefing:
    """Structured debriefing process following traumatic incidents. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#CriticalIncidentDebriefing"


@dataclass
class CyberCrimeUnit:
    """Unit specialized in cyber crime investigations. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#CyberCrimeUnit"
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
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    operational_capacity: Optional[int] = field(default=None)


@dataclass
class DetectionDog:
    """Trained dog used for detection operations in CAC investigations. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#DetectionDog"
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
    has_capability: list[TripleThreatCapability] = field(default_factory=list)


@dataclass
class DeviceDetection:
    """Detection of electronic storage devices during search operations. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#DeviceDetection"
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
class DigitalForensicsUnit:
    """Unit specialized in digital forensics analysis. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#DigitalForensicsUnit"
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
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    operational_capacity: Optional[int] = field(default=None)


@dataclass
class ElectronicStorageDeviceK9:
    """K9 trained to detect electronic storage devices during search operations. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#ElectronicStorageDeviceK9"
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
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)


@dataclass
class InteragencyOperationSituation:
    """Situation involving operations across multiple agencies and jurisdictions. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#InteragencyOperationSituation"


@dataclass
class K9DetectionProgram:
    """Program utilizing trained detection dogs for CAC investigations. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#K9DetectionProgram"
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
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)


@dataclass
class K9Officer:
    """Law enforcement officer handling and working with detection dogs. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#K9Officer"
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
class K9SearchOperation:
    """Search operation utilizing K9 detection capabilities. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#K9SearchOperation"
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
    search_warrants_executed: Optional[int] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class K9TrainingProgram:
    """Training program for K9 units and handlers. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#K9TrainingProgram"
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
class MarylandStatePoliceComputerCrimesUnit:
    """Maryland State Police unit coordinating the Maryland Internet Crimes Against Children Task Force. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#MarylandStatePoliceComputerCrimesUnit"
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
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    operational_capacity: Optional[int] = field(default=None)


@dataclass
class MentalHealthSupport:
    """Mental health services and support for officers dealing with traumatic content. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#MentalHealthSupport"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: Optional[str] = field(default=None)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)


@dataclass
class MultiJurisdictionalOperation:
    """Operation involving multiple jurisdictions and agencies. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#MultiJurisdictionalOperation"
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
    arrest_count: Optional[int] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class MultiUnitCoordinationSituation:
    """Complex situation involving coordination between multiple specialized units. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#MultiUnitCoordinationSituation"


@dataclass
class NamedOperation:
    """Formally named multi-phase operation with specific objectives. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#NamedOperation"
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
    arrest_count: Optional[int] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class OfficerWellnessProgram:
    """Program providing mental health and wellness support to CAC officers. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#OfficerWellnessProgram"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: Optional[str] = field(default=None)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)


@dataclass
class OperationEvaluationPhase:
    """Phase of post-operation analysis and evaluation. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#OperationEvaluationPhase"


@dataclass
class OperationExecutionPhase:
    """Phase of active operation execution. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#OperationExecutionPhase"


@dataclass
class OperationMetrics:
    """Metrics and performance data for specialized operations. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#OperationMetrics"
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
class OperationPlanningPhase:
    """Phase of operation planning and preparation. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#OperationPlanningPhase"


@dataclass
class OperationSafeOnlineSummer:
    """National operation across 61 CAC Task Forces during summer months. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#OperationSafeOnlineSummer"
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
    arrest_count: Optional[int] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class OperationUnhinged:
    """Specific operation conducted by Idaho CAC resulting in 12 arrests. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#OperationUnhinged"
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
    arrest_count: Optional[int] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class PeerSupport:
    """Peer-to-peer support programs for CAC personnel. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#PeerSupport"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: Optional[str] = field(default=None)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)


@dataclass
class PrinceGeorgesCountyPolice:
    """Prince George's County Police Department supporting Maryland State Police computer crimes investigations. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#PrinceGeorgesCountyPolice"
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
class SpecializedCapabilitySituation:
    """Situation requiring deployment of specialized unit capabilities. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#SpecializedCapabilitySituation"


@dataclass
class SpecializedInvestigativeUnit:
    """Specialized unit with unique capabilities for CAC investigations. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#SpecializedInvestigativeUnit"
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
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    operational_capacity: Optional[int] = field(default=None)


@dataclass
class SpecializedOperatorRole:
    """Role of specialized operator within unit. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#SpecializedOperatorRole"
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
class StatePoliceBarrack:
    """Regional state police barrack providing local law enforcement support and coordination. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#StatePoliceBarrack"
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
class StatePoliceComputerCrimesUnit:
    """State police unit specialized in computer crimes and digital investigations involving child exploitation. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#StatePoliceComputerCrimesUnit"
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
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    operational_capacity: Optional[int] = field(default=None)


@dataclass
class StressManagement:
    """Programs and techniques for managing work-related stress. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#StressManagement"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: Optional[str] = field(default=None)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)


@dataclass
class TacticalUnit:
    """Unit handling high-risk tactical operations. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#TacticalUnit"
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
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    operational_capacity: Optional[int] = field(default=None)


@dataclass
class TechnicalSpecialistRole:
    """Role of technical specialist providing specialized capabilities. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#TechnicalSpecialistRole"
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
class TherapyDog:
    """Trained therapy dog providing emotional support to officers. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#TherapyDog"
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
    provides_wellness_support: list[Person] = field(default_factory=list)


@dataclass
class UndercoverUnit:
    """Unit conducting undercover operations. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#UndercoverUnit"
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
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    operational_capacity: Optional[int] = field(default=None)


@dataclass
class UnitCommanderRole:
    """Role of commanding officer for specialized unit. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#UnitCommanderRole"
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
class UnitDeploymentPhase:
    """Phase when specialized unit is deployed for operations. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#UnitDeploymentPhase"


@dataclass
class UnitMaintenancePhase:
    """Phase for equipment maintenance and unit readiness. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#UnitMaintenancePhase"


@dataclass
class UnitTrainingPhase:
    """Phase focused on specialized unit training and preparation. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#UnitTrainingPhase"


@dataclass
class VictimServicesUnit:
    """Unit providing specialized victim services and support. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#VictimServicesUnit"
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
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    operational_capacity: Optional[int] = field(default=None)


@dataclass
class WellnessCheck:
    """Regular check on officer mental health and wellbeing. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#WellnessCheck"
    performer: Optional[Person] = field(default=None)
    start_time: Optional[datetime] = field(default=None)

