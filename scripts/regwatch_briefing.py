"""regwatch human-readable briefing, tiered for a phased team rollout.

Builds a clean, marked-up briefing focused on FDA food safety that directly
impacts the United States beverage industry, plus Canada and Mexico. The same
data renders at three complexity tiers so reports can be rolled out to a team
from simple to detailed:

- v1: the headlines — what happened, what is coming due, the key items. One
  screen, no jargon, US only.
- v2: adds the context and the governing CFR per item, the FDA warning-letter
  themes, and the Canada and Mexico view.
- v3: the full briefing — adds What We Need To Do per item, the affected
  portfolio, full warning-letter detail, the unconfirmed live feed, and a
  consolidated action list.

Each finding is written as What Happened / What It Means / What We Need To Do,
with the governing CFR (or national equivalent) and backlinks. Pure function
over already-loaded data; returns markdown.
"""

from __future__ import annotations

import datetime as dt

STATUS_ORDER = {"enacted": 0, "finalized": 0, "voluntary": 1, "proposed": 2, "in-progress": 3, "monitoring": 4}
TIER_ORDER = {"v1": 1, "v2": 2, "v3": 3}


def _at_least(tier: str, floor: str) -> bool:
    return TIER_ORDER[tier] >= TIER_ORDER[floor]


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


def _parse(date: str) -> dt.date | None:
    try:
        return dt.date.fromisoformat(date)
    except (ValueError, TypeError):
        return None


def _recent_window(events: list[dict], today: dt.date, since_days: int | None, recent_count: int):
    """Select recent change-log events.

    With a window, return events within `since_days` of an anchor date. The
    anchor is today when there is recent activity, otherwise the latest recorded
    development, so a report stays populated against a historical change log and
    states the window it actually covers.
    """
    dated = [(e, _parse(e.get("date", ""))) for e in events]
    dated = [(e, d) for e, d in dated if d is not None]
    if since_days is None:
        ordered = [e for e, _ in sorted(dated, key=lambda pair: pair[1], reverse=True)]
        return ordered[:recent_count], None
    latest = max((d for _, d in dated), default=today)
    has_recent = any(today - dt.timedelta(days=since_days) <= d <= today for _, d in dated)
    anchor = today if has_recent else latest
    start = anchor - dt.timedelta(days=since_days)
    selected = [(e, d) for e, d in dated if start <= d <= anchor]
    ordered = [e for e, _ in sorted(selected, key=lambda pair: pair[1], reverse=True)]
    return ordered, (start, anchor, anchor != today)


def _upcoming(obligations: list[dict], today: dt.date, horizon_days: int = 540) -> list[dict]:
    horizon = today + dt.timedelta(days=horizon_days)
    kept = []
    for ob in obligations:
        date = _parse(ob.get("effective_date", ""))
        if date and today <= date <= horizon:
            kept.append(ob)
    return sorted(kept, key=lambda ob: ob["effective_date"])


def _obligation_block(ob: dict, detail: dict, impacts_by_ob: dict[str, list[str]], tier: str) -> list[str]:
    oid = ob["obligation_id"]
    info = detail.get(oid)
    effective = f", effective {ob['effective_date']}" if ob["effective_date"] else ""
    lines = [f"### {ob['title']}  \n_{ob['status']}{effective} · {ob['jurisdiction']}_", ""]

    if info:
        lines += [f"**What happened.** {info['what']}", ""]
        means = info["means"]
        products = impacts_by_ob.get(oid)
        if products and tier == "v3":
            means += f" Affected portfolio: {', '.join(products)}."
        lines += [f"**What it means.** {means}", ""]
        cfr = _links(info.get("cfr", []))
        if cfr:
            lines += [f"**Governing rule.** {cfr}", ""]
        if tier == "v3":
            lines += [f"**What we need to do.** {info['action']}", ""]
        backlinks = _backlinks(info.get("backlinks", []))
        if backlinks:
            lines += [f"**Sources.** {backlinks}", ""]
    else:
        note = ob.get("notes") or "Detail pending; confirm against primary source."
        lines += [f"**What happened.** {ob['title']} ({ob['status']}).", ""]
        lines += [f"**What it means.** {note}", ""]
        if tier == "v3":
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
    candidates: list[dict] | None = None,
    tier: str = "v3",
    since_days: int | None = None,
) -> str:
    if tier not in TIER_ORDER:
        raise ValueError(f"unknown tier '{tier}'")
    impacts_by_ob = _impacts_by_obligation(impacts)
    window_label = {"v1": "v1 (headlines)", "v2": "v2 (context and CFR)", "v3": "v3 (full detail)"}[tier]

    out: list[str] = []
    out.append("# regwatch-fda-beverage-briefing")
    out.append("")
    out.append(f"_Generated {today.isoformat()} · {window_label} · internal research, not legal advice._")
    out.append("")

    # Scope, scaled to tier.
    out.append("## Scope")
    out.append("")
    scope = (
        "FDA food safety and labeling that directly impacts the United States beverage industry."
    )
    if _at_least(tier, "v2"):
        scope += " Canada and Mexico are covered as the other markets the portfolio reaches."
    if tier == "v3":
        scope += (
            " Each item is written as What happened, What it means (with the governing CFR and the "
            "context for what the rule is), and What we need to do, with backlinks to primary sources."
        )
    out += [scope, ""]

    # Recent developments.
    events, window = _recent_window(changelog.get("events", []), today, since_days, recent_count)
    heading = "What Happened Recently" if since_days is None else f"What Happened (Last {since_days} Days)"
    out.append(f"## {heading}")
    out.append("")
    if window and window[2]:
        out.append(
            f"Covering {window[0].isoformat()} to {window[1].isoformat()}, anchored to the latest recorded "
            "development because no newer entries are in the change log yet."
        )
        out.append("")
    elif window:
        out.append(f"Covering {window[0].isoformat()} to {window[1].isoformat()}.")
        out.append("")
    if not events:
        out += ["No recorded developments in this window.", ""]
    elif tier == "v1":
        for event in events:
            out.append(f"- {event['date']} — {event['headline']} ([source]({event.get('source_url', '')}))")
        out.append("")
    else:
        for event in events:
            out.append(f"### {event['date']} — {event['headline']}")
            out.append("")
            out.append(f"**What happened.** {event['what_happened']}")
            out.append("")
            cfr = _links(event.get("cfr", []))
            if cfr:
                out += [f"**Governing rule.** {cfr}", ""]
            out.append(f"**Source.** [{event['agency']} — {event['country']}]({event.get('source_url', '')})")
            out.append("")

    # Coming due (all tiers).
    upcoming = _upcoming(obligations, today)
    out.append("## Coming Due")
    out.append("")
    if upcoming:
        for ob in upcoming:
            out.append(f"- {ob['effective_date']} — {ob['jurisdiction']}: {ob['title']} ({ob['status']})")
    else:
        out.append("- Nothing with a dated effective date in the horizon.")
    out.append("")

    # Live unconfirmed feed (v3 only).
    candidates = candidates or []
    if tier == "v3" and candidates:
        out.append("## Newly Detected — Unconfirmed (Federal Register Feed)")
        out.append("")
        out.append(
            f"{len(candidates)} item(s) from the live feed, flagged for analyst confirmation before "
            "promotion into the change log."
        )
        out.append("")
        for candidate in candidates[:recent_count]:
            out.append(f"### {candidate.get('date', '')} — {candidate.get('headline', '')}")
            out.append("")
            out.append(f"**What happened (unconfirmed).** {candidate.get('what_happened', '')}")
            out.append("")
            cfr = _links(candidate.get("cfr", []))
            if cfr:
                out += [f"**CFR (from the feed).** {cfr}", ""]
            if candidate.get("source_url"):
                out += [f"**Source.** [Federal Register {candidate.get('document_number', '')}]({candidate['source_url']})", ""]

    federal = sorted(
        [ob for ob in obligations if ob["jurisdiction"] == "US-Federal"],
        key=lambda ob: (STATUS_ORDER.get(ob["status"], 9), ob["title"]),
    )
    california = sorted(
        [ob for ob in obligations if ob["jurisdiction"] == "US-CA"],
        key=lambda ob: (STATUS_ORDER.get(ob["status"], 9), ob["title"]),
    )

    if tier == "v1":
        # Compact one-line list of the items that matter.
        out.append("## Key Items")
        out.append("")
        for ob in federal + california:
            date = ob["effective_date"] or "no date"
            out.append(f"- {ob['title']} — {ob['status']}, {date} ({ob['jurisdiction']})")
        out.append("")
    else:
        out.append("## United States — FDA Food Safety (Beverage Focus)")
        out.append("")
        for ob in federal:
            out += _obligation_block(ob, detail, impacts_by_ob, tier)
        out.append("### California (State Overlay)")
        out.append("")
        out.append("California is not FDA but sets the strictest US bar and often parallels federal action.")
        out.append("")
        for ob in california:
            out += _obligation_block(ob, detail, impacts_by_ob, tier)

    # FDA warning letters (v2 brief, v3 full).
    if _at_least(tier, "v2"):
        out.append("## FDA Warning Letters — Enforcement Themes For Beverages")
        out.append("")
        out.append(
            "FDA enforces largely through warning letters; these recurring themes signal where attention "
            f"lands. Live database: [FDA Warning Letters]({warning_letters['database_url']})."
        )
        out.append("")
        for theme in warning_letters.get("themes", []):
            out.append(f"### {theme['theme']}")
            out.append("")
            out.append(f"**What triggers it.** {theme['what_triggers']}")
            out.append("")
            if tier == "v3":
                cfr = _links(theme.get("cfr", []))
                if cfr:
                    out += [f"**Governing rule.** {cfr}", ""]
                out += [f"**For beverages.** {theme['beverage_note']}", ""]

        # Canada and Mexico.
        for country_name, code in (("Canada", "CA"), ("Mexico", "MX")):
            out.append(f"## {country_name}")
            out.append("")
            rows = [ob for ob in obligations if ob["country"] == code]
            if rows:
                for ob in rows:
                    out += _obligation_block(ob, detail, impacts_by_ob, tier)
            else:
                out += [f"No {country_name} obligations tracked yet.", ""]

    # Consolidated actions (v3 only).
    if tier == "v3":
        out.append("## What To Do Next (Consolidated)")
        out.append("")
        seen: set[str] = set()
        for ob in federal + california:
            info = detail.get(ob["obligation_id"])
            if info and info["action"] not in seen:
                out.append(f"- {ob['title']}: {info['action']}")
                seen.add(info["action"])
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
