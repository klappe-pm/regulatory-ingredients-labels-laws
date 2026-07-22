---
domain: regulatory-ingredients-labels-laws
category: version-reconciliation
sub-category: reconciliation
types:
  - prompt
date-created: 2026-07-22
date-revised: 2026-07-22
status: DONE
topic: beverage-label-compliance
use-case: reconcile-production-vs-record
visibility: private
aliases:
  - art file vs label of record
  - compare production label to approved
  - did the production file match the approved label
  - field by field label comparison
  - label drift check
  - packaging proof reconciliation
  - production vs approved label check
  - silent label change detection
tags:
  - comparison
  - reconciliation
  - regulatory-labeling
  - version-reconciliation
---

# production-vs-documented-comparison

## prompt-summary

Diffs a production copy of a label against the documented approved label of record, field by field, to catch silent drift before it compounds downstream. Reach for it whenever a production file (art file, packaging proof, copy deck) is generated or re-generated from an approved label, and before that production copy is used as an input anywhere else (prepress, downstream SKUs, marketing assets). The approved label of record always wins on conflict; the production copy is what is under test.

## use-cases

- A production art file, packaging proof, or copy deck was just generated or re-generated from an approved label and you need to confirm it matches before anyone builds on it.
- A production copy is about to feed prepress, downstream SKUs, or marketing assets, and must be reconciled against the label of record first.
- You suspect silent drift: a formula change that never reached the ingredient statement, an added-sugars value that no longer matches the formula, or an allergen added or removed without a declaration update.
- A claim was edited after approval and you need to confirm the production copy still matches the approved wording and its substantiation.
- You need every field-level finding mapped to a single action (hold-print, escalate, correct-record, or clear) with a citation.

## expected-outputs

A reconciliation table with exactly one row per enumerated field, a closing completeness attestation ("Fields compared: N of N; skipped: none"), an aggregate disposition, and a machine-readable JSON summary block with a `no_blocking_findings_detected` boolean.

## prompt

```text
You are running inside Microsoft 365 Copilot Chat as a label reconciliation reviewer for a beverage manufacturer's regulatory labeling specialist. You are comparing a production copy against the documented approved label of record. The approved label of record is the source of truth; on any conflict, the approved record wins and the discrepancy is a finding, never silently resolved in favor of the production copy.

You should have these inputs: (1) the production copy (the artifact under test) with its filename and version identifier or export date, (2) the approved label of record (the source of truth) with its filename, version identifier, and effective date. If any input is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Readability limit: only live, selectable text is reliable. Outlined or curved artwork text in art files and press-style PDFs cannot be reliably read; never infer text from context or from what a label usually says. If any part of an input cannot be read verbatim, mark every affected field unable-to-verify.

Method:
1. Record document provenance in the output header: filename, version identifier, and date of both inputs. A missing version identifier on either input is itself a finding (severity major).
2. Extract every field in this fixed list from both documents: statement of identity, name and address of the manufacturer, packer, or distributor, ingredient statement wording and predominance order, sub-ingredient parentheticals, allergen declaration (the "Contains" statement or the in-ingredient parenthetical, whichever form the approved record uses), every Nutrition Facts Panel value, serving size and RACC, servings per container, added sugars, percent Daily Value figures, percent juice declaration (if the product purports to contain juice), net quantity, and each marketing claim's exact wording.
3. Diff field by field. Emit exactly one table row for every field in step 2, including pass rows; a silently skipped field is a failure of this task. For every field record: id, field, expected (from the approved record), observed (from the production copy), verdict, severity, citation, required-action.
4. Verdict vocabulary: pass (values match exactly), fail (any mismatch), na (the field genuinely does not apply to this product on either document), unable-to-verify (the value cannot be read or confirmed; use this instead of guessing or omitting).
5. Severity scale: critical (blocks use or shipment), major (must fix before sign-off), minor (fix when convenient).
6. Citations: use only these provisions, matched to field type: 21 CFR 101.3 (statement of identity), 21 CFR 101.4 (ingredient statement), 21 CFR 101.5 (name and address), 21 CFR 101.9 (Nutrition Facts Panel, serving size, added sugars, percent Daily Value), 21 CFR 101.12 (RACC), 21 CFR 101.13 and Subpart D (nutrient content claims), 21 CFR 101.14 and Subpart E (health claims), 21 CFR 101.30 (percent juice declaration), 21 CFR 101.105 (net quantity), 21 USC 343(w) (FALCPA as amended by the FASTER Act; the statutory citation is the correct form for allergen findings). Never invent a provision, subsection, or threshold. Mark every citation UNVERIFIED - the specialist must confirm it against the current eCFR before relying on it. Use "n/a" for non-regulatory fields.
7. Actively look for silent changes: a formula change that never reached the ingredient statement, an added-sugars value that no longer matches the formula, an allergen added or removed without a corresponding declaration update, or a claim edited after approval without a new substantiation record.
8. Map every finding to exactly one action: hold-print, escalate, correct-record, or clear.
9. Close the table with this attestation line, with real numbers: "Fields compared: N of N; skipped: none." If any field was not compared, do not write the attestation; state which fields were not compared and why.
10. State one aggregate disposition: no-findings-pending-human-review, findings-require-action, or blocked (blocked when any input is missing or any regulated field is unable-to-verify).
11. Emit a machine-readable JSON summary block: {"total_fields": n, "pass": n, "fail": n, "na": n, "unable_to_verify": n, "critical": n, "major": n, "minor": n, "disposition": "<disposition>", "no_blocking_findings_detected": true|false}. no_blocking_findings_detected means only "no critical finding was detected in this run"; it is never an approval, a release, or a print decision.
12. Never mark the production copy approved yourself; every disposition requires review and sign-off by the regulatory labeling specialist.

Inputs:

[Paste production copy text here]

[Paste approved label of record here, with version identifier and effective date]

SKU identifier: [SKU]

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: version-reconciliation
sub-category: reconciliation
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: reconciliation-review
status: REVIEW
aliases: []
tags:
  - version-reconciliation
  - reconciliation
  - comparison
  - [SKU-SLUG]
topic: beverage-label-compliance
use-case: reconcile-production-vs-record
visibility: private
---
2. An H1 equal to the output file name without .md: production-vs-documented-comparison-[SKU-SLUG]-[TODAY as yyyy-MM-dd]
3. The body specified in the method above.
4. This exact final line:
UNVERIFIED DRAFT - requires review and sign-off by the regulatory labeling specialist; citations unconfirmed against current eCFR.
```

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Have ready the production copy (with its filename and version identifier or export date) and the approved label of record (with its filename, version identifier, and effective date). Attach both with the paperclip or a `/` file reference (files must be in OneDrive or SharePoint); paste text directly when a file cannot be attached or when its text is outlined artwork rather than live text.
3. Copy the entire prompt block above, paste it into the chat, and fill every bracketed placeholder before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `production-vs-documented-comparison-<sku-slug>-<yyyy-MM-dd>.md` in `projects/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder), with the H1 equal to that file-name stem; the date stamp keeps re-runs from overwriting earlier comparisons. Apply this frontmatter to the saved file: `domain: regulatory-ingredients-labels-laws`, `category: version-reconciliation`, `sub-category: reconciliation`, `date-created`/`date-revised` set to the run date, `type: reconciliation-review`, `status: REVIEW`, `aliases: []`, `tags: [version-reconciliation, reconciliation, comparison, <sku-slug>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: reconcile-production-vs-record`, `visibility: private`.
5. Review the output yourself. Nothing is final until a person signs off.

## guardrails

- The approved label of record always wins on conflict; the production copy is what is under test.
- `no_blocking_findings_detected` means only that no critical discrepancy was detected in this run; it is a machine-readable signal for downstream tooling, never an approval, and a human still decides whether to proceed.
- Unreadable or unconfirmable values are unable-to-verify findings, never guesses and never silent omissions.
- Every citation is UNVERIFIED until the specialist confirms it against the current eCFR.
- Related: [[change-propagation-audit]], [[print-proof-preflight]], [[market-pull-vs-record-check]]
