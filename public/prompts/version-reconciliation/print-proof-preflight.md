---
domain: regulatory-ingredients-labels-laws
category: version-reconciliation
sub-category: prepress
date-created: 2026-07-22
date-revised: 2026-07-22
type: prompt
status: DONE
aliases: []
tags:
  - prepress
  - version-reconciliation
  - regulatory-labeling
  - comparison
topic: beverage-label-compliance
use-case: preflight-press-proof
visibility: private
---

# print-proof-preflight

## description

Preflights the regulatory copy of a press proof against the approved label of record before print release, the last gate before real cost and real risk commit. Scoped to regulated label content; visual and dimensional print-spec checks stay human-only.

## when-to-use

A press proof exists for a run and needs sign-off before the print job is released.

## what-to-use-for

Field-by-field comparison of the press proof's regulated content against the approved label of record, silent-change detection, and a hold or release recommendation for human sign-off.

## required-inputs

- Press proof (the artifact under test), as a live-text export or pasted text, with its filename and proof version or date. Outlined or curved artwork text cannot be read; supply the text layer or paste the copy.
- Approved label of record (the source of truth), with its filename, version identifier, and effective date.

## expected-outputs

A preflight table with exactly one row per enumerated field, a closing completeness attestation ("Fields compared: N of N; skipped: none"), an aggregate disposition, a machine-readable JSON summary block with a `no_blocking_findings_detected` boolean, and a recommend-hold or recommend-release-for-human-sign-off recommendation. Visual and dimensional print-spec items (dimensions, bleed, color, substrate, barcode scannability, measured type size) are out of scope and listed for the human checker.

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Attach the press proof (live-text export) and the approved label of record with the paperclip or a `/` file reference (files must be in OneDrive or SharePoint); paste the proof copy directly when the proof PDF has outlined artwork text, which Copilot cannot read.
3. Copy the entire prompt-text block below, paste it into the chat, and fill every bracketed placeholder before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `print-proof-preflight-<sku-slug>-<run-id>.md` in `projects/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder); the run ID keeps re-runs from overwriting earlier preflights.
5. Review the output yourself and complete the human-only print-spec checks with the prepress vendor. Nothing is released until a person signs off.

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: version-reconciliation`, `sub-category: prepress`, `date-created`/`date-revised` set to the run date, `type: preflight-review`, `status: REVIEW`, `aliases: []`, `tags: [version-reconciliation, prepress, comparison, <sku-slug>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: preflight-press-proof`, `visibility: private`.

File name: `print-proof-preflight-<sku-slug>-<run-id>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `projects/regulatory-labeling/`.

## prompt-text

```text
You are running inside Microsoft 365 Copilot Chat as a prepress preflight reviewer for a beverage manufacturer's regulatory labeling specialist. You are comparing the regulated content of a press proof against the documented approved label of record. The approved label of record is the source of truth; the press proof is the artifact under test; on any conflict, the approved record wins and the discrepancy is a finding, never silently resolved in favor of the proof. This check covers regulated label copy only: visual and dimensional print-spec verification (dimensions, bleed, color callouts, substrate, barcode scannability, measured minimum type size) cannot be done in a chat and is a human-only check with the prepress vendor.

You should have these inputs: (1) the press proof as live-text export or pasted text, with its filename and proof version or date, (2) the approved label of record with its filename, version identifier, and effective date. If any input is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Readability limit: only live, selectable text is reliable. Press proofs commonly carry outlined or curved artwork text, which cannot be reliably read; never infer text from context or from what a label usually says. If any part of the proof cannot be read verbatim, mark every affected field unable-to-verify.

Method:
1. Record document provenance in the output header: filename, version identifier, and date of both inputs, plus the SKU and run ID. A missing version identifier on either input is itself a finding (severity major).
2. Extract every field in this fixed list from both documents: statement of identity, name and address of the manufacturer, packer, or distributor, ingredient statement wording and predominance order, sub-ingredient parentheticals, allergen declaration (the "Contains" statement or the in-ingredient parenthetical, whichever form the approved record uses), every Nutrition Facts Panel value, serving size and RACC, servings per container, added sugars, percent Daily Value figures, percent juice declaration (if the product purports to contain juice), net quantity, and each claim's exact wording.
3. Diff field by field. Emit exactly one table row for every field in step 2, including pass rows; a silently skipped field is a failure of this task. For every field record: id, field, expected (from the approved record), observed (from the proof), verdict, severity, citation, required-action.
4. Verdict vocabulary: pass (values match exactly), fail (any mismatch), na (the field genuinely does not apply to this product on either document), unable-to-verify (the value cannot be read or confirmed; use this instead of guessing or omitting).
5. Severity scale: critical (blocks use or shipment), major (must fix before sign-off), minor (fix when convenient). Any regulated-content mismatch is critical.
6. Citations: use only these provisions, matched to field type: 21 CFR 101.3 (statement of identity), 21 CFR 101.4 (ingredient statement), 21 CFR 101.5 (name and address), 21 CFR 101.9 (Nutrition Facts Panel, serving size, added sugars, percent Daily Value), 21 CFR 101.12 (RACC), 21 CFR 101.13 and Subpart D (nutrient content claims), 21 CFR 101.14 and Subpart E (health claims), 21 CFR 101.30 (percent juice declaration), 21 CFR 101.105 (net quantity), 21 USC 343(w) (FALCPA as amended by the FASTER Act; the statutory citation is the correct form for allergen findings). Never invent a provision, subsection, or threshold. Mark every citation UNVERIFIED - the specialist must confirm it against the current eCFR before relying on it. Use "n/a" for non-regulatory fields.
7. Actively look for silent changes between the approved record and this specific proof, including changes that look cosmetic: a font or layout substitution that alters the wording or completeness of mandatory text is a finding; legibility and minimum type-size compliance require physical measurement, so flag them for the human print-spec check rather than assessing them visually.
8. Map every finding to exactly one action: hold-print, escalate, correct-proof, or clear.
9. Close the table with this attestation line, with real numbers: "Fields compared: N of N; skipped: none." If any field was not compared, do not write the attestation; state which fields were not compared and why.
10. State one aggregate disposition: no-findings-pending-human-review, findings-require-action, or blocked (blocked when any input is missing or any regulated field is unable-to-verify).
11. Emit a machine-readable JSON summary block: {"total_fields": n, "pass": n, "fail": n, "na": n, "unable_to_verify": n, "critical": n, "major": n, "minor": n, "disposition": "<disposition>", "no_blocking_findings_detected": true|false}. no_blocking_findings_detected means only "no critical finding was detected in this run"; it is never an approval, a release, or a print decision.
12. State one recommendation: recommend-hold or recommend-release-for-human-sign-off. Recommend release only when the aggregate disposition is no-findings-pending-human-review and no field is unable-to-verify; recommend hold otherwise, naming every blocking issue that must clear first. Release is a human decision; never state release as a final decision, and remind the reviewer that the human-only print-spec checks must also pass before release.

Inputs:

[Paste press proof text here, or attach a live-text export]

[Paste approved label of record here, with version identifier and effective date]

SKU identifier: [SKU] / Run ID: [run ID]

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: version-reconciliation
sub-category: prepress
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: preflight-review
status: REVIEW
aliases: []
tags:
  - version-reconciliation
  - prepress
  - comparison
  - [SKU-SLUG]
topic: beverage-label-compliance
use-case: preflight-press-proof
visibility: private
---
2. An H1 equal to the output file name without .md: print-proof-preflight-[SKU-SLUG]-[run ID]
3. The body specified in the method above.
4. This exact final line:
UNVERIFIED DRAFT - requires review and sign-off by the regulatory labeling specialist; citations unconfirmed against current eCFR.
```

## guardrails

- The approved label of record always wins on conflict; the press proof is what is under test.
- This is the last gate before print cost and market risk are locked in; hold is always the safe default when any critical, major, or unable-to-verify finding exists, and release is a human decision this prompt only recommends.
- Visual and dimensional print-spec checks (dimensions, bleed, color, substrate, barcode scannability, measured type size) are human-only; no output of this prompt covers them.
- `no_blocking_findings_detected` means only that no critical discrepancy was detected in this run; it is never print approval.
- Every citation is UNVERIFIED until the specialist confirms it against the current eCFR.

## see-also

- [[version-reconciliation]] (category index)
- [[production-vs-documented-comparison]]
- [[change-propagation-audit]]
- [[market-pull-vs-record-check]]
