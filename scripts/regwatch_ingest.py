"""regwatch live ingestion from the Federal Register API.

Pulls recent FDA food documents from the Federal Register, filters to the ones
relevant to beverages, and turns each into a candidate change-log event with a
date, the document type, a source backlink, and the CFR references the API
itself reports. Candidates are written to the state directory flagged
unconfirmed: the loop self-populates what happened, and a human confirms before
anything is promoted into the curated change log. Standard library only.

The Federal Register API is documented at https://www.federalregister.gov/developers/api/v1
and returns cfr_references per document, so CFR tagging is sourced, not guessed.
"""

from __future__ import annotations

import datetime as dt
import json

API_BASE = "https://www.federalregister.gov/api/v1/documents.json"

# CFR parts (title 21) that bear on food and beverages.
RELEVANT_PARTS = {
    70, 71, 73, 74, 80, 81, 82, 101, 102, 113, 114, 117, 120,
    129, 165, 170, 172, 173, 180, 182, 184, 189,
}

RELEVANT_TERMS = [
    "beverage", "drink", "soda", "soft drink", "juice", "bottled water", "sparkling",
    "color additive", "dye", "sweetener", "sugar", "caffeine", "gras", "food additive",
    "labeling", "front-of-package", "front of package", "nutrition", "healthy",
    "ultra-processed", "ultraprocessed", "additive", "preservative", "brominated",
]


def build_query_url(since: str, per_page: int = 100) -> str:
    """Federal Register API URL for recent FDA rules, proposed rules, and notices."""
    fields = [
        "title", "abstract", "publication_date", "html_url",
        "document_number", "type", "cfr_references", "agencies",
    ]
    parts = [
        f"{API_BASE}?per_page={per_page}",
        "order=newest",
        "conditions[type][]=RULE",
        "conditions[type][]=PRORULE",
        "conditions[type][]=NOTICE",
        "conditions[agencies][]=food-and-drug-administration",
        f"conditions[publication_date][gte]={since}",
    ]
    parts += [f"fields[]={field}" for field in fields]
    return "&".join(parts)


def _cfr_list(doc: dict) -> list[dict]:
    out: list[dict] = []
    seen: set[str] = set()
    for ref in doc.get("cfr_references") or []:
        title = ref.get("title")
        part = ref.get("part")
        if title is None or part is None:
            continue
        citation = f"{title} CFR {part}"
        if citation in seen:
            continue
        seen.add(citation)
        out.append({"citation": citation, "url": f"https://www.ecfr.gov/current/title-{title}/part-{part}"})
    return out


def _is_relevant(doc: dict) -> bool:
    for ref in doc.get("cfr_references") or []:
        if ref.get("title") == 21 and ref.get("part") in RELEVANT_PARTS:
            return True
    haystack = f"{doc.get('title', '')} {doc.get('abstract', '')}".lower()
    return any(term in haystack for term in RELEVANT_TERMS)


def _truncate(text: str, limit: int = 320) -> str:
    text = " ".join((text or "").split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def parse_candidates(json_text: str, today: dt.date) -> list[dict]:
    """Turn an API response into candidate change-log events, beverage-filtered."""
    data = json.loads(json_text)
    candidates: list[dict] = []
    for doc in data.get("results", []):
        if not _is_relevant(doc):
            continue
        doc_type = doc.get("type", "Document")
        title = _truncate(doc.get("title", ""), 200)
        candidates.append(
            {
                "date": doc.get("publication_date", ""),
                "country": "US",
                "agency": "FDA",
                "obligation_id": None,
                "headline": f"{doc_type}: {title}",
                "what_happened": _truncate(doc.get("abstract") or doc.get("title", "")),
                "cfr": _cfr_list(doc),
                "source_url": doc.get("html_url", ""),
                "document_number": doc.get("document_number", ""),
                "type": doc_type,
                "needs_review": True,
                "confidence": "unconfirmed",
                "detected": today.isoformat(),
            }
        )
    candidates.sort(key=lambda c: c["date"], reverse=True)
    return candidates


def candidates_document(candidates: list[dict], today: dt.date, origin: str) -> dict:
    return {
        "version": "0.1.0",
        "generated": today.isoformat(),
        "source": "Federal Register API",
        "origin": origin,
        "note": "Unconfirmed candidates from the live feed. A human confirms and promotes into regwatch-changelog.json before any compliance use.",
        "candidates": candidates,
    }
