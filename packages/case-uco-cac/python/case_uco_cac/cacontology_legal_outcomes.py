"""CAC Ontology - Crimes Against Children — cacontology-legal-outcomes module."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AVAAAssessment:
    """Assessment under the Amy, Vicky, and Andy Child Pornography Victim Assistance Act of 2018 (18 U.S.C. § 2259A)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#AVAAAssessment"
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
    concurrent_with: list[CriminalSentence] = field(default_factory=list)
    sentence_concurrency: Optional[str] = field(default=None)


@dataclass
class AppealProcess:
    """Legal process to challenge conviction or sentence in higher court. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#AppealProcess"
    bail_status: Optional[str] = field(default=None)


@dataclass
class AppellateDisposition:
    """Outcome of an appellate issue or appeal (e.g., affirmed, reversed, vacated, remanded). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#AppellateDisposition"
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
    disposition_type: Optional[str] = field(default=None)


@dataclass
class AppellateIssue:
    """Issue raised on appeal to challenge a conviction or sentence (e.g., evidentiary admission, sufficiency of evidence, sentencing reasonableness). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#AppellateIssue"
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
    applies_standard_of_review: list[StandardOfReview] = field(default_factory=list)
    cites_evidence_rule: list[EvidenceRule] = field(default_factory=list)
    issue_disposition: list[AppellateDisposition] = field(default_factory=list)


@dataclass
class ArraignmentProceeding:
    """Initial court appearance where charges are formally read and plea is entered. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#ArraignmentProceeding"
    bail_status: Optional[str] = field(default=None)


@dataclass
class CSAM_AccessingAndViewing:
    """Charge for intentionally accessing and viewing child sexual abuse material. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CSAM_AccessingAndViewing"
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
class CSAM_CausingProduction:
    """Charge for causing or facilitating the production of child sexual abuse material, distinct from direct production. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CSAM_CausingProduction"
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
class CSAM_Distribution:
    """Charge for distribution of child sexual abuse material. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CSAM_Distribution"
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
class CSAM_Possession:
    """Charge for possession of child sexual abuse material. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CSAM_Possession"
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
class CSAM_Production:
    """Charge for production of child sexual abuse material, typically carrying severe mandatory minimum sentences. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CSAM_Production"
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
class CSAM_ReceivingOnCellularDevice:
    """Charge for receiving child sexual abuse material on cellular phone or mobile device. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CSAM_ReceivingOnCellularDevice"
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
class CarriageServiceCSAMTransmission:
    """Use of carriage service to cause child abuse material to be transmitted to self, contrary to section 474.22(1)(a)(ii) Criminal Code (Cth). Maximum penalty 15 years imprisonment. Modeled as gUFO Object"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CarriageServiceCSAMTransmission"
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
class CarriageServiceIndecentCommunication:
    """Use of carriage service to transmit indecent communication to person under 16 years, contrary to section 474.27A Criminal Code (Cth). Maximum penalty 10 years imprisonment. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CarriageServiceIndecentCommunication"
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
class ChargingInstrument:
    """Abstract superclass for formal charging documents: criminal complaint, indictment, criminal information, and superseding instruments. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#ChargingInstrument"
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
    charging_instrument_counts: Optional[int] = field(default=None)
    filed_date: Optional[TypedLiteral] = field(default=None)


@dataclass
class CommonwealthChildAbuseOffense:
    """Child abuse offense under Commonwealth law subject to mandatory minimum sentencing provisions. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CommonwealthChildAbuseOffense"
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
class CommunityService:
    """Sentence requiring unpaid work for community benefit. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CommunityService"
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
    concurrent_with: list[CriminalSentence] = field(default_factory=list)
    sentence_concurrency: Optional[str] = field(default=None)


@dataclass
class ComputerInternetMonitoringCondition:
    """Condition requiring participation in a computer and internet monitoring program, commonly including device inventory, disclosure of accounts and credentials, consent to unannounced examination, and pr"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#ComputerInternetMonitoringCondition"
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
    condition_text: Optional[str] = field(default=None)
    defendant_pays_cost: Optional[bool] = field(default=None)
    requires_probation_approval: Optional[bool] = field(default=None)


@dataclass
class ComputerSeduceSolicitLure:
    """Florida state charge for using a computer to seduce, solicit, or lure a child to engage in sexual conduct. Covers electronic communication with minors for sexual purposes. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#ComputerSeduceSolicitLure"
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
    label: Optional[TypedLiteral] = field(default=None)
    charge_classification: Optional[str] = field(default=None)
    florida_statute: Optional[str] = field(default=None)
    computer_lure_method: Optional[str] = field(default=None)


@dataclass
class ContributingToDelinquency:
    """Florida state charge for contributing to the delinquency or dependency of a child. Applies when adult actions contribute to a child becoming delinquent or dependent. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#ContributingToDelinquency"
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
    label: Optional[TypedLiteral] = field(default=None)
    charge_classification: Optional[str] = field(default=None)
    florida_statute: Optional[str] = field(default=None)
    child_delinquency_contribution: Optional[bool] = field(default=None)


@dataclass
class ConvictionRecord:
    """A durable record that a person was convicted of one or more criminal charges (e.g., by jury verdict, bench trial, or plea agreement). Used for current-case dispositions and for limited prior-convictio"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#ConvictionRecord"
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
    charge_count: Optional[int] = field(default=None)
    conviction_date: Optional[datetime] = field(default=None)
    conviction_type: Optional[str] = field(default=None)
    prior_convictions: Optional[int] = field(default=None)


@dataclass
class CriminalCharge:
    """Formal accusation of criminal activity in CAC cases. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CriminalCharge"
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
class CriminalComplaint:
    """A written statement of the essential facts constituting the offense charged, made under oath before a magistrate judge (or clerk where authorized) prior to indictment. Fed. R. Crim. P. 3. Modeled as g"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CriminalComplaint"
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
    charging_instrument_counts: Optional[int] = field(default=None)
    filed_date: Optional[TypedLiteral] = field(default=None)


@dataclass
class CriminalInformation:
    """A charging instrument filed by the prosecutor without grand-jury action, typically after the defendant waives indictment. Fed. R. Crim. P. 7(b). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CriminalInformation"
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
    charging_instrument_counts: Optional[int] = field(default=None)
    filed_date: Optional[TypedLiteral] = field(default=None)


@dataclass
class CriminalSentence:
    """Punishment imposed by court for criminal conviction. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#CriminalSentence"
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
    concurrent_with: list[CriminalSentence] = field(default_factory=list)
    sentence_concurrency: Optional[str] = field(default=None)


@dataclass
class DefendantRole:
    """Role of individual charged with CAC crimes. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#DefendantRole"
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
class DefenseAttorneyRole:
    """Role of defense attorney representing CAC defendants. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#DefenseAttorneyRole"
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
class DirectPromotionOfSexualPerformance:
    """Florida state charge for direct promotion of a sexual performance by a child. Applies when defendant promotes, directs, or produces sexual conduct involving a minor. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#DirectPromotionOfSexualPerformance"
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
    label: Optional[TypedLiteral] = field(default=None)
    charge_classification: Optional[str] = field(default=None)
    florida_statute: Optional[str] = field(default=None)
    sexual_performance_promotion: Optional[bool] = field(default=None)


@dataclass
class EvidenceRule:
    """A rule of evidence cited in an appellate issue or opinion (e.g., Federal Rule of Evidence 403, 404(b), 414). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#EvidenceRule"
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
    rule_citation: Optional[str] = field(default=None)


@dataclass
class EvidentiaryRuling:
    """Appellate issue concerning a trial court evidentiary ruling, including admission/exclusion decisions and related prejudice analysis (e.g., under Federal Rules of Evidence). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#EvidentiaryRuling"
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
    applies_standard_of_review: list[StandardOfReview] = field(default_factory=list)
    cites_evidence_rule: list[EvidenceRule] = field(default_factory=list)
    issue_disposition: list[AppellateDisposition] = field(default_factory=list)


@dataclass
class FederalCharge:
    """Criminal charge under federal law and jurisdiction. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#FederalCharge"
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
class FederalProsecution:
    """Alias for cacontology-usa-federal:FederalProsecution, provided for continuity with existing graphs pending the namespace-alignment decision in CAC-Ontology issue #40."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#FederalProsecution"
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
class FloridaStateCharge:
    """Criminal charge under Florida state law and jurisdiction for ICAC-related offenses. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#FloridaStateCharge"
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
    label: Optional[TypedLiteral] = field(default=None)
    charge_classification: Optional[str] = field(default=None)
    florida_statute: Optional[str] = field(default=None)


@dataclass
class GeorgiaStateCharge:
    """Criminal charge under Georgia state law and jurisdiction for CAC-related offenses. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#GeorgiaStateCharge"
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
class Indictment:
    """A grand-jury charging instrument. Fed. R. Crim. P. 6, 7. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#Indictment"
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
    charging_instrument_counts: Optional[int] = field(default=None)
    filed_date: Optional[TypedLiteral] = field(default=None)


@dataclass
class InstallmentPaymentSchedule:
    """Payment schedule requiring periodic installments, typically with a monthly minimum and a commencement trigger."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#InstallmentPaymentSchedule"
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
    due_timing: Optional[str] = field(default=None)
    total_amount_usd: Optional[Any] = field(default=None)


@dataclass
class JVTAAssessment:
    """Assessment under the Justice for Victims of Trafficking Act of 2015 (18 U.S.C. § 3014)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#JVTAAssessment"
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
    concurrent_with: list[CriminalSentence] = field(default_factory=list)
    sentence_concurrency: Optional[str] = field(default=None)


@dataclass
class JudgeRole:
    """Role of judge presiding over CAC legal proceedings. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#JudgeRole"
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
class JudicialSystemSituation:
    """Broader situation involving judicial system processing of CAC cases. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#JudicialSystemSituation"


@dataclass
class JuryRole:
    """Role of jury members in CAC trial proceedings. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#JuryRole"
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
class LegalCaseSituation:
    """Complex situation encompassing the entire legal case from charges to resolution. Modeled as gUFO Situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#LegalCaseSituation"


@dataclass
class LegalProceeding:
    """Formal judicial process for prosecuting cacontology-related crimes. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#LegalProceeding"
    bail_status: Optional[str] = field(default=None)


@dataclass
class LifeImprisonmentSentence:
    """Prison sentence of life imprisonment (typically without a fixed term duration). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#LifeImprisonmentSentence"
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
    concurrent_with: list[CriminalSentence] = field(default_factory=list)
    sentence_concurrency: Optional[str] = field(default=None)


@dataclass
class LiveStreamingOffense:
    """Offense involving live streaming of child abuse, often carrying severe sentences. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#LiveStreamingOffense"
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
class LumpSumPaymentSchedule:
    """Payment schedule requiring a lump-sum payment (e.g., due immediately, on a date, or after release)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#LumpSumPaymentSchedule"
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
    due_timing: Optional[str] = field(default=None)
    total_amount_usd: Optional[Any] = field(default=None)


@dataclass
class MagistrateComplaint:
    """A criminal complaint sworn before a federal magistrate judge, typically supported by a law-enforcement agent affidavit or statement of facts. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#MagistrateComplaint"
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
    charging_instrument_counts: Optional[int] = field(default=None)
    filed_date: Optional[TypedLiteral] = field(default=None)


@dataclass
class MandatoryMinimumSentencing:
    """Sentencing under mandatory minimum provisions for Commonwealth child sexual abuse offenses. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#MandatoryMinimumSentencing"
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
    concurrent_with: list[CriminalSentence] = field(default_factory=list)
    sentence_concurrency: Optional[str] = field(default=None)


@dataclass
class MinorContactRestrictionCondition:
    """Condition restricting contact with persons under a specified age, typically requiring written probation approval and/or presence of a responsible adult aware of the offense history."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#MinorContactRestrictionCondition"
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
    condition_text: Optional[str] = field(default=None)
    defendant_pays_cost: Optional[bool] = field(default=None)
    requires_probation_approval: Optional[bool] = field(default=None)


@dataclass
class MonetaryPenalty:
    """Financial penalty including fines, restitution, or forfeiture. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#MonetaryPenalty"
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
    concurrent_with: list[CriminalSentence] = field(default_factory=list)
    sentence_concurrency: Optional[str] = field(default=None)


@dataclass
class OnlineEnticement:
    """Charge for online enticement of minors for illegal sexual activity. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#OnlineEnticement"
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
class PaymentSchedule:
    """Schedule of criminal monetary payments imposed in a judgment (AO 245B Schedule of Payments). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#PaymentSchedule"
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
    due_timing: Optional[str] = field(default=None)
    total_amount_usd: Optional[Any] = field(default=None)


@dataclass
class PleaBargaining:
    """Negotiation process between prosecution and defense for plea agreement. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#PleaBargaining"
    bail_status: Optional[str] = field(default=None)


@dataclass
class PostConvictionPhase:
    """Phase after conviction including appeals and compliance. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#PostConvictionPhase"


@dataclass
class PreTrialPhase:
    """Phase before trial including arraignment and plea bargaining. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#PreTrialPhase"


@dataclass
class PrisonSentence:
    """Sentence involving incarceration in federal or state prison. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#PrisonSentence"
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
    concurrent_with: list[CriminalSentence] = field(default_factory=list)
    sentence_concurrency: Optional[str] = field(default=None)


@dataclass
class ProbationOfficerRole:
    """Role of probation officer supervising CAC offenders. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#ProbationOfficerRole"
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
class ProbationSearchCondition:
    """Condition authorizing probation-officer searches of person, property, residence, vehicle, or devices, typically on reasonable suspicion and at a reasonable time and manner."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#ProbationSearchCondition"
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
    condition_text: Optional[str] = field(default=None)
    defendant_pays_cost: Optional[bool] = field(default=None)
    requires_probation_approval: Optional[bool] = field(default=None)


@dataclass
class ProbationSentence:
    """Supervised release with conditions instead of or after incarceration. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#ProbationSentence"
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
    concurrent_with: list[CriminalSentence] = field(default_factory=list)
    sentence_concurrency: Optional[str] = field(default=None)
    probation_conditions: Optional[int] = field(default=None)
    reporting_frequency: Optional[str] = field(default=None)
    supervision_level: Optional[str] = field(default=None)


@dataclass
class ProfessionalLicenseSurrenderCondition:
    """Condition associated with a plea agreement or sentencing outcome requiring the defendant to surrender a professional license (e.g., a nursing license)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#ProfessionalLicenseSurrenderCondition"
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
    condition_applies_to_person: list[Person] = field(default_factory=list)
    requires_license_surrender: list[ProfessionalLicense] = field(default_factory=list)


@dataclass
class ProsecutorRole:
    """Role of prosecutor handling CAC criminal charges. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#ProsecutorRole"
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
class SORNAComplianceCondition:
    """Condition requiring compliance with the Sex Offender Registration and Notification Act (34 U.S.C. § 20901 et seq.) as directed by the probation officer or registration authority."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SORNAComplianceCondition"
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
    condition_text: Optional[str] = field(default=None)
    defendant_pays_cost: Optional[bool] = field(default=None)
    requires_probation_approval: Optional[bool] = field(default=None)


@dataclass
class SentencingHearing:
    """Court proceeding where sentence is determined and imposed. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SentencingHearing"
    bail_status: Optional[str] = field(default=None)


@dataclass
class SentencingPhase:
    """Phase focused on sentencing determination and imposition. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SentencingPhase"


@dataclass
class SentencingReasonablenessIssue:
    """Appellate issue challenging the procedural and/or substantive reasonableness of a sentence (e.g., under 18 U.S.C. § 3553(a)). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SentencingReasonablenessIssue"
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
    applies_standard_of_review: list[StandardOfReview] = field(default_factory=list)
    cites_evidence_rule: list[EvidenceRule] = field(default_factory=list)
    issue_disposition: list[AppellateDisposition] = field(default_factory=list)


@dataclass
class SexOffenderTreatmentCondition:
    """Condition requiring participation in a sex-offense-specific treatment program, commonly including polygraph examination, confidentiality waiver, and cost provisions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SexOffenderTreatmentCondition"
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
    condition_text: Optional[str] = field(default=None)
    defendant_pays_cost: Optional[bool] = field(default=None)
    requires_probation_approval: Optional[bool] = field(default=None)


@dataclass
class SexTrafficking:
    """Charge for sex trafficking of minors. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SexTrafficking"
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
class SextortionCharge:
    """Criminal charge specifically related to sextortion involving sexual extortion of children through online blackmail. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SextortionCharge"
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
class SexualExploitationOfMinorCharge:
    """Georgia state charge for sexual exploitation of a minor, as reported in a Georgia Attorney General press release. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SexualExploitationOfMinorCharge"
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
class SolicitingExplicitMaterial:
    """Offense of soliciting sexually explicit material from children (e.g., from 10 foreign children via social media). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SolicitingExplicitMaterial"
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
class SpecialAssessment:
    """Mandatory special assessment imposed per count of conviction (18 U.S.C. § 3013), or a statute-specific additional assessment. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SpecialAssessment"
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
    concurrent_with: list[CriminalSentence] = field(default_factory=list)
    sentence_concurrency: Optional[str] = field(default=None)


@dataclass
class StandardOfReview:
    """Appellate standard of review applied to an appellate issue (e.g., de novo, abuse of discretion, plain error). Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#StandardOfReview"
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
    standard_of_review_type: Optional[str] = field(default=None)


@dataclass
class StateCharge:
    """Criminal charge under state law and jurisdiction. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#StateCharge"
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
class SubstanceAbuseTreatmentCondition:
    """Condition requiring substance-abuse testing and/or treatment (residential or outpatient), commonly with urinalysis limits, abstinence requirements, and cost provisions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SubstanceAbuseTreatmentCondition"
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
    condition_text: Optional[str] = field(default=None)
    defendant_pays_cost: Optional[bool] = field(default=None)
    requires_probation_approval: Optional[bool] = field(default=None)


@dataclass
class SufficiencyOfEvidenceIssue:
    """Appellate issue challenging whether the evidence was sufficient to sustain a conviction under the applicable legal standard. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SufficiencyOfEvidenceIssue"
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
    applies_standard_of_review: list[StandardOfReview] = field(default_factory=list)
    cites_evidence_rule: list[EvidenceRule] = field(default_factory=list)
    issue_disposition: list[AppellateDisposition] = field(default_factory=list)


@dataclass
class SupersedingIndictment:
    """An indictment that replaces an earlier charging instrument in the same case, typically adding, modifying, or dropping counts or defendants. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SupersedingIndictment"
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
    charging_instrument_counts: Optional[int] = field(default=None)
    filed_date: Optional[TypedLiteral] = field(default=None)


@dataclass
class SupervisedRelease:
    """Period of supervision following completion of prison sentence. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SupervisedRelease"
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
    concurrent_with: list[CriminalSentence] = field(default_factory=list)
    sentence_concurrency: Optional[str] = field(default=None)


@dataclass
class SupervisedReleaseCondition:
    """A special condition of supervised release or probation imposed in a criminal judgment. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#SupervisedReleaseCondition"
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
    condition_text: Optional[str] = field(default=None)
    defendant_pays_cost: Optional[bool] = field(default=None)
    requires_probation_approval: Optional[bool] = field(default=None)


@dataclass
class TraffickingOfPersonsForSexualServitudeCharge:
    """Georgia state charge for trafficking of persons for sexual servitude, as reported in a Georgia Attorney General press release. Modeled as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#TraffickingOfPersonsForSexualServitudeCharge"
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
class TravelingToMeetAfterComputerLure:
    """Florida state charge for traveling to meet after using a computer to lure a child. Applies when defendant uses electronic communication to lure a child and then travels to meet them. Modeled as gUFO O"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#TravelingToMeetAfterComputerLure"
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
    label: Optional[TypedLiteral] = field(default=None)
    charge_classification: Optional[str] = field(default=None)
    florida_statute: Optional[str] = field(default=None)
    electronic_communication_used: Optional[bool] = field(default=None)
    travel_occurred: Optional[bool] = field(default=None)


@dataclass
class TrialPhase:
    """Active trial phase with proceedings and evidence presentation. Modeled as anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#TrialPhase"


@dataclass
class TrialProceeding:
    """Formal trial process with jury or judge determining guilt or innocence. Modeled as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#TrialProceeding"
    bail_status: Optional[str] = field(default=None)


@dataclass
class VictimRole:
    """Role of victim in CAC legal proceedings. Modeled as anti-rigid gUFO Role."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/legal-outcomes#VictimRole"
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

