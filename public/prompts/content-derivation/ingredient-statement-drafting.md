---
domain: regulatory-ingredients-labels-laws
category: content-derivation
sub-category: ingredient-statement
date-created: 2026-07-22
date-revised: 2026-07-22
type: prompt
status: DONE
aliases: []
tags:
  - content-derivation
  - ingredient-statement
  - regulatory-labeling
topic: beverage-label-compliance
use-case: draft-ingredient-statement
visibility: private
---

# ingredient-statement-drafting

## description

Derives a compliant ingredient statement from the formula, ordering ingredients by predominance by weight and formatting sub-ingredient parentheticals correctly.

## when-to-use

An intake record ([[brief-and-formula-intake]]) exists with a formula table, and the ingredient statement has not yet been drafted or the formula has changed since the last draft.

## what-to-use-for

Turning a formula (ingredients with quantities, sub-ingredients for compound ingredients) into a draft ingredient statement in descending order by predominance by weight, with parentheticals for sub-ingredients and flags for anything that needs a human decision (for example: two ingredients close enough in weight that order is ambiguous, or an ingredient needing a common-or-usual name determination).

## required-inputs

- Formula with quantities
- Sub-ingredient breakdowns for any compound ingredient

## expected-outputs

- Ingredient statement in descending predominance order
- Parentheticals for sub-ingredients
- Flags for ambiguous ordering or naming decisions

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: content-derivation`, `sub-category: ingredient-statement`, `date-created`/`date-revised` set to the run date, `type: ingredient-statement-draft`, `status: DRAFT`, `aliases: []`, `tags: [content-derivation, ingredient-statement, <sku-slug>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: ingredient-statement-draft`, `visibility: private`.

File name: `ingredient-statement-<sku-slug>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `{private_folder}`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: derive a compliant draft ingredient statement from a formula.

Method:
1. Read the formula (ingredients with quantities, sub-ingredient breakdowns for compound ingredients) I provide below.
2. Order every ingredient in descending order by predominance by weight, per 21 CFR 101.4.
3. For each compound/sub-ingredient, format its own sub-ingredients as a parenthetical immediately after the compound ingredient's name, also in descending order by weight within that parenthetical.
4. Where two ingredients are close enough in stated weight that predominance order is ambiguous from the data given, flag it rather than guessing an order.
5. Flag any ingredient whose common-or-usual name is not obvious from the formula (for example, a proprietary blend name) as needing a human naming decision.
6. Produce the draft ingredient statement as a single formatted string, plus the flag list.

Source of truth: the formula I provide is the only source; do not add or infer ingredients not present in it.

Cite 21 CFR 101.4 for the predominance-order rule. If you cannot confirm the current text of 101.4, say so explicitly rather than asserting it.

This is a draft for human review, not a final approved statement. It has not been checked against allergen requirements (see [[allergen-statement-verification]]) or against the checklist ([[checklist-template-evaluation]]); do not represent it as final or compliant.

Do not fabricate a quantity, an ingredient, or a sub-ingredient not present in the formula I provide. Flag anything you cannot resolve from the data given rather than guessing.

Return the complete file content, beginning with the YAML frontmatter block, ready to save at the path I specify, with no commentary outside the file content.

[Paste formula with quantities and sub-ingredients here]

SKU identifier: [SKU]
```

## guardrails

Human-in-the-loop: this is a draft, not an approved ingredient statement; ambiguous ordering and naming decisions are flagged for a human, never resolved silently. Always route the draft through [[allergen-statement-verification]] before it is treated as complete.

Related: [[allergen-statement-verification]].
