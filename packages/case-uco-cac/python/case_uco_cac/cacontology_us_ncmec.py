"""CAC Ontology - Crimes Against Children — cacontology_us_ncmec module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, ClassVar, Optional, Union

import case_uco.uco.action as _uco_action
import case_uco.uco.core as _uco_core
import case_uco.uco.observable as _uco_observable
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AccountLinking", "AggregateReportStatistic", "CSAMSolicitationAnnotation", "ChildSexTourismIncident", "ChildSexTraffickingIncident", "ContentIdentification", "CyberTipAnalysis", "CybertipExtractedIdentifierSet", "CybertipIdentifierExtractionAction", "CybertipJurisdictionRoutingAssessment", "FederalReferral", "InvestigationTrigger", "LocalLawEnforcementReferral", "MinorToMinorInteractionAnnotation", "NCMECCybertipReport", "NCMECIncidentType", "NCMECReportAnnotation", "OnlineEnticementIncident", "PhoneNumberTrace", "PlatformCooperation", "PossessionIndicator", "SextortionAnnotation", "SpamAnnotation", "TaskForceReferral", "TipEnrichment", "TipPrioritization", "TipProcessing", "TipValidation", "TransferDetection"]


@dataclass
class CyberTipAnalysis(_uco_observable.ObservableObject):
    """Analytical processing and assessment of NCMEC CyberTip reports by law enforcement."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#CyberTipAnalysis"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    analysis_confidence: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:analysisConfidence', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    analysis_of: Optional[NCMECCybertipReport] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:analysisOf', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://cacontology.projectvic.org/us/ncmec#NCMECCybertipReport', 'alternate_range_iris': []})
    performer: Optional[Person] = field(default=None, metadata={'jsonld_key': 'uco-action:performer', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/identity/Person', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    end_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:endTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class AccountLinking(CyberTipAnalysis):
    """Process of linking digital accounts to suspects through NCMEC tip analysis."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#AccountLinking"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    account_confidence: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:accountConfidence', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    linked_to_account: list[DigitalAccount] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-us-ncmec:linkedToAccount', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/observable/DigitalAccount', 'alternate_range_iris': []})


@dataclass
class AggregateReportStatistic(_uco_core.Assertion):
    """A single published aggregate statistic about CyberTipline reporting or related NCMEC program activity (e.g., annual report volume, category growth rate, cumulative hash counts), as stated in NCMEC pub"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#AggregateReportStatistic"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    percent_change_from_prior_period: Optional[Any] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:percentChangeFromPriorPeriod', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': ['http://www.w3.org/2001/XMLSchema#integer']})
    reporting_period: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:reportingPeriod', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    statistic_qualifier: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:statisticQualifier', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    statistic_unit: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:statisticUnit', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    statistic_value: Optional[Any] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:statisticValue', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': ['http://www.w3.org/2001/XMLSchema#integer']})


@dataclass
class NCMECReportAnnotation(_cac_core.EnduringEntity):
    """Tags to describe the NCMEC report. Source: NCMEC Cybertip API Section B.1.1, reportAnnotations element."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#NCMECReportAnnotation"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CSAMSolicitationAnnotation(NCMECReportAnnotation):
    """Annotation indicating the report is associated with solicitation of CSAM. Source: NCMEC Cybertip API Section B.1.1, reportAnnotations/csamSolicitation element."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#CSAMSolicitationAnnotation"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class NCMECIncidentType(_cac_core.EnduringEntity):
    """Types of incidents as defined by NCMEC Cybertip API (Section B.1.1). This class represents the standardized incident categories used in NCMEC reporting."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#NCMECIncidentType"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    incident_code: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:incidentCode', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ChildSexTourismIncident(NCMECIncidentType):
    """Incidents involving child sex tourism. Source: NCMEC Cybertip API Section B.1.1, incidentType 'Child Sex Tourism'."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#ChildSexTourismIncident"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ChildSexTraffickingIncident(NCMECIncidentType):
    """Incidents involving child sex trafficking. Source: NCMEC Cybertip API Section B.1.1, incidentType 'Child Sex Trafficking'."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#ChildSexTraffickingIncident"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ContentIdentification(CyberTipAnalysis):
    """Identification and classification of illegal content in NCMEC tips."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#ContentIdentification"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    identified_content: list[DigitalArtifact] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-us-ncmec:identifiedContent', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/observable/DigitalArtifact', 'alternate_range_iris': []})


@dataclass
class CybertipExtractedIdentifierSet(_uco_observable.ObservableObject):
    """An information artifact representing the set of identifiers extracted from a CyberTipline report, used to support triage, enrichment, and routing."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#CybertipExtractedIdentifierSet"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CybertipIdentifierExtractionAction(_uco_action.Action):
    """A CAC-domain action that extracts structured identifiers (screen names, phone numbers, IP addresses, email addresses) from a CyberTipline report document, including by OCR or document parsing."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#CybertipIdentifierExtractionAction"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CybertipJurisdictionRoutingAssessment(CyberTipAnalysis):
    """A triage assessment that uses extracted identifiers and enrichment results to recommend or determine the responsible jurisdiction or agency for routing or investigation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#CybertipJurisdictionRoutingAssessment"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InvestigationTrigger(_uco_observable.ObservableObject):
    """Event or information that triggers law enforcement investigation based on NCMEC tip."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#InvestigationTrigger"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    referral_jurisdiction: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:referralJurisdiction', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    trigger_criteria: list[str] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-us-ncmec:triggerCriteria', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    triggered_by: Optional[NCMECCybertipReport] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:triggeredBy', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://cacontology.projectvic.org/us/ncmec#NCMECCybertipReport', 'alternate_range_iris': []})
    urgency_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:urgencyLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class FederalReferral(InvestigationTrigger):
    """Referral of NCMEC tip to federal law enforcement agencies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#FederalReferral"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LocalLawEnforcementReferral(InvestigationTrigger):
    """Referral of NCMEC tip to local law enforcement agency."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#LocalLawEnforcementReferral"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MinorToMinorInteractionAnnotation(NCMECReportAnnotation):
    """Annotation indicating the report is associated with an interaction between minors. Source: NCMEC Cybertip API Section B.1.1, reportAnnotations/minorToMinorInteraction element."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#MinorToMinorInteractionAnnotation"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class NCMECCybertipReport(_uco_observable.ObservableObject):
    """A report submitted to NCMEC's CyberTipline. This class represents the root structure of a NCMEC report as defined in the NCMEC Cybertip API documentation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#NCMECCybertipReport"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_ncmec_incident_type: Optional[NCMECIncidentType] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:hasNCMECIncidentType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://cacontology.projectvic.org/us/ncmec#NCMECIncidentType', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class OnlineEnticementIncident(NCMECIncidentType):
    """Incidents involving online enticement of children for sexual acts. Source: NCMEC Cybertip API Section B.1.1, incidentType 'Online Enticement of Children for Sexual Acts'."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#OnlineEnticementIncident"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PhoneNumberTrace(CyberTipAnalysis):
    """Tracing of phone numbers linked to accounts in NCMEC tips."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#PhoneNumberTrace"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    phone_verification_status: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:phoneVerificationStatus', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    traced_to_phone: Optional[PhoneNumber] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:tracedToPhone', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/observable/PhoneNumber', 'alternate_range_iris': []})


@dataclass
class PlatformCooperation(_uco_observable.ObservableObject):
    """Cooperation from digital platforms in providing information for NCMEC tips."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#PlatformCooperation"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    cooperation_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:cooperationLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    data_provided: list[str] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-us-ncmec:dataProvided', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    involves_platform: Optional[DigitalService] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:involvesPlatform', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/observable/DigitalService', 'alternate_range_iris': []})
    platform_response_time: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:platformResponseTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class PossessionIndicator(CyberTipAnalysis):
    """Evidence or indicators suggesting possession of child sexual abuse material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#PossessionIndicator"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    indicator_strength: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:indicatorStrength', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SextortionAnnotation(NCMECReportAnnotation):
    """Annotation indicating the report is associated with sextortion. Source: NCMEC Cybertip API Section B.1.1, reportAnnotations/sextortion element."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#SextortionAnnotation"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SpamAnnotation(NCMECReportAnnotation):
    """Annotation indicating the report is associated with spam. Source: NCMEC Cybertip API Section B.1.1, reportAnnotations/spam element."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#SpamAnnotation"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TaskForceReferral(InvestigationTrigger):
    """Referral of NCMEC tip to appropriate CAC task force for investigation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#TaskForceReferral"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TipProcessing(_uco_observable.ObservableObject):
    """Processing workflow for NCMEC tips from receipt to investigation referral."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#TipProcessing"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    processed_tip: Optional[NCMECCybertipReport] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:processedTip', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://cacontology.projectvic.org/us/ncmec#NCMECCybertipReport', 'alternate_range_iris': []})
    processing_time: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:processingTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    end_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:endTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class TipEnrichment(TipProcessing):
    """Enhancement of NCMEC tips with additional investigative information."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#TipEnrichment"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    enrichment_type: list[str] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-us-ncmec:enrichmentType', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class TipPrioritization(TipProcessing):
    """Priority assessment and ranking of NCMEC tips for investigation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#TipPrioritization"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    priority_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:priorityLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class TipValidation(TipProcessing):
    """Validation and verification of information in NCMEC tips."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#TipValidation"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    validation_status: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:validationStatus', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class TransferDetection(CyberTipAnalysis):
    """Detection of transfer or sharing of child sexual abuse material."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/us/ncmec#TransferDetection"
    NAMESPACE_PREFIX: str = "cacontology-us-ncmec"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    transfer_frequency: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:transferFrequency', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    transfer_volume: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-us-ncmec:transferVolume', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
