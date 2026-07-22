---
domain: regulatory-ingredients-labels-laws
category: content-derivation
sub-category: ingredient-statement
types:
  - prompt
date-created: 2026-07-22
date-revised: 2026-07-22
status: DONE
topic: beverage-label-compliance
use-case: verify-allergen-declaration
visibility: private
aliases:
  - allergen check
  - contains statement draft
  - cross-contact allergen review
  - does this need a contains statement
  - may contain labeling
  - nine major allergens check
  - precautionary allergen labeling
  - sesame declaration
tags:
  - allergens
  - content-derivation
  - ingredient-statement
  - regulatory-labeling
---

# allergen-statement-verification

## prompt-summary

Verifies a product's allergen declaration against the formula and the facility's cross-contact data, checking all nine major food allergens and producing a per-allergen findings table, a draft Contains statement, and a precautionary allergen labeling (PAL) assessment. Reach for it once a draft ingredient statement exists, or whenever the formula, allergen matrix, or facility statement changes. It flags generic declarations (a bare "fish" or "tree nuts" entry) as findings rather than passes, and marks any gap in the supplied data instead of guessing.

## use-cases

- A draft ingredient statement from [[ingredient-statement-drafting]] is ready and needs an allergen cross-check before sign-off.
- The formula, the facility allergen matrix, or the cross-contact statement changed since the last verification.
- You need a Contains statement drafted per 21 USC 343(w) from the food source names of every major allergen present.
- You need to decide whether a voluntary "may contain" (PAL) statement is warranted from facility cross-contact risk.
- You must confirm fish, crustacean shellfish, and tree nuts are declared by specific species or type, not generically.
- You want to surface gaps where the allergen matrix or facility statement does not cover an ingredient present in the formula.

## expected-outputs

- Findings table with one row per major allergen (all nine, including pass rows) and the attestation line "Allergens checked: 9 of 9; skipped: none."
- Draft Contains statement
- Gaps in the supplied data
- PAL (precautionary allergen labeling, e.g. "may contain") assessment, marked voluntary
- Aggregate disposition (no-findings-pending-human-review, findings-require-action, or blocked)

## prompt

```
You are running inside Microsoft 365 Copilot Chat. Your single task: verify the allergen declaration for a formula against the major food allergens and facility cross-contact data.

You should have these inputs: (1) the formula with sub-ingredients, (2) the allergen matrix (facility-level allergen handling data), (3) the facility statement (cross-contact controls). If any input is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Method:
1. Read the formula, the allergen matrix, and the facility statement I provide below.
2. Check the formula's ingredients and sub-ingredients against each of the nine major food allergens defined at 21 USC 321(qq) (FALCPA, as amended by the FASTER Act to add sesame): milk, eggs, fish, crustacean shellfish, tree nuts, peanuts, wheat, soybeans, sesame. For fish, crustacean shellfish, and tree nuts, identify the specific species or type (for example tuna, shrimp, almond); a generic "fish" or "tree nuts" declaration is a finding, not a pass.
3. Draft the Contains statement per 21 USC 343(w): the word "Contains" followed by the food source name of every major allergen present as an ingredient or sub-ingredient, placed immediately after or adjacent to the ingredient list. Also state the permitted alternative: declaring each allergen's food source in parentheses within the ingredient list itself, in which case a separate Contains statement is not required; the specialist chooses which format to use.
4. Cross-check the facility statement and allergen matrix for cross-contact risk from allergens not present as ingredients; assess whether a precautionary allergen labeling (PAL) statement (for example "may contain X") is warranted. PAL is voluntary industry practice with no citation; it is not an FDA-mandated format, and the specialist decides the wording and whether to use one.
5. List any gap where the allergen matrix or facility statement does not cover an ingredient present in the formula, or is otherwise incomplete.
6. Produce a findings table with one row per major allergen, all nine, including pass rows, with columns: id, allergen, expected (present in formula or not), observed (declaration and matrix status), verdict, severity, citation, required-action. Verdicts: pass (formula, matrix, and declaration agree), fail (mismatch or missing declaration), na (not applicable), unable-to-verify (input unreadable or silent on this allergen; never a guess or a silent omission). Severity: critical (blocks use or shipment), major (must fix before sign-off), minor (fix when convenient). PAL rows carry "no citation - voluntary practice" in the citation column. Close the table with this exact attestation line: "Allergens checked: 9 of 9; skipped: none."
7. Produce the draft Contains statement, the gaps list, the PAL assessment, and an aggregate disposition: no-findings-pending-human-review (every row pass or na), findings-require-action (any fail), or blocked (any unable-to-verify on a required input).

Source of truth: the formula, allergen matrix, and facility statement I provide are the only sources.

Citations: use only the provisions listed in this prompt (21 USC 343(w) and 21 USC 321(qq), FALCPA as amended by the FASTER Act). Never invent a provision, subsection, or threshold. Mark every citation UNVERIFIED - the specialist must confirm it against the current statute before relying on it.

This is an independent verification pass supporting a human reviewer. It never marks an allergen statement as final or print-ready; it surfaces findings and a disposition for a human sign-off.

Do not fabricate an allergen finding, a cross-contact risk, or a gap not grounded in the data I provide. Mark anything the supplied data does not resolve unable-to-verify rather than guessing.

[Paste formula here]

[Paste allergen matrix here]

[Paste facility statement here]

SKU identifier: [SKU]

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: content-derivation
sub-category: ingredient-statement
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: allergen-verification
status: REVIEW
aliases: []
tags:
  - content-derivation
  - ingredient-statement
  - allergens
  - [SKU-SLUG]
topic: beverage-label-compliance
use-case: allergen-verification
visibility: private
---
2. An H1 equal to the output file name without .md: allergen-verification-<sku-slug>
3. The body specified in the method above.
4. This exact final line:
UNVERIFIED DRAFT - requires review and sign-off by the regulatory labeling specialist; citations unconfirmed against current eCFR.
```

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Have the three inputs ready: the formula with sub-ingredients, the allergen matrix (facility-level allergen handling data), and the facility statement (cross-contact controls); attach them with the paperclip or a `/` file reference (files must be in OneDrive or SharePoint), or paste each into its placeholder when a file cannot be attached.
3. Copy the entire prompt block above, paste it into the chat, and fill every bracketed placeholder before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `allergen-verification-<sku-slug>.md` (kebab-case, H1 equal to the file-name stem) saved to `projects/regulatory-labeling/` in this vault, or your team's equivalent OneDrive/SharePoint folder.
5. Review the output yourself. Nothing is final until a person signs off.

## guardrails

Human-in-the-loop: this prompt verifies, it does not approve; any gap or cross-contact ambiguity is a finding for a human, not a decision made here. The allergen citations are statutory (21 USC 343(w), 321(qq)), not CFR rounding-style rules; the specialist confirms them against the current statute. PAL wording is a specialist judgment call, not an FDA-prescribed format; never present a PAL recommendation as mandatory.

Related: [[ingredient-statement-drafting]].
