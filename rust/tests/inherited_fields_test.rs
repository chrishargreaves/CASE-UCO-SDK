//! Rust structs carry inherited properties, matching Python, Java, and C# (#35).

use case_uco::uco::core::{Relationship, UcoObject};
use case_uco::uco::observable::ObservableRelationship;

#[test]
fn relationship_has_uco_object_fields() {
    let rel = Relationship::builder()
        .name("rel".to_string())
        .description(vec!["described".to_string()])
        .tag(vec!["t".to_string()])
        .source(vec![UcoObject::builder().build()])
        .target(UcoObject::builder().build())
        .kind_of_relationship("Contained_Within".to_string())
        .build();
    let value = serde_json::to_value(&rel).expect("serialize");
    assert_eq!(value["uco-core:name"], "rel");
    assert_eq!(value["uco-core:description"][0], "described");
    assert_eq!(value["uco-core:tag"][0], "t");
}

#[test]
fn observable_relationship_has_relationship_and_uco_object_fields() {
    let rel = ObservableRelationship::builder()
        .name("obs-rel".to_string())
        .kind_of_relationship("Contained_Within".to_string())
        .is_directional(true)
        .build();
    let value = serde_json::to_value(&rel).expect("serialize");
    assert_eq!(value["uco-core:name"], "obs-rel");
    assert_eq!(value["uco-core:kindOfRelationship"], "Contained_Within");
}
