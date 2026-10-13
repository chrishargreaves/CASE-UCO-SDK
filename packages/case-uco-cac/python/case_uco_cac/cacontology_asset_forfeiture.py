"""CAC Ontology - Crimes Against Children — cacontology_asset_forfeiture module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional

import case_uco.uco.identity as _uco_identity
import case_uco.uco.observable as _uco_observable
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AssetAssessmentAction", "AssetForfeitureAction", "AssetForfeitureOfficer", "AssetIdentificationPhase", "AssetValuationExpert", "CACTInvestigation", "CompleteForfeiture", "ConsentOrder", "CriminalAssetsConfiscationTaskforce", "EquipmentSeizureAction", "FinancialAccount", "FinancialPenaltyAction", "ForensicAccountant", "ForfeitureOutcome", "HouseholdItems", "InstrumentOfOffense", "JurisdictionalCoordination", "LegalBasisForForfeiture", "LegalCounsel", "LegalProceedingsPhase", "LegalProceedingsSituation", "MultiStateForfeiture", "NonProfitOffenderAssets", "PartialForfeiture", "ProceedsOfCrime", "PropertyForfeitureAction", "PropertyManager", "PropertyRestraintAction", "RecoveryPhase", "ResidentialProperty", "RestraintPhase", "StateSupremeCourt", "TechnicalEquipment", "Vehicle"]


@dataclass
class AssetAssessmentAction(_cac_core.LegalEvent):
    """Action to assess the value and ownership of assets for potential forfeiture. Enhanced as gUFO Event with assessment phases."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#AssetAssessmentAction"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AssetForfeitureAction(_cac_core.LegalEvent):
    """Legal action to forfeit assets derived from or used in child exploitation crimes. Enhanced as gUFO Event for comprehensive temporal and causal modeling of forfeiture proceedings."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#AssetForfeitureAction"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    current_phase: Optional[Phase] = field(default=None, metadata={'jsonld_key': 'cacontology-asset-forfeiture:currentPhase', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'https://cacontology.projectvic.org/core#Phase', 'alternate_range_iris': []})
    involves_taskforce: Optional[CriminalAssetsConfiscationTaskforce] = field(default=None, metadata={'jsonld_key': 'cacontology-asset-forfeiture:involvesTaskforce', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'https://cacontology.projectvic.org/asset-forfeiture#CriminalAssetsConfiscationTaskforce', 'alternate_range_iris': []})
    targeted_asset: list[ObservableObject] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-asset-forfeiture:targetedAsset', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/observable/ObservableObject', 'alternate_range_iris': []})
    forfeiture_begin_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#forfeitureBeginTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    forfeiture_end_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#forfeitureEndTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class AssetForfeitureOfficer(_cac_core.Role):
    """Officer specializing in asset identification and forfeiture proceedings."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#AssetForfeitureOfficer"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class AssetIdentificationPhase(_cac_core.Phase):
    """Phase during which assets are identified and assessed for potential forfeiture. Anti-rigid gUFO Phase supporting dynamic operational transitions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#AssetIdentificationPhase"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    phase_transition_time: list[datetime] = field(default_factory=list, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#phaseTransitionTime', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class AssetValuationExpert(_cac_core.Role):
    """Expert responsible for determining market value of assets for forfeiture proceedings."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#AssetValuationExpert"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CACTInvestigation(_cac_core.InvestigativeAction):
    """Investigation conducted by Criminal Assets Confiscation Taskforce targeting assets of child exploitation offenders. Enhanced as gUFO Event."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#CACTInvestigation"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    investigation_begin_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#investigationBeginTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    investigation_end_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#investigationEndTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class ForfeitureOutcome(_uco_observable.ObservableObject):
    """Result of asset forfeiture proceedings. Enhanced as gUFO Object for outcome modeling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#ForfeitureOutcome"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CompleteForfeiture(ForfeitureOutcome):
    """Complete forfeiture of property to the Commonwealth or state. Enhanced as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#CompleteForfeiture"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ConsentOrder(ForfeitureOutcome):
    """Court order agreed to by parties for financial penalty payment. Enhanced as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#ConsentOrder"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CriminalAssetsConfiscationTaskforce(_uco_identity.Organization):
    """Specialized taskforce responsible for asset restraint and forfeiture in child exploitation cases. Enhanced as gUFO Organization with structured operational frameworks."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#CriminalAssetsConfiscationTaskforce"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class EquipmentSeizureAction(AssetForfeitureAction):
    """Seizure of equipment used in commission of child exploitation offenses. Enhanced as gUFO Event for seizure operations."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#EquipmentSeizureAction"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FinancialAccount(_uco_observable.ObservableObject):
    """Bank account or financial instrument subject to restraint or forfeiture. Enhanced as gUFO Object for financial asset modeling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#FinancialAccount"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    account_funds: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-asset-forfeiture:accountFunds', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    financial_institution: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-asset-forfeiture:financialInstitution', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class FinancialPenaltyAction(AssetForfeitureAction):
    """Court-ordered financial penalty equal to benefits derived from child exploitation offenses. Enhanced as gUFO Event for penalty proceedings."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#FinancialPenaltyAction"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    financial_penalty_amount: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-asset-forfeiture:financialPenaltyAmount', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    penalty_imposition_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#penaltyImpositionTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class ForensicAccountant(_cac_core.Role):
    """Specialist in tracing financial assets and determining proceeds of crime."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#ForensicAccountant"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class HouseholdItems(_uco_observable.ObservableObject):
    """High-value household items including electronics, furniture, and appliances subject to forfeiture. Enhanced as gUFO Object for personal property modeling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#HouseholdItems"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class InstrumentOfOffense(_uco_observable.ObservableObject):
    """Assets used as instruments in the commission of child exploitation offenses. Enhanced as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#InstrumentOfOffense"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class JurisdictionalCoordination(_cac_core.Situation):
    """Complex coordination situation involving multiple legal jurisdictions for asset forfeiture operations. gUFO Situation for inter-jurisdictional modeling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#JurisdictionalCoordination"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    coordination_begin_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#coordinationBeginTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class LegalBasisForForfeiture(_cac_core.EnduringEntity):
    """Legal justification and framework for asset forfeiture action."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#LegalBasisForForfeiture"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegalCounsel(_cac_core.Role):
    """Legal counsel specialized in asset forfeiture law and proceedings."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#LegalCounsel"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegalProceedingsPhase(_cac_core.Phase):
    """Phase during which formal forfeiture proceedings occur in court. Anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#LegalProceedingsPhase"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegalProceedingsSituation(_cac_core.Situation):
    """Complex situation involving courts, legal counsel, and multiple parties in forfeiture proceedings. gUFO Situation for legal process coordination."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#LegalProceedingsSituation"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class MultiStateForfeiture(AssetForfeitureAction):
    """Asset forfeiture operation spanning multiple Australian states and territories. Subclasses AssetForfeitureAction (Event) only; multi-jurisdictional coordination modeled via involvesCoordination to Jur"""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#MultiStateForfeiture"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class NonProfitOffenderAssets(LegalBasisForForfeiture):
    """Assets of offenders who were not accused of profiting from their crimes, representing first-of-kind forfeiture precedent. Enhanced as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#NonProfitOffenderAssets"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PartialForfeiture(ForfeitureOutcome):
    """Forfeiture of a percentage of property value (e.g., 50% of market value). Enhanced as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#PartialForfeiture"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    forfeiture_percentage: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-asset-forfeiture:forfeiturePercentage', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class ProceedsOfCrime(_uco_observable.ObservableObject):
    """Assets that are proceeds or benefits derived from child exploitation offenses. Enhanced as gUFO Object."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#ProceedsOfCrime"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PropertyForfeitureAction(AssetForfeitureAction):
    """Legal action resulting in permanent forfeiture of property to the Commonwealth or state. Enhanced as gUFO Event with completion modeling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#PropertyForfeitureAction"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    forfeiture_outcome: Optional[ForfeitureOutcome] = field(default=None, metadata={'jsonld_key': 'cacontology-asset-forfeiture:forfeitureOutcome', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'https://cacontology.projectvic.org/asset-forfeiture#ForfeitureOutcome', 'alternate_range_iris': []})
    forfeiture_completion_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#forfeitureCompletionTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class PropertyManager(_cac_core.Role):
    """Specialist responsible for managing restrained and forfeited property."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#PropertyManager"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PropertyRestraintAction(AssetForfeitureAction):
    """Legal action to restrain property pending forfeiture proceedings, preventing disposal or transfer. Enhanced as gUFO Event with restraint temporal modeling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#PropertyRestraintAction"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    restraint_begin_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'https://cacontology.projectvic.org/gufo#restraintBeginTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class RecoveryPhase(_cac_core.Phase):
    """Phase during which forfeited assets are recovered and transferred to appropriate authorities. Anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#RecoveryPhase"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ResidentialProperty(_uco_observable.ObservableObject):
    """Residential home subject to restraint or forfeiture in child exploitation cases. Enhanced as gUFO Object for comprehensive property modeling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#ResidentialProperty"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    market_value: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-asset-forfeiture:marketValue', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    property_owner: list[Person] = field(default_factory=list, metadata={'jsonld_key': 'uco-observable:propertyOwner', 'required': True, 'cardinality': 'one_or_more', 'range_iri': 'https://ontology.unifiedcyberontology.org/uco/identity/Person', 'alternate_range_iris': []})


@dataclass
class RestraintPhase(_cac_core.Phase):
    """Phase during which property is restrained pending forfeiture proceedings. Anti-rigid gUFO Phase."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#RestraintPhase"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StateSupremeCourt(_uco_identity.Organization):
    """State Supreme Court with jurisdiction over forfeiture proceedings. Enhanced as gUFO Organization for judicial institution modeling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#StateSupremeCourt"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class TechnicalEquipment(_uco_observable.ObservableObject):
    """Technical equipment used in child exploitation offenses (cameras, computers, drones, etc.). Enhanced as gUFO Object for equipment modeling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#TechnicalEquipment"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    equipment_type: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-asset-forfeiture:equipmentType', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class Vehicle(_uco_observable.ObservableObject):
    """Vehicle used in or purchased with proceeds from child exploitation offenses. Enhanced as gUFO Object for vehicle asset modeling."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/asset-forfeiture#Vehicle"
    NAMESPACE_PREFIX: str = "cacontology-asset-forfeiture"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
