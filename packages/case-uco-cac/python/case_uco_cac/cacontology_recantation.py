"""CAC Ontology - Crimes Against Children — cacontology_recantation module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional

from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["CommunityPressureRisk", "DisclosureStatement", "OffenderContactRisk", "PartialRecantationStatement", "PostDisclosureDenialStatement", "PostRecantationForensicInterview", "ReaffirmedDisclosureStatement", "RecantationAssessment", "RecantationNotification", "RecantationPressure", "RecantationRiskFactor", "RecantationStatement", "SiblingSeparationConcern", "StatementChangeContext", "SystemInterventionFear", "TentativeDisclosureStatement", "UnsupportiveFamilyResponse", "VictimStatement"]


@dataclass
class RecantationRiskFactor(_cac_core.AssessmentResult):
    """A factor correlated with increased likelihood of post-disclosure denial or recantation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recantation#RecantationRiskFactor"
    NAMESPACE_PREFIX: str = "cacontology-recantation"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    risk_factor_category: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-recantation:riskFactorCategory', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CommunityPressureRisk(RecantationRiskFactor):
    """A recantation risk created by pressure, shame, or expectation from community, school, faith, or other social networks."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recantation#CommunityPressureRisk"
    NAMESPACE_PREFIX: str = "cacontology-recantation"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimStatement(_cac_core.Artifact):
    """A statement or account by a child victim concerning abuse, disclosure, denial, or recantation. Modeled as a gUFO Object to support linkage to persons, contexts, and investigative assessments."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recantation#VictimStatement"
    NAMESPACE_PREFIX: str = "cacontology-recantation"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    statement_about_event: Optional[Crime] = field(default=None, metadata={'jsonld_key': 'cacontology-recantation:statementAboutEvent', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/action/Crime', 'alternate_range_iris': []})
    statement_date: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'cacontology-recantation:statementDate', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    statement_made_by: Optional[Person] = field(default=None, metadata={'jsonld_key': 'cacontology-recantation:statementMadeBy', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/identity/Person', 'alternate_range_iris': []})
    statement_received_by: Optional[Person] = field(default=None, metadata={'jsonld_key': 'cacontology-recantation:statementReceivedBy', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/identity/Person', 'alternate_range_iris': []})


@dataclass
class DisclosureStatement(VictimStatement):
    """A statement in which a child victim discloses abuse or exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recantation#DisclosureStatement"
    NAMESPACE_PREFIX: str = "cacontology-recantation"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OffenderContactRisk(RecantationRiskFactor):
    """A recantation risk created by continued offender access, visitation, or indirect contact after disclosure."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recantation#OffenderContactRisk"
    NAMESPACE_PREFIX: str = "cacontology-recantation"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PostDisclosureDenialStatement(VictimStatement):
    """A denial made after an earlier disclosure has already occurred."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recantation#PostDisclosureDenialStatement"
    NAMESPACE_PREFIX: str = "cacontology-recantation"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RecantationStatement(PostDisclosureDenialStatement):
    """A statement in which a child victim retracts or disavows an earlier disclosure."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recantation#RecantationStatement"
    NAMESPACE_PREFIX: str = "cacontology-recantation"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    retracts_statement: Optional[DisclosureStatement] = field(default=None, metadata={'jsonld_key': 'cacontology-recantation:retractsStatement', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://cacontology.projectvic.org/recantation#DisclosureStatement', 'alternate_range_iris': []})


@dataclass
class PartialRecantationStatement(RecantationStatement):
    """A recantation that withdraws only part of a prior disclosure or muddies the disclosure without fully retracting it."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recantation#PartialRecantationStatement"
    NAMESPACE_PREFIX: str = "cacontology-recantation"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RecantationAssessment(_cac_core.InvestigativeAction):
    """An investigative or prosecutorial assessment of a recantation, its credibility, surrounding pressures, and implications for case strategy."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recantation#RecantationAssessment"
    NAMESPACE_PREFIX: str = "cacontology-recantation"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    assessment_disposition: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-recantation:assessmentDisposition', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PostRecantationForensicInterview(RecantationAssessment):
    """A follow-up forensic interview conducted after recantation or denial to explore circumstances, pressure, and statement change dynamics."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recantation#PostRecantationForensicInterview"
    NAMESPACE_PREFIX: str = "cacontology-recantation"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ReaffirmedDisclosureStatement(DisclosureStatement):
    """A later statement that reaffirms an earlier disclosure after denial, pressure, or recantation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recantation#ReaffirmedDisclosureStatement"
    NAMESPACE_PREFIX: str = "cacontology-recantation"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    reaffirms_statement: Optional[DisclosureStatement] = field(default=None, metadata={'jsonld_key': 'cacontology-recantation:reaffirmsStatement', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://cacontology.projectvic.org/recantation#DisclosureStatement', 'alternate_range_iris': []})


@dataclass
class RecantationNotification(_cac_core.Event):
    """An action in which a family member, caregiver, professional, or other person reports that a child has recanted or denied an earlier disclosure."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recantation#RecantationNotification"
    NAMESPACE_PREFIX: str = "cacontology-recantation"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    notification_channel: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-recantation:notificationChannel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class RecantationPressure(_cac_core.Event):
    """A coercive or inducement-bearing action intended to influence a victim to deny, minimize, or retract a disclosure."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recantation#RecantationPressure"
    NAMESPACE_PREFIX: str = "cacontology-recantation"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    pressure_method: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-recantation:pressureMethod', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SiblingSeparationConcern(RecantationRiskFactor):
    """A concern that sibling removal, foster placement, or sibling separation may drive statement withdrawal."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recantation#SiblingSeparationConcern"
    NAMESPACE_PREFIX: str = "cacontology-recantation"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StatementChangeContext(_cac_core.Situation):
    """A situation capturing the social, familial, investigative, and coercive conditions surrounding a victim's change in statement."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recantation#StatementChangeContext"
    NAMESPACE_PREFIX: str = "cacontology-recantation"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    assessed_by_action: list[RecantationAssessment] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-recantation:assessedByAction', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org/recantation#RecantationAssessment', 'alternate_range_iris': []})
    has_recantation_risk_factor: list[RecantationRiskFactor] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-recantation:hasRecantationRiskFactor', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org/recantation#RecantationRiskFactor', 'alternate_range_iris': []})
    reported_through_notification: Optional[RecantationNotification] = field(default=None, metadata={'jsonld_key': 'cacontology-recantation:reportedThroughNotification', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'https://cacontology.projectvic.org/recantation#RecantationNotification', 'alternate_range_iris': []})


@dataclass
class SystemInterventionFear(RecantationRiskFactor):
    """Fear of court, child-protection action, family breakup, or other multidisciplinary system consequences following disclosure."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recantation#SystemInterventionFear"
    NAMESPACE_PREFIX: str = "cacontology-recantation"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TentativeDisclosureStatement(DisclosureStatement):
    """A partial or testing-the-waters disclosure that precedes fuller disclosure."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recantation#TentativeDisclosureStatement"
    NAMESPACE_PREFIX: str = "cacontology-recantation"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class UnsupportiveFamilyResponse(RecantationRiskFactor):
    """A family response that sides with the offender, undermines the child, or otherwise erodes support for the disclosure."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recantation#UnsupportiveFamilyResponse"
    NAMESPACE_PREFIX: str = "cacontology-recantation"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
