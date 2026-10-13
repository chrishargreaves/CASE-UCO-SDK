"""CAC Ontology - Crimes Against Children — cacontology_investigation_coordination module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional, Union

import case_uco.uco.core as _uco_core
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["CaseInformationSharing", "CaseResolutionTimeMetrics", "CommunicationProtocol", "CoordinationAgreement", "CoordinationEffectivenessMetrics", "CoordinationMetrics", "CostEfficiencyMetrics", "EmergencyCommunicationChannel", "EncryptedCommunicationChannel", "EquipmentSharing", "EvidenceSharing", "ExpertiseSharing", "FacilitySharing", "FederalCoordination", "FormalAgreement", "FormalCommunicationChannel", "FundingSharing", "InformalAgreement", "InformalCommunicationChannel", "InformationSharing", "InformationSharingRateMetrics", "IntelligenceLiaison", "IntelligenceSharing", "InternationalCoordination", "InvestigationCoordination", "JointInvestigation", "JointOperationsPlan", "LegalLiaison", "LiaisonCommunicationChannel", "LiaisonOfficer", "LocalCoordination", "MemorandumOfAgreement", "MemorandumOfUnderstanding", "MissingChildRescueOperation", "MultiAgencyCoordination", "MultiStateCoordination", "OperationalLiaison", "ParallelInvestigation", "PersonnelSharing", "PrimaryLiaison", "RegionalCoordination", "ResourceSharing", "ResourceUtilizationMetrics", "ResponseTimeMetrics", "SecondaryLiaison", "SecureCommunicationChannel", "StateCoordination", "SuspectInformationSharing", "TaskForceCharter", "TaskForceCoordination", "TechnicalDataSharing", "TechnicalLiaison", "TechnologySharing", "VictimInformationSharing"]


@dataclass
class InformationSharing(_cac_core.CoordinationEvent):
    """Systematic sharing of information between agencies including intelligence, evidence, case data, and technical information."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#InformationSharing"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})
    has_end_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasEndPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})
    comment: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:comment', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    classification_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:classificationLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_data_completeness: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasDataCompleteness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_data_consistency: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasDataConsistency', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_data_quality: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasDataQuality', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_security_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasSecurityLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_sharing_efficiency: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasSharingEfficiency', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_timeliness: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasTimeliness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_validation_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasValidationLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    reciprocity: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:reciprocity', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    sharing_agreement: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:sharingAgreement', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    sharing_mechanism: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:sharingMechanism', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    sharing_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:sharingType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    modified_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:modifiedTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class CaseInformationSharing(InformationSharing):
    """Sharing of case-specific information including case files, reports, witness statements, and investigative findings."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#CaseInformationSharing"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CoordinationMetrics(_cac_core.AssessmentResult):
    """Performance metrics for measuring effectiveness and efficiency of inter-agency coordination."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#CoordinationMetrics"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})
    benchmark_comparison: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:benchmarkComparison', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_accuracy: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasAccuracy', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_reliability: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasReliability', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    measurement_period: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:measurementPeriod', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    metric_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:metricType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    metric_value: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:metricValue', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class CaseResolutionTimeMetrics(CoordinationMetrics):
    """Metrics measuring impact of coordination on case resolution times and outcomes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#CaseResolutionTimeMetrics"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CommunicationProtocol(_uco_core.UcoObject):
    """Formal protocols governing communication between agencies including channels, frequencies, and procedures."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#CommunicationProtocol"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    communication_frequency: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:communicationFrequency', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    escalation_procedure: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:escalationProcedure', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    protocol_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:protocolType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    response_time_requirement: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:responseTimeRequirement', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class CoordinationAgreement(_uco_core.UcoObject):
    """Formal agreements governing coordination between agencies including MOUs, MOAs, and operational agreements."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#CoordinationAgreement"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})
    has_end_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasEndPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})
    comment: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:comment', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    agreement_scope: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:agreementScope', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    agreement_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:agreementType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    effective_date: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:effectiveDate', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    expiration_date: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:expirationDate', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    has_data_completeness: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasDataCompleteness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_data_consistency: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasDataConsistency', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_data_quality: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasDataQuality', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_validation_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasValidationLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    renewal_clause: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:renewalClause', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    termination_clause: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:terminationClause', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class CoordinationEffectivenessMetrics(CoordinationMetrics):
    """Metrics measuring overall effectiveness of coordination efforts and outcomes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#CoordinationEffectivenessMetrics"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CostEfficiencyMetrics(CoordinationMetrics):
    """Metrics measuring cost efficiency and financial benefits of coordination activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#CostEfficiencyMetrics"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EmergencyCommunicationChannel(CommunicationProtocol):
    """Emergency communication channels for urgent coordination and crisis response."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#EmergencyCommunicationChannel"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SecureCommunicationChannel(CommunicationProtocol):
    """Secure communication channels for sensitive information and classified communications."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#SecureCommunicationChannel"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EncryptedCommunicationChannel(SecureCommunicationChannel):
    """Encrypted communication channels providing enhanced security for sensitive operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#EncryptedCommunicationChannel"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ResourceSharing(_cac_core.CoordinationEvent):
    """Systematic sharing of resources between agencies including personnel, equipment, facilities, and expertise."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#ResourceSharing"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})
    has_end_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasEndPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})
    comment: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:comment', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    availability_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:availabilityLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    cost_sharing: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:costSharing', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    has_data_completeness: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasDataCompleteness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_data_consistency: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasDataConsistency', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_data_quality: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasDataQuality', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_validation_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasValidationLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    reimbursement: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:reimbursement', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    resource_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:resourceType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    sharing_duration: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:sharingDuration', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    modified_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:modifiedTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class EquipmentSharing(ResourceSharing):
    """Sharing of specialized equipment including forensic tools, surveillance equipment, and technical devices."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#EquipmentSharing"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EvidenceSharing(InformationSharing):
    """Formal sharing of evidence between agencies including digital evidence, physical evidence, and forensic analysis results."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#EvidenceSharing"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ExpertiseSharing(ResourceSharing):
    """Sharing of specialized expertise including subject matter experts, consultants, and technical specialists."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#ExpertiseSharing"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FacilitySharing(ResourceSharing):
    """Sharing of facilities including laboratories, command centers, training facilities, and secure meeting spaces."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#FacilitySharing"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InvestigationCoordination(_cac_core.CoordinationEvent):
    """Comprehensive framework for coordinating investigations across multiple agencies, jurisdictions, and organizational boundaries."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#InvestigationCoordination"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})
    has_end_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasEndPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})
    comment: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:comment', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    coordination_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:coordinationLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    coordination_status: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:coordinationStatus', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    coordination_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:coordinationType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_complexity_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasComplexityLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_coordination_effectiveness: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasCoordinationEffectiveness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_data_completeness: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasDataCompleteness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_data_consistency: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasDataConsistency', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_data_quality: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasDataQuality', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_success_rate: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasSuccessRate', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_validation_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasValidationLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    lead_agency: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:leadAgency', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    participating_agencies: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:participatingAgencies', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    end_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:endTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    modified_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:modifiedTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class FederalCoordination(InvestigationCoordination):
    """Coordination involving federal agencies and national-level law enforcement."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#FederalCoordination"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FormalAgreement(CoordinationAgreement):
    """Comprehensive formal agreement with legal binding terms for inter-agency coordination."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#FormalAgreement"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FormalCommunicationChannel(CommunicationProtocol):
    """Official communication channels following established protocols and hierarchies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#FormalCommunicationChannel"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FundingSharing(ResourceSharing):
    """Coordinated funding arrangements including cost sharing, joint funding, and resource pooling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#FundingSharing"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InformalAgreement(CoordinationAgreement):
    """Informal agreement or understanding for coordination without formal legal binding."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#InformalAgreement"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InformalCommunicationChannel(CommunicationProtocol):
    """Informal communication channels for rapid information exchange and coordination."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#InformalCommunicationChannel"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InformationSharingRateMetrics(CoordinationMetrics):
    """Metrics measuring the rate and volume of information sharing between agencies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#InformationSharingRateMetrics"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LiaisonOfficer(_cac_core.Role):
    """Designated officer responsible for maintaining communication and coordination between agencies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#LiaisonOfficer"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})
    has_end_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasEndPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})
    comment: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:comment', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    assignment_duration: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:assignmentDuration', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    clearance_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:clearanceLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    communication_authority: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:communicationAuthority', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_data_completeness: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasDataCompleteness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_data_consistency: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasDataConsistency', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_data_quality: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasDataQuality', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_liaison_effectiveness: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasLiaisonEffectiveness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_responsiveness: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasResponsiveness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_trust_level: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasTrustLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_validation_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasValidationLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    liaison_role: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:liaisonRole', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class IntelligenceLiaison(LiaisonOfficer):
    """Intelligence liaison officer managing intelligence sharing and coordination activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#IntelligenceLiaison"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class IntelligenceSharing(InformationSharing):
    """Specialized sharing of intelligence information including tactical, strategic, operational, and threat assessment data."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#IntelligenceSharing"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_actionability: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasActionability', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_intelligence_value: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasIntelligenceValue', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    information_accuracy: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:informationAccuracy', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    intelligence_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:intelligenceType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    source_reliability: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:sourceReliability', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class InternationalCoordination(InvestigationCoordination):
    """Coordination activities involving international agencies and cross-border cooperation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#InternationalCoordination"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class JointInvestigation(InvestigationCoordination):
    """Formal joint investigation involving multiple agencies working together with shared resources, command structure, and unified reporting."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#JointInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_coordination_intensity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasCoordinationIntensity', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_unification_level: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:hasUnificationLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    investigation_scope: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:investigationScope', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    resource_pooling: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:resourcePooling', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    shared_command: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:sharedCommand', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    unified_reporting: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:unifiedReporting', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})


@dataclass
class JointOperationsPlan(CoordinationAgreement):
    """Detailed operational plan for joint investigations and coordinated activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#JointOperationsPlan"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegalLiaison(LiaisonOfficer):
    """Legal liaison officer handling legal aspects of inter-agency coordination and agreements."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#LegalLiaison"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LiaisonCommunicationChannel(CommunicationProtocol):
    """Communication channels managed through designated liaison officers for inter-agency coordination."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#LiaisonCommunicationChannel"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LocalCoordination(InvestigationCoordination):
    """Coordination activities within local jurisdictions and municipal boundaries."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#LocalCoordination"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MemorandumOfAgreement(CoordinationAgreement):
    """Formal MOA defining specific terms and conditions for inter-agency cooperation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#MemorandumOfAgreement"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MemorandumOfUnderstanding(CoordinationAgreement):
    """Formal MOU establishing framework for ongoing cooperation and coordination between agencies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#MemorandumOfUnderstanding"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MissingChildRescueOperation(_cac_core.InvestigativeAction):
    """Time-boxed, multi-party operation focused on locating missing children/teens at risk of endangerment, exploitation, or harm, and connecting them with appropriate services and supports. Modeled as an i"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#MissingChildRescueOperation"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    cases_in_progress_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:casesInProgressCount', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    children_located_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:childrenLocatedCount', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class MultiAgencyCoordination(InvestigationCoordination):
    """Coordination involving multiple law enforcement agencies at various jurisdictional levels."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#MultiAgencyCoordination"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MultiStateCoordination(InvestigationCoordination):
    """Coordination activities spanning multiple states requiring interstate cooperation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#MultiStateCoordination"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OperationalLiaison(LiaisonOfficer):
    """Operational liaison officer coordinating operational activities and tactical coordination."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#OperationalLiaison"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ParallelInvestigation(InvestigationCoordination):
    """Parallel investigation where multiple agencies investigate related aspects independently while maintaining coordination."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#ParallelInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PersonnelSharing(ResourceSharing):
    """Sharing of specialized personnel including investigators, analysts, technical experts, and support staff."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#PersonnelSharing"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    personnel_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:personnelCount', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    security_clearance: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:securityClearance', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    specialization: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-investigation-coordination:specialization', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PrimaryLiaison(LiaisonOfficer):
    """Primary liaison officer with full authority for inter-agency communication and coordination."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#PrimaryLiaison"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RegionalCoordination(InvestigationCoordination):
    """Coordination activities spanning regional areas and multiple local jurisdictions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#RegionalCoordination"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ResourceUtilizationMetrics(CoordinationMetrics):
    """Metrics measuring efficiency of shared resource utilization and allocation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#ResourceUtilizationMetrics"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ResponseTimeMetrics(CoordinationMetrics):
    """Metrics measuring response times for coordination requests and information sharing."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#ResponseTimeMetrics"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SecondaryLiaison(LiaisonOfficer):
    """Secondary liaison officer providing backup and specialized coordination support."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#SecondaryLiaison"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StateCoordination(InvestigationCoordination):
    """Coordination activities within state boundaries involving state and local agencies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#StateCoordination"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SuspectInformationSharing(InformationSharing):
    """Sharing of suspect-related information including identification, criminal history, and behavioral patterns."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#SuspectInformationSharing"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TaskForceCharter(CoordinationAgreement):
    """Charter document establishing task force structure, authority, and operational parameters."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#TaskForceCharter"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TaskForceCoordination(InvestigationCoordination):
    """Coordination through specialized task forces bringing together personnel from multiple agencies for specific operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#TaskForceCoordination"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TechnicalDataSharing(InformationSharing):
    """Sharing of technical data including forensic tools, methodologies, and technical analysis results."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#TechnicalDataSharing"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TechnicalLiaison(LiaisonOfficer):
    """Technical liaison officer specializing in technical coordination and information sharing."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#TechnicalLiaison"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TechnologySharing(ResourceSharing):
    """Sharing of technology resources including software, databases, communication systems, and analytical tools."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#TechnologySharing"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimInformationSharing(InformationSharing):
    """Coordinated sharing of victim information while maintaining privacy and protection protocols."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/investigation-coordination#VictimInformationSharing"
    NAMESPACE_PREFIX: str = "cacontology-investigation-coordination"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
