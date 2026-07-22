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

Builds the Nutrition Facts Panel field set at the correct serving size from supplied nutrient data, the supplied Reference Amount Customarily Consumed (RACC), and supplied Daily Value (DV) table values, with the arithmetic shown for every computed value.

## when-to-use

Nutrient data and a serving size or RACC determination exist for a SKU and the NFP has not yet been built, or the formula/fill volume changed since the last build.

## what-to-use-for

Turning nutrient testing data, a serving size/RACC determination, fill volume, and the DV values in use into the full NFP field set: serving size, servings per container, all mandatory nutrients, %DV, and the added-sugars line, applying the numeric single-serving and dual-column rules.

## required-inputs

- Nutrient data (per-serving or per-100g test results)
- Serving size / RACC determination
- Fill volume (container size)
- Daily Value (DV) table values in use

## expected-outputs

- NFP field set (all mandatory nutrients with values and %DV), with the arithmetic shown for every computed value
- Dual-column labeling determination (with the fill-volume-to-RACC percentage computation shown)
- Added-sugars line
- UNVERIFIED marks on any value not directly computable from the supplied data
- Citations for each rule applied

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Have all four inputs ready (nutrient data, serving size/RACC determination, fill volume, DV values in use); attach them with the paperclip or a `/` file reference (files must be in OneDrive or SharePoint), or paste each into its placeholder when a file cannot be attached.
3. Copy the entire prompt-text block below, paste it into the chat, and fill every bracketed placeholder before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `nfp-draft-<sku-slug>.md` in `projects/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder).
5. Review the output yourself. Nothing is final until a person signs off.

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: content-derivation`, `sub-category: nutrition-facts-panel`, `date-created`/`date-revised` set to the run date, `type: nfp-draft`, `status: REVIEW`, `aliases: []`, `tags: [content-derivation, nutrition-facts-panel, <sku-slug>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: nfp-draft`, `visibility: private`.

File name: `nfp-draft-<sku-slug>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `projects/regulatory-labeling/`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: build the Nutrition Facts Panel field set at the correct serving size.

You should have these inputs: (1) nutrient data (per-serving or per-100g test results), (2) the serving size/RACC determination, (3) the fill volume, (4) the Daily Value (DV) table values in use. If any input is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input; in particular, never recall a RACC value or a DV value from memory.

Method:
1. Read the nutrient data, serving size/RACC determination, fill volume, and DV values I provide below.
2. Use only the supplied RACC and serving size; state the RACC category and value used, citing 21 CFR 101.12 as the source rule. If the RACC determination is not supplied, stop and ask for it.
3. Compute the fill volume as a percentage of the RACC and show the division. Under 200 percent of the RACC, label as one serving per 21 CFR 101.9(b)(6). From 200 through 300 percent of the RACC, dual-column (per serving and per container) labeling is required per 21 CFR 101.9(b)(12)(i). Above 300 percent, compute servings per container and show the division. State which case applies and why.
4. Build the full mandatory nutrient field set per 21 CFR 101.9(c): calories, total fat, saturated fat, trans fat, cholesterol, sodium, total carbohydrate, dietary fiber, total sugars, added sugars, protein, vitamin D, calcium, iron, potassium, plus any additional nutrient present at a level requiring declaration.
5. Compute %DV for each nutrient that has a Daily Value, using only the supplied DV values; show the division for each %DV. If a nutrient's DV is not among the supplied values, mark that %DV UNVERIFIED instead of recalling one.
6. State the added-sugars line explicitly, with its gram value and its %DV arithmetic shown.
7. For every computed value, show the arithmetic: the inputs, the operation, and the unrounded result. Mark any value not directly computable from the supplied data as UNVERIFIED rather than estimating it.
8. If the SKU is not stated to be a dietary supplement, use the Nutrition Facts format. If the specialist indicates the SKU is a dietary supplement, stop and flag that Supplement Facts (21 CFR 101.36) governs instead and is out of scope for this prompt.

Source of truth: the nutrient data, serving size/RACC, fill volume, and DV values I provide are the only sources.

Citations: use only the provisions listed in this prompt (21 CFR 101.9(b)(6), 101.9(b)(12)(i), 101.9(c), 101.12, and 101.36). Never invent a provision, subsection, or threshold. Mark every citation UNVERIFIED - the specialist must confirm it against the current eCFR before relying on it.

This is a draft NFP for human review, not a final approved panel. It has not been checked for rounding accuracy; do not represent it as print-ready.

Do not fabricate a nutrient value not present in or computable from the data I provide. Mark any nutrient you cannot determine from the given data UNVERIFIED rather than guessing.

[Paste nutrient data here]

[Paste serving size/RACC determination here]

[Paste DV table values in use here]

Fill volume: [fill volume]

SKU identifier: [SKU]

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: content-derivation
sub-category: nutrition-facts-panel
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: nfp-draft
status: REVIEW
aliases: []
tags:
  - content-derivation
  - nutrition-facts-panel
  - [SKU-SLUG]
topic: beverage-label-compliance
use-case: nfp-draft
visibility: private
---
2. An H1 equal to the output file name without .md: nfp-draft-<sku-slug>
3. The body specified in the method above.
4. This exact final line:
UNVERIFIED DRAFT - requires review and sign-off by the regulatory labeling specialist; citations unconfirmed against current eCFR.
```

## guardrails

Human-in-the-loop: this is a draft, not a final NFP; always route it through [[nutrition-facts-panel-rounding-check]] before treating it as complete. The RACC and DV values are supplied inputs, never recalled from memory; the prompt stops when they are absent. Every computed value carries its shown arithmetic, and anything not computable from the supplied data is marked UNVERIFIED, never estimated.

Related: [[nutrition-facts-panel-rounding-check]].
