"""CAC Ontology - Crimes Against Children — cacontology_specialized_units module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional, Union

import case_uco.uco.identity as _uco_identity
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AnalystRole", "CollegeParkBarrack", "CommunityEngagementK9", "CoordinatedArrest", "CountyPoliceSupport", "CriticalIncidentDebriefing", "CyberCrimeUnit", "DetectionDog", "DeviceDetection", "DigitalForensicsUnit", "ElectronicStorageDeviceK9", "InteragencyOperationSituation", "K9DetectionProgram", "K9Officer", "K9SearchOperation", "K9TrainingProgram", "MarylandStatePoliceComputerCrimesUnit", "MentalHealthSupport", "MultiJurisdictionalOperation", "MultiUnitCoordinationSituation", "NamedOperation", "OfficerWellnessProgram", "OperationEvaluationPhase", "OperationExecutionPhase", "OperationMetrics", "OperationPlanningPhase", "OperationSafeOnlineSummer", "OperationUnhinged", "PeerSupport", "PrinceGeorgesCountyPolice", "SpecializedCapabilitySituation", "SpecializedInvestigativeUnit", "SpecializedOperatorRole", "StatePoliceBarrack", "StatePoliceComputerCrimesUnit", "StressManagement", "TacticalUnit", "TechnicalSpecialistRole", "TherapyDog", "UndercoverUnit", "UnitCommanderRole", "UnitDeploymentPhase", "UnitMaintenancePhase", "UnitTrainingPhase", "VictimServicesUnit", "WellnessCheck"]


@dataclass
class AnalystRole(_cac_core.Role):
    """Role of analyst supporting specialized unit operations. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#AnalystRole"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StatePoliceBarrack(_uco_identity.Organization):
    """Regional state police barrack providing local law enforcement support and coordination. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#StatePoliceBarrack"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CollegeParkBarrack(StatePoliceBarrack):
    """Maryland State Police College Park Barrack supporting computer crimes investigations. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#CollegeParkBarrack"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class K9DetectionProgram(_cac_core.OrganizationLikeEntity):
    """Program utilizing trained detection dogs for CAC investigations. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#K9DetectionProgram"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    comment: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:comment', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CommunityEngagementK9(K9DetectionProgram):
    """K9 utilized for community outreach and educational programs. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#CommunityEngagementK9"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CoordinatedArrest(_cac_core.InvestigativeAction):
    """Arrest coordinated as part of larger operation. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#CoordinatedArrest"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CountyPoliceSupport(_uco_identity.Organization):
    """County-level police department providing support to state computer crimes investigations. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#CountyPoliceSupport"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CriticalIncidentDebriefing(_cac_core.SupportEvent):
    """Structured debriefing process following traumatic incidents. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#CriticalIncidentDebriefing"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SpecializedInvestigativeUnit(_uco_identity.Organization):
    """Specialized unit with unique capabilities for CAC investigations. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#SpecializedInvestigativeUnit"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    comment: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:comment', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    operational_capacity: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-specialized-units:operationalCapacity', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class CyberCrimeUnit(SpecializedInvestigativeUnit):
    """Unit specialized in cyber crime investigations. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#CyberCrimeUnit"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DetectionDog(_uco_identity.Identity):
    """Trained dog used for detection operations in CAC investigations. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#DetectionDog"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_capability: list[TripleThreatCapability] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-specialized-units:hasCapability', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'https://cacontology.projectvic.org/specialized-units#TripleThreatCapability', 'alternate_range_iris': []})


@dataclass
class DeviceDetection(_cac_core.InvestigativeAction):
    """Detection of electronic storage devices during search operations. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#DeviceDetection"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DigitalForensicsUnit(SpecializedInvestigativeUnit):
    """Unit specialized in digital forensics analysis. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#DigitalForensicsUnit"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ElectronicStorageDeviceK9(K9DetectionProgram):
    """K9 trained to detect electronic storage devices during search operations. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#ElectronicStorageDeviceK9"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InteragencyOperationSituation(_cac_core.Situation):
    """Situation involving operations across multiple agencies and jurisdictions. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#InteragencyOperationSituation"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class K9Officer(_cac_core.Role):
    """Law enforcement officer handling and working with detection dogs. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#K9Officer"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class K9SearchOperation(_cac_core.InvestigativeAction):
    """Search operation utilizing K9 detection capabilities. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#K9SearchOperation"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    search_warrants_executed: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-specialized-units:searchWarrantsExecuted', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#integer', 'alternate_range_iris': []})
    end_time_uco_core: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:endTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    start_time_uco_core: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class K9TrainingProgram(_cac_core.OrganizationLikeEntity):
    """Training program for K9 units and handlers. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#K9TrainingProgram"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StatePoliceComputerCrimesUnit(CyberCrimeUnit):
    """State police unit specialized in computer crimes and digital investigations involving child exploitation. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#StatePoliceComputerCrimesUnit"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MarylandStatePoliceComputerCrimesUnit(StatePoliceComputerCrimesUnit):
    """Maryland State Police unit coordinating the Maryland Internet Crimes Against Children Task Force. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#MarylandStatePoliceComputerCrimesUnit"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OfficerWellnessProgram(_cac_core.OrganizationLikeEntity):
    """Program providing mental health and wellness support to CAC officers. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#OfficerWellnessProgram"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    comment: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:comment', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class MentalHealthSupport(OfficerWellnessProgram):
    """Mental health services and support for officers dealing with traumatic content. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#MentalHealthSupport"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class NamedOperation(_cac_core.InvestigativeAction):
    """Formally named multi-phase operation with specific objectives. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#NamedOperation"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    arrest_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-specialized-units:arrestCount', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#integer', 'alternate_range_iris': []})
    end_time_uco_core: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:endTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    start_time_uco_core: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class MultiJurisdictionalOperation(NamedOperation):
    """Operation involving multiple jurisdictions and agencies. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#MultiJurisdictionalOperation"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MultiUnitCoordinationSituation(_cac_core.Situation):
    """Complex situation involving coordination between multiple specialized units. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#MultiUnitCoordinationSituation"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OperationEvaluationPhase(_cac_core.Phase):
    """Phase of post-operation analysis and evaluation. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#OperationEvaluationPhase"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OperationExecutionPhase(_cac_core.Phase):
    """Phase of active operation execution. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#OperationExecutionPhase"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OperationMetrics(_cac_core.AssessmentResult):
    """Metrics and performance data for specialized operations. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#OperationMetrics"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OperationPlanningPhase(_cac_core.Phase):
    """Phase of operation planning and preparation. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#OperationPlanningPhase"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OperationSafeOnlineSummer(NamedOperation):
    """National operation across 61 CAC Task Forces during summer months. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#OperationSafeOnlineSummer"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OperationUnhinged(NamedOperation):
    """Specific operation conducted by Idaho CAC resulting in 12 arrests. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#OperationUnhinged"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PeerSupport(OfficerWellnessProgram):
    """Peer-to-peer support programs for CAC personnel. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#PeerSupport"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PrinceGeorgesCountyPolice(CountyPoliceSupport):
    """Prince George's County Police Department supporting Maryland State Police computer crimes investigations. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#PrinceGeorgesCountyPolice"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SpecializedCapabilitySituation(_cac_core.Situation):
    """Situation requiring deployment of specialized unit capabilities. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#SpecializedCapabilitySituation"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SpecializedOperatorRole(_cac_core.Role):
    """Role of specialized operator within unit. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#SpecializedOperatorRole"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StressManagement(OfficerWellnessProgram):
    """Programs and techniques for managing work-related stress. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#StressManagement"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TacticalUnit(SpecializedInvestigativeUnit):
    """Unit handling high-risk tactical operations. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#TacticalUnit"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TechnicalSpecialistRole(_cac_core.Role):
    """Role of technical specialist providing specialized capabilities. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#TechnicalSpecialistRole"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TherapyDog(_uco_identity.Identity):
    """Trained therapy dog providing emotional support to officers. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#TherapyDog"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    provides_wellness_support: list[Person] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-specialized-units:providesWellnessSupport', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/identity/Person', 'alternate_range_iris': []})


@dataclass
class UndercoverUnit(SpecializedInvestigativeUnit):
    """Unit conducting undercover operations. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#UndercoverUnit"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class UnitCommanderRole(_cac_core.Role):
    """Role of commanding officer for specialized unit. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#UnitCommanderRole"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class UnitDeploymentPhase(_cac_core.Phase):
    """Phase when specialized unit is deployed for operations. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#UnitDeploymentPhase"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class UnitMaintenancePhase(_cac_core.Phase):
    """Phase for equipment maintenance and unit readiness. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#UnitMaintenancePhase"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class UnitTrainingPhase(_cac_core.Phase):
    """Phase focused on specialized unit training and preparation. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#UnitTrainingPhase"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimServicesUnit(SpecializedInvestigativeUnit):
    """Unit providing specialized victim services and support. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#VictimServicesUnit"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class WellnessCheck(_cac_core.SupportEvent):
    """Regular check on officer mental health and wellbeing. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/specialized-units#WellnessCheck"
    NAMESPACE_PREFIX: str = "cacontology-specialized-units"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    performer: Optional[Person] = field(default=None, metadata={'jsonld_key': 'uco-action:performer', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/identity/Person', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})
