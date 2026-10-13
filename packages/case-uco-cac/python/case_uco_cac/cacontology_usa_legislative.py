"""CAC Ontology - Crimes Against Children — cacontology_usa_legislative module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar, Optional

import case_uco.uco.identity as _uco_identity
from case_uco_cac import cac_core as _cac_core
from case_uco_cac import cacontology_legal_harmonization as _cacontology_legal_harmonization
from case_uco_cac import cacontology_taskforce as _cacontology_taskforce
from case_uco_cac._context import NAMESPACES

__all__ = ["AppropriationType", "FundingNeed", "FundingStream", "LegislativeStage", "Outcome", "USCabinetAgency", "USConferenceCommittee", "USCongressionalCommittee", "USExecutiveAction", "USFederalAgencyOffice", "USFederalDirectorate", "USReconciliation", "USRulemakingProcess", "USStateAgency", "USStateAttorneyGeneral", "USStateICACtaskForce", "USStateLegislature", "USSubCabinetAgency"]


@dataclass
class AppropriationType(_cac_core.EnduringEntity):
    """Type of Congressional appropriation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-legislative#AppropriationType"
    NAMESPACE_PREFIX: str = "cacontology-usa-legislative"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FundingNeed(_cac_core.EnduringEntity):
    """Funding requirement from an CAC task force."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-legislative#FundingNeed"
    NAMESPACE_PREFIX: str = "cacontology-usa-legislative"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class FundingStream(_cac_core.EnduringEntity):
    """Source of funding for CAC programs."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-legislative#FundingStream"
    NAMESPACE_PREFIX: str = "cacontology-usa-legislative"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LegislativeStage(_cac_core.Phase):
    """Stage in the U.S. legislative process."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-legislative#LegislativeStage"
    NAMESPACE_PREFIX: str = "cacontology-usa-legislative"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class Outcome(_cac_core.AssessmentResult):
    """Result of advocacy efforts."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-legislative#Outcome"
    NAMESPACE_PREFIX: str = "cacontology-usa-legislative"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class USCabinetAgency(_uco_identity.Organization):
    """Cabinet-level department of the United States Federal Government."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-legislative#USCabinetAgency"
    NAMESPACE_PREFIX: str = "cacontology-usa-legislative"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class USConferenceCommittee(_cacontology_legal_harmonization.LegislativeProcess):
    """Bicameral reconciliation process between House and Senate versions."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-legislative#USConferenceCommittee"
    NAMESPACE_PREFIX: str = "cacontology-usa-legislative"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class USCongressionalCommittee(_uco_identity.Organization):
    """Committee of the United States Congress."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-legislative#USCongressionalCommittee"
    NAMESPACE_PREFIX: str = "cacontology-usa-legislative"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class USExecutiveAction(_cacontology_legal_harmonization.LegislativeProcess):
    """Presidential signing or veto of legislation."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-legislative#USExecutiveAction"
    NAMESPACE_PREFIX: str = "cacontology-usa-legislative"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class USFederalAgencyOffice(_uco_identity.Organization):
    """Office within a U.S. Federal Government agency."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-legislative#USFederalAgencyOffice"
    NAMESPACE_PREFIX: str = "cacontology-usa-legislative"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class USFederalDirectorate(_uco_identity.Organization):
    """Directorate or division within a sub-cabinet agency."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-legislative#USFederalDirectorate"
    NAMESPACE_PREFIX: str = "cacontology-usa-legislative"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class USReconciliation(_cacontology_legal_harmonization.LegislativeProcess):
    """Special budget reconciliation process in U.S. Congress."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-legislative#USReconciliation"
    NAMESPACE_PREFIX: str = "cacontology-usa-legislative"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class USRulemakingProcess(_cacontology_legal_harmonization.LegislativeProcess):
    """Administrative Procedure Act rulemaking process."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-legislative#USRulemakingProcess"
    NAMESPACE_PREFIX: str = "cacontology-usa-legislative"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class USStateAgency(_uco_identity.Organization):
    """Agency of a U.S. state government."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-legislative#USStateAgency"
    NAMESPACE_PREFIX: str = "cacontology-usa-legislative"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class USStateAttorneyGeneral(USStateAgency):
    """Attorney General office of a U.S. state."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-legislative#USStateAttorneyGeneral"
    NAMESPACE_PREFIX: str = "cacontology-usa-legislative"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class USStateICACtaskForce(_cacontology_taskforce.ICACtaskForce):
    """State-level CAC Task Force in the United States."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-legislative#USStateICACtaskForce"
    NAMESPACE_PREFIX: str = "cacontology-usa-legislative"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class USStateLegislature(_uco_identity.Organization):
    """Legislative body of a U.S. state."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-legislative#USStateLegislature"
    NAMESPACE_PREFIX: str = "cacontology-usa-legislative"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class USSubCabinetAgency(_uco_identity.Organization):
    """Sub-cabinet law enforcement agency within a cabinet department."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/usa-legislative#USSubCabinetAgency"
    NAMESPACE_PREFIX: str = "cacontology-usa-legislative"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
