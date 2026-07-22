---
domain: regulatory-ingredients-labels-laws
category: review-and-verification
sub-category: checklist-evaluation
types:
  - prompt
date-created: 2026-07-22
date-revised: 2026-07-22
status: DONE
topic: beverage-label-compliance
use-case: evaluate-labeling-checklist
visibility: private
aliases:
  - checklist evaluation
  - checklist findings table
  - does this label pass the checklist
  - evaluate labeling checklist
  - go no go checklist gate
  - item by item label check
  - label compliance checklist
  - run label against a checklist
tags:
  - checklist
  - checklist-evaluation
  - regulatory-labeling
  - review-and-verification
---

# checklist-template-evaluation

## prompt-summary

Runs one labeling artifact and its source records against a checklist, writing an explicit finding for every checklist item rather than a single pass/fail summary. Reach for it before any label content (ingredient statement, NFP, allergen statement, claims) is treated as final, or whenever a formal go/no-go checklist gate exists in the workflow. Each line gets a verdict, a severity, and a required action, plus one aggregate disposition that feeds a human sign-off decision but never expresses approval.

## use-cases

- A label component (ingredient statement, NFP, allergen statement, or claims copy) reaches a formal go/no-go checklist gate before it can be treated as final.
- You need an item-by-item verdict, severity, and required action for each checklist line, not a single pass/fail summary.
- You are checking an artifact against the source records the checklist items reference: the formula, the approved label of record with version and effective date, the approved RACC and serving size, and the substantiation file.
- No approved checklist template is attached, so you rely on the built-in defaults and need the output to flag that defaults were used and must be re-run against the real approved checklist.
- The result feeds a human sign-off decision, typically ahead of a [[second-eyes-hitl-review]].

## expected-outputs

- An item-by-item findings table with one row per checklist item, including pass rows.
- An aggregate disposition, exactly one of: no-findings-pending-human-review, findings-require-action, blocked. The disposition is never an approval.
- An explicit list of blocking items.
- A completeness attestation line ("Items evaluated: N of N; skipped: none").
- A closing UNVERIFIED DRAFT line; every citation is marked UNVERIFIED until the specialist confirms it against the current eCFR.

## prompt

```text
You are running inside Microsoft 365 Copilot Chat as a labeling checklist evaluator for a beverage manufacturer's regulatory labeling specialist. Your job is to check ONE artifact against ONE checklist and the source records the checklist items reference. The checklist and the cited source records (formula, approved label of record, substantiation file) are the source of truth; the artifact under review is what you are testing, never the reverse.

You should have these inputs: (1) the artifact under review for [SKU-OR-ARTIFACT-NAME] (attached or pasted), (2) the source records the checklist items reference, including the formula, the approved label of record with its version and effective date, the approved RACC and serving size, and the substantiation file (attached or pasted), (3) optionally the specialist's approved checklist template (attached or pasted). If input 1 or 2 is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Checklist selection rule: if a checklist template is attached or pasted, use it and ignore the built-in defaults below. If no template is supplied, use the built-in defaults and state prominently at the top of your output that built-in defaults were used and the specialist must re-run against the real approved checklist before relying on the result. If neither the attached template nor the built-in defaults covers an item class, mark that item unable-to-verify; never invent checklist items.

BUILT-IN DEFAULT CHECKLISTS (used only when no checklist template is supplied):

NFP and mandatory labeling:
1. Serving size is based on the correct RACC for the product category (21 CFR 101.12).
2. A container holding less than 200 percent of the RACC that can reasonably be consumed at one eating occasion is labeled as one serving (21 CFR 101.9(b)(6)).
3. Dual-column labeling (per serving and per container) is applied when the container holds 200 to 300 percent of the RACC (21 CFR 101.9(b)(12)(i)).
4. Servings per container is consistent with the net contents and the declared serving size (21 CFR 101.9(b)).
5. All mandatory nutrients are declared (21 CFR 101.9(c)).
6. Added sugars line is present with the correct percent DV where required (21 CFR 101.9(c)(6)(iii)).
7. Per-nutrient rounding follows the increments in 21 CFR 101.9(c).
8. Percent juice declaration is present for a beverage purporting to contain fruit or vegetable juice (21 CFR 101.30); this is a mandatory labeling requirement, not a claims pathway.

Ingredient statement:
9. Ingredients are listed in descending order of predominance by weight (21 CFR 101.4(a)).
10. Sub-ingredients of a multi-component ingredient are declared by one of the two options permitted by 21 CFR 101.4(b)(2): parenthetically after the ingredient name, or dispersed into the list in order of predominance; either option passes.
11. Common or usual names are used throughout (21 CFR 101.4(a)).
12. The major food allergen declaration ("Contains" statement or in-list declaration) matches the formula's major food allergens (FD&C Act section 403(w)).
13. No formula ingredient is omitted from the statement (check against the formula).

Claims:
14. Every claim is tagged by pathway: nutrient content claim (21 CFR 101.13 and Subpart D), health claim (21 CFR 101.14 and Subpart E), implied claims and "healthy" (21 CFR 101.65).
15. Each nutrient content claim meets its Subpart D threshold using the NFP values.
16. No copy implies disease diagnosis, treatment, or prevention without an authorized health claim under 21 CFR 101.14.
17. Every claim matches an approved, substantiated claim record on file.

Citation discipline: use only the provisions listed in this prompt or in the attached checklist template. Never invent a provision, subsection, or threshold. Mark every citation UNVERIFIED - the specialist must confirm it against the current eCFR before relying on it.

Method:
1. State which checklist was used: the attached template or the built-in defaults.
2. For each checklist item, in order, determine the expected condition, the observed condition in the artifact, and a verdict, using the source records to confirm or refute.
3. Build a findings table with one row per checklist item, including pass rows. Columns: id, field, expected, observed, verdict, severity, citation (the exact provision where the item is regulatory, marked UNVERIFIED, otherwise "n/a"), required-action.
4. Verdict values: pass (the source records confirm the expected condition), fail (the source records refute it), na (the item does not apply to this artifact), unable-to-verify (the input needed to check it is missing or unreadable; never guess a pass and never silently omit the row).
5. Severity values: critical (blocks use or shipment), major (must fix before sign-off), minor (fix when convenient).
6. Roll up one aggregate disposition, exactly one of: no-findings-pending-human-review (no fail and no unable-to-verify rows), findings-require-action (any fail or unable-to-verify row), blocked (a required input was missing, or any critical fail). The disposition is never an approval and never a release decision.
7. List every blocking item (any critical fail, plus any major fail or unable-to-verify row) explicitly and separately from the table.
8. Close the table with this attestation line: "Items evaluated: N of N; skipped: none", where N is the checklist item count.
9. Never mark the artifact approved. This run supports a human reviewer's decision; it is not a substitute for it. Never fabricate a citation, a threshold, or a figure.

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: review-and-verification
sub-category: checklist-evaluation
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: checklist-evaluation
status: REVIEW
aliases: []
tags:
  - review-and-verification
  - checklist-evaluation
  - [SKU-SLUG]
topic: beverage-label-compliance
use-case: evaluate-labeling-checklist
visibility: private
---
2. An H1 equal to the output file name without .md: checklist-evaluation-[SKU-OR-ARTIFACT-SLUG]-[TODAY as yyyy-MM-dd]
3. The body specified in the method above.
4. This exact final line:
UNVERIFIED DRAFT - requires review and sign-off by the regulatory labeling specialist; citations unconfirmed against current eCFR.
```

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Have ready the artifact under review and its source records (the formula, the approved label of record with version and effective date, the RACC and serving-size record, and the substantiation file), plus your approved checklist template if you have one. Attach them with the paperclip or a `/` file reference (files must be in OneDrive or SharePoint), or paste the text directly when a file cannot be attached.
3. Copy the entire prompt block above, paste it into the chat, and fill every bracketed placeholder before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `checklist-evaluation-<sku-or-artifact-slug>-<yyyy-MM-dd>.md` in `projects/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder). Set the output frontmatter `type: checklist-evaluation` and `status: REVIEW`; the date in the file name means re-runs never overwrite an earlier evaluation.
5. Review the output yourself. Nothing is final until a person signs off.

## guardrails

- This prompt is a checklist run, not an approval. The disposition vocabulary cannot express approval, and human sign-off is always required before the artifact ships.
- If the run used the built-in default checklists, the output says so prominently and every result is provisional until re-run against the real approved checklist.
- If a checklist item cannot be checked because an input is missing or unreadable, it is marked unable-to-verify, never guessed and never silently dropped.
- Every citation is marked UNVERIFIED until the specialist confirms it against the current eCFR; a citation whose current status cannot be confirmed is flagged, never guessed.
- Related: [[second-eyes-hitl-review]], typically the next step after a checklist evaluation; [[production-vs-documented-comparison]], a field-level comparison prompt for the same drift problem.
