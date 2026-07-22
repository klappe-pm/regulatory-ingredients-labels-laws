# regwatch rollout — v3 changelog (full detail)

The third and final tier. v3 keeps everything in v2 and adds the decision-grade
detail: the action for each item, the products it touches, the live feed, and a
single consolidated to-do list. This is the complete briefing.

## What Is New Versus v2

- **What we need to do.** Every obligation entry gains the action — the concrete
  next step — after What happened and What it means.
- **Affected portfolio.** "What it means" now names the specific Talking Rain
  products exposed to each obligation, from the impact analysis.
- **Full warning-letter detail.** Each FDA enforcement theme now carries its
  governing CFR and a beverage-specific note, not just the trigger.
- **New section — Newly Detected, Unconfirmed.** Items pulled live from the
  Federal Register feed, each flagged for analyst confirmation before promotion
  into the curated change log.
- **New section — What To Do Next (Consolidated).** A single de-duplicated
  action list across all items, so nothing has to be reassembled by hand.

## Relationship to the Tiers Below

v3 is a strict superset of v2, which is a strict superset of v1. The same data
and the same engine produce all three; only the depth changes, set by `--tier`.

## How to Generate

```bash
python3 scripts/regwatch.py briefing --tier v3 --since-days 90 --out report.md
```

## Audience

The regulatory or compliance owner who acts on the detail and assigns the
follow-ups.
