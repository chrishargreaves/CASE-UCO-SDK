//! Auto-generated uco-marking types for the CASE/UCO ontology.

use serde::Serialize;
use crate::graph::CaseObject;

use crate::uco::core::ExternalReference;
use crate::uco::core::Facet;
use crate::uco::core::IdentityAbstraction;
use crate::uco::core::MarkingDefinitionAbstraction;

/// A granular marking is a grouping of characteristics unique to specification of marking definitions (restrictions, permissions, and other guidance for how data can be used and shared) that apply to par
#[derive(Debug, Clone, Serialize)]
pub struct GranularMarking {
    #[serde(skip_serializing)]
    pub class_iri: &'static str,
    #[serde(rename = "uco-marking:contentSelectors")]
    pub content_selectors: Vec<String>,
    #[serde(rename = "uco-marking:marking")]
    pub marking: Vec<MarkingDefinition>,
}

impl GranularMarking {
    pub const CLASS_IRI: &'static str = "https://ontology.unifiedcyberontology.org/uco/marking/GranularMarking";
    pub const NAMESPACE_PREFIX: &'static str = "uco-marking";

    pub fn builder() -> GranularMarkingBuilder {
        GranularMarkingBuilder {
            content_selectors: Vec::new(),
            marking: Vec::new(),
        }
    }
}

#[derive(Debug, Default, Clone)]
pub struct GranularMarkingBuilder {
    content_selectors: Vec<String>,
    marking: Vec<MarkingDefinition>,
}

impl GranularMarkingBuilder {
    pub fn content_selectors(mut self, value: Vec<String>) -> Self {
        self.content_selectors = value;
        self
    }

    pub fn marking(mut self, value: Vec<MarkingDefinition>) -> Self {
        self.marking = value;
        self
    }

    pub fn build(self) -> GranularMarking {
        GranularMarking {
            class_iri: GranularMarking::CLASS_IRI,
            content_selectors: self.content_selectors,
            marking: self.marking,
        }
    }
}

impl CaseObject for GranularMarking {
    fn class_iri() -> &'static str { GranularMarking::CLASS_IRI }
    fn type_name() -> &'static str { "GranularMarking" }
}

/// A license marking is a grouping of characteristics unique to the expression of data marking definitions (restrictions, permissions, and other guidance for how data can be used and shared) to convey de
#[derive(Debug, Clone, Serialize)]
pub struct LicenseMarking {
    #[serde(skip_serializing)]
    pub class_iri: &'static str,
    #[serde(rename = "uco-marking:definitionType")]
    pub definition_type: Vec<String>,
    #[serde(rename = "uco-marking:license")]
    pub license: Option<String>,
}

impl LicenseMarking {
    pub const CLASS_IRI: &'static str = "https://ontology.unifiedcyberontology.org/uco/marking/LicenseMarking";
    pub const NAMESPACE_PREFIX: &'static str = "uco-marking";

    pub fn builder() -> LicenseMarkingBuilder {
        LicenseMarkingBuilder {
            definition_type: Vec::new(),
            license: None,
        }
    }
}

#[derive(Debug, Default, Clone)]
pub struct LicenseMarkingBuilder {
    definition_type: Vec<String>,
    license: Option<String>,
}

impl LicenseMarkingBuilder {
    pub fn definition_type(mut self, value: Vec<String>) -> Self {
        self.definition_type = value;
        self
    }

    pub fn license(mut self, value: String) -> Self {
        self.license = Some(value);
        self
    }

    pub fn build(self) -> LicenseMarking {
        LicenseMarking {
            class_iri: LicenseMarking::CLASS_IRI,
            definition_type: self.definition_type,
            license: self.license,
        }
    }
}

impl CaseObject for LicenseMarking {
    fn class_iri() -> &'static str { LicenseMarking::CLASS_IRI }
    fn type_name() -> &'static str { "LicenseMarking" }
    fn validate(&self) -> Result<(), String> {
        if self.license.is_none() {
            return Err("LicenseMarking.license is required but was not provided.".to_string());
        }
        Ok(())
    }
}

/// A marking definition is a grouping of characteristics unique to the expression of a specific data marking conveying restrictions, permissions, and other guidance for how marked data can be used and sh
#[derive(Debug, Clone, Serialize)]
pub struct MarkingDefinition {
    #[serde(skip_serializing)]
    pub class_iri: &'static str,
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
    #[serde(rename = "uco-marking:definition")]
    pub definition: Vec<MarkingModel>,
    #[serde(rename = "uco-marking:definitionType")]
    pub definition_type: Option<String>,
}

impl MarkingDefinition {
    pub const CLASS_IRI: &'static str = "https://ontology.unifiedcyberontology.org/uco/marking/MarkingDefinition";
    pub const NAMESPACE_PREFIX: &'static str = "uco-marking";

    pub fn builder() -> MarkingDefinitionBuilder {
        MarkingDefinitionBuilder {
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
            definition: Vec::new(),
            definition_type: None,
        }
    }
}

#[derive(Debug, Default, Clone)]
pub struct MarkingDefinitionBuilder {
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
    definition: Vec<MarkingModel>,
    definition_type: Option<String>,
}

impl MarkingDefinitionBuilder {
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

    pub fn definition(mut self, value: Vec<MarkingModel>) -> Self {
        self.definition = value;
        self
    }

    pub fn definition_type(mut self, value: String) -> Self {
        self.definition_type = Some(value);
        self
    }

    pub fn build(self) -> MarkingDefinition {
        MarkingDefinition {
            class_iri: MarkingDefinition::CLASS_IRI,
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
            definition: self.definition,
            definition_type: self.definition_type,
        }
    }
}

impl CaseObject for MarkingDefinition {
    fn class_iri() -> &'static str { MarkingDefinition::CLASS_IRI }
    fn type_name() -> &'static str { "MarkingDefinition" }
    fn validate(&self) -> Result<(), String> {
        if self.definition_type.is_none() {
            return Err("MarkingDefinition.definition_type is required but was not provided.".to_string());
        }
        Ok(())
    }
}

/// A marking model is a grouping of characteristics unique to the expression of a particular form of data marking definitions (restrictions, permissions, and other guidance for how data can be used and s
#[derive(Debug, Clone, Serialize)]
pub struct MarkingModel {
    #[serde(skip_serializing)]
    pub class_iri: &'static str,
}

impl MarkingModel {
    pub const CLASS_IRI: &'static str = "https://ontology.unifiedcyberontology.org/uco/marking/MarkingModel";
    pub const NAMESPACE_PREFIX: &'static str = "uco-marking";

    pub fn builder() -> MarkingModelBuilder {
        MarkingModelBuilder {
        }
    }
}

#[derive(Debug, Default, Clone)]
pub struct MarkingModelBuilder {
}

impl MarkingModelBuilder {
    pub fn build(self) -> MarkingModel {
        MarkingModel {
            class_iri: MarkingModel::CLASS_IRI,
        }
    }
}

impl CaseObject for MarkingModel {
    fn class_iri() -> &'static str { MarkingModel::CLASS_IRI }
    fn type_name() -> &'static str { "MarkingModel" }
}

/// A release-to marking is a grouping of characteristics unique to the expression of data marking definitions (restrictions, permissions, and other guidance for how data can be used and shared) to convey
#[derive(Debug, Clone, Serialize)]
pub struct ReleaseToMarking {
    #[serde(skip_serializing)]
    pub class_iri: &'static str,
    #[serde(rename = "uco-marking:authorizedIdentities")]
    pub authorized_identities: Vec<String>,
    #[serde(rename = "uco-marking:definitionType")]
    pub definition_type: Vec<String>,
}

impl ReleaseToMarking {
    pub const CLASS_IRI: &'static str = "https://ontology.unifiedcyberontology.org/uco/marking/ReleaseToMarking";
    pub const NAMESPACE_PREFIX: &'static str = "uco-marking";

    pub fn builder() -> ReleaseToMarkingBuilder {
        ReleaseToMarkingBuilder {
            authorized_identities: Vec::new(),
            definition_type: Vec::new(),
        }
    }
}

#[derive(Debug, Default, Clone)]
pub struct ReleaseToMarkingBuilder {
    authorized_identities: Vec<String>,
    definition_type: Vec<String>,
}

impl ReleaseToMarkingBuilder {
    pub fn authorized_identities(mut self, value: Vec<String>) -> Self {
        self.authorized_identities = value;
        self
    }

    pub fn definition_type(mut self, value: Vec<String>) -> Self {
        self.definition_type = value;
        self
    }

    pub fn build(self) -> ReleaseToMarking {
        ReleaseToMarking {
            class_iri: ReleaseToMarking::CLASS_IRI,
            authorized_identities: self.authorized_identities,
            definition_type: self.definition_type,
        }
    }
}

impl CaseObject for ReleaseToMarking {
    fn class_iri() -> &'static str { ReleaseToMarking::CLASS_IRI }
    fn type_name() -> &'static str { "ReleaseToMarking" }
    fn validate(&self) -> Result<(), String> {
        if self.authorized_identities.is_empty() {
            return Err("ReleaseToMarking.authorized_identities requires at least one value.".to_string());
        }
        Ok(())
    }
}

/// A statement marking is a grouping of characteristics unique to the expression of data marking definitions (restrictions, permissions, and other guidance for how data can be used and shared) to convey 
#[derive(Debug, Clone, Serialize)]
pub struct StatementMarking {
    #[serde(skip_serializing)]
    pub class_iri: &'static str,
    #[serde(rename = "uco-marking:definitionType")]
    pub definition_type: Vec<String>,
    #[serde(rename = "uco-marking:statement")]
    pub statement: Option<String>,
}

impl StatementMarking {
    pub const CLASS_IRI: &'static str = "https://ontology.unifiedcyberontology.org/uco/marking/StatementMarking";
    pub const NAMESPACE_PREFIX: &'static str = "uco-marking";

    pub fn builder() -> StatementMarkingBuilder {
        StatementMarkingBuilder {
            definition_type: Vec::new(),
            statement: None,
        }
    }
}

#[derive(Debug, Default, Clone)]
pub struct StatementMarkingBuilder {
    definition_type: Vec<String>,
    statement: Option<String>,
}

impl StatementMarkingBuilder {
    pub fn definition_type(mut self, value: Vec<String>) -> Self {
        self.definition_type = value;
        self
    }

    pub fn statement(mut self, value: String) -> Self {
        self.statement = Some(value);
        self
    }

    pub fn build(self) -> StatementMarking {
        StatementMarking {
            class_iri: StatementMarking::CLASS_IRI,
            definition_type: self.definition_type,
            statement: self.statement,
        }
    }
}

impl CaseObject for StatementMarking {
    fn class_iri() -> &'static str { StatementMarking::CLASS_IRI }
    fn type_name() -> &'static str { "StatementMarking" }
    fn validate(&self) -> Result<(), String> {
        if self.statement.is_none() {
            return Err("StatementMarking.statement is required but was not provided.".to_string());
        }
        Ok(())
    }
}

/// A terms of use marking is a grouping of characteristics unique to the expression of data marking definitions (restrictions, permissions, and other guidance for how data can be used and shared) to conv
#[derive(Debug, Clone, Serialize)]
pub struct TermsOfUseMarking {
    #[serde(skip_serializing)]
    pub class_iri: &'static str,
    #[serde(rename = "uco-marking:definitionType")]
    pub definition_type: Vec<String>,
    #[serde(rename = "uco-marking:termsOfUse")]
    pub terms_of_use: Option<String>,
}

impl TermsOfUseMarking {
    pub const CLASS_IRI: &'static str = "https://ontology.unifiedcyberontology.org/uco/marking/TermsOfUseMarking";
    pub const NAMESPACE_PREFIX: &'static str = "uco-marking";

    pub fn builder() -> TermsOfUseMarkingBuilder {
        TermsOfUseMarkingBuilder {
            definition_type: Vec::new(),
            terms_of_use: None,
        }
    }
}

#[derive(Debug, Default, Clone)]
pub struct TermsOfUseMarkingBuilder {
    definition_type: Vec<String>,
    terms_of_use: Option<String>,
}

impl TermsOfUseMarkingBuilder {
    pub fn definition_type(mut self, value: Vec<String>) -> Self {
        self.definition_type = value;
        self
    }

    pub fn terms_of_use(mut self, value: String) -> Self {
        self.terms_of_use = Some(value);
        self
    }

    pub fn build(self) -> TermsOfUseMarking {
        TermsOfUseMarking {
            class_iri: TermsOfUseMarking::CLASS_IRI,
            definition_type: self.definition_type,
            terms_of_use: self.terms_of_use,
        }
    }
}

impl CaseObject for TermsOfUseMarking {
    fn class_iri() -> &'static str { TermsOfUseMarking::CLASS_IRI }
    fn type_name() -> &'static str { "TermsOfUseMarking" }
    fn validate(&self) -> Result<(), String> {
        if self.terms_of_use.is_none() {
            return Err("TermsOfUseMarking.terms_of_use is required but was not provided.".to_string());
        }
        Ok(())
    }
}
