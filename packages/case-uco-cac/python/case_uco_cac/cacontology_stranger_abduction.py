"""CAC Ontology - Crimes Against Children — cacontology_stranger_abduction module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional

import case_uco.case.investigation as _case_investigation
import case_uco.uco.core as _uco_core
import case_uco.uco.observable as _uco_observable
from case_uco_cac import cac_core as _cac_core
from case_uco_cac import cacontology as _cacontology
from case_uco_cac import cacontology_physical_evidence as _cacontology_physical_evidence
from case_uco_cac._context import NAMESPACES

__all__ = ["AbductionExploitationPattern", "AbductionSceneEvidence", "AgeBasedVulnerability", "ApartmentIsolation", "BluntObjectThreats", "ClothingDisguise", "ComplianceEnforcement", "ComplianceUnderThreat", "ControlledEnvironmentExploitation", "DelayedDisclosure", "DisguiseBasedConcealment", "DisguiseEvidence", "EscapeAttempt", "ExploitationSceneEvidence", "FacialConcealment", "FireEscapeEntry", "FirearmThreats", "ForcedLocationEntry", "HoodedConcealment", "HumiliationBasedExploitation", "ImmediateDisclosure", "ImmediateExploitation", "ImpliedWeaponThreats", "InitialResistance", "IsolatedChildTargeting", "IsolationVulnerability", "KnifeThreats", "LocationBasedExploitation", "LocationIsolation", "MaskConcealment", "MovementRestriction", "OpportunisticPredation", "OpportunityBasedTargeting", "PhysicalForceWithWeapon", "PhysicalIntimidation", "PostAbductionReporting", "PublicSpaceAbduction", "RandomVictimSelection", "RitualizedExploitation", "RoutineActivityTargeting", "SchoolRouteAbduction", "SchoolRouteTargeting", "SecondaryLocationControl", "SilenceEnforcement", "SizeBasedVulnerability", "SkiMaskConcealment", "StrangerAbduction", "StrangerAbductionInvestigation", "StreetLevelAbduction", "SurveillanceEvidence", "SurvivalBehavior", "ThreatBasedControl", "UnconventionalEntry", "VehicleConcealment", "VerbalThreats", "VictimAbductionResponse", "VictimControlMechanism", "VictimTargetingPattern", "VulnerabilityExploitation", "WeaponBasedCoercion", "WeaponDisplayIntimidation", "WeaponEvidence", "WindowEntry", "WitnessEvidence"]


@dataclass
class AbductionExploitationPattern(_cacontology.ChildSexualAbuseEvent):
    """Patterns of sexual exploitation following stranger abduction."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#AbductionExploitationPattern"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AbductionSceneEvidence(_uco_observable.ObservableObject):
    """Physical evidence collected from abduction scene."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#AbductionSceneEvidence"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class VulnerabilityExploitation(_cac_core.ExploitationEvent):
    """Exploitation of specific victim vulnerabilities during stranger abduction."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#VulnerabilityExploitation"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AgeBasedVulnerability(VulnerabilityExploitation):
    """Exploitation of victim's young age and limited ability to resist or escape."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#AgeBasedVulnerability"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LocationIsolation(_cac_core.ExploitationEvent):
    """Use of isolated or secluded locations to prevent victim escape or discovery."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#LocationIsolation"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ApartmentIsolation(LocationIsolation):
    """Use of apartment or residential unit for victim isolation and exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#ApartmentIsolation"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class WeaponBasedCoercion(_cac_core.ExploitationEvent):
    """Use of weapons to threaten, intimidate, and control victims during abduction and exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#WeaponBasedCoercion"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class BluntObjectThreats(WeaponBasedCoercion):
    """Use of blunt objects as weapons to threaten and control victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#BluntObjectThreats"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DisguiseBasedConcealment(_cac_core.ExploitationEvent):
    """Use of disguises or concealment methods to hide identity during approach and abduction."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#DisguiseBasedConcealment"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ClothingDisguise(DisguiseBasedConcealment):
    """Use of specific clothing to alter appearance or blend into environment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#ClothingDisguise"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimControlMechanism(_cac_core.ExploitationEvent):
    """Methods used to maintain control over victim during abduction and exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#VictimControlMechanism"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ComplianceEnforcement(VictimControlMechanism):
    """Methods used to enforce victim compliance with perpetrator demands."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#ComplianceEnforcement"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimAbductionResponse(_cac_core.Event):
    """Victim's response to stranger abduction and exploitation attempts."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#VictimAbductionResponse"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ComplianceUnderThreat(VictimAbductionResponse):
    """Victim compliance due to weapon threats or intimidation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#ComplianceUnderThreat"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LocationBasedExploitation(AbductionExploitationPattern):
    """Exploitation occurring at specific location following victim transportation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#LocationBasedExploitation"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ControlledEnvironmentExploitation(LocationBasedExploitation):
    """Exploitation in environment controlled by perpetrator to prevent escape or discovery."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#ControlledEnvironmentExploitation"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PostAbductionReporting(VictimAbductionResponse):
    """Victim's reporting of abduction and exploitation to authorities or family."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#PostAbductionReporting"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DelayedDisclosure(PostAbductionReporting):
    """Delayed disclosure due to trauma, threats, or other factors."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#DelayedDisclosure"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DisguiseEvidence(_cacontology_physical_evidence.DisguiseItem):
    """Disguise items or concealment materials recovered as evidence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#DisguiseEvidence"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EscapeAttempt(VictimAbductionResponse):
    """Victim's attempts to escape during or after abduction."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#EscapeAttempt"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ExploitationSceneEvidence(_uco_observable.ObservableObject):
    """Physical evidence collected from exploitation location."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#ExploitationSceneEvidence"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class FacialConcealment(DisguiseBasedConcealment):
    """Concealment of facial features to prevent identification."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#FacialConcealment"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ForcedLocationEntry(_cac_core.ExploitationEvent):
    """Forcing victim to enter buildings, apartments, or other locations for exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#ForcedLocationEntry"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FireEscapeEntry(ForcedLocationEntry):
    """Forcing victim to climb fire escapes to enter buildings through windows."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#FireEscapeEntry"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FirearmThreats(WeaponBasedCoercion):
    """Use of firearm to threaten and control victim during abduction."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#FirearmThreats"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HoodedConcealment(FacialConcealment):
    """Use of hooded clothing to partially conceal identity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#HoodedConcealment"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HumiliationBasedExploitation(AbductionExploitationPattern):
    """Exploitation designed to humiliate and degrade victim beyond sexual assault."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#HumiliationBasedExploitation"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ImmediateDisclosure(PostAbductionReporting):
    """Immediate disclosure of abduction and assault upon release or escape."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#ImmediateDisclosure"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ImmediateExploitation(AbductionExploitationPattern):
    """Sexual exploitation occurring immediately following abduction without delay."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#ImmediateExploitation"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ImpliedWeaponThreats(WeaponBasedCoercion):
    """Threats suggesting weapon possession without displaying actual weapon."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#ImpliedWeaponThreats"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InitialResistance(VictimAbductionResponse):
    """Victim's initial attempts to resist abduction or escape."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#InitialResistance"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VictimTargetingPattern(_uco_core.UcoObject):
    """Patterns of victim selection and targeting in stranger abduction cases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#VictimTargetingPattern"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class IsolatedChildTargeting(VictimTargetingPattern):
    """Targeting children who are alone without adult supervision or companions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#IsolatedChildTargeting"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class IsolationVulnerability(VulnerabilityExploitation):
    """Exploitation of victim being alone without potential helpers or witnesses."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#IsolationVulnerability"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class KnifeThreats(WeaponBasedCoercion):
    """Use of knife or bladed weapon to threaten and control victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#KnifeThreats"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MaskConcealment(FacialConcealment):
    """Use of masks or face coverings to hide identity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#MaskConcealment"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MovementRestriction(VictimControlMechanism):
    """Physical or psychological restriction of victim movement and escape attempts."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#MovementRestriction"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StrangerAbduction(_cacontology.ChildSexualAbuseEvent):
    """Abduction of child by unknown perpetrator without prior relationship or contact."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#StrangerAbduction"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    comment: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:comment', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    abduction_location: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-stranger-abduction:abductionLocation', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    abduction_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'cacontology-stranger-abduction:abductionTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    abduction_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-stranger-abduction:abductionType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    reported_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'cacontology-stranger-abduction:reportedTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    response_time: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-stranger-abduction:responseTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    risk_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-stranger-abduction:riskLevel', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    victim_age: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-stranger-abduction:victimAge', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class OpportunisticPredation(StrangerAbduction):
    """Spontaneous targeting and exploitation of vulnerable children encountered by chance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#OpportunisticPredation"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OpportunityBasedTargeting(VictimTargetingPattern):
    """Targeting based on immediate opportunity rather than planned surveillance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#OpportunityBasedTargeting"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PhysicalForceWithWeapon(WeaponBasedCoercion):
    """Combination of physical force and weapon use to control victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#PhysicalForceWithWeapon"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PhysicalIntimidation(VictimControlMechanism):
    """Use of physical presence and intimidation to control victim behavior."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#PhysicalIntimidation"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PublicSpaceAbduction(StrangerAbduction):
    """Abduction occurring in public spaces such as parks, playgrounds, or commercial areas."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#PublicSpaceAbduction"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RandomVictimSelection(OpportunisticPredation):
    """Selection of victim based on opportunity rather than specific targeting or grooming."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#RandomVictimSelection"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RitualizedExploitation(AbductionExploitationPattern):
    """Exploitation following specific ritualized patterns (forced showering, specific commands)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#RitualizedExploitation"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RoutineActivityTargeting(VictimTargetingPattern):
    """Targeting children during predictable routine activities (school, recreation, errands)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#RoutineActivityTargeting"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StreetLevelAbduction(StrangerAbduction):
    """Abduction occurring on public streets or sidewalks during victim's routine activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#StreetLevelAbduction"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SchoolRouteAbduction(StreetLevelAbduction):
    """Abduction of child while traveling to or from school or educational activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#SchoolRouteAbduction"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SchoolRouteTargeting(VictimTargetingPattern):
    """Targeting children on routes to or from school when they are alone and vulnerable."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#SchoolRouteTargeting"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SecondaryLocationControl(LocationIsolation):
    """Movement of victim to secondary location for enhanced control and exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#SecondaryLocationControl"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ThreatBasedControl(VictimControlMechanism):
    """Use of threats to maintain victim compliance and prevent resistance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#ThreatBasedControl"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SilenceEnforcement(ThreatBasedControl):
    """Specific threats or actions to prevent victim from calling for help."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#SilenceEnforcement"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SizeBasedVulnerability(VulnerabilityExploitation):
    """Exploitation of victim's small physical size relative to perpetrator."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#SizeBasedVulnerability"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SkiMaskConcealment(FacialConcealment):
    """Use of ski mask or balaclava to conceal identity during approach."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#SkiMaskConcealment"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StrangerAbductionInvestigation(_case_investigation.Investigation):
    """Specialized investigation of stranger abduction and sexual exploitation cases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#StrangerAbductionInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SurveillanceEvidence(_uco_observable.ObservableObject):
    """Video or photographic surveillance evidence of abduction or related activity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#SurveillanceEvidence"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SurvivalBehavior(VictimAbductionResponse):
    """Victim behavior focused on survival and minimizing harm."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#SurvivalBehavior"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class UnconventionalEntry(ForcedLocationEntry):
    """Use of non-standard entry methods to avoid detection or surveillance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#UnconventionalEntry"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VehicleConcealment(DisguiseBasedConcealment):
    """Use of vehicles to conceal approach or provide mobile concealment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#VehicleConcealment"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VerbalThreats(ThreatBasedControl):
    """Use of verbal threats to maintain victim compliance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#VerbalThreats"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class WeaponDisplayIntimidation(WeaponBasedCoercion):
    """Display of weapon to intimidate victim into compliance without direct threats."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#WeaponDisplayIntimidation"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class WeaponEvidence(_cacontology_physical_evidence.PhysicalEvidence):
    """Weapons used in abduction and coercion recovered as evidence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#WeaponEvidence"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class WindowEntry(ForcedLocationEntry):
    """Forcing victim to enter location through windows rather than doors."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#WindowEntry"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class WitnessEvidence(_uco_observable.ObservableObject):
    """Witness testimony regarding abduction or suspicious activity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#WitnessEvidence"
    NAMESPACE_PREFIX: str = "cacontology-stranger-abduction"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
