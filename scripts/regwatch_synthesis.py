"""regwatch synthesis.

Content abstraction and synthesis: turn raw register rows, scan deltas, and
impact scores into a single document model the renderers can emit in any format.
Two cadences are produced. The daily brief is short and change-driven; the
weekly synthesis is a full portfolio analysis with the beverage lens and a
recommended-action list.

All functions are pure and return the document model documented in
regwatch_render.
"""

from __future__ import annotations

import datetime as dt

DISCLAIMER = (
    "Draft for analyst review and internal research only. Detection and analysis flag; a human "
    "confirms against primary source text and current product specifications before any compliance "
    "or marketing use. Not legal advice."
)


def _upcoming(obligations: list[dict], days: int, today: dt.date) -> list[dict]:
    horizon = today + dt.timedelta(days=days)
    kept = []
    for ob in obligations:
        date = ob.get("effective_date", "")
        try:
            parsed = dt.date.fromisoformat(date) if date else None
        except ValueError:
            parsed = None
        if parsed and today <= parsed <= horizon:
            kept.append(ob)
    return sorted(kept, key=lambda r: r["effective_date"])


def _severity_counts(impacts: list[dict]) -> dict[str, int]:
    counts = {"act-now": 0, "high": 0, "watch": 0, "info": 0}
    for impact in impacts:
        counts[impact["severity"]] += 1
    return counts


def daily_brief(company: str, scan_results: list[dict], obligations: list[dict], impacts: list[dict], today: dt.date) -> dict:
    sections: list[dict] = []

    changed = [r for r in scan_results if r["status"] in ("NEW", "CHANGED")]
    change_section = {"heading": "What Changed", "level": 2, "paragraphs": [], "bullets": []}
    if changed:
        change_section["paragraphs"].append(
            f"{len(changed)} upstream source(s) changed since the last accepted baseline and need a look."
        )
        change_section["bullets"] = [f"{r['status']}: {r['source_id']}" for r in changed]
    else:
        change_section["paragraphs"].append("No upstream source changes since the last accepted baseline.")
    sections.append(change_section)

    soon = _upcoming(obligations, 30, today)
    sections.append(
        {
            "heading": "Effective Within 30 Days",
            "level": 2,
            "paragraphs": [] if soon else ["Nothing reaches an effective date in the next 30 days."],
            "bullets": [f"{r['effective_date']} — {r['jurisdiction']}: {r['title']}" for r in soon],
        }
    )

    priority = [i for i in impacts if i["severity"] in ("act-now", "high")][:6]
    sections.append(
        {
            "heading": "Priority Actions",
            "level": 2,
            "paragraphs": [] if priority else ["No act-now or high-severity impacts on the portfolio today."],
            "bullets": [
                f"{i['product_name']}: {i['obligation_title']} ({i['jurisdiction']}, {i['severity']})"
                for i in priority
            ],
        }
    )

    return {
        "title": f"{company} regulatory daily brief",
        "subtitle": "Change detection and near-term obligations",
        "generated": today.isoformat(),
        "sections": sections,
        "disclaimer": DISCLAIMER,
    }


def weekly_synthesis(
    company: str,
    obligations: list[dict],
    impacts: list[dict],
    findings: list[dict],
    products: list[dict],
    jurisdiction_count: int,
    confirmed_count: int,
    today: dt.date,
) -> dict:
    counts = _severity_counts(impacts)
    impacted_products = sorted({i["product_id"] for i in impacts})
    soonest = _upcoming(obligations, 365, today)

    sections: list[dict] = []

    summary = [
        f"{company} carries {len(products)} modeled products. The register tracks {len(obligations)} "
        f"obligations across {jurisdiction_count} jurisdictions, {confirmed_count} of them with confirmed rows. "
        "This synthesis maps every tracked obligation onto the portfolio.",
        f"{len(impacts)} product-obligation impacts were identified: {counts['act-now']} act-now, "
        f"{counts['high']} high, {counts['watch']} watch, and {counts['info']} informational. "
        f"{len(impacted_products)} of {len(products)} products carry at least one impact.",
    ]
    if soonest:
        first = soonest[0]
        summary.append(
            f"{len(soonest)} obligations reach an effective date within a year; the soonest is "
            f"{first['title']} ({first['jurisdiction']}) on {first['effective_date']}."
        )
    sections.append({"heading": "Executive Summary", "level": 2, "paragraphs": summary, "bullets": []})

    sections.append(
        {
            "heading": "Coming Due Within 365 Days",
            "level": 2,
            "paragraphs": [] if soonest else ["No obligations reach an effective date within a year."],
            "bullets": [f"{r['effective_date']} — {r['jurisdiction']}: {r['title']} ({r['status']})" for r in soonest],
        }
    )

    sections.append(
        {
            "heading": "Portfolio Impact By Product",
            "level": 2,
            "paragraphs": [
                f"{len(impacted_products)} of {len(products)} products are exposed. Each product's obligations "
                "are listed worst-first below."
            ],
            "bullets": [],
        }
    )
    by_product: dict[str, list[dict]] = {}
    for impact in impacts:
        by_product.setdefault(impact["product_name"], []).append(impact)
    for name in sorted(by_product, key=lambda n: min(_severity_rank(i["severity"]) for i in by_product[n])):
        rows = by_product[name]
        bullets = [
            f"{i['obligation_title']} — {i['jurisdiction']}, {i['severity']}"
            + (f", effective {i['effective_date']}" if i["effective_date"] else "")
            + (f" [{'; '.join(i['reasons'])}]" if i["reasons"] else "")
            for i in rows
        ]
        sections.append({"heading": name, "level": 3, "paragraphs": [], "bullets": bullets})

    sections.append(
        {
            "heading": "Beverage Lens",
            "level": 2,
            "paragraphs": ["Category-specific reading of where the portfolio meets the rules."],
            "bullets": [],
        }
    )
    for finding in findings:
        bullets = []
        if finding["affected_products"]:
            bullets.append("Affected products: " + ", ".join(finding["affected_products"]))
        if finding["obligations"]:
            bullets.append("Related obligations: " + ", ".join(finding["obligations"]))
        bullets.append("Action: " + finding["action"])
        sections.append({"heading": finding["title"], "level": 3, "paragraphs": [finding["why"]], "bullets": bullets})

    actions: list[str] = []
    for impact in impacts:
        if impact["severity"] == "act-now":
            date = f", effective {impact['effective_date']}" if impact["effective_date"] else ""
            actions.append(f"Act now: {impact['product_name']} against {impact['obligation_title']} ({impact['jurisdiction']}{date}).")
    seen = set(actions)
    for finding in findings:
        if finding["action"] not in seen:
            actions.append(finding["action"])
            seen.add(finding["action"])
    sections.append(
        {
            "heading": "Recommended Actions",
            "level": 2,
            "paragraphs": [] if actions else ["No portfolio actions are outstanding this week."],
            "bullets": actions,
        }
    )

    return {
        "title": f"{company} regulatory weekly synthesis",
        "subtitle": "Synthesized impact analysis for the beverage portfolio",
        "generated": today.isoformat(),
        "sections": sections,
        "disclaimer": DISCLAIMER,
    }


def _severity_rank(severity: str) -> int:
    return {"act-now": 0, "high": 1, "watch": 2, "info": 3}[severity]
