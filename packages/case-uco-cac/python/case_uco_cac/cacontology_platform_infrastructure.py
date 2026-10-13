"""CAC Ontology - Crimes Against Children — cacontology_platform_infrastructure module (generated; do not edit)."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Optional, Union

import case_uco.uco.identity as _uco_identity
import case_uco.uco.observable as _uco_observable
from case_uco.typed_literal import TypedLiteral
from case_uco_cac import cac_core as _cac_core
from case_uco_cac._context import NAMESPACES

__all__ = ["AccountFreezing", "AnalystRole", "AnonymityInfrastructure", "ContentDeliveryNetwork", "CryptocurrencyInfrastructure", "DataMirrorCreation", "DatabaseInfrastructure", "DomainInfrastructure", "DomainSinkholing", "EncryptionInfrastructure", "FinancialFlowAnalysis", "FinancialObfuscation", "GeographicDistribution", "HostingProvider", "InfrastructureAnalysis", "InfrastructureCompromiseSituation", "InfrastructureDecommissionPhase", "InfrastructureDeploymentPhase", "InfrastructureDiscoverySituation", "InfrastructureFailureSituation", "InfrastructureMaintenancePhase", "InfrastructureOperationalPhase", "InfrastructureTakedown", "LoadBalancer", "NetworkInfrastructure", "NetworkTopologyAnalysis", "PaymentProcessing", "PlatformInfrastructure", "ProxyInfrastructure", "SecurityInfrastructure", "SecurityOperatorRole", "ServerInfrastructure", "ServerSeizure", "SubscriptionManagement", "SystemAdministratorRole", "TakedownOperatorRole", "UserAccessPatternAnalysis"]


@dataclass
class InfrastructureTakedown(_cac_core.InvestigativeAction):
    """Coordinated operation to dismantle platform infrastructure including servers, domains, and supporting systems (gUFO Event)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#InfrastructureTakedown"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    takedown_duration: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-platform-infrastructure:takedownDuration', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    end_time_uco_core: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:endTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    start_time_uco_core: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class AccountFreezing(InfrastructureTakedown):
    """Freezing financial accounts and cryptocurrency wallets associated with platform operations (gUFO Event)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#AccountFreezing"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    accounts_frozen: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-platform-infrastructure:accountsFrozen', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class AnalystRole(_cac_core.Role):
    """Role of person conducting infrastructure analysis (gUFO Role - anti-rigid)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#AnalystRole"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class PlatformInfrastructure(_uco_observable.ObservableObject):
    """Technical infrastructure supporting child exploitation platforms, including servers, networks, and supporting systems (gUFO Object)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#PlatformInfrastructure"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class SecurityInfrastructure(PlatformInfrastructure):
    """Security systems protecting platform infrastructure from detection and takedown efforts (gUFO FunctionalComplex)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#SecurityInfrastructure"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    obfuscation_methods: list[str] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-platform-infrastructure:obfuscationMethods', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class AnonymityInfrastructure(SecurityInfrastructure):
    """Systems providing anonymity to users and operators, including Tor integration and VPN services (gUFO FunctionalComplex)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#AnonymityInfrastructure"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    anonymity_level: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-platform-infrastructure:anonymityLevel', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ContentDeliveryNetwork(PlatformInfrastructure):
    """CDN infrastructure used for distributing illegal content globally with high availability and performance (gUFO FunctionalComplex)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#ContentDeliveryNetwork"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    bandwidth_capacity: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-platform-infrastructure:bandwidthCapacity', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class PaymentProcessing(_uco_observable.ObservableObject):
    """Financial processing systems enabling platform monetization through subscription fees, content purchases, or cryptocurrency transactions (gUFO FunctionalComplex)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#PaymentProcessing"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    monthly_revenue: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-platform-infrastructure:monthlyRevenue', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})
    payment_methods: list[str] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-platform-infrastructure:paymentMethods', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class CryptocurrencyInfrastructure(PaymentProcessing):
    """Cryptocurrency wallets, exchanges, and payment processing systems used for anonymous financial transactions (gUFO FunctionalComplex)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#CryptocurrencyInfrastructure"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    crypto_currency_types: list[str] = field(default_factory=list, metadata={'jsonld_key': 'cacontology-platform-infrastructure:cryptoCurrencyTypes', 'required': False, 'cardinality': 'zero_or_more', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class DataMirrorCreation(InfrastructureTakedown):
    """Creating forensic mirrors of seized infrastructure for analysis and evidence preservation (gUFO Event)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#DataMirrorCreation"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    data_volume_mirrored: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-platform-infrastructure:dataVolumeMirrored', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class DatabaseInfrastructure(PlatformInfrastructure):
    """Database systems storing user accounts, content metadata, and platform operational data (gUFO FunctionalComplex)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#DatabaseInfrastructure"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    storage_capacity: Optional[float] = field(default=None, metadata={'jsonld_key': 'cacontology-platform-infrastructure:storageCapacity', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#decimal', 'alternate_range_iris': []})


@dataclass
class DomainInfrastructure(PlatformInfrastructure):
    """Domain name system infrastructure including domain registration, DNS services, and subdomain management (gUFO FunctionalComplex)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#DomainInfrastructure"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    domain_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-platform-infrastructure:domainCount', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class DomainSinkholing(InfrastructureTakedown):
    """Redirecting domain traffic to law enforcement controlled servers to gather intelligence (gUFO Event)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#DomainSinkholing"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    domains_sinkholed: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-platform-infrastructure:domainsSinkholed', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class EncryptionInfrastructure(SecurityInfrastructure):
    """Encryption systems protecting data transmission, storage, and user communications (gUFO FunctionalComplex)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#EncryptionInfrastructure"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    encryption_strength: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-platform-infrastructure:encryptionStrength', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class InfrastructureAnalysis(_cac_core.InvestigativeAction):
    """Analysis of seized infrastructure to understand platform operations and identify additional targets (gUFO Event)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#InfrastructureAnalysis"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})
    start_time_uco_core: Optional[Union[str, TypedLiteral]] = field(default=None, metadata={'jsonld_key': 'uco-core:startTime', 'required': True, 'cardinality': 'exactly_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': [], 'literal_datatype': True})


@dataclass
class FinancialFlowAnalysis(InfrastructureAnalysis):
    """Analysis of financial transactions and payment flows through platform monetization systems (gUFO Event)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#FinancialFlowAnalysis"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    financial_complexity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-platform-infrastructure:financialComplexity', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class FinancialObfuscation(PaymentProcessing):
    """Methods used to obscure financial transactions and payment flows to avoid detection (gUFO Object)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#FinancialObfuscation"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class GeographicDistribution(PlatformInfrastructure):
    """Geographic distribution of infrastructure across multiple countries to complicate law enforcement efforts (gUFO Object)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#GeographicDistribution"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    geographic_locations: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-platform-infrastructure:geographicLocations', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class HostingProvider(_uco_identity.Organization):
    """Organizations providing server hosting, cloud services, or infrastructure-as-a-service for platforms (gUFO Object)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#HostingProvider"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    label: Optional[str] = field(default=None, metadata={'jsonld_key': 'rdfs:label', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    hosting_provider: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-platform-infrastructure:hostingProvider', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    created_time: Optional[datetime] = field(default=None, metadata={'jsonld_key': 'uco-core:createdTime', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#dateTime', 'alternate_range_iris': []})


@dataclass
class InfrastructureCompromiseSituation(_cac_core.Situation):
    """Situation where platform infrastructure has been compromised or breached (gUFO Situation)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#InfrastructureCompromiseSituation"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InfrastructureDecommissionPhase(_cac_core.Phase):
    """Phase during which infrastructure is being decommissioned or shut down (gUFO Phase - anti-rigid)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#InfrastructureDecommissionPhase"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InfrastructureDeploymentPhase(_cac_core.Phase):
    """Phase during which platform infrastructure is being deployed and configured (gUFO Phase - anti-rigid)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#InfrastructureDeploymentPhase"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InfrastructureDiscoverySituation(_cac_core.Situation):
    """Situation involving the discovery of previously unknown infrastructure components (gUFO Situation)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#InfrastructureDiscoverySituation"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InfrastructureFailureSituation(_cac_core.Situation):
    """Situation involving infrastructure failure or outage (gUFO Situation)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#InfrastructureFailureSituation"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InfrastructureMaintenancePhase(_cac_core.Phase):
    """Phase during which infrastructure undergoes maintenance and updates (gUFO Phase - anti-rigid)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#InfrastructureMaintenancePhase"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class InfrastructureOperationalPhase(_cac_core.Phase):
    """Phase during which platform infrastructure is actively supporting operations (gUFO Phase - anti-rigid)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#InfrastructureOperationalPhase"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class LoadBalancer(PlatformInfrastructure):
    """Load balancing infrastructure distributing traffic across multiple servers for high availability (gUFO FunctionalComplex)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#LoadBalancer"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class NetworkInfrastructure(PlatformInfrastructure):
    """Network topology and routing infrastructure supporting platform connectivity and distribution (gUFO FunctionalComplex)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#NetworkInfrastructure"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class NetworkTopologyAnalysis(InfrastructureAnalysis):
    """Analysis of network architecture and connectivity patterns within platform infrastructure (gUFO Event)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#NetworkTopologyAnalysis"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    network_complexity: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-platform-infrastructure:networkComplexity', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})


@dataclass
class ProxyInfrastructure(PlatformInfrastructure):
    """Proxy servers and reverse proxy systems used to hide platform origins and provide redundancy (gUFO FunctionalComplex)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#ProxyInfrastructure"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class SecurityOperatorRole(_cac_core.Role):
    """Role of person managing security infrastructure and operations (gUFO Role - anti-rigid)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#SecurityOperatorRole"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class ServerInfrastructure(PlatformInfrastructure):
    """Server and hosting infrastructure supporting platform operations, including web servers, database servers, and application servers (gUFO FunctionalComplex)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#ServerInfrastructure"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    cloud_platform: Optional[str] = field(default=None, metadata={'jsonld_key': 'cacontology-platform-infrastructure:cloudPlatform', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#string', 'alternate_range_iris': []})
    server_count: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-platform-infrastructure:serverCount', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class ServerSeizure(InfrastructureTakedown):
    """Physical or virtual seizure of servers hosting platform infrastructure (gUFO Event)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#ServerSeizure"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    servers_seized: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-platform-infrastructure:serversSeized', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class SubscriptionManagement(PaymentProcessing):
    """Systems managing user subscriptions, access levels, and recurring payment processing (gUFO FunctionalComplex)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#SubscriptionManagement"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    subscription_tiers: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-platform-infrastructure:subscriptionTiers', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})


@dataclass
class SystemAdministratorRole(_cac_core.Role):
    """Role of person responsible for infrastructure system administration (gUFO Role - anti-rigid)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#SystemAdministratorRole"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class TakedownOperatorRole(_cac_core.Role):
    """Role of law enforcement personnel conducting takedown operations (gUFO Role - anti-rigid)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#TakedownOperatorRole"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES


@dataclass
class UserAccessPatternAnalysis(InfrastructureAnalysis):
    """Analysis of user access patterns and geographic distribution based on infrastructure logs (gUFO Event)."""

    CLASS_IRI: str = "https://cacontology.projectvic.org/infrastructure#UserAccessPatternAnalysis"
    NAMESPACE_PREFIX: str = "cacontology-platform-infrastructure"
    JSONLD_CONTEXT: ClassVar[dict[str, str]] = NAMESPACES
    user_geographic_spread: Optional[int] = field(default=None, metadata={'jsonld_key': 'cacontology-platform-infrastructure:userGeographicSpread', 'required': False, 'cardinality': 'zero_or_one', 'range_iri': 'http://www.w3.org/2001/XMLSchema#nonNegativeInteger', 'alternate_range_iris': []})
