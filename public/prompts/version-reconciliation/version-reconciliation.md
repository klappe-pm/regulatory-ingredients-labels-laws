---
domain: regulatory-ingredients-labels-laws
category: version-reconciliation
sub-category: reconciliation
date-created: 2026-07-22
date-revised: 2026-07-22
type: index
status: DONE
aliases: []
tags:
  - version-reconciliation
  - regulatory-labeling
topic: beverage-label-compliance
use-case: browse-version-reconciliation
visibility: private
---

# version-reconciliation

Catches drift between the documented approved label of record and what actually gets produced, propagated, or printed. Product development and regulatory iterate on formula and copy; changes are not always shared, so downstream labels can print and reach market incorrect. Every prompt here treats the approved label of record as the source of truth, diffs field by field, and maps findings to an action rather than resolving them itself. The category covers two stages: field-level reconciliation (a production copy against the record, and an approved change against every downstream artifact) and the prepress last gate, where a press proof is checked before print release commits real cost and real risk.

## capability-caveats

- Copilot Chat reads live, selectable text only. Outlined or curved artwork text in art files and press-style PDFs is not reliably readable; attach live-text exports or paste the copy, and expect unable-to-verify findings when you cannot.
- Visual and dimensional print-spec checks (dimensions, bleed, color, substrate, barcode scannability, measured type size) are human-only work with the prepress vendor; no prompt in this category performs them.
- Every output is an unverified draft with unconfirmed citations; nothing any prompt returns is print approval or release authority. A `no_blocking_findings_detected: true` in a JSON summary means only that the run detected no critical discrepancy.

## prompts

- [[production-vs-documented-comparison]]
- [[change-propagation-audit]]
- [[print-proof-preflight]]

## workflow

1. Run [[production-vs-documented-comparison]] whenever a production file is generated or re-generated from an approved label; its reconciliation output gates whether that file may feed prepress or any downstream asset.
2. Run [[change-propagation-audit]] after any approved formula, claim, or NFP change; unpropagated findings route back to correction, then step 1 re-runs on each corrected artifact.
3. Run [[print-proof-preflight]] on the press proof as the last gate before print release; its recommend-hold or recommend-release output feeds the specialist's release decision alongside the human-only print-spec checks.
4. Post-market drift is covered by [[market-pull-vs-record-check]] in its own category; feed it the same approved label of record these prompts use.

## see-also

- [[regulatory-labeling]] (master index)
- [[market-pull-vs-record-check]], the fourth comparison prompt in the library

![[bases/version-reconciliation.base]]
