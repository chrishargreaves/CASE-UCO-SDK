"""CAC Ontology - Crimes Against Children — cacontology-stranger-abduction module."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AbductionExploitationPattern:
    """Patterns of sexual exploitation following stranger abduction."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#AbductionExploitationPattern"


@dataclass
class AbductionSceneEvidence:
    """Physical evidence collected from abduction scene."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#AbductionSceneEvidence"
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
class AgeBasedVulnerability:
    """Exploitation of victim's young age and limited ability to resist or escape."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#AgeBasedVulnerability"


@dataclass
class ApartmentIsolation:
    """Use of apartment or residential unit for victim isolation and exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#ApartmentIsolation"


@dataclass
class BluntObjectThreats:
    """Use of blunt objects as weapons to threaten and control victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#BluntObjectThreats"


@dataclass
class ClothingDisguise:
    """Use of specific clothing to alter appearance or blend into environment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#ClothingDisguise"


@dataclass
class ComplianceEnforcement:
    """Methods used to enforce victim compliance with perpetrator demands."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#ComplianceEnforcement"


@dataclass
class ComplianceUnderThreat:
    """Victim compliance due to weapon threats or intimidation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#ComplianceUnderThreat"


@dataclass
class ControlledEnvironmentExploitation:
    """Exploitation in environment controlled by perpetrator to prevent escape or discovery."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#ControlledEnvironmentExploitation"


@dataclass
class DelayedDisclosure:
    """Delayed disclosure due to trauma, threats, or other factors."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#DelayedDisclosure"


@dataclass
class DisguiseBasedConcealment:
    """Use of disguises or concealment methods to hide identity during approach and abduction."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#DisguiseBasedConcealment"


@dataclass
class DisguiseEvidence:
    """Disguise items or concealment materials recovered as evidence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#DisguiseEvidence"
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
class EscapeAttempt:
    """Victim's attempts to escape during or after abduction."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#EscapeAttempt"


@dataclass
class ExploitationSceneEvidence:
    """Physical evidence collected from exploitation location."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#ExploitationSceneEvidence"
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
class FacialConcealment:
    """Concealment of facial features to prevent identification."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#FacialConcealment"


@dataclass
class FireEscapeEntry:
    """Forcing victim to climb fire escapes to enter buildings through windows."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#FireEscapeEntry"


@dataclass
class FirearmThreats:
    """Use of firearm to threaten and control victim during abduction."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#FirearmThreats"


@dataclass
class ForcedLocationEntry:
    """Forcing victim to enter buildings, apartments, or other locations for exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#ForcedLocationEntry"


@dataclass
class HoodedConcealment:
    """Use of hooded clothing to partially conceal identity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#HoodedConcealment"


@dataclass
class HumiliationBasedExploitation:
    """Exploitation designed to humiliate and degrade victim beyond sexual assault."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#HumiliationBasedExploitation"


@dataclass
class ImmediateDisclosure:
    """Immediate disclosure of abduction and assault upon release or escape."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#ImmediateDisclosure"


@dataclass
class ImmediateExploitation:
    """Sexual exploitation occurring immediately following abduction without delay."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#ImmediateExploitation"


@dataclass
class ImpliedWeaponThreats:
    """Threats suggesting weapon possession without displaying actual weapon."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#ImpliedWeaponThreats"


@dataclass
class InitialResistance:
    """Victim's initial attempts to resist abduction or escape."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#InitialResistance"


@dataclass
class IsolatedChildTargeting:
    """Targeting children who are alone without adult supervision or companions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#IsolatedChildTargeting"
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
class IsolationVulnerability:
    """Exploitation of victim being alone without potential helpers or witnesses."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#IsolationVulnerability"


@dataclass
class KnifeThreats:
    """Use of knife or bladed weapon to threaten and control victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#KnifeThreats"


@dataclass
class LocationBasedExploitation:
    """Exploitation occurring at specific location following victim transportation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#LocationBasedExploitation"


@dataclass
class LocationIsolation:
    """Use of isolated or secluded locations to prevent victim escape or discovery."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#LocationIsolation"


@dataclass
class MaskConcealment:
    """Use of masks or face coverings to hide identity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#MaskConcealment"


@dataclass
class MovementRestriction:
    """Physical or psychological restriction of victim movement and escape attempts."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#MovementRestriction"


@dataclass
class OpportunisticPredation:
    """Spontaneous targeting and exploitation of vulnerable children encountered by chance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#OpportunisticPredation"
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    abduction_location: Optional[str] = field(default=None)
    abduction_time: Optional[datetime] = field(default=None)
    abduction_type: Optional[str] = field(default=None)
    reported_time: Optional[datetime] = field(default=None)
    response_time: Optional[float] = field(default=None)
    risk_level: Optional[str] = field(default=None)
    victim_age: Optional[int] = field(default=None)


@dataclass
class OpportunityBasedTargeting:
    """Targeting based on immediate opportunity rather than planned surveillance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#OpportunityBasedTargeting"
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
class PhysicalForceWithWeapon:
    """Combination of physical force and weapon use to control victim."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#PhysicalForceWithWeapon"


@dataclass
class PhysicalIntimidation:
    """Use of physical presence and intimidation to control victim behavior."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#PhysicalIntimidation"


@dataclass
class PostAbductionReporting:
    """Victim's reporting of abduction and exploitation to authorities or family."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#PostAbductionReporting"


@dataclass
class PublicSpaceAbduction:
    """Abduction occurring in public spaces such as parks, playgrounds, or commercial areas."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#PublicSpaceAbduction"
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    abduction_location: Optional[str] = field(default=None)
    abduction_time: Optional[datetime] = field(default=None)
    abduction_type: Optional[str] = field(default=None)
    reported_time: Optional[datetime] = field(default=None)
    response_time: Optional[float] = field(default=None)
    risk_level: Optional[str] = field(default=None)
    victim_age: Optional[int] = field(default=None)


@dataclass
class RandomVictimSelection:
    """Selection of victim based on opportunity rather than specific targeting or grooming."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#RandomVictimSelection"
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    abduction_location: Optional[str] = field(default=None)
    abduction_time: Optional[datetime] = field(default=None)
    abduction_type: Optional[str] = field(default=None)
    reported_time: Optional[datetime] = field(default=None)
    response_time: Optional[float] = field(default=None)
    risk_level: Optional[str] = field(default=None)
    victim_age: Optional[int] = field(default=None)


@dataclass
class RitualizedExploitation:
    """Exploitation following specific ritualized patterns (forced showering, specific commands)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#RitualizedExploitation"


@dataclass
class RoutineActivityTargeting:
    """Targeting children during predictable routine activities (school, recreation, errands)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#RoutineActivityTargeting"
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
class SchoolRouteAbduction:
    """Abduction of child while traveling to or from school or educational activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#SchoolRouteAbduction"
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    abduction_location: Optional[str] = field(default=None)
    abduction_time: Optional[datetime] = field(default=None)
    abduction_type: Optional[str] = field(default=None)
    reported_time: Optional[datetime] = field(default=None)
    response_time: Optional[float] = field(default=None)
    risk_level: Optional[str] = field(default=None)
    victim_age: Optional[int] = field(default=None)


@dataclass
class SchoolRouteTargeting:
    """Targeting children on routes to or from school when they are alone and vulnerable."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#SchoolRouteTargeting"
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
class SecondaryLocationControl:
    """Movement of victim to secondary location for enhanced control and exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#SecondaryLocationControl"


@dataclass
class SilenceEnforcement:
    """Specific threats or actions to prevent victim from calling for help."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#SilenceEnforcement"


@dataclass
class SizeBasedVulnerability:
    """Exploitation of victim's small physical size relative to perpetrator."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#SizeBasedVulnerability"


@dataclass
class SkiMaskConcealment:
    """Use of ski mask or balaclava to conceal identity during approach."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#SkiMaskConcealment"


@dataclass
class StrangerAbduction:
    """Abduction of child by unknown perpetrator without prior relationship or contact."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#StrangerAbduction"
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    abduction_location: Optional[str] = field(default=None)
    abduction_time: Optional[datetime] = field(default=None)
    abduction_type: Optional[str] = field(default=None)
    reported_time: Optional[datetime] = field(default=None)
    response_time: Optional[float] = field(default=None)
    risk_level: Optional[str] = field(default=None)
    victim_age: Optional[int] = field(default=None)


@dataclass
class StrangerAbductionInvestigation:
    """Specialized investigation of stranger abduction and sexual exploitation cases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#StrangerAbductionInvestigation"
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
    object: list[UcoObject] = field(default_factory=list)
    focus: list[str] = field(default_factory=list)
    investigation_form: Optional[str] = field(default=None)
    investigation_status: Optional[str] = field(default=None)
    relevant_authorization: list[Authorization] = field(default_factory=list)
    end_time: Optional[datetime] = field(default=None)
    start_time: Optional[datetime] = field(default=None)


@dataclass
class StreetLevelAbduction:
    """Abduction occurring on public streets or sidewalks during victim's routine activities."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#StreetLevelAbduction"
    comment: Optional[str] = field(default=None)
    label: Optional[str] = field(default=None)
    abduction_location: Optional[str] = field(default=None)
    abduction_time: Optional[datetime] = field(default=None)
    abduction_type: Optional[str] = field(default=None)
    reported_time: Optional[datetime] = field(default=None)
    response_time: Optional[float] = field(default=None)
    risk_level: Optional[str] = field(default=None)
    victim_age: Optional[int] = field(default=None)


@dataclass
class SurveillanceEvidence:
    """Video or photographic surveillance evidence of abduction or related activity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#SurveillanceEvidence"
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
class SurvivalBehavior:
    """Victim behavior focused on survival and minimizing harm."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#SurvivalBehavior"


@dataclass
class ThreatBasedControl:
    """Use of threats to maintain victim compliance and prevent resistance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#ThreatBasedControl"


@dataclass
class UnconventionalEntry:
    """Use of non-standard entry methods to avoid detection or surveillance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#UnconventionalEntry"


@dataclass
class VehicleConcealment:
    """Use of vehicles to conceal approach or provide mobile concealment."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#VehicleConcealment"


@dataclass
class VerbalThreats:
    """Use of verbal threats to maintain victim compliance."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#VerbalThreats"


@dataclass
class VictimAbductionResponse:
    """Victim's response to stranger abduction and exploitation attempts."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#VictimAbductionResponse"


@dataclass
class VictimControlMechanism:
    """Methods used to maintain control over victim during abduction and exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#VictimControlMechanism"


@dataclass
class VictimTargetingPattern:
    """Patterns of victim selection and targeting in stranger abduction cases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#VictimTargetingPattern"
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
class VulnerabilityExploitation:
    """Exploitation of specific victim vulnerabilities during stranger abduction."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#VulnerabilityExploitation"


@dataclass
class WeaponBasedCoercion:
    """Use of weapons to threaten, intimidate, and control victims during abduction and exploitation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#WeaponBasedCoercion"


@dataclass
class WeaponDisplayIntimidation:
    """Display of weapon to intimidate victim into compliance without direct threats."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#WeaponDisplayIntimidation"


@dataclass
class WeaponEvidence:
    """Weapons used in abduction and coercion recovered as evidence."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#WeaponEvidence"
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
class WindowEntry:
    """Forcing victim to enter location through windows rather than doors."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#WindowEntry"


@dataclass
class WitnessEvidence:
    """Witness testimony regarding abduction or suspicious activity."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/abduction#WitnessEvidence"
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

