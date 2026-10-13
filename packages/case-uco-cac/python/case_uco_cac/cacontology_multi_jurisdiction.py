"""CAC Ontology - Crimes Against Children — cacontology_multi_jurisdiction module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional, Union

import case_uco.uco.action as _uco_action
import case_uco.uco.identity as _uco_identity
import case_uco.uco.observable as _uco_observable
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AllFBIFieldOfficesOperation", "AutomatedEvidenceDistribution", "CEOSCoordinatedOperation", "ChildRescueCoordination", "CommunityOutreachTriggeredInvestigation", "ComplianceMonitoringOperation", "ComplianceVisitCoordination", "CoordinatedArrestWave", "CoordinatedCharging", "CoordinatingAgent", "CrossBorderOperation", "CrossStateEvidence", "DistributedProsecutionTeam", "ExtraditionRequest", "FederalAgency", "FederalJurisdiction", "FederalJurisdictionTrigger", "HandsOnOffenseInvestigation", "InformationSharing", "InformationSharingAgreement", "InformationSynthesisPhase", "InitialCoordinationPhase", "InteragencyAgreement", "InteragencyCooperationSituation", "InternationalAgency", "InternationalJurisdiction", "InternationalLegalHarmonization", "InternationalProsecutionFramework", "InterstateCoordination", "InterstateFlightFromProsecution", "InterstateTraffickingNetwork", "InterstateTransportationOffense", "InterstateVictimTransport", "JointExecutionPhase", "JointInvestigation", "Jurisdiction", "JurisdictionalConflictSituation", "JurisdictionalHandoff", "JurisdictionalNegotiationPhase", "JurisdictionalWarrant", "LargeScaleOperation", "LawEnforcementAgency", "LeadAgency", "LiaisonOfficer", "LocalAgency", "LocalJurisdiction", "MassChildRescueOperation", "MassProsecutionCoordination", "MassUserJurisdictionMapping", "MultiJurisdictionalInvestigation", "MultiJurisdictionalSituation", "MultiStateTraffickingInvestigation", "MutualAidRequest", "NamedMultiJurisdictionalOperation", "NationalCoordinatedOperation", "NationwideChildRescueCoordination", "NationwideOperation", "OperationMetricsTracking", "OperationSafeOnlineSummerType", "ParticipatingAgency", "PriorityProsecutionTrack", "ProactiveInvestigationCampaign", "ProjectSafeChildhoodOperation", "ProsecutionCapacityAnalysis", "RapidResponseCoordination", "RegistrationComplianceViolation", "ResourceSharing", "SchoolPresentationDisclosureWorkflow", "SexOffenderComplianceCheck", "SimultaneousChildRescue", "StateAgency", "StateJurisdiction", "StateLineCrossing", "StatewideSweep", "TaskForce", "TaskForceLeader", "TaskForceOperation", "TraffickingCoordinationCenter", "TraffickingInvestigationTask", "TransportationForIllegalPurpose", "USAttorneyOfficeParticipation", "UserTriageProsecution", "VictimIdentificationTask"]


@dataclass
class MultiJurisdictionalInvestigation(_cac_core.CoordinationEvent):
    """Investigation spanning multiple legal jurisdictions requiring coordination between agencies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#MultiJurisdictionalInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_data_completeness: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:hasDataCompleteness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_data_consistency: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:hasDataConsistency', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_data_quality: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:hasDataQuality', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_validation_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:hasValidationLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class NamedMultiJurisdictionalOperation(MultiJurisdictionalInvestigation):
    """Formally named multi-phase operation coordinated across jurisdictions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#NamedMultiJurisdictionalOperation"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    comment: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:comment', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    coordination_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:coordinationLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_complexity_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:hasComplexityLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_coordination_effectiveness: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:hasCoordinationEffectiveness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_coordination_intensity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:hasCoordinationIntensity', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_success_rate: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:hasSuccessRate', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_unification_level: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:hasUnificationLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    jurisdiction_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:jurisdictionCount', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    lead_agency: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:leadAgency', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    operation_duration: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:operationDuration', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    operation_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:operationType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    end_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:endTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class NationwideOperation(NamedMultiJurisdictionalOperation):
    """Law enforcement operation coordinated across entire country involving all FBI field offices."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#NationwideOperation"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AllFBIFieldOfficesOperation(NationwideOperation):
    """Operation involving all 55 FBI field offices in coordinated enforcement effort."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#AllFBIFieldOfficesOperation"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AutomatedEvidenceDistribution(_uco_action.Action):
    """Automated system for distributing evidence packages to appropriate jurisdictions based on user location and evidence strength."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#AutomatedEvidenceDistribution"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CEOSCoordinatedOperation(NationwideOperation):
    """Operation coordinated by Child Exploitation and Obscenity Section (CEOS)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#CEOSCoordinatedOperation"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ChildRescueCoordination(_uco_action.Action):
    """Coordination of child rescue operations across jurisdictions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#ChildRescueCoordination"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CommunityOutreachTriggeredInvestigation(MultiJurisdictionalInvestigation):
    """Investigation triggered by victim disclosure following community outreach presentation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#CommunityOutreachTriggeredInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ComplianceMonitoringOperation(MultiJurisdictionalInvestigation):
    """Large-scale operation monitoring sex offender compliance and registration requirements."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#ComplianceMonitoringOperation"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ComplianceVisitCoordination(_uco_action.Action):
    """Coordination of multiple compliance visits across jurisdictions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#ComplianceVisitCoordination"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CoordinatedArrestWave(MultiJurisdictionalInvestigation):
    """Coordinated arrests conducted as part of larger operation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#CoordinatedArrestWave"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CoordinatedCharging(_uco_action.Action):
    """Coordinated charging decisions across multiple jurisdictions to ensure consistent prosecution approach."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#CoordinatedCharging"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CoordinatingAgent(_cac_core.Role):
    """Personnel responsible for coordinating multi-jurisdictional activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#CoordinatingAgent"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CrossBorderOperation(MultiJurisdictionalInvestigation):
    """Law enforcement operation that crosses state or national borders."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#CrossBorderOperation"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    border_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:borderType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    legal_framework: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:legalFramework', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    treaty_basis: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:treatyBasis', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CrossStateEvidence(_cac_core.Artifact):
    """Evidence collected across multiple states in trafficking investigation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#CrossStateEvidence"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DistributedProsecutionTeam(_uco_identity.Organization):
    """Prosecution team distributed across multiple jurisdictions for handling massive caseloads."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#DistributedProsecutionTeam"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ExtraditionRequest(_uco_observable.ObservableObject):
    """Legal request to transfer suspect between jurisdictions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#ExtraditionRequest"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class LawEnforcementAgency(_uco_identity.Organization):
    """Government organization responsible for law enforcement within a jurisdiction."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#LawEnforcementAgency"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_capability_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:hasCapabilityLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_cooperation_willingness: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:hasCooperationWillingness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_resource_capacity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:hasResourceCapacity', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class FederalAgency(LawEnforcementAgency):
    """Law enforcement agency with federal jurisdiction."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#FederalAgency"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Jurisdiction(_cac_core.PlaceLikeEntity):
    """Legal authority and geographic area where an agency has enforcement power."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#Jurisdiction"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FederalJurisdiction(Jurisdiction):
    """Legal authority under federal law and courts."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#FederalJurisdiction"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FederalJurisdictionTrigger(_cac_core.EnduringEntity):
    """Interstate activity that triggers federal jurisdiction."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#FederalJurisdictionTrigger"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HandsOnOffenseInvestigation(MultiJurisdictionalInvestigation):
    """Investigation specifically targeting hands-on sexual offenses against children."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#HandsOnOffenseInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InformationSharing(_cac_core.CoordinationEvent):
    """Formal sharing of intelligence or evidence between jurisdictions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#InformationSharing"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    classification_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:classificationLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_actionability: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:hasActionability', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_intelligence_value: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:hasIntelligenceValue', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_security_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:hasSecurityLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_sharing_efficiency: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:hasSharingEfficiency', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_timeliness: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:hasTimeliness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    reciprocity_required: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:reciprocityRequired', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    sharing_date: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:sharingDate', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    sharing_mechanism: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:sharingMechanism', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    sharing_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:sharingType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class InformationSharingAgreement(_uco_observable.ObservableObject):
    """Agreement governing sharing of sensitive information between agencies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#InformationSharingAgreement"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class InformationSynthesisPhase(_cac_core.Phase):
    """Phase involving compilation and analysis of multi-jurisdictional evidence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#InformationSynthesisPhase"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InitialCoordinationPhase(_cac_core.Phase):
    """Phase involving initial contact and coordination between jurisdictions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#InitialCoordinationPhase"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InteragencyAgreement(_uco_observable.ObservableObject):
    """Formal agreement between agencies for cooperation and resource sharing."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#InteragencyAgreement"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class InteragencyCooperationSituation(_cac_core.Situation):
    """Situation involving successful coordination between agencies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#InteragencyCooperationSituation"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InternationalAgency(LawEnforcementAgency):
    """Law enforcement agency from foreign jurisdiction."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#InternationalAgency"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InternationalJurisdiction(Jurisdiction):
    """Legal authority in foreign countries."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#InternationalJurisdiction"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InternationalProsecutionFramework(CrossBorderOperation):
    """Framework for coordinating prosecutions across multiple countries for global platform takedowns."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#InternationalProsecutionFramework"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InternationalLegalHarmonization(InternationalProsecutionFramework):
    """Harmonization of legal approaches across countries for consistent prosecution of global platform users."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#InternationalLegalHarmonization"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InterstateCoordination(InformationSharing):
    """Coordination between law enforcement agencies across state lines."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#InterstateCoordination"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StateLineCrossing(_uco_action.Action):
    """Documented crossing of state boundaries during offense."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#StateLineCrossing"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class InterstateFlightFromProsecution(StateLineCrossing):
    """Crossing state lines to avoid prosecution or arrest."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#InterstateFlightFromProsecution"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InterstateTraffickingNetwork(_cac_core.OrganizationLikeEntity):
    """Criminal network operating across state boundaries for trafficking."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#InterstateTraffickingNetwork"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InterstateTransportationOffense(_cac_core.ExploitationEvent):
    """Criminal offense involving transportation of victim across state lines."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#InterstateTransportationOffense"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InterstateVictimTransport(StateLineCrossing):
    """Transportation of minor victim across state lines."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#InterstateVictimTransport"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class JointExecutionPhase(_cac_core.Phase):
    """Phase involving coordinated execution of multi-jurisdictional operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#JointExecutionPhase"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class JointInvestigation(MultiJurisdictionalInvestigation):
    """Investigation conducted jointly by multiple law enforcement agencies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#JointInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class JurisdictionalConflictSituation(_cac_core.Situation):
    """Situation involving disputes over jurisdictional authority."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#JurisdictionalConflictSituation"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class JurisdictionalHandoff(_uco_action.Action):
    """Transfer of investigative authority between state and federal agencies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#JurisdictionalHandoff"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class JurisdictionalNegotiationPhase(_cac_core.Phase):
    """Phase involving determination of lead agency and jurisdictional authority."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#JurisdictionalNegotiationPhase"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class JurisdictionalWarrant(_uco_observable.ObservableObject):
    """Legal authorization that specifies jurisdictional authority."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#JurisdictionalWarrant"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class LargeScaleOperation(NamedMultiJurisdictionalOperation):
    """Operation involving 100+ law enforcement actions or extensive coordination."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#LargeScaleOperation"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LeadAgency(_cac_core.Role):
    """Primary agency responsible for coordinating multi-jurisdictional investigation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#LeadAgency"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LiaisonOfficer(_cac_core.Role):
    """Officer responsible for communication between agencies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#LiaisonOfficer"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LocalAgency(LawEnforcementAgency):
    """Law enforcement agency with local jurisdiction (city, county, municipal)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#LocalAgency"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LocalJurisdiction(Jurisdiction):
    """Legal authority at local level (city, county, municipal)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#LocalJurisdiction"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MassChildRescueOperation(ChildRescueCoordination):
    """Large-scale operation resulting in rescue of 100+ children."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#MassChildRescueOperation"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MassProsecutionCoordination(NamedMultiJurisdictionalOperation):
    """Coordination of prosecutions for massive user bases from large-scale platform takedowns requiring simultaneous action across multiple jurisdictions (nearly 2 million users for Kidflix operation)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#MassProsecutionCoordination"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MassUserJurisdictionMapping(_uco_action.Action):
    """Mapping of massive user bases to appropriate jurisdictions for prosecution based on location and legal frameworks."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#MassUserJurisdictionMapping"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class MultiJurisdictionalSituation(_cac_core.Situation):
    """Complex situation requiring coordination across multiple jurisdictions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#MultiJurisdictionalSituation"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MultiStateTraffickingInvestigation(CrossBorderOperation):
    """Child sex trafficking investigation spanning multiple states."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#MultiStateTraffickingInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MutualAidRequest(_uco_observable.ObservableObject):
    """Formal request for assistance from another jurisdiction."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#MutualAidRequest"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class NationalCoordinatedOperation(NamedMultiJurisdictionalOperation):
    """Operation coordinated across multiple CAC task forces nationally."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#NationalCoordinatedOperation"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class NationwideChildRescueCoordination(MassChildRescueOperation):
    """Coordination of child rescue operations across entire country."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#NationwideChildRescueCoordination"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OperationMetricsTracking(_cac_core.AssessmentResult):
    """Comprehensive tracking of operation outcomes and effectiveness."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#OperationMetricsTracking"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OperationSafeOnlineSummerType(NationalCoordinatedOperation):
    """Type of national operation coordinated across 61+ CAC Task Forces."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#OperationSafeOnlineSummerType"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ParticipatingAgency(_cac_core.Role):
    """Agency providing support or resources to multi-jurisdictional investigation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#ParticipatingAgency"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class UserTriageProsecution(_uco_action.Action):
    """Prosecution strategy based on automated triage of user risk levels and evidence strength for massive user databases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#UserTriageProsecution"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PriorityProsecutionTrack(UserTriageProsecution):
    """High-priority prosecution track for most serious offenders identified in mass user analysis."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#PriorityProsecutionTrack"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProactiveInvestigationCampaign(MultiJurisdictionalInvestigation):
    """Campaign focused on proactive investigation rather than reactive response."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#ProactiveInvestigationCampaign"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProjectSafeChildhoodOperation(NationwideOperation):
    """Operation conducted under Project Safe Childhood initiative framework."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#ProjectSafeChildhoodOperation"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProsecutionCapacityAnalysis(_uco_action.Action):
    """Analysis of prosecution capacity across jurisdictions to optimize case distribution for massive operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#ProsecutionCapacityAnalysis"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class RapidResponseCoordination(_uco_action.Action):
    """Coordination enabling rapid response from victim disclosure to arrest."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#RapidResponseCoordination"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class RegistrationComplianceViolation(_cac_core.EnduringEntity):
    """Violation of sex offender registration requirements."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#RegistrationComplianceViolation"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ResourceSharing(_cac_core.CoordinationEvent):
    """Sharing of personnel, equipment, or expertise between agencies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#ResourceSharing"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    cost_sharing: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:costSharing', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_availability: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:hasAvailability', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_cost_effectiveness: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:hasCostEffectiveness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_resource_utilization: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:hasResourceUtilization', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    resource_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:resourceType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    resource_value: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:resourceValue', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    sharing_duration: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:sharingDuration', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class SchoolPresentationDisclosureWorkflow(RapidResponseCoordination):
    """Workflow from school safety presentation to victim disclosure to rapid arrest."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#SchoolPresentationDisclosureWorkflow"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SexOffenderComplianceCheck(_uco_action.Action):
    """Individual compliance check visit to registered sex offender."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#SexOffenderComplianceCheck"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SimultaneousChildRescue(MassChildRescueOperation):
    """Rescue of multiple children across different locations simultaneously."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#SimultaneousChildRescue"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StateAgency(LawEnforcementAgency):
    """Law enforcement agency with state-level jurisdiction."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#StateAgency"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StateJurisdiction(Jurisdiction):
    """Legal authority under state law and courts."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#StateJurisdiction"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StatewideSweep(ComplianceMonitoringOperation):
    """Statewide operation conducting compliance checks across all jurisdictions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#StatewideSweep"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TaskForce(_uco_identity.Organization):
    """Temporary multi-agency organization formed for specific operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#TaskForce"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_cohesion_level: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:hasCohesionLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_expertise_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:hasExpertiseLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_operational_readiness: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-multi-jurisdiction:hasOperationalReadiness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class TaskForceLeader(_cac_core.Role):
    """Officer responsible for leading multi-agency task force operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#TaskForceLeader"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TaskForceOperation(MultiJurisdictionalInvestigation):
    """Coordinated operation conducted by multi-agency task force."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#TaskForceOperation"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TraffickingCoordinationCenter(_uco_identity.Organization):
    """Center coordinating multi-state trafficking investigations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#TraffickingCoordinationCenter"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class TraffickingInvestigationTask(_uco_action.Action):
    """Specific investigation task in multi-state trafficking case."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#TraffickingInvestigationTask"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class TransportationForIllegalPurpose(InterstateTransportationOffense):
    """Transportation with intent to engage in criminal sexual activity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#TransportationForIllegalPurpose"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class USAttorneyOfficeParticipation(MassProsecutionCoordination):
    """Participation of US Attorney's Offices around the country in coordinated operation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#USAttorneyOfficeParticipation"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimIdentificationTask(_uco_action.Action):
    """Task focused on identifying new child victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/multi-jurisdiction#VictimIdentificationTask"
    NAMESPACE_PREFIX: str = "cacontology-multi-jurisdiction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
