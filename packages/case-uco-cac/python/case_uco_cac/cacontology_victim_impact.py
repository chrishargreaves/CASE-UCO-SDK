"""CAC Ontology - Crimes Against Children — cacontology_victim_impact module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional, Union

import case_uco.uco.action as _uco_action
import case_uco.uco.core as _uco_core
import case_uco.uco.identity as _uco_identity
import case_uco.uco.observable as _uco_observable
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AcuteImpactPhase", "AcuteTrauma", "BehavioralIndicator", "ChildExploitationTaskForce", "ChronicTrauma", "CognitiveBehavioralTherapy", "CognitiveIndicator", "CommunitySupport", "ComplexTrauma", "ComprehensiveImpactAssessment", "CrisisIntervention", "DevelopmentalImpact", "EducationalSupport", "EmergencyHelpSeeking", "EmergencyResponse", "EmotionalIndicator", "FamilyRejectionVulnerability", "FamilyReunification", "FamilyTherapy", "FearlessHudsonValleySupport", "GroupTherapy", "HelpSeekingBarrier", "HelpSeekingFacilitator", "HometownReturn", "HospitalDischarge", "HospitalIntervention", "HousingInstabilityVulnerability", "HumanTraffickingSquad", "InitialImpactAssessment", "InterstateVictimServices", "LegalSupport", "LongTermEffect", "LongTermMonitoringPhase", "MedicalTraumaAssessment", "MultiAgencyVictimResponse", "NineOneOneCall", "NonOffendingCaregiverSupport", "OngoingDangerAssessment", "OngoingImpactMonitoring", "PeerSupportService", "PhysicalIndicator", "PortAuthorityYouthServices", "ProtectiveAffirmingSupport", "PsychologicalHarm", "RecoveryMilestone", "RecoveryPhase", "RecoveryProcess", "ReintegrationPhase", "ResilienceFactors", "SOGIVulnerabilityContext", "SafetyPlanning", "SocialIndicator", "SuicidalIdeationResponse", "TherapeuticIntervention", "TherapistRole", "TherapyParticipant", "TraffickerControlBarrier", "TraumaIndicator", "TraumaTherapy", "TraumatizedVictim", "VictimAdvocacy", "VictimAdvocateRole", "VictimExtraction", "VictimImpactAssessment", "VictimInRecovery", "VictimReintegration", "VictimSafetyPlanning", "VictimSelfReporting", "VictimServiceCoordination", "VictimSupport", "VictimTransportationAssistance", "VulnerabilityContext"]


@dataclass
class AcuteImpactPhase(_cac_core.Phase):
    """Immediate phase following victimization with acute psychological impact."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#AcuteImpactPhase"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PsychologicalHarm(_uco_observable.ObservableObject):
    """Mental or emotional harm experienced by child victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#PsychologicalHarm"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    duration: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:duration', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    harm_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:harmType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    onset_timing: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:onsetTiming', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    severity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:severity', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class AcuteTrauma(PsychologicalHarm):
    """Immediate psychological trauma following victimization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#AcuteTrauma"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TraumaIndicator(_uco_observable.ObservableObject):
    """Observable signs or symptoms indicating psychological trauma."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#TraumaIndicator"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    frequency: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:frequency', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    indicator_severity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:indicatorSeverity', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    indicator_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:indicatorType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class BehavioralIndicator(TraumaIndicator):
    """Changes in behavior that indicate trauma or distress."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#BehavioralIndicator"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ChildExploitationTaskForce(_uco_identity.Organization):
    """Joint task force between FBI and local law enforcement for child exploitation cases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#ChildExploitationTaskForce"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ChronicTrauma(PsychologicalHarm):
    """Long-term psychological trauma from prolonged or repeated victimization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#ChronicTrauma"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TherapeuticIntervention(_cac_core.SupportEvent):
    """Professional therapeutic treatment or intervention for victim recovery."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#TherapeuticIntervention"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    intervention_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:interventionType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    session_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:sessionCount', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    treatment_duration: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:treatmentDuration', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    treatment_modality: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:treatmentModality', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    end_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:endTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class CognitiveBehavioralTherapy(TherapeuticIntervention):
    """CBT-based therapeutic intervention for trauma and behavioral issues."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#CognitiveBehavioralTherapy"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CognitiveIndicator(TraumaIndicator):
    """Changes in thinking, memory, or learning ability due to trauma."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#CognitiveIndicator"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimSupport(_cac_core.SupportEvent):
    """Support services provided to child victims and their families."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#VictimSupport"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    service_provider: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:serviceProvider', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    service_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:serviceType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CommunitySupport(VictimSupport):
    """Community-based support services for trafficking victims during reintegration."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#CommunitySupport"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ComplexTrauma(PsychologicalHarm):
    """Complex trauma resulting from multiple types of victimization or prolonged abuse."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#ComplexTrauma"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    attachment_disruption: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:attachmentDisruption', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    developmental_impact: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:developmentalImpact', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    trauma_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:traumaType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class VictimImpactAssessment(_uco_observable.ObservableObject):
    """Comprehensive assessment of the impact of criminal activity on child victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#VictimImpactAssessment"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    comment: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:comment', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    assessment_date: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:assessmentDate', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    assessment_duration: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:assessmentDuration', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    assessment_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:assessmentType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    assessor_credentials: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:assessorCredentials', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    severity_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:severityLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ComprehensiveImpactAssessment(VictimImpactAssessment):
    """Detailed evaluation of victim impact for legal proceedings and treatment planning."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#ComprehensiveImpactAssessment"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    assessment_domains: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:assessmentDomains', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    standardized_instruments: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:standardizedInstruments', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})


@dataclass
class CrisisIntervention(TherapeuticIntervention):
    """Immediate therapeutic intervention for acute crisis situations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#CrisisIntervention"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DevelopmentalImpact(PsychologicalHarm):
    """Impact on normal child development due to victimization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#DevelopmentalImpact"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    age_at_impact: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:ageAtImpact', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    developmental_delay: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:developmentalDelay', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    developmental_domain: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:developmentalDomain', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class EducationalSupport(VictimSupport):
    """Educational accommodations and support for victim's schooling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#EducationalSupport"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EmergencyHelpSeeking:
    """Victim's attempt to seek emergency help during trafficking or exploitation, such as calling 911 (e.g., Wilmington, NC call)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#EmergencyHelpSeeking"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class EmergencyResponse(_uco_action.Action):
    """Immediate response to victim emergency help requests, including law enforcement and victim services coordination."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#EmergencyResponse"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class EmotionalIndicator(TraumaIndicator):
    """Emotional symptoms or reactions indicating trauma."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#EmotionalIndicator"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VulnerabilityContext(_uco_core.UcoObject):
    """A contextual circumstance that may increase a minor's risk of exploitation or trafficking (e.g., family rejection, housing instability, coercive dependency, barriers to reporting). A context describes"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#VulnerabilityContext"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    associated_with_family_rejection: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:associatedWithFamilyRejection', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    associated_with_housing_instability: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:associatedWithHousingInstability', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})


@dataclass
class FamilyRejectionVulnerability(VulnerabilityContext):
    """A vulnerability factor where rejection by caregivers or family contributes to isolation, homelessness, dependency, or reduced reporting options."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#FamilyRejectionVulnerability"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RecoveryProcess(_uco_observable.ObservableObject):
    """Process of healing and recovery from victimization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#RecoveryProcess"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    recovery_milestones: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:recoveryMilestones', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    recovery_progress: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:recoveryProgress', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    recovery_stage: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:recoveryStage', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    time_in_recovery: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:timeInRecovery', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class VictimReintegration(RecoveryProcess):
    """Process of reintegrating trafficking victims back into their communities and families."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#VictimReintegration"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FamilyReunification(VictimReintegration):
    """Process of reuniting trafficking victims with their families."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#FamilyReunification"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FamilyTherapy(TherapeuticIntervention):
    """Therapeutic intervention involving the victim's family."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#FamilyTherapy"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FearlessHudsonValleySupport(VictimSupport):
    """Support services provided by Fearless! Hudson Valley organization for trafficking victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#FearlessHudsonValleySupport"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class GroupTherapy(TherapeuticIntervention):
    """Therapeutic intervention conducted in group settings with other victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#GroupTherapy"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HelpSeekingBarrier(_cac_core.EnduringEntity):
    """Factor that prevents or impedes victim from seeking help (fear, control, isolation, trauma bonding)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#HelpSeekingBarrier"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HelpSeekingFacilitator(_cac_core.EnduringEntity):
    """Factor that enables or encourages victim to seek help (opportunity, trust, desperation, external support)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#HelpSeekingFacilitator"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HometownReturn(VictimReintegration):
    """Return of trafficking victim to their hometown or place of origin."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#HometownReturn"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HospitalDischarge(_uco_action.Action):
    """Discharge of trafficking victim from hospital with safety planning and transportation arrangements."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#HospitalDischarge"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class HospitalIntervention(EmergencyResponse):
    """Medical intervention and assessment of trafficking victim at hospital following emergency call."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#HospitalIntervention"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HousingInstabilityVulnerability(VulnerabilityContext):
    """A vulnerability factor where unstable housing (homelessness, runaway status, couch-surfing) increases susceptibility to grooming, coercion, trafficking, or survival-based exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#HousingInstabilityVulnerability"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HumanTraffickingSquad(_uco_identity.Organization):
    """Specialized law enforcement unit focused on human trafficking investigations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#HumanTraffickingSquad"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class InitialImpactAssessment(VictimImpactAssessment):
    """Initial evaluation of victim impact conducted early in investigation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#InitialImpactAssessment"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MultiAgencyVictimResponse(VictimSupport):
    """Coordinated victim assistance involving multiple agencies across jurisdictions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#MultiAgencyVictimResponse"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InterstateVictimServices(MultiAgencyVictimResponse):
    """Victim services coordination across state lines for trafficking cases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#InterstateVictimServices"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegalSupport(VictimSupport):
    """Legal assistance and representation for victims in proceedings."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#LegalSupport"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LongTermEffect(_uco_observable.ObservableObject):
    """Long-term consequences of victimization on the child's life."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#LongTermEffect"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    effect_duration: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:effectDuration', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    effect_severity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:effectSeverity', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    effect_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:effectType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    functional_impairment: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:functionalImpairment', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})


@dataclass
class LongTermMonitoringPhase(_cac_core.Phase):
    """Extended phase monitoring long-term effects and continued support needs."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#LongTermMonitoringPhase"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MedicalTraumaAssessment(VictimImpactAssessment):
    """Medical assessment of physical and psychological trauma in trafficking victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#MedicalTraumaAssessment"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class NineOneOneCall(EmergencyHelpSeeking):
    """Emergency call to 911 by trafficking victim seeking help and reporting forced prostitution."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#NineOneOneCall"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class NonOffendingCaregiverSupport(VictimSupport):
    """Support services directed to the non-offending caregiver to stabilize the child-support system after disclosure and reduce pressure toward recantation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#NonOffendingCaregiverSupport"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OngoingDangerAssessment(VictimImpactAssessment):
    """Assessment of victim's ongoing danger from trafficking network and need for protection."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#OngoingDangerAssessment"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OngoingImpactMonitoring(VictimImpactAssessment):
    """Continuous monitoring of victim impact during investigation and recovery."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#OngoingImpactMonitoring"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PeerSupportService(VictimSupport):
    """Support rooted in peer connection, mutuality, and survivor- or youth-informed encouragement."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#PeerSupportService"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PhysicalIndicator(TraumaIndicator):
    """Physical symptoms or manifestations of psychological trauma."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#PhysicalIndicator"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PortAuthorityYouthServices(_uco_identity.Organization):
    """Specialized youth services unit within Port Authority Police Department."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#PortAuthorityYouthServices"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ProtectiveAffirmingSupport(_uco_core.UcoObject):
    """A protective factor representing access to affirming adults, services, shelters, school personnel, advocates, or community resources that mitigate vulnerability."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#ProtectiveAffirmingSupport"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class RecoveryMilestone(_cac_core.SupportEvent):
    """Significant achievement or progress point in victim recovery."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#RecoveryMilestone"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RecoveryPhase(_cac_core.Phase):
    """Phase focused on healing and therapeutic intervention."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#RecoveryPhase"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ReintegrationPhase(_cac_core.Phase):
    """Phase involving return to normal activities and social reintegration."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#ReintegrationPhase"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ResilienceFactors(_uco_observable.ObservableObject):
    """Protective factors that promote victim resilience and recovery."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#ResilienceFactors"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SOGIVulnerabilityContext(VulnerabilityContext):
    """A vulnerability context related to sexual orientation, gender identity, or expression — typically arising from family rejection, housing instability, lack of trusted adults, coercive dependency, or ba"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#SOGIVulnerabilityContext"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SafetyPlanning(VictimSupport):
    """Development of safety plans to protect victims from further harm."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#SafetyPlanning"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SocialIndicator(TraumaIndicator):
    """Changes in social behavior or relationships due to trauma."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#SocialIndicator"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SuicidalIdeationResponse(EmergencyResponse):
    """Emergency response to trafficking victim reporting suicidal thoughts or intentions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#SuicidalIdeationResponse"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TherapistRole(_cac_core.Role):
    """Role of mental health professional providing therapeutic services."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#TherapistRole"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TherapyParticipant(_cac_core.Role):
    """Role of victim participating in therapeutic interventions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#TherapyParticipant"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TraffickerControlBarrier(HelpSeekingBarrier):
    """Control mechanisms used by traffickers that prevent victims from seeking help."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#TraffickerControlBarrier"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TraumaTherapy(TherapeuticIntervention):
    """Specialized therapy for treating trauma and its effects."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#TraumaTherapy"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    evidence_based: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:evidenceBased', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    trauma_focused: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-victim-impact:traumaFocused', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})


@dataclass
class TraumatizedVictim(_cac_core.Role):
    """Role of a child victim experiencing psychological trauma. Where age at time of victimization or at time of assessment is analytically relevant, that age SHOULD be expressed via cacontology-temporal:Ag"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#TraumatizedVictim"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimAdvocacy(VictimSupport):
    """Advocacy services to protect victim rights and interests."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#VictimAdvocacy"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimAdvocateRole(_cac_core.Role):
    """Role of professional providing advocacy support to victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#VictimAdvocateRole"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimExtraction(EmergencyResponse):
    """Immediate removal of victim from dangerous trafficking situation following emergency call."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#VictimExtraction"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimInRecovery(_cac_core.Role):
    """Role of a victim actively engaged in recovery process."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#VictimInRecovery"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimSafetyPlanning(VictimSupport):
    """Development of safety plan for trafficking victim to prevent re-victimization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#VictimSafetyPlanning"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimSelfReporting(EmergencyHelpSeeking):
    """Victim's direct reporting of their trafficking or exploitation situation to authorities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#VictimSelfReporting"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimServiceCoordination(_uco_action.Action):
    """Coordination of victim services between multiple agencies and organizations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#VictimServiceCoordination"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class VictimTransportationAssistance(VictimSupport):
    """Provision of transportation assistance to trafficking victims (bus tickets, safe transport)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/victim-impact#VictimTransportationAssistance"
    NAMESPACE_PREFIX: str = "cacontology-victim-impact"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
