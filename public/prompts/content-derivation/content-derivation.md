---
domain: regulatory-ingredients-labels-laws
category: content-derivation
sub-category: content-derivation
date-created: 2026-07-22
date-revised: 2026-07-22
type: index
status: DONE
aliases: []
tags:
  - content-derivation
  - regulatory-labeling
topic: beverage-label-compliance
use-case: browse-content-derivation-prompts
visibility: private
---

# content-derivation

Prompts that derive the regulated content of a label directly from the formula and specification: the ingredient statement, the allergen declaration, and the Nutrition Facts Panel. These are drafting prompts, not review prompts; each output still needs a downstream verification pass ([[review-and-verification]]) before it is treated as final. The ingredient-statement pair covers drafting the predominance-ordered ingredient list plus verifying the allergen declaration and cross-contact; the NFP pair covers building the panel at the correct serving size, then verifying rounding and %DV on every value before it is treated as final.

## prompts

- [[ingredient-statement-drafting]], derive a compliant ingredient statement from the formula
- [[allergen-statement-verification]], verify the allergen declaration and cross-contact against the nine major food allergens
- [[nutrition-facts-panel-buildout]], build the NFP at the correct serving size from supplied nutrient data, RACC, and DV values
- [[nutrition-facts-panel-rounding-check]], verify rounding and %DV on every NFP value

## workflow

1. Run [[ingredient-statement-drafting]] on the intake record's formula; its draft feeds step 2.
2. Run [[allergen-statement-verification]] on the same formula plus the allergen matrix and facility statement; its findings gate the ingredient statement.
3. Run [[nutrition-facts-panel-buildout]] on the nutrient data, RACC determination, fill volume, and DV values; its draft feeds step 4.
4. Run [[nutrition-facts-panel-rounding-check]] on the draft NFP; its disposition gates the panel.
5. All four outputs feed [[review-and-verification]] for the full-label check and then [[version-reconciliation]] before print.

Up: [[regulatory-labeling]]

![[bases/content-derivation.base]]
