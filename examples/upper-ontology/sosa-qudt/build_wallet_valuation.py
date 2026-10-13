#!/usr/bin/env python3
"""QUDT-only exemplar for docs/recipes/qudt-quantities-and-units.md.

A wallet's balance and its fiat valuation are quantities, not sensor
observations (ucoProject/UCO#404): the balance is read from the wallet and the
valuation is a lookup against a published exchange rate at a stated time. Both
are modeled as ``qudt:Quantity`` nodes with a ``qudt:QuantityValue``; the
lookup is an InvestigativeAction so the rate source and time are recorded.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from case_uco import CASEGraph
from case_uco.case.investigation import Investigation, InvestigativeAction
from case_uco.uco.observable import FileFacet, ObservableObject, URLFacet
from case_uco.uco.tool import Tool

HERE = Path(__file__).resolve().parent
OUTPUT = HERE / "wallet-valuation.jsonld"

EXTRA_CONTEXT = {
    "qudt": "http://qudt.org/schema/qudt/",
    "unit": "http://qudt.org/vocab/unit/",
    "quantitykind": "http://qudt.org/vocab/quantitykind/",
    "prov": "http://www.w3.org/ns/prov#",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
}


def _quantity(graph: CASEGraph, node_id: str, value: str, unit: str, label: str) -> str:
    value_id = f"{node_id}-value"
    graph.upsert_node(value_id, types=["qudt:QuantityValue"], properties={
        "qudt:value": {"@type": "xsd:decimal", "@value": value},
        "qudt:hasUnit": {"@id": unit},
    })
    graph.upsert_node(node_id, types=["qudt:Quantity"], properties={
        "rdfs:label": label,
        "qudt:hasQuantityKind": {"@id": "quantitykind:Currency"},
        "qudt:quantityValue": {"@id": value_id},
    })
    return node_id


def build() -> CASEGraph:
    graph = CASEGraph(extra_context=EXTRA_CONTEXT)
    tz = timezone.utc

    wallet_id = "kb:wallet-1"
    wallet = graph.create(ObservableObject, id=wallet_id, name="Recovered desktop wallet file",
                          has_facet=[FileFacet(file_name="wallet.dat", size_in_bytes=1048576)])
    rate_source_id = "kb:rate-source-1"
    rate_source = graph.create(ObservableObject, id=rate_source_id, name="Published BTC/USD reference rate",
                               has_facet=[URLFacet(full_value="https://rates.example.org/btc-usd")])

    balance_id = _quantity(graph, "kb:wallet-balance-1", "0.41250000", "unit:CCY_BTC",
                           "Wallet balance read from the wallet file")
    graph.link(balance_id, "prov:wasDerivedFrom", wallet_id)

    lookup_id = "kb:valuation-action-1"
    graph.create(
        InvestigativeAction,
        id=lookup_id,
        name="Value wallet balance in USD",
        description=["Balance multiplied by the reference rate published for the stated time."],
        start_time=datetime(2024, 8, 14, 16, 0, tzinfo=tz),
        end_time=datetime(2024, 8, 14, 16, 0, tzinfo=tz),
        instrument=[graph.create(Tool, name="Example valuation script", version="0.3")],
        object=[wallet, rate_source],
    )

    valuation_id = _quantity(graph, "kb:wallet-valuation-1", "24537.83", "unit:CCY_USD",
                             "Wallet balance valued in USD at 2024-08-14T16:00:00Z")
    graph.link(valuation_id, "prov:wasGeneratedBy", lookup_id)
    graph.link(valuation_id, "prov:wasDerivedFrom", balance_id)
    graph.link(valuation_id, "prov:wasDerivedFrom", rate_source_id)

    graph.create(
        Investigation,
        name="Synthetic case 2024-FIN-031",
        description=["Valuation of a cryptocurrency wallet recovered from a seized laptop."],
        object=[wallet],
    )
    return graph


def main() -> None:
    graph = build()
    graph.write(str(OUTPUT))
    print(f"wrote {OUTPUT} ({len(graph)} nodes)")


if __name__ == "__main__":
    main()
