"""CAC Ontology - Crimes Against Children — cacontology_usa_federal_law module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar, Optional, Union

import case_uco.uco.core as _uco_core
import case_uco.uco.identity as _uco_identity
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AbusiveContactWithMinor", "AggravatedSexualAbuse", "CEOSAttorneyRole", "CEOSdivision", "ChildPornographyDistribution", "ChildPornographyPossession", "ChildPornographyProduction", "ChildPornographyReceipt", "ChildSupportEnforcementLaw", "ChildSupportEvasion", "ChildSupportExploitationLink", "CommercialSexualExploitation", "ExtraterritorialProduction", "ExtraterritorialSexualExploitationLaw", "FederalChildExploitationLaw", "FederalChildPornographyLaw", "FederalChildSexTraffickingLaw", "FederalChildSexualAbuseLaw", "FederalDefendantRole", "FederalInvestigation", "FederalInvestigatorRole", "FederalObscenityLaw", "FederalProsecution", "FederalProsecutorRole", "FederalVictimRole", "FinancialControlPattern", "ForeignCommerceExploitation", "ObscenityDistribution", "ObscenityImportation", "ObscenityTransportation", "OnlineObscenityDistribution", "PostConvictionPhase", "PreTrialPhase", "SentencingPhase", "SexTourism", "SexTraffickingConspiracy", "SexTraffickingOfMinors", "SexualAbuseOfMinor", "TransportationForSexualExploitation", "TrialPhase"]


@dataclass
class AbusiveContactWithMinor(_cac_core.ExploitationEvent):
    """Federal crime involving abusive sexual contact with minor victims. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#AbusiveContactWithMinor"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AggravatedSexualAbuse(_cac_core.ExploitationEvent):
    """Federal crime of aggravated sexual abuse involving children in federal jurisdiction. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#AggravatedSexualAbuse"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FederalProsecutorRole(_cac_core.Role):
    """Role of federal prosecutor handling child exploitation cases. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#FederalProsecutorRole"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_role_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:hasRoleBeginPoint', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    role_experience: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:roleExperience', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#integer', 'alternate_range_iris': []})
    role_specialization: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:roleSpecialization', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CEOSAttorneyRole(FederalProsecutorRole):
    """Role of DOJ CEOS attorney specializing in child exploitation prosecution. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#CEOSAttorneyRole"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    collaborates_with: list[FederalInvestigatorRole] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-usa-federal-law:collaboratesWith', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org/usa-federal-law#FederalInvestigatorRole', 'alternate_range_iris': []})


@dataclass
class CEOSdivision(_uco_identity.Organization):
    """DOJ Child Exploitation and Obscenity Section serving unique and critical function in enforcement of federal laws protecting children from exploitation and prohibiting distribution of obscenity. Modele"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#CEOSdivision"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ChildPornographyDistribution(_cac_core.ExploitationEvent):
    """Federal crime of distributing child pornography across state or international boundaries. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#ChildPornographyDistribution"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_interstate_nexus: list[str] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-usa-federal-law:hasInterstateNexus', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ChildPornographyPossession(_cac_core.ExploitationEvent):
    """Federal crime of possessing child pornography that has traveled in interstate or foreign commerce. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#ChildPornographyPossession"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ChildPornographyProduction(_cac_core.ExploitationEvent):
    """Federal crime of producing child pornography, carrying severe mandatory minimum sentences. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#ChildPornographyProduction"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    crime_jurisdiction: list[str] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-usa-federal-law:crimeJurisdiction', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    crime_severity_level: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:crimeSeverityLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#integer', 'alternate_range_iris': []})
    mandatory_minimum_sentence: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:mandatoryMinimumSentence', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#integer', 'alternate_range_iris': []})


@dataclass
class ChildPornographyReceipt(_cac_core.ExploitationEvent):
    """Federal crime of knowingly receiving child pornography through interstate or foreign commerce. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#ChildPornographyReceipt"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FederalChildExploitationLaw(_cac_core.EnduringEntity):
    """U.S. federal law related to child exploitation as enforced by CEOS. Modeled as gUFO Object providing legal framework."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#FederalChildExploitationLaw"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ChildSupportEnforcementLaw(FederalChildExploitationLaw):
    """Federal laws related to child support enforcement that intersect with child exploitation cases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#ChildSupportEnforcementLaw"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ChildSupportEvasion(_cac_core.ExploitationEvent):
    """Federal crime of willfully failing to pay child support across state lines. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#ChildSupportEvasion"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ChildSupportExploitationLink(_uco_core.UcoObject):
    """Connection between child support violations and child exploitation crimes. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#ChildSupportExploitationLink"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CommercialSexualExploitation(_cac_core.ExploitationEvent):
    """Federal crime involving commercial sexual exploitation of children through force, fraud, or coercion. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#CommercialSexualExploitation"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ExtraterritorialProduction(_cac_core.ExploitationEvent):
    """Federal crime of producing child pornography outside U.S. by U.S. citizens or residents. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#ExtraterritorialProduction"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    foreign_countries_involved: list[str] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-usa-federal-law:foreignCountriesInvolved', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    involves_international_elements: list[bool] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-usa-federal-law:involvesInternationalElements', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})


@dataclass
class ExtraterritorialSexualExploitationLaw(FederalChildExploitationLaw):
    """Federal laws criminalizing sexual exploitation of children committed by U.S. citizens or residents abroad."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#ExtraterritorialSexualExploitationLaw"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FederalChildPornographyLaw(FederalChildExploitationLaw):
    """Federal statutes criminalizing child pornography production, distribution, receipt, and possession."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#FederalChildPornographyLaw"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FederalChildSexTraffickingLaw(FederalChildExploitationLaw):
    """Federal statutes criminalizing child sex trafficking, commercial sexual exploitation, and related crimes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#FederalChildSexTraffickingLaw"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FederalChildSexualAbuseLaw(FederalChildExploitationLaw):
    """Federal statutes criminalizing child sexual abuse in federal jurisdiction or involving interstate elements."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#FederalChildSexualAbuseLaw"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FederalDefendantRole(_cac_core.Role):
    """Role of individual charged in federal child exploitation case. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#FederalDefendantRole"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    defended_by: list[ExploitationEvent] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-usa-federal-law:defendedBy', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org/core#ExploitationEvent', 'alternate_range_iris': []})
    has_role_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:hasRoleBeginPoint', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class FederalInvestigation(_cac_core.InvestigativeAction):
    """Federal investigation of child exploitation crimes. Modeled as gUFO Event with temporal boundaries and evidence gathering."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#FederalInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    collects_evidence: list[ObservableObject] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-usa-federal-law:collectsEvidence', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/observable/ObservableObject', 'alternate_range_iris': []})
    investigated_by: list[FederalInvestigatorRole] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-usa-federal-law:investigatedBy', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org/usa-federal-law#FederalInvestigatorRole', 'alternate_range_iris': []})
    involves_digital_evidence: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:involvesDigitalEvidence', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    requires_forensic_analysis: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:requiresForensicAnalysis', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})


@dataclass
class FederalInvestigatorRole(_cac_core.Role):
    """Role of federal investigator (FBI, ICE, etc.) investigating child exploitation. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#FederalInvestigatorRole"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FederalObscenityLaw(_cac_core.EnduringEntity):
    """U.S. federal law related to obscenity distribution and enforcement as managed by CEOS. Modeled as gUFO Object providing legal framework."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#FederalObscenityLaw"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FederalProsecution(_cac_core.LegalEvent):
    """Federal legal prosecution process for child exploitation crimes. Modeled as gUFO Event with temporal progression through phases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#FederalProsecution"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_legal_phase: list[Phase] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-usa-federal-law:hasLegalPhase', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org/core#Phase', 'alternate_range_iris': []})
    has_prosecution_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:hasProsecutionBeginPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_prosecution_end_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:hasProsecutionEndPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    prosecuted_by: list[FederalProsecutorRole] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-usa-federal-law:prosecutedBy', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org/usa-federal-law#FederalProsecutorRole', 'alternate_range_iris': []})
    prosecution_complexity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:prosecutionComplexity', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    prosecution_severity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:prosecutionSeverity', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    prosecution_status: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:prosecutionStatus', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class FederalVictimRole(_cac_core.Role):
    """Role of victim in federal child exploitation prosecution. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#FederalVictimRole"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_role_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:hasRoleBeginPoint', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    victimized_by: list[ExploitationEvent] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-usa-federal-law:victimizedBy', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org/core#ExploitationEvent', 'alternate_range_iris': []})


@dataclass
class FinancialControlPattern(ChildSupportExploitationLink):
    """Pattern where child support evasion is used as mechanism of control in exploitation cases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#FinancialControlPattern"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ForeignCommerceExploitation(_cac_core.ExploitationEvent):
    """Federal crime involving sexual exploitation of children in foreign commerce. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#ForeignCommerceExploitation"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    foreign_countries_involved: list[str] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-usa-federal-law:foreignCountriesInvolved', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    involves_international_elements: list[bool] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-usa-federal-law:involvesInternationalElements', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})


@dataclass
class ObscenityDistribution(_cac_core.ExploitationEvent):
    """Federal crime of distributing obscene materials through interstate or foreign commerce. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#ObscenityDistribution"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ObscenityImportation(_cac_core.ExploitationEvent):
    """Federal crime of importing obscene materials into the United States. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#ObscenityImportation"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ObscenityTransportation(_cac_core.ExploitationEvent):
    """Federal crime of transporting obscene materials across state or international boundaries. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#ObscenityTransportation"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OnlineObscenityDistribution(ObscenityDistribution):
    """Federal crime of distributing obscene materials through internet and digital platforms. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#OnlineObscenityDistribution"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PostConvictionPhase(_cac_core.Phase):
    """Post-conviction phase including appeals and compliance monitoring."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#PostConvictionPhase"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PreTrialPhase(_cac_core.Phase):
    """Pre-trial phase of federal prosecution including investigation and charging."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#PreTrialPhase"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_phase_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:hasPhaseBeginPoint', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_phase_end_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:hasPhaseEndPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    is_phase_of: Optional[FederalProsecution] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:isPhaseOf', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://cacontology.projectvic.org/usa-federal-law#FederalProsecution', 'alternate_range_iris': []})


@dataclass
class SentencingPhase(_cac_core.Phase):
    """Sentencing phase of federal prosecution including penalty determination. Modeled as anti-rigid gUFO Phase that prosecution temporarily exemplifies."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#SentencingPhase"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_phase_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:hasPhaseBeginPoint', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_phase_end_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:hasPhaseEndPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    is_phase_of: Optional[FederalProsecution] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:isPhaseOf', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://cacontology.projectvic.org/usa-federal-law#FederalProsecution', 'alternate_range_iris': []})


@dataclass
class SexTourism(_cac_core.ExploitationEvent):
    """Federal crime of traveling abroad with intent to engage in sexual conduct with minors. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#SexTourism"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    foreign_countries_involved: list[str] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-usa-federal-law:foreignCountriesInvolved', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    involves_international_elements: list[bool] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-usa-federal-law:involvesInternationalElements', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})


@dataclass
class SexTraffickingConspiracy(_cac_core.ExploitationEvent):
    """Federal crime of conspiracy to engage in sex trafficking of minors. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#SexTraffickingConspiracy"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SexTraffickingOfMinors(_cac_core.ExploitationEvent):
    """Federal crime of sex trafficking involving minors, including recruitment, harboring, transportation, or obtaining. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#SexTraffickingOfMinors"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_begin_point_in_xsd_date_time_stamp: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'http://purl.org/nemo/gufo#hasBeginPointInXSDDateTimeStamp', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    crime_severity_level: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:crimeSeverityLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#integer', 'alternate_range_iris': []})
    involves_multiple_states: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:involvesMultipleStates', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    mandatory_minimum_sentence: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:mandatoryMinimumSentence', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#integer', 'alternate_range_iris': []})


@dataclass
class SexualAbuseOfMinor(_cac_core.ExploitationEvent):
    """Federal crime of sexual abuse specifically involving minor victims. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#SexualAbuseOfMinor"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TransportationForSexualExploitation(_cac_core.ExploitationEvent):
    """Federal crime of transporting minors across international boundaries for sexual exploitation. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#TransportationForSexualExploitation"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    foreign_countries_involved: list[str] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-usa-federal-law:foreignCountriesInvolved', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    involves_international_elements: list[bool] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-usa-federal-law:involvesInternationalElements', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})


@dataclass
class TrialPhase(_cac_core.Phase):
    """Trial phase of federal prosecution including court proceedings."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-federal-law#TrialPhase"
    NAMESPACE_PREFIX: str = "cacontology-usa-federal-law"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_phase_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:hasPhaseBeginPoint', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_phase_end_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:hasPhaseEndPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    is_phase_of: Optional[FederalProsecution] = field(default=None, metadata={'jsonld_key': 'cacontology-usa-federal-law:isPhaseOf', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://cacontology.projectvic.org/usa-federal-law#FederalProsecution', 'alternate_range_iris': []})
