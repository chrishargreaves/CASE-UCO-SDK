#!/usr/bin/env python3
"""Model a resource catalog / desk reference (synthetic sample) with typed CAC classes.

The catalog is a document that lists organizations, tools, training, and
prevention material. It records no investigation, so the graph holds the
document, one Grouping per section, and the listed resources — nothing else.
"""

from __future__ import annotations

import hashlib
import importlib.util
import sys
from pathlib import Path

from case_uco import CASEGraph
from case_uco.uco.core import ExternalReference, Grouping, Relationship
from case_uco.uco.identity import Organization
from case_uco.uco.observable import ContentDataFacet, FileFacet, ObservableObject
from case_uco.uco.tool import Tool
from case_uco.uco.types import Hash

if importlib.util.find_spec("case_uco_cac") is None:  # checkout without `pip install case-uco-cac`
    sdk_root = Path(sys.modules["case_uco"].__file__).resolve().parents[2]
    sys.path.insert(0, str(sdk_root / "packages" / "case-uco-cac" / "python"))

from case_uco_cac.cacontology_hotlines import HotlineOrganization  # noqa: E402
from case_uco_cac.cacontology_prevention import EducationalResource  # noqa: E402
from case_uco_cac.cacontology_training import TrainingInstitution  # noqa: E402

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "resource-catalog-sample.txt"
OUTPUT = HERE / "resource-catalog.jsonld"


def link(url: str, access: str | None = None) -> ExternalReference:
    return ExternalReference(
        reference_url=url,
        defining_context=f"Listed in the catalog; access: {access}" if access else "Listed in the catalog",
    )


def build() -> CASEGraph:
    data = SOURCE.read_bytes()
    graph = CASEGraph(kb_prefix="http://example.org/kb/resource-catalog/")

    guide = graph.create(
        ObservableObject,
        has_facet=[
            FileFacet(file_name=SOURCE.name, size_in_bytes=len(data)),
            ContentDataFacet(
                hash=[Hash(hash_method="SHA256", hash_value=hashlib.sha256(data).hexdigest().upper())],
                size_in_bytes=len(data),
                mime_type="text/plain",
            ),
        ],
    )

    def section(title: str, members: list) -> None:
        grouping = graph.create(Grouping, name=title, context=["Resource catalog section"], object=members)
        graph.create(
            Relationship,
            source=[grouping],
            target=guide,
            kind_of_relationship="Contained_Within",
            is_directional=True,
        )

    portal = graph.create(
        Organization, name="Example Task Force Portal",
        external_reference=[link("https://taskforce.example.org", "login required")],
    )
    section("Day 1 starter kit", [portal])

    hotline = graph.create(
        HotlineOrganization, name="Example Hotline Network", label="Example Hotline Network",
        description="Receives online reports of child sexual abuse material.",
        external_reference=[link("https://hotline.example.org/report")],
    )
    helpline = graph.create(
        Organization, name="Example Family Helpline",
        description="Connects victims and families with crisis support resources.",
        external_reference=[link("https://help.example.org")],
    )
    section("Hotlines", [hotline, helpline])

    training = graph.create(
        TrainingInstitution, name="Example Training Center", label="Example Training Center",
        description="Investigator and examiner training.",
        external_reference=[link("https://training.example.org/courses")],
    )
    academy = graph.create(
        TrainingInstitution, name="Example Forensics Academy", label="Example Forensics Academy",
        description="Computer forensics training and certification.",
        external_reference=[link("https://academy.example.net", "paid")],
    )
    section("Training and certification", [training, academy])

    imager = graph.create(
        Tool, name="Example Imaging Tool", description="Acquires images of computers and storage media.",
        external_reference=[link("https://tools.example.com/imager", "free download")],
    )
    hash_library = graph.create(
        Tool, name="Example Hash Library", description="Hash sets for victim identification.",
        external_reference=[link("https://hashes.example.org", "login required")],
    )
    section("Digital forensics resources", [imager, hash_library])

    nonprofit = graph.create(
        Organization, name="Example Safety Nonprofit",
        external_reference=[link("https://parents.example.org")],
    )
    for_parents = graph.create(
        EducationalResource, name="For Parents", label="For Parents", created_by=nonprofit,
        target_audience="parents", description="Resources to protect children online.",
        external_reference=[link("https://parents.example.org")],
    )
    school_program = graph.create(
        EducationalResource, name="School Program", label="School Program", created_by=nonprofit,
        target_audience="children", description="Internet safety education for children and communities.",
        external_reference=[link("https://schools.example.org")],
    )
    section("Prevention and parent resources", [nonprofit, for_parents, school_program])

    statutes = graph.create(
        EducationalResource, name="Federal Statutes", label="Federal Statutes",
        target_audience="professionals", description="Federal child exploitation statutes.",
        external_reference=[link("https://law.example.edu/statutes")],
    )
    warrant_builder = graph.create(
        Tool, name="Example Warrant Builder", description="Drafts legal process for a jurisdiction and provider.",
        external_reference=[link("https://warrants.example.org", "login required")],
    )
    section("Legal resources", [statutes, warrant_builder])
    return graph


if __name__ == "__main__":
    build().write(str(OUTPUT))
    print(f"Wrote {OUTPUT}")
