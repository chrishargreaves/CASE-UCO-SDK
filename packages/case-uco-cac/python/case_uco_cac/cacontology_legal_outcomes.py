"""CAC Ontology - Crimes Against Children — cacontology_legal_outcomes module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, ClassVar, Optional, Union

import case_uco.uco.core as _uco_core
import case_uco.uco.observable as _uco_observable
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AVAAAssessment", "AppealProcess", "AppellateDisposition", "AppellateIssue", "ArraignmentProceeding", "CSAM_AccessingAndViewing", "CSAM_CausingProduction", "CSAM_Distribution", "CSAM_Possession", "CSAM_Production", "CSAM_ReceivingOnCellularDevice", "CarriageServiceCSAMTransmission", "CarriageServiceIndecentCommunication", "ChargingInstrument", "CommonwealthChildAbuseOffense", "CommunityService", "ComputerInternetMonitoringCondition", "ComputerSeduceSolicitLure", "ContributingToDelinquency", "ConvictionRecord", "CriminalCharge", "CriminalComplaint", "CriminalInformation", "CriminalSentence", "DefendantRole", "DefenseAttorneyRole", "DirectPromotionOfSexualPerformance", "EvidenceRule", "EvidentiaryRuling", "FederalCharge", "FederalProsecution", "FloridaStateCharge", "GeorgiaStateCharge", "Indictment", "InstallmentPaymentSchedule", "JVTAAssessment", "JudgeRole", "JudicialSystemSituation", "JuryRole", "LegalCaseSituation", "LegalProceeding", "LifeImprisonmentSentence", "LiveStreamingOffense", "LumpSumPaymentSchedule", "MagistrateComplaint", "MandatoryMinimumSentencing", "MinorContactRestrictionCondition", "MonetaryPenalty", "OnlineEnticement", "PaymentSchedule", "PleaBargaining", "PostConvictionPhase", "PreTrialPhase", "PrisonSentence", "ProbationOfficerRole", "ProbationSearchCondition", "ProbationSentence", "ProfessionalLicenseSurrenderCondition", "ProsecutorRole", "SORNAComplianceCondition", "SentencingHearing", "SentencingPhase", "SentencingReasonablenessIssue", "SexOffenderTreatmentCondition", "SexTrafficking", "SextortionCharge", "SexualExploitationOfMinorCharge", "SolicitingExplicitMaterial", "SpecialAssessment", "StandardOfReview", "StateCharge", "SubstanceAbuseTreatmentCondition", "SufficiencyOfEvidenceIssue", "SupersedingIndictment", "SupervisedRelease", "SupervisedReleaseCondition", "TraffickingOfPersonsForSexualServitudeCharge", "TravelingToMeetAfterComputerLure", "TrialPhase", "TrialProceeding", "VictimRole"]


@dataclass
class CriminalSentence(_uco_observable.ObservableObject):
    """Punishment imposed by court for criminal conviction. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CriminalSentence"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    concurrent_with: list[CriminalSentence] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-legal-outcomes:concurrentWith', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'https://cacontology.projectvic.org/legal-outcomes#CriminalSentence', 'alternate_range_iris': []})
    sentence_concurrency: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:sentenceConcurrency', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class MonetaryPenalty(CriminalSentence):
    """Financial penalty including fines, restitution, or forfeiture. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#MonetaryPenalty"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SpecialAssessment(MonetaryPenalty):
    """Mandatory special assessment imposed per count of conviction (18 U.S.C. § 3013), or a statute-specific additional assessment. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SpecialAssessment"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AVAAAssessment(SpecialAssessment):
    """Assessment under the Amy, Vicky, and Andy Child Pornography Victim Assistance Act of 2018 (18 U.S.C. § 2259A)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#AVAAAssessment"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegalProceeding(_cac_core.LegalEvent):
    """Formal judicial process for prosecuting cacontology-related crimes. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#LegalProceeding"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    bail_status: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:bailStatus', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class AppealProcess(LegalProceeding):
    """Legal process to challenge conviction or sentence in higher court. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#AppealProcess"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AppellateDisposition(_uco_observable.ObservableObject):
    """Outcome of an appellate issue or appeal (e.g., affirmed, reversed, vacated, remanded). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#AppellateDisposition"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    disposition_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:dispositionType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class AppellateIssue(_uco_observable.ObservableObject):
    """Issue raised on appeal to challenge a conviction or sentence (e.g., evidentiary admission, sufficiency of evidence, sentencing reasonableness). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#AppellateIssue"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    applies_standard_of_review: list[StandardOfReview] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-legal-outcomes:appliesStandardOfReview', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'https://cacontology.projectvic.org/legal-outcomes#StandardOfReview', 'alternate_range_iris': []})
    cites_evidence_rule: list[EvidenceRule] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-legal-outcomes:citesEvidenceRule', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'https://cacontology.projectvic.org/legal-outcomes#EvidenceRule', 'alternate_range_iris': []})
    issue_disposition: list[AppellateDisposition] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-legal-outcomes:issueDisposition', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org/legal-outcomes#AppellateDisposition', 'alternate_range_iris': []})


@dataclass
class ArraignmentProceeding(LegalProceeding):
    """Initial court appearance where charges are formally read and plea is entered. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#ArraignmentProceeding"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CriminalCharge(_uco_observable.ObservableObject):
    """Formal accusation of criminal activity in CAC cases. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CriminalCharge"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class FederalCharge(CriminalCharge):
    """Criminal charge under federal law and jurisdiction. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#FederalCharge"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CSAM_Possession(FederalCharge):
    """Charge for possession of child sexual abuse material. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CSAM_Possession"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CSAM_AccessingAndViewing(CSAM_Possession):
    """Charge for intentionally accessing and viewing child sexual abuse material. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CSAM_AccessingAndViewing"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CSAM_Production(FederalCharge):
    """Charge for production of child sexual abuse material, typically carrying severe mandatory minimum sentences. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CSAM_Production"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CSAM_CausingProduction(CSAM_Production):
    """Charge for causing or facilitating the production of child sexual abuse material, distinct from direct production. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CSAM_CausingProduction"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CSAM_Distribution(FederalCharge):
    """Charge for distribution of child sexual abuse material. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CSAM_Distribution"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CSAM_ReceivingOnCellularDevice(CSAM_Possession):
    """Charge for receiving child sexual abuse material on cellular phone or mobile device. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CSAM_ReceivingOnCellularDevice"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CarriageServiceCSAMTransmission(FederalCharge):
    """Use of carriage service to cause child abuse material to be transmitted to self, contrary to section 474.22(1)(a)(ii) Criminal Code (Cth). Maximum penalty 15 years imprisonment. Modeled as gUFO Object"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CarriageServiceCSAMTransmission"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CarriageServiceIndecentCommunication(FederalCharge):
    """Use of carriage service to transmit indecent communication to person under 16 years, contrary to section 474.27A Criminal Code (Cth). Maximum penalty 10 years imprisonment. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CarriageServiceIndecentCommunication"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ChargingInstrument(_uco_observable.ObservableObject):
    """Abstract superclass for formal charging documents: criminal complaint, indictment, criminal information, and superseding instruments. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#ChargingInstrument"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    charging_instrument_counts: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:chargingInstrumentCounts', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#integer', 'alternate_range_iris': []})
    filed_date: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:filedDate', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#date', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class CommonwealthChildAbuseOffense(FederalCharge):
    """Child abuse offense under Commonwealth law subject to mandatory minimum sentencing provisions. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CommonwealthChildAbuseOffense"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CommunityService(CriminalSentence):
    """Sentence requiring unpaid work for community benefit. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CommunityService"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SupervisedReleaseCondition(_uco_observable.ObservableObject):
    """A special condition of supervised release or probation imposed in a criminal judgment. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SupervisedReleaseCondition"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    condition_text: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:conditionText', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    defendant_pays_cost: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:defendantPaysCost', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    requires_probation_approval: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:requiresProbationApproval', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})


@dataclass
class ComputerInternetMonitoringCondition(SupervisedReleaseCondition):
    """Condition requiring participation in a computer and internet monitoring program, commonly including device inventory, disclosure of accounts and credentials, consent to unannounced examination, and pr"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#ComputerInternetMonitoringCondition"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StateCharge(CriminalCharge):
    """Criminal charge under state law and jurisdiction. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#StateCharge"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FloridaStateCharge(StateCharge):
    """Criminal charge under Florida state law and jurisdiction for ICAC-related offenses. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#FloridaStateCharge"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    charge_classification: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:chargeClassification', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    florida_statute: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:floridaStatute', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ComputerSeduceSolicitLure(FloridaStateCharge):
    """Florida state charge for using a computer to seduce, solicit, or lure a child to engage in sexual conduct. Covers electronic communication with minors for sexual purposes. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#ComputerSeduceSolicitLure"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    computer_lure_method: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:computerLureMethod', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ContributingToDelinquency(FloridaStateCharge):
    """Florida state charge for contributing to the delinquency or dependency of a child. Applies when adult actions contribute to a child becoming delinquent or dependent. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#ContributingToDelinquency"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    child_delinquency_contribution: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:childDelinquencyContribution', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})


@dataclass
class ConvictionRecord(_uco_observable.ObservableObject):
    """A durable record that a person was convicted of one or more criminal charges (e.g., by jury verdict, bench trial, or plea agreement). Used for current-case dispositions and for limited prior-convictio"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#ConvictionRecord"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    charge_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:chargeCount', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    conviction_date: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:convictionDate', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    conviction_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:convictionType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    prior_convictions: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:priorConvictions', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class CriminalComplaint(ChargingInstrument):
    """A written statement of the essential facts constituting the offense charged, made under oath before a magistrate judge (or clerk where authorized) prior to indictment. Fed. R. Crim. P. 3. Modeled as g"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CriminalComplaint"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CriminalInformation(ChargingInstrument):
    """A charging instrument filed by the prosecutor without grand-jury action, typically after the defendant waives indictment. Fed. R. Crim. P. 7(b). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CriminalInformation"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DefendantRole(_cac_core.Role):
    """Role of individual charged with CAC crimes. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#DefendantRole"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DefenseAttorneyRole(_cac_core.Role):
    """Role of defense attorney representing CAC defendants. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#DefenseAttorneyRole"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DirectPromotionOfSexualPerformance(FloridaStateCharge):
    """Florida state charge for direct promotion of a sexual performance by a child. Applies when defendant promotes, directs, or produces sexual conduct involving a minor. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#DirectPromotionOfSexualPerformance"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    sexual_performance_promotion: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:sexualPerformancePromotion', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})


@dataclass
class EvidenceRule(_uco_observable.ObservableObject):
    """A rule of evidence cited in an appellate issue or opinion (e.g., Federal Rule of Evidence 403, 404(b), 414). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#EvidenceRule"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    rule_citation: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:ruleCitation', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class EvidentiaryRuling(AppellateIssue):
    """Appellate issue concerning a trial court evidentiary ruling, including admission/exclusion decisions and related prejudice analysis (e.g., under Federal Rules of Evidence). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#EvidentiaryRuling"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FederalProsecution(_uco_core.UcoObject):
    """Alias for cacontology-usa-federal:FederalProsecution, provided for continuity with existing graphs pending the namespace-alignment decision in CAC-Ontology issue #40."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#FederalProsecution"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class GeorgiaStateCharge(StateCharge):
    """Criminal charge under Georgia state law and jurisdiction for CAC-related offenses. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#GeorgiaStateCharge"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Indictment(ChargingInstrument):
    """A grand-jury charging instrument. Fed. R. Crim. P. 6, 7. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#Indictment"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PaymentSchedule(_uco_observable.ObservableObject):
    """Schedule of criminal monetary payments imposed in a judgment (AO 245B Schedule of Payments). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#PaymentSchedule"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    due_timing: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:dueTiming', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    total_amount_usd: Optional[Any] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:totalAmountUSD', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': ['http://www.w3.org/2001/XMLSchema#integer']})


@dataclass
class InstallmentPaymentSchedule(PaymentSchedule):
    """Payment schedule requiring periodic installments, typically with a monthly minimum and a commencement trigger."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#InstallmentPaymentSchedule"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class JVTAAssessment(SpecialAssessment):
    """Assessment under the Justice for Victims of Trafficking Act of 2015 (18 U.S.C. § 3014)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#JVTAAssessment"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class JudgeRole(_cac_core.Role):
    """Role of judge presiding over CAC legal proceedings. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#JudgeRole"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class JudicialSystemSituation(_cac_core.Situation):
    """Broader situation involving judicial system processing of CAC cases. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#JudicialSystemSituation"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class JuryRole(_cac_core.Role):
    """Role of jury members in CAC trial proceedings. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#JuryRole"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegalCaseSituation(_cac_core.Situation):
    """Complex situation encompassing the entire legal case from charges to resolution. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#LegalCaseSituation"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PrisonSentence(CriminalSentence):
    """Sentence involving incarceration in federal or state prison. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#PrisonSentence"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LifeImprisonmentSentence(PrisonSentence):
    """Prison sentence of life imprisonment (typically without a fixed term duration). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#LifeImprisonmentSentence"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LiveStreamingOffense(CommonwealthChildAbuseOffense):
    """Offense involving live streaming of child abuse, often carrying severe sentences. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#LiveStreamingOffense"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LumpSumPaymentSchedule(PaymentSchedule):
    """Payment schedule requiring a lump-sum payment (e.g., due immediately, on a date, or after release)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#LumpSumPaymentSchedule"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MagistrateComplaint(CriminalComplaint):
    """A criminal complaint sworn before a federal magistrate judge, typically supported by a law-enforcement agent affidavit or statement of facts. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#MagistrateComplaint"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MandatoryMinimumSentencing(PrisonSentence):
    """Sentencing under mandatory minimum provisions for Commonwealth child sexual abuse offenses. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#MandatoryMinimumSentencing"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MinorContactRestrictionCondition(SupervisedReleaseCondition):
    """Condition restricting contact with persons under a specified age, typically requiring written probation approval and/or presence of a responsible adult aware of the offense history."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#MinorContactRestrictionCondition"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OnlineEnticement(FederalCharge):
    """Charge for online enticement of minors for illegal sexual activity. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#OnlineEnticement"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PleaBargaining(LegalProceeding):
    """Negotiation process between prosecution and defense for plea agreement. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#PleaBargaining"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PostConvictionPhase(_cac_core.Phase):
    """Phase after conviction including appeals and compliance. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#PostConvictionPhase"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PreTrialPhase(_cac_core.Phase):
    """Phase before trial including arraignment and plea bargaining. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#PreTrialPhase"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProbationOfficerRole(_cac_core.Role):
    """Role of probation officer supervising CAC offenders. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#ProbationOfficerRole"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProbationSearchCondition(SupervisedReleaseCondition):
    """Condition authorizing probation-officer searches of person, property, residence, vehicle, or devices, typically on reasonable suspicion and at a reasonable time and manner."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#ProbationSearchCondition"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ProbationSentence(CriminalSentence):
    """Supervised release with conditions instead of or after incarceration. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#ProbationSentence"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    probation_conditions: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:probationConditions', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
    reporting_frequency: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:reportingFrequency', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    supervision_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:supervisionLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ProfessionalLicenseSurrenderCondition(_uco_observable.ObservableObject):
    """Condition associated with a plea agreement or sentencing outcome requiring the defendant to surrender a professional license (e.g., a nursing license)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#ProfessionalLicenseSurrenderCondition"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    condition_applies_to_person: list[Person] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-legal-outcomes:conditionAppliesToPerson', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/identity/Person', 'alternate_range_iris': []})
    requires_license_surrender: list[ProfessionalLicense] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-legal-outcomes:requiresLicenseSurrender', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org/sex-offender-registry#ProfessionalLicense', 'alternate_range_iris': []})


@dataclass
class ProsecutorRole(_cac_core.Role):
    """Role of prosecutor handling CAC criminal charges. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#ProsecutorRole"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SORNAComplianceCondition(SupervisedReleaseCondition):
    """Condition requiring compliance with the Sex Offender Registration and Notification Act (34 U.S.C. § 20901 et seq.) as directed by the probation officer or registration authority."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SORNAComplianceCondition"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SentencingHearing(LegalProceeding):
    """Court proceeding where sentence is determined and imposed. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SentencingHearing"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SentencingPhase(_cac_core.Phase):
    """Phase focused on sentencing determination and imposition. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SentencingPhase"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SentencingReasonablenessIssue(AppellateIssue):
    """Appellate issue challenging the procedural and/or substantive reasonableness of a sentence (e.g., under 18 U.S.C. § 3553(a)). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SentencingReasonablenessIssue"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SexOffenderTreatmentCondition(SupervisedReleaseCondition):
    """Condition requiring participation in a sex-offense-specific treatment program, commonly including polygraph examination, confidentiality waiver, and cost provisions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SexOffenderTreatmentCondition"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SexTrafficking(FederalCharge):
    """Charge for sex trafficking of minors. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SexTrafficking"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SextortionCharge(FederalCharge):
    """Criminal charge specifically related to sextortion involving sexual extortion of children through online blackmail. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SextortionCharge"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SexualExploitationOfMinorCharge(GeorgiaStateCharge):
    """Georgia state charge for sexual exploitation of a minor, as reported in a Georgia Attorney General press release. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SexualExploitationOfMinorCharge"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SolicitingExplicitMaterial(CommonwealthChildAbuseOffense):
    """Offense of soliciting sexually explicit material from children (e.g., from 10 foreign children via social media). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SolicitingExplicitMaterial"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StandardOfReview(_uco_observable.ObservableObject):
    """Appellate standard of review applied to an appellate issue (e.g., de novo, abuse of discretion, plain error). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#StandardOfReview"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    standard_of_review_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:standardOfReviewType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SubstanceAbuseTreatmentCondition(SupervisedReleaseCondition):
    """Condition requiring substance-abuse testing and/or treatment (residential or outpatient), commonly with urinalysis limits, abstinence requirements, and cost provisions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SubstanceAbuseTreatmentCondition"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SufficiencyOfEvidenceIssue(AppellateIssue):
    """Appellate issue challenging whether the evidence was sufficient to sustain a conviction under the applicable legal standard. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SufficiencyOfEvidenceIssue"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SupersedingIndictment(Indictment):
    """An indictment that replaces an earlier charging instrument in the same case, typically adding, modifying, or dropping counts or defendants. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SupersedingIndictment"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SupervisedRelease(CriminalSentence):
    """Period of supervision following completion of prison sentence. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SupervisedRelease"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TraffickingOfPersonsForSexualServitudeCharge(GeorgiaStateCharge):
    """Georgia state charge for trafficking of persons for sexual servitude, as reported in a Georgia Attorney General press release. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#TraffickingOfPersonsForSexualServitudeCharge"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TravelingToMeetAfterComputerLure(FloridaStateCharge):
    """Florida state charge for traveling to meet after using a computer to lure a child. Applies when defendant uses electronic communication to lure a child and then travels to meet them. Modeled as gUFO O"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#TravelingToMeetAfterComputerLure"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    electronic_communication_used: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:electronicCommunicationUsed', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    travel_occurred: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-legal-outcomes:travelOccurred', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})


@dataclass
class TrialPhase(_cac_core.Phase):
    """Active trial phase with proceedings and evidence presentation. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#TrialPhase"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TrialProceeding(LegalProceeding):
    """Formal trial process with jury or judge determining guilt or innocence. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#TrialProceeding"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimRole(_cac_core.Role):
    """Role of victim in CAC legal proceedings. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#VictimRole"
    NAMESPACE_PREFIX: str = "cacontology-legal-outcomes"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
