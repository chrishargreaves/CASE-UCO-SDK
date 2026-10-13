"""CAC Ontology - Crimes Against Children — cacontology-production module."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class ActiveProductionPhase:
    """Phase during which production activities are actively occurring."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ActiveProductionPhase"
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    duration_minutes: Optional[float] = field(default=None)
    production_method: Optional[str] = field(default=None)
    session_count: Optional[int] = field(default=None)
    victim_count: Optional[int] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)
    production_activity: Optional[str] = field(default=None)


@dataclass
class BathroomSurveillance:
    """Specific surveillance of bathroom facilities, as observed in Vermont case."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#BathroomSurveillance"


@dataclass
class BedroomSurveillance:
    """Specific surveillance of sleeping areas and bedrooms."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#BedroomSurveillance"


@dataclass
class ConcealmentContainer:
    """Object used to hide recording equipment such as backpacks, furniture, or everyday items with modifications."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ConcealmentContainer"
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
class ContentCreation:
    """Process of creating, editing, or enhancing child sexual abuse material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ContentCreation"


@dataclass
class ControlledEnvironment:
    """Location specifically prepared or modified for production activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ControlledEnvironment"
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
    access_control: Optional[str] = field(default=None)
    location_type: Optional[str] = field(default=None)
    privacy_level: Optional[str] = field(default=None)


@dataclass
class DeviceConcealment:
    """Specific methods and techniques used to hide recording devices for covert surveillance operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#DeviceConcealment"


@dataclass
class DigitalManipulation:
    """Digital alteration or enhancement of images or videos to create child sexual abuse material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#DigitalManipulation"


@dataclass
class EditedContent:
    """Original content that has been digitally modified or enhanced."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#EditedContent"
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
class EditingEquipment:
    """Computer hardware and software used to edit or enhance produced material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#EditingEquipment"
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
    equipment_condition: Optional[str] = field(default=None)
    equipment_type: Optional[str] = field(default=None)


@dataclass
class ExtendedProductionPeriod:
    """Ongoing pattern of production over an extended time period."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ExtendedProductionPeriod"
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
class HiddenRecordingDevice:
    """Covert recording equipment designed to capture content without victim awareness."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#HiddenRecordingDevice"
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
    equipment_condition: Optional[str] = field(default=None)
    equipment_type: Optional[str] = field(default=None)
    recording_quality: Optional[str] = field(default=None)
    storage_capacity: Optional[float] = field(default=None)


@dataclass
class LiveProductionEvent:
    """Real-time production of child sexual abuse material involving live victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#LiveProductionEvent"
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    duration_minutes: Optional[float] = field(default=None)
    production_method: Optional[str] = field(default=None)
    session_count: Optional[int] = field(default=None)
    victim_count: Optional[int] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)
    streaming_platform: Optional[str] = field(default=None)
    viewer_count: Optional[int] = field(default=None)


@dataclass
class LiveStreamContent:
    """Content transmitted in real-time during live production events."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#LiveStreamContent"
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
class MobileRecordingDevice:
    """Mobile phone, tablet, or portable device used for recording."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#MobileRecordingDevice"
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
    equipment_condition: Optional[str] = field(default=None)
    equipment_type: Optional[str] = field(default=None)
    recording_quality: Optional[str] = field(default=None)
    storage_capacity: Optional[float] = field(default=None)


@dataclass
class PhysicalDeviceModification:
    """Physical alterations made to recording devices to enable concealment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#PhysicalDeviceModification"


@dataclass
class PrivateSpaceSurveillance:
    """Covert surveillance of private spaces where victims have expectation of privacy."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#PrivateSpaceSurveillance"


@dataclass
class ProducedContent:
    """Child sexual abuse material created through production activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProducedContent"
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
class ProducedImage:
    """Still images created through production activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProducedImage"
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
class ProducedVideo:
    """Video content created through production activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProducedVideo"
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
class Producer:
    """Individual who creates, directs, or facilitates the production of child sexual abuse material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#Producer"
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
    production_experience: Optional[float] = field(default=None)
    technical_skill_level: Optional[str] = field(default=None)


@dataclass
class ProductionDistributionPhase:
    """Phase during which produced content is distributed or shared."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProductionDistributionPhase"
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    duration_minutes: Optional[float] = field(default=None)
    production_method: Optional[str] = field(default=None)
    session_count: Optional[int] = field(default=None)
    victim_count: Optional[int] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class ProductionEquipment:
    """Devices and equipment used to produce child sexual abuse material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProductionEquipment"
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
    equipment_condition: Optional[str] = field(default=None)
    equipment_type: Optional[str] = field(default=None)


@dataclass
class ProductionFacilitator:
    """Individual who assists in or enables production activities without directly producing content."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProductionFacilitator"
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
class ProductionLocation:
    """Physical location where child sexual abuse material production occurred."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProductionLocation"
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
    access_control: Optional[str] = field(default=None)
    location_type: Optional[str] = field(default=None)
    privacy_level: Optional[str] = field(default=None)


@dataclass
class ProductionOffense:
    """Criminal offense involving the production, creation, or manufacturing of child sexual abuse material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProductionOffense"
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    duration_minutes: Optional[float] = field(default=None)
    production_method: Optional[str] = field(default=None)
    session_count: Optional[int] = field(default=None)
    victim_count: Optional[int] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class ProductionPreparationPhase:
    """Phase involving preparation and setup for production activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProductionPreparationPhase"
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    duration_minutes: Optional[float] = field(default=None)
    production_method: Optional[str] = field(default=None)
    session_count: Optional[int] = field(default=None)
    victim_count: Optional[int] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class ProductionSeries:
    """Connected series of production sessions targeting the same victim(s)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProductionSeries"
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
class ProductionSession:
    """Individual instance or session of producing child sexual abuse material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProductionSession"
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
class ProductionVictim:
    """Child victim directly involved in production of sexual abuse material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProductionVictim"
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
class RecordingAction:
    """Action of recording child sexual abuse for the purpose of creating illegal material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#RecordingAction"


@dataclass
class RecordingDevice:
    """Device capable of capturing video or photographic content."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#RecordingDevice"
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
    equipment_condition: Optional[str] = field(default=None)
    equipment_type: Optional[str] = field(default=None)
    recording_quality: Optional[str] = field(default=None)
    storage_capacity: Optional[float] = field(default=None)


@dataclass
class ResidentialProductionSite:
    """Private residence used for production activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ResidentialProductionSite"
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
    access_control: Optional[str] = field(default=None)
    location_type: Optional[str] = field(default=None)
    privacy_level: Optional[str] = field(default=None)


@dataclass
class StationaryCamera:
    """Fixed camera equipment including webcams, digital cameras, and video cameras."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#StationaryCamera"
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
    equipment_condition: Optional[str] = field(default=None)
    equipment_type: Optional[str] = field(default=None)
    recording_quality: Optional[str] = field(default=None)
    storage_capacity: Optional[float] = field(default=None)

