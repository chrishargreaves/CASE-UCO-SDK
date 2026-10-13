"""CAC Ontology - Crimes Against Children — cacontology-training module."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AssessmentPhase:
    """Phase of participant assessment and competency evaluation. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#AssessmentPhase"


@dataclass
class CapacityBuildingPartner:
    """Partner organization supporting capacity building efforts. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#CapacityBuildingPartner"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)


@dataclass
class CapacityBuildingProgram:
    """Structured program for building organizational and individual capacity. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#CapacityBuildingProgram"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: Optional[datetime] = field(default=None)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    capacity_level: Optional[str] = field(default=None)
    created_time: Optional[datetime] = field(default=None)


@dataclass
class CapacityBuildingSituation:
    """Situation focused on building institutional and individual capacity for child protection. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#CapacityBuildingSituation"


@dataclass
class CertificationBody:
    """Organization responsible for professional certification. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#CertificationBody"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)


@dataclass
class CertificationPhase:
    """Phase of awarding certifications and credentials. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#CertificationPhase"


@dataclass
class CertifiedProfessional:
    """Professional who has achieved certification. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#CertifiedProfessional"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)


@dataclass
class ChildProtectionTraining:
    """Training focused on child protection methodologies. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#ChildProtectionTraining"
    completion_rate: Optional[float] = field(default=None)
    participation_rate: Optional[float] = field(default=None)
    training_duration: Optional[float] = field(default=None)
    training_language: list[str] = field(default_factory=list)
    training_reach_count: Optional[int] = field(default=None)
    created_time: Optional[datetime] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    modified_time: Optional[datetime] = field(default=None)
    name: Optional[str] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class CommunityEducationTraining:
    """Training designed to educate community members and caregivers about child abuse dynamics, disclosure support, and prevention awareness."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#CommunityEducationTraining"
    completion_rate: Optional[float] = field(default=None)
    participation_rate: Optional[float] = field(default=None)
    training_duration: Optional[float] = field(default=None)
    training_language: list[str] = field(default_factory=list)
    training_reach_count: Optional[int] = field(default=None)
    created_time: Optional[datetime] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    modified_time: Optional[datetime] = field(default=None)
    name: Optional[str] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class CompetencyAssessment:
    """Assessment of professional competencies acquired through training. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#CompetencyAssessment"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    competency_level: Optional[str] = field(default=None)


@dataclass
class ContentDevelopmentPhase:
    """Phase of developing training content and materials. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#ContentDevelopmentPhase"


@dataclass
class ContinuingEducation:
    """Ongoing education for certified professionals. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#ContinuingEducation"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: Optional[datetime] = field(default=None)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    capacity_level: Optional[str] = field(default=None)
    created_time: Optional[datetime] = field(default=None)


@dataclass
class CriminalJusticeTraining:
    """Training for criminal justice professionals on child protection. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#CriminalJusticeTraining"
    completion_rate: Optional[float] = field(default=None)
    participation_rate: Optional[float] = field(default=None)
    training_duration: Optional[float] = field(default=None)
    training_language: list[str] = field(default_factory=list)
    training_reach_count: Optional[int] = field(default=None)
    created_time: Optional[datetime] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    modified_time: Optional[datetime] = field(default=None)
    name: Optional[str] = field(default=None)
    start_time: Optional[datetime] = field(default=None)
    capacity_level: Optional[str] = field(default=None)


@dataclass
class DigitalForensicsTraining:
    """Training on digital forensics techniques for child protection cases. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#DigitalForensicsTraining"
    completion_rate: Optional[float] = field(default=None)
    participation_rate: Optional[float] = field(default=None)
    training_duration: Optional[float] = field(default=None)
    training_language: list[str] = field(default_factory=list)
    training_reach_count: Optional[int] = field(default=None)
    created_time: Optional[datetime] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    modified_time: Optional[datetime] = field(default=None)
    name: Optional[str] = field(default=None)
    start_time: Optional[datetime] = field(default=None)
    capacity_level: Optional[str] = field(default=None)


@dataclass
class GlobalTrainingSituation:
    """Situation involving global training initiatives across multiple countries and organizations. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#GlobalTrainingSituation"


@dataclass
class HotlineTraining:
    """Training for hotline operators and managers. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#HotlineTraining"
    completion_rate: Optional[float] = field(default=None)
    participation_rate: Optional[float] = field(default=None)
    training_duration: Optional[float] = field(default=None)
    training_language: list[str] = field(default_factory=list)
    training_reach_count: Optional[int] = field(default=None)
    created_time: Optional[datetime] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    modified_time: Optional[datetime] = field(default=None)
    name: Optional[str] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class HybridTraining:
    """Training combining online and in-person delivery. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#HybridTraining"
    completion_rate: Optional[float] = field(default=None)
    participation_rate: Optional[float] = field(default=None)
    training_duration: Optional[float] = field(default=None)
    training_language: list[str] = field(default_factory=list)
    training_reach_count: Optional[int] = field(default=None)
    created_time: Optional[datetime] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    modified_time: Optional[datetime] = field(default=None)
    name: Optional[str] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class InPersonTraining:
    """Training delivered in physical classroom settings. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#InPersonTraining"
    completion_rate: Optional[float] = field(default=None)
    participation_rate: Optional[float] = field(default=None)
    training_duration: Optional[float] = field(default=None)
    training_language: list[str] = field(default_factory=list)
    training_reach_count: Optional[int] = field(default=None)
    created_time: Optional[datetime] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    modified_time: Optional[datetime] = field(default=None)
    name: Optional[str] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class InternationalTrainer:
    """Trainer delivering international training programs. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#InternationalTrainer"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)


@dataclass
class InternationalTraining:
    """Training program conducted across multiple countries. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#InternationalTraining"
    completion_rate: Optional[float] = field(default=None)
    participation_rate: Optional[float] = field(default=None)
    training_duration: Optional[float] = field(default=None)
    training_language: list[str] = field(default_factory=list)
    training_reach_count: Optional[int] = field(default=None)
    created_time: Optional[datetime] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    modified_time: Optional[datetime] = field(default=None)
    name: Optional[str] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class InvestigationTraining:
    """Training on investigation methodologies and techniques. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#InvestigationTraining"
    completion_rate: Optional[float] = field(default=None)
    participation_rate: Optional[float] = field(default=None)
    training_duration: Optional[float] = field(default=None)
    training_language: list[str] = field(default_factory=list)
    training_reach_count: Optional[int] = field(default=None)
    created_time: Optional[datetime] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    modified_time: Optional[datetime] = field(default=None)
    name: Optional[str] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class JudicialEducationTraining:
    """Training focused on judicial understanding of trauma, recantation, and accommodation needs in child abuse cases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#JudicialEducationTraining"
    completion_rate: Optional[float] = field(default=None)
    participation_rate: Optional[float] = field(default=None)
    training_duration: Optional[float] = field(default=None)
    training_language: list[str] = field(default_factory=list)
    training_reach_count: Optional[int] = field(default=None)
    created_time: Optional[datetime] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    modified_time: Optional[datetime] = field(default=None)
    name: Optional[str] = field(default=None)
    start_time: Optional[datetime] = field(default=None)
    capacity_level: Optional[str] = field(default=None)


@dataclass
class LegalTraining:
    """Training on legal aspects of child protection. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#LegalTraining"
    completion_rate: Optional[float] = field(default=None)
    participation_rate: Optional[float] = field(default=None)
    training_duration: Optional[float] = field(default=None)
    training_language: list[str] = field(default_factory=list)
    training_reach_count: Optional[int] = field(default=None)
    created_time: Optional[datetime] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    modified_time: Optional[datetime] = field(default=None)
    name: Optional[str] = field(default=None)
    start_time: Optional[datetime] = field(default=None)
    capacity_level: Optional[str] = field(default=None)


@dataclass
class MentorshipProgram:
    """One-on-one mentorship for professional development. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#MentorshipProgram"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: Optional[datetime] = field(default=None)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    capacity_level: Optional[str] = field(default=None)
    created_time: Optional[datetime] = field(default=None)
    training_reach_count: Optional[int] = field(default=None)


@dataclass
class MultiStakeholderTrainingSituation:
    """Situation involving training coordination between multiple stakeholder organizations. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#MultiStakeholderTrainingSituation"


@dataclass
class OnlineTraining:
    """Training delivered through online platforms. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#OnlineTraining"
    completion_rate: Optional[float] = field(default=None)
    participation_rate: Optional[float] = field(default=None)
    training_duration: Optional[float] = field(default=None)
    training_language: list[str] = field(default_factory=list)
    training_reach_count: Optional[int] = field(default=None)
    created_time: Optional[datetime] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    modified_time: Optional[datetime] = field(default=None)
    name: Optional[str] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class ProfessionalCertification:
    """Formal certification for child protection professionals. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#ProfessionalCertification"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: Optional[datetime] = field(default=None)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    has_changed: Optional[bool] = field(default=None)
    state: Optional[str] = field(default=None)
    certification_status: Optional[str] = field(default=None)
    certification_validity_period: Optional[float] = field(default=None)
    created_time: Optional[datetime] = field(default=None)


@dataclass
class ProfessionalDevelopment:
    """Career development for child protection professionals. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#ProfessionalDevelopment"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)


@dataclass
class ProgramPlanningPhase:
    """Phase of training program planning and curriculum development. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#ProgramPlanningPhase"


@dataclass
class RecantationResponseTraining:
    """Training for multidisciplinary teams on anticipating recantation, strengthening support, and investigating statement change."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#RecantationResponseTraining"
    completion_rate: Optional[float] = field(default=None)
    participation_rate: Optional[float] = field(default=None)
    training_duration: Optional[float] = field(default=None)
    training_language: list[str] = field(default_factory=list)
    training_reach_count: Optional[int] = field(default=None)
    created_time: Optional[datetime] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    modified_time: Optional[datetime] = field(default=None)
    name: Optional[str] = field(default=None)
    start_time: Optional[datetime] = field(default=None)
    capacity_level: Optional[str] = field(default=None)


@dataclass
class SkillsDevelopmentProgram:
    """Program focused on developing specific professional skills. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#SkillsDevelopmentProgram"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: Optional[datetime] = field(default=None)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    capacity_level: Optional[str] = field(default=None)
    created_time: Optional[datetime] = field(default=None)


@dataclass
class SkillsValidation:
    """Validation of skills acquired through training programs. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#SkillsValidation"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    skills_acquired: Optional[str] = field(default=None)


@dataclass
class SubjectMatterExpert:
    """Expert providing specialized knowledge in training. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#SubjectMatterExpert"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)


@dataclass
class TrainingCertificate:
    """Certificate awarded upon successful completion of training. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#TrainingCertificate"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    has_changed: Optional[bool] = field(default=None)
    state: Optional[str] = field(default=None)


@dataclass
class TrainingCoordinator:
    """Coordinator responsible for organizing training programs. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#TrainingCoordinator"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)


@dataclass
class TrainingCurriculum:
    """Structured curriculum for child protection training. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#TrainingCurriculum"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    has_changed: Optional[bool] = field(default=None)
    state: Optional[str] = field(default=None)


@dataclass
class TrainingDeliveryPhase:
    """Phase of active training delivery and instruction. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#TrainingDeliveryPhase"


@dataclass
class TrainingInstitution:
    """Institution providing child protection training. Modeled as gUFO Organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#TrainingInstitution"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)


@dataclass
class TrainingMetrics:
    """Metrics measuring training effectiveness and reach. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#TrainingMetrics"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: Optional[datetime] = field(default=None)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    created_time: Optional[datetime] = field(default=None)


@dataclass
class TrainingModule:
    """Individual training module covering specific topics. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#TrainingModule"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: Optional[str] = field(default=None)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)
    has_changed: Optional[bool] = field(default=None)
    state: Optional[str] = field(default=None)


@dataclass
class TrainingParticipant:
    """Professional participating in training programs. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#TrainingParticipant"
    created_by: Optional[IdentityAbstraction] = field(default=None)
    description: list[str] = field(default_factory=list)
    external_reference: list[ExternalReference] = field(default_factory=list)
    has_facet: list[Facet] = field(default_factory=list)
    modified_time: list[datetime] = field(default_factory=list)
    name: Optional[str] = field(default=None)
    object_created_time: Optional[datetime] = field(default=None)
    object_marking: list[MarkingDefinitionAbstraction] = field(default_factory=list)
    object_status: Optional[str] = field(default=None)
    spec_version: Optional[str] = field(default=None)
    tag: list[str] = field(default_factory=list)


@dataclass
class VictimServiceTraining:
    """Training for professionals providing victim services. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/training#VictimServiceTraining"
    completion_rate: Optional[float] = field(default=None)
    participation_rate: Optional[float] = field(default=None)
    training_duration: Optional[float] = field(default=None)
    training_language: list[str] = field(default_factory=list)
    training_reach_count: Optional[int] = field(default=None)
    created_time: Optional[datetime] = field(default=None)
    end_time: Optional[datetime] = field(default=None)
    modified_time: Optional[datetime] = field(default=None)
    name: Optional[str] = field(default=None)
    start_time: Optional[datetime] = field(default=None)

