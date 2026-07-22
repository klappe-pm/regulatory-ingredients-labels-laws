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

Derives a compliant ingredient statement from the formula, ordering ingredients by predominance by weight and formatting sub-ingredient parentheticals, flavor declarations, and preservative-function declarations correctly.

## when-to-use

An intake record ([[brief-and-formula-intake]]) exists with a formula table, and the ingredient statement has not yet been drafted or the formula has changed since the last draft.

## what-to-use-for

Turning a formula (ingredients with quantities, sub-ingredients for compound ingredients) into a draft ingredient statement in descending order by predominance by weight, with parentheticals for sub-ingredients, the 2-percent-or-less grouping where it applies, flavor and preservative-function declarations, and flags for anything that needs a human decision (for example: two ingredients close enough in weight that order is ambiguous, or an ingredient needing a common-or-usual name determination).

## required-inputs

- Formula with quantities
- Sub-ingredient breakdowns for any compound ingredient

## expected-outputs

- Ingredient statement in descending predominance order
- Parentheticals for sub-ingredients
- Statement of whether the 2-percent-or-less grouping was applied, and to which ingredients
- Flags for ambiguous ordering, naming, flavor, or preservative-function decisions

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Have the formula (with quantities and sub-ingredient breakdowns) ready; attach it with the paperclip or a `/` file reference (files must be in OneDrive or SharePoint), or paste it into the placeholder when a file cannot be attached.
3. Copy the entire prompt-text block below, paste it into the chat, and fill every bracketed placeholder before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `ingredient-statement-<sku-slug>.md` in `projects/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder).
5. Review the output yourself. Nothing is final until a person signs off.

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: content-derivation`, `sub-category: ingredient-statement`, `date-created`/`date-revised` set to the run date, `type: ingredient-statement-draft`, `status: REVIEW`, `aliases: []`, `tags: [content-derivation, ingredient-statement, <sku-slug>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: ingredient-statement-draft`, `visibility: private`.

File name: `ingredient-statement-<sku-slug>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `projects/regulatory-labeling/`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: derive a compliant draft ingredient statement from a formula.

You should have these inputs: (1) the formula with quantities, (2) sub-ingredient breakdowns for any compound ingredient. If any input is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Method:
1. Read the formula (ingredients with quantities, sub-ingredient breakdowns for compound ingredients) I provide below.
2. Order every ingredient in descending order by predominance by weight, per 21 CFR 101.4(a)(1).
3. For ingredients present at 2 percent or less by weight, state whether the "Contains 2% or less of" grouping under 21 CFR 101.4(a)(2) applies, and if you apply it, list which ingredients it covers.
4. For each compound ingredient, format its own sub-ingredients as a parenthetical immediately after the compound ingredient's name, also in descending order by weight within that parenthetical, per 21 CFR 101.4(b)(2).
5. Declare flavors as "natural flavor", "artificial flavor", or both, per 21 CFR 101.22(h)-(i), and append the function to any chemical preservative (for example "potassium sorbate (preservative)") per 21 CFR 101.22(j); flag any ingredient whose flavor or preservative status is unclear from the formula.
6. Use each ingredient's common or usual name per 21 CFR 101.4(a)(1) and 21 CFR 102.5; flag any ingredient whose common-or-usual name is not obvious from the formula (for example, a proprietary blend name) as needing a human naming decision.
7. Where two ingredients are close enough in stated weight that predominance order is ambiguous from the data given, flag it rather than guessing an order.
8. Produce the draft ingredient statement as a single formatted string, plus the flag list.

Source of truth: the formula I provide is the only source; do not add or infer ingredients not present in it.

Citations: use only the provisions listed in this prompt (21 CFR 101.4(a)(1), 101.4(a)(2), 101.4(b)(2), 101.22(h), 101.22(i), 101.22(j), and 21 CFR 102.5). Never invent a provision, subsection, or threshold. Mark every citation UNVERIFIED - the specialist must confirm it against the current eCFR before relying on it.

This is a draft for human review, not a final approved statement. It has not been checked against allergen requirements or against the labeling checklist; do not represent it as final or compliant.

Do not fabricate a quantity, an ingredient, or a sub-ingredient not present in the formula I provide. Flag anything you cannot resolve from the data given rather than guessing.

[Paste formula with quantities and sub-ingredients here]

SKU identifier: [SKU]

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: content-derivation
sub-category: ingredient-statement
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: ingredient-statement-draft
status: REVIEW
aliases: []
tags:
  - content-derivation
  - ingredient-statement
  - [SKU-SLUG]
topic: beverage-label-compliance
use-case: ingredient-statement-draft
visibility: private
---
2. An H1 equal to the output file name without .md: ingredient-statement-<sku-slug>
3. The body specified in the method above.
4. This exact final line:
UNVERIFIED DRAFT - requires review and sign-off by the regulatory labeling specialist; citations unconfirmed against current eCFR.
```

## guardrails

Human-in-the-loop: this is a draft, not an approved ingredient statement; ambiguous ordering, naming, flavor, and preservative-function decisions are flagged for a human, never resolved silently. Always route the draft through [[allergen-statement-verification]] before it is treated as complete.

Related: [[allergen-statement-verification]].
