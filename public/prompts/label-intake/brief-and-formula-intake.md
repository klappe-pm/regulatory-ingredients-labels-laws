---
domain: regulatory-ingredients-labels-laws
category: label-intake
sub-category: intake
date-created: 2026-07-22
date-revised: 2026-07-22
type: prompt
status: DONE
aliases: []
tags:
  - label-intake
  - intake
  - regulatory-labeling
topic: beverage-label-compliance
use-case: normalize-intake-record
visibility: private
---

# brief-and-formula-intake

## description

Normalizes a dev brief and a formula/spec into a single structured labeling intake record, so drafting and review prompts downstream have one consistent source instead of a scattered brief and spreadsheet.

## when-to-use

A new SKU, reformulation, or line extension has a dev brief and a formula but no structured intake record yet.

## what-to-use-for

Turning free-form brief text and a formula/spec sheet into a normalized record: SKU identity, formula table with quantities, intended serving size, claims mentioned in the brief, and a list of open questions or missing data blocking downstream drafting.

## required-inputs

- Dev brief (text or pasted document content)
- Formula or spec sheet (ingredient list with quantities, sub-ingredient breakdowns if any)
- SKU identifier

## expected-outputs

- Structured intake record (SKU identity, formula table, serving size, claims mentioned)
- Open questions list
- Missing-data list, each item naming what is missing and what it blocks

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: label-intake`, `sub-category: intake`, `date-created` and `date-revised` set to the day the specialist runs this prompt, `type: intake-record`, `status: DRAFT` (advance to `INPRG`/`DONE` per the status vocabulary as the SKU progresses), `aliases: []`, `tags: [label-intake, intake, <sku-slug>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: intake-record`, `visibility: private`.

File name: `intake-record-<sku-slug>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `{private_folder}`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: normalize a dev brief and a formula/spec into one structured labeling intake record for a beverage SKU.

Method:
1. Read the dev brief and the formula/spec I provide below.
2. Extract SKU identity (name, SKU code if given, package size, intended channel).
3. Build a formula table: each ingredient, its sub-ingredients if compound, and quantity or percentage as stated. Preserve the order given; do not reorder into predominance order, that is a separate downstream task.
4. Extract the intended serving size, if stated, and flag if it is absent.
5. List every claim mentioned anywhere in the brief (marketing copy, positioning language, or explicit claim language), verbatim.
6. Produce an open-questions list: anything ambiguous in the brief or formula that a human needs to resolve before drafting can start.
7. Produce a missing-data list: anything downstream drafting or review will need that is not present (for example: no serving size given, no allergen statement from the facility, no substantiation file referenced for a claim). For each item, name what it blocks.

Source of truth: the dev brief and formula/spec I provide are the only sources; do not infer facts not stated in them.

This is not a compliance judgment. Do not approve or reject any claim here; that is out of scope for this prompt. Surface ambiguity in the open-questions list rather than resolving it yourself.

Do not fabricate any figure, ingredient, or claim not present in the source materials. If something is unclear, put it in the open-questions list rather than guessing.

Return the complete file content, beginning with the YAML frontmatter block, ready to save at the path I specify, with no commentary outside the file content.

[Paste dev brief here]

[Paste formula/spec here]

SKU identifier: [SKU]
```

## guardrails

Human-in-the-loop: this is a normalization pass, not a compliance decision; open questions and missing data are surfaced for a human to resolve, never silently filled in. Escalate any brief that already states a claim requiring health-claim substantiation (see [[claims-target-scoping]]) as an open question rather than accepting it at face value.

Related: [[claims-target-scoping]] (run next, after the intake record is normalized).
