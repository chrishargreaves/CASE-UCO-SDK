"""CAC Ontology - Crimes Against Children — cacontology_ai_csam module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional, Union

import case_uco.case.investigation as _case_investigation
import case_uco.uco.tool as _uco_tool
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AIAlteredCSAM", "AICSAMInvestigation", "AIContentDetection", "AIContentGeneration", "AIContentInvestigationSituation", "AIDetectionPhase", "AIDetectionTool", "AIForensicAnalyst", "AIGeneratedCSAM", "AIModelAnalyst", "AgeProgression", "ArtifactAnalysis", "BiometricInconsistencyAnalysis", "ContentGenerationPhase", "CrossPlatformDetectionSituation", "DeepfakeCSAM", "DeepfakeDetection", "DeepfakeDetectionSpecialist", "DeepfakeDetectionTool", "FaceSwapping", "ForensicAnalysisPhase", "GenerationSourceTracking", "HybridCSAM", "ImageGeneration", "MetadataAnalysisTool", "ModelIdentification", "ModelTraining", "Nudification", "NudificationTool", "NudifiedCSAM", "SyntheticImageDetector", "SyntheticMediaAnalysis", "SyntheticMediaCSAM", "SyntheticMediaExaminer", "TechnicalAnalysisSituation", "TrainingDataAnalysis", "VideoGeneration"]


@dataclass
class AIAlteredCSAM(_cac_core.Artifact):
    """Existing CSAM that has been modified using AI techniques to alter appearance, age, or other characteristics. Enhanced as gUFO Object with alteration tracking."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#AIAlteredCSAM"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AICSAMInvestigation(_case_investigation.Investigation):
    """Investigation specifically focused on AI-generated child sexual abuse material, requiring specialized techniques and legal frameworks. Enhanced as gUFO Event for complex investigation modeling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#AICSAMInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    investigation_challenge_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-ai-csam:investigationChallengeLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    legal_framework_challenges: list[str] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-ai-csam:legalFrameworkChallenges', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    prosecution_difficulty: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-ai-csam:prosecutionDifficulty', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    victim_identification_difficulty: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-ai-csam:victimIdentificationDifficulty', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class AIContentDetection(_cac_core.DetectionEvent):
    """Process of identifying AI-generated or AI-altered content to distinguish from authentic material during investigations. Enhanced as gUFO Event for forensic process modeling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#AIContentDetection"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    detection_confidence: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-ai-csam:detectionConfidence', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    detection_method: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-ai-csam:detectionMethod', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    evidence_admissibility: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-ai-csam:evidenceAdmissibility', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    processing_time: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-ai-csam:processingTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    detection_time_point: list[datetime] = field(default_factory=list, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#detectionTimePoint', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class AIContentGeneration(_cac_core.Event):
    """Process of creating artificial CSAM using machine learning models, neural networks, or other AI technologies. Enhanced as gUFO Event for precise temporal and causal modeling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#AIContentGeneration"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    generation_complexity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-ai-csam:generationComplexity', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    generation_technique: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-ai-csam:generationTechnique', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    technical_expertise_required: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-ai-csam:technicalExpertiseRequired', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    generation_duration: Optional[str] = field(default=None, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#generationDuration', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#duration', 'alternate_range_iris': []})
    end_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:endTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class AIContentInvestigationSituation(_cac_core.Situation):
    """Complex situation involving multiple stakeholders, technologies, and legal frameworks for investigating AI-generated CSAM."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#AIContentInvestigationSituation"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AIDetectionPhase(_cac_core.Phase):
    """Anti-rigid phase during which AI-generated content undergoes detection and analysis processes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#AIDetectionPhase"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    begin_time_point: list[datetime] = field(default_factory=list, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#beginTimePoint', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class AIDetectionTool(_uco_tool.AnalyticTool):
    """Software tool specialized for detecting AI-generated content in digital media. Enhanced as gUFO Object for tool modeling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#AIDetectionTool"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    false_positive_rate: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-ai-csam:falsePositiveRate', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class AIForensicAnalyst(_cac_core.Role):
    """Anti-rigid role of specialist analyzing AI-generated content for authenticity and generation methods."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#AIForensicAnalyst"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AIGeneratedCSAM(_cac_core.Artifact):
    """Child sexual abuse material fully generated by artificial intelligence without depicting real victims, but still contributing to objectification and sexualization of children. Enhanced as gUFO Object """

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#AIGeneratedCSAM"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    ai_model_used: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-ai-csam:aiModelUsed', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    artificialness_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-ai-csam:artificialnessLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    real_victim_depicted: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-ai-csam:realVictimDepicted', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    rendering_quality: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-ai-csam:renderingQuality', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    creation_time_point: list[datetime] = field(default_factory=list, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#creationTimePoint', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class AIModelAnalyst(AIForensicAnalyst):
    """Anti-rigid role of specialist identifying and analyzing AI models used for content generation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#AIModelAnalyst"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AgeProgression(AIContentGeneration):
    """AI technique for artificially aging or de-aging subjects in content, potentially creating illegal material from legal content. Enhanced as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#AgeProgression"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SyntheticMediaAnalysis(AIContentDetection):
    """Forensic analysis of media to determine if it was artificially generated and identify generation techniques used. Enhanced as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#SyntheticMediaAnalysis"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    analysis_completion_time_point: list[datetime] = field(default_factory=list, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#analysisCompletionTimePoint', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    performer: Optional[Person] = field(default=None, metadata={'jsonld_key': 'uco-action:performer', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/identity/Person', 'alternate_range_iris': []})


@dataclass
class ArtifactAnalysis(SyntheticMediaAnalysis):
    """Analysis of digital artifacts and inconsistencies that may indicate AI generation, such as compression patterns or noise characteristics. Enhanced as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#ArtifactAnalysis"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class BiometricInconsistencyAnalysis(SyntheticMediaAnalysis):
    """Analysis of biometric inconsistencies in AI-generated content, such as unnatural eye movements or facial feature distortions. Enhanced as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#BiometricInconsistencyAnalysis"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ContentGenerationPhase(_cac_core.Phase):
    """Anti-rigid phase during which AI systems generate illegal content."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#ContentGenerationPhase"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CrossPlatformDetectionSituation(AIContentInvestigationSituation):
    """Situation involving detection and analysis of AI-generated content across multiple platforms and technologies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#CrossPlatformDetectionSituation"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DeepfakeCSAM(AIAlteredCSAM):
    """CSAM created by using AI to alter genuine content, potentially making real victims appear in fabricated scenarios or altering existing abuse material. Enhanced as gUFO Object with manipulation trackin"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#DeepfakeCSAM"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    manipulation_time_point: list[datetime] = field(default_factory=list, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#manipulationTimePoint', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class DeepfakeDetection(AIContentDetection):
    """Specialized analysis for detecting deepfake technology use in content, including face replacement and manipulation. Enhanced as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#DeepfakeDetection"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DeepfakeDetectionSpecialist(AIForensicAnalyst):
    """Anti-rigid role of specialist focused on detecting and analyzing deepfake technology use."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#DeepfakeDetectionSpecialist"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DeepfakeDetectionTool(AIDetectionTool):
    """Tool specifically designed to identify deepfake content and face manipulation techniques. Enhanced as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#DeepfakeDetectionTool"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FaceSwapping(AIContentGeneration):
    """AI technique for replacing faces in existing content with different faces, potentially placing victims in abusive scenarios. Enhanced as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#FaceSwapping"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ForensicAnalysisPhase(_cac_core.Phase):
    """Anti-rigid phase during which AI-generated content undergoes detailed forensic examination."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#ForensicAnalysisPhase"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class GenerationSourceTracking(_cac_core.InvestigativeAction):
    """Investigation process to identify the source, tools, and methods used to generate AI-CSAM. Enhanced as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#GenerationSourceTracking"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HybridCSAM(AIGeneratedCSAM):
    """Content combining real and AI-generated elements, making it difficult to distinguish between authentic and artificial material. Enhanced as gUFO Object with composition modeling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#HybridCSAM"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ImageGeneration(AIContentGeneration):
    """Generation of static images using AI models such as diffusion models, GANs, or other generative techniques. Enhanced as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#ImageGeneration"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MetadataAnalysisTool(AIDetectionTool):
    """Tool for analyzing metadata patterns that may indicate AI generation or manipulation. Enhanced as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#MetadataAnalysisTool"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ModelIdentification(_cac_core.InvestigativeAction):
    """Process of identifying the specific AI model or algorithm used to generate illegal content. Enhanced as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#ModelIdentification"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ModelTraining(AIContentGeneration):
    """Process of training AI models on datasets that may include illegal content for the purpose of generating new CSAM. Enhanced as gUFO Event with training phases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#ModelTraining"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Nudification(AIContentGeneration):
    """AI content generation/manipulation process that produces synthetic nudity (e.g., 'nudifying apps' / nudifying functionalities) from existing media. Modeled as a gUFO Event and UCO Action."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#Nudification"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    nudification_technique: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-ai-csam:nudificationTechnique', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class NudificationTool(_uco_tool.Tool):
    """Software tool or functionality capable of performing AI-enabled nudification (synthetic nudity) of existing media."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#NudificationTool"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class NudifiedCSAM(AIAlteredCSAM):
    """Child sexual abuse material created by AI-enabled nudification (synthetic nudity) of an existing image or video. This models 'nudifying functionalities' discussed in policy contexts."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#NudifiedCSAM"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SyntheticImageDetector(AIDetectionTool):
    """Tool for detecting synthetically generated images using machine learning classifiers. Enhanced as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#SyntheticImageDetector"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SyntheticMediaCSAM(AIGeneratedCSAM):
    """Completely synthetic media generated using AI models trained on large datasets, creating realistic but artificial depictions. Enhanced as gUFO Object for synthetic media modeling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#SyntheticMediaCSAM"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SyntheticMediaExaminer(AIForensicAnalyst):
    """Anti-rigid role of expert examining synthetic media for forensic artifacts and generation signatures."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#SyntheticMediaExaminer"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TechnicalAnalysisSituation(AIContentInvestigationSituation):
    """Situation requiring coordination between technical experts, forensic analysts, and legal teams for AI content analysis."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#TechnicalAnalysisSituation"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TrainingDataAnalysis(_cac_core.InvestigativeAction):
    """Analysis of datasets potentially used to train AI models for generating illegal content. Enhanced as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#TrainingDataAnalysis"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VideoGeneration(AIContentGeneration):
    """Generation of video content using AI models capable of creating temporal sequences and motion. Enhanced as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/ai-csam#VideoGeneration"
    NAMESPACE_PREFIX: str = "cacontology-ai-csam"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
