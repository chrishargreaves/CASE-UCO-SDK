"""CAC Ontology - Crimes Against Children — cacontology_forensics module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional, Union

import case_uco.uco.action as _uco_action
import case_uco.uco.observable as _uco_observable
import case_uco.uco.tool as _uco_tool
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AcquisitionPhase", "AdvancedSearchTechnique", "AnalysisPhase", "AttributionAssessment", "AutomatedContentAnalysis", "BehavioralFingerprinting", "ChainOfCustodyAction", "CommunicationPatternAnalysis", "ContentCorrelationAnalysis", "CorrelationEvidence", "CrossPlatformCorrelation", "CrossReferenceAnalysis", "CustodyDocument", "DatabaseIntelligenceIntegration", "DetectionDogAssist", "DistributedForensicProcessing", "ElectronicStorageDeviceDetection", "EvidenceCustodianRole", "EvidenceTriageSystem", "EvidenceVerificationAction", "ExtendedInvestigationTimeline", "ForensicAcquisitionAction", "ForensicExaminerRole", "ForensicImage", "ForensicImagingTool", "GeospatialCorrelation", "HashingTool", "HiddenDeviceRecovery", "IPCorrelationEvidence", "ImageAnalysisForVictimID", "InternationalEvidenceProcessing", "K9AssistedForensics", "MachineLearningCorrelation", "MassDigitalEvidenceProcessing", "MemoryDump", "MemoryForensicTool", "MetadataCorrelation", "MetadataExtractionAction", "MobileForensicTool", "NetworkCapture", "NetworkForensicTool", "NetworkTrafficAnalysis", "RealTimeCorrelation", "RecoveredFile", "ReportingPhase", "ScalableHashAnalysis", "SubscriberRecordCorrelation", "TemporalPatternAnalysis", "TestimonyPhase", "TimelineAnalysisAction", "UserBehaviorForensics", "VictimIdentificationProcess", "VictimIdentificationSpecialist", "VictimRemovalAction"]


@dataclass
class AcquisitionPhase(_cac_core.Phase):
    """Phase involving forensic acquisition of digital evidence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#AcquisitionPhase"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AdvancedSearchTechnique(_uco_action.Action):
    """Specialized search techniques for locating digital evidence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#AdvancedSearchTechnique"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class AnalysisPhase(_cac_core.Phase):
    """Phase involving detailed forensic analysis of acquired evidence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#AnalysisPhase"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AttributionAssessment(_uco_observable.ObservableObject):
    """Analytic conclusion that two or more observables (accounts, IP addresses, devices) are controlled by the same subject, with stated confidence and method. The assessment is an interpretation layered ov"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#AttributionAssessment"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    attribution_confidence: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:attributionConfidence', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class MassDigitalEvidenceProcessing(_uco_action.Action):
    """Processing of massive volumes of digital evidence requiring specialized automated tools and distributed processing systems (terabytes of data from platforms with millions of users)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#MassDigitalEvidenceProcessing"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    comment: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:comment', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    evidence_volume_terabytes: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:evidenceVolumeTerabytes', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    files_processed_millions: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:filesProcessedMillions', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    processing_timeframe_days: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:processingTimeframeDays', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    start_time_uco_core: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class AutomatedContentAnalysis(MassDigitalEvidenceProcessing):
    """Automated analysis of large volumes of content using machine learning and AI for rapid classification and triage."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#AutomatedContentAnalysis"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    automation_percentage: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:automationPercentage', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    false_positive_rate: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:falsePositiveRate', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    processing_speed: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:processingSpeed', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class UserBehaviorForensics(MassDigitalEvidenceProcessing):
    """Forensic analysis of user behavior patterns across massive user databases for investigation prioritization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#UserBehaviorForensics"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class BehavioralFingerprinting(UserBehaviorForensics):
    """Analysis creating unique behavioral fingerprints from user activities to identify individuals across platforms."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#BehavioralFingerprinting"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ChainOfCustodyAction(_cac_core.InvestigativeAction):
    """An action that documents evidence handling, transfer, and custody maintaining legal admissibility."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#ChainOfCustodyAction"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_end_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasEndPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    custody_integrity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:custodyIntegrity', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    custody_reason: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:custodyReason', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    custody_transferred_from: Optional[UcoObject] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:custodyTransferredFrom', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/core/UcoObject', 'alternate_range_iris': []})
    custody_transferred_to: Optional[UcoObject] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:custodyTransferredTo', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/core/UcoObject', 'alternate_range_iris': []})
    start_time_uco_core: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class CommunicationPatternAnalysis(UserBehaviorForensics):
    """Analysis of communication patterns to identify relationships and networks."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#CommunicationPatternAnalysis"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ContentCorrelationAnalysis(AutomatedContentAnalysis):
    """Analysis correlating content across multiple users and platforms for identifying networks and relationships."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#ContentCorrelationAnalysis"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CorrelationEvidence(_uco_observable.ObservableObject):
    """Structured evidence that observables are linked by overlapping usage, records, or artifacts. Superclass for typed correlation evidence supporting attribution assessments."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#CorrelationEvidence"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    correlation_method: list[str] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-forensics:correlationMethod', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    correlation_time_window_end: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:correlationTimeWindowEnd', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    correlation_time_window_start: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:correlationTimeWindowStart', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class CrossPlatformCorrelation(ContentCorrelationAnalysis):
    """Analysis correlating evidence across multiple platforms and services to identify coordinated criminal activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#CrossPlatformCorrelation"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    uses_tool: list[Tool] = field(default_factory=list, metadata={'jsonld_key': 'uco-action:usesTool', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/tool/Tool', 'alternate_range_iris': []})


@dataclass
class VictimIdentificationProcess(_cac_core.InvestigativeAction):
    """Systematic process for identifying child victims from seized images and videos during long-term investigations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#VictimIdentificationProcess"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    victim_age_range: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:victimAgeRange', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    victim_geographic_origin: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:victimGeographicOrigin', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    victims_identified_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:victimsIdentifiedCount', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    start_time_uco_core: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class CrossReferenceAnalysis(VictimIdentificationProcess):
    """Cross-referencing of digital evidence across multiple cases and international databases for victim identification."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#CrossReferenceAnalysis"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CustodyDocument(_uco_observable.ObservableObject):
    """Documentation recording the handling and transfer of evidence maintaining chain of custody."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#CustodyDocument"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    document_status: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:documentStatus', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    document_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:documentType', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class DatabaseIntelligenceIntegration(MassDigitalEvidenceProcessing):
    """Integration and correlation against multiple international databases and intelligence sources."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#DatabaseIntelligenceIntegration"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DetectionDogAssist(_uco_action.Action):
    """Assistance provided by trained detection dogs in forensic searches."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#DetectionDogAssist"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class DistributedForensicProcessing(MassDigitalEvidenceProcessing):
    """Forensic processing distributed across multiple systems and locations for handling massive evidence volumes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#DistributedForensicProcessing"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ElectronicStorageDeviceDetection(_uco_action.Action):
    """Specialized detection of electronic storage devices using K9 or advanced scanning methods."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#ElectronicStorageDeviceDetection"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    detection_accuracy: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:detectionAccuracy', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    detection_method: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:detectionMethod', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class EvidenceCustodianRole(_cac_core.Role):
    """Role of a person responsible for evidence custody and security."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#EvidenceCustodianRole"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_end_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasEndPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    access_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:accessLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    custody_authority: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:custodyAuthority', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class EvidenceTriageSystem(AutomatedContentAnalysis):
    """Automated system for triaging massive evidence volumes to prioritize high-value targets and critical cases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#EvidenceTriageSystem"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    priority_classification: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:priorityClassification', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    triage_accuracy: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:triageAccuracy', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class EvidenceVerificationAction(_cac_core.InvestigativeAction):
    """The action of verifying evidence integrity using cryptographic hashes and comparison methods."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#EvidenceVerificationAction"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    verification_hash: list[UcoObject] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-forensics:verificationHash', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/core/UcoObject', 'alternate_range_iris': []})
    verification_method: list[str] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-forensics:verificationMethod', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    verification_result: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:verificationResult', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    uses_tool: Optional[Tool] = field(default=None, metadata={'jsonld_key': 'uco-action:usesTool', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/tool/Tool', 'alternate_range_iris': []})
    object_uco_core: list[UcoObject] = field(default_factory=list, metadata={'jsonld_key': 'uco-core:object', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/core/UcoObject', 'alternate_range_iris': []})
    start_time_uco_core: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class TimelineAnalysisAction(_cac_core.InvestigativeAction):
    """The action of creating chronological sequences of digital artifacts and events for investigation analysis."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#TimelineAnalysisAction"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    temporal_accuracy: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:temporalAccuracy', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    timeline_event: list[UcoObject] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-forensics:timelineEvent', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/core/UcoObject', 'alternate_range_iris': []})
    timeline_scope: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:timelineScope', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    uses_tool: list[Tool] = field(default_factory=list, metadata={'jsonld_key': 'uco-action:usesTool', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/tool/Tool', 'alternate_range_iris': []})


@dataclass
class ExtendedInvestigationTimeline(TimelineAnalysisAction):
    """Investigation timeline spanning weeks, months, or years for complex child exploitation cases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#ExtendedInvestigationTimeline"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ForensicAcquisitionAction(_cac_core.InvestigativeAction):
    """The action of creating a forensically sound copy of digital evidence using write-blocking and verification procedures."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#ForensicAcquisitionAction"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_end_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasEndPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    comment: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:comment', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    acquisition_completeness: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:acquisitionCompleteness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    acquisition_method: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:acquisitionMethod', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    acquisition_quality: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:acquisitionQuality', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    evidence_seized: list[UcoObject] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-forensics:evidenceSeized', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/core/UcoObject', 'alternate_range_iris': []})
    forensic_copy: list[ForensicImage] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-forensics:forensicCopy', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org/forensics#ForensicImage', 'alternate_range_iris': []})
    write_blocking_used: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:writeBlockingUsed', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    uses_tool: list[Tool] = field(default_factory=list, metadata={'jsonld_key': 'uco-action:usesTool', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/tool/Tool', 'alternate_range_iris': []})
    end_time_uco_core: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:endTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    start_time_uco_core: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class ForensicExaminerRole(_cac_core.Role):
    """Role of a person conducting digital forensic examination and analysis."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#ForensicExaminerRole"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_end_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasEndPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    certification_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:certificationLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    specialization_area: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:specializationArea', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ForensicImage(_uco_observable.Image):
    """A bit-for-bit copy of digital media created using forensically sound methods, maintaining evidence integrity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#ForensicImage"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    comment: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:comment', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    acquisition_method: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:acquisitionMethod', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    compression_used: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:compressionUsed', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    image_format: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:imageFormat', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    image_integrity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:imageIntegrity', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    source_hash: list[UcoObject] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-forensics:sourceHash', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/core/UcoObject', 'alternate_range_iris': []})
    verification_hash: list[UcoObject] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-forensics:verificationHash', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/core/UcoObject', 'alternate_range_iris': []})
    write_blocking_used: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:writeBlockingUsed', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    size_in_bytes: Optional[float] = field(default=None, metadata={'jsonld_key': 'uco-core:sizeInBytes', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class ForensicImagingTool(_uco_tool.AnalyticTool):
    """A tool specialized for creating forensic images of digital media using write-blocking and verification methods (e.g., FTK Imager, dd, Guymager, PALADIN)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#ForensicImagingTool"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    tool_reliability: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:toolReliability', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    tool_version: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:toolVersion', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    validation_status: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:validationStatus', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class GeospatialCorrelation(ContentCorrelationAnalysis):
    """Correlation analysis based on geographic and location data from multiple sources."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#GeospatialCorrelation"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HashingTool(_uco_tool.AnalyticTool):
    """A tool specialized for generating cryptographic hashes for evidence verification (e.g., hashdeep, md5deep, NIST NSRL)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#HashingTool"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    tool_reliability: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:toolReliability', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    tool_version: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:toolVersion', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    validation_status: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:validationStatus', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class HiddenDeviceRecovery(ForensicAcquisitionAction):
    """Recovery of concealed or hidden electronic storage devices during search operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#HiddenDeviceRecovery"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    devices_recovered: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:devicesRecovered', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class IPCorrelationEvidence(CorrelationEvidence):
    """Structured evidence of overlapping IP usage across accounts, sessions, or platforms within a date-time scope (e.g., 13 of 20 platform session IPs matching another platform's access logs for the same s"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#IPCorrelationEvidence"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ImageAnalysisForVictimID(VictimIdentificationProcess):
    """Analysis of seized images to identify and remove child victims from continued exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#ImageAnalysisForVictimID"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    uses_tool: list[Tool] = field(default_factory=list, metadata={'jsonld_key': 'uco-action:usesTool', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/tool/Tool', 'alternate_range_iris': []})


@dataclass
class InternationalEvidenceProcessing(MassDigitalEvidenceProcessing):
    """Processing of evidence collected from international operations requiring coordination across multiple forensic labs."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#InternationalEvidenceProcessing"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class K9AssistedForensics(ForensicAcquisitionAction):
    """Forensic process enhanced by K9 detection capabilities for electronic storage devices."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#K9AssistedForensics"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    k9_assistance_provided: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:k9AssistanceProvided', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})


@dataclass
class MachineLearningCorrelation(ContentCorrelationAnalysis):
    """AI/ML-powered correlation analysis to identify complex patterns not visible through traditional methods."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#MachineLearningCorrelation"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MemoryDump(_uco_observable.ObservableObject):
    """A snapshot of volatile system memory captured for forensic analysis."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#MemoryDump"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class MemoryForensicTool(_uco_tool.AnalyticTool):
    """A tool specialized for analyzing volatile memory dumps (e.g., Volatility, Rekall, MAGNET RAM Capture)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#MemoryForensicTool"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    tool_reliability: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:toolReliability', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    tool_version: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:toolVersion', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    validation_status: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:validationStatus', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class MetadataCorrelation(ContentCorrelationAnalysis):
    """Correlation analysis of metadata across multiple files and platforms."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#MetadataCorrelation"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MetadataExtractionAction(_cac_core.InvestigativeAction):
    """The action of extracting metadata from digital artifacts including EXIF, file system timestamps, and application metadata."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#MetadataExtractionAction"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    extraction_completeness: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:extractionCompleteness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    metadata_types: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:metadataTypes', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    uses_tool: list[Tool] = field(default_factory=list, metadata={'jsonld_key': 'uco-action:usesTool', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/tool/Tool', 'alternate_range_iris': []})
    object_uco_core: list[UcoObject] = field(default_factory=list, metadata={'jsonld_key': 'uco-core:object', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/core/UcoObject', 'alternate_range_iris': []})


@dataclass
class MobileForensicTool(_uco_tool.AnalyticTool):
    """A tool specialized for mobile device forensics including logical and physical extraction (e.g., Cellebrite UFED, MSAB XRY, Oxygen Detective Suite)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#MobileForensicTool"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    tool_reliability: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:toolReliability', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    tool_version: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:toolVersion', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    validation_status: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:validationStatus', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class NetworkCapture(_uco_observable.ObservableObject):
    """A capture of network traffic packets for forensic analysis."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#NetworkCapture"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class NetworkForensicTool(_uco_tool.AnalyticTool):
    """A tool specialized for network traffic analysis and packet capture (e.g., Wireshark, NetworkMiner, Xplico)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#NetworkForensicTool"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    tool_reliability: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:toolReliability', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    tool_version: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:toolVersion', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    validation_status: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:validationStatus', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class NetworkTrafficAnalysis(UserBehaviorForensics):
    """Analysis of network traffic patterns to identify suspicious communications and data transfers."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#NetworkTrafficAnalysis"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RealTimeCorrelation(ContentCorrelationAnalysis):
    """Real-time correlation analysis for immediate identification of related evidence and ongoing activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#RealTimeCorrelation"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RecoveredFile(_uco_observable.File):
    """A file recovered from deleted or unallocated space on digital media through forensic analysis techniques."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#RecoveredFile"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    data_integrity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:dataIntegrity', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    recovery_confidence: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:recoveryConfidence', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    recovery_method: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:recoveryMethod', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    file_name: Optional[str] = field(default=None, metadata={'jsonld_key': 'uco-observable:fileName', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    file_path: Optional[str] = field(default=None, metadata={'jsonld_key': 'uco-observable:filePath', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ReportingPhase(_cac_core.Phase):
    """Phase involving preparation of forensic reports and findings."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#ReportingPhase"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ScalableHashAnalysis(AutomatedContentAnalysis):
    """Hash analysis systems capable of processing millions of files against large databases of known illegal content."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#ScalableHashAnalysis"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    hash_database_size: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:hashDatabaseSize', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    hash_matches_found: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-forensics:hashMatchesFound', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class SubscriberRecordCorrelation(CorrelationEvidence):
    """Evidence linking a platform account to carrier or ISP subscriber records (e.g., produced under legal process)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#SubscriberRecordCorrelation"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TemporalPatternAnalysis(ContentCorrelationAnalysis):
    """Analysis of temporal patterns and timing correlations across different pieces of evidence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#TemporalPatternAnalysis"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    end_time_uco_core: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:endTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class TestimonyPhase(_cac_core.Phase):
    """Phase involving expert testimony and courtroom presentation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#TestimonyPhase"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimIdentificationSpecialist(_cac_core.Role):
    """Role of specialist focused on identifying child victims from digital evidence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#VictimIdentificationSpecialist"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimRemovalAction(_cac_core.InvestigativeAction):
    """Action taken to remove identified victims from further harm and exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/forensics#VictimRemovalAction"
    NAMESPACE_PREFIX: str = "cacontology-forensics"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
