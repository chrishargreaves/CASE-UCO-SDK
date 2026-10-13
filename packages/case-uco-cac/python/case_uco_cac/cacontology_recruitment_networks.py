"""CAC Ontology - Crimes Against Children — cacontology-recruitment-networks module."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AcademicStruggles:
    """Academic difficulties creating vulnerability to recruitment offers."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#AcademicStruggles"
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
class AfterSchoolRecruitment:
    """Recruitment occurring after school hours when supervision is reduced."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#AfterSchoolRecruitment"
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
class AttendanceProblems:
    """School attendance issues that may indicate or facilitate trafficking involvement."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#AttendanceProblems"
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
class ClassmateIntroduction:
    """Introduction of new victim to trafficker through existing victim who is a classmate."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#ClassmateIntroduction"


@dataclass
class ClassmateRecruitmentNetwork:
    """Recruitment network operating within educational institutions using existing victims to recruit classmates."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#ClassmateRecruitmentNetwork"
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
class CoercedPeerRecruitment:
    """Recruitment where existing victims are forced or coerced to recruit their peers."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#CoercedPeerRecruitment"


@dataclass
class EducationalInstitution:
    """School or educational facility where recruitment occurs or reporting takes place."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#EducationalInstitution"
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
class ExtracurricularRecruitment:
    """Recruitment occurring during extracurricular activities or school events."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#ExtracurricularRecruitment"
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
class FriendshipExploitation:
    """Exploitation of existing friendships and trust relationships between minors for recruitment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#FriendshipExploitation"


@dataclass
class LunchBreakRecruitment:
    """Recruitment occurring during lunch breaks or between classes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#LunchBreakRecruitment"
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
class MandatoryReportingActivation:
    """Activation of mandatory reporting requirements by school personnel."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#MandatoryReportingActivation"


@dataclass
class PeerInfluenceRecruitment:
    """Recruitment leveraging peer pressure and social influence among minors."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#PeerInfluenceRecruitment"


@dataclass
class PeerPressureVulnerability:
    """Susceptibility to peer pressure enabling recruitment through classmates."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#PeerPressureVulnerability"
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
class PeerRecruitmentNetwork:
    """Network of traffickers utilizing existing victims to recruit new victims through peer relationships and social connections."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#PeerRecruitmentNetwork"
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
class RecruitmentIncentive:
    """Incentives offered to existing victims for successful recruitment of new victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#RecruitmentIncentive"


@dataclass
class RecruitmentPunishment:
    """Punishment threatened or applied to victims who fail to recruit new victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#RecruitmentPunishment"


@dataclass
class RecruitmentQuota:
    """System where existing victims must recruit specified number of new victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#RecruitmentQuota"


@dataclass
class RecruitmentTiming:
    """Temporal patterns and timing of recruitment activities within educational environments."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#RecruitmentTiming"
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
class SchoolBasedRecruitment:
    """Trafficking recruitment occurring within or through school environments and relationships."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#SchoolBasedRecruitment"


@dataclass
class SchoolBasedReporting:
    """Reporting of trafficking incidents through educational institution personnel."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#SchoolBasedReporting"


@dataclass
class SchoolCounselor:
    """School counselor who may receive disclosures from trafficking victims."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#SchoolCounselor"
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
class SchoolHoursRecruitment:
    """Recruitment occurring during regular school hours through peer interactions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#SchoolHoursRecruitment"
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
class SchoolPoliceContact:
    """Contact made by school personnel to law enforcement regarding trafficking concerns."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#SchoolPoliceContact"


@dataclass
class SchoolSocialWorker:
    """Social worker employed by educational institution who receives victim reports."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#SchoolSocialWorker"
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
class SchoolStaffMember:
    """Employee of educational institution involved in reporting or responding to trafficking."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#SchoolStaffMember"
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
class SchoolVulnerabilityFactor:
    """Factors within educational environment that increase vulnerability to recruitment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#SchoolVulnerabilityFactor"
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
class SocialConnectionLeverage:
    """Leveraging existing social connections between victims to facilitate new recruitment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#SocialConnectionLeverage"


@dataclass
class SocialIsolationAtSchool:
    """Student isolation within school environment making them vulnerable to recruitment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#SocialIsolationAtSchool"
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
class SocialWorkerReport:
    """Report made by school social worker to law enforcement regarding trafficking victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#SocialWorkerReport"


@dataclass
class StudentNetworkExploitation:
    """Exploitation of student social networks and peer relationships for trafficking recruitment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#StudentNetworkExploitation"


@dataclass
class TeacherReporter:
    """Teacher who identifies signs of trafficking or receives disclosures from students."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#TeacherReporter"
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
class VictimMediatedRecruitment:
    """Recruitment of new victims through existing trafficking victims acting as intermediaries."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#VictimMediatedRecruitment"


@dataclass
class VictimSchoolDisclosure:
    """Disclosure by trafficking victim to school personnel about their situation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/recruitment-networks#VictimSchoolDisclosure"

