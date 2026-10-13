//! Auto-generated uco-analysis types for the CASE/UCO ontology.

use serde::Serialize;
use crate::graph::CaseObject;

use crate::uco::action::Action;
use crate::uco::core::ExternalReference;
use crate::uco::core::Facet;
use crate::uco::core::IdentityAbstraction;
use crate::uco::core::MarkingDefinitionAbstraction;
use crate::uco::core::UcoObject;
use crate::uco::location::Location;

/// An analysis is an action of detailed examination of something in order to understand its nature, context or essential features.
#[derive(Debug, Clone, Serialize)]
pub struct Analysis {
    #[serde(skip_serializing)]
    pub class_iri: &'static str,
    #[serde(rename = "uco-action:actionCount")]
    pub action_count: Option<u64>,
    #[serde(rename = "uco-action:actionStatus")]
    pub action_status: Option<String>,
    #[serde(rename = "uco-action:endTime")]
    pub end_time: Option<String>,
    #[serde(rename = "uco-action:environment")]
    pub environment: Option<UcoObject>,
    #[serde(rename = "uco-action:error")]
    pub error: Vec<UcoObject>,
    #[serde(rename = "uco-action:instrument")]
    pub instrument: Vec<UcoObject>,
    #[serde(rename = "uco-action:location")]
    pub location: Vec<Location>,
    #[serde(rename = "uco-action:object")]
    pub object: Vec<UcoObject>,
    #[serde(rename = "uco-action:participant")]
    pub participant: Vec<UcoObject>,
    #[serde(rename = "uco-action:performer")]
    pub performer: Option<UcoObject>,
    #[serde(rename = "uco-action:result")]
    pub result: Vec<UcoObject>,
    #[serde(rename = "uco-action:startTime")]
    pub start_time: Option<String>,
    #[serde(rename = "uco-action:subaction")]
    pub subaction: Vec<Action>,
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

impl Analysis {
    pub const CLASS_IRI: &'static str = "https://ontology.unifiedcyberontology.org/uco/analysis/Analysis";
    pub const NAMESPACE_PREFIX: &'static str = "uco-analysis";

    pub fn builder() -> AnalysisBuilder {
        AnalysisBuilder {
            action_count: None,
            action_status: None,
            end_time: None,
            environment: None,
            error: Vec::new(),
            instrument: Vec::new(),
            location: Vec::new(),
            object: Vec::new(),
            participant: Vec::new(),
            performer: None,
            result: Vec::new(),
            start_time: None,
            subaction: Vec::new(),
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
pub struct AnalysisBuilder {
    action_count: Option<u64>,
    action_status: Option<String>,
    end_time: Option<String>,
    environment: Option<UcoObject>,
    error: Vec<UcoObject>,
    instrument: Vec<UcoObject>,
    location: Vec<Location>,
    object: Vec<UcoObject>,
    participant: Vec<UcoObject>,
    performer: Option<UcoObject>,
    result: Vec<UcoObject>,
    start_time: Option<String>,
    subaction: Vec<Action>,
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

impl AnalysisBuilder {
    pub fn action_count(mut self, value: u64) -> Self {
        self.action_count = Some(value);
        self
    }

    pub fn action_status(mut self, value: String) -> Self {
        self.action_status = Some(value);
        self
    }

    pub fn end_time(mut self, value: String) -> Self {
        self.end_time = Some(value);
        self
    }

    pub fn environment(mut self, value: UcoObject) -> Self {
        self.environment = Some(value);
        self
    }

    pub fn error(mut self, value: Vec<UcoObject>) -> Self {
        self.error = value;
        self
    }

    pub fn instrument(mut self, value: Vec<UcoObject>) -> Self {
        self.instrument = value;
        self
    }

    pub fn location(mut self, value: Vec<Location>) -> Self {
        self.location = value;
        self
    }

    pub fn object(mut self, value: Vec<UcoObject>) -> Self {
        self.object = value;
        self
    }

    pub fn participant(mut self, value: Vec<UcoObject>) -> Self {
        self.participant = value;
        self
    }

    pub fn performer(mut self, value: UcoObject) -> Self {
        self.performer = Some(value);
        self
    }

    pub fn result(mut self, value: Vec<UcoObject>) -> Self {
        self.result = value;
        self
    }

    pub fn start_time(mut self, value: String) -> Self {
        self.start_time = Some(value);
        self
    }

    pub fn subaction(mut self, value: Vec<Action>) -> Self {
        self.subaction = value;
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

    pub fn build(self) -> Analysis {
        Analysis {
            class_iri: Analysis::CLASS_IRI,
            action_count: self.action_count,
            action_status: self.action_status,
            end_time: self.end_time,
            environment: self.environment,
            error: self.error,
            instrument: self.instrument,
            location: self.location,
            object: self.object,
            participant: self.participant,
            performer: self.performer,
            result: self.result,
            start_time: self.start_time,
            subaction: self.subaction,
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

impl CaseObject for Analysis {
    fn class_iri() -> &'static str { Analysis::CLASS_IRI }
    fn type_name() -> &'static str { "Analysis" }
}

/// An analytic result is a characterization of the understanding resulting from an analysis action.
#[derive(Debug, Clone, Serialize)]
pub struct AnalyticResult {
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
    #[serde(rename = "uco-core:statement")]
    pub statement: Vec<String>,
    #[serde(rename = "uco-core:tag")]
    pub tag: Vec<String>,
}

impl AnalyticResult {
    pub const CLASS_IRI: &'static str = "https://ontology.unifiedcyberontology.org/uco/analysis/AnalyticResult";
    pub const NAMESPACE_PREFIX: &'static str = "uco-analysis";

    pub fn builder() -> AnalyticResultBuilder {
        AnalyticResultBuilder {
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
            statement: Vec::new(),
            tag: Vec::new(),
        }
    }
}

#[derive(Debug, Default, Clone)]
pub struct AnalyticResultBuilder {
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
    statement: Vec<String>,
    tag: Vec<String>,
}

impl AnalyticResultBuilder {
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

    pub fn statement(mut self, value: Vec<String>) -> Self {
        self.statement = value;
        self
    }

    pub fn tag(mut self, value: Vec<String>) -> Self {
        self.tag = value;
        self
    }

    pub fn build(self) -> AnalyticResult {
        AnalyticResult {
            class_iri: AnalyticResult::CLASS_IRI,
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
            statement: self.statement,
            tag: self.tag,
        }
    }
}

impl CaseObject for AnalyticResult {
    fn class_iri() -> &'static str { AnalyticResult::CLASS_IRI }
    fn type_name() -> &'static str { "AnalyticResult" }
}

/// An analytic result facet is a grouping of characteristics unique to the results of an analysis action.
#[derive(Debug, Clone, Serialize)]
pub struct AnalyticResultFacet {
    #[serde(skip_serializing)]
    pub class_iri: &'static str,
}

impl AnalyticResultFacet {
    pub const CLASS_IRI: &'static str = "https://ontology.unifiedcyberontology.org/uco/analysis/AnalyticResultFacet";
    pub const NAMESPACE_PREFIX: &'static str = "uco-analysis";

    pub fn builder() -> AnalyticResultFacetBuilder {
        AnalyticResultFacetBuilder {
        }
    }
}

#[derive(Debug, Default, Clone)]
pub struct AnalyticResultFacetBuilder {
}

impl AnalyticResultFacetBuilder {
    pub fn build(self) -> AnalyticResultFacet {
        AnalyticResultFacet {
            class_iri: AnalyticResultFacet::CLASS_IRI,
        }
    }
}

impl CaseObject for AnalyticResultFacet {
    fn class_iri() -> &'static str { AnalyticResultFacet::CLASS_IRI }
    fn type_name() -> &'static str { "AnalyticResultFacet" }
}

/// An artifact classification is a single specific assertion that a particular class of a classification taxonomy applies to something.
#[derive(Debug, Clone, Serialize)]
pub struct ArtifactClassification {
    #[serde(skip_serializing)]
    pub class_iri: &'static str,
    #[serde(rename = "uco-analysis:class")]
    pub class: Vec<String>,
    #[serde(rename = "uco-analysis:classificationConfidence")]
    pub classification_confidence: Option<f64>,
}

impl ArtifactClassification {
    pub const CLASS_IRI: &'static str = "https://ontology.unifiedcyberontology.org/uco/analysis/ArtifactClassification";
    pub const NAMESPACE_PREFIX: &'static str = "uco-analysis";

    pub fn builder() -> ArtifactClassificationBuilder {
        ArtifactClassificationBuilder {
            class: Vec::new(),
            classification_confidence: None,
        }
    }
}

#[derive(Debug, Default, Clone)]
pub struct ArtifactClassificationBuilder {
    class: Vec<String>,
    classification_confidence: Option<f64>,
}

impl ArtifactClassificationBuilder {
    pub fn class(mut self, value: Vec<String>) -> Self {
        self.class = value;
        self
    }

    pub fn classification_confidence(mut self, value: f64) -> Self {
        self.classification_confidence = Some(value);
        self
    }

    pub fn build(self) -> ArtifactClassification {
        ArtifactClassification {
            class_iri: ArtifactClassification::CLASS_IRI,
            class: self.class,
            classification_confidence: self.classification_confidence,
        }
    }
}

impl CaseObject for ArtifactClassification {
    fn class_iri() -> &'static str { ArtifactClassification::CLASS_IRI }
    fn type_name() -> &'static str { "ArtifactClassification" }
    fn validate(&self) -> Result<(), String> {
        if self.class.is_empty() {
            return Err("ArtifactClassification.class requires at least one value.".to_string());
        }
        Ok(())
    }
}

/// An artifact classification result facet is a grouping of characteristics unique to the results of an artifact classification analysis action.
#[derive(Debug, Clone, Serialize)]
pub struct ArtifactClassificationResultFacet {
    #[serde(skip_serializing)]
    pub class_iri: &'static str,
    #[serde(rename = "uco-analysis:classification")]
    pub classification: Vec<ArtifactClassification>,
}

impl ArtifactClassificationResultFacet {
    pub const CLASS_IRI: &'static str = "https://ontology.unifiedcyberontology.org/uco/analysis/ArtifactClassificationResultFacet";
    pub const NAMESPACE_PREFIX: &'static str = "uco-analysis";

    pub fn builder() -> ArtifactClassificationResultFacetBuilder {
        ArtifactClassificationResultFacetBuilder {
            classification: Vec::new(),
        }
    }
}

#[derive(Debug, Default, Clone)]
pub struct ArtifactClassificationResultFacetBuilder {
    classification: Vec<ArtifactClassification>,
}

impl ArtifactClassificationResultFacetBuilder {
    pub fn classification(mut self, value: Vec<ArtifactClassification>) -> Self {
        self.classification = value;
        self
    }

    pub fn build(self) -> ArtifactClassificationResultFacet {
        ArtifactClassificationResultFacet {
            class_iri: ArtifactClassificationResultFacet::CLASS_IRI,
            classification: self.classification,
        }
    }
}

impl CaseObject for ArtifactClassificationResultFacet {
    fn class_iri() -> &'static str { ArtifactClassificationResultFacet::CLASS_IRI }
    fn type_name() -> &'static str { "ArtifactClassificationResultFacet" }
}
