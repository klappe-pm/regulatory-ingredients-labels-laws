---
domain: regulatory-ingredients-labels-laws
category: review-and-verification
sub-category: checklist-evaluation
date-created: 2026-07-22
date-revised: 2026-07-22
type: prompt
status: DONE
aliases: []
tags:
  - checklist-evaluation
  - review-and-verification
  - regulatory-labeling
  - checklist
topic: beverage-label-compliance
use-case: evaluate-labeling-checklist
visibility: private
---

# checklist-template-evaluation

## description

Runs a labeling artifact and its source records against a checklist template, writing an explicit finding for every checklist item rather than a single pass/fail summary.

## when-to-use

Before any label content (ingredient statement, NFP, allergen statement, claims) is treated as final, and whenever a formal go/no-go checklist gate exists in the workflow.

## what-to-use-for

Item-by-item evaluation of an artifact against a checklist, producing a finding, a severity, and a required action for every line, plus one aggregate disposition.

## required-inputs

- Checklist template (see placeholder below if none is supplied).
- The artifact under review (ingredient statement, NFP, allergen statement, or claims copy).
- Source records the checklist items reference (formula, approved label of record, substantiation file).

No checklist template was supplied for this library. The placeholder below is a representative starting checklist covering NFP, ingredient-statement, and claims fields; replace it with the specialist's real, approved checklist before relying on this prompt in production.

```text
PLACEHOLDER CHECKLIST (replace before production use)
NFP:
  1. Serving size matches approved RACC
  2. Servings per container matches fill volume
  3. Added sugars line present and non-zero if formula contains added sugar
  4. %DV values match current DV table
  5. Calories, total fat, sodium, total carbohydrate, total sugars, protein present
Ingredient statement:
  6. Ingredients listed in descending order by predominance
  7. Sub-ingredients parenthetically disclosed where required
  8. Allergen "Contains" statement present and matches the formula's major allergens
Claims:
  9. Every claim on the label matches an approved, substantiated claim record
  10. No claim uses "healthy" or an implied health claim without a current eligibility check on file
```

## expected-outputs

An item-by-item findings table (one row per checklist item), an aggregate disposition (pass, conditional-pass, fail), and an explicit list of blocking items.

## output-handling

Apply this note's frontmatter convention (domain, category, sub-category, date-created, date-revised, type, status, aliases, tags, then topic, use-case, visibility) to the saved output file. File name pattern: `checklist-evaluation-<sku-or-artifact-slug>-<yyyy-MM-dd>.md`. Save path: `projects/regulatory-labeling/` (visibility: private).

## prompt-text

```text
You are running inside Microsoft 365 Copilot Chat as a labeling checklist evaluator for a beverage manufacturer's regulatory labeling specialist. Your job is to check ONE artifact against ONE checklist template and the source records it references. The checklist template and the cited source records (formula, approved label of record, substantiation file) are the source of truth; the artifact under review is what you are testing, never the reverse.

Method:
1. Read the checklist template and confirm it is not empty; if the specialist has not replaced the placeholder checklist, say so explicitly before proceeding.
2. For each checklist item, in order, determine the expected condition, the observed condition in the artifact, and a verdict.
3. Build a findings table with columns: id, field (the checklist item), expected, observed, verdict (pass / fail / na), severity (critical / major / minor), citation (the exact regulatory provision if the item is regulatory in nature, otherwise "n/a"), required-action.
4. Roll the findings up into one aggregate disposition: pass (no fail items), conditional-pass (only minor/major fails with a clear required-action), or fail (any critical fail).
5. List every blocking item (any fail with severity critical or major) explicitly and separately from the table.
6. Never mark the artifact approved. This is a second set of eyes supporting a human reviewer's decision, not a substitute for it. State plainly that a human must sign off before the artifact ships.
7. Never fabricate a citation, a threshold, or a figure. If you cannot confirm the current status of a cited regulation, say so and mark that finding's citation as unconfirmed rather than guessing.

Return the complete file content for this evaluation, beginning with YAML frontmatter (domain, category, sub-category, date-created, date-revised, type, status, aliases, tags, topic, use-case, visibility), ready to save at the path given in this prompt's output-handling section. Return only the file content, no commentary outside it.
```

## guardrails

- This prompt is a checklist run, not an approval. Human sign-off is always required before the artifact ships.
- If the checklist template is still the placeholder, the run must say so and treat every result as provisional.
- Any citation whose current regulatory status cannot be confirmed is flagged, never guessed.

## see also

- [[checklist-evaluation]] (sub-category index)
- [[second-eyes-hitl-review]], typically the next step after a checklist evaluation
- [[production-vs-documented-comparison]], a field-level comparison prompt for the same drift problem
