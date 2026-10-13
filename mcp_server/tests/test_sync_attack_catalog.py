"""Unit tests for the pinned ATT&CK STIX catalog synchronizer."""

from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

from tools.sync_attack_catalog import (
    build_catalog,
    catalog_technique_ids,
    load_bundles,
    render_catalog,
)

FIXTURE = (
    Path(__file__).resolve().parent / "fixtures" / "enterprise-attack-mini.json"
)


def _offline_bundles(tmp_path: Path):
    shutil.copy(FIXTURE, tmp_path / "enterprise-attack-19.1.json")
    return load_bundles("19.1", tmp_path, ["enterprise"])


def test_offline_load_records_sha256(tmp_path):
    bundles = _offline_bundles(tmp_path)
    _, provenance = bundles["enterprise"]
    assert provenance["sha256"] == hashlib.sha256(FIXTURE.read_bytes()).hexdigest()
    assert provenance["source"].endswith("(local copy)")


def test_build_catalog_from_mini_stix(tmp_path):
    techniques, _ = build_catalog(_offline_bundles(tmp_path))
    assert "T1566.001" in techniques
    assert techniques["T1566.001"].name.endswith("Spearphishing Attachment")


def test_render_catalog_contains_punning_pattern(tmp_path):
    bundles = _offline_bundles(tmp_path)
    techniques, tactics = build_catalog(bundles)
    ttl = render_catalog(techniques, tactics, attack_version="19.1", bundles=bundles)
    assert "attack:T1566.001" in ttl
    assert "action:Technique" in ttl
    assert 'action:techniqueID "T1566.001"' in ttl
    assert "GENERATED FILE" in ttl
    assert "The MITRE Corporation" in ttl


def test_live_catalog_is_the_complete_release():
    ids = catalog_technique_ids()
    manifest = json.loads(
        (Path(__file__).resolve().parents[2] / "extensions/attack-technique/manifest.json")
        .read_text(encoding="utf-8")
    )
    assert len(ids) == manifest["provenance"]["technique_count"]
    assert len(ids) > 1000
    assert {"T1566.001", "T1059.007", "T0800", "T1398"} <= ids
