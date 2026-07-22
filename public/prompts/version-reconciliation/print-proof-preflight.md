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

Preflights a press proof against the approved label of record and the print spec before print release, the last gate before real cost and real risk commit.

## when-to-use

A press proof exists for a run and needs sign-off before the print job is released.

## what-to-use-for

Field-by-field comparison of the press proof against the approved label of record (and the print spec for physical/production parameters), silent-change detection, and a hold/release recommendation.

## required-inputs

- Press proof (the artifact under test)
- Approved label (the source of truth)
- Print spec (physical dimensions, color, substrate parameters relevant to the run)

## expected-outputs

- Preflight verdict
- Discrepancies (regulatory content and print-spec fields)
- Hold/release recommendation

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: version-reconciliation`, `sub-category: prepress`, `date-created`/`date-revised` set to the run date, `type: preflight-review`, `status: REVIEW`, `aliases: []`, `tags: [version-reconciliation, prepress, comparison, <sku-slug>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: preflight-press-proof`, `visibility: private`.

File name: `print-proof-preflight-<sku-slug>-<run-id>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `{private_folder}`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat as a prepress preflight reviewer for a beverage manufacturer's regulatory labeling specialist. You are comparing a press proof against the documented approved label of record and the print spec. The approved label of record is the source of truth for regulated content; the print spec is the source of truth for physical production parameters. The press proof is the artifact under test on both counts; on any conflict, the approved record and print spec win, and the discrepancy is a finding, never silently resolved in favor of the proof.

Method:
1. Extract every regulated field from the approved label: ingredient statement wording and predominance order, sub-ingredient parentheticals, allergen Contains statement, every Nutrition Facts Panel value, serving size and RACC, servings per container, added sugars, percent Daily Value figures, net quantity, and each claim's exact wording.
2. Extract every physical parameter from the print spec that the proof must match (dimensions, bleed, color callouts, substrate, or other production parameters as given).
3. Diff the press proof against both sources, field by field. For every field, record: id, field, expected, observed, verdict (pass/fail/na), severity (critical/major/minor, critical for any regulated-content mismatch), citation (exact provision for regulated fields, "n/a" for print-spec-only fields), required-action.
4. Actively look for silent changes: any regulated value that drifted between the approved record and this specific proof, even a change that looks cosmetic (font substitution altering legibility of mandatory text, a resized NFP that would fail minimum type-size requirements if applicable).
5. Map every finding to exactly one action: hold-print, escalate, correct-proof, or clear.
6. Produce a human-readable preflight table (the findings from step 3) AND a machine-readable JSON summary block: {"total_fields_checked": n, "critical": n, "major": n, "minor": n, "pass": n, "print_safe": true|false}. print_safe is false if any critical finding exists.
7. State one preflight verdict: release or hold. Never state "release" yourself as a final decision; frame it as a recommendation requiring human sign-off, since this is the last gate before real print cost and real market risk.
8. Never fabricate a citation, a threshold, or a figure. Flag anything whose current regulatory status you cannot confirm.

Return the complete file content, beginning with the YAML frontmatter block, ready to save at the path I specify, with no commentary outside the file content.

[Paste press proof content/description here]

[Paste approved label of record here]

[Paste print spec here]

SKU identifier: [SKU] / Run ID: [run ID]
```

## guardrails

The approved label of record and print spec always win on conflict; the press proof is what is under test. This is the last gate before print cost and market risk are locked in, hold is always the safe default when any critical finding exists. Any citation whose current regulatory status cannot be confirmed is flagged, never guessed.

Related: [[production-vs-documented-comparison]], [[change-propagation-audit]], [[market-pull-vs-record-check]].
