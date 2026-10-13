"""CAC Ontology - Crimes Against Children — cacontology_case_management module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional

import case_uco.uco.core as _uco_core
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AccommodationMotion", "ActiveInvestigationPhase", "AdministrativeReview", "AnalystAssignment", "ArrestWarrant", "CaseAnalystRole", "CaseAssignment", "CaseClosure", "CaseDocumentation", "CaseDurationMetrics", "CaseInitiationPhase", "CaseManagement", "CaseManagerRole", "CaseMetrics", "CaseProsecutorRole", "CaseReport", "CaseReview", "CaseTracking", "CaseWorkflow", "ColdCaseManagement", "ComplexCaseManagement", "CostPerCaseMetrics", "CourtFiling", "CourtProceedingsPhase", "CourtroomAccommodationPlan", "DispositionPhase", "DispositionWorkflow", "EvidenceLog", "ExpertReport", "ExternalReview", "HighPriorityCaseManagement", "IntakeWorkflow", "InterviewNotes", "InvestigationWorkflow", "InvestigatorAssignment", "LeadInvestigatorRole", "LegalReview", "MultiJurisdictionalCaseManagement", "PeerReview", "PrimaryInvestigatorAssignment", "ProsecutionPreparationPhase", "ProsecutionWorkflow", "ProsecutorAssignment", "QualityAssuranceReview", "QualityScoreMetrics", "ResolutionRateMetrics", "ResourceUtilizationMetrics", "SearchWarrant", "SecondaryInvestigatorAssignment", "SupervisorAssignment", "SupervisoryReview", "TestimonyContingencyPlan"]


@dataclass
class CaseDocumentation(_cac_core.Artifact):
    """Comprehensive documentation management for case files, reports, evidence logs, and legal documents. Enhanced as gUFO Object for document management."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#CaseDocumentation"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    document_status: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-case-management:documentStatus', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    document_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-case-management:documentType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CourtFiling(CaseDocumentation):
    """Legal documents filed with courts including motions, briefs, and procedural filings. Enhanced as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#CourtFiling"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AccommodationMotion(CourtFiling):
    """Court filing requesting witness or victim accommodations needed for testimony, accessibility, or trauma-informed participation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#AccommodationMotion"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    prepared_for_witness: Optional[Person] = field(default=None, metadata={'jsonld_key': 'cacontology-case-management:preparedForWitness', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/identity/Person', 'alternate_range_iris': []})
    supports_accommodation_plan: Optional[CourtroomAccommodationPlan] = field(default=None, metadata={'jsonld_key': 'cacontology-case-management:supportsAccommodationPlan', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://cacontology.projectvic.org/case-management#CourtroomAccommodationPlan', 'alternate_range_iris': []})


@dataclass
class ActiveInvestigationPhase(_cac_core.Phase):
    """Phase during which active investigation activities occur including evidence collection and analysis. Anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#ActiveInvestigationPhase"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CaseReview(_cac_core.InvestigativeAction):
    """Formal review processes for case quality assurance, supervisory oversight, and legal compliance. Enhanced as gUFO Event for review processes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#CaseReview"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    review_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-case-management:reviewType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    review_begin_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#reviewBeginTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    review_end_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#reviewEndTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class AdministrativeReview(CaseReview):
    """Administrative review of case management, resource allocation, and procedural compliance. Enhanced as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#AdministrativeReview"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CaseAssignment(_uco_core.UcoObject):
    """Assignment of personnel and resources to specific cases with defined roles and responsibilities. Enhanced as gUFO Event linking to gUFO Roles."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#CaseAssignment"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    assigned_to_role: list[Role] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-case-management:assignedToRole', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'https://cacontology.projectvic.org/core#Role', 'alternate_range_iris': []})
    assignment_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-case-management:assignmentType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    assignment_begin_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#assignmentBeginTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    assignment_end_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#assignmentEndTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class AnalystAssignment(CaseAssignment):
    """Assignment of analysts for data analysis, intelligence gathering, and technical support. Enhanced as gUFO Event linking to anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#AnalystAssignment"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ArrestWarrant(CaseDocumentation):
    """Legal documentation for arrest warrants including applications, approvals, and execution records. Enhanced as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#ArrestWarrant"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CaseAnalystRole(_cac_core.Role):
    """Role responsible for case analysis, intelligence gathering, and data processing. Enhanced as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#CaseAnalystRole"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CaseClosure(_cac_core.InvestigativeAction):
    """Formal case closure process including disposition, appeals status, and archival procedures. Enhanced as gUFO Event for closure processes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#CaseClosure"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CaseMetrics(_cac_core.AssessmentResult):
    """Performance metrics and analytics for case management including duration, resolution rates, and resource utilization. Enhanced as gUFO Object for metric management."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#CaseMetrics"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CaseDurationMetrics(CaseMetrics):
    """Metrics tracking case duration from opening to closure across different stages. Enhanced as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#CaseDurationMetrics"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CaseInitiationPhase(_cac_core.Phase):
    """Initial phase where case is opened and basic assignment occurs. Anti-rigid gUFO Phase supporting dynamic operational transitions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#CaseInitiationPhase"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    phase_transition_time: list[datetime] = field(default_factory=list, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#phaseTransitionTime', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class CaseManagement(_cac_core.EnduringEntity):
    """Comprehensive management framework for CAC cases including status tracking, priority assignment, and resource allocation. Enhanced as gUFO Object for comprehensive structural modeling and property man"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#CaseManagement"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    case_priority: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-case-management:casePriority', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    case_status: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-case-management:caseStatus', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    current_phase: Optional[Phase] = field(default=None, metadata={'jsonld_key': 'cacontology-case-management:currentPhase', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'https://cacontology.projectvic.org/core#Phase', 'alternate_range_iris': []})


@dataclass
class CaseManagerRole(_cac_core.Role):
    """Role responsible for overall case management coordination and oversight. Enhanced as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#CaseManagerRole"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CaseProsecutorRole(_cac_core.Role):
    """Role responsible for legal review, charging decisions, and prosecution activities. Enhanced as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#CaseProsecutorRole"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CaseReport(CaseDocumentation):
    """Formal case report documenting investigation findings, evidence, and recommendations. Enhanced as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#CaseReport"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CaseTracking(_cac_core.DigitalSystemEntity):
    """Systematic tracking of case progress, updates, and status changes across multiple systems and jurisdictions. Enhanced as gUFO Object for systematic monitoring."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#CaseTracking"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CaseWorkflow(_cac_core.InvestigativeAction):
    """Structured workflow stages and processes for managing case progression from intake to disposition. Enhanced as gUFO Event for comprehensive temporal and causal modeling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#CaseWorkflow"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    workflow_stage: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-case-management:workflowStage', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    workflow_begin_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#workflowBeginTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    workflow_end_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#workflowEndTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class ColdCaseManagement(CaseManagement):
    """Management protocols for cold cases including periodic review and new evidence integration. Subclasses CaseManagement (EnduringEntity) only."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#ColdCaseManagement"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ComplexCaseManagement(CaseManagement):
    """Specialized management for complex cases involving multiple offenses, victims, or extensive evidence. Subclasses CaseManagement (EnduringEntity) only."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#ComplexCaseManagement"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CostPerCaseMetrics(CaseMetrics):
    """Financial metrics tracking costs associated with case investigation and prosecution. Enhanced as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#CostPerCaseMetrics"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CourtProceedingsPhase(_cac_core.Phase):
    """Phase during which court proceedings occur including trials and hearings. Anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#CourtProceedingsPhase"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CourtroomAccommodationPlan(CaseDocumentation):
    """Case documentation specifying planned courtroom accommodations for a child witness, including support persons, sensory adjustments, or assistive response methods."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#CourtroomAccommodationPlan"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    accommodation_type: list[str] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-case-management:accommodationType', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    prepared_for_witness: Optional[Person] = field(default=None, metadata={'jsonld_key': 'cacontology-case-management:preparedForWitness', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/identity/Person', 'alternate_range_iris': []})


@dataclass
class DispositionPhase(_cac_core.Phase):
    """Final phase involving case disposition, sentencing, and closure activities. Anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#DispositionPhase"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DispositionWorkflow(CaseWorkflow):
    """Final case disposition workflow including sentencing, appeals, and case closure procedures. Enhanced as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#DispositionWorkflow"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EvidenceLog(CaseDocumentation):
    """Comprehensive log of all evidence collected, analyzed, and maintained for the case. Enhanced as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#EvidenceLog"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ExpertReport(CaseDocumentation):
    """Expert analysis reports including forensic findings, psychological evaluations, and technical assessments. Enhanced as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#ExpertReport"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ExternalReview(CaseReview):
    """External review by independent parties for oversight, audit, or specialized expertise. Enhanced as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#ExternalReview"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HighPriorityCaseManagement(CaseManagement):
    """Enhanced management protocols for critical and high-priority cases requiring expedited processing. Subclasses CaseManagement (EnduringEntity) only."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#HighPriorityCaseManagement"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class IntakeWorkflow(CaseWorkflow):
    """Initial case intake and assessment workflow including triage and preliminary evaluation. Enhanced as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#IntakeWorkflow"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    intake_begin_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#intakeBeginTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    triage_completion_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#triageCompletionTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class InterviewNotes(CaseDocumentation):
    """Documentation of interviews conducted with victims, witnesses, and suspects. Enhanced as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#InterviewNotes"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InvestigationWorkflow(CaseWorkflow):
    """Active investigation workflow including evidence collection, analysis, and suspect identification. Enhanced as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#InvestigationWorkflow"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InvestigatorAssignment(CaseAssignment):
    """Specific assignment of investigators to cases with experience levels, caseload management, and specialization tracking. Enhanced as gUFO Event with Role relationships."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#InvestigatorAssignment"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LeadInvestigatorRole(_cac_core.Role):
    """Primary investigator role with leadership responsibilities for case investigation. Enhanced as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#LeadInvestigatorRole"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegalReview(CaseReview):
    """Legal review of case materials, procedures, and prosecution readiness. Enhanced as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#LegalReview"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MultiJurisdictionalCaseManagement(CaseManagement):
    """Specialized management for cases spanning multiple jurisdictions with coordination requirements. Subclasses CaseManagement (EnduringEntity) only; situation-like aspects modeled separately."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#MultiJurisdictionalCaseManagement"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PeerReview(CaseReview):
    """Peer review process for case methodology, analysis, and conclusions. Enhanced as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#PeerReview"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PrimaryInvestigatorAssignment(InvestigatorAssignment):
    """Lead investigator assignment with primary responsibility for case management and coordination. Enhanced as gUFO Event linking to anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#PrimaryInvestigatorAssignment"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProsecutionPreparationPhase(_cac_core.Phase):
    """Phase involving preparation for prosecution including legal review and case building. Anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#ProsecutionPreparationPhase"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProsecutionWorkflow(CaseWorkflow):
    """Prosecution preparation and court proceedings workflow including case presentation and trial management. Enhanced as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#ProsecutionWorkflow"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProsecutorAssignment(CaseAssignment):
    """Assignment of prosecutors for legal review, charging decisions, and court representation. Enhanced as gUFO Event linking to anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#ProsecutorAssignment"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class QualityAssuranceReview(CaseReview):
    """Systematic quality assurance review ensuring compliance with standards and procedures. Enhanced as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#QualityAssuranceReview"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class QualityScoreMetrics(CaseMetrics):
    """Quality assessment metrics evaluating case management effectiveness and outcomes. Enhanced as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#QualityScoreMetrics"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ResolutionRateMetrics(CaseMetrics):
    """Metrics tracking case resolution rates including conviction and closure statistics. Enhanced as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#ResolutionRateMetrics"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ResourceUtilizationMetrics(CaseMetrics):
    """Metrics tracking resource allocation and utilization efficiency across cases. Enhanced as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#ResourceUtilizationMetrics"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SearchWarrant(CaseDocumentation):
    """Legal documentation for search warrants including applications, approvals, and execution records. Enhanced as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#SearchWarrant"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SecondaryInvestigatorAssignment(InvestigatorAssignment):
    """Supporting investigator assignment providing specialized skills or additional resources. Enhanced as gUFO Event linking to anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#SecondaryInvestigatorAssignment"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SupervisorAssignment(CaseAssignment):
    """Supervisory assignment for case oversight, quality assurance, and administrative guidance. Enhanced as gUFO Event linking to anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#SupervisorAssignment"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SupervisoryReview(CaseReview):
    """Formal supervisory review of case progress, decisions, and quality standards. Enhanced as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#SupervisoryReview"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TestimonyContingencyPlan(CaseDocumentation):
    """Case documentation describing fallback testimony strategies when a child witness recants, shuts down, becomes unavailable, or needs alternative response methods."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/case-management#TestimonyContingencyPlan"
    NAMESPACE_PREFIX: str = "cacontology-case-management"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    contingency_type: list[str] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-case-management:contingencyType', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    prepared_for_witness: Optional[Person] = field(default=None, metadata={'jsonld_key': 'cacontology-case-management:preparedForWitness', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/identity/Person', 'alternate_range_iris': []})
