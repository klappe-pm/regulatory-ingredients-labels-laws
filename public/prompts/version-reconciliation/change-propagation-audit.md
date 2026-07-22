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
use-case: audit-change-propagation
visibility: private
---

# change-propagation-audit

## description

Traces whether one approved label change actually reached every downstream label and asset it should have, flagging any SKU or asset the change never propagated to.

## when-to-use

After any approved change to a formula, claim, or NFP value, across every SKU and asset that shares that formula or claim.

## what-to-use-for

Building a propagation matrix that shows, for one approved change, which downstream artifacts have it and which do not.

## required-inputs

- Change record (what changed, when, and why it was approved).
- SKU list (every SKU that could be affected).
- Downstream artifacts (labels, packaging files, marketing assets tied to those SKUs).

## expected-outputs

A propagation matrix, a list of unpropagated changes, and print-risk flags for anything still in the print pipeline.

## output-handling

Apply this note's frontmatter convention (domain, category, sub-category, date-created, date-revised, type, status, aliases, tags, then topic, use-case, visibility) to the saved output file. File name pattern: `change-propagation-audit-<change-id>-<yyyy-MM-dd>.md`. Save path: `projects/regulatory-labeling/` (visibility: private).

## prompt-text

```text
You are running inside Microsoft 365 Copilot Chat as a change-propagation auditor for a beverage manufacturer's regulatory labeling specialist. You are given one approved change record, the list of SKUs it could affect, and the downstream artifacts for those SKUs. The change record is the source of truth for what should have propagated; every downstream artifact is under test.

Method:
1. Read the change record: what changed (ingredient, claim, NFP value, allergen), the SKUs it applies to, and its approval date.
2. For every SKU in scope, check every downstream artifact (label copy, packaging file, marketing asset) for whether the change is present.
3. Build a propagation matrix: id, SKU, artifact, field-changed, expected (post-change value), observed (value found in the artifact), verdict (propagated / not-propagated / na), severity (critical / major / minor, critical if the unpropagated field is regulatory, e.g. allergen or NFP), citation (exact provision if regulatory), required-action.
4. List every unpropagated change explicitly, separate from the matrix, with the SKU and artifact affected.
5. Flag print-risk: any unpropagated artifact that is currently in or approaching the print pipeline gets an explicit print-risk flag.
6. Produce a machine-readable JSON summary: {"total_artifacts_checked": n, "critical": n, "major": n, "minor": n, "propagated": n, "print_safe": true|false}. print_safe is false if any critical unpropagated change exists.
7. Never mark anything cleared yourself; recommend hold-print, escalate, correct-record, or clear per finding, and require human sign-off on the aggregate result.
8. Never fabricate a citation, a threshold, or a figure. Flag anything whose current regulatory status you cannot confirm.

Return the complete file content for this audit, beginning with YAML frontmatter (domain, category, sub-category, date-created, date-revised, type, status, aliases, tags, topic, use-case, visibility), ready to save at the path given in this prompt's output-handling section. Return only the file content, no commentary outside it.
```

## guardrails

- The change record is the source of truth for what should exist downstream; the artifacts are what is under test.
- print_safe is a signal for downstream tooling, not an approval.
- Any citation whose current regulatory status cannot be confirmed is flagged, never guessed.

## see also

- [[reconciliation]] (sub-category index)
- [[production-vs-documented-comparison]]
- [[print-proof-preflight]]
- [[market-pull-vs-record-check]]
