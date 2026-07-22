---
domain: regulatory-ingredients-labels-laws
category: content-derivation
sub-category: nutrition-facts-panel
date-created: 2026-07-22
date-revised: 2026-07-22
type: prompt
status: DONE
aliases: []
tags:
  - content-derivation
  - nutrition-facts-panel
  - regulatory-labeling
topic: beverage-label-compliance
use-case: build-nutrition-facts-panel
visibility: private
---

# nutrition-facts-panel-buildout

## description

Builds the Nutrition Facts Panel field set at the correct serving size, using nutrient data and the applicable Reference Amount Customarily Consumed (RACC), including the added-sugars line.

## when-to-use

Nutrient data and a serving size or RACC determination exist for a SKU and the NFP has not yet been built, or the formula/fill volume changed since the last build.

## what-to-use-for

Turning nutrient testing data, a serving size/RACC determination, and fill volume into the full NFP field set: serving size, servings per container, all mandatory nutrients, %DV, and the added-sugars line, flagging whether dual-column labeling is required.

## required-inputs

- Nutrient data (per-serving or per-100g test results)
- Serving size / RACC determination
- Fill volume (container size)

## expected-outputs

- NFP field set (all mandatory nutrients with values and %DV)
- Dual-column labeling need (yes/no, with reasoning)
- Added-sugars line
- Citations for each rule applied

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: content-derivation`, `sub-category: nutrition-facts-panel`, `date-created`/`date-revised` set to the run date, `type: nfp-draft`, `status: DRAFT`, `aliases: []`, `tags: [content-derivation, nutrition-facts-panel, <sku-slug>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: nfp-draft`, `visibility: private`.

File name: `nfp-draft-<sku-slug>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `{private_folder}`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: build the Nutrition Facts Panel field set at the correct serving size.

Method:
1. Read the nutrient data, serving size/RACC determination, and fill volume I provide below.
2. Confirm the RACC and resulting serving size against 21 CFR 101.12; state the RACC category used.
3. Determine whether the container requires dual-column (per serving and per container/per unit) labeling per 21 CFR 101.9, and state the reasoning (for example: a container is between 1 and 2 servings, or is a single-serving container that could reasonably be consumed in one sitting versus multiple).
4. Build the full mandatory nutrient field set per 21 CFR 101.9: calories, total fat, saturated fat, trans fat, cholesterol, sodium, total carbohydrate, dietary fiber, total sugars, added sugars, protein, vitamin D, calcium, iron, potassium, plus any additional nutrient present at a level requiring declaration.
5. Compute %DV for each nutrient that has a Daily Value, against the current DV table; state the DV basis used.
6. State the added-sugars line explicitly and flag if you cannot confirm the added-sugars definition or DV is current.
7. If no SKU is stated as a dietary supplement, use the Nutrition Facts format (not Supplement Facts, 21 CFR 101.36); if the specialist indicates the SKU is a supplement, flag that Supplement Facts formatting is out of scope for this prompt and needs separate handling.

Source of truth: the nutrient data, serving size/RACC, and fill volume I provide are the only sources; %DV values are computed from the current published DV table, which you must state and flag if you cannot confirm it is current.

Cite 21 CFR 101.9 (NFP format, added sugars, %DV) and 21 CFR 101.12 (RACC/serving size) for every rule applied. If you cannot confirm current compliance status of the added-sugars final rule or DV table, flag it explicitly rather than asserting it.

This is a draft NFP for human review, not a final approved panel. It has not been checked for rounding accuracy (see [[nutrition-facts-panel-rounding-check]]); do not represent it as print-ready.

Do not fabricate a nutrient value not present in or computable from the data I provide. Flag any nutrient you cannot determine from the given data rather than guessing.

Return the complete file content, beginning with the YAML frontmatter block, ready to save at the path I specify, with no commentary outside the file content.

[Paste nutrient data here]

[Paste serving size/RACC determination here]

Fill volume: [fill volume]

SKU identifier: [SKU]
```

## guardrails

Human-in-the-loop: this is a draft, not a final NFP; always route it through [[nutrition-facts-panel-rounding-check]] before treating it as complete. Flag, never assume, when RACC category or DV-table currency is uncertain.

Related: [[nutrition-facts-panel-rounding-check]].
