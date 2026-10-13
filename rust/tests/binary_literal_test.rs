//! Binary ranges serialize as typed hex/base64 literals, matching Python (#36).

use case_uco::graph::{encode_base64_binary, encode_hex_binary};
use case_uco::uco::observable::ExtractedString;
use case_uco::uco::types::Hash;

#[test]
fn hash_value_is_uppercase_hex_binary_literal() {
    let hash = Hash::builder()
        .hash_method("SHA256".to_string())
        .hash_value(vec![0xde, 0xad, 0xbe, 0xef])
        .build();
    let value = serde_json::to_value(&hash).expect("serialize");
    assert_eq!(value["uco-types:hashValue"]["@type"], "xsd:hexBinary");
    assert_eq!(value["uco-types:hashValue"]["@value"], "DEADBEEF");
}

#[test]
fn absent_hash_value_stays_null() {
    let hash = Hash::builder().hash_method("SHA256".to_string()).build();
    let value = serde_json::to_value(&hash).expect("serialize");
    assert!(value["uco-types:hashValue"].is_null());
}

#[test]
fn base64_binary_range_uses_base64_lexical_form() {
    let extracted = ExtractedString::builder()
        .byte_string_value(b"hello".to_vec())
        .build();
    let value = serde_json::to_value(&extracted).expect("serialize");
    assert_eq!(value["uco-observable:byteStringValue"]["@type"], "xsd:base64Binary");
    assert_eq!(value["uco-observable:byteStringValue"]["@value"], "aGVsbG8=");
}

#[test]
fn encoders_match_rfc4648_vectors() {
    assert_eq!(encode_hex_binary(&[]), "");
    assert_eq!(encode_hex_binary(&[0x00, 0x0f, 0xa0]), "000FA0");
    for (input, expected) in [
        ("", ""),
        ("f", "Zg=="),
        ("fo", "Zm8="),
        ("foo", "Zm9v"),
        ("foob", "Zm9vYg=="),
        ("fooba", "Zm9vYmE="),
        ("foobar", "Zm9vYmFy"),
    ] {
        assert_eq!(encode_base64_binary(input.as_bytes()), expected);
    }
}
