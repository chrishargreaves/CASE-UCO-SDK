"""CAC Ontology - Crimes Against Children — cacontology_physical_evidence module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar, Optional

import case_uco.case.investigation as _case_investigation
import case_uco.uco.observable as _uco_observable
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AbuseFacilitationItem", "BodycamFootage", "CellphoneSearch", "ChainOfCustodyBreachSituation", "ChildTargetedItem", "CommunicationDevice", "ComputerEquipment", "Condoms", "ConsentToSearchAuthorization", "CriminalProcurement", "DashcamFootage", "DeviceConsentSearch", "DisguiseItem", "DocumentaryEvidence", "EvidenceAnalysisPhase", "EvidenceCollectionAction", "EvidenceCollectionPhase", "EvidenceContaminationSituation", "EvidenceCustodianRole", "EvidenceDispositionPhase", "EvidenceRecoverySituation", "EvidenceSeizure", "EvidenceStoragePhase", "ForensicAnalystRole", "GloveCompartmentSearch", "IntoxicatingSubstance", "ItemModification", "OnlinePurchase", "PersonalItem", "PhysicalEvidence", "PhysicalEvidenceProvenanceRecord", "PhysicalPurchase", "PhysicalSearch", "RecordingEquipment", "ResidenceSearch", "RestraintItem", "SearchOfficerRole", "StorageMedia", "SurveillanceRecording", "SuspectVehicle", "VapeDevice", "VehicleConsentSearch", "VehicleSearch", "WorkplaceSearch"]


@dataclass
class PhysicalEvidence(_uco_observable.ObservableObject):
    """Tangible items collected as evidence in CAC investigations (gUFO Object)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#PhysicalEvidence"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class AbuseFacilitationItem(PhysicalEvidence):
    """Physical items intended for use in facilitating child abuse or exploitation (gUFO Object)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#AbuseFacilitationItem"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class BodycamFootage(_uco_observable.ObservableObject):
    """Body camera footage from law enforcement officers. Used for suspect identification and evidence. IS a digital observable as it is a digital recording."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#BodycamFootage"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PhysicalSearch(_cac_core.InvestigativeAction):
    """Law enforcement search of physical premises for evidence. Extends investigation:InvestigativeAction for CASE ontology integration (gUFO Event)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#PhysicalSearch"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CellphoneSearch(PhysicalSearch):
    """Search of cellphone or mobile device for evidence. Typically requires consent or warrant (gUFO Event)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#CellphoneSearch"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ChainOfCustodyBreachSituation(_cac_core.Situation):
    """Situation where the chain of custody for evidence has been breached (gUFO Situation)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#ChainOfCustodyBreachSituation"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ChildTargetedItem(AbuseFacilitationItem):
    """Items specifically designed to appeal to or attract children (gUFO Object)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#ChildTargetedItem"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ComputerEquipment(PhysicalEvidence):
    """Digital devices including computers, laptops, tablets, and mobile phones seized as evidence (gUFO FunctionalComplex)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#ComputerEquipment"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class CommunicationDevice(ComputerEquipment):
    """Devices used to communicate with victims or distribute illegal content (gUFO FunctionalComplex)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#CommunicationDevice"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Condoms(AbuseFacilitationItem):
    """Contraceptive devices found as evidence corroborating intent to engage in sexual activity. Extends AbuseFacilitationItem as physical evidence (NOT a digital observable)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#Condoms"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ConsentToSearchAuthorization(_case_investigation.Authorization):
    """Authorization obtained through suspect's consent to search property or devices. Extends investigation:Authorization for CASE ontology integration."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#ConsentToSearchAuthorization"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class CriminalProcurement(_cac_core.ExploitationEvent):
    """Action of acquiring items specifically for criminal purposes (gUFO Event)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#CriminalProcurement"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DashcamFootage(BodycamFootage):
    """Dashboard camera footage from police vehicles. Digital observable."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#DashcamFootage"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DeviceConsentSearch(ConsentToSearchAuthorization):
    """Consent authorization specific to electronic device search (cellphone, computer, etc.)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#DeviceConsentSearch"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PersonalItem(PhysicalEvidence):
    """Personal belongings that may contain evidence or indicate criminal behavior (gUFO Object)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#PersonalItem"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DisguiseItem(PersonalItem):
    """Items used to conceal identity or change appearance (gUFO Object)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#DisguiseItem"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class DocumentaryEvidence(PhysicalEvidence):
    """Physical documents, printed materials, or written items relevant to the investigation (gUFO Object)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#DocumentaryEvidence"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EvidenceAnalysisPhase(_cac_core.Phase):
    """Phase during which physical evidence is undergoing forensic analysis (gUFO Phase - anti-rigid)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#EvidenceAnalysisPhase"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EvidenceCollectionAction(_cac_core.InvestigativeAction):
    """Action of collecting and documenting physical evidence during search. Extends investigation:InvestigativeAction (gUFO Event)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#EvidenceCollectionAction"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EvidenceCollectionPhase(_cac_core.Phase):
    """Phase during which physical evidence is being collected (gUFO Phase - anti-rigid)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#EvidenceCollectionPhase"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EvidenceContaminationSituation(_cac_core.Situation):
    """Situation where physical evidence has been contaminated or compromised (gUFO Situation)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#EvidenceContaminationSituation"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EvidenceCustodianRole(_cac_core.Role):
    """Role of person responsible for evidence custody and chain of custody (gUFO Role - anti-rigid). Roles are non-rigid capacities; persons play roles via holdsRole."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#EvidenceCustodianRole"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EvidenceDispositionPhase(_cac_core.Phase):
    """Phase during which evidence disposition is determined and executed (gUFO Phase - anti-rigid)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#EvidenceDispositionPhase"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EvidenceRecoverySituation(_cac_core.Situation):
    """Situation involving the recovery of previously lost or missing evidence (gUFO Situation)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#EvidenceRecoverySituation"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EvidenceSeizure(_cac_core.InvestigativeAction):
    """Legal seizure of physical items as evidence. Extends investigation:InvestigativeAction (gUFO Event)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#EvidenceSeizure"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class EvidenceStoragePhase(_cac_core.Phase):
    """Phase during which physical evidence is in secure storage (gUFO Phase - anti-rigid)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#EvidenceStoragePhase"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ForensicAnalystRole(_cac_core.Role):
    """Role of person conducting forensic analysis of physical evidence (gUFO Role - anti-rigid). Roles are non-rigid capacities; persons play roles via holdsRole."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#ForensicAnalystRole"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VehicleSearch(PhysicalSearch):
    """Search of motor vehicles for evidence or contraband. May be conducted with consent or warrant (gUFO Event)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#VehicleSearch"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class GloveCompartmentSearch(VehicleSearch):
    """Search of vehicle glove compartment as specific evidence location (gUFO Event)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#GloveCompartmentSearch"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class IntoxicatingSubstance(AbuseFacilitationItem):
    """Alcohol, drugs, or other intoxicating substances intended to impair victim judgment. Extends AbuseFacilitationItem."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#IntoxicatingSubstance"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ItemModification(_cac_core.ExploitationEvent):
    """Alteration or customization of items to facilitate criminal activity (gUFO Event)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#ItemModification"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class OnlinePurchase(CriminalProcurement):
    """Purchase of items through online platforms for criminal purposes (gUFO Event)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#OnlinePurchase"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PhysicalEvidenceProvenanceRecord(_case_investigation.ProvenanceRecord):
    """Provenance record tracking chain of custody and handling of physical evidence. Extends investigation:ProvenanceRecord for CASE ontology integration."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#PhysicalEvidenceProvenanceRecord"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class PhysicalPurchase(CriminalProcurement):
    """In-person purchase of items for criminal purposes (gUFO Event)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#PhysicalPurchase"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RecordingEquipment(AbuseFacilitationItem):
    """Devices used to create audio or video recordings of criminal activity (gUFO FunctionalComplex)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#RecordingEquipment"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ResidenceSearch(PhysicalSearch):
    """Search of residential premises including homes and apartments (gUFO Event)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#ResidenceSearch"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class RestraintItem(AbuseFacilitationItem):
    """Items intended for restraining or controlling victims (gUFO Object)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#RestraintItem"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SearchOfficerRole(_cac_core.Role):
    """Role of law enforcement officer conducting physical searches (gUFO Role - anti-rigid). Roles are non-rigid capacities; persons play roles via holdsRole."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#SearchOfficerRole"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class StorageMedia(PhysicalEvidence):
    """External storage devices including hard drives, USB drives, memory cards, and optical media (gUFO Object)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#StorageMedia"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SurveillanceRecording(_uco_observable.ObservableObject):
    """Recording from surveillance or security cameras. Digital observable."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#SurveillanceRecording"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class SuspectVehicle(PhysicalEvidence):
    """Vehicle registered to or used by suspect in CAC offense. Used for evidence tracking when suspect travels to meet alleged minor. Physical evidence item."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#SuspectVehicle"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VapeDevice(AbuseFacilitationItem):
    """Electronic vaporizer or e-cigarette found as evidence. Often brought to lure or facilitate abuse of minors. Extends AbuseFacilitationItem as physical evidence (NOT a digital observable)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#VapeDevice"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class VehicleConsentSearch(ConsentToSearchAuthorization):
    """Consent authorization specific to vehicle search."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#VehicleConsentSearch"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class WorkplaceSearch(PhysicalSearch):
    """Search of workplace or commercial premises (gUFO Event)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/physical#WorkplaceSearch"
    NAMESPACE_PREFIX: str = "cacontology-physical-evidence"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
