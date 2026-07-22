---
domain: regulatory-ingredients-labels-laws
category: market-and-reporting
sub-category: surveillance
date-created: 2026-07-22
date-revised: 2026-07-22
type: prompt
status: DONE
aliases: []
tags:
  - market-and-reporting
  - surveillance
  - regulatory-labeling
  - comparison
topic: beverage-label-compliance
use-case: check-market-label-vs-record
visibility: private
---

# market-pull-vs-record-check

## description

Compares a label already in the market against the approved record, field by field, to catch drift that reached consumers and needs a recall or relabel decision, not just a print hold.

## when-to-use

A market pull sample, a consumer photo, or a routine shelf audit surfaces an in-market label that needs checking against the approved record of what should be on shelf.

## what-to-use-for

Field-by-field comparison of an in-market label against the approved record, silent-change detection, and escalation of any in-market discrepancy to a recall/relabel decision path.

## required-inputs

- In-market label (image or extracted text)
- Approved record (the source of truth)

## expected-outputs

- Discrepancy findings
- Severity
- Recall/relabel escalation flag
- Machine-readable summary

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: market-and-reporting`, `sub-category: surveillance`, `date-created`/`date-revised` set to the run date, `type: market-surveillance-review`, `status: REVIEW`, `aliases: []`, `tags: [market-and-reporting, surveillance, comparison, <sku-slug>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: market-pull-vs-record-check`, `visibility: private`.

File name: `market-pull-vs-record-<sku-slug>-<yyyy-MM-dd>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `{private_folder}`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat as a market surveillance reviewer for a beverage manufacturer's regulatory labeling specialist. You are comparing an in-market label against the documented approved record. The approved record is the source of truth; on any conflict, the approved record wins and the discrepancy is a finding, never silently resolved in favor of what is on shelf. This label already reached consumers, so findings here carry more weight than a pre-print check.

Method:
1. Extract every field from the in-market label and the approved record: ingredient statement wording and predominance order, sub-ingredient parentheticals, allergen Contains statement, every Nutrition Facts Panel value, serving size and RACC, servings per container, added sugars, percent Daily Value figures, net quantity, and each claim's exact wording.
2. Diff field by field. For every field, record: id, field, expected (approved record), observed (in-market label), verdict (pass/fail/na), severity (critical/major/minor), citation (exact provision if regulatory, otherwise "n/a"), required-action.
3. Actively look for silent changes: any regulated value that drifted between the approved record and what is actually on shelf.
4. Map every finding to exactly one action: recall-escalation, relabel, correct-record, or clear. Recall-escalation applies to any critical allergen or safety-relevant discrepancy already in consumers' hands; relabel applies to critical non-safety discrepancies; correct-record applies when the approved record itself is stale relative to a properly-approved change.
5. Produce a human-readable discrepancy table AND a machine-readable JSON summary block: {"total_fields": n, "critical": n, "major": n, "minor": n, "pass": n, "market_safe": true|false, "recall_escalation": true|false}. recall_escalation is true if any critical allergen or safety-relevant discrepancy is found.
6. Never mark the in-market label cleared yourself; any critical finding is an immediate escalation to a human decision-maker, given the product is already in consumers' hands.
7. Never fabricate a citation, a threshold, or a figure. Flag anything whose current regulatory status you cannot confirm.

Return the complete file content, beginning with the YAML frontmatter block, ready to save at the path I specify, with no commentary outside the file content.

[Paste in-market label image description/text here]

[Paste approved record here]

SKU identifier: [SKU]
```

## guardrails

The approved record always wins on conflict. Any critical finding here is an immediate human escalation, not a wait-for-next-cycle item, because the product is already in market. Never fabricate a recall recommendation without a critical, clearly-grounded finding.

Related: [[production-vs-documented-comparison]], [[change-propagation-audit]], [[print-proof-preflight]] (the same drift-detection family, run at earlier stages, in version-reconciliation/), [[weekly-status-report]].
