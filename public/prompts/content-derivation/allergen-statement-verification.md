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
  - allergens
  - regulatory-labeling
topic: beverage-label-compliance
use-case: verify-allergen-declaration
visibility: private
---

# allergen-statement-verification

## description

Verifies the allergen declaration against the formula and facility cross-contact information, producing a Contains statement verdict and a precautionary-allergen-labeling (PAL) assessment.

## when-to-use

After [[ingredient-statement-drafting]] has produced a draft ingredient statement, or whenever the formula, allergen matrix, or facility statement changes.

## what-to-use-for

Checking every major food allergen against the formula and the facility's allergen matrix and cross-contact statement, producing an allergen verdict, a draft Contains statement, gaps in the supplied data, and a PAL assessment.

## required-inputs

- Formula (with sub-ingredients)
- Allergen matrix (facility-level allergen handling data)
- Facility statement (cross-contact controls)

## expected-outputs

- Allergen verdict (which of the major allergens are present)
- Draft Contains statement
- Gaps in the supplied data
- PAL (precautionary allergen labeling, e.g. "may contain") assessment

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: content-derivation`, `sub-category: ingredient-statement`, `date-created`/`date-revised` set to the run date, `type: allergen-verification`, `status: DRAFT`, `aliases: []`, `tags: [content-derivation, ingredient-statement, allergens, <sku-slug>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: allergen-verification`, `visibility: private`.

File name: `allergen-verification-<sku-slug>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `{private_folder}`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: verify the allergen declaration for a formula against the major food allergens and facility cross-contact data.

Method:
1. Read the formula, the allergen matrix, and the facility statement I provide below.
2. Check the formula's ingredients and sub-ingredients against the major food allergens under FALCPA as amended by the FASTER Act (milk, eggs, fish, crustacean shellfish, tree nuts, peanuts, wheat, soybeans, and sesame).
3. Draft the "Contains" statement listing every major allergen present as an ingredient or sub-ingredient.
4. Cross-check the facility statement and allergen matrix for cross-contact risk with allergens not present as ingredients; assess whether a precautionary statement (PAL, e.g. "may contain X") is warranted. State explicitly that PAL statements are voluntary industry practice, not an FDA-mandated format, and that the specialist must decide the wording and whether to use one.
5. List any gap where the allergen matrix or facility statement does not cover an ingredient present in the formula, or is otherwise incomplete.
6. Produce an allergen verdict (a clear list of allergens present, by ingredient), the draft Contains statement, the gaps list, and the PAL assessment.

Source of truth: the formula, allergen matrix, and facility statement I provide are the only sources.

Cite FALCPA and the FASTER Act as the basis for the major-allergen list. If you cannot confirm the current major-allergen list or its statutory basis, say so explicitly rather than asserting it.

This is an independent verification pass supporting a human reviewer. It never marks an allergen statement as final or print-ready; it surfaces gaps and a verdict for a human sign-off.

Do not fabricate an allergen finding, a cross-contact risk, or a gap not grounded in the data I provide. Flag anything the supplied data does not resolve rather than guessing.

Return the complete file content, beginning with the YAML frontmatter block, ready to save at the path I specify, with no commentary outside the file content.

[Paste formula here]

[Paste allergen matrix here]

[Paste facility statement here]

SKU identifier: [SKU]
```

## guardrails

Human-in-the-loop: this prompt verifies, it does not approve; any gap or cross-contact ambiguity is a finding for a human, not a decision made here. PAL wording is a specialist judgment call, not an FDA-prescribed format; never present a PAL recommendation as mandatory.

Related: [[ingredient-statement-drafting]].
