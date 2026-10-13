"""CAC Ontology - Crimes Against Children — cacontology-law-enforcement-corruption module."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AccessPrivilegeAbuse:
    """Abuse of special access privileges granted to law enforcement personnel."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#AccessPrivilegeAbuse"


@dataclass
class AuthoritySymbolExploitation:
    """Use of badges, weapons, or other authority symbols to enhance exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#AuthoritySymbolExploitation"


@dataclass
class BadgeDisplayedProduction:
    """CSAM production where law enforcement badge is prominently displayed."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#BadgeDisplayedProduction"


@dataclass
class CorruptArmyReservist:
    """Army reservist engaged in child exploitation activities while in military uniform."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#CorruptArmyReservist"
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
class CorruptLawEnforcementOfficer:
    """Law enforcement officer engaged in child exploitation activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#CorruptLawEnforcementOfficer"
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
class CorruptMetropolitanPoliceDepartmentOfficer:
    """Former or current metropolitan police department officer engaged in child trafficking."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#CorruptMetropolitanPoliceDepartmentOfficer"
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
class CorruptStateTrooper:
    """State trooper engaged in child exploitation activities while in uniform."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#CorruptStateTrooper"
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
class DatabaseAccessAbuse:
    """Misuse of law enforcement database access for personal exploitation activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#DatabaseAccessAbuse"


@dataclass
class EvidenceManipulation:
    """Manipulation or destruction of evidence to protect exploitation activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#EvidenceManipulation"


@dataclass
class ExternalOversightInvestigation:
    """Investigation by external agency into law enforcement corruption."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#ExternalOversightInvestigation"


@dataclass
class FormerLawEnforcementOfficer:
    """Former law enforcement officer using previous position and contacts for exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#FormerLawEnforcementOfficer"
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
class InformationLeakage:
    """Leaking of law enforcement information to facilitate exploitation or trafficking."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#InformationLeakage"


@dataclass
class InsiderThreat:
    """Threat posed by individuals within law enforcement or military who exploit their position for criminal activity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#InsiderThreat"


@dataclass
class InsiderThreatDetection:
    """Detection of corruption within law enforcement or military personnel."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#InsiderThreatDetection"


@dataclass
class InternalAffairsInvestigation:
    """Investigation by internal affairs department into officer corruption."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#InternalAffairsInvestigation"


@dataclass
class InvestigativeAuthorityAbuse:
    """Abuse of investigative powers and access for exploitation purposes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#InvestigativeAuthorityAbuse"


@dataclass
class LawEnforcementCorruption:
    """Corruption involving law enforcement personnel in child exploitation activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#LawEnforcementCorruption"


@dataclass
class MilitaryUniformProduction:
    """Production of CSAM while wearing military uniform."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#MilitaryUniformProduction"


@dataclass
class OfficerChildTrafficking:
    """Child trafficking conducted by law enforcement officers using their position and authority."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#OfficerChildTrafficking"


@dataclass
class OfficerProducedCSAM:
    """Child sexual abuse material produced by law enforcement officers, often while in uniform."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#OfficerProducedCSAM"


@dataclass
class OfficialVehicleExploitation:
    """Use of official law enforcement vehicles in exploitation activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#OfficialVehicleExploitation"


@dataclass
class PoliceUniformProduction:
    """Production of CSAM while wearing police uniform."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#PoliceUniformProduction"


@dataclass
class PositionOfAuthorityAbuse:
    """Abuse of law enforcement or military position of authority for exploitation purposes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#PositionOfAuthorityAbuse"


@dataclass
class PublicIntegrityInvestigation:
    """Investigation into public integrity violations by law enforcement personnel."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#PublicIntegrityInvestigation"


@dataclass
class UniformBasedExploitation:
    """Exploitation activity conducted while wearing official law enforcement or military uniform for authority enhancement."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#UniformBasedExploitation"


@dataclass
class UniformEnhancedProduction:
    """Production of CSAM enhanced by wearing official uniform to project authority."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#UniformEnhancedProduction"


@dataclass
class WhistleblowerReport:
    """Report by insider regarding corruption within law enforcement organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#WhistleblowerReport"

