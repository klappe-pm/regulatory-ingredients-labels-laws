# regwatch rollout — v2 changelog (adds context and CFR)

The second tier. v2 keeps everything in v1 and adds the context, the legal
citations, and the other two markets, turning a headline list into a briefing a
regulatory-aware reader can act on.

## What Is New Versus v1

- **Recent developments are now explained.** Each item in "What Happened" gains a
  What happened sentence, the governing CFR with an eCFR link, and a labeled
  source, instead of a single headline bullet.
- **New section — United States, FDA Food Safety.** Each FDA obligation (and a
  California overlay) is written as What happened, What it means, Governing rule
  (CFR), and Sources. The compact "Key Items" list from v1 is replaced by these
  fuller entries.
- **New section — FDA Warning Letters.** The recurring enforcement themes that
  hit beverages, each with what triggers it.
- **New sections — Canada and Mexico.** The two other markets the portfolio
  reaches, each as a What happened / What it means / CFR entry.

## Still Held Back (Added in v3)

- What we need to do per item (the action).
- The affected Talking Rain products on each item.
- Full warning-letter detail (governing CFR and beverage-specific notes).
- The live, unconfirmed Federal Register feed.
- A consolidated action list.

## How to Generate

```bash
python3 scripts/regwatch.py briefing --tier v2 --since-days 90 --out report.md
```

## Audience

Regulatory-aware leads in R&D, brand, and operations who need the why and the
citation, not only the headline.
