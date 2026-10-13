"""CAC Ontology - Crimes Against Children — cacontology_custodial module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional, Union

import case_uco.uco.core as _uco_core
import case_uco.uco.observable as _uco_observable
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["ActiveCustodyPhase", "AuthorityAbuse", "AuthorityFigure", "Babysitter", "BackgroundCheck", "BreachOfCare", "CaregiverRelationship", "ChildcareProvider", "Coach", "CustodialAbuse", "CustodialAuthorization", "CustodialCrisisSituation", "CustodialRelationship", "CustodyArrangement", "EmergencyCustody", "FamilialRelationship", "FamilyFriend", "FormalCustody", "Guardian", "InformalCustody", "Mentor", "ParentalConsent", "PositionOfTrust", "ProbationaryCustodyPhase", "ProfessionalCareRelationship", "Relative", "RestrictedContactArrangement", "SupervisionBreakdownSituation", "SupervisionFailure", "SuspendedCustodyPhase", "Teacher", "TemporaryCustody", "TerminatedCustodyPhase", "TrustBreachSituation", "TrustViolation", "VisitationArrangement", "VulnerabilityExposureSituation"]


@dataclass
class CustodialRelationship(_uco_core.Relationship):
    """Legal or informal relationship involving custody, care, or supervision of a child. Modeled as gUFO Object with Kind typing for rigid identity criteria."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#CustodialRelationship"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    comment: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:comment', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    access_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:accessLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    has_custody_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:hasCustodyBeginPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_custody_end_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:hasCustodyEndPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    in_custody_phase: Optional[Phase] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:inCustodyPhase', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://cacontology.projectvic.org/core#Phase', 'alternate_range_iris': []})
    relationship_duration: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:relationshipDuration', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    relationship_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:relationshipType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    trust_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:trustLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ActiveCustodyPhase(CustodialRelationship):
    """Phase when custodial relationship is actively maintained and operational. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#ActiveCustodyPhase"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TrustViolation(_cac_core.Event):
    """Action that violates a position of trust or custodial responsibility. Modeled as gUFO Event with temporal boundaries and participation patterns."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#TrustViolation"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_violation_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:hasViolationBeginPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_violation_end_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:hasViolationEndPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    perpetrated_by: list[AuthorityFigure] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-custodial:perpetratedBy', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org/custodial#AuthorityFigure', 'alternate_range_iris': []})
    trust_level_after: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:trustLevelAfter', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    trust_level_before: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:trustLevelBefore', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    violation_severity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:violationSeverity', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    violation_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:violationType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class AuthorityAbuse(TrustViolation):
    """Abuse of authority position to exploit or harm children. Modeled as gUFO SubKind with authority relationship violations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#AuthorityAbuse"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AuthorityFigure(_cac_core.Role):
    """Individual in position of authority, trust, or power over children. Modeled as anti-rigid gUFO Role with relational foundation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#AuthorityFigure"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Babysitter(AuthorityFigure):
    """Individual temporarily caring for children in parents' absence. Modeled as anti-rigid gUFO Role with temporary scope."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#Babysitter"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class BackgroundCheck(_uco_observable.ObservableObject):
    """Background verification conducted for custodial or care position. Modeled as gUFO Object with verification results."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#BackgroundCheck"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    check_date: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:checkDate', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    check_result: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:checkResult', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    check_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:checkType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    expiration_date: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:expirationDate', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class BreachOfCare(TrustViolation):
    """Failure to provide appropriate care while in custodial role. Modeled as gUFO SubKind with care obligation failures."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#BreachOfCare"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CaregiverRelationship(CustodialRelationship):
    """Relationship involving responsibility for child's care, welfare, or supervision. Modeled as gUFO SubKind of CustodialRelationship."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#CaregiverRelationship"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    caregiving_responsibilities: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:caregivingResponsibilities', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    supervision_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:supervisionLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ChildcareProvider(AuthorityFigure):
    """Professional childcare or daycare provider. Modeled as anti-rigid gUFO Role with professional care obligations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#ChildcareProvider"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Coach(AuthorityFigure):
    """Sports or activity coach with authority over young participants. Modeled as anti-rigid gUFO Role with activity-based authority."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#Coach"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CustodialAbuse(TrustViolation):
    """Abuse committed by someone in custodial or caregiving role. Modeled as gUFO SubKind of TrustViolation with role-based context."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#CustodialAbuse"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CustodialAuthorization(_uco_observable.ObservableObject):
    """Official authorization granting custodial rights or responsibilities. Modeled as gUFO Object with legal authority."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#CustodialAuthorization"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CustodialCrisisSituation(_cac_core.Situation):
    """Emergency situation requiring immediate custodial intervention. Modeled as gUFO Situation with crisis characteristics."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#CustodialCrisisSituation"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CustodyArrangement(_uco_observable.ObservableObject):
    """Formal or informal arrangement for child custody or care. Modeled as gUFO Object with temporal arrangement characteristics."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#CustodyArrangement"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class EmergencyCustody(CustodyArrangement):
    """Temporary custody arrangement due to emergency circumstances. Modeled as anti-rigid gUFO Phase with crisis response characteristics."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#EmergencyCustody"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FamilialRelationship(CustodialRelationship):
    """Family-based relationship with natural or assumed custodial responsibilities. Modeled as gUFO SubKind with inherent care obligations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#FamilialRelationship"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FamilyFriend(AuthorityFigure):
    """Friend of family with trusted access to children. Modeled as anti-rigid gUFO Role with social trust basis."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#FamilyFriend"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FormalCustody(CustodyArrangement):
    """Legally established custody arrangement with court orders or official documentation. Modeled as gUFO SubKind with legal foundation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#FormalCustody"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Guardian(AuthorityFigure):
    """Legal or appointed guardian responsible for child's welfare. Modeled as anti-rigid gUFO Role with legal authority."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#Guardian"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InformalCustody(CustodyArrangement):
    """Informal custody arrangement without legal documentation. Modeled as gUFO SubKind with social agreement basis."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#InformalCustody"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Mentor(AuthorityFigure):
    """Adult mentor or role model with trusted relationship with child. Modeled as anti-rigid gUFO Role with developmental basis."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#Mentor"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ParentalConsent(_uco_observable.ObservableObject):
    """Consent given by parent or guardian for custodial arrangement. Modeled as gUFO Object with authorization characteristics."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#ParentalConsent"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PositionOfTrust(_cac_core.Role):
    """Role or position that grants special access to or authority over children. Modeled as anti-rigid gUFO Role with temporal participation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#PositionOfTrust"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    has_role_begin_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:hasRoleBeginPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    has_role_end_point: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:hasRoleEndPoint', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTimeStamp', 'alternate_range_iris': [], 'literal_datatype': True})
    trust_basis: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:trustBasis', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    trust_scope: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:trustScope', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ProbationaryCustodyPhase(CustodialRelationship):
    """Phase when custodial relationship is under evaluation or supervision. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#ProbationaryCustodyPhase"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProfessionalCareRelationship(CustodialRelationship):
    """Professional relationship involving child care or supervision duties. Modeled as gUFO SubKind with professional obligations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#ProfessionalCareRelationship"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Relative(AuthorityFigure):
    """Family member in position of trust or authority over child. Modeled as anti-rigid gUFO Role with familial basis."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#Relative"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VisitationArrangement(CustodyArrangement):
    """Scheduled visitation or contact arrangement with child. Modeled as gUFO SubKind with temporal scheduling patterns."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#VisitationArrangement"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RestrictedContactArrangement(VisitationArrangement):
    """A visitation or contact arrangement that restricts or suspends offender or high-risk contact after disclosure, investigation, or safeguarding concerns."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#RestrictedContactArrangement"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    contact_restriction_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:contactRestrictionType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    custody_schedule: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:custodySchedule', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SupervisionBreakdownSituation(_cac_core.Situation):
    """Situation where supervision systems have failed or become inadequate. Modeled as gUFO Situation with system failure characteristics."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#SupervisionBreakdownSituation"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SupervisionFailure(TrustViolation):
    """Failure to properly supervise or protect child while in position of authority. Modeled as gUFO SubKind with supervision duty violations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#SupervisionFailure"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    contributing_factors: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:contributingFactors', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    failure_severity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:failureSeverity', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    failure_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-custodial:failureType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SuspendedCustodyPhase(CustodialRelationship):
    """Phase when custodial relationship is temporarily suspended but not terminated. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#SuspendedCustodyPhase"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Teacher(AuthorityFigure):
    """Educational professional with authority over students. Modeled as anti-rigid gUFO Role with institutional authority."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#Teacher"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TemporaryCustody(CustodialRelationship):
    """Short-term custody arrangement or supervision of a child. Modeled as anti-rigid gUFO Phase with temporal boundaries."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#TemporaryCustody"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TerminatedCustodyPhase(CustodialRelationship):
    """Phase when custodial relationship has been formally ended. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#TerminatedCustodyPhase"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TrustBreachSituation(_cac_core.Situation):
    """Situation arising from violation of trust or authority position. Modeled as gUFO Situation with trust violation context."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#TrustBreachSituation"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VulnerabilityExposureSituation(_cac_core.Situation):
    """Situation where child vulnerability factors create elevated risk. Modeled as gUFO Situation with protection need characteristics."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/custodial#VulnerabilityExposureSituation"
    NAMESPACE_PREFIX: str = "cacontology-custodial"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
