# regwatch rollout — v1 changelog (baseline)

The first tier in a phased rollout of the FDA beverage briefing. v1 is the
baseline, so this changelog describes what it includes and what is deliberately
held back for later tiers.

## Purpose

The headlines a busy team member can read in under a minute: what changed, what
is coming due, and the items that matter. No jargon, United States only.

## Included

- **Scope** — a one-line statement (FDA food safety impacting US beverages).
- **What Happened (Last 90 Days)** — a plain bulleted list of dated developments,
  each with a source link.
- **Coming Due** — obligations with a dated effective date in the horizon.
- **Key Items** — every FDA and California item as a one-line entry (title,
  status, date, jurisdiction).
- **Disclaimer.**

## Deliberately Held Back (Added in Later Tiers)

- The context for what each rule is, and what it means (v2).
- Governing CFR citations (v2).
- FDA warning-letter enforcement themes (v2).
- Canada and Mexico (v2).
- What we need to do per item, affected products, the live unconfirmed feed, and
  a consolidated action list (v3).

## How to Generate

```bash
python3 scripts/regwatch.py briefing --tier v1 --since-days 90 --out report.md
```

## Audience

Everyone on the team — a shared situational baseline.
