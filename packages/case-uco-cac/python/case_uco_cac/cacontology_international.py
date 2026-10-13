"""CAC Ontology - Crimes Against Children — cacontology_international module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional, Union

import case_uco.uco.core as _uco_core
import case_uco.uco.observable as _uco_observable
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AutomatedCrossMatching", "CountryPartnership", "CrossBorderDeviceSeizure", "CrossBorderEffectiveness", "CrossBorderForensics", "CrossBorderInvestigation", "CrossBorderOperation", "CrossBorderThreatAlert", "CrossJurisdictionalInvestigation", "CrossReferenceAnalysis", "CrossReferralProtocol", "DataExchangeProtocol", "DistributedIntelligenceProcessing", "EmergencyCoordinationProtocol", "EuropeanCooperationFramework", "EuropolCoordination", "EuropolOperation", "ExtraditionAgreement", "FederatedDatabaseQuery", "GlobalCaseTracking", "GlobalDatabaseNetwork", "GlobalHotlineNetwork", "GlobalInvestigativeTeam", "GlobalMissingChildrenCenter", "GlobalPlatformTakedown", "GlobalReach", "GlobalTakedownCoordination", "InformationSharingAgreement", "InstantAlertSystem", "IntelligenceDataLake", "IntelligenceFusion", "InternationalAlert", "InternationalAnalyst", "InternationalCoordination", "InternationalCoordinator", "InternationalDatabase", "InternationalEvidence", "InternationalEvidenceSharing", "InternationalHotlineCoordination", "InternationalImpact", "InternationalIntelligenceSharing", "InternationalNetworkDisruption", "InternationalPartnership", "InternationalProsecution", "InternationalReferral", "InternationalResourceCoordination", "InternationalTaskForce", "InternationalWarrant", "JurisdictionalCoordination", "LiaisonOfficer", "LiveIntelligenceFeed", "MassUserAnalysis", "MultiCountryTakedown", "MultilingualSupport", "MutualLegalAssistance", "MutualLegalAssistanceTreatyOperation", "OperationalSyncronization", "RealTimeIntelligenceSharing", "RegionalCoordination", "SecureChannel", "SecureCommunicationChannel", "ThreatAssessmentSharing"]


@dataclass
class CrossReferenceAnalysis(_cac_core.CoordinationEvent):
    """Analysis correlating data across multiple international databases to identify connections and patterns."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#CrossReferenceAnalysis"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AutomatedCrossMatching(CrossReferenceAnalysis):
    """Automated system for continuous cross-matching of new data against international databases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#AutomatedCrossMatching"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InternationalPartnership(_uco_core.UcoObject):
    """A formal partnership between countries or organizations for child protection cooperation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#InternationalPartnership"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})
    has_end_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasEndPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})
    coordination_method: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-international:coordinationMethod', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_coordination_effectiveness: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-international:hasCoordinationEffectiveness', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_data_quality: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-international:hasDataQuality', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_reliability_score: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-international:hasReliabilityScore', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_trust_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-international:hasTrustLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    partner_country_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-international:partnerCountryCount', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class CountryPartnership(InternationalPartnership):
    """A bilateral or multilateral partnership between specific countries for child protection."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#CountryPartnership"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MutualLegalAssistance(_uco_core.UcoObject):
    """Formal legal assistance between countries for investigations and prosecutions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#MutualLegalAssistance"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})
    has_data_quality: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-international:hasDataQuality', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_reliability_score: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-international:hasReliabilityScore', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    treaty_basis: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-international:treatyBasis', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class MutualLegalAssistanceTreatyOperation(MutualLegalAssistance):
    """Operational process using Mutual Legal Assistance Treaty (MLAT) for international evidence sharing and cooperation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#MutualLegalAssistanceTreatyOperation"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CrossBorderDeviceSeizure(MutualLegalAssistanceTreatyOperation):
    """Seizure of electronic devices across international borders with subsequent evidence sharing through MLAT processes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#CrossBorderDeviceSeizure"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CrossBorderEffectiveness(_uco_core.UcoObject):
    """Effectiveness measurement for cross-border operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#CrossBorderEffectiveness"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CrossBorderForensics(_cac_core.CoordinationEvent):
    """Forensic analysis requiring coordination across multiple countries for large-scale evidence processing."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#CrossBorderForensics"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CrossBorderOperation(_cac_core.CoordinationEvent):
    """Investigation or operation spanning multiple countries."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#CrossBorderOperation"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})
    has_end_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasEndPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})
    coordination_complexity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-international:coordinationComplexity', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    cross_border_capability: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-international:crossBorderCapability', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_data_quality: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-international:hasDataQuality', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_operational_urgency: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-international:hasOperationalUrgency', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_reliability_score: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-international:hasReliabilityScore', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_success_likelihood: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-international:hasSuccessLikelihood', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    end_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:endTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    modified_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:modifiedTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class CrossBorderInvestigation(CrossBorderOperation):
    """Investigation requiring coordination across national boundaries."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#CrossBorderInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    jurisdiction_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-international:jurisdictionCount', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class InformationSharingAgreement(_uco_core.UcoObject):
    """Formal agreement governing information sharing between countries."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#InformationSharingAgreement"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})
    has_end_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasEndPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})
    has_agreement_stability: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-international:hasAgreementStability', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_compliance: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-international:hasCompliance', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    has_data_quality: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-international:hasDataQuality', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_reliability_score: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-international:hasReliabilityScore', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    information_sharing_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-international:informationSharingLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    multilateral_agreement: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-international:multilateralAgreement', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    shares_data_with: list[Organization] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-international:sharesDataWith', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/identity/Organization', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class InternationalIntelligenceSharing(InformationSharingAgreement):
    """Intelligence sharing framework for large-scale operations requiring coordination across multiple intelligence agencies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#InternationalIntelligenceSharing"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RealTimeIntelligenceSharing(InternationalIntelligenceSharing):
    """Real-time sharing of intelligence and alerts between international partners for immediate threat response and coordination."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#RealTimeIntelligenceSharing"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InstantAlertSystem(RealTimeIntelligenceSharing):
    """System for instant notification of threats, discoveries, and urgent coordination needs across international partners."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#InstantAlertSystem"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CrossBorderThreatAlert(InstantAlertSystem):
    """Alert about threats that require immediate action across multiple countries."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#CrossBorderThreatAlert"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CrossJurisdictionalInvestigation(CrossBorderInvestigation):
    """Investigation spanning multiple jurisdictions and countries targeting international criminal networks."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#CrossJurisdictionalInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CrossReferralProtocol(_uco_core.UcoObject):
    """Protocol for referring reports between national hotlines."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#CrossReferralProtocol"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class DataExchangeProtocol(_uco_core.UcoObject):
    """Technical protocol for secure data exchange between international partners."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#DataExchangeProtocol"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class DistributedIntelligenceProcessing(_cac_core.CoordinationEvent):
    """Distributed processing of intelligence across multiple international systems for scalable analysis."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#DistributedIntelligenceProcessing"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EmergencyCoordinationProtocol(RealTimeIntelligenceSharing):
    """Protocol for emergency coordination when immediate international response is required."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#EmergencyCoordinationProtocol"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EuropeanCooperationFramework(InternationalPartnership):
    """Framework for cooperation among European Union member states in child protection operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#EuropeanCooperationFramework"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InternationalCoordination(_cac_core.CoordinationEvent):
    """Coordination activities between international law enforcement and child protection organizations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#InternationalCoordination"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EuropolCoordination(InternationalCoordination):
    """Coordination framework provided by Europol for international law enforcement operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#EuropolCoordination"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EuropolOperation(CrossBorderOperation):
    """Large-scale international operation coordinated by Europol involving multiple EU member states and international partners."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#EuropolOperation"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    jurisdiction_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-international:jurisdictionCount', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class ExtraditionAgreement(_uco_core.UcoObject):
    """Agreement for extraditing suspects between countries."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#ExtraditionAgreement"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class InternationalDatabase(_uco_core.UcoObject):
    """Shared database accessible by multiple countries for child protection."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#InternationalDatabase"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class FederatedDatabaseQuery(InternationalDatabase):
    """Query system enabling simultaneous searches across multiple international databases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#FederatedDatabaseQuery"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class GlobalCaseTracking(_uco_core.UcoObject):
    """System for tracking cases across multiple jurisdictions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#GlobalCaseTracking"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class GlobalDatabaseNetwork(InternationalDatabase):
    """Network of interconnected international databases enabling comprehensive cross-referencing and correlation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#GlobalDatabaseNetwork"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class GlobalHotlineNetwork(_uco_core.UcoObject):
    """Network of interconnected national hotlines for child protection reporting."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#GlobalHotlineNetwork"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})
    has_data_quality: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-international:hasDataQuality', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_reliability_score: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-international:hasReliabilityScore', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#double', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class InternationalTaskForce(_uco_core.UcoObject):
    """Multi-national task force for coordinating child protection investigations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#InternationalTaskForce"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class GlobalInvestigativeTeam(InternationalTaskForce):
    """Multi-national investigative team for large-scale operations like platform takedowns."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#GlobalInvestigativeTeam"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class GlobalMissingChildrenCenter(_uco_core.UcoObject):
    """International coordination center for missing children cases across borders."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#GlobalMissingChildrenCenter"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class GlobalPlatformTakedown(CrossBorderOperation):
    """Takedown of global platforms with international user bases requiring coordinated action across multiple countries."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#GlobalPlatformTakedown"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class GlobalReach(_uco_core.UcoObject):
    """Measurement of international coverage and impact."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#GlobalReach"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class GlobalTakedownCoordination(RealTimeIntelligenceSharing):
    """Real-time coordination for simultaneous takedown operations across multiple countries."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#GlobalTakedownCoordination"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class IntelligenceDataLake(InternationalDatabase):
    """Centralized repository aggregating intelligence from multiple international sources for comprehensive analysis."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#IntelligenceDataLake"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class IntelligenceFusion(RealTimeIntelligenceSharing):
    """Real-time fusion of intelligence from multiple international sources to create comprehensive threat pictures."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#IntelligenceFusion"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InternationalAlert(_cac_core.CoordinationEvent):
    """Alert system for sharing critical information across borders."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#InternationalAlert"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class InternationalAnalyst(_cac_core.Role):
    """Analyst specializing in cross-border case analysis."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#InternationalAnalyst"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InternationalCoordinator(_cac_core.Role):
    """Role responsible for international coordination activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#InternationalCoordinator"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InternationalEvidence(_uco_observable.ObservableObject):
    """Evidence collected from international operations requiring coordination across multiple jurisdictions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#InternationalEvidence"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class InternationalEvidenceSharing(MutualLegalAssistanceTreatyOperation):
    """Sharing of evidence between countries through formal legal assistance mechanisms and treaties."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#InternationalEvidenceSharing"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InternationalHotlineCoordination(GlobalHotlineNetwork):
    """Coordination mechanism between different national hotlines."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#InternationalHotlineCoordination"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InternationalImpact(_uco_core.UcoObject):
    """Assessment of international program effectiveness."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#InternationalImpact"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class InternationalNetworkDisruption(CrossJurisdictionalInvestigation):
    """Coordinated international effort to disrupt criminal networks operating across borders."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#InternationalNetworkDisruption"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InternationalProsecution(_cac_core.LegalEvent):
    """Prosecution strategy coordinated across multiple countries for users identified in large-scale operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#InternationalProsecution"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InternationalReferral(_cac_core.CoordinationEvent):
    """Referral of cases or information to international partners."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#InternationalReferral"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    response_time_international: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-international:responseTimeInternational', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    undercover_coordination: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-international:undercoverCoordination', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class InternationalResourceCoordination(InternationalCoordination):
    """Coordination of technical and human resources across countries for large-scale operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#InternationalResourceCoordination"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InternationalWarrant(_uco_core.UcoObject):
    """Warrant recognized across multiple jurisdictions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#InternationalWarrant"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class JurisdictionalCoordination(_uco_core.UcoObject):
    """Coordination mechanism for resolving jurisdictional conflicts."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#JurisdictionalCoordination"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class LiaisonOfficer(_cac_core.Role):
    """Officer serving as liaison between international partners."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#LiaisonOfficer"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LiveIntelligenceFeed(RealTimeIntelligenceSharing):
    """Continuous feed of intelligence updates shared in real-time between international law enforcement agencies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#LiveIntelligenceFeed"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MassUserAnalysis(_cac_core.CoordinationEvent):
    """Analysis of massive user databases requiring international coordination for processing users across multiple countries."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#MassUserAnalysis"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MultiCountryTakedown(CrossBorderOperation):
    """Coordinated takedown operation involving law enforcement from multiple countries (like Kidflix operation involving multiple nations)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#MultiCountryTakedown"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    jurisdiction_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-international:jurisdictionCount', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class MultilingualSupport(_uco_core.UcoObject):
    """Support for multiple languages in international coordination."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#MultilingualSupport"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    language_support: list[str] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-international:languageSupport', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class OperationalSyncronization(RealTimeIntelligenceSharing):
    """Real-time synchronization of operational activities across multiple countries for coordinated response."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#OperationalSyncronization"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RegionalCoordination(InternationalPartnership):
    """Coordination mechanisms within specific geographic regions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#RegionalCoordination"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    global_coverage: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-international:globalCoverage', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SecureChannel(_uco_core.UcoObject):
    """Secure communication mechanism for international coordination."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#SecureChannel"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SecureCommunicationChannel(RealTimeIntelligenceSharing):
    """Encrypted communication channel for secure real-time coordination between international partners."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#SecureCommunicationChannel"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ThreatAssessmentSharing(RealTimeIntelligenceSharing):
    """Real-time sharing of threat assessments and risk evaluations between international partners."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/international#ThreatAssessmentSharing"
    NAMESPACE_PREFIX: str = "cacontology-international"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
