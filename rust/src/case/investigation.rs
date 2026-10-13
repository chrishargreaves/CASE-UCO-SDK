//! Auto-generated case-investigation types for the CASE/UCO ontology.

use serde::Serialize;
use crate::graph::CaseObject;

use crate::uco::action::Action;
use crate::uco::action::ArrayOfAction;
use crate::uco::core::ExternalReference;
use crate::uco::core::Facet;
use crate::uco::core::IdentityAbstraction;
use crate::uco::core::MarkingDefinitionAbstraction;
use crate::uco::core::UcoObject;
use crate::uco::location::Location;

/// Attorney is a role involved in preparing, interpreting, and applying law.
#[derive(Debug, Clone, Serialize)]
pub struct Attorney {
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
}

impl Attorney {
    pub const CLASS_IRI: &'static str = "https://ontology.caseontology.org/case/investigation/Attorney";
    pub const NAMESPACE_PREFIX: &'static str = "case-investigation";

    pub fn builder() -> AttorneyBuilder {
        AttorneyBuilder {
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
pub struct AttorneyBuilder {
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

impl AttorneyBuilder {
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

    pub fn build(self) -> Attorney {
        Attorney {
            class_iri: Attorney::CLASS_IRI,
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

impl CaseObject for Attorney {
    fn class_iri() -> &'static str { Attorney::CLASS_IRI }
    fn type_name() -> &'static str { "Attorney" }
}

/// An authorization is a grouping of characteristics unique to some form of authoritative permission identified for investigative action.
#[derive(Debug, Clone, Serialize)]
pub struct Authorization {
    #[serde(skip_serializing)]
    pub class_iri: &'static str,
    #[serde(rename = "case-investigation:authorizationIdentifier")]
    pub authorization_identifier: Vec<String>,
    #[serde(rename = "case-investigation:authorizationType")]
    pub authorization_type: Option<String>,
    #[serde(rename = "uco-core:createdBy")]
    pub created_by: Option<IdentityAbstraction>,
    #[serde(rename = "uco-core:description")]
    pub description: Vec<String>,
    #[serde(rename = "uco-core:endTime")]
    pub end_time: Option<String>,
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
    #[serde(rename = "uco-core:startTime")]
    pub start_time: Option<String>,
    #[serde(rename = "uco-core:tag")]
    pub tag: Vec<String>,
}

impl Authorization {
    pub const CLASS_IRI: &'static str = "https://ontology.caseontology.org/case/investigation/Authorization";
    pub const NAMESPACE_PREFIX: &'static str = "case-investigation";

    pub fn builder() -> AuthorizationBuilder {
        AuthorizationBuilder {
            authorization_identifier: Vec::new(),
            authorization_type: None,
            created_by: None,
            description: Vec::new(),
            end_time: None,
            external_reference: Vec::new(),
            has_facet: Vec::new(),
            modified_time: Vec::new(),
            name: None,
            object_created_time: None,
            object_marking: Vec::new(),
            object_status: None,
            spec_version: None,
            start_time: None,
            tag: Vec::new(),
        }
    }
}

#[derive(Debug, Default, Clone)]
pub struct AuthorizationBuilder {
    authorization_identifier: Vec<String>,
    authorization_type: Option<String>,
    created_by: Option<IdentityAbstraction>,
    description: Vec<String>,
    end_time: Option<String>,
    external_reference: Vec<ExternalReference>,
    has_facet: Vec<Facet>,
    modified_time: Vec<String>,
    name: Option<String>,
    object_created_time: Option<String>,
    object_marking: Vec<MarkingDefinitionAbstraction>,
    object_status: Option<String>,
    spec_version: Option<String>,
    start_time: Option<String>,
    tag: Vec<String>,
}

impl AuthorizationBuilder {
    pub fn authorization_identifier(mut self, value: Vec<String>) -> Self {
        self.authorization_identifier = value;
        self
    }

    pub fn authorization_type(mut self, value: String) -> Self {
        self.authorization_type = Some(value);
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

    pub fn end_time(mut self, value: String) -> Self {
        self.end_time = Some(value);
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

    pub fn start_time(mut self, value: String) -> Self {
        self.start_time = Some(value);
        self
    }

    pub fn tag(mut self, value: Vec<String>) -> Self {
        self.tag = value;
        self
    }

    pub fn build(self) -> Authorization {
        Authorization {
            class_iri: Authorization::CLASS_IRI,
            authorization_identifier: self.authorization_identifier,
            authorization_type: self.authorization_type,
            created_by: self.created_by,
            description: self.description,
            end_time: self.end_time,
            external_reference: self.external_reference,
            has_facet: self.has_facet,
            modified_time: self.modified_time,
            name: self.name,
            object_created_time: self.object_created_time,
            object_marking: self.object_marking,
            object_status: self.object_status,
            spec_version: self.spec_version,
            start_time: self.start_time,
            tag: self.tag,
        }
    }
}

impl CaseObject for Authorization {
    fn class_iri() -> &'static str { Authorization::CLASS_IRI }
    fn type_name() -> &'static str { "Authorization" }
}

/// Examiner is a role involved in providing scientific evaluations of evidence that are used to aid law enforcement investigations and court cases.
#[derive(Debug, Clone, Serialize)]
pub struct Examiner {
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
}

impl Examiner {
    pub const CLASS_IRI: &'static str = "https://ontology.caseontology.org/case/investigation/Examiner";
    pub const NAMESPACE_PREFIX: &'static str = "case-investigation";

    pub fn builder() -> ExaminerBuilder {
        ExaminerBuilder {
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
pub struct ExaminerBuilder {
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

impl ExaminerBuilder {
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

    pub fn build(self) -> Examiner {
        Examiner {
            class_iri: Examiner::CLASS_IRI,
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

impl CaseObject for Examiner {
    fn class_iri() -> &'static str { Examiner::CLASS_IRI }
    fn type_name() -> &'static str { "Examiner" }
}

/// An examiner action lifecycle is an action pattern consisting of an ordered set of actions or subordinate action-lifecycles performed by an entity acting in a role involved in providing scientific eval
#[derive(Debug, Clone, Serialize)]
pub struct ExaminerActionLifecycle {
    #[serde(skip_serializing)]
    pub class_iri: &'static str,
    #[serde(rename = "uco-action:environment")]
    pub environment: Option<UcoObject>,
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
    #[serde(rename = "uco-action:phase")]
    pub phase: Option<ArrayOfAction>,
    #[serde(rename = "uco-action:result")]
    pub result: Vec<UcoObject>,
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

impl ExaminerActionLifecycle {
    pub const CLASS_IRI: &'static str = "https://ontology.caseontology.org/case/investigation/ExaminerActionLifecycle";
    pub const NAMESPACE_PREFIX: &'static str = "case-investigation";

    pub fn builder() -> ExaminerActionLifecycleBuilder {
        ExaminerActionLifecycleBuilder {
            environment: None,
            instrument: Vec::new(),
            location: Vec::new(),
            object: Vec::new(),
            participant: Vec::new(),
            performer: None,
            phase: None,
            result: Vec::new(),
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
pub struct ExaminerActionLifecycleBuilder {
    environment: Option<UcoObject>,
    instrument: Vec<UcoObject>,
    location: Vec<Location>,
    object: Vec<UcoObject>,
    participant: Vec<UcoObject>,
    performer: Option<UcoObject>,
    phase: Option<ArrayOfAction>,
    result: Vec<UcoObject>,
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

impl ExaminerActionLifecycleBuilder {
    pub fn environment(mut self, value: UcoObject) -> Self {
        self.environment = Some(value);
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

    pub fn phase(mut self, value: ArrayOfAction) -> Self {
        self.phase = Some(value);
        self
    }

    pub fn result(mut self, value: Vec<UcoObject>) -> Self {
        self.result = value;
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

    pub fn build(self) -> ExaminerActionLifecycle {
        ExaminerActionLifecycle {
            class_iri: ExaminerActionLifecycle::CLASS_IRI,
            environment: self.environment,
            instrument: self.instrument,
            location: self.location,
            object: self.object,
            participant: self.participant,
            performer: self.performer,
            phase: self.phase,
            result: self.result,
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

impl CaseObject for ExaminerActionLifecycle {
    fn class_iri() -> &'static str { ExaminerActionLifecycle::CLASS_IRI }
    fn type_name() -> &'static str { "ExaminerActionLifecycle" }
    fn validate(&self) -> Result<(), String> {
        if self.phase.is_none() {
            return Err("ExaminerActionLifecycle.phase is required but was not provided.".to_string());
        }
        Ok(())
    }
}

/// An investigation is a grouping of characteristics unique to an exploration of the facts involved in a cyber-relevant set of suspicious activity.
#[derive(Debug, Clone, Serialize)]
pub struct Investigation {
    #[serde(skip_serializing)]
    pub class_iri: &'static str,
    #[serde(rename = "case-investigation:focus")]
    pub focus: Vec<String>,
    #[serde(rename = "case-investigation:investigationForm")]
    pub investigation_form: Option<String>,
    #[serde(rename = "case-investigation:investigationStatus")]
    pub investigation_status: Option<String>,
    #[serde(rename = "case-investigation:relevantAuthorization")]
    pub relevant_authorization: Vec<Authorization>,
    #[serde(rename = "uco-core:createdBy")]
    pub created_by: Option<IdentityAbstraction>,
    #[serde(rename = "uco-core:description")]
    pub description: Vec<String>,
    #[serde(rename = "uco-core:endTime")]
    pub end_time: Option<String>,
    #[serde(rename = "uco-core:externalReference")]
    pub external_reference: Vec<ExternalReference>,
    #[serde(rename = "uco-core:hasFacet")]
    pub has_facet: Vec<Facet>,
    #[serde(rename = "uco-core:modifiedTime")]
    pub modified_time: Vec<String>,
    #[serde(rename = "uco-core:name")]
    pub name: Option<String>,
    #[serde(rename = "uco-core:object")]
    pub object: Vec<UcoObject>,
    #[serde(rename = "uco-core:objectCreatedTime")]
    pub object_created_time: Option<String>,
    #[serde(rename = "uco-core:objectMarking")]
    pub object_marking: Vec<MarkingDefinitionAbstraction>,
    #[serde(rename = "uco-core:objectStatus")]
    pub object_status: Option<String>,
    #[serde(rename = "uco-core:specVersion")]
    pub spec_version: Option<String>,
    #[serde(rename = "uco-core:startTime")]
    pub start_time: Option<String>,
    #[serde(rename = "uco-core:tag")]
    pub tag: Vec<String>,
}

impl Investigation {
    pub const CLASS_IRI: &'static str = "https://ontology.caseontology.org/case/investigation/Investigation";
    pub const NAMESPACE_PREFIX: &'static str = "case-investigation";

    pub fn builder() -> InvestigationBuilder {
        InvestigationBuilder {
            focus: Vec::new(),
            investigation_form: None,
            investigation_status: None,
            relevant_authorization: Vec::new(),
            created_by: None,
            description: Vec::new(),
            end_time: None,
            external_reference: Vec::new(),
            has_facet: Vec::new(),
            modified_time: Vec::new(),
            name: None,
            object: Vec::new(),
            object_created_time: None,
            object_marking: Vec::new(),
            object_status: None,
            spec_version: None,
            start_time: None,
            tag: Vec::new(),
        }
    }
}

#[derive(Debug, Default, Clone)]
pub struct InvestigationBuilder {
    focus: Vec<String>,
    investigation_form: Option<String>,
    investigation_status: Option<String>,
    relevant_authorization: Vec<Authorization>,
    created_by: Option<IdentityAbstraction>,
    description: Vec<String>,
    end_time: Option<String>,
    external_reference: Vec<ExternalReference>,
    has_facet: Vec<Facet>,
    modified_time: Vec<String>,
    name: Option<String>,
    object: Vec<UcoObject>,
    object_created_time: Option<String>,
    object_marking: Vec<MarkingDefinitionAbstraction>,
    object_status: Option<String>,
    spec_version: Option<String>,
    start_time: Option<String>,
    tag: Vec<String>,
}

impl InvestigationBuilder {
    pub fn focus(mut self, value: Vec<String>) -> Self {
        self.focus = value;
        self
    }

    pub fn investigation_form(mut self, value: String) -> Self {
        self.investigation_form = Some(value);
        self
    }

    pub fn investigation_status(mut self, value: String) -> Self {
        self.investigation_status = Some(value);
        self
    }

    pub fn relevant_authorization(mut self, value: Vec<Authorization>) -> Self {
        self.relevant_authorization = value;
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

    pub fn end_time(mut self, value: String) -> Self {
        self.end_time = Some(value);
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

    pub fn object(mut self, value: Vec<UcoObject>) -> Self {
        self.object = value;
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

    pub fn start_time(mut self, value: String) -> Self {
        self.start_time = Some(value);
        self
    }

    pub fn tag(mut self, value: Vec<String>) -> Self {
        self.tag = value;
        self
    }

    pub fn build(self) -> Investigation {
        Investigation {
            class_iri: Investigation::CLASS_IRI,
            focus: self.focus,
            investigation_form: self.investigation_form,
            investigation_status: self.investigation_status,
            relevant_authorization: self.relevant_authorization,
            created_by: self.created_by,
            description: self.description,
            end_time: self.end_time,
            external_reference: self.external_reference,
            has_facet: self.has_facet,
            modified_time: self.modified_time,
            name: self.name,
            object: self.object,
            object_created_time: self.object_created_time,
            object_marking: self.object_marking,
            object_status: self.object_status,
            spec_version: self.spec_version,
            start_time: self.start_time,
            tag: self.tag,
        }
    }
}

impl CaseObject for Investigation {
    fn class_iri() -> &'static str { Investigation::CLASS_IRI }
    fn type_name() -> &'static str { "Investigation" }
}

/// An investigative action is something that may be done or performed within the context of an investigation, typically to examine or analyze evidence or other data.
#[derive(Debug, Clone, Serialize)]
pub struct InvestigativeAction {
    #[serde(skip_serializing)]
    pub class_iri: &'static str,
    #[serde(rename = "case-investigation:wasInformedBy")]
    pub was_informed_by: Vec<InvestigativeAction>,
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

impl InvestigativeAction {
    pub const CLASS_IRI: &'static str = "https://ontology.caseontology.org/case/investigation/InvestigativeAction";
    pub const NAMESPACE_PREFIX: &'static str = "case-investigation";

    pub fn builder() -> InvestigativeActionBuilder {
        InvestigativeActionBuilder {
            was_informed_by: Vec::new(),
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
pub struct InvestigativeActionBuilder {
    was_informed_by: Vec<InvestigativeAction>,
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

impl InvestigativeActionBuilder {
    pub fn was_informed_by(mut self, value: Vec<InvestigativeAction>) -> Self {
        self.was_informed_by = value;
        self
    }

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

    pub fn build(self) -> InvestigativeAction {
        InvestigativeAction {
            class_iri: InvestigativeAction::CLASS_IRI,
            was_informed_by: self.was_informed_by,
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

impl CaseObject for InvestigativeAction {
    fn class_iri() -> &'static str { InvestigativeAction::CLASS_IRI }
    fn type_name() -> &'static str { "InvestigativeAction" }
}

/// Investigator is a role involved in coordinating an investigation.
#[derive(Debug, Clone, Serialize)]
pub struct Investigator {
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
}

impl Investigator {
    pub const CLASS_IRI: &'static str = "https://ontology.caseontology.org/case/investigation/Investigator";
    pub const NAMESPACE_PREFIX: &'static str = "case-investigation";

    pub fn builder() -> InvestigatorBuilder {
        InvestigatorBuilder {
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
pub struct InvestigatorBuilder {
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

impl InvestigatorBuilder {
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

    pub fn build(self) -> Investigator {
        Investigator {
            class_iri: Investigator::CLASS_IRI,
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

impl CaseObject for Investigator {
    fn class_iri() -> &'static str { Investigator::CLASS_IRI }
    fn type_name() -> &'static str { "Investigator" }
}

/// A provenance record is a grouping of characteristics unique to the provenantial (chronology of the ownership, custody or location) connection between an investigative action and a set of observations 
#[derive(Debug, Clone, Serialize)]
pub struct ProvenanceRecord {
    #[serde(skip_serializing)]
    pub class_iri: &'static str,
    #[serde(rename = "case-investigation:exhibitNumber")]
    pub exhibit_number: Option<String>,
    #[serde(rename = "case-investigation:rootExhibitNumber")]
    pub root_exhibit_number: Vec<String>,
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
    #[serde(rename = "uco-core:object")]
    pub object: Vec<UcoObject>,
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

impl ProvenanceRecord {
    pub const CLASS_IRI: &'static str = "https://ontology.caseontology.org/case/investigation/ProvenanceRecord";
    pub const NAMESPACE_PREFIX: &'static str = "case-investigation";

    pub fn builder() -> ProvenanceRecordBuilder {
        ProvenanceRecordBuilder {
            exhibit_number: None,
            root_exhibit_number: Vec::new(),
            created_by: None,
            description: Vec::new(),
            external_reference: Vec::new(),
            has_facet: Vec::new(),
            modified_time: Vec::new(),
            name: None,
            object: Vec::new(),
            object_created_time: None,
            object_marking: Vec::new(),
            object_status: None,
            spec_version: None,
            tag: Vec::new(),
        }
    }
}

#[derive(Debug, Default, Clone)]
pub struct ProvenanceRecordBuilder {
    exhibit_number: Option<String>,
    root_exhibit_number: Vec<String>,
    created_by: Option<IdentityAbstraction>,
    description: Vec<String>,
    external_reference: Vec<ExternalReference>,
    has_facet: Vec<Facet>,
    modified_time: Vec<String>,
    name: Option<String>,
    object: Vec<UcoObject>,
    object_created_time: Option<String>,
    object_marking: Vec<MarkingDefinitionAbstraction>,
    object_status: Option<String>,
    spec_version: Option<String>,
    tag: Vec<String>,
}

impl ProvenanceRecordBuilder {
    pub fn exhibit_number(mut self, value: String) -> Self {
        self.exhibit_number = Some(value);
        self
    }

    pub fn root_exhibit_number(mut self, value: Vec<String>) -> Self {
        self.root_exhibit_number = value;
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

    pub fn object(mut self, value: Vec<UcoObject>) -> Self {
        self.object = value;
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

    pub fn build(self) -> ProvenanceRecord {
        ProvenanceRecord {
            class_iri: ProvenanceRecord::CLASS_IRI,
            exhibit_number: self.exhibit_number,
            root_exhibit_number: self.root_exhibit_number,
            created_by: self.created_by,
            description: self.description,
            external_reference: self.external_reference,
            has_facet: self.has_facet,
            modified_time: self.modified_time,
            name: self.name,
            object: self.object,
            object_created_time: self.object_created_time,
            object_marking: self.object_marking,
            object_status: self.object_status,
            spec_version: self.spec_version,
            tag: self.tag,
        }
    }
}

impl CaseObject for ProvenanceRecord {
    fn class_iri() -> &'static str { ProvenanceRecord::CLASS_IRI }
    fn type_name() -> &'static str { "ProvenanceRecord" }
}

/// Subject is a role whose conduct is within the scope of an investigation.
#[derive(Debug, Clone, Serialize)]
pub struct Subject {
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
}

impl Subject {
    pub const CLASS_IRI: &'static str = "https://ontology.caseontology.org/case/investigation/Subject";
    pub const NAMESPACE_PREFIX: &'static str = "case-investigation";

    pub fn builder() -> SubjectBuilder {
        SubjectBuilder {
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
pub struct SubjectBuilder {
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

impl SubjectBuilder {
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

    pub fn build(self) -> Subject {
        Subject {
            class_iri: Subject::CLASS_IRI,
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

impl CaseObject for Subject {
    fn class_iri() -> &'static str { Subject::CLASS_IRI }
    fn type_name() -> &'static str { "Subject" }
}

/// A subject action lifecycle is an action pattern consisting of an ordered set of multiple actions or subordinate action-lifecycles performed by an entity acting in a role whose conduct may be within th
#[derive(Debug, Clone, Serialize)]
pub struct SubjectActionLifecycle {
    #[serde(skip_serializing)]
    pub class_iri: &'static str,
    #[serde(rename = "uco-action:environment")]
    pub environment: Option<UcoObject>,
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
    #[serde(rename = "uco-action:phase")]
    pub phase: Option<ArrayOfAction>,
    #[serde(rename = "uco-action:result")]
    pub result: Vec<UcoObject>,
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

impl SubjectActionLifecycle {
    pub const CLASS_IRI: &'static str = "https://ontology.caseontology.org/case/investigation/SubjectActionLifecycle";
    pub const NAMESPACE_PREFIX: &'static str = "case-investigation";

    pub fn builder() -> SubjectActionLifecycleBuilder {
        SubjectActionLifecycleBuilder {
            environment: None,
            instrument: Vec::new(),
            location: Vec::new(),
            object: Vec::new(),
            participant: Vec::new(),
            performer: None,
            phase: None,
            result: Vec::new(),
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
pub struct SubjectActionLifecycleBuilder {
    environment: Option<UcoObject>,
    instrument: Vec<UcoObject>,
    location: Vec<Location>,
    object: Vec<UcoObject>,
    participant: Vec<UcoObject>,
    performer: Option<UcoObject>,
    phase: Option<ArrayOfAction>,
    result: Vec<UcoObject>,
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

impl SubjectActionLifecycleBuilder {
    pub fn environment(mut self, value: UcoObject) -> Self {
        self.environment = Some(value);
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

    pub fn phase(mut self, value: ArrayOfAction) -> Self {
        self.phase = Some(value);
        self
    }

    pub fn result(mut self, value: Vec<UcoObject>) -> Self {
        self.result = value;
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

    pub fn build(self) -> SubjectActionLifecycle {
        SubjectActionLifecycle {
            class_iri: SubjectActionLifecycle::CLASS_IRI,
            environment: self.environment,
            instrument: self.instrument,
            location: self.location,
            object: self.object,
            participant: self.participant,
            performer: self.performer,
            phase: self.phase,
            result: self.result,
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

impl CaseObject for SubjectActionLifecycle {
    fn class_iri() -> &'static str { SubjectActionLifecycle::CLASS_IRI }
    fn type_name() -> &'static str { "SubjectActionLifecycle" }
    fn validate(&self) -> Result<(), String> {
        if self.phase.is_none() {
            return Err("SubjectActionLifecycle.phase is required but was not provided.".to_string());
        }
        Ok(())
    }
}

/// A victim action lifecycle is an action pattern consisting of an ordered set of multiple actions or subordinate action-lifecycles performed by an entity acting in a role characterized by its potential 
#[derive(Debug, Clone, Serialize)]
pub struct VictimActionLifecycle {
    #[serde(skip_serializing)]
    pub class_iri: &'static str,
    #[serde(rename = "uco-action:environment")]
    pub environment: Option<UcoObject>,
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
    #[serde(rename = "uco-action:phase")]
    pub phase: Option<ArrayOfAction>,
    #[serde(rename = "uco-action:result")]
    pub result: Vec<UcoObject>,
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

impl VictimActionLifecycle {
    pub const CLASS_IRI: &'static str = "https://ontology.caseontology.org/case/investigation/VictimActionLifecycle";
    pub const NAMESPACE_PREFIX: &'static str = "case-investigation";

    pub fn builder() -> VictimActionLifecycleBuilder {
        VictimActionLifecycleBuilder {
            environment: None,
            instrument: Vec::new(),
            location: Vec::new(),
            object: Vec::new(),
            participant: Vec::new(),
            performer: None,
            phase: None,
            result: Vec::new(),
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
pub struct VictimActionLifecycleBuilder {
    environment: Option<UcoObject>,
    instrument: Vec<UcoObject>,
    location: Vec<Location>,
    object: Vec<UcoObject>,
    participant: Vec<UcoObject>,
    performer: Option<UcoObject>,
    phase: Option<ArrayOfAction>,
    result: Vec<UcoObject>,
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

impl VictimActionLifecycleBuilder {
    pub fn environment(mut self, value: UcoObject) -> Self {
        self.environment = Some(value);
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

    pub fn phase(mut self, value: ArrayOfAction) -> Self {
        self.phase = Some(value);
        self
    }

    pub fn result(mut self, value: Vec<UcoObject>) -> Self {
        self.result = value;
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

    pub fn build(self) -> VictimActionLifecycle {
        VictimActionLifecycle {
            class_iri: VictimActionLifecycle::CLASS_IRI,
            environment: self.environment,
            instrument: self.instrument,
            location: self.location,
            object: self.object,
            participant: self.participant,
            performer: self.performer,
            phase: self.phase,
            result: self.result,
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

impl CaseObject for VictimActionLifecycle {
    fn class_iri() -> &'static str { VictimActionLifecycle::CLASS_IRI }
    fn type_name() -> &'static str { "VictimActionLifecycle" }
    fn validate(&self) -> Result<(), String> {
        if self.phase.is_none() {
            return Err("VictimActionLifecycle.phase is required but was not provided.".to_string());
        }
        Ok(())
    }
}
