"""Shared Turtle rendering for vendored technique catalogs (ATT&CK, ATLAS).

Both ``sync_attack_catalog.py`` and ``sync_atlas_catalog.py`` emit catalogs in
the UCO 1.5.0 ``uco-action:Technique`` metaclass pattern: every technique is a
punned ``owl:Class`` that is also an instance of ``uco-action:Technique``,
specializes ``uco-action:Action`` (directly, or through its parent technique
for sub-techniques), and carries ``uco-action:techniqueID``. Tactics,
platforms, matrix membership and replacement links are OWL annotations that
reuse Dublin Core terms, so the catalogs mint no new vocabulary.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

ANNOTATION_PREFIXES = (
    "@prefix owl: <http://www.w3.org/2002/07/owl#> .\n"
    "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
    "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n"
    "@prefix dcterms: <http://purl.org/dc/terms/> .\n"
    "@prefix action: <https://ontology.unifiedcyberontology.org/uco/action/> .\n"
)

ANNOTATION_DECLARATIONS = """\
dcterms:subject
\ta owl:AnnotationProperty ;
\trdfs:comment "In this catalog: a tactic (adversary goal) the technique serves."@en ;
\t.

dcterms:coverage
\ta owl:AnnotationProperty ;
\trdfs:comment "In this catalog: a platform the technique applies to."@en ;
\t.

dcterms:isPartOf
\ta owl:AnnotationProperty ;
\trdfs:comment "In this catalog: the matrix (knowledge-base domain) a technique or tactic belongs to."@en ;
\t.

dcterms:isReplacedBy
\ta owl:AnnotationProperty ;
\trdfs:comment "In this catalog: the technique that superseded a revoked technique."@en ;
\t.

dcterms:identifier
\ta owl:AnnotationProperty ;
\t.

dcterms:modified
\ta owl:AnnotationProperty ;
\t.
"""

_CITATION_RE = re.compile(r"\s*\(Citation:[^)]*\)")
_MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]*\)")
_HTML_TAG_RE = re.compile(r"</?[a-zA-Z][^>]*>")
_SENTENCE_END_RE = re.compile(r"(?<=[.!?])\s")


def ttl_string(text: str) -> str:
    """Escape *text* as the body of a single-line Turtle string literal."""

    out = (
        text.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\r", " ")
        .replace("\n", " ")
        .replace("\t", " ")
    )
    return re.sub(r" {2,}", " ", out).strip()


def summarize_description(markdown: str, max_chars: int = 500) -> str:
    """First paragraph of an upstream markdown description, as plain text.

    Citation markers, markdown links and inline HTML are reduced to their
    text, and the result is cut on a sentence boundary at or below
    *max_chars* (falling back to a hard cut with an ellipsis).
    """

    text = markdown.strip()
    if not text:
        return ""
    paragraph = re.split(r"\n\s*\n", text, maxsplit=1)[0]
    paragraph = _CITATION_RE.sub("", paragraph)
    paragraph = _MD_LINK_RE.sub(r"\1", paragraph)
    paragraph = _HTML_TAG_RE.sub("", paragraph)
    paragraph = re.sub(r"\s+", " ", paragraph).strip()
    if len(paragraph) <= max_chars:
        return paragraph
    cut = 0
    for match in _SENTENCE_END_RE.finditer(paragraph):
        if match.start() > max_chars:
            break
        cut = match.start()
    if cut >= max_chars // 3:
        return paragraph[:cut].strip()
    return paragraph[: max_chars - 1].rstrip() + "\u2026"


def technique_sort_key(technique_id: str) -> tuple:
    """Order IDs numerically: T1001 < T1001.001 < T1002; AML.T0000 < AML.T0000.000."""

    parts = re.findall(r"\d+", technique_id)
    prefix = re.sub(r"[\d.]+$", "", technique_id)
    return (prefix, tuple(int(p) for p in parts))


@dataclass
class TechniqueEntry:
    """One technique, ready to render as a punned Technique class."""

    technique_id: str
    curie: str
    name: str
    description: str = ""
    parent_curie: str | None = None
    tactic_curies: list[str] = field(default_factory=list)
    platforms: list[str] = field(default_factory=list)
    matrix_iris: list[str] = field(default_factory=list)
    see_also: list[str] = field(default_factory=list)
    replaced_by_curies: list[str] = field(default_factory=list)
    deprecated: bool = False
    modified: str | None = None
    comment_suffix: str = ""


@dataclass
class TacticEntry:
    """A tactic, rendered as an annotation value (not a class)."""

    tactic_id: str
    curie: str
    name: str
    description: str = ""
    matrix_iri: str | None = None
    see_also: str | None = None


def qualify_subtechnique_labels(techniques: dict[str, TechniqueEntry]) -> None:
    """Label sub-techniques "Parent: Sub" (MITRE's display convention)."""

    by_curie = {entry.curie: entry for entry in techniques.values()}
    base_names = {curie: entry.name for curie, entry in by_curie.items()}
    for entry in techniques.values():
        parent_name = base_names.get(entry.parent_curie or "")
        if parent_name and not entry.name.startswith(f"{parent_name}: "):
            entry.name = f"{parent_name}: {entry.name}"


def render_technique(entry: TechniqueEntry, framework: str) -> str:
    comment = entry.description or f"{framework} technique {entry.technique_id}."
    if entry.comment_suffix:
        comment = f"{comment} {entry.comment_suffix}"
    lines = [
        entry.curie,
        "\ta",
        "\t\towl:Class ,",
        "\t\taction:Technique",
        "\t\t;",
        f"\trdfs:subClassOf {entry.parent_curie or 'action:Action'} ;",
        f'\trdfs:label "{ttl_string(entry.name)}"@en ;',
        f'\trdfs:comment "{ttl_string(comment)}"@en ;',
        f'\taction:techniqueID "{entry.technique_id}" ;',
    ]
    for tactic in entry.tactic_curies:
        lines.append(f"\tdcterms:subject {tactic} ;")
    for platform in entry.platforms:
        lines.append(f'\tdcterms:coverage "{ttl_string(platform)}" ;')
    for matrix in entry.matrix_iris:
        lines.append(f"\tdcterms:isPartOf <{matrix}> ;")
    for replacement in entry.replaced_by_curies:
        lines.append(f"\tdcterms:isReplacedBy {replacement} ;")
    if entry.modified:
        lines.append(f'\tdcterms:modified "{entry.modified}"^^xsd:date ;')
    for url in entry.see_also:
        lines.append(f"\trdfs:seeAlso <{url}> ;")
    if entry.deprecated:
        lines.append("\towl:deprecated true ;")
    lines.append("\t.")
    return "\n".join(lines) + "\n"


def render_tactic(entry: TacticEntry) -> str:
    lines = [
        entry.curie,
        f'\trdfs:label "{ttl_string(entry.name)}"@en ;',
    ]
    if entry.description:
        lines.append(f'\trdfs:comment "{ttl_string(entry.description)}"@en ;')
    lines.append(f'\tdcterms:identifier "{entry.tactic_id}" ;')
    if entry.matrix_iri:
        lines.append(f"\tdcterms:isPartOf <{entry.matrix_iri}> ;")
    if entry.see_also:
        lines.append(f"\trdfs:seeAlso <{entry.see_also}> ;")
    lines.append("\t.")
    return "\n".join(lines) + "\n"


def render_matrix(iri: str, label: str, version: str, see_also: str | None = None) -> str:
    lines = [
        f"<{iri}>",
        f'\trdfs:label "{ttl_string(label)}"@en ;',
        f'\towl:versionInfo "{version}" ;',
    ]
    if see_also:
        lines.append(f"\trdfs:seeAlso <{see_also}> ;")
    lines.append("\t.")
    return "\n".join(lines) + "\n"
