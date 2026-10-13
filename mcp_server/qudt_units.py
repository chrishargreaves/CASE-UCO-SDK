"""Look up QUDT unit IRIs by symbol, label, UCUM code, or quantity kind.

Agents tend to guess unit IRIs (``unit:KM-PER-HR``) or reach for the QUDT 2
pattern (``qudt:unit`` / ``qudt:numericValue``). This module answers from
``qudt_unit_index.json``, generated from the pinned QUDT units vocabulary by
``tools/build_upper_ontology_registry.py``, so every returned IRI is one that
strict concept coverage accepts under the ``qudt`` profile.
"""

from __future__ import annotations

import json
import threading
from pathlib import Path
from typing import Any

INDEX_PATH = Path(__file__).resolve().parent / "qudt_unit_index.json"

_INDEX: dict[str, Any] | None = None
_LOCK = threading.Lock()

USAGE = (
    "Attach a value as a qudt:QuantityValue node with exactly one qudt:value "
    "(xsd:decimal or another numeric type) and exactly one qudt:hasUnit. QUDT 3 "
    "has no qudt:unit property; qudt:numericValue is legacy. Validate with "
    "profiles=['qudt']."
)


def load_index() -> dict[str, Any]:
    global _INDEX
    with _LOCK:
        if _INDEX is None:
            _INDEX = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
        return _INDEX


def _normalize_kind(kind: str) -> str:
    kind = kind.strip()
    if not kind:
        return ""
    if kind.startswith("http://qudt.org/vocab/quantitykind/"):
        return "quantitykind:" + kind.rsplit("/", 1)[1]
    if not kind.startswith("quantitykind:"):
        kind = "quantitykind:" + kind
    return kind


_IRREGULAR_PLURALS = {"feet": "foot", "inches": "inch", "degrees": "degree"}


def _singular(query: str) -> str:
    words = []
    for word in query.lower().split():
        if word in _IRREGULAR_PLURALS:
            word = _IRREGULAR_PLURALS[word]
        elif len(word) > 3 and word.endswith("s") and not word.endswith("ss"):
            word = word[:-1]
        words.append(word)
    return " ".join(words)


_SPELLINGS = (("meter", "metre"), ("liter", "litre"))
_SYMBOL_JOINERS = str.maketrans("", "", "·⋅.* ")


def _spelling(text: str) -> str:
    for us, gb in _SPELLINGS:
        text = text.replace(us, gb)
    return text


def _score(unit: dict[str, Any], query: str) -> int:
    local = unit["id"].split(":", 1)[1]
    symbols = [s for s in [unit.get("symbol"), *unit.get("alt_symbols", []), *unit.get("ucum", [])] if s]
    labels = [_spelling(label.lower()) for label in unit.get("labels", [])]
    q = query.strip()
    ql = _spelling(q.lower())
    if q in (unit["id"], local) or q in symbols:
        return 100
    if len(q) > 1 and q.translate(_SYMBOL_JOINERS) in {s.translate(_SYMBOL_JOINERS) for s in symbols}:
        return 96
    if local.startswith("CCY_") and ql == local[4:].lower():
        return 95  # ISO 4217 currency code, carried only in the IRI
    if ql in {s.lower() for s in symbols} or ql == local.lower():
        return 90
    if ql in {label.lower() for label in labels}:
        return 85
    words = ql.replace("/", " per ").split()
    if len(ql) >= 3 and words and any(all(w in label for w in words) for label in labels):
        return 50
    if len(ql) >= 3 and any(ql in s.lower() for s in symbols):
        return 30
    return 0


def lookup_units(query: str = "", quantity_kind: str = "", limit: int = 10) -> dict[str, Any]:
    """Return QUDT units matching ``query`` and/or ``quantity_kind``."""

    index = load_index()
    kind = _normalize_kind(quantity_kind)
    limit = max(1, min(int(limit or 10), 50))
    candidates = index["units"]
    if kind:
        candidates = [u for u in candidates if kind in u.get("quantity_kinds", [])]

    if query.strip():
        singular = _singular(query)
        scored = [
            (s, u)
            for u in candidates
            if (s := max(_score(u, query), _score(u, singular) if singular != query else 0)) > 0
        ]
    else:
        scored = [(1, u) for u in candidates] if kind else []
    # Prefer current units over deprecated ones, then shorter ids.
    scored.sort(key=lambda item: (-item[0], bool(item[1].get("deprecated")), len(item[1]["id"]), item[1]["id"]))

    unit_prefix = index["prefixes"]["unit"]
    results = []
    for score, unit in scored[:limit]:
        kinds = unit.get("quantity_kinds", [])
        results.append(
            {
                "id": unit["id"],
                "iri": unit_prefix + unit["id"].split(":", 1)[1],
                "label": (unit.get("labels") or [None])[0],
                "symbol": unit.get("symbol"),
                "ucum": unit.get("ucum", []),
                "quantity_kinds": kinds[:8],
                "quantity_kind_count": len(kinds),
                "conversion_multiplier": unit.get("conversion_multiplier"),
                "deprecated": bool(unit.get("deprecated")),
                "match_score": score,
            }
        )

    out: dict[str, Any] = {
        "query": query,
        "quantity_kind": kind or None,
        "qudt_version": index["qudt_version"],
        "total_matches": len(scored),
        "units": results,
        "usage": USAGE,
    }
    if not results:
        out["hint"] = (
            "No pinned QUDT unit matched. Try the unit symbol (km/h), the UCUM "
            "code (km.h-1), or an English label (kilometre per hour), or pass "
            "quantity_kind (e.g. Velocity) to list every unit for a kind. Do "
            "not invent a unit IRI; strict coverage rejects it."
        )
    return out
