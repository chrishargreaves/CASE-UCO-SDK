"""CAC Ontology - Crimes Against Children — cacontology_taskforce module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional, Union

import case_uco.uco.identity as _uco_identity
import case_uco.uco.location as _uco_location
import case_uco.uco.observable as _uco_observable
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AnalyticsUnit", "AnnualPerformance", "ArrestMetrics", "AssessmentPhase", "AttorneyGeneralHost", "CaliforniaRegionalSystem", "CoordinationMechanism", "CoordinationPhase", "CountyBasedTaskForce", "CyberTipMetrics", "DeploymentPhase", "DigitalForensicsUnit", "DistrictAttorneyHost", "EquipmentSharing", "ExecutionPhase", "ExpertiseSharing", "FederalICACtaskForce", "FloridaRegionalSystem", "GovernorsOfficeCrimePreventionFunding", "HistoricalMetrics", "ICACtaskForce", "IllinoisICACtaskForce", "IntelligenceSharing", "InterAgencyCoordination", "JointOperation", "LocalICACtaskForce", "LocalPoliceHost", "MarylandICACtaskForce", "MetropolitanTaskForce", "MilitaryICACtaskForce", "MultiRegionalState", "NationalHotline", "NationalICACtaskForceDirectory", "NetworkPerformance", "NewYorkRegionalSystem", "PersonnelSharing", "PlanningPhase", "ProactiveOperation", "ReactiveOperation", "RegionalCoordination", "RegionalTaskForce", "RegionalTaskForceCoordination", "ResourceSharing", "SheriffOfficeHost", "SpecializedUnit", "StateAgencyHost", "StateBureauHost", "StateICACtaskForce", "StateLocalFundingCombination", "StatePoliceHost", "StatewideTaskForce", "SweepOperation", "TacticalUnit", "TaskForceAlliance", "TaskForceAnalyst", "TaskForceCommander", "TaskForceContactInformation", "TaskForceCoordinator", "TaskForceForensicExaminer", "TaskForceHostOrganization", "TaskForceHotline", "TaskForceInvestigator", "TaskForceMember", "TaskForceMetrics", "TaskForceOperation", "TaskForceWebsite", "TexasRegionalSystem", "TrainingReachMetrics", "TrainingUnit", "UndercoverUnit", "VictimServiceUnit"]


@dataclass
class SpecializedUnit(_uco_observable.ObservableObject):
    """Specialized unit within CAC task force focused on specific aspects of investigations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#SpecializedUnit"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class AnalyticsUnit(SpecializedUnit):
    """Unit specializing in data analysis and intelligence gathering."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#AnalyticsUnit"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TaskForceMetrics(_cac_core.AssessmentResult):
    """Performance metrics and statistics for CAC task force operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#TaskForceMetrics"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AnnualPerformance(TaskForceMetrics):
    """Year-specific performance metrics for task force operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#AnnualPerformance"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ArrestMetrics(TaskForceMetrics):
    """Metrics tracking arrests made by task force operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#ArrestMetrics"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AssessmentPhase(_cac_core.Phase):
    """Phase involving post-operation assessment and evaluation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#AssessmentPhase"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TaskForceHostOrganization(_uco_identity.Organization):
    """Organization that hosts and coordinates an CAC task force."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#TaskForceHostOrganization"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class AttorneyGeneralHost(TaskForceHostOrganization):
    """State attorney general office hosting CAC task force (Idaho AG, Illinois AG, Texas AG, etc.)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#AttorneyGeneralHost"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MultiRegionalState(_uco_location.Location):
    """State with multiple CAC task forces covering different geographic regions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#MultiRegionalState"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CaliforniaRegionalSystem(MultiRegionalState):
    """California's 5-region CAC system: Fresno, Los Angeles, Sacramento, San Diego, San Jose areas."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#CaliforniaRegionalSystem"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CoordinationMechanism(_uco_observable.ObservableObject):
    """Formal mechanism for coordinating task force activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#CoordinationMechanism"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CoordinationPhase(_cac_core.Phase):
    """Phase focused on inter-agency coordination and resource sharing."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#CoordinationPhase"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ICACtaskForce(_uco_observable.ObservableObject):
    """Internet Crimes Against Children task force unit specializing in child exploitation investigations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#ICACtaskForce"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class StateICACtaskForce(ICACtaskForce):
    """State-level CAC task force coordinating regional investigations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#StateICACtaskForce"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RegionalTaskForce(StateICACtaskForce):
    """CAC task force covering specific geographic region within a state."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#RegionalTaskForce"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CountyBasedTaskForce(RegionalTaskForce):
    """CAC task force hosted by and primarily serving specific county jurisdiction."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#CountyBasedTaskForce"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CyberTipMetrics(TaskForceMetrics):
    """Metrics tracking CyberTip processing and analysis by task force."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#CyberTipMetrics"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DeploymentPhase(_cac_core.Phase):
    """Phase involving deployment of personnel and resources."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#DeploymentPhase"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DigitalForensicsUnit(SpecializedUnit):
    """Specialized unit focused on digital evidence acquisition and analysis."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#DigitalForensicsUnit"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DistrictAttorneyHost(TaskForceHostOrganization):
    """District or county attorney office hosting CAC task force (Delaware County DA, Cook County SA, etc.)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#DistrictAttorneyHost"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ResourceSharing(_uco_observable.ObservableObject):
    """Sharing of resources, personnel, or expertise between task forces."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#ResourceSharing"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class EquipmentSharing(ResourceSharing):
    """Sharing of specialized equipment or technology."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#EquipmentSharing"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ExecutionPhase(_cac_core.Phase):
    """Phase involving active execution of task force operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#ExecutionPhase"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ExpertiseSharing(ResourceSharing):
    """Sharing of specialized knowledge or technical expertise."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#ExpertiseSharing"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FederalICACtaskForce(ICACtaskForce):
    """Federal-level CAC task force for complex or multi-jurisdictional cases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#FederalICACtaskForce"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FloridaRegionalSystem(MultiRegionalState):
    """Florida's 3-region CAC system: Central, Northern, Southern regions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#FloridaRegionalSystem"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class GovernorsOfficeCrimePreventionFunding(_cac_core.EnduringEntity):
    """State-level funding provided by Governor's Office for Crime Prevention and Policy for CAC task force operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#GovernorsOfficeCrimePreventionFunding"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HistoricalMetrics(TaskForceMetrics):
    """Long-term historical performance data for task force operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#HistoricalMetrics"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class IllinoisICACtaskForce(StateICACtaskForce):
    """Illinois state CAC task force with specialized capabilities and extensive network partnerships."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#IllinoisICACtaskForce"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class IntelligenceSharing(ResourceSharing):
    """Sharing of intelligence and investigative information."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#IntelligenceSharing"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InterAgencyCoordination(CoordinationMechanism):
    """Coordination mechanism between different law enforcement agencies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#InterAgencyCoordination"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TaskForceOperation(_cac_core.InvestigativeAction):
    """Coordinated operation conducted by CAC task force."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#TaskForceOperation"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    operation_duration: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-taskforce:operationDuration', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    operation_scope: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-taskforce:operationScope', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    operation_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-taskforce:operationType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    participating_agencies: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-taskforce:participatingAgencies', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    end_time_uco_core: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:endTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    start_time_uco_core: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class JointOperation(TaskForceOperation):
    """Operation involving multiple task forces or agencies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#JointOperation"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    coordination_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-taskforce:coordinationLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    lead_task_force: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-taskforce:leadTaskForce', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class LocalICACtaskForce(ICACtaskForce):
    """Local or regional CAC task force unit."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#LocalICACtaskForce"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LocalPoliceHost(TaskForceHostOrganization):
    """Local police department hosting CAC task force (Phoenix PD, Los Angeles PD, San Jose PD, etc.)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#LocalPoliceHost"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MarylandICACtaskForce(StateICACtaskForce):
    """Maryland state CAC task force coordinated by Maryland State Police Computer Crimes Unit with Governor's Office for Crime Prevention and Policy funding."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#MarylandICACtaskForce"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MetropolitanTaskForce(RegionalTaskForce):
    """CAC task force covering major metropolitan area (Los Angeles, Dallas, Houston, NYC)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#MetropolitanTaskForce"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MilitaryICACtaskForce(ICACtaskForce):
    """CAC task force for U.S. Armed Forces military branches with specialized military jurisdiction."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#MilitaryICACtaskForce"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TaskForceContactInformation(_cac_core.EnduringEntity):
    """Contact information for CAC task force including phone, email, and website."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#TaskForceContactInformation"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class NationalHotline(TaskForceContactInformation):
    """National CAC hotline (877-798-7682) for general information and coordination."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#NationalHotline"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class NationalICACtaskForceDirectory(_cac_core.Artifact):
    """Comprehensive directory of all 61 CAC task forces across the United States, territories, and military branches."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#NationalICACtaskForceDirectory"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class NetworkPerformance(TaskForceMetrics):
    """Performance metrics for multi-agency network coordination."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#NetworkPerformance"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class NewYorkRegionalSystem(MultiRegionalState):
    """New York's 2-region CAC system: Statewide and New York City area."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#NewYorkRegionalSystem"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PersonnelSharing(ResourceSharing):
    """Sharing of specialized personnel between task forces."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#PersonnelSharing"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PlanningPhase(_cac_core.Phase):
    """Phase involving operational planning and resource allocation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#PlanningPhase"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProactiveOperation(TaskForceOperation):
    """Proactive operation to identify and investigate potential offenders."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#ProactiveOperation"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ReactiveOperation(TaskForceOperation):
    """Operation in response to specific tips or reports."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#ReactiveOperation"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RegionalCoordination(CoordinationMechanism):
    """Coordination mechanism for regional task force activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#RegionalCoordination"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RegionalTaskForceCoordination(CoordinationMechanism):
    """Coordination mechanism between multiple task forces within the same state."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#RegionalTaskForceCoordination"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SheriffOfficeHost(TaskForceHostOrganization):
    """County sheriff's office hosting CAC task force (Fresno County SO, Broward County SO, etc.)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#SheriffOfficeHost"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StateAgencyHost(TaskForceHostOrganization):
    """Other state agency hosting CAC task force (Delaware DOJ, Hawaii DOA, etc.)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#StateAgencyHost"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StateBureauHost(TaskForceHostOrganization):
    """State bureau of investigation hosting CAC task force (Georgia BIA, North Carolina SBI, etc.)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#StateBureauHost"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StateLocalFundingCombination(_cac_core.EnduringEntity):
    """Combined funding from state Governor's Office and federal DOJ grants for task force operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#StateLocalFundingCombination"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StatePoliceHost(TaskForceHostOrganization):
    """State police agency hosting CAC task force (Maryland State Police, Connecticut State Police, etc.)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#StatePoliceHost"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StatewideTaskForce(StateICACtaskForce):
    """CAC task force with statewide jurisdiction and coordination responsibility."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#StatewideTaskForce"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SweepOperation(TaskForceOperation):
    """Large-scale coordinated operation targeting multiple suspects."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#SweepOperation"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TacticalUnit(SpecializedUnit):
    """Unit handling high-risk arrests and tactical operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#TacticalUnit"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TaskForceAlliance(CoordinationMechanism):
    """Formal alliance between multiple CAC task forces."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#TaskForceAlliance"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TaskForceMember(_cac_core.Role):
    """Individual member of an CAC task force with specialized training."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#TaskForceMember"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    member_role: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-taskforce:memberRole', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    membership_end_date: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'cacontology-taskforce:membershipEndDate', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    membership_start_date: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'cacontology-taskforce:membershipStartDate', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    membership_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-taskforce:membershipType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    security_clearance: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-taskforce:securityClearance', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    training_completed: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-taskforce:trainingCompleted', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})


@dataclass
class TaskForceAnalyst(TaskForceMember):
    """Analyst specializing in CAC intelligence and data analysis."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#TaskForceAnalyst"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TaskForceCommander(TaskForceMember):
    """Command-level officer responsible for task force operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#TaskForceCommander"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    command_authority: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-taskforce:commandAuthority', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    years_experience: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-taskforce:yearsExperience', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class TaskForceCoordinator(TaskForceMember):
    """Coordinator responsible for inter-agency cooperation and resource management."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#TaskForceCoordinator"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TaskForceForensicExaminer(TaskForceMember):
    """Digital forensic examiner specializing in CAC evidence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#TaskForceForensicExaminer"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TaskForceHotline(TaskForceContactInformation):
    """Dedicated phone line for CAC task force operations and reporting."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#TaskForceHotline"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TaskForceInvestigator(TaskForceMember):
    """Investigator specializing in CAC cases and child exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#TaskForceInvestigator"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TaskForceWebsite(TaskForceContactInformation):
    """Official website for CAC task force with resources and information."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#TaskForceWebsite"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TexasRegionalSystem(MultiRegionalState):
    """Texas's 3-region CAC system: Statewide, Dallas, Houston areas."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#TexasRegionalSystem"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TrainingReachMetrics(TaskForceMetrics):
    """Metrics tracking training and education reach to professionals and community."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#TrainingReachMetrics"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TrainingUnit(SpecializedUnit):
    """Unit responsible for training and education of task force members."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#TrainingUnit"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class UndercoverUnit(SpecializedUnit):
    """Unit specializing in undercover operations and online investigations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#UndercoverUnit"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimServiceUnit(SpecializedUnit):
    """Unit providing specialized services and support to child victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/taskforce#VictimServiceUnit"
    NAMESPACE_PREFIX: str = "cacontology-taskforce"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
