"""CAC Ontology - Crimes Against Children — cacontology_production module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional, Union

import case_uco.uco.location as _uco_location
import case_uco.uco.observable as _uco_observable
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["ActiveProductionPhase", "BathroomSurveillance", "BedroomSurveillance", "ConcealmentContainer", "ContentCreation", "ControlledEnvironment", "DeviceConcealment", "DigitalManipulation", "EditedContent", "EditingEquipment", "ExtendedProductionPeriod", "HiddenRecordingDevice", "LiveProductionEvent", "LiveStreamContent", "MobileRecordingDevice", "PhysicalDeviceModification", "PrivateSpaceSurveillance", "ProducedContent", "ProducedImage", "ProducedVideo", "Producer", "ProductionDistributionPhase", "ProductionEquipment", "ProductionFacilitator", "ProductionLocation", "ProductionOffense", "ProductionPreparationPhase", "ProductionSeries", "ProductionSession", "ProductionVictim", "RecordingAction", "RecordingDevice", "ResidentialProductionSite", "StationaryCamera"]


@dataclass
class ActiveProductionPhase(_cac_core.Phase):
    """Phase during which production activities are actively occurring."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ActiveProductionPhase"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    production_activity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-production:productionActivity', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class RecordingAction(_cac_core.ExploitationEvent):
    """Action of recording child sexual abuse for the purpose of creating illegal material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#RecordingAction"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PrivateSpaceSurveillance(RecordingAction):
    """Covert surveillance of private spaces where victims have expectation of privacy."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#PrivateSpaceSurveillance"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class BathroomSurveillance(PrivateSpaceSurveillance):
    """Specific surveillance of bathroom facilities, as observed in Vermont case."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#BathroomSurveillance"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class BedroomSurveillance(PrivateSpaceSurveillance):
    """Specific surveillance of sleeping areas and bedrooms."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#BedroomSurveillance"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ConcealmentContainer(_uco_observable.ObservableObject):
    """Object used to hide recording equipment such as backpacks, furniture, or everyday items with modifications."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ConcealmentContainer"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ContentCreation(_cac_core.ExploitationEvent):
    """Process of creating, editing, or enhancing child sexual abuse material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ContentCreation"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProductionLocation(_uco_location.Location):
    """Physical location where child sexual abuse material production occurred."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProductionLocation"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    access_control: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-production:accessControl', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    location_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-production:locationType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    privacy_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-production:privacyLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ControlledEnvironment(ProductionLocation):
    """Location specifically prepared or modified for production activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ControlledEnvironment"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DeviceConcealment(_cac_core.ExploitationEvent):
    """Specific methods and techniques used to hide recording devices for covert surveillance operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#DeviceConcealment"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DigitalManipulation(ContentCreation):
    """Digital alteration or enhancement of images or videos to create child sexual abuse material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#DigitalManipulation"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProducedContent(_cac_core.Artifact):
    """Child sexual abuse material created through production activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProducedContent"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EditedContent(ProducedContent):
    """Original content that has been digitally modified or enhanced."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#EditedContent"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProductionEquipment(_uco_observable.ObservableObject):
    """Devices and equipment used to produce child sexual abuse material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProductionEquipment"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    equipment_condition: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-production:equipmentCondition', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    equipment_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-production:equipmentType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class EditingEquipment(ProductionEquipment):
    """Computer hardware and software used to edit or enhance produced material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#EditingEquipment"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ExtendedProductionPeriod(_uco_observable.ObservableObject):
    """Ongoing pattern of production over an extended time period."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ExtendedProductionPeriod"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class RecordingDevice(ProductionEquipment):
    """Device capable of capturing video or photographic content."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#RecordingDevice"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    recording_quality: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-production:recordingQuality', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    storage_capacity: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-production:storageCapacity', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class HiddenRecordingDevice(RecordingDevice):
    """Covert recording equipment designed to capture content without victim awareness."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#HiddenRecordingDevice"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LiveProductionEvent(_cac_core.ExploitationEvent):
    """Real-time production of child sexual abuse material involving live victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#LiveProductionEvent"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    streaming_platform: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-production:streamingPlatform', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    viewer_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-production:viewerCount', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class LiveStreamContent(ProducedContent):
    """Content transmitted in real-time during live production events."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#LiveStreamContent"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MobileRecordingDevice(RecordingDevice):
    """Mobile phone, tablet, or portable device used for recording."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#MobileRecordingDevice"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PhysicalDeviceModification(_cac_core.ExploitationEvent):
    """Physical alterations made to recording devices to enable concealment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#PhysicalDeviceModification"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProducedImage(ProducedContent):
    """Still images created through production activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProducedImage"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProducedVideo(ProducedContent):
    """Video content created through production activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProducedVideo"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Producer(_cac_core.Role):
    """Individual who creates, directs, or facilitates the production of child sexual abuse material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#Producer"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    production_experience: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-production:productionExperience', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    technical_skill_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-production:technicalSkillLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ProductionDistributionPhase(_cac_core.Phase):
    """Phase during which produced content is distributed or shared."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProductionDistributionPhase"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProductionFacilitator(_cac_core.Role):
    """Individual who assists in or enables production activities without directly producing content."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProductionFacilitator"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProductionOffense(_cac_core.ExploitationEvent):
    """Criminal offense involving the production, creation, or manufacturing of child sexual abuse material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProductionOffense"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    comment: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:comment', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    duration_minutes: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-production:durationMinutes', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    production_method: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-production:productionMethod', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    session_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-production:sessionCount', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    victim_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-production:victimCount', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    end_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:endTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class ProductionPreparationPhase(_cac_core.Phase):
    """Phase involving preparation and setup for production activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProductionPreparationPhase"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProductionSeries(ExtendedProductionPeriod):
    """Connected series of production sessions targeting the same victim(s)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProductionSeries"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProductionSession(_uco_observable.ObservableObject):
    """Individual instance or session of producing child sexual abuse material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProductionSession"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ProductionVictim(_cac_core.Role):
    """Child victim directly involved in production of sexual abuse material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ProductionVictim"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ResidentialProductionSite(ProductionLocation):
    """Private residence used for production activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#ResidentialProductionSite"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StationaryCamera(RecordingDevice):
    """Fixed camera equipment including webcams, digital cameras, and video cameras."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/production#StationaryCamera"
    NAMESPACE_PREFIX: str = "cacontology-production"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
