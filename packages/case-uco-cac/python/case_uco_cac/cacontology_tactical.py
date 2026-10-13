"""CAC Ontology - Crimes Against Children — cacontology_tactical module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional, Union

import case_uco.case.investigation as _case_investigation
import case_uco.uco.core as _uco_core
import case_uco.uco.observable as _uco_observable
import case_uco.uco.role as _uco_role
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["ArrestOperation", "ArrestReport", "BarricadeSituation", "BookingAction", "Breacher", "BreachingTool", "CommunicationEquipment", "CorrectionalFacility", "DynamicEntry", "HighRiskArrest", "ImmigrationHold", "InterviewWithoutCounsel", "LessLethalWeapon", "LocationIntelligence", "Marksman", "Negotiator", "ProtectiveGear", "SWATOperation", "SurrenderNegotiation", "SurveillanceEquipment", "SuspectProfile", "TacticalCommander", "TacticalEquipment", "TacticalOperation", "TacticalTeamMember", "TeamLeader", "ThreatAssessment", "TrafficStop"]


@dataclass
class ArrestOperation(_cac_core.InvestigativeAction):
    """Law enforcement operation to apprehend and take suspect into custody. Extends investigation:InvestigativeAction for proper CASE ontology integration."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#ArrestOperation"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    arrest_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:arrestType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    resistance_expected: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:resistanceExpected', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    target_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:targetCount', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    weapons_expected: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:weaponsExpected', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    start_time_uco_core: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class ArrestReport(_case_investigation.ProvenanceRecord):
    """Formal arrest report documenting the arrest including charges, evidence, and suspect information. Extends investigation:ProvenanceRecord for evidence tracking."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#ArrestReport"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    documents_arrest: Optional[ArrestOperation] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:documentsArrest', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'https://cacontology.projectvic.org/tactical#ArrestOperation', 'alternate_range_iris': []})
    report_date: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:reportDate', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#date', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class BarricadeSituation(_cac_core.Situation):
    """Situation where suspect has barricaded themselves and refuses to surrender. A state/context, not an operation; TacticalOperation may occurInSituation a BarricadeSituation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#BarricadeSituation"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class BookingAction(_cac_core.InvestigativeAction):
    """Process of booking a suspect into a correctional facility including fingerprinting, photography, and data entry. Extends investigation:InvestigativeAction for CASE ontology integration."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#BookingAction"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    booking_date: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:bookingDate', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#date', 'alternate_range_iris': [], 'literal_datatype': True})
    booking_officer: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:bookingOfficer', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    occurs_at_facility: Optional[CorrectionalFacility] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:occursAtFacility', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'https://cacontology.projectvic.org/tactical#CorrectionalFacility', 'alternate_range_iris': []})


@dataclass
class TacticalTeamMember(_uco_role.Role):
    """Law enforcement officer specialized in tactical operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#TacticalTeamMember"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class Breacher(TacticalTeamMember):
    """Specialist responsible for gaining entry through doors, walls, or barriers."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#Breacher"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TacticalEquipment(_uco_observable.ObservableObject):
    """Specialized equipment used in tactical operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#TacticalEquipment"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    certification_required: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:certificationRequired', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    equipment_status: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:equipmentStatus', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    equipment_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:equipmentType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    last_maintenance: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:lastMaintenance', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    maintenance_interval: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:maintenanceInterval', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class BreachingTool(TacticalEquipment):
    """Tool used to gain entry through doors, walls, or barriers."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#BreachingTool"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CommunicationEquipment(TacticalEquipment):
    """Specialized communication devices for tactical operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#CommunicationEquipment"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CorrectionalFacility(_cac_core.PlaceLikeEntity):
    """Physical correctional facility where suspects are booked and held. Examples include county jails and correctional centers. Extends uco-core:UcoObject as physical location (NOT digital observable)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#CorrectionalFacility"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    correctional_facility_name: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:correctionalFacilityName', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class TacticalOperation(_cac_core.InvestigativeAction):
    """Specialized law enforcement operation requiring tactical teams and advanced planning."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#TacticalOperation"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    comment: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:comment', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    operation_scope: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:operationScope', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    operation_status: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:operationStatus', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    operation_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:operationType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    personnel_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:personnelCount', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    planning_duration: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:planningDuration', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    risk_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:riskLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    end_time_uco_core: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:endTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    start_time_uco_core: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class DynamicEntry(TacticalOperation):
    """Rapid forced entry into a location to apprehend suspects and secure evidence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#DynamicEntry"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HighRiskArrest(TacticalOperation):
    """Arrest operation involving suspects who pose significant threat or flight risk."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#HighRiskArrest"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ImmigrationHold(_cac_core.Artifact):
    """Immigration detainer placed on suspect due to immigration status. Links booking to immigration enforcement coordination."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#ImmigrationHold"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    immigration_hold_reason: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:immigrationHoldReason', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    immigration_status: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:immigrationStatus', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class InterviewWithoutCounsel(_cac_core.InvestigativeAction):
    """Suspect interview conducted after suspect waives right to legal counsel. Extends investigation:InvestigativeAction."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#InterviewWithoutCounsel"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LessLethalWeapon(TacticalEquipment):
    """Non-lethal weapons for suspect control and compliance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#LessLethalWeapon"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LocationIntelligence(_uco_core.UcoObject):
    """Information about the physical location of tactical operation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#LocationIntelligence"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class Marksman(TacticalTeamMember):
    """Precision shooter providing overwatch and threat elimination capability."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#Marksman"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Negotiator(_uco_role.Role):
    """Specialist trained in crisis negotiation and de-escalation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#Negotiator"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ProtectiveGear(TacticalEquipment):
    """Armor and protective equipment for tactical team members."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#ProtectiveGear"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    gear_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:gearType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    protection_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:protectionLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    threat_protection: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-tactical:threatProtection', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SWATOperation(TacticalOperation):
    """Special Weapons and Tactics team operation for high-risk situations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#SWATOperation"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SurrenderNegotiation(TacticalOperation):
    """Attempt to negotiate peaceful surrender of barricaded or resistant suspects."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#SurrenderNegotiation"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SurveillanceEquipment(TacticalEquipment):
    """Equipment for monitoring and observing tactical situations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#SurveillanceEquipment"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SuspectProfile(_uco_core.UcoObject):
    """Assessment of suspect behavior, capabilities, and threat level."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#SuspectProfile"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class TacticalCommander(_uco_role.Role):
    """Senior officer responsible for overall tactical operation command."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#TacticalCommander"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class TeamLeader(TacticalTeamMember):
    """Officer responsible for commanding tactical team operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#TeamLeader"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ThreatAssessment(_uco_core.UcoObject):
    """Evaluation of potential threats and risks in tactical situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#ThreatAssessment"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class TrafficStop(_cac_core.InvestigativeAction):
    """Investigative traffic stop used as part of undercover operation or to apprehend suspect. Extends investigation:InvestigativeAction."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/tactical#TrafficStop"
    NAMESPACE_PREFIX: str = "cacontology-tactical"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
