---
domain: regulatory-ingredients-labels-laws
category: label-intake
sub-category: intake
types:
  - prompt
date-created: 2026-07-22
date-revised: 2026-07-22
status: DONE
topic: beverage-label-compliance
use-case: normalize-intake-record
visibility: private
aliases:
  - allergen capture table
  - formula spec intake
  - new sku intake
  - normalize dev brief
  - open questions and missing data
  - reformulation intake
  - serving size racc check
  - structure intake record
tags:
  - intake
  - label-intake
  - regulatory-labeling
---

# brief-and-formula-intake

## prompt-summary

Normalizes a dev brief and a formula or spec sheet into one structured labeling intake record, so downstream drafting and review prompts work from a single consistent source instead of a scattered brief and spreadsheet. Reach for it when a new SKU, reformulation, or line extension has a dev brief and a formula but no structured intake record yet. It captures SKU identity, a formula table with quantities, an allergen capture table, intended serving size with a RACC cross-check flag, claims mentioned in the brief, and a list of open questions and missing data blocking downstream drafting.

## use-cases

- A new SKU, reformulation, or line extension arrives with a dev brief and a formula but no structured intake record yet.
- You need to turn free-form brief text and a formula/spec sheet into one normalized record (SKU identity, formula table, allergen capture, serving size) before drafting starts.
- You need an allergen capture table built from the formula: the nine major allergens per FALCPA and the FASTER Act, plus any sulfite stated at or above 10 ppm (declaration required per 21 CFR 101.100(a)(4)).
- You need the intended serving size cross-checked against the RACC for the product category in 21 CFR 101.12(b) Table 2.
- You need every claim mentioned in the brief captured verbatim before running [[claims-target-scoping]].
- You need open questions and missing data surfaced (for example an absent supplier allergen statement that blocks allergen verification) before downstream drafting or review.

## expected-outputs

- Structured intake record (SKU identity, formula table, allergen capture table, serving size with RACC cross-check flag, claims mentioned)
- Open questions list
- Missing-data list, each item naming what is missing and what it blocks

## prompt

```
You are running inside Microsoft 365 Copilot Chat. Your single task: normalize a dev brief and a formula/spec into one structured labeling intake record for a beverage SKU.

You should have these inputs: (1) the dev brief, (2) the formula or spec sheet, (3) the SKU identifier, (4) optional: a supplier allergen statement, (5) optional: the RACC for this product category from 21 CFR 101.12(b) Table 2. If any of inputs 1 to 3 is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Method:
1. Read the dev brief and the formula/spec pasted below.
2. Extract SKU identity (name, SKU code if given, package size, intended channel).
3. Build a formula table: each ingredient, its sub-ingredients if compound, and quantity or percentage as stated. Preserve the order given; do not reorder into predominance order, that is a separate downstream task. Close the formula table with this attestation line: Ingredients captured: N of N lines in the spec; skipped: none.
4. Build an allergen capture table: for each formula line item, record any of the nine major food allergens (milk, egg, fish, crustacean shellfish, tree nuts, peanuts, wheat, soybean, sesame) that the source materials declare or that the ingredient name plainly states, per FALCPA and the FASTER Act, and record any sulfite the sources state at or above 10 ppm (declaration required per 21 CFR 101.100(a)(4)). Where the sources are silent, record "not stated"; never infer that an allergen is absent.
5. Extract the intended serving size, if stated, and flag if it is absent. Cross-check it against the RACC for this product category under 21 CFR 101.12(b): if a RACC is pasted below, compare the stated serving size against it and flag any difference; if no RACC is supplied, flag the RACC cross-check as an open question for the specialist to verify against 21 CFR 101.12(b) Table 2. Never assert a RACC value from memory.
6. List every claim mentioned anywhere in the brief (marketing copy, positioning language, or explicit claim language), verbatim.
7. Produce an open-questions list: anything ambiguous in the brief or formula that a human needs to resolve before drafting can start.
8. Produce a missing-data list: anything downstream drafting or review will need that is not present (for example: no serving size given, no supplier allergen statement, which blocks allergen-statement verification, no substantiation file referenced for a claim). For each item, name what it blocks.

Source of truth: the dev brief, formula/spec, and optional inputs pasted below are the only sources; do not infer facts not stated in them.

Use only the provisions listed in this prompt. Never invent a provision, subsection, or threshold. Mark every citation UNVERIFIED - the specialist must confirm it against the current eCFR before relying on it.

This is not a compliance judgment. Do not approve or reject any claim here; that is out of scope for this prompt. Surface ambiguity in the open-questions list rather than resolving it yourself.

Do not fabricate any figure, ingredient, allergen, or claim not present in the source materials. If something is unclear, put it in the open-questions list rather than guessing.

[Paste dev brief here]

[Paste formula/spec here]

SKU identifier: [SKU]

Supplier allergen statement (optional): [Paste supplier allergen statement here, or write "none provided"]

RACC from 21 CFR 101.12(b) Table 2 (optional): [Paste RACC here, or write "not supplied"]

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: label-intake
sub-category: intake
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: intake-record
status: REVIEW
aliases: []
tags:
  - label-intake
  - intake
  - [SKU-SLUG]
topic: beverage-label-compliance
use-case: intake-record
visibility: private
---
2. An H1 equal to the output file name without .md: intake-record-[SKU-SLUG]
3. The body specified in the method above.
4. This exact final line:
UNVERIFIED DRAFT - requires review and sign-off by the regulatory labeling specialist; citations unconfirmed against current eCFR.
```

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Have ready the dev brief, the formula or spec sheet (ingredient list with quantities and any sub-ingredient breakdowns), and the SKU identifier; optionally the supplier allergen statement (its absence is recorded as missing data because it blocks downstream allergen verification) and the RACC for the product category from 21 CFR 101.12(b) Table 2 (when not supplied, the RACC cross-check is flagged for you to verify). Paste their text into the bracketed placeholders, or attach a file with the paperclip or a `/` file reference only if it already lives in OneDrive or SharePoint.
3. Copy the entire prompt block above, paste it into the chat, and fill every bracketed placeholder before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `intake-record-<sku-slug>.md` (kebab-case, H1 equal to the file-name stem) and save it to `projects/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder).
5. Review the output yourself. Nothing is final until a person signs off.

## guardrails

Human-in-the-loop: this is a normalization pass, not a compliance decision; open questions and missing data are surfaced for a human to resolve, never silently filled in. Escalate any brief that already states a claim requiring health-claim substantiation (see [[claims-target-scoping]]) as an open question rather than accepting it at face value.

Related: [[claims-target-scoping]] (run next, after the intake record is normalized).
