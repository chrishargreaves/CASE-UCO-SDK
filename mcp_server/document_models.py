"""Shared document extraction models used by the processor and semantic mapper."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

# A provider row can legitimately associate many account/device/network facts.
# Keep a denial-of-service ceiling without dropping ordinary wide spreadsheets.
MAX_EVENT_CONTEXT = 128


@dataclass(frozen=True)
class ExtractedRecord:
    """One reviewable record extracted from a source document.

    ``anchor`` (Spec026 extraction-bundle contract 1.0) locates the record in
    the canonical extracted content. Records that cannot be honestly located
    carry ``anchor=None`` and are simply absent from ``annotations.jsonld`` —
    anchors are never fabricated.

    When ``ontology_class`` is set (semantic mapping stage), the case graph
    node uses that verified CASE/UCO class instead of a generic
    ``uco-observable:ObservableObject`` ExtractedString wrapper.
    """

    label: str
    text: str
    anchor: dict[str, Any] | None = None
    # A normalized entity can occur many times in one source.  Keep one
    # CASE/UCO object for the identity while retaining every source location
    # as an annotation.  This avoids graph-node explosions without making
    # later occurrences disappear from the document reader.
    additional_anchors: tuple[dict[str, Any], ...] = ()
    # Stable identities of other records that were present in the same
    # provider row.  Row Events resolve these into uco-core:eventContext so
    # timestamp/IP/account/device co-occurrence remains queryable.
    context_identities: tuple[tuple[str, str], ...] = ()
    ontology_class: str | None = None
    graph_facets: tuple[dict[str, Any], ...] = ()
    extra_properties: dict[str, Any] | None = None
