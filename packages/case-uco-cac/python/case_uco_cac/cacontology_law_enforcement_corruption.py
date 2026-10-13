"""CAC Ontology - Crimes Against Children — cacontology_law_enforcement_corruption module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar

from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AccessPrivilegeAbuse", "AuthoritySymbolExploitation", "BadgeDisplayedProduction", "CorruptArmyReservist", "CorruptLawEnforcementOfficer", "CorruptMetropolitanPoliceDepartmentOfficer", "CorruptStateTrooper", "DatabaseAccessAbuse", "EvidenceManipulation", "ExternalOversightInvestigation", "FormerLawEnforcementOfficer", "InformationLeakage", "InsiderThreat", "InsiderThreatDetection", "InternalAffairsInvestigation", "InvestigativeAuthorityAbuse", "LawEnforcementCorruption", "MilitaryUniformProduction", "OfficerChildTrafficking", "OfficerProducedCSAM", "OfficialVehicleExploitation", "PoliceUniformProduction", "PositionOfAuthorityAbuse", "PublicIntegrityInvestigation", "UniformBasedExploitation", "UniformEnhancedProduction", "WhistleblowerReport"]


@dataclass
class LawEnforcementCorruption(_cac_core.ExploitationEvent):
    """Corruption involving law enforcement personnel in child exploitation activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#LawEnforcementCorruption"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PositionOfAuthorityAbuse(LawEnforcementCorruption):
    """Abuse of law enforcement or military position of authority for exploitation purposes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#PositionOfAuthorityAbuse"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InvestigativeAuthorityAbuse(PositionOfAuthorityAbuse):
    """Abuse of investigative powers and access for exploitation purposes."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#InvestigativeAuthorityAbuse"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AccessPrivilegeAbuse(InvestigativeAuthorityAbuse):
    """Abuse of special access privileges granted to law enforcement personnel."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#AccessPrivilegeAbuse"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InsiderThreat(LawEnforcementCorruption):
    """Threat posed by individuals within law enforcement or military who exploit their position for criminal activity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#InsiderThreat"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class UniformBasedExploitation(InsiderThreat):
    """Exploitation activity conducted while wearing official law enforcement or military uniform for authority enhancement."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#UniformBasedExploitation"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AuthoritySymbolExploitation(UniformBasedExploitation):
    """Use of badges, weapons, or other authority symbols to enhance exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#AuthoritySymbolExploitation"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class BadgeDisplayedProduction(AuthoritySymbolExploitation):
    """CSAM production where law enforcement badge is prominently displayed."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#BadgeDisplayedProduction"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CorruptLawEnforcementOfficer(_cac_core.Role):
    """Law enforcement officer engaged in child exploitation activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#CorruptLawEnforcementOfficer"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CorruptArmyReservist(CorruptLawEnforcementOfficer):
    """Army reservist engaged in child exploitation activities while in military uniform."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#CorruptArmyReservist"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CorruptMetropolitanPoliceDepartmentOfficer(CorruptLawEnforcementOfficer):
    """Former or current metropolitan police department officer engaged in child trafficking."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#CorruptMetropolitanPoliceDepartmentOfficer"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CorruptStateTrooper(CorruptLawEnforcementOfficer):
    """State trooper engaged in child exploitation activities while in uniform."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#CorruptStateTrooper"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DatabaseAccessAbuse(AccessPrivilegeAbuse):
    """Misuse of law enforcement database access for personal exploitation activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#DatabaseAccessAbuse"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EvidenceManipulation(InvestigativeAuthorityAbuse):
    """Manipulation or destruction of evidence to protect exploitation activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#EvidenceManipulation"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InsiderThreatDetection(_cac_core.DetectionEvent):
    """Detection of corruption within law enforcement or military personnel."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#InsiderThreatDetection"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ExternalOversightInvestigation(InsiderThreatDetection):
    """Investigation by external agency into law enforcement corruption."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#ExternalOversightInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FormerLawEnforcementOfficer(CorruptLawEnforcementOfficer):
    """Former law enforcement officer using previous position and contacts for exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#FormerLawEnforcementOfficer"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InformationLeakage(InvestigativeAuthorityAbuse):
    """Leaking of law enforcement information to facilitate exploitation or trafficking."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#InformationLeakage"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InternalAffairsInvestigation(InsiderThreatDetection):
    """Investigation by internal affairs department into officer corruption."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#InternalAffairsInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OfficerProducedCSAM(UniformBasedExploitation):
    """Child sexual abuse material produced by law enforcement officers, often while in uniform."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#OfficerProducedCSAM"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class UniformEnhancedProduction(OfficerProducedCSAM):
    """Production of CSAM enhanced by wearing official uniform to project authority."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#UniformEnhancedProduction"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MilitaryUniformProduction(UniformEnhancedProduction):
    """Production of CSAM while wearing military uniform."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#MilitaryUniformProduction"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OfficerChildTrafficking(PositionOfAuthorityAbuse):
    """Child trafficking conducted by law enforcement officers using their position and authority."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#OfficerChildTrafficking"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OfficialVehicleExploitation(PositionOfAuthorityAbuse):
    """Use of official law enforcement vehicles in exploitation activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#OfficialVehicleExploitation"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PoliceUniformProduction(UniformEnhancedProduction):
    """Production of CSAM while wearing police uniform."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#PoliceUniformProduction"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PublicIntegrityInvestigation(ExternalOversightInvestigation):
    """Investigation into public integrity violations by law enforcement personnel."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#PublicIntegrityInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class WhistleblowerReport(InsiderThreatDetection):
    """Report by insider regarding corruption within law enforcement organization."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/law-enforcement-corruption#WhistleblowerReport"
    NAMESPACE_PREFIX: str = "cacontology-law-enforcement-corruption"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
