---
domain: regulatory-ingredients-labels-laws
category: market-and-reporting
sub-category: market-and-reporting
date-created: 2026-07-22
date-revised: 2026-07-22
type: index
status: DONE
aliases: []
tags:
  - market-and-reporting
  - regulatory-labeling
topic: beverage-label-compliance
use-case: browse-market-and-reporting-prompts
visibility: private
---

# market-and-reporting

Checking an in-market label against the approved record after it has already shipped, and rolling the labeling function's findings into a weekly status report. The in-market check is the last-resort comparison in the drift-detection family: it catches drift that already reached consumers, after the earlier checks in version-reconciliation/.

Copilot does not fetch market data: a person collects every pull (shelf photo, sample, transcription, consumer complaint) and attaches or pastes it. Web-grounded Copilot answers about in-market products are unreliable and tenant-dependent and must never feed a finding.

## prompts

- [[market-pull-vs-record-check]], compare an in-market label against the approved record (surveillance)
- [[weekly-status-report]], roll in-progress items, findings, deadlines, and incidents into a categorized weekly status report (status-reporting)

## workflow

1. A person pulls an in-market label (shelf audit, sample, consumer photo) and records SKU, lot or date code, pull date and location.
2. Run [[market-pull-vs-record-check]] against the approved record in force at the sample's production date; save the dated output to `projects/regulatory-labeling/`.
3. Any critical finding escalates immediately to a human decision-maker (health-hazard evaluation, recall classification, Reportable Food Registry assessment); everything else lands in the findings log.
4. Weekly, run [[weekly-status-report]] over the in-progress items, findings log, deadlines, and incidents; the report feeds stakeholder updates and next week's priorities.

Up: [[regulatory-labeling]]

![[bases/market-and-reporting.base]]
