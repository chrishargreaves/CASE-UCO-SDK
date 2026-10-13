"""Every extension manifest must satisfy extensions/manifest-schema.json.

Nothing enforced the schema before v1.24.0, so it drifted: six of nine
manifests carried prose in fields the schema declares as enums, and two used
keys (`depends_on`, `provenance`) the schema never declared. Both classes of
drift are silent — the manifests are only read key-by-key at runtime — so a
test is the only thing that keeps the schema honest.
"""

from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import pytest

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
SCHEMA_PATH = PROJECT_ROOT / "extensions" / "manifest-schema.json"

MANIFESTS = sorted(PROJECT_ROOT.glob("extensions/*/manifest.json"))


def _schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text())


def test_schema_is_itself_valid_draft7() -> None:
    jsonschema.Draft7Validator.check_schema(_schema())


def test_at_least_one_manifest_is_discovered() -> None:
    # Guards against the glob silently matching nothing, which would make
    # every parametrised case below vacuously pass.
    assert MANIFESTS, f"no manifests found under {PROJECT_ROOT / 'extensions'}"


@pytest.mark.parametrize("manifest_path", MANIFESTS, ids=lambda p: p.parent.name)
def test_manifest_conforms_to_schema(manifest_path: Path) -> None:
    manifest = json.loads(manifest_path.read_text())
    errors = sorted(
        jsonschema.Draft7Validator(_schema()).iter_errors(manifest),
        key=lambda e: list(e.path),
    )
    assert not errors, "\n".join(
        f"{'/'.join(map(str, e.path)) or '(root)'}: {e.message}" for e in errors
    )


@pytest.mark.parametrize("manifest_path", MANIFESTS, ids=lambda p: p.parent.name)
def test_manifest_name_matches_directory(manifest_path: Path) -> None:
    manifest = json.loads(manifest_path.read_text())
    assert manifest["name"] == manifest_path.parent.name


@pytest.mark.parametrize("manifest_path", MANIFESTS, ids=lambda p: p.parent.name)
def test_declared_files_exist(manifest_path: Path) -> None:
    manifest = json.loads(manifest_path.read_text())
    ext_dir = manifest_path.parent
    missing = [
        rel
        for key in ("owl_files", "shacl_files", "bridge_files", "exemplar_files")
        for rel in manifest.get(key, [])
        if not (ext_dir / rel).is_file()
    ]
    assert not missing, f"declared but absent: {missing}"


@pytest.mark.parametrize("manifest_path", MANIFESTS, ids=lambda p: p.parent.name)
def test_depends_on_targets_resolve(manifest_path: Path) -> None:
    manifest = json.loads(manifest_path.read_text())
    known = {p.parent.name for p in MANIFESTS}
    unresolved = [d for d in manifest.get("depends_on", []) if d not in known]
    assert not unresolved, f"depends_on names no such extension: {unresolved}"


@pytest.mark.parametrize("manifest_path", MANIFESTS, ids=lambda p: p.parent.name)
def test_notes_keys_match_their_verdict_keys(manifest_path: Path) -> None:
    manifest = json.loads(manifest_path.read_text())
    verdicts = set(manifest.get("cdo_shapes_compatibility", {}))
    notes = set(manifest.get("cdo_shapes_notes", {}))
    assert notes <= verdicts, f"notes for profiles with no verdict: {notes - verdicts}"
