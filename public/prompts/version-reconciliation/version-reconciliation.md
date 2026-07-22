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

Catches drift between the documented approved label of record and what actually gets produced, propagated, or printed. Product development and regulatory iterate on formula and copy; changes are not always shared, so downstream labels can print and reach market incorrect. Every prompt here treats the approved label of record as the source of truth, diffs field by field, and maps findings to an action rather than resolving them itself.

## sub-categories

- [[reconciliation]]
- [[prepress]]

## prompts

- [[production-vs-documented-comparison]]
- [[change-propagation-audit]]
- [[print-proof-preflight]]

## see also

- [[regulatory-labeling]] (master index)
- [[market-pull-vs-record-check]], the fourth comparison prompt in the library

![[bases/version-reconciliation.base]]
