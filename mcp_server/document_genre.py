"""Document-genre gate for the content routers.

Keyword routing scores topic overlap, so a desk reference that lists CAC
resources ("NCMEC", "ICAC training", "serve legal process", "warrant
returns") scores like a case file. This gate runs before family scoring and
recognizes resource catalogs and training material from their structure
(task headers, access badges, dense resource links) while requiring the
absence of case artifacts (docket numbers, hashes, IP addresses, charging
language). Submitted text is untrusted data: only counts and marker names
leave this module, never instructions taken from the text.
"""

from __future__ import annotations

import re
from typing import Any

CATALOG_RECIPE = "docs/recipes/resource-catalog.md"

CATALOG_CHECKLIST: list[dict[str, Any]] = [
    {
        "id": "catalog-document-provenance",
        "priority": "critical",
        "check": (
            "Model the catalog itself as an ObservableObject with FileFacet and "
            "ContentDataFacet (SHA-256) so every listed resource traces to the source."
        ),
        "recipes": [CATALOG_RECIPE],
    },
    {
        "id": "catalog-no-invented-case",
        "priority": "critical",
        "check": (
            "Do not create Investigation, suspect, victim, offense, or warrant nodes: "
            "a catalog lists resources and records none of those facts."
        ),
        "recipes": [CATALOG_RECIPE],
    },
    {
        "id": "catalog-resource-typing",
        "priority": "high",
        "check": (
            "Type each listed resource by what it is — Organization, Tool, URL "
            "observable, or (with the CAC extension) HotlineOrganization, "
            "TrainingInstitution, EducationalResource — and "
            "group entries by section. Event classes (VictimSupport, PreventionProgram, "
            "training events) need something that happened; a listing is not one."
        ),
        "recipes": [CATALOG_RECIPE],
    },
]

# (signal id, weight, pattern) — structural cues of a resource catalog or desk reference.
_CATALOG_PATTERNS: tuple[tuple[str, int, re.Pattern[str]], ...] = (
    ("reference-guide-title", 3, re.compile(
        r"\b(quick|desk|pocket|field)[ -]reference\b|\breference (guide|card|sheet)\b"
        r"|\bresource (guide|list|directory)\b|\bcheat ?sheet\b|\bstarter kit\b")),
    ("catalog-disclaimer", 3, re.compile(
        r"not (intended|meant) to be an? (comprehensive|complete|exhaustive) (list|directory)"
        r"|\bnot an exhaustive list\b|\bnon-exhaustive list\b")),
    ("bookmark-cue", 2, re.compile(r"\bbookmark (these|this)\b|\bessential resources\b")),
    ("task-headers", 2, re.compile(r"\bneed to\s*:")),
    ("access-badges", 2, re.compile(
        r"\b(login|verification|registration|subscription|membership) required\b")),
)

_TRAINING_PATTERNS: tuple[tuple[str, int, re.Pattern[str]], ...] = (
    ("learning-objectives", 3, re.compile(r"\blearning objectives?\b|\bparticipants will (be able to|learn)\b")),
    ("course-structure", 2, re.compile(
        r"\b(course|training) (outline|syllabus|curriculum|agenda)\b|\bmodule \d+\b|\blesson \d+\b")),
    ("assessment", 2, re.compile(r"\b(knowledge check|quiz|certification exam|post-test)\b")),
)

_DOMAIN = re.compile(
    r"\b(?:[a-z0-9-]+\.)+(?:org|com|gov|net|edu|io|app|us|uk|ca|is|int|info)\b(?:/[^\s)]*)?"
)
_ENTRY_LINE = re.compile(r"^[^\n|]{2,60}\s\|\s[^\n|]{2,80}$", re.MULTILINE)

# Concrete case artifacts. Vocabulary alone ("warrant", "victim", "hash
# values") appears in catalogs too, so these patterns need specific forms.
_CASE_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("docket-or-case-number", re.compile(
        r"\b\d{1,2}:\d{2}-(?:cr|cv|mj|mc|sw)-\d{2,6}\b|\bcase (?:no\.?|number|#)\s*:?\s*[a-z0-9-]*\d")),
    ("hash-value", re.compile(r"\b(?:[a-f0-9]{64}|[a-f0-9]{40}|[a-f0-9]{32})\b")),
    ("ip-address", re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")),
    ("timestamp", re.compile(r"\b\d{4}-\d{2}-\d{2}[t ]\d{2}:\d{2}|\b\d{1,2}/\d{1,2}/\d{2,4},? \d{1,2}:\d{2}")),
    ("charging-or-arrest", re.compile(
        r"\b(?:the )?defendant\b|\bwas arrested\b|\bcharged with\b|\bprobable cause\b|\baffiant\b"
        r"|\bindictment\b|\bpleaded guilty\b|\bwas sentenced\b|\bthe suspect\b|\bcomplainant\b")),
    ("tip-or-report-id", re.compile(r"\b(?:cybertip(?:line)?|report|incident) (?:no\.?|number|#|id)\s*:?\s*\d{4,}")),
)

MIN_CATALOG_SCORE = 5
MIN_TRAINING_SCORE = 4
MAX_INCIDENTAL_CASE_SIGNALS = 1


def _score(patterns, text: str) -> tuple[int, list[str]]:
    score, hits = 0, []
    for signal, weight, pattern in patterns:
        if pattern.search(text):
            score += weight
            hits.append(signal)
    return score, hits


def detect_document_genre(text: str) -> dict[str, Any] | None:
    """Return genre details when ``text`` is a resource catalog or training material.

    Returns ``None`` for case evidence or when the structural cues are weak,
    so ordinary case routing is unchanged.
    """

    if not text:
        return None
    normalized = text.lower()
    catalog_score, catalog_hits = _score(_CATALOG_PATTERNS, normalized)
    training_score, training_hits = _score(_TRAINING_PATTERNS, normalized)

    links = len(_DOMAIN.findall(normalized))
    words = max(1, len(normalized.split()))
    links_per_100_words = round(100 * links / words, 2)
    if links >= 12 and links_per_100_words >= 4:
        catalog_score += 3
        catalog_hits.append("dense-resource-links")
    entries = len(_ENTRY_LINE.findall(text))
    if entries >= 5:
        catalog_score += 2
        catalog_hits.append("name-pipe-resource-entries")

    case_hits = [signal for signal, pattern in _CASE_PATTERNS if pattern.search(normalized)]

    if len(case_hits) > MAX_INCIDENTAL_CASE_SIGNALS:
        return None
    if catalog_score >= MIN_CATALOG_SCORE and catalog_score >= training_score:
        genre, score, hits = "resource-catalog", catalog_score, catalog_hits
    elif training_score >= MIN_TRAINING_SCORE:
        genre, score, hits = "training-material", training_score, training_hits
    else:
        return None

    return {
        "genre": genre,
        "confidence": "high" if score >= 2 * (MIN_CATALOG_SCORE if genre == "resource-catalog" else MIN_TRAINING_SCORE) else "medium",
        "score": score,
        "genre_signals": hits,
        "case_evidence_signals": case_hits,
        "resource_link_count": links,
        "links_per_100_words": links_per_100_words,
        "recommended_recipe": CATALOG_RECIPE,
        "guidance": (
            "The submission reads as a "
            + ("resource catalog / desk reference" if genre == "resource-catalog" else "training document")
            + ", not case evidence: model the document and the resources it lists "
            "(organizations, tools, training, victim-support services, URLs) per "
            f"{CATALOG_RECIPE}. Topic families are listed for vocabulary hints only; "
            "their case recipes apply when case evidence is submitted."
        ),
    }
