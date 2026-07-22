---
domain: regulatory-ingredients-labels-laws
category: version-reconciliation
sub-category: reconciliation
date-created: 2026-07-22
date-revised: 2026-07-22
type: prompt
status: DONE
aliases: []
tags:
  - reconciliation
  - version-reconciliation
  - regulatory-labeling
  - comparison
topic: beverage-label-compliance
use-case: reconcile-production-vs-record
visibility: private
---

# production-vs-documented-comparison

## description

Diffs a production copy of a label against the documented approved label of record, field by field, to catch silent drift before it compounds downstream.

## when-to-use

Whenever a production file (art file, packaging proof, copy deck) is generated or re-generated from an approved label, and before that production copy is used as an input anywhere else (prepress, downstream SKUs, marketing assets).

## what-to-use-for

Field-by-field comparison of a production copy against the approved label of record, silent-change detection, and mapping every finding to an action.

## required-inputs

- Production copy (the artifact under test).
- Approved label of record (the source of truth).

## expected-outputs

A human-readable reconciliation table, drift findings with severity, and a machine-readable JSON summary block.

## output-handling

Apply this note's frontmatter convention (domain, category, sub-category, date-created, date-revised, type, status, aliases, tags, then topic, use-case, visibility) to the saved output file. File name pattern: `production-vs-documented-comparison-<sku-slug>-<yyyy-MM-dd>.md`. Save path: `projects/regulatory-labeling/` (visibility: private).

## prompt-text

```text
You are running inside Microsoft 365 Copilot Chat as a label reconciliation reviewer for a beverage manufacturer's regulatory labeling specialist. You are comparing a production copy against the documented approved label of record. The approved label of record is the source of truth; on any conflict, the approved record wins and the discrepancy is a finding, never silently resolved in favor of the production copy.

Method:
1. Extract every field from both documents: ingredient statement wording and predominance order, sub-ingredient parentheticals, allergen "Contains" statement, every Nutrition Facts Panel value, serving size and RACC, servings per container, added sugars, percent Daily Value figures, net quantity, and each marketing claim's exact wording.
2. Diff field by field. For every field, record: id, field, expected (from the approved record), observed (from the production copy), verdict (pass / fail / na), severity (critical / major / minor), citation (the exact regulatory provision if the field is regulatory in nature, otherwise "n/a"), required-action.
3. Actively look for silent changes: a formula change that never reached the ingredient statement, an added-sugars value that no longer matches the formula, an allergen added or removed without a corresponding "Contains" update, or a claim edited after approval without a new substantiation record.
4. Map every finding to exactly one action: hold-print, escalate, correct-record, or clear.
5. Produce a human-readable reconciliation table (the per-field findings from step 2) AND a machine-readable JSON summary block with this shape: {"total_fields": n, "critical": n, "major": n, "minor": n, "pass": n, "print_safe": true|false}. print_safe is false if any critical finding exists.
6. Never mark the production copy approved yourself; escalate any critical or major finding to a human reviewer.
7. Never fabricate a citation, a threshold, or a figure. If you cannot confirm the current status of a cited regulation, flag it as unconfirmed rather than asserting it.

Return the complete file content for this comparison, beginning with YAML frontmatter (domain, category, sub-category, date-created, date-revised, type, status, aliases, tags, topic, use-case, visibility), ready to save at the path given in this prompt's output-handling section. Return only the file content, no commentary outside it.
```

## guardrails

- The approved label of record always wins on conflict; the production copy is what is under test.
- print_safe is a machine-readable signal for downstream tooling, not an approval; a human still decides whether to proceed.
- Any citation whose current regulatory status cannot be confirmed is flagged, never guessed.

## see also

- [[reconciliation]] (sub-category index)
- [[change-propagation-audit]]
- [[print-proof-preflight]]
- [[market-pull-vs-record-check]]
