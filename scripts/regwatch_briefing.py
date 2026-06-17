"""regwatch human-readable briefing.

Builds a clean, marked-up briefing focused on FDA food safety that directly
impacts the United States beverage industry, plus Canada and Mexico. Every
finding is written as What Happened / What It Means / What We Need To Do, with
the governing CFR (or national equivalent) and backlinks to supporting sources.
It reads the rich detail sidecar, the dated change log, and the FDA
warning-letter themes so the output is usable, not just a list of titles.

Pure function over already-loaded data; returns markdown.
"""

from __future__ import annotations

import datetime as dt

STATUS_ORDER = {"enacted": 0, "finalized": 0, "voluntary": 1, "proposed": 2, "in-progress": 3, "monitoring": 4}


def _links(items: list[dict]) -> str:
    return "; ".join(f"[{i['citation']}]({i['url']})" for i in items) if items else ""


def _backlinks(items: list[dict]) -> str:
    return " · ".join(f"[{i['label']}]({i['url']})" for i in items) if items else ""


def _impacts_by_obligation(impacts: list[dict]) -> dict[str, list[str]]:
    grouped: dict[str, list[str]] = {}
    for impact in impacts:
        grouped.setdefault(impact["obligation_id"], [])
        if impact["product_name"] not in grouped[impact["obligation_id"]]:
            grouped[impact["obligation_id"]].append(impact["product_name"])
    return grouped


def _obligation_block(ob: dict, detail: dict, impacts_by_ob: dict[str, list[str]]) -> list[str]:
    oid = ob["obligation_id"]
    info = detail.get(oid)
    effective = f", effective {ob['effective_date']}" if ob["effective_date"] else ""
    lines = [f"### {ob['title']}  \n_{ob['status']}{effective} · {ob['jurisdiction']}_", ""]

    if info:
        lines += [f"**What happened.** {info['what']}", ""]
        means = info["means"]
        products = impacts_by_ob.get(oid)
        if products:
            means += f" Affected portfolio: {', '.join(products)}."
        lines += [f"**What it means.** {means}", ""]
        cfr = _links(info.get("cfr", []))
        if cfr:
            lines += [f"**Governing rule.** {cfr}", ""]
        lines += [f"**What we need to do.** {info['action']}", ""]
        backlinks = _backlinks(info.get("backlinks", []))
        if backlinks:
            lines += [f"**Sources.** {backlinks}", ""]
    else:
        note = ob.get("notes") or "Detail pending; confirm against primary source."
        lines += [f"**What happened.** {ob['title']} ({ob['status']}).", ""]
        lines += [f"**What it means.** {note}", ""]
        lines += ["**What we need to do.** Confirm scope and effective date against the source, then add to the detail sidecar.", ""]
        if ob.get("source_url"):
            lines += [f"**Sources.** [{ob['jurisdiction']} source]({ob['source_url']})", ""]
    return lines


def build_briefing(
    obligations: list[dict],
    detail: dict,
    changelog: dict,
    warning_letters: dict,
    impacts: list[dict],
    today: dt.date,
    recent_count: int = 8,
) -> str:
    impacts_by_ob = _impacts_by_obligation(impacts)
    by_id = {ob["obligation_id"]: ob for ob in obligations}

    out: list[str] = []
    out.append("# regwatch-fda-beverage-briefing")
    out.append("")
    out.append(f"_Generated {today.isoformat()}. Internal research; not legal advice._")
    out.append("")

    out.append("## Scope And How To Read This")
    out.append("")
    out.append(
        "This briefing is focused on FDA food safety and labeling that directly impacts the "
        "United States beverage industry, with Canada and Mexico covered as the two other markets "
        "the portfolio reaches. Each item is written as **What happened**, **What it means** (with "
        "the governing CFR or national equivalent and the context for what the rule actually is), "
        "and **What we need to do**, with backlinks to primary sources. Confirm anything that "
        "touches a live label against current source text and counsel before acting."
    )
    out.append("")

    # Recent developments from the change log, most recent first.
    events = sorted(changelog.get("events", []), key=lambda e: e["date"], reverse=True)[:recent_count]
    out.append("## What Happened Recently")
    out.append("")
    out.append(
        "Dated regulatory developments, most recent first. This is maintained as a change log so the "
        "briefing reflects more than a single in-window item; the live scan and FDA feeds add to it."
    )
    out.append("")
    for event in events:
        out.append(f"### {event['date']} — {event['headline']}")
        out.append("")
        out.append(f"**What happened.** {event['what_happened']}")
        out.append("")
        cfr = _links(event.get("cfr", []))
        if cfr:
            out.append(f"**Governing rule.** {cfr}")
            out.append("")
        out.append(f"**Source.** [{event['agency']} — {event['country']}]({event['source_url']})")
        out.append("")

    # United States: FDA first, then a condensed California subsection.
    out.append("## United States — FDA Food Safety (Beverage Focus)")
    out.append("")
    federal = [ob for ob in obligations if ob["jurisdiction"] == "US-Federal"]
    federal.sort(key=lambda ob: (STATUS_ORDER.get(ob["status"], 9), ob["title"]))
    for ob in federal:
        out += _obligation_block(ob, detail, impacts_by_ob)

    out.append("### California (State Overlay)")
    out.append("")
    out.append(
        "California is not FDA but it sets the strictest US bar and frequently parallels federal "
        "action, so it is tracked here for the beverage portfolio."
    )
    out.append("")
    california = [ob for ob in obligations if ob["jurisdiction"] == "US-CA"]
    california.sort(key=lambda ob: (STATUS_ORDER.get(ob["status"], 9), ob["title"]))
    for ob in california:
        out += _obligation_block(ob, detail, impacts_by_ob)

    # FDA warning letters.
    out.append("## FDA Warning Letters — Enforcement Themes For Beverages")
    out.append("")
    out.append(
        "FDA enforces food safety and labeling largely through warning letters, so the recurring "
        f"themes below are a leading signal of where attention lands. Check the live database: "
        f"[FDA Warning Letters]({warning_letters['database_url']})."
    )
    out.append("")
    for theme in warning_letters.get("themes", []):
        out.append(f"### {theme['theme']}")
        out.append("")
        out.append(f"**What triggers it.** {theme['what_triggers']}")
        out.append("")
        cfr = _links(theme.get("cfr", []))
        if cfr:
            out.append(f"**Governing rule.** {cfr}")
            out.append("")
        out.append(f"**For beverages.** {theme['beverage_note']}")
        out.append("")

    # Canada and Mexico.
    out.append("## Canada")
    out.append("")
    canada = [ob for ob in obligations if ob["country"] == "CA"]
    if canada:
        for ob in canada:
            out += _obligation_block(ob, detail, impacts_by_ob)
    else:
        out += ["No Canadian obligations tracked yet.", ""]

    out.append("## Mexico")
    out.append("")
    mexico = [ob for ob in obligations if ob["country"] == "MX"]
    if mexico:
        for ob in mexico:
            out += _obligation_block(ob, detail, impacts_by_ob)
    else:
        out += ["No Mexican obligations tracked yet.", ""]

    # Consolidated actions.
    out.append("## What To Do Next (Consolidated)")
    out.append("")
    actions: list[str] = []
    seen: set[str] = set()
    priority_ids = [ob["obligation_id"] for ob in federal] + [
        ob["obligation_id"] for ob in obligations if ob["jurisdiction"] == "US-CA"
    ]
    for oid in priority_ids:
        info = detail.get(oid)
        if info and info["action"] not in seen:
            actions.append(f"{by_id[oid]['title']}: {info['action']}")
            seen.add(info["action"])
    for action in actions:
        out.append(f"- {action}")
    out.append("")

    out.append("---")
    out.append("")
    out.append(
        "> Draft for analyst review and internal research only. Detection and analysis flag; a human "
        "confirms against primary source text and current product specifications before any compliance "
        "or marketing use. Not legal advice."
    )
    out.append("")
    return "\n".join(out).rstrip() + "\n"
