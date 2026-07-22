---
domain: regulatory-ingredients-labels-laws
category: market-and-reporting
sub-category: status-reporting
types:
  - prompt
date-created: 2026-07-22
date-revised: 2026-07-22
status: DONE
topic: beverage-label-compliance
use-case: generate-weekly-status-report
visibility: private
aliases:
  - blockers and decisions needed
  - labeling status update
  - open incidents this week
  - review findings summary
  - stakeholder status report
  - upcoming deadlines report
  - weekly rollup for stakeholders
  - weekly status report
tags:
  - market-and-reporting
  - regulatory-labeling
  - status-reporting
---

# weekly-status-report

## prompt-summary

Rolls up the labeling function's week into a categorized status report from your own inputs: in-progress items, a findings log, deadlines, and incidents. Reach for it weekly, or whenever you need a single status view across active SKUs, reviews, and open incidents for a stakeholder update. It is a synthesis prompt, not a compliance judgment: it never resolves an open decision or invents a fact, it organizes what the inputs already say and surfaces the rest for a human to decide.

## use-cases

- The weekly stakeholder update is due and you need a structured report across active SKUs, reviews, and open incidents.
- You have in-progress items, a findings log, deadlines, and incidents to synthesize into clear sections without inventing any fact not present in the inputs.
- You need findings grouped by severity, blockers flagged with what they are waiting on, and open decisions listed for a human to make.
- Upcoming deadlines must be laid out in date order with any missed deadline flagged.
- Incidents escalated this period need to be reported with their current disposition, each in-progress item grouped under exactly one library category.

## expected-outputs

- Structured report with frontmatter, sections, blockers, and decisions needed

## prompt

```
You are running inside Microsoft 365 Copilot Chat. Your single task: generate a categorized weekly status report for the labeling function from the inputs I provide.

You should have these inputs: (1) the reporting period as week start and week end dates, (2) in-progress items, (3) the findings log, (4) deadlines, (5) incidents. If any input is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Source of truth: the in-progress items, findings log, deadlines, and incidents I provide are the only sources. Do not add a date, a status, or a fact not present in them.

Method:
1. Read the in-progress items, findings log, deadlines, and incidents I provide below, scoped to the stated reporting period.
2. Organize into sections: In Progress (active SKU/label work with current status), Findings This Week (summarized from the findings log, grouped by severity), Blockers (anything stalled, with what it is waiting on), Decisions Needed (open items requiring a human decision this week, each with who needs to decide and by when if stated), Upcoming Deadlines (from the deadlines input, in date order, flagging any missed deadline), Incidents (anything escalated this period, with current disposition).
3. Within In Progress, group every item under exactly one library category: label-intake, content-derivation, claims-compliance, review-and-verification, version-reconciliation, market-and-reporting, communication-email, or other. Use other for anything that fits none of these; never invent a new category.
4. Severity scale for grouped findings: critical = blocks use or shipment, major = must fix before sign-off, minor = fix when convenient. Report severities exactly as the findings log states them; do not re-grade.
5. Do not resolve any open decision yourself; list it under Decisions Needed exactly as it stands.
6. Do not fabricate a deadline, a finding, a status, or an incident detail not present in the inputs. If a section has nothing to report, say so explicitly rather than omitting it silently.
7. Where a finding references a regulatory provision, carry the citation through into the report exactly as given, marked UNVERIFIED; never add, complete, or correct a provision yourself. A compliance claim in a status item is repeated with its citation, never restated as settled fact.

This is a reporting and synthesis prompt, not a compliance judgment; it never resolves an open decision, it surfaces it for the reader.

[Paste in-progress items here]

[Paste findings log here]

[Paste deadlines here]

[Paste incidents here]

Reporting period: [week start yyyy-MM-dd] to [week end yyyy-MM-dd]

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: market-and-reporting
sub-category: status-reporting
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: status-report
status: REVIEW
aliases: []
tags:
  - market-and-reporting
  - status-reporting
  - weekly
topic: beverage-label-compliance
use-case: weekly-status-report
visibility: private
---
2. An H1 equal to the output file name without .md: weekly-status-report-<yyyy-MM-dd>, using the week-ending date
3. The body specified in the method above.
4. This exact final line:
UNVERIFIED DRAFT - requires review and sign-off by the regulatory labeling specialist; citations unconfirmed against current eCFR.
```

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Have these inputs ready: the reporting period (week start and week end dates; the week-ending date names the output file), the in-progress items (current SKU/label work), the findings log (recent review, checklist, or comparison findings), the deadlines (upcoming dates), and the incidents (anything escalated this period). Attach them with the paperclip or a `/` file reference (files must be in OneDrive or SharePoint); paste text directly when a file cannot be attached, or combine the four inputs into one document if attachment limits bite.
3. Copy the entire prompt block above, paste it into the chat, and fill every bracketed placeholder (the four inputs plus the week start and end dates) before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `weekly-status-report-<yyyy-MM-dd>.md` where the date is the week-ending date (kebab-case, H1 equal to the file-name stem, so each week's report never overwrites the last) in `projects/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder).
5. Review the output yourself. Nothing is final until a person signs off.

## guardrails

This prompt never resolves an open decision on the specialist's behalf; every item under Decisions Needed stays open until a human decides. No fact, date, figure, or status is invented beyond what the inputs state. A status report is not a compliance verdict: carried citations stay marked UNVERIFIED and items are grouped only under the listed library categories or other, never an invented category.

Related: [[market-pull-vs-record-check]], [[checklist-template-evaluation]], [[second-eyes-hitl-review]] (common upstream sources for the findings log, in review-and-verification/).
