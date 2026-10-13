//! Auto-generated uco-configuration types for the CASE/UCO ontology.

use serde::Serialize;
use crate::graph::CaseObject;

use crate::uco::core::ExternalReference;
use crate::uco::core::Facet;
use crate::uco::core::IdentityAbstraction;
use crate::uco::core::MarkingDefinitionAbstraction;
use crate::uco::core::UcoObject;

/// A configuration is a grouping of characteristics unique to a set of parameters or initial settings for the use of a tool, application, software, or other cyber object.
#[derive(Debug, Clone, Serialize)]
pub struct Configuration {
    #[serde(skip_serializing)]
    pub class_iri: &'static str,
    #[serde(rename = "uco-configuration:configurationEntry")]
    pub configuration_entry: Vec<ConfigurationEntry>,
    #[serde(rename = "uco-configuration:dependencies")]
    pub dependencies: Vec<Dependency>,
    #[serde(rename = "uco-configuration:usageContextAssumptions")]
    pub usage_context_assumptions: Vec<String>,
    #[serde(rename = "uco-core:createdBy")]
    pub created_by: Option<IdentityAbstraction>,
    #[serde(rename = "uco-core:description")]
    pub description: Vec<String>,
    #[serde(rename = "uco-core:externalReference")]
    pub external_reference: Vec<ExternalReference>,
    #[serde(rename = "uco-core:hasFacet")]
    pub has_facet: Vec<Facet>,
    #[serde(rename = "uco-core:modifiedTime")]
    pub modified_time: Vec<String>,
    #[serde(rename = "uco-core:name")]
    pub name: Option<String>,
    #[serde(rename = "uco-core:objectCreatedTime")]
    pub object_created_time: Option<String>,
    #[serde(rename = "uco-core:objectMarking")]
    pub object_marking: Vec<MarkingDefinitionAbstraction>,
    #[serde(rename = "uco-core:objectStatus")]
    pub object_status: Option<String>,
    #[serde(rename = "uco-core:specVersion")]
    pub spec_version: Option<String>,
    #[serde(rename = "uco-core:tag")]
    pub tag: Vec<String>,
}

impl Configuration {
    pub const CLASS_IRI: &'static str = "https://ontology.unifiedcyberontology.org/uco/configuration/Configuration";
    pub const NAMESPACE_PREFIX: &'static str = "uco-configuration";

    pub fn builder() -> ConfigurationBuilder {
        ConfigurationBuilder {
            configuration_entry: Vec::new(),
            dependencies: Vec::new(),
            usage_context_assumptions: Vec::new(),
            created_by: None,
            description: Vec::new(),
            external_reference: Vec::new(),
            has_facet: Vec::new(),
            modified_time: Vec::new(),
            name: None,
            object_created_time: None,
            object_marking: Vec::new(),
            object_status: None,
            spec_version: None,
            tag: Vec::new(),
        }
    }
}

#[derive(Debug, Default, Clone)]
pub struct ConfigurationBuilder {
    configuration_entry: Vec<ConfigurationEntry>,
    dependencies: Vec<Dependency>,
    usage_context_assumptions: Vec<String>,
    created_by: Option<IdentityAbstraction>,
    description: Vec<String>,
    external_reference: Vec<ExternalReference>,
    has_facet: Vec<Facet>,
    modified_time: Vec<String>,
    name: Option<String>,
    object_created_time: Option<String>,
    object_marking: Vec<MarkingDefinitionAbstraction>,
    object_status: Option<String>,
    spec_version: Option<String>,
    tag: Vec<String>,
}

impl ConfigurationBuilder {
    pub fn configuration_entry(mut self, value: Vec<ConfigurationEntry>) -> Self {
        self.configuration_entry = value;
        self
    }

    pub fn dependencies(mut self, value: Vec<Dependency>) -> Self {
        self.dependencies = value;
        self
    }

    pub fn usage_context_assumptions(mut self, value: Vec<String>) -> Self {
        self.usage_context_assumptions = value;
        self
    }

    pub fn created_by(mut self, value: IdentityAbstraction) -> Self {
        self.created_by = Some(value);
        self
    }

    pub fn description(mut self, value: Vec<String>) -> Self {
        self.description = value;
        self
    }

    pub fn external_reference(mut self, value: Vec<ExternalReference>) -> Self {
        self.external_reference = value;
        self
    }

    pub fn has_facet(mut self, value: Vec<Facet>) -> Self {
        self.has_facet = value;
        self
    }

    pub fn modified_time(mut self, value: Vec<String>) -> Self {
        self.modified_time = value;
        self
    }

    pub fn name(mut self, value: String) -> Self {
        self.name = Some(value);
        self
    }

    pub fn object_created_time(mut self, value: String) -> Self {
        self.object_created_time = Some(value);
        self
    }

    pub fn object_marking(mut self, value: Vec<MarkingDefinitionAbstraction>) -> Self {
        self.object_marking = value;
        self
    }

    pub fn object_status(mut self, value: String) -> Self {
        self.object_status = Some(value);
        self
    }

    pub fn spec_version(mut self, value: String) -> Self {
        self.spec_version = Some(value);
        self
    }

    pub fn tag(mut self, value: Vec<String>) -> Self {
        self.tag = value;
        self
    }

    pub fn build(self) -> Configuration {
        Configuration {
            class_iri: Configuration::CLASS_IRI,
            configuration_entry: self.configuration_entry,
            dependencies: self.dependencies,
            usage_context_assumptions: self.usage_context_assumptions,
            created_by: self.created_by,
            description: self.description,
            external_reference: self.external_reference,
            has_facet: self.has_facet,
            modified_time: self.modified_time,
            name: self.name,
            object_created_time: self.object_created_time,
            object_marking: self.object_marking,
            object_status: self.object_status,
            spec_version: self.spec_version,
            tag: self.tag,
        }
    }
}

impl CaseObject for Configuration {
    fn class_iri() -> &'static str { Configuration::CLASS_IRI }
    fn type_name() -> &'static str { "Configuration" }
}

/// A configuration entry is a grouping of characteristics unique to a particular parameter or initial setting for the use of a tool, application, software, or other cyber object.
#[derive(Debug, Clone, Serialize)]
pub struct ConfigurationEntry {
    #[serde(skip_serializing)]
    pub class_iri: &'static str,
    #[serde(rename = "uco-configuration:itemDescription")]
    pub item_description: Option<String>,
    #[serde(rename = "uco-configuration:itemName")]
    pub item_name: Option<String>,
    #[serde(rename = "uco-configuration:itemObject")]
    pub item_object: Vec<UcoObject>,
    #[serde(rename = "uco-configuration:itemType")]
    pub item_type: Option<String>,
    #[serde(rename = "uco-configuration:itemValue")]
    pub item_value: Vec<String>,
}

impl ConfigurationEntry {
    pub const CLASS_IRI: &'static str = "https://ontology.unifiedcyberontology.org/uco/configuration/ConfigurationEntry";
    pub const NAMESPACE_PREFIX: &'static str = "uco-configuration";

    pub fn builder() -> ConfigurationEntryBuilder {
        ConfigurationEntryBuilder {
            item_description: None,
            item_name: None,
            item_object: Vec::new(),
            item_type: None,
            item_value: Vec::new(),
        }
    }
}

#[derive(Debug, Default, Clone)]
pub struct ConfigurationEntryBuilder {
    item_description: Option<String>,
    item_name: Option<String>,
    item_object: Vec<UcoObject>,
    item_type: Option<String>,
    item_value: Vec<String>,
}

impl ConfigurationEntryBuilder {
    pub fn item_description(mut self, value: String) -> Self {
        self.item_description = Some(value);
        self
    }

    pub fn item_name(mut self, value: String) -> Self {
        self.item_name = Some(value);
        self
    }

    pub fn item_object(mut self, value: Vec<UcoObject>) -> Self {
        self.item_object = value;
        self
    }

    pub fn item_type(mut self, value: String) -> Self {
        self.item_type = Some(value);
        self
    }

    pub fn item_value(mut self, value: Vec<String>) -> Self {
        self.item_value = value;
        self
    }

    pub fn build(self) -> ConfigurationEntry {
        ConfigurationEntry {
            class_iri: ConfigurationEntry::CLASS_IRI,
            item_description: self.item_description,
            item_name: self.item_name,
            item_object: self.item_object,
            item_type: self.item_type,
            item_value: self.item_value,
        }
    }
}

impl CaseObject for ConfigurationEntry {
    fn class_iri() -> &'static str { ConfigurationEntry::CLASS_IRI }
    fn type_name() -> &'static str { "ConfigurationEntry" }
}

/// A dependency is a grouping of characteristics unique to something that a tool or other software relies on to function as intended.
#[derive(Debug, Clone, Serialize)]
pub struct Dependency {
    #[serde(skip_serializing)]
    pub class_iri: &'static str,
    #[serde(rename = "uco-configuration:dependencyDescription")]
    pub dependency_description: Option<String>,
    #[serde(rename = "uco-configuration:dependencyType")]
    pub dependency_type: Option<String>,
}

impl Dependency {
    pub const CLASS_IRI: &'static str = "https://ontology.unifiedcyberontology.org/uco/configuration/Dependency";
    pub const NAMESPACE_PREFIX: &'static str = "uco-configuration";

    pub fn builder() -> DependencyBuilder {
        DependencyBuilder {
            dependency_description: None,
            dependency_type: None,
        }
    }
}

#[derive(Debug, Default, Clone)]
pub struct DependencyBuilder {
    dependency_description: Option<String>,
    dependency_type: Option<String>,
}

impl DependencyBuilder {
    pub fn dependency_description(mut self, value: String) -> Self {
        self.dependency_description = Some(value);
        self
    }

    pub fn dependency_type(mut self, value: String) -> Self {
        self.dependency_type = Some(value);
        self
    }

    pub fn build(self) -> Dependency {
        Dependency {
            class_iri: Dependency::CLASS_IRI,
            dependency_description: self.dependency_description,
            dependency_type: self.dependency_type,
        }
    }
}

impl CaseObject for Dependency {
    fn class_iri() -> &'static str { Dependency::CLASS_IRI }
    fn type_name() -> &'static str { "Dependency" }
}
