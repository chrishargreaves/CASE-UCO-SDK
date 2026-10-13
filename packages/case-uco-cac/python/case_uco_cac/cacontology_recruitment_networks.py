"""CAC Ontology - Crimes Against Children — cacontology_recruitment_networks module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar, Optional

import case_uco.uco.core as _uco_core
import case_uco.uco.identity as _uco_identity
import case_uco.uco.role as _uco_role
from case_uco_cac import cac_core as _cac_core
from case_uco_cac import cacontology_sex_trafficking as _cacontology_sex_trafficking
from case_uco_cac._context import NAMESPACES

__all__ = ["AcademicStruggles", "AfterSchoolRecruitment", "AttendanceProblems", "ClassmateIntroduction", "ClassmateRecruitmentNetwork", "CoercedPeerRecruitment", "EducationalInstitution", "ExtracurricularRecruitment", "FriendshipExploitation", "LunchBreakRecruitment", "MandatoryReportingActivation", "PeerInfluenceRecruitment", "PeerPressureVulnerability", "PeerRecruitmentNetwork", "RecruitmentIncentive", "RecruitmentPunishment", "RecruitmentQuota", "RecruitmentTiming", "SchoolBasedRecruitment", "SchoolBasedReporting", "SchoolCounselor", "SchoolHoursRecruitment", "SchoolPoliceContact", "SchoolSocialWorker", "SchoolStaffMember", "SchoolVulnerabilityFactor", "SocialConnectionLeverage", "SocialIsolationAtSchool", "SocialWorkerReport", "StudentNetworkExploitation", "TeacherReporter", "VictimMediatedRecruitment", "VictimSchoolDisclosure"]


@dataclass
class SchoolVulnerabilityFactor(_uco_core.UcoObject):
    """Factors within educational environment that increase vulnerability to recruitment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#SchoolVulnerabilityFactor"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class AcademicStruggles(SchoolVulnerabilityFactor):
    """Academic difficulties creating vulnerability to recruitment offers."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#AcademicStruggles"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RecruitmentTiming(_uco_core.UcoObject):
    """Temporal patterns and timing of recruitment activities within educational environments."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#RecruitmentTiming"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class AfterSchoolRecruitment(RecruitmentTiming):
    """Recruitment occurring after school hours when supervision is reduced."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#AfterSchoolRecruitment"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AttendanceProblems(SchoolVulnerabilityFactor):
    """School attendance issues that may indicate or facilitate trafficking involvement."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#AttendanceProblems"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimMediatedRecruitment(_cacontology_sex_trafficking.VictimRecruitment):
    """Recruitment of new victims through existing trafficking victims acting as intermediaries."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#VictimMediatedRecruitment"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ClassmateIntroduction(VictimMediatedRecruitment):
    """Introduction of new victim to trafficker through existing victim who is a classmate."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#ClassmateIntroduction"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PeerRecruitmentNetwork(_uco_core.UcoObject):
    """Network of traffickers utilizing existing victims to recruit new victims through peer relationships and social connections."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#PeerRecruitmentNetwork"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ClassmateRecruitmentNetwork(PeerRecruitmentNetwork):
    """Recruitment network operating within educational institutions using existing victims to recruit classmates."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#ClassmateRecruitmentNetwork"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CoercedPeerRecruitment(VictimMediatedRecruitment):
    """Recruitment where existing victims are forced or coerced to recruit their peers."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#CoercedPeerRecruitment"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EducationalInstitution(_uco_identity.Organization):
    """School or educational facility where recruitment occurs or reporting takes place."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#EducationalInstitution"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ExtracurricularRecruitment(AfterSchoolRecruitment):
    """Recruitment occurring during extracurricular activities or school events."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#ExtracurricularRecruitment"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PeerInfluenceRecruitment(VictimMediatedRecruitment):
    """Recruitment leveraging peer pressure and social influence among minors."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#PeerInfluenceRecruitment"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FriendshipExploitation(PeerInfluenceRecruitment):
    """Exploitation of existing friendships and trust relationships between minors for recruitment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#FriendshipExploitation"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SchoolHoursRecruitment(RecruitmentTiming):
    """Recruitment occurring during regular school hours through peer interactions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#SchoolHoursRecruitment"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LunchBreakRecruitment(SchoolHoursRecruitment):
    """Recruitment occurring during lunch breaks or between classes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#LunchBreakRecruitment"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SchoolBasedReporting(_cac_core.CoordinationEvent):
    """Reporting of trafficking incidents through educational institution personnel."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#SchoolBasedReporting"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MandatoryReportingActivation(SchoolBasedReporting):
    """Activation of mandatory reporting requirements by school personnel."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#MandatoryReportingActivation"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PeerPressureVulnerability(SchoolVulnerabilityFactor):
    """Susceptibility to peer pressure enabling recruitment through classmates."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#PeerPressureVulnerability"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RecruitmentIncentive(CoercedPeerRecruitment):
    """Incentives offered to existing victims for successful recruitment of new victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#RecruitmentIncentive"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RecruitmentPunishment(CoercedPeerRecruitment):
    """Punishment threatened or applied to victims who fail to recruit new victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#RecruitmentPunishment"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RecruitmentQuota(CoercedPeerRecruitment):
    """System where existing victims must recruit specified number of new victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#RecruitmentQuota"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SchoolBasedRecruitment(_cacontology_sex_trafficking.VictimRecruitment):
    """Trafficking recruitment occurring within or through school environments and relationships."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#SchoolBasedRecruitment"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SchoolStaffMember(_uco_role.Role):
    """Employee of educational institution involved in reporting or responding to trafficking."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#SchoolStaffMember"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SchoolCounselor(SchoolStaffMember):
    """School counselor who may receive disclosures from trafficking victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#SchoolCounselor"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SchoolPoliceContact(SchoolBasedReporting):
    """Contact made by school personnel to law enforcement regarding trafficking concerns."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#SchoolPoliceContact"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SchoolSocialWorker(SchoolStaffMember):
    """Social worker employed by educational institution who receives victim reports."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#SchoolSocialWorker"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SocialConnectionLeverage(FriendshipExploitation):
    """Leveraging existing social connections between victims to facilitate new recruitment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#SocialConnectionLeverage"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SocialIsolationAtSchool(SchoolVulnerabilityFactor):
    """Student isolation within school environment making them vulnerable to recruitment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#SocialIsolationAtSchool"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SocialWorkerReport(SchoolBasedReporting):
    """Report made by school social worker to law enforcement regarding trafficking victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#SocialWorkerReport"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StudentNetworkExploitation(SchoolBasedRecruitment):
    """Exploitation of student social networks and peer relationships for trafficking recruitment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#StudentNetworkExploitation"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TeacherReporter(SchoolStaffMember):
    """Teacher who identifies signs of trafficking or receives disclosures from students."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#TeacherReporter"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimSchoolDisclosure(SchoolBasedReporting):
    """Disclosure by trafficking victim to school personnel about their situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#VictimSchoolDisclosure"
    NAMESPACE_PREFIX: str = "cacontology-recruitment-networks"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
