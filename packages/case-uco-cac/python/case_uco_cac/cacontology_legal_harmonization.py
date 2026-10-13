"""CAC Ontology - Crimes Against Children — cacontology_legal_harmonization module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar, Optional

import case_uco.uco.core as _uco_core
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AdvocacyProcess", "AgeVerificationLaw", "AmendmentProcess", "AnnualReview", "AuditProcess", "BestPractice", "BillDrafting", "BillSponsor", "CSAMCriminalization", "CSAMModelLaw", "CapacityBuilding", "CertificationProcess", "ChildExploitationLaw", "ChildTraffickingLaw", "CoalitionBuilding", "CommitteeMember", "CommitteeReview", "ComplianceBenchmark", "ComplianceDocumentationArtifact", "ComplianceIntelligenceFramework", "ComplianceMetrics", "ComplianceProcess", "Correspondence", "DataProtectionForMinorsLaw", "ExtraditionAgreement", "FloorVote", "GlobalLegalReview", "GrantCompliance", "GrassrootsAdvocacy", "HarmonizationInitiative", "HarmonizationProgress", "ImpactAssessment", "InternationalLawEnforcement", "InternationalStandard", "JurisdictionalCoordination", "JurisdictionalVariation", "KnowingParadox", "LawEnforcementOfficer", "LegalCompliance", "LegalCoverageAssessment", "LegalEffectiveness", "LegalFrameworkGap", "LegalReform", "LegalSystemCompatibility", "LegislativeAdvocate", "LegislativeAssessment", "LegislativeDrafting", "LegislativeEducation", "LegislativeInstrument", "LegislativeProcess", "LegislativeRole", "Legislator", "MandatoryReporting", "MandatoryReportingLaw", "MediaOutreach", "MinimumStandard", "MutualLegalAssistance", "NationalLegislation", "OnlineGroomingLaw", "OnlineSafetyLaw", "PlatformAccountabilityLaw", "PolicyAnalyst", "PolicyDevelopment", "PolicyHarmonization", "ProsecutorAdvocate", "PublicHearing", "RegionalFramework", "SafeHarbor", "SextortionLaw", "StakeholderEngagement", "Statute", "StatutoryReporting", "TaskForceLiaison", "TechnicalAssistance", "TestimonySubmission", "TreatyFramework", "VictimAdvocate", "VictimProtectionLaw"]


@dataclass
class AdvocacyProcess(_cac_core.LegalEvent):
    """Process used in legislative advocacy."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#AdvocacyProcess"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AgeVerificationLaw(_cac_core.Artifact):
    """Laws requiring age verification for online services."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#AgeVerificationLaw"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegislativeProcess(_cac_core.LegalEvent):
    """A step in the legislative lifecycle - applicable across jurisdictions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#LegislativeProcess"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AmendmentProcess(LegislativeProcess):
    """Process of amending legislation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#AmendmentProcess"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ComplianceProcess(_cac_core.LegalEvent):
    """Process for ensuring legal compliance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#ComplianceProcess"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AnnualReview(ComplianceProcess):
    """Annual compliance review process."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#AnnualReview"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AuditProcess(ComplianceProcess):
    """Audit for compliance verification."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#AuditProcess"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class BestPractice(_cac_core.Artifact):
    """Best practice in child protection legislation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#BestPractice"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class BillDrafting(LegislativeProcess):
    """Process of drafting legislation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#BillDrafting"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegislativeRole(_cac_core.Role):
    """Role an actor plays in the legislative ecosystem."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#LegislativeRole"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class BillSponsor(LegislativeRole):
    """Legislator who introduces or sponsors legislation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#BillSponsor"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CSAMCriminalization(_cac_core.Artifact):
    """Legislation criminalizing child sexual abuse material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#CSAMCriminalization"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CSAMModelLaw(_cac_core.Artifact):
    """Model legislation for Child Sexual Abuse Material regulations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#CSAMModelLaw"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CapacityBuilding(_cac_core.LegalEvent):
    """Building legal capacity for child protection."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#CapacityBuilding"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CertificationProcess(ComplianceProcess):
    """Process for obtaining compliance certification."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#CertificationProcess"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ChildExploitationLaw(_cac_core.Artifact):
    """Laws addressing child exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#ChildExploitationLaw"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ChildTraffickingLaw(_cac_core.Artifact):
    """Legislation addressing child trafficking crimes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#ChildTraffickingLaw"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CoalitionBuilding(AdvocacyProcess):
    """Building coalitions to support advocacy goals."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#CoalitionBuilding"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CommitteeMember(LegislativeRole):
    """Member of a legislative committee."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#CommitteeMember"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CommitteeReview(LegislativeProcess):
    """Review of legislation by a committee."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#CommitteeReview"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ComplianceBenchmark(_cac_core.AssessmentResult):
    """Benchmark for measuring legal compliance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#ComplianceBenchmark"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ComplianceDocumentationArtifact(_cac_core.Artifact):
    """Documentation artifact (record/report/audit trail element) used to prove appropriate action to regulators and support claims of good-faith compliance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#ComplianceDocumentationArtifact"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ComplianceIntelligenceFramework(_cac_core.EnduringEntity):
    """A verified compliance intelligence framework used to document good-faith content moderation and reporting efforts (beyond simple detection) and support risk-stratified operational decisions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#ComplianceIntelligenceFramework"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ComplianceMetrics(_cac_core.AssessmentResult):
    """Metrics for measuring legal compliance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#ComplianceMetrics"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Correspondence(_cac_core.Artifact):
    """Communication between actors regarding legislation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#Correspondence"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DataProtectionForMinorsLaw(_cac_core.Artifact):
    """Laws protecting children's personal data."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#DataProtectionForMinorsLaw"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ExtraditionAgreement(_cac_core.Artifact):
    """Agreement enabling extradition for child protection crimes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#ExtraditionAgreement"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FloorVote(LegislativeProcess):
    """Vote on legislation by the full legislative body."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#FloorVote"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class GlobalLegalReview(_cac_core.Artifact):
    """Comprehensive review of child protection legislation across countries."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#GlobalLegalReview"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class GrantCompliance(ComplianceProcess):
    """Compliance with grant requirements."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#GrantCompliance"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class GrassrootsAdvocacy(AdvocacyProcess):
    """Mobilizing public support for advocacy goals."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#GrassrootsAdvocacy"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HarmonizationInitiative(_cac_core.Situation):
    """Organized effort to harmonize laws across jurisdictions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#HarmonizationInitiative"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HarmonizationProgress(_cac_core.AssessmentResult):
    """Progress measurement for policy harmonization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#HarmonizationProgress"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ImpactAssessment(AdvocacyProcess):
    """Assessing the impact of proposed legislation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#ImpactAssessment"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InternationalLawEnforcement(_cac_core.LegalEvent):
    """Law enforcement cooperation across international boundaries."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#InternationalLawEnforcement"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InternationalStandard(_cac_core.Artifact):
    """International standard for child protection legislation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#InternationalStandard"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class JurisdictionalCoordination(_cac_core.EnduringEntity):
    """Framework for coordinating across legal jurisdictions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#JurisdictionalCoordination"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class JurisdictionalVariation(_cac_core.EnduringEntity):
    """Variation in legal approaches across jurisdictions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#JurisdictionalVariation"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class KnowingParadox(_cac_core.Situation):
    """A policy incentive conflict where platforms face liability both for detecting content (creating knowledge) and for failing to detect content, discouraging proactive detection."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#KnowingParadox"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LawEnforcementOfficer(LegislativeRole):
    """Officer involved in child safety investigations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#LawEnforcementOfficer"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegalCompliance(_uco_core.UcoObject):
    """Situation of compliance with international standards."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#LegalCompliance"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class LegalCoverageAssessment(_cac_core.AssessmentResult):
    """Assessment of legal coverage for child protection."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#LegalCoverageAssessment"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegalEffectiveness(_cac_core.AssessmentResult):
    """Assessment of legal framework effectiveness."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#LegalEffectiveness"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegalFrameworkGap(_cac_core.EnduringEntity):
    """Identified gap in legal framework coverage."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#LegalFrameworkGap"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegalReform(_cac_core.LegalEvent):
    """Process of reforming child protection legislation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#LegalReform"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegalSystemCompatibility(_uco_core.UcoObject):
    """Compatibility situation between different legal systems."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#LegalSystemCompatibility"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class LegislativeAdvocate(LegislativeRole):
    """Person who advocates for legislative change."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#LegislativeAdvocate"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegislativeAssessment(_cac_core.AssessmentResult):
    """Assessment of existing child protection legislation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#LegislativeAssessment"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegislativeDrafting(_cac_core.LegalEvent):
    """Process of drafting child protection legislation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#LegislativeDrafting"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegislativeEducation(AdvocacyProcess):
    """Educating legislators on issues."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#LegislativeEducation"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegislativeInstrument:
    """A bill, resolution, or other legislative document."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#LegislativeInstrument"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class Legislator(LegislativeRole):
    """Elected member of a legislative body."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#Legislator"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MandatoryReporting(ComplianceProcess):
    """Required reporting to authorities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#MandatoryReporting"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MandatoryReportingLaw(_cac_core.Artifact):
    """Legislation requiring mandatory reporting of child abuse."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#MandatoryReportingLaw"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MediaOutreach(AdvocacyProcess):
    """Engaging media to support advocacy goals."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#MediaOutreach"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MinimumStandard(_cac_core.Artifact):
    """Minimum standard for child protection laws."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#MinimumStandard"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MutualLegalAssistance(_cac_core.Artifact):
    """Framework for mutual legal assistance between countries."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#MutualLegalAssistance"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class NationalLegislation(_cac_core.Artifact):
    """National child protection legislation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#NationalLegislation"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OnlineGroomingLaw(_cac_core.Artifact):
    """Legislation addressing online grooming behaviors."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#OnlineGroomingLaw"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OnlineSafetyLaw(_cac_core.Artifact):
    """General laws addressing online child safety."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#OnlineSafetyLaw"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PlatformAccountabilityLaw(_cac_core.Artifact):
    """Laws holding online platforms accountable for child safety."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#PlatformAccountabilityLaw"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PolicyAnalyst(LegislativeRole):
    """Person who analyzes and develops policy recommendations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#PolicyAnalyst"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PolicyDevelopment(_cac_core.LegalEvent):
    """Development of child protection policies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#PolicyDevelopment"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PolicyHarmonization(_cac_core.LegalEvent):
    """Process of harmonizing policies across jurisdictions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#PolicyHarmonization"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProsecutorAdvocate(LegislativeRole):
    """Prosecutor who advocates for stronger laws."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#ProsecutorAdvocate"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PublicHearing(LegislativeProcess):
    """Public hearing on proposed legislation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#PublicHearing"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RegionalFramework(_cac_core.Artifact):
    """Regional legal framework for child protection."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#RegionalFramework"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SafeHarbor(_cac_core.Artifact):
    """A statutory or regulatory safe harbor provision intended to distinguish good-faith compliance efforts from negligence (e.g., incentives for verified compliance intelligence frameworks)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#SafeHarbor"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SextortionLaw(_cac_core.Artifact):
    """Laws addressing sextortion of children."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#SextortionLaw"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StakeholderEngagement(AdvocacyProcess):
    """Engaging stakeholders in advocacy efforts."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#StakeholderEngagement"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Statute:
    """Enacted law within a jurisdiction."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#Statute"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class StatutoryReporting(ComplianceProcess):
    """Reporting required by statute."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#StatutoryReporting"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TaskForceLiaison(LegislativeRole):
    """Person who coordinates between task forces and other entities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#TaskForceLiaison"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TechnicalAssistance(_cac_core.LegalEvent):
    """Technical assistance for legal framework development."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#TechnicalAssistance"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TestimonySubmission(AdvocacyProcess):
    """Submitting testimony to legislative bodies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#TestimonySubmission"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TreatyFramework(_cac_core.Artifact):
    """International treaty framework for child protection."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#TreatyFramework"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimAdvocate(LegislativeRole):
    """Person who advocates on behalf of crime victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#VictimAdvocate"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimProtectionLaw(_cac_core.Artifact):
    """Legislation protecting child victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-harmonization#VictimProtectionLaw"
    NAMESPACE_PREFIX: str = "cacontology-legal-harmonization"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
