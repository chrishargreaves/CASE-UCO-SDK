"""CAC Ontology - Crimes Against Children — cacontology_detection module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional, Union

import case_uco.uco.tool as _uco_tool
import case_uco.uco.types as _uco_types
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AutomatedDetectionAction", "ClassificationResult", "ContentAnalystRole", "ContentHashingAction", "ContentHashingTool", "CrossPlatformDetectionSituation", "DatabaseMatchAction", "DatabaseMatchingTool", "DetectionResult", "FalsePositiveAnalysisAction", "FalsePositiveManagementSituation", "HashAnalystRole", "HashComparisonPhase", "InitialDetectionPhase", "MachineLearningDetectionTool", "MachineLearningSpecialistRole", "ManualClassificationAction", "ManualReviewPhase", "ManualReviewTool", "MassContentAnalysisSituation", "PerceptualHash", "PhotoDNAHash", "QualityAssuranceAnalystRole", "ReportingPhase", "RiskStratificationAction", "RiskStratificationResult", "ValidationPhase"]


@dataclass
class AutomatedDetectionAction(_cac_core.DetectionEvent):
    """The action of using automated systems to detect potential CSAM content. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#AutomatedDetectionAction"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    confidence_score: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:confidenceScore', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    has_detection_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasDetectionBeginPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_detection_end_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasDetectionEndPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    instrument: Optional[MachineLearningDetectionTool] = field(default=None, metadata={'jsonld_key': 'uco-action:instrument', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://cacontology.projectvic.org/detection#MachineLearningDetectionTool', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class ClassificationResult(_cac_core.AssessmentResult):
    """The result of content classification using standard scales like SAR or COPINE."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#ClassificationResult"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    age_estimate: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:ageEstimate', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#integer', 'alternate_range_iris': []})
    tanner_stage: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:tannerStage', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#integer', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class ContentAnalystRole(_cac_core.Role):
    """Role of professional analyzing flagged content for classification. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#ContentAnalystRole"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_role_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasRoleBeginPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_role_end_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasRoleEndPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class ContentHashingAction(_cac_core.DetectionEvent):
    """The action of generating cryptographic or perceptual hashes for content identification and matching. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#ContentHashingAction"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_detection_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasDetectionBeginPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_detection_end_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasDetectionEndPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    instrument: Optional[ContentHashingTool] = field(default=None, metadata={'jsonld_key': 'uco-action:instrument', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://cacontology.projectvic.org/detection#ContentHashingTool', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class ContentHashingTool(_uco_tool.AnalyticTool):
    """A tool for generating perceptual or cryptographic hashes for content matching (e.g., PhotoDNA, pHash, MD5). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#ContentHashingTool"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CrossPlatformDetectionSituation(_cac_core.Situation):
    """Situation involving detection across multiple platforms and services. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#CrossPlatformDetectionSituation"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DatabaseMatchAction(_cac_core.DetectionEvent):
    """The action of comparing content against known CSAM hash databases. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#DatabaseMatchAction"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_detection_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasDetectionBeginPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_detection_end_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasDetectionEndPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class DatabaseMatchingTool(_uco_tool.AnalyticTool):
    """A tool for matching content against known CSAM databases (e.g., NCMEC hash database, INTERPOL ICSE database). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#DatabaseMatchingTool"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class DetectionResult(_cac_core.AssessmentResult):
    """The result of a content detection action including confidence scores and classification."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#DetectionResult"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    confidence_score: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:confidenceScore', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class FalsePositiveAnalysisAction(_cac_core.DetectionEvent):
    """The action of analyzing and documenting false positive detections to improve accuracy. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#FalsePositiveAnalysisAction"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_detection_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasDetectionBeginPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_detection_end_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasDetectionEndPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class FalsePositiveManagementSituation(_cac_core.Situation):
    """Situation focused on managing and reducing false positive detection rates. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#FalsePositiveManagementSituation"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HashAnalystRole(_cac_core.Role):
    """Role of specialist working with hash databases and matching systems. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#HashAnalystRole"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_role_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasRoleBeginPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_role_end_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasRoleEndPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class HashComparisonPhase(_cac_core.Phase):
    """Phase of comparing content hashes against known databases. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#HashComparisonPhase"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_phase_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasPhaseBeginPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_phase_end_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasPhaseEndPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class InitialDetectionPhase(_cac_core.Phase):
    """Phase of initial automated content detection and flagging. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#InitialDetectionPhase"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_phase_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasPhaseBeginPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_phase_end_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasPhaseEndPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class MachineLearningDetectionTool(_uco_tool.AnalyticTool):
    """A tool using machine learning algorithms to detect CSAM content (e.g., Google's CSAI Classifier, Facebook's neural networks). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#MachineLearningDetectionTool"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    detection_threshold: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:detectionThreshold', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    model_version: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:modelVersion', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class MachineLearningSpecialistRole(_cac_core.Role):
    """Role of specialist developing and maintaining ML detection systems. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#MachineLearningSpecialistRole"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_role_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasRoleBeginPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_role_end_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasRoleEndPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class ManualClassificationAction(_cac_core.DetectionEvent):
    """The action of human review and classification of suspected CSAM content. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#ManualClassificationAction"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_detection_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasDetectionBeginPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_detection_end_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasDetectionEndPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    review_decision: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:reviewDecision', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    performer: Optional[Person] = field(default=None, metadata={'jsonld_key': 'uco-action:performer', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/identity/Person', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class ManualReviewPhase(_cac_core.Phase):
    """Phase of human expert review and classification. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#ManualReviewPhase"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_phase_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasPhaseBeginPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_phase_end_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasPhaseEndPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class ManualReviewTool(_uco_tool.AnalyticTool):
    """A tool supporting human review and classification of potentially illegal content. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#ManualReviewTool"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class MassContentAnalysisSituation(_cac_core.Situation):
    """Situation involving analysis of large volumes of content requiring coordinated detection systems. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#MassContentAnalysisSituation"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PerceptualHash(_uco_types.Hash):
    """A hash that captures visual similarity rather than exact bit patterns (e.g., pHash, aHash, dHash). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#PerceptualHash"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    hash_algorithm: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hashAlgorithm', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    perceptual_hash_value: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:perceptualHashValue', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class PhotoDNAHash(_uco_types.Hash):
    """A Microsoft PhotoDNA hash for robust image matching that survives common transformations. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#PhotoDNAHash"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    photo_dna_value: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:photoDNAValue', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class QualityAssuranceAnalystRole(_cac_core.Role):
    """Role focused on validating detection accuracy and managing quality metrics. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#QualityAssuranceAnalystRole"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_role_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasRoleBeginPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_role_end_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasRoleEndPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class ReportingPhase(_cac_core.Phase):
    """Phase of generating reports and notifications to authorities. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#ReportingPhase"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_phase_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasPhaseBeginPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_phase_end_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasPhaseEndPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class RiskStratificationAction(_cac_core.DetectionEvent):
    """The action of producing a risk-stratified assessment to prioritize downstream review and operational response beyond raw detection flags (e.g., risk-tiering, scoring, rationale)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#RiskStratificationAction"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_detection_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasDetectionBeginPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_detection_end_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasDetectionEndPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class RiskStratificationResult(_cac_core.AssessmentResult):
    """A risk-stratified output artifact (tier/score/rationale) produced from detection or tip signals to support explainable prioritization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#RiskStratificationResult"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    risk_rationale: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:riskRationale', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    risk_score: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:riskScore', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    risk_tier: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:riskTier', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ValidationPhase(_cac_core.Phase):
    """Phase of validating detection results and reducing false positives. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/detection#ValidationPhase"
    NAMESPACE_PREFIX: str = "cacontology-detection"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_phase_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasPhaseBeginPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_phase_end_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-detection:hasPhaseEndPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
