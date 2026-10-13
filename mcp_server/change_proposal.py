"""Change proposal drafts for the CASE, UCO, and CAC Ontology issue trackers.

A proposal is a discussion draft built around competency questions. Every
statement records where it came from, so ontologists can tell the
contributor's ideas from quoted sources and from AI-drafted text:

- ``contributor``: the contributor wrote or approved it; rendered unmarked.
- ``cited``: quoted or paraphrased from a person or publication; rendered
  ``*[from [label](url)]*``, and the URL must point at the exact comment or
  page quoted.
- ``ai``: written by an AI assistant; rendered ``*[AI-drafted]*``. Plain
  strings default to this.

The ontology design itself (classes, properties, SHACL, SPARQL) is left to
the committee section. A contributor's draft classes become local companion
files for testing (``.ttl``, ``-shapes.ttl``, ``.jsonld``, ``.sparql``) and
only appear in the issue body when ``include_design_sketch`` is set.
"""

from __future__ import annotations

import html
import re
import uuid
from dataclasses import dataclass, field
from typing import Any, Callable, Iterable
from urllib.parse import urlsplit

TRACKERS: dict[str, dict[str, str]] = {
    "UCO": {
        "repo": "ucoProject/UCO",
        "issues_url": "https://github.com/ucoProject/UCO/issues",
        "new_issue_url": "https://github.com/ucoProject/UCO/issues/new",
        "release_label": "CASE/UCO",
    },
    "CASE": {
        "repo": "casework/CASE",
        "issues_url": "https://github.com/casework/CASE/issues",
        "new_issue_url": "https://github.com/casework/CASE/issues/new",
        "release_label": "CASE/UCO",
    },
    "CAC": {
        "repo": "Project-VIC-International/CAC-Ontology",
        "issues_url": "https://github.com/Project-VIC-International/CAC-Ontology/issues",
        "new_issue_url": "https://github.com/Project-VIC-International/CAC-Ontology/issues/new",
        "release_label": "CAC Ontology",
    },
}

# CASE and UCO 1.5.0 are released; backward-compatible additions go to the
# next minor on ``develop``. The CAC Ontology versions independently.
DEFAULT_TARGET_RELEASE: dict[str, str | None] = {"UCO": "1.6.0", "CASE": "1.6.0", "CAC": None}

PROVENANCE_CONTRIBUTOR = "contributor"
PROVENANCE_AI = "ai"
PROVENANCE_CITED = "cited"
_PROVENANCE_ALIASES = {
    "contributor": PROVENANCE_CONTRIBUTOR,
    "human": PROVENANCE_CONTRIBUTOR,
    "user": PROVENANCE_CONTRIBUTOR,
    "ai": PROVENANCE_AI,
    "ai-drafted": PROVENANCE_AI,
    "ai_drafted": PROVENANCE_AI,
    "cited": PROVENANCE_CITED,
    "from": PROVENANCE_CITED,
    "source": PROVENANCE_CITED,
}

DISCUSSION_DRAFT_NOTE = (
    "_This is a discussion draft, not a finished design. Every part of it is "
    "open to challenge; the open questions are where input is most wanted._"
)
PROVENANCE_LEGEND = (
    "_Unmarked statements are the contributor's ideas. Statements marked "
    "*[from …]* come from the person or publication cited. Statements marked "
    "*[AI-drafted]* were written by an AI assistant, not supplied by the "
    "contributor._"
)
COMMITTEE_PLACEHOLDER = "To be filled out by the committee."
COMMITTEE_CHECKLIST = (
    "- [ ] Each defined term has an agreed definition and connection point",
    "- [ ] Benefits and risks recorded from discussion",
    "- [ ] Proposed ontology changes drafted and linked",
    "- [ ] Each competency question has a SPARQL query tested against example data",
    "- [ ] Example instance data passes `case_validate`",
    '- [ ] No "To be filled out by the committee." placeholders remain',
)

UCO_BASE = "https://ontology.unifiedcyberontology.org/"
CASE_BASE = "https://ontology.caseontology.org/"
CAC_BASE = "https://cacontology.projectvic.org"
XSD = "http://www.w3.org/2001/XMLSchema#"
FACET_IRI = UCO_BASE + "uco/core/Facet"

# Prefixes CASE and UCO documentation uses without the ``uco-`` form.
_DOC_PREFIX_ALIASES = {
    "core": UCO_BASE + "uco/core/",
    "observable": UCO_BASE + "uco/observable/",
    "action": UCO_BASE + "uco/action/",
    "identity": UCO_BASE + "uco/identity/",
    "location": UCO_BASE + "uco/location/",
    "tool": UCO_BASE + "uco/tool/",
    "types": UCO_BASE + "uco/types/",
    "role": UCO_BASE + "uco/role/",
    "marking": UCO_BASE + "uco/marking/",
    "pattern": UCO_BASE + "uco/pattern/",
    "analysis": UCO_BASE + "uco/analysis/",
    "configuration": UCO_BASE + "uco/configuration/",
    "victim": UCO_BASE + "uco/victim/",
    "investigation": CASE_BASE + "case/investigation/",
    "case-vocabulary": CASE_BASE + "case/vocabulary/",
}

# Vocabularies a proposal is likely to borrow from. A statement that names
# one next to a backticked term should link that term's definition page.
EXTERNAL_VOCABULARIES = (
    "schema.org", "akoma ntoso", "prov-o", "sosa", "ssn", "qudt", "foaf",
    "dublin core", "dcterms", "geosparql", "owl-time", "bfo", "gufo",
    "wikidata", "dcat", "skos", "uslm", "eli",
)

_STANDARD_RE = re.compile(r"\bstandards?\b", re.IGNORECASE)
_EXCLUSIONARY_RES = (
    re.compile(r"\bnone of us\b", re.IGNORECASE),
    re.compile(r"\bno(?:body| one)\s+(?:in|on|from)\s+(?:the|this|our)\b", re.IGNORECASE),
    re.compile(r"\bthere (?:are|is) no \w+\s+(?:in|on)\s+(?:the|this|our)\b", re.IGNORECASE),
)
_ENDORSEMENT_RES = (
    re.compile(r"\b(?:lead|leads|leading|leader|leaders)\b", re.IGNORECASE),
    re.compile(r"\bendors(?:e|es|ed|ing|ement)\b", re.IGNORECASE),
    re.compile(r"\bnist recommends?\b", re.IGNORECASE),
)
_URL_RE = re.compile(r"https?://[^\s)\]>`\"']+")
_BACKTICK_RE = re.compile(r"`[^`]+`")


class ProposalInputError(ValueError):
    """A typed input error (the message is the error code)."""

    def __init__(self, code: str, detail: str) -> None:
        super().__init__(code)
        self.code = code
        self.detail = detail


@dataclass(frozen=True)
class Statement:
    text: str
    provenance: str
    source_label: str | None = None
    source_url: str | None = None


@dataclass(frozen=True)
class CompetencyQuestion:
    question: Statement
    expected_answer: Statement | None
    sparql: str | None = None


@dataclass(frozen=True)
class Term:
    name: str
    vocabulary: str | None
    concept_url: str | None
    definition: Statement | None
    might_connect_to: Statement | None


@dataclass(frozen=True)
class OpenQuestion:
    question: Statement
    subquestions: tuple[Statement, ...] = ()


@dataclass(frozen=True)
class Reference:
    label: str
    url: str | None
    note: str | None = None


@dataclass
class Proposal:
    title: str
    target_repo: str
    target_release: str | None
    contributor: str | None
    ai_model: str | None
    sdk_version: str
    background: list[Statement] = field(default_factory=list)
    scenario: Statement | None = None
    competency_questions: list[CompetencyQuestion] = field(default_factory=list)
    terms: list[Term] = field(default_factory=list)
    open_questions: list[OpenQuestion] = field(default_factory=list)
    references: list[Reference] = field(default_factory=list)
    proposed_classes: list[dict[str, Any]] = field(default_factory=list)
    proposed_properties: list[dict[str, Any]] = field(default_factory=list)
    include_design_sketch: bool = False

    def statements(self) -> Iterable[tuple[str, Statement]]:
        for index, stmt in enumerate(self.background, 1):
            yield f"background[{index}]", stmt
        if self.scenario is not None:
            yield "scenario", self.scenario
        for index, cq in enumerate(self.competency_questions, 1):
            yield f"CQ {index} question", cq.question
            if cq.expected_answer is not None:
                yield f"CQ {index} expected answer", cq.expected_answer
        for index, term in enumerate(self.terms, 1):
            if term.definition is not None:
                yield f"Term {index} definition", term.definition
            if term.might_connect_to is not None:
                yield f"Term {index} might connect to", term.might_connect_to
        for index, oq in enumerate(self.open_questions, 1):
            yield f"open question {index}", oq.question
            for sub_index, sub in enumerate(oq.subquestions):
                yield f"open question {index}{chr(ord('a') + sub_index)}", sub


@dataclass(frozen=True)
class Finding:
    code: str
    severity: str  # "error" | "warning" | "info"
    location: str
    message: str

    def as_dict(self) -> dict[str, str]:
        return {
            "code": self.code,
            "severity": self.severity,
            "location": self.location,
            "message": self.message,
        }


# --- Input normalization ------------------------------------------------------


def to_statement(value: Any, location: str) -> Statement:
    """Normalize a string or ``{"text", "provenance", "source_label", "source_url"}``."""

    if isinstance(value, Statement):
        return value
    if isinstance(value, str):
        text = value.strip()
        if not text:
            raise ProposalInputError("proposal_statement_empty", location)
        return Statement(text=text, provenance=PROVENANCE_AI)
    if not isinstance(value, dict):
        raise ProposalInputError("proposal_statement_invalid", location)
    text = str(value.get("text") or "").strip()
    if not text:
        raise ProposalInputError("proposal_statement_empty", location)
    label = value.get("source_label") or value.get("from")
    url = value.get("source_url") or value.get("url")
    raw = value.get("provenance")
    if raw is None:
        provenance = PROVENANCE_CITED if (label or url) else PROVENANCE_AI
    else:
        provenance = _PROVENANCE_ALIASES.get(str(raw).strip().lower(), "")
        if not provenance:
            raise ProposalInputError("proposal_provenance_unknown", f"{location}: {raw!r}")
    return Statement(
        text=text,
        provenance=provenance,
        source_label=str(label).strip() if label else None,
        source_url=str(url).strip() if url else None,
    )


def _optional_statement(value: Any, location: str) -> Statement | None:
    if value is None or (isinstance(value, str) and not value.strip()):
        return None
    return to_statement(value, location)


def _statement_list(value: Any, location: str) -> list[Statement]:
    if value is None:
        return []
    items = value if isinstance(value, list) else [value]
    return [to_statement(item, f"{location}[{index}]") for index, item in enumerate(items, 1)]


def build_proposal(
    *,
    title: str,
    target_repo: str,
    target_release: str | None,
    contributor: str | None,
    ai_model: str | None,
    sdk_version: str,
    background: Any = None,
    scenario: Any = None,
    competency_questions: list[dict[str, Any]] | None = None,
    terms: list[dict[str, Any]] | None = None,
    open_questions: list[Any] | None = None,
    references: list[Any] | None = None,
    proposed_classes: list[dict[str, Any]] | None = None,
    proposed_properties: list[dict[str, Any]] | None = None,
    include_design_sketch: bool = False,
) -> Proposal:
    cqs: list[CompetencyQuestion] = []
    for index, raw in enumerate(competency_questions or [], 1):
        if not isinstance(raw, dict) or not raw.get("question"):
            raise ProposalInputError("proposal_cq_invalid", f"CQ {index}")
        cqs.append(
            CompetencyQuestion(
                question=to_statement(raw["question"], f"CQ {index} question"),
                expected_answer=_optional_statement(
                    raw.get("expected_answer"), f"CQ {index} expected answer"
                ),
                sparql=(str(raw["sparql"]).strip() or None) if raw.get("sparql") else None,
            )
        )
    term_list: list[Term] = []
    for index, raw in enumerate(terms or [], 1):
        if not isinstance(raw, dict) or not str(raw.get("name") or "").strip():
            raise ProposalInputError("proposal_term_invalid", f"Term {index}")
        term_list.append(
            Term(
                name=str(raw["name"]).strip(),
                vocabulary=(str(raw["vocabulary"]).strip() or None) if raw.get("vocabulary") else None,
                concept_url=(str(raw["concept_url"]).strip() or None) if raw.get("concept_url") else None,
                definition=_optional_statement(raw.get("definition"), f"Term {index} definition"),
                might_connect_to=_optional_statement(
                    raw.get("might_connect_to"), f"Term {index} might connect to"
                ),
            )
        )
    oqs: list[OpenQuestion] = []
    for index, raw in enumerate(open_questions or [], 1):
        if isinstance(raw, dict) and "question" in raw:
            oqs.append(
                OpenQuestion(
                    question=to_statement(raw["question"], f"open question {index}"),
                    subquestions=tuple(
                        _statement_list(raw.get("subquestions"), f"open question {index}")
                    ),
                )
            )
        else:
            oqs.append(OpenQuestion(question=to_statement(raw, f"open question {index}")))
    refs: list[Reference] = []
    for index, raw in enumerate(references or [], 1):
        if isinstance(raw, str):
            text = raw.strip()
            if not text:
                continue
            is_url = bool(_URL_RE.fullmatch(text))
            refs.append(Reference(label=text, url=text if is_url else None))
        elif isinstance(raw, dict) and (raw.get("label") or raw.get("url")):
            refs.append(
                Reference(
                    label=str(raw.get("label") or raw.get("url")).strip(),
                    url=(str(raw["url"]).strip() or None) if raw.get("url") else None,
                    note=(str(raw["note"]).strip() or None) if raw.get("note") else None,
                )
            )
        else:
            raise ProposalInputError("proposal_reference_invalid", f"reference {index}")
    return Proposal(
        title=title.strip(),
        target_repo=target_repo,
        target_release=target_release,
        contributor=(contributor or "").strip() or None,
        ai_model=(ai_model or "").strip() or None,
        sdk_version=sdk_version,
        background=_statement_list(background, "background"),
        scenario=_optional_statement(scenario, "scenario"),
        competency_questions=cqs,
        terms=term_list,
        open_questions=oqs,
        references=refs,
        proposed_classes=list(proposed_classes or []),
        proposed_properties=list(proposed_properties or []),
        include_design_sketch=include_design_sketch,
    )


# --- Rendering ----------------------------------------------------------------


def render_statement(stmt: Statement) -> str:
    if stmt.provenance == PROVENANCE_CONTRIBUTOR:
        return stmt.text
    if stmt.provenance == PROVENANCE_AI:
        return f"{stmt.text} *[AI-drafted]*"
    label = stmt.source_label or stmt.source_url or "source"
    if stmt.source_url:
        return f"{stmt.text} *[from [{label}]({stmt.source_url})]*"
    return f"{stmt.text} *[from {label}]*"


def release_line(proposal: Proposal) -> str:
    label = TRACKERS.get(proposal.target_repo, {}).get("release_label", "CASE/UCO")
    if proposal.target_release:
        return f"{label} {proposal.target_release}"
    return f"the next {label} release"


def contributor_line(proposal: Proposal) -> str:
    who = proposal.contributor or "_(contributor name and GitHub handle)_"
    model = proposal.ai_model or "an unspecified AI model"
    return (
        f"{who} with the assistance of the CASE/UCO SDK MCP/Agent "
        f"(v{proposal.sdk_version}) powered by {model}"
    )


def render_markdown(proposal: Proposal, design_sketch: str | None = None) -> str:
    out: list[str] = [
        f"<!-- Change proposal: {proposal.title} -->",
        f"<!-- Target repository: {proposal.target_repo} -->",
        "",
        f"**Suggested target release:** {release_line(proposal)}  ",
        f"**Contributor:** {contributor_line(proposal)}",
        "",
        DISCUSSION_DRAFT_NOTE,
        "",
        PROVENANCE_LEGEND,
        "",
        "# Background",
        "",
        " ".join(render_statement(s) for s in proposal.background)
        or "_(Why this is needed, in the contributor's words.)_",
        "",
        "# Competency questions",
        "",
    ]
    if proposal.scenario is not None:
        out += [f"**Scenario:** {render_statement(proposal.scenario)}", ""]
    if not proposal.competency_questions:
        out += ["_(Competency questions this change should let a graph answer.)_", ""]
    for index, cq in enumerate(proposal.competency_questions, 1):
        out += [f"## CQ {index}", "", f"- **Question:** {render_statement(cq.question)}"]
        answer = render_statement(cq.expected_answer) if cq.expected_answer else "_(expected answer)_"
        out += [f"- **Expected answer:** {answer}", ""]
    out += ["# Requirements", ""]
    if not proposal.terms:
        out += ["_(Terms the competency questions need, with sourced definitions.)_", ""]
    for index, term in enumerate(proposal.terms, 1):
        heading = f"## Term {index}: {term.name}"
        if term.vocabulary:
            heading += f" ({term.vocabulary})"
        out += [heading, ""]
        definition = render_statement(term.definition) if term.definition else "_(definition)_"
        out.append(f"- **Definition:** {definition}")
        if term.might_connect_to is not None:
            out.append(f"- **Might connect to:** {render_statement(term.might_connect_to)}")
        out.append("")
    out += ["# Open questions", ""]
    if not proposal.open_questions:
        out += ["_(What the contributor most wants input on.)_", ""]
    for index, oq in enumerate(proposal.open_questions, 1):
        out.append(f"{index}. {render_statement(oq.question)}")
        for sub_index, sub in enumerate(oq.subquestions):
            out.append(f"   - **{index}{chr(ord('a') + sub_index)}.** {render_statement(sub)}")
    out += ["", "# Related issues and references", ""]
    if not proposal.references:
        out += ["_(Related issues, prior discussion, and sources.)_"]
    for ref in proposal.references:
        line = f"- [{ref.label}]({ref.url})" if ref.url and ref.url != ref.label else f"- {ref.label}"
        if ref.note:
            line += f", {ref.note}"
        out.append(line)
    out += [
        "",
        "---",
        "",
        "<details>",
        "<summary><b>Committee section</b> (to be filled out during review)</summary>",
        "",
        "## Benefits and risks",
        "",
        COMMITTEE_PLACEHOLDER,
        "",
        "## Proposed ontology changes",
        "",
        design_sketch or COMMITTEE_PLACEHOLDER,
        "",
        "## Competency question queries and example data",
        "",
        COMMITTEE_PLACEHOLDER,
        "",
        "## Review checklist",
        "",
        *COMMITTEE_CHECKLIST,
        "",
        "</details>",
        "",
    ]
    return "\n".join(out)


# --- Ontology term references -------------------------------------------------


def reference_prefixes(base: dict[str, str], extra: dict[str, str] | None = None) -> dict[str, str]:
    """Prefixes whose namespaces are CASE, UCO, or CAC (the ones lint checks)."""

    prefixes = dict(_DOC_PREFIX_ALIASES)
    for source in (base, extra or {}):
        for prefix, iri in source.items():
            if isinstance(iri, str) and iri.startswith((UCO_BASE, CASE_BASE, CAC_BASE)):
                prefixes[prefix] = iri
    return prefixes


def _curie_re(prefixes: dict[str, str]) -> re.Pattern[str]:
    names = sorted((re.escape(p) for p in prefixes), key=len, reverse=True)
    return re.compile(
        r"(?<![\w/#:.-])(" + "|".join(names) + r"):([A-Za-z_][A-Za-z0-9_]*(?:[.-][A-Za-z0-9_]+)*)"
    )


def referenced_terms(texts: Iterable[str], prefixes: dict[str, str]) -> dict[str, str]:
    """``{IRI: as written}`` for CASE/UCO/CAC terms mentioned in ``texts``."""

    curie = _curie_re(prefixes)
    found: dict[str, str] = {}
    for text in texts:
        for match in curie.finditer(text):
            found.setdefault(prefixes[match.group(1)] + match.group(2), match.group(0))
        for match in _URL_RE.finditer(text):
            url = match.group(0).rstrip(".,;:")
            if not url.startswith((UCO_BASE, CASE_BASE, CAC_BASE)):
                continue
            local = re.split(r"[/#]", url)[-1]
            if local and local[0].isalpha() and "documentation" not in url:
                found.setdefault(url, url)
    return found


def expand(term: str, prefixes: dict[str, str], proposed_ns: str) -> str:
    prefix, sep, local = term.partition(":")
    if sep and not local.startswith("//"):
        if prefix in prefixes:
            return prefixes[prefix] + local
        if prefix == "proposed":
            return proposed_ns + local
        if prefix == "xsd":
            return XSD + local
        return term
    return proposed_ns + term


def proposed_iris(proposal: Proposal, prefixes: dict[str, str], proposed_ns: str) -> set[str]:
    names = [str(c.get("name") or "") for c in proposal.proposed_classes]
    for cls in proposal.proposed_classes:
        names += [str(p.get("name") or "") for p in cls.get("properties") or []]
    names += [str(p.get("name") or "") for p in proposal.proposed_properties]
    return {expand(n, prefixes, proposed_ns) for n in names if n}


# --- Lint ---------------------------------------------------------------------


def _github_person_citation(stmt: Statement) -> bool:
    return bool(stmt.source_label and "@" in stmt.source_label)


def lint_proposal(
    proposal: Proposal,
    *,
    declared: set[str] | frozenset[str],
    prefixes: dict[str, str],
    proposed_ns: str,
) -> list[Finding]:
    findings: list[Finding] = []

    def add(code: str, severity: str, location: str, message: str) -> None:
        findings.append(Finding(code, severity, location, message))

    if proposal.target_repo not in TRACKERS:
        add("target_repo_unresolved", "error", "header",
            "Set target_repo to UCO, CASE, or CAC before filing.")
    if not proposal.contributor:
        add("contributor_missing", "error", "header",
            "Name the contributor (name and GitHub handle); a person must own the proposal.")
    if not proposal.ai_model:
        add("ai_model_unspecified", "warning", "header",
            "Name the AI model in the contributor line so the AI disclosure is complete.")
    if not proposal.competency_questions:
        add("no_competency_questions", "error", "Competency questions",
            "Add at least one competency question; they are what the committee responds to.")
    for index, cq in enumerate(proposal.competency_questions, 1):
        if cq.expected_answer is None:
            add("cq_missing_expected_answer", "error", f"CQ {index}",
                "Give the answer the scenario should produce, so a query can be tested against it.")
    if proposal.competency_questions and proposal.scenario is None:
        add("scenario_missing", "warning", "Competency questions",
            "Add a concrete scenario so the expected answers can be checked.")
    if not proposal.open_questions:
        add("no_open_questions", "info", "Open questions",
            "Open questions are where reviewers' input is most wanted.")
    statements = list(proposal.statements())
    if statements and all(s.provenance != PROVENANCE_CONTRIBUTOR for _, s in statements):
        add("no_contributor_statements", "info", "proposal",
            "Every statement is AI-drafted or cited. Mark the statements the contributor "
            "wrote or approved as provenance='contributor'.")

    for index, term in enumerate(proposal.terms, 1):
        location = f"Term {index}"
        if term.vocabulary and not term.concept_url:
            add("vocabulary_claim_unlinked", "error", location,
                f"Link the {term.vocabulary} definition page for '{term.name}' (concept_url) "
                "so a reviewer can confirm it exists and says what the proposal claims.")
        if term.definition is not None and term.definition.provenance == PROVENANCE_AI and term.vocabulary:
            add("vocabulary_definition_ai_drafted", "warning", location,
                f"Quote the {term.vocabulary} definition and cite it instead of an AI paraphrase.")

    for location, stmt in statements:
        if stmt.provenance == PROVENANCE_CITED:
            if not stmt.source_url:
                add("citation_missing_url", "error", location,
                    "A *[from …]* tag must link the exact comment or page quoted.")
            elif (
                _github_person_citation(stmt)
                and urlsplit(stmt.source_url).hostname == "github.com"
                and "#issuecomment-" not in stmt.source_url
            ):
                add("citation_link_not_comment", "info", location,
                    "If this quotes a comment, link that comment (…#issuecomment-…). "
                    "The issue link is right only for the opening post.")
            continue
        text = stmt.text
        if _STANDARD_RE.search(text):
            add("avoid_standard_wording", "warning", location,
                "'Standard' implies a standards development organization. Say "
                "'vocabulary', 'specification', or 'publication' unless the source is an SDO.")
        for pattern in _EXCLUSIONARY_RES:
            if pattern.search(text):
                add("exclusionary_phrasing", "warning", location,
                    "Describe who drafted the proposal rather than who is in the community, "
                    "e.g. 'This proposal was not posted or drafted by a lawyer.'")
                break
        for pattern in _ENDORSEMENT_RES:
            if pattern.search(text):
                add("endorsement_wording", "warning", location,
                    "Avoid wording that ranks or endorses a source ('lead', 'endorse'); "
                    "ask how sources should be reconciled instead.")
                break
        lowered = text.casefold()
        if (
            any(vocab in lowered for vocab in EXTERNAL_VOCABULARIES)
            and _BACKTICK_RE.search(text)
            and not _URL_RE.search(text)
        ):
            add("vocabulary_term_unlinked", "warning", location,
                "This names a term from an outside vocabulary without a link. Link the "
                "term's definition so a reviewer can confirm it.")

    if _STANDARD_RE.search(proposal.title):
        add("avoid_standard_wording", "warning", "title",
            "'Standard' implies a standards development organization.")

    texts = [s.text for _, s in statements] + [t.name for t in proposal.terms]
    texts += [str(c.get("parent") or "") for c in proposal.proposed_classes]
    for cls in proposal.proposed_classes:
        texts += [str(p.get("type") or "") for p in cls.get("properties") or []]
    texts += [str(p.get("target_class") or "") for p in proposal.proposed_properties]
    texts += [str(p.get("type") or "") for p in proposal.proposed_properties]
    proposed = proposed_iris(proposal, prefixes, proposed_ns)
    for iri, written in sorted(referenced_terms(texts, prefixes).items()):
        if iri in declared or iri in proposed:
            continue
        add("ontology_term_not_found", "error", written,
            f"{written} is not declared in the pinned CASE/UCO (or CAC) ontology. Check the "
            "spelling, or list it under proposed_classes/proposed_properties if it is new.")

    for cls in proposal.proposed_classes:
        parent = str(cls.get("parent") or "uco-core:UcoObject")
        parent_iri = expand(parent, prefixes, proposed_ns)
        if parent_iri not in declared and parent_iri not in proposed:
            add("parent_class_undeclared", "error", f"proposed class {cls.get('name')}",
                f"Parent {parent} is not a declared CASE/UCO class or another proposed class.")
    return findings


# --- Human review -------------------------------------------------------------


def _excerpt(text: str, limit: int = 90) -> str:
    flat = " ".join(text.split())
    return flat if len(flat) <= limit else flat[: limit - 1] + "…"


def concept_links(proposal: Proposal) -> list[tuple[str, str, Statement | None]]:
    """``(location, url, statement it supports)`` for every outside link."""

    links: list[tuple[str, str, Statement | None]] = []
    seen: set[tuple[str, str]] = set()

    def add(location: str, url: str, stmt: Statement | None) -> None:
        key = (location, url)
        if key not in seen:
            seen.add(key)
            links.append((location, url, stmt))

    for index, term in enumerate(proposal.terms, 1):
        if term.concept_url:
            add(f"Term {index}", term.concept_url, term.definition)
    for location, stmt in proposal.statements():
        if stmt.source_url:
            add(location, stmt.source_url, stmt)
        for match in _URL_RE.finditer(stmt.text):
            add(location, match.group(0).rstrip(".,;:"), stmt)
    return links


def review_checklist(proposal: Proposal, findings: list[Finding]) -> list[str]:
    items: list[str] = []
    for location, url, stmt in concept_links(proposal):
        claim = f': "{_excerpt(stmt.text)}"' if stmt is not None else ""
        items.append(f"[ ] {location}: opened {url}; it resolves and supports the text{claim}")
    for location, stmt in proposal.statements():
        if stmt.provenance == PROVENANCE_CITED:
            items.append(
                f"[ ] {location}: the *[from {stmt.source_label or stmt.source_url}]* tag "
                "links the exact comment or page quoted, and the quote is accurate"
            )
    ai_count = sum(1 for _, s in proposal.statements() if s.provenance == PROVENANCE_AI)
    if ai_count:
        items.append(
            f"[ ] Read all {ai_count} *[AI-drafted]* statement(s). Keep, rewrite (then mark as "
            "the contributor's), or delete each one"
        )
    missing = [f for f in findings if f.code == "ontology_term_not_found"]
    items.append(
        "[ ] Every CASE/UCO/CAC term named exists in the target release"
        + (f" ({len(missing)} not found by lint)" if missing else " (lint found none missing)")
    )
    items += [
        "[ ] No single jurisdiction, legal system, or locale is treated as the default",
        "[ ] Things that should be objects (statutes, people, organizations, roles) are not stood in for by strings",
        "[ ] Roles are kept distinct from the people or organizations that hold them",
        "[ ] Sources are not circular: no AI-drafted statement is cited as support for itself",
        "[ ] Existing vocabularies were considered before new terms (for example SOSA/SSN, PROV-O, schema.org)",
        "[ ] check_existing_proposals was run, and related or duplicate issues are linked",
    ]
    return items


def _normalize_for_match(text: str) -> str:
    text = html.unescape(re.sub(r"<[^>]+>", " ", text))
    text = text.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    return " ".join(text.split()).casefold()


def _quoted(stmt: Statement) -> str | None:
    match = re.search(r"[\"\u201c]([^\"\u201d]{12,})[\"\u201d]", stmt.text)
    return match.group(1) if match else None


def verify_links(
    proposal: Proposal,
    fetch: Callable[[str], tuple[int | None, str]],
) -> list[dict[str, Any]]:
    """Fetch each outside link; report status and whether a quoted definition appears.

    A link check never replaces the human checklist: a page can resolve and
    still not say what the statement claims.
    """

    results: list[dict[str, Any]] = []
    cache: dict[str, tuple[int | None, str]] = {}
    for location, url, stmt in concept_links(proposal):
        if not url.startswith(("http://", "https://")):
            continue
        if url not in cache:
            cache[url] = fetch(url)
        status, body = cache[url]
        quote = _quoted(stmt) if stmt is not None else None
        quote_found: bool | None = None
        if quote and status is not None and 200 <= status < 300:
            page = _normalize_for_match(body)
            wanted = _normalize_for_match(quote)
            quote_found = wanted in page or wanted[:60] in page
        results.append(
            {
                "location": location,
                "url": url,
                "status": status,
                "resolves": status is not None and 200 <= status < 400,
                "quote_found": quote_found,
            }
        )
    return results


def render_review(
    proposal: Proposal,
    *,
    findings: list[Finding],
    checklist: list[str],
    link_checks: list[dict[str, Any]] | None,
    companion_files: list[str],
    test_results: dict[str, Any] | None,
    slug: str,
) -> str:
    tracker = TRACKERS.get(proposal.target_repo, {}).get("new_issue_url", "the target tracker")
    out = [
        f"# Review notes: {proposal.title}",
        "",
        f"_Working notes for the contributor. Not part of the issue. Work through them "
        f"before filing at {tracker}._",
        "",
        "## Lint findings",
        "",
    ]
    if findings:
        for f in findings:
            out.append(f"- **{f.severity}** `{f.code}` ({f.location}): {f.message}")
    else:
        out.append("None.")
    out += ["", "## Confirm by hand", ""]
    out += [f"- {item}" for item in checklist]
    if link_checks is not None:
        out += ["", "## Link checks", ""]
        if not link_checks:
            out.append("No outside links to check.")
        for check in link_checks:
            quote = {True: "quote found", False: "QUOTE NOT FOUND", None: "no quote to match"}[
                check["quote_found"]
            ]
            out.append(
                f"- {check['location']}: {check['url']}, HTTP {check['status'] or 'unreachable'}, {quote}"
            )
        out.append("")
        out.append("_A link that resolves can still say something different; the hand checks stand._")
    out += ["", "## Companion files", ""]
    if companion_files:
        out += [f"- `{path}`" for path in companion_files]
        out += [
            "",
            (
                "These are a local sketch for testing, not part of the issue. Offer them in the "
                "discussion if the committee asks for a design."
            ),
            "",
            f"Re-run with `make test-proposal PROPOSAL={slug}`.",
        ]
    else:
        out.append("None (no proposed classes or properties were given).")
    if test_results:
        out += ["", "## Test results", ""]
        validation = test_results.get("validation")
        if validation:
            out.append(
                f"- `case_validate`: conforms={validation.get('conforms')}, "
                f"violations={validation.get('violation_count')}, "
                f"warnings={validation.get('warning_count')}"
            )
            if validation.get("summary"):
                out.append(f"  - {validation['summary']}")
        for query in test_results.get("sparql") or []:
            out.append(
                f"- SPARQL {query['label']}: {query['status']} ({query['result_count']} result(s))"
            )
    out.append("")
    return "\n".join(out)


# --- Companion artifacts (#31) ------------------------------------------------


def _local(term: str) -> str:
    return re.split(r"[/#:]", term.strip("<>"))[-1] or "Node"


def _ttl_literal(text: str) -> str:
    escaped = text.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\r", "")
    return f'"{escaped}"@en'


def _is_xsd(type_name: str) -> bool:
    return type_name.startswith(("xsd:", XSD))


def _example_literal(type_name: str, name: str) -> Any:
    local = type_name.split(":", 1)[-1] if type_name.startswith("xsd:") else type_name[len(XSD):]
    samples = {
        "decimal": "1.0",
        "double": "1.0",
        "float": "1.0",
        "integer": "1",
        "int": "1",
        "long": "1",
        "nonNegativeInteger": "1",
        "positiveInteger": "1",
        "boolean": "true",
        "dateTime": "2024-01-01T00:00:00Z",
        "date": "2024-01-01",
        "hexBinary": "00",
        "base64Binary": "AA==",
        "anyURI": "http://example.org/",
    }
    if local == "string":
        return f"example {name}"
    return {"@type": f"xsd:{local}", "@value": samples.get(local, f"example {name}")}


@dataclass
class Companions:
    ttl: str
    shapes: str
    jsonld: dict[str, Any]
    sparql: str | None


def build_companions(
    proposal: Proposal,
    *,
    slug: str,
    base_context: dict[str, str],
    superclasses: dict[str, frozenset[str]],
    extra_prefixes: dict[str, str] | None = None,
) -> Companions | None:
    """OWL, SHACL, example graph, and SPARQL for the contributor's draft terms.

    Facet subclasses attach to an ``ObservableObject`` through
    ``uco-core:hasFacet``; every other class is a top-level node. Every node
    has an ``@id``, and object-range properties point at a typed node.
    """

    if not proposal.proposed_classes and not proposal.proposed_properties:
        return None
    proposed_ns = f"http://example.org/ontology/proposed/{slug}/"
    known = {k: v for k, v in base_context.items() if isinstance(v, str)}
    known.update(extra_prefixes or {})
    prefixes = dict(known)
    prefixes.update(reference_prefixes(known))
    used: set[str] = set()

    def curie(term: str) -> str:
        iri = expand(term, prefixes, proposed_ns)
        if iri.startswith(proposed_ns):
            return "proposed:" + iri[len(proposed_ns):]
        if iri.startswith(XSD):
            return "xsd:" + iri[len(XSD):]
        for prefix, ns in sorted(prefixes.items(), key=lambda kv: -len(kv[1])):
            if prefix not in known:
                continue
            if iri.startswith(ns):
                used.add(prefix)
                return f"{prefix}:{iri[len(ns):]}"
        return f"<{iri}>"

    class_parent: dict[str, str] = {}
    for cls in proposal.proposed_classes:
        class_parent[curie(str(cls.get("name") or "ProposedClass"))] = curie(
            str(cls.get("parent") or "uco-core:UcoObject")
        )

    def is_facet(class_curie: str, depth: int = 0) -> bool:
        if depth > 8:
            return False
        if class_curie in class_parent:
            return is_facet(class_parent[class_curie], depth + 1)
        iri = expand(class_curie, prefixes, proposed_ns)
        return iri == FACET_IRI or FACET_IRI in superclasses.get(iri, frozenset())

    def node_id(kind: str, *parts: str) -> str:
        return f"kb:{kind}-{uuid.uuid5(uuid.NAMESPACE_URL, '/'.join((slug, kind, *parts)))}"

    ttl = [
        "@prefix owl: <http://www.w3.org/2002/07/owl#> .",
        "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .",
        f"@prefix xsd: <{XSD}> .",
        f"@prefix proposed: <{proposed_ns}> .",
        "{prefixes}",
        "",
        f"<{proposed_ns}> a owl:Ontology ;",
        f"    rdfs:label {_ttl_literal('Draft terms: ' + proposal.title)} ;",
        "    rdfs:comment "
        + _ttl_literal(
            f"Local draft for testing the '{proposal.title}' change proposal. Not part "
            "of any CASE, UCO, or CAC release."
        )
        + " .",
        "",
    ]
    shapes = [
        "@prefix sh: <http://www.w3.org/ns/shacl#> .",
        f"@prefix xsd: <{XSD}> .",
        f"@prefix proposed: <{proposed_ns}> .",
        "{prefixes}",
        "",
    ]
    graph: list[dict[str, Any]] = []
    queries: list[str] = []
    declared_props: set[str] = set()

    def declare_property(prop: dict[str, Any]) -> tuple[str, str]:
        name = curie(str(prop.get("name") or "proposedProperty"))
        type_name = str(prop.get("type") or "xsd:string")
        range_curie = curie(type_name)
        if name.startswith("proposed:") and name not in declared_props:
            declared_props.add(name)
            kind = "owl:DatatypeProperty" if _is_xsd(type_name) else "owl:ObjectProperty"
            comment = str(prop.get("description") or f"Proposed in '{proposal.title}'.")
            ttl.extend(
                [
                    f"{name} a {kind} ;",
                    f"    rdfs:label {_ttl_literal(name.split(':', 1)[1])} ;",
                    f"    rdfs:comment {_ttl_literal(comment)} ;",
                    f"    rdfs:range {range_curie} .",
                    "",
                ]
            )
        return name, range_curie

    def property_shape(owner: str, props: list[dict[str, Any]], shape_name: str) -> None:
        if not props:
            return
        lines = [f"{shape_name} a sh:NodeShape ;", f"    sh:targetClass {owner} ;"]
        parts = []
        for prop in props:
            name, range_curie = declare_property(prop)
            constraint = (
                f"sh:datatype {range_curie}"
                if _is_xsd(str(prop.get("type") or "xsd:string"))
                else f"sh:class {range_curie}"
            )
            parts.append(f"    sh:property [ sh:path {name} ; {constraint} ]")
        lines.append(" ;\n".join(parts) + " .")
        shapes.extend(lines + [""])

    def example_node(type_curie: str, props: list[dict[str, Any]], key: str) -> str:
        nid = node_id(_local(type_curie), key)
        node: dict[str, Any] = {"@id": nid, "@type": type_curie}
        for prop in props:
            name, range_curie = declare_property(prop)
            type_name = str(prop.get("type") or "xsd:string")
            if _is_xsd(type_name):
                node[name] = _example_literal(type_name, name.split(":", 1)[1])
            else:
                target = node_id(_local(range_curie), key, name)
                node[name] = {"@id": target}
                graph.append({"@id": target, "@type": range_curie})
        if is_facet(type_curie):
            graph.append(
                {
                    "@id": node_id("ObservableObject", key),
                    "@type": "uco-observable:ObservableObject",
                    "uco-core:hasFacet": [{"@id": nid}],
                }
            )
            used.update({"uco-observable", "uco-core"})
        graph.append(node)
        return nid

    def select_query(type_curie: str, props: list[dict[str, Any]], label: str) -> None:
        names = [curie(str(p.get("name") or "")) for p in props[:4] if p.get("name")]
        variables = [f"?{n.split(':', 1)[1]}" for n in names]
        if is_facet(type_curie):
            pattern = [
                "    ?observable a uco-observable:ObservableObject ;",
                "        uco-core:hasFacet ?node .",
                f"    ?node a {type_curie} .",
            ]
        else:
            pattern = [f"    ?node a {type_curie} ."]
        pattern += [f"    ?node {n} {v} ." for n, v in zip(names, variables)]
        queries.append(
            "\n".join(
                [f"# {label}", "{prefixes}", "", f"SELECT ?node {' '.join(variables)}", "WHERE {"]
                + pattern
                + ["}"]
            )
        )

    for index, cls in enumerate(proposal.proposed_classes, 1):
        name = curie(str(cls.get("name") or "ProposedClass"))
        parent = class_parent[name]
        description = str(cls.get("description") or f"Proposed in '{proposal.title}'.")
        ttl_lines = [
            f"{name} a owl:Class ;",
            f"    rdfs:subClassOf {parent} ;",
            f"    rdfs:label {_ttl_literal(name.split(':', 1)[1])} ;",
            f"    rdfs:comment {_ttl_literal(description)}",
        ]
        if cls.get("source_url"):
            ttl_lines[-1] += " ;"
            ttl_lines.append(f"    rdfs:seeAlso <{cls['source_url']}>")
        ttl.extend(ttl_lines[:-1] + [ttl_lines[-1] + " .", ""])
        props = list(cls.get("properties") or [])
        property_shape(name, props, f"proposed:{name.split(':', 1)[1]}-shape")
        example_node(name, props, f"class{index}")
        select_query(name, props, f"Instances of {name} and their proposed properties")

    by_target: dict[str, list[dict[str, Any]]] = {}
    for prop in proposal.proposed_properties:
        target = curie(str(prop.get("target_class") or "uco-core:UcoObject"))
        by_target.setdefault(target, []).append(prop)
    for index, (target, props) in enumerate(by_target.items(), 1):
        property_shape(target, props, f"proposed:{_local(target)}-proposed-properties-shape")
        example_node(target, props, f"target{index}")
        select_query(target, props, f"{target} nodes carrying the proposed properties")

    if any(cq.sparql for cq in proposal.competency_questions):
        queries = [
            f"# CQ {index}: {' '.join(cq.question.text.split())}\n{cq.sparql}"
            for index, cq in enumerate(proposal.competency_questions, 1)
            if cq.sparql
        ]

    def prefix_block(syntax: str) -> str:
        lines = []
        for prefix in sorted(used):
            ns = prefixes[prefix]
            lines.append(
                f"@prefix {prefix}: <{ns}> ." if syntax == "turtle" else f"PREFIX {prefix}: <{ns}>"
            )
        return "\n".join(lines)

    turtle_prefixes = prefix_block("turtle")
    sparql_prefixes = "\n".join(
        [prefix_block("sparql"), f"PREFIX proposed: <{proposed_ns}>", f"PREFIX xsd: <{XSD}>"]
    ).strip()
    context: dict[str, str] = {
        "kb": "http://example.org/kb/",
        "proposed": proposed_ns,
        "xsd": XSD,
    }
    for prefix in sorted(used):
        context[prefix] = prefixes[prefix]
    return Companions(
        ttl="\n".join(ttl).replace("{prefixes}", turtle_prefixes),
        shapes="\n".join(shapes).replace("{prefixes}", turtle_prefixes),
        jsonld={"@context": context, "@graph": graph},
        sparql=(
            "\n# ---\n".join(q.replace("{prefixes}", sparql_prefixes) for q in queries) + "\n"
            if queries
            else None
        ),
    )


def design_sketch(proposal: Proposal) -> str | None:
    """Contributor's draft terms for the committee section, when requested."""

    if not proposal.include_design_sketch:
        return None
    if not proposal.proposed_classes and not proposal.proposed_properties:
        return None
    lines = [
        (
            "A sketch offered for the committee to accept, revise, or discard. "
            "Local test files are available on request. *[AI-drafted]*"
        ),
        "",
    ]
    for cls in proposal.proposed_classes:
        lines.append(
            f"- Class `{cls.get('name')}`, a subclass of `{cls.get('parent') or 'uco-core:UcoObject'}`"
        )
        for prop in cls.get("properties") or []:
            lines.append(f"  - `{prop.get('name')}` ({prop.get('type') or 'xsd:string'})")
    for prop in proposal.proposed_properties:
        lines.append(
            f"- Property `{prop.get('name')}` ({prop.get('type') or 'xsd:string'}) "
            f"on `{prop.get('target_class') or 'uco-core:UcoObject'}`"
        )
    return "\n".join(lines)
