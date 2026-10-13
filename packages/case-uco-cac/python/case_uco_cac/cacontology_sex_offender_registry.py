"""CAC Ontology - Crimes Against Children — cacontology_sex_offender_registry module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional, Union

import case_uco.uco.core as _uco_core
import case_uco.uco.identity as _uco_identity
import case_uco.uco.location as _uco_location
import case_uco.uco.observable as _uco_observable
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AddressHistory", "AgeAwareExploitation", "Alias", "AnnualRegistrationReview", "BidirectionalContentExchange", "CommunityNotification", "ComplianceBasedArrest", "ComplianceHistory", "ComplianceScheduleCoordination", "ComplianceViolation", "ContactRestriction", "ConvictingOffense", "CourtOrder", "CrossStateDigitalInvestigation", "CrossStateRecidivism", "DigitalRecidivismPattern", "EducationInformation", "EmploymentInformation", "EmploymentRestriction", "FailureToRegisterOffense", "FalseInformationRegistrationOffense", "GeographicRestriction", "HighVolumeDigitalExploitation", "IdentifyingMark", "InternetInformation", "InternetRestriction", "InternetServiceProvider", "MultiModalDigitalEvidence", "NotificationTier", "OffenderDeviceSearchWarrant", "OffenderProfile", "OffenseClassification", "OnlineIdentifier", "PersonalIdentifiers", "Photograph", "PhysicalDescription", "PrimaryResidence", "ProfessionalLicense", "PublicWebsite", "RecidivistSexOffender", "RegisteredAddress", "RegisteredSexOffender", "RegisteredVehicle", "RegistrationAlert", "RegistrationRecord", "RegistrationRequirement", "RegistrationRestriction", "RegistrationReviewArrest", "RegistrationStatus", "RegistrationUpdate", "RegistryAgency", "RegistryOfficer", "RegistrySystem", "SchoolLocation", "SexOffenderRegistry", "SocialMediaAccount", "TemporaryAddress", "VehicleInformation", "VerificationCheck", "VictimDeviceForensics", "VictimInformation", "WorkLocation"]


@dataclass
class AddressHistory(_uco_core.UcoObject):
    """Historical record of registered addresses."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#AddressHistory"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class AgeAwareExploitation(_uco_core.UcoObject):
    """Exploitation where offender explicitly acknowledges victim's minor status but continues criminal activity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#AgeAwareExploitation"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class Alias(_uco_identity.Identity):
    """Known alias or alternate name used by registered sex offender."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#Alias"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class VerificationCheck(_cac_core.LegalEvent):
    """Official verification of sex offender registration information."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#VerificationCheck"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    performer: Optional[Person] = field(default=None, metadata={'jsonld_key': 'uco-action:performer', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/identity/Person', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class AnnualRegistrationReview(VerificationCheck):
    """Annual review and update of sex offender registration information."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#AnnualRegistrationReview"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class BidirectionalContentExchange(_uco_core.UcoObject):
    """Exchange where offender both sends explicit content to victim and solicits/receives explicit content from victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#BidirectionalContentExchange"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CommunityNotification(_cac_core.LegalEvent):
    """Notification to community about registered sex offender."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#CommunityNotification"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ComplianceBasedArrest(_cac_core.InvestigativeAction):
    """Arrest coordinated with scheduled compliance activity such as annual registration review."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#ComplianceBasedArrest"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ComplianceHistory(_uco_core.UcoObject):
    """History of compliance with registration requirements."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#ComplianceHistory"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ComplianceScheduleCoordination(_cac_core.CoordinationEvent):
    """Coordination between law enforcement investigations and compliance schedules for arrest timing."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#ComplianceScheduleCoordination"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ComplianceViolation(_uco_core.UcoObject):
    """Violation of sex offender registration requirements."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#ComplianceViolation"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    violation_category: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sex-offender-registry:violationCategory', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class RegistrationRestriction(_uco_core.UcoObject):
    """Restriction placed on registered sex offender."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#RegistrationRestriction"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ContactRestriction(RegistrationRestriction):
    """Restriction on contact with certain individuals or groups."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#ContactRestriction"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ConvictingOffense(_uco_core.UcoObject):
    """Criminal offense that resulted in sex offender registration requirement."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#ConvictingOffense"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    conviction_date: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-sex-offender-registry:convictionDate', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#date', 'alternate_range_iris': [], 'literal_datatype': True})
    offense_description: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sex-offender-registry:offenseDescription', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    sentence_length: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sex-offender-registry:sentenceLength', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class CourtOrder(_uco_observable.ObservableObject):
    """Court order mandating sex offender registration."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#CourtOrder"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CrossStateDigitalInvestigation(_uco_core.UcoObject):
    """Investigation involving registered sex offender targeting victims across state boundaries using digital platforms."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#CrossStateDigitalInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CrossStateRecidivism(_uco_core.UcoObject):
    """Pattern of recidivism involving offenses across state boundaries."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#CrossStateRecidivism"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class DigitalRecidivismPattern(_uco_core.UcoObject):
    """Pattern of repeat sexual offenses using digital communication platforms."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#DigitalRecidivismPattern"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class EducationInformation(_uco_core.UcoObject):
    """Educational enrollment information for registered sex offender."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#EducationInformation"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class EmploymentInformation(_uco_core.UcoObject):
    """Current employment information for registered sex offender."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#EmploymentInformation"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#date', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class EmploymentRestriction(RegistrationRestriction):
    """Restriction on types of employment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#EmploymentRestriction"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FailureToRegisterOffense(ConvictingOffense):
    """Criminal offense for failing to register or update required information in a sex offender registry. Typically serves as a registry-triggering or enhancing offense for compliance analytics."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#FailureToRegisterOffense"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FalseInformationRegistrationOffense(ConvictingOffense):
    """Criminal offense for knowingly providing false or misleading information in connection with sex offender registration (e.g., false address, contact information, or online identifiers)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#FalseInformationRegistrationOffense"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class GeographicRestriction(RegistrationRestriction):
    """Geographic area where offender is restricted from being."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#GeographicRestriction"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HighVolumeDigitalExploitation(_uco_core.UcoObject):
    """Digital exploitation involving thousands of messages or communications over extended period."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#HighVolumeDigitalExploitation"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class IdentifyingMark(_uco_core.UcoObject):
    """Distinctive physical mark (scar, tattoo, birthmark) for identification."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#IdentifyingMark"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class InternetInformation(_uco_core.UcoObject):
    """Internet-related information for registered sex offender."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#InternetInformation"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class InternetRestriction(RegistrationRestriction):
    """Restriction on internet use or online activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#InternetRestriction"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InternetServiceProvider(_uco_identity.Organization):
    """Internet service provider used by registered sex offender."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#InternetServiceProvider"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class MultiModalDigitalEvidence(_uco_observable.ObservableObject):
    """Digital evidence containing multiple content types (text, images, audio, video) in single exploitation case."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#MultiModalDigitalEvidence"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class NotificationTier(_uco_core.UcoObject):
    """Classification tier determining level of community notification required."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#NotificationTier"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class OffenderDeviceSearchWarrant(_uco_observable.ObservableObject):
    """Search warrant executed on registered sex offender's residence and devices for digital evidence recovery."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#OffenderDeviceSearchWarrant"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class OffenderProfile(_uco_core.UcoObject):
    """Comprehensive profile of registered sex offender including all required information."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#OffenderProfile"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    last_update: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'cacontology-sex-offender-registry:lastUpdate', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class OffenseClassification(_uco_core.UcoObject):
    """Classification of sexual offense (felony/misdemeanor, degree, special categories)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#OffenseClassification"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class OnlineIdentifier(_uco_identity.Identity):
    """Online username, email, or identifier used by registered sex offender."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#OnlineIdentifier"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PersonalIdentifiers(_uco_core.UcoObject):
    """Collection of identifiers for registered sex offender (SSN, DOB, aliases, etc.)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#PersonalIdentifiers"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class Photograph(_uco_observable.ObservableObject):
    """Official photograph of registered sex offender."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#Photograph"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PhysicalDescription(_uco_core.UcoObject):
    """Physical description of registered sex offender (height, weight, scars, tattoos)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#PhysicalDescription"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    eye_color: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sex-offender-registry:eyeColor', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    hair_color: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sex-offender-registry:hairColor', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    height: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sex-offender-registry:height', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    race: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sex-offender-registry:race', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    weight: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sex-offender-registry:weight', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class RegisteredAddress(_uco_location.Location):
    """Official registered address of sex offender."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#RegisteredAddress"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    city: Optional[str] = field(default=None, metadata={'jsonld_key': 'uco-location:city', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    postal_code: Optional[str] = field(default=None, metadata={'jsonld_key': 'uco-location:postalCode', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    state: Optional[str] = field(default=None, metadata={'jsonld_key': 'uco-location:state', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    street: Optional[str] = field(default=None, metadata={'jsonld_key': 'uco-location:street', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PrimaryResidence(RegisteredAddress):
    """Primary residential address where offender lives."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#PrimaryResidence"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#date', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class ProfessionalLicense(_uco_observable.ObservableObject):
    """Professional license held by registered sex offender."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#ProfessionalLicense"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PublicWebsite(_uco_observable.ObservableObject):
    """Public website for searching sex offender registry information."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#PublicWebsite"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class RegisteredSexOffender(_cac_core.Role):
    """Legal status/role that a person can gain or lose; individual required to register as a sex offender."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#RegisteredSexOffender"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    date_of_birth: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-sex-offender-registry:dateOfBirth', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#date', 'alternate_range_iris': [], 'literal_datatype': True})
    full_name: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sex-offender-registry:fullName', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    registered_in: list[SexOffenderRegistry] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-sex-offender-registry:registeredIn', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://cacontology.projectvic.org/sex-offender-registry#SexOffenderRegistry', 'alternate_range_iris': []})
    sex: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sex-offender-registry:sex', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    social_security_number: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sex-offender-registry:socialSecurityNumber', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class RecidivistSexOffender(RegisteredSexOffender):
    """Registered sex offender who has committed subsequent sexual offenses after initial conviction and registration."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#RecidivistSexOffender"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    post_registration_event: list[ChildSexualAbuseEvent] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-sex-offender-registry:postRegistrationEvent', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'https://cacontology.projectvic.org#ChildSexualAbuseEvent', 'alternate_range_iris': []})


@dataclass
class VehicleInformation(_uco_observable.ObservableObject):
    """Information about vehicles owned or operated by registered sex offender."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#VehicleInformation"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    license_plate: Optional[str] = field(default=None, metadata={'jsonld_key': 'uco-observable:licensePlate', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    make: Optional[str] = field(default=None, metadata={'jsonld_key': 'uco-observable:make', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    model: Optional[str] = field(default=None, metadata={'jsonld_key': 'uco-observable:model', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    year: Optional[int] = field(default=None, metadata={'jsonld_key': 'uco-observable:year', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#integer', 'alternate_range_iris': []})


@dataclass
class RegisteredVehicle(VehicleInformation):
    """Vehicle registered to sex offender."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#RegisteredVehicle"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RegistrationAlert(_uco_core.UcoObject):
    """Alert generated by registry system (non-compliance, address change, etc.)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#RegistrationAlert"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class RegistrationRecord(_uco_core.UcoObject):
    """Official record of sex offender registration including all required data elements."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#RegistrationRecord"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    expiration_date: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-sex-offender-registry:expirationDate', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#date', 'alternate_range_iris': [], 'literal_datatype': True})
    lifetime_registration: Optional[bool] = field(default=None, metadata={'jsonld_key': 'cacontology-sex-offender-registry:lifetimeRegistration', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#boolean', 'alternate_range_iris': []})
    registration_date: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'cacontology-sex-offender-registry:registrationDate', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#date', 'alternate_range_iris': [], 'literal_datatype': True})
    registration_number: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sex-offender-registry:registrationNumber', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    tier: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-sex-offender-registry:tier', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#integer', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class RegistrationRequirement(_uco_core.UcoObject):
    """Specific requirement for sex offender registration (location, frequency, restrictions)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#RegistrationRequirement"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class RegistrationReviewArrest(ComplianceBasedArrest):
    """Arrest executed when offender arrives for scheduled registration review or update."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#RegistrationReviewArrest"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RegistrationStatus(_uco_core.UcoObject):
    """Current status of sex offender registration (active, inactive, non-compliant, etc.)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#RegistrationStatus"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    start_time: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class RegistrationUpdate(_cac_core.LegalEvent):
    """Update to sex offender registration information."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#RegistrationUpdate"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RegistryAgency(_uco_identity.Organization):
    """Law enforcement agency responsible for maintaining sex offender registry."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#RegistryAgency"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class RegistryOfficer(_cac_core.Role):
    """Officer responsible for sex offender registration management."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#RegistryOfficer"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RegistrySystem(_uco_core.UcoObject):
    """Information system used to manage sex offender registry."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#RegistrySystem"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SchoolLocation(_uco_location.Location):
    """Educational institution where offender is enrolled."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#SchoolLocation"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SexOffenderRegistry(_uco_core.UcoObject):
    """Registry system maintaining information about registered sex offenders."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#SexOffenderRegistry"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    managed_by: Optional[Organization] = field(default=None, metadata={'jsonld_key': 'cacontology-sex-offender-registry:managedBy', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/identity/Organization', 'alternate_range_iris': []})


@dataclass
class SocialMediaAccount(OnlineIdentifier):
    """Social media account belonging to registered sex offender."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#SocialMediaAccount"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TemporaryAddress(RegisteredAddress):
    """Temporary address where offender will be residing."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#TemporaryAddress"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimDeviceForensics(_cac_core.InvestigativeAction):
    """Forensic examination of victim's device to recover evidence of digital exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#VictimDeviceForensics"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimInformation(_uco_core.UcoObject):
    """Information about victims relevant to registration (age, relationship, count)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#VictimInformation"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    victim_age: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-sex-offender-registry:victimAge', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#integer', 'alternate_range_iris': []})
    victim_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-sex-offender-registry:victimCount', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#integer', 'alternate_range_iris': []})
    victim_relationship: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-sex-offender-registry:victimRelationship', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class WorkLocation(_uco_location.Location):
    """Location where registered sex offender is employed."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/sex-offender-registry#WorkLocation"
    NAMESPACE_PREFIX: str = "cacontology-sex-offender-registry"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
