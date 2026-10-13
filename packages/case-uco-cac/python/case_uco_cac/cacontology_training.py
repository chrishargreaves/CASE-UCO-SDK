"""CAC Ontology - Crimes Against Children — cacontology_training module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional, Union

import case_uco.uco.identity as _uco_identity
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AssessmentPhase", "CapacityBuildingPartner", "CapacityBuildingProgram", "CapacityBuildingSituation", "CertificationBody", "CertificationPhase", "CertifiedProfessional", "ChildProtectionTraining", "CommunityEducationTraining", "CompetencyAssessment", "ContentDevelopmentPhase", "ContinuingEducation", "CriminalJusticeTraining", "DigitalForensicsTraining", "GlobalTrainingSituation", "HotlineTraining", "HybridTraining", "InPersonTraining", "InternationalTrainer", "InternationalTraining", "InvestigationTraining", "JudicialEducationTraining", "LegalTraining", "MentorshipProgram", "MultiStakeholderTrainingSituation", "OnlineTraining", "ProfessionalCertification", "ProfessionalDevelopment", "ProgramPlanningPhase", "RecantationResponseTraining", "SkillsDevelopmentProgram", "SkillsValidation", "SubjectMatterExpert", "TrainingCertificate", "TrainingCoordinator", "TrainingCurriculum", "TrainingDeliveryPhase", "TrainingInstitution", "TrainingMetrics", "TrainingModule", "TrainingParticipant", "VictimServiceTraining"]


@dataclass
class AssessmentPhase(_cac_core.Phase):
    """Phase of participant assessment and competency evaluation. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#AssessmentPhase"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CapacityBuildingPartner(_uco_identity.Organization):
    """Partner organization supporting capacity building efforts. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#CapacityBuildingPartner"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CapacityBuildingProgram(_cac_core.OrganizationLikeEntity):
    """Structured program for building organizational and individual capacity. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#CapacityBuildingProgram"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    capacity_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-training:capacityLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class CapacityBuildingSituation(_cac_core.Situation):
    """Situation focused on building institutional and individual capacity for child protection. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#CapacityBuildingSituation"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CertificationBody(_uco_identity.Organization):
    """Organization responsible for professional certification. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#CertificationBody"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CertificationPhase(_cac_core.Phase):
    """Phase of awarding certifications and credentials. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#CertificationPhase"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CertifiedProfessional(_cac_core.Role):
    """Professional who has achieved certification. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#CertifiedProfessional"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InternationalTraining(_cac_core.SupportEvent):
    """Training program conducted across multiple countries. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#InternationalTraining"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    completion_rate: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-training:completionRate', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    participation_rate: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-training:participationRate', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    training_duration: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-training:trainingDuration', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    training_language: list[str] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-training:trainingLanguage', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    training_reach_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-training:trainingReachCount', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    end_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:endTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    modified_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:modifiedTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    name: Optional[str] = field(default=None, metadata={'jsonld_key': 'uco-core:name', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class ChildProtectionTraining(InternationalTraining):
    """Training focused on child protection methodologies. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#ChildProtectionTraining"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CommunityEducationTraining(ChildProtectionTraining):
    """Training designed to educate community members and caregivers about child abuse dynamics, disclosure support, and prevention awareness."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#CommunityEducationTraining"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CompetencyAssessment(_cac_core.AssessmentResult):
    """Assessment of professional competencies acquired through training. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#CompetencyAssessment"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    competency_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-training:competencyLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ContentDevelopmentPhase(_cac_core.Phase):
    """Phase of developing training content and materials. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#ContentDevelopmentPhase"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ContinuingEducation(CapacityBuildingProgram):
    """Ongoing education for certified professionals. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#ContinuingEducation"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CriminalJusticeTraining(InternationalTraining):
    """Training for criminal justice professionals on child protection. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#CriminalJusticeTraining"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    capacity_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-training:capacityLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class DigitalForensicsTraining(InternationalTraining):
    """Training on digital forensics techniques for child protection cases. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#DigitalForensicsTraining"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    capacity_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-training:capacityLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class GlobalTrainingSituation(_cac_core.Situation):
    """Situation involving global training initiatives across multiple countries and organizations. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#GlobalTrainingSituation"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HotlineTraining(InternationalTraining):
    """Training for hotline operators and managers. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#HotlineTraining"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HybridTraining(InternationalTraining):
    """Training combining online and in-person delivery. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#HybridTraining"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InPersonTraining(InternationalTraining):
    """Training delivered in physical classroom settings. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#InPersonTraining"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InternationalTrainer(_cac_core.Role):
    """Trainer delivering international training programs. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#InternationalTrainer"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InvestigationTraining(InternationalTraining):
    """Training on investigation methodologies and techniques. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#InvestigationTraining"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegalTraining(InternationalTraining):
    """Training on legal aspects of child protection. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#LegalTraining"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    capacity_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-training:capacityLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class JudicialEducationTraining(LegalTraining):
    """Training focused on judicial understanding of trauma, recantation, and accommodation needs in child abuse cases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#JudicialEducationTraining"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MentorshipProgram(CapacityBuildingProgram):
    """One-on-one mentorship for professional development. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#MentorshipProgram"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    training_reach_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-training:trainingReachCount', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class MultiStakeholderTrainingSituation(_cac_core.Situation):
    """Situation involving training coordination between multiple stakeholder organizations. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#MultiStakeholderTrainingSituation"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OnlineTraining(InternationalTraining):
    """Training delivered through online platforms. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#OnlineTraining"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProfessionalCertification(_cac_core.Artifact):
    """Formal certification for child protection professionals. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#ProfessionalCertification"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    certification_status: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-training:certificationStatus', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    certification_validity_period: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-training:certificationValidityPeriod', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class ProfessionalDevelopment(_cac_core.EnduringEntity):
    """Career development for child protection professionals. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#ProfessionalDevelopment"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProgramPlanningPhase(_cac_core.Phase):
    """Phase of training program planning and curriculum development. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#ProgramPlanningPhase"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimServiceTraining(InternationalTraining):
    """Training for professionals providing victim services. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#VictimServiceTraining"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RecantationResponseTraining(VictimServiceTraining):
    """Training for multidisciplinary teams on anticipating recantation, strengthening support, and investigating statement change."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#RecantationResponseTraining"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    capacity_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-training:capacityLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SkillsDevelopmentProgram(CapacityBuildingProgram):
    """Program focused on developing specific professional skills. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#SkillsDevelopmentProgram"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SkillsValidation(_cac_core.AssessmentResult):
    """Validation of skills acquired through training programs. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#SkillsValidation"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    skills_acquired: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-training:skillsAcquired', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SubjectMatterExpert(_cac_core.Role):
    """Expert providing specialized knowledge in training. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#SubjectMatterExpert"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TrainingCertificate(_cac_core.Artifact):
    """Certificate awarded upon successful completion of training. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#TrainingCertificate"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TrainingCoordinator(_cac_core.Role):
    """Coordinator responsible for organizing training programs. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#TrainingCoordinator"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TrainingCurriculum(_cac_core.Artifact):
    """Structured curriculum for child protection training. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#TrainingCurriculum"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TrainingDeliveryPhase(_cac_core.Phase):
    """Phase of active training delivery and instruction. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#TrainingDeliveryPhase"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TrainingInstitution(_uco_identity.Organization):
    """Institution providing child protection training. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#TrainingInstitution"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class TrainingMetrics(_cac_core.AssessmentResult):
    """Metrics measuring training effectiveness and reach. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#TrainingMetrics"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class TrainingModule(_cac_core.Artifact):
    """Individual training module covering specific topics. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#TrainingModule"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TrainingParticipant(_cac_core.Role):
    """Professional participating in training programs. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#TrainingParticipant"
    NAMESPACE_PREFIX: str = "cacontology-training"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
