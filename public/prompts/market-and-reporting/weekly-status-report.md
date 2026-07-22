---
domain: regulatory-ingredients-labels-laws
category: market-and-reporting
sub-category: status-reporting
date-created: 2026-07-22
date-revised: 2026-07-22
type: prompt
status: DONE
aliases: []
tags:
  - market-and-reporting
  - status-reporting
  - regulatory-labeling
topic: beverage-label-compliance
use-case: generate-weekly-status-report
visibility: private
---

# weekly-status-report

## description

Generates a categorized weekly status report for the labeling function from in-progress items, a findings log, deadlines, and incidents.

## when-to-use

Weekly, or whenever the specialist needs a rolled-up status view across active SKUs, reviews, and open incidents for a stakeholder update.

## what-to-use-for

Synthesizing in-progress items, findings, deadlines, and incidents into a structured report with clear sections, without inventing any fact not present in the inputs.

## required-inputs

- In-progress items (current SKU/label work)
- Findings log (recent review, checklist, or comparison findings)
- Deadlines (upcoming dates)
- Incidents (anything escalated this period)

## expected-outputs

- Structured report with frontmatter, sections, blockers, and decisions needed

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: market-and-reporting`, `sub-category: status-reporting`, `date-created`/`date-revised` set to the report date, `type: status-report`, `status: DONE`, `aliases: []`, `tags: [market-and-reporting, status-reporting, weekly]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: weekly-status-report`, `visibility: private`.

File name: `weekly-status-report-<yyyy-MM-dd>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `{private_folder}`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: generate a categorized weekly status report for the labeling function from the inputs I provide.

Source of truth: the in-progress items, findings log, deadlines, and incidents I provide are the only sources. Do not add a date, a status, or a fact not present in them.

Method:
1. Read the in-progress items, findings log, deadlines, and incidents I provide below.
2. Organize into sections: In Progress (active SKU/label work with current status), Findings This Week (summarized from the findings log, grouped by severity), Blockers (anything stalled, with what it is waiting on), Decisions Needed (open items requiring a human decision this week, each with who needs to decide and by when if stated), Upcoming Deadlines (from the deadlines input, in date order), Incidents (anything escalated this period, with current disposition).
3. Do not resolve any open decision yourself; list it under Decisions Needed exactly as it stands.
4. Do not fabricate a deadline, a finding, or an incident detail not present in the inputs. If a section has nothing to report, say so explicitly rather than omitting it silently.
5. Where a finding references a regulatory provision, carry the citation through into the report rather than dropping it.

This is a reporting and synthesis prompt, not a compliance judgment; it never resolves an open decision, it surfaces it for the reader.

Return the complete file content, beginning with the YAML frontmatter block, ready to save at the path I specify, with no commentary outside the file content.

[Paste in-progress items here]

[Paste findings log here]

[Paste deadlines here]

[Paste incidents here]

Report week of: [date]
```

## guardrails

This prompt never resolves an open decision on the specialist's behalf; every item under Decisions Needed stays open until a human decides. No fact, date, or figure is invented beyond what the inputs state.

Related: [[market-pull-vs-record-check]], [[checklist-template-evaluation]], [[second-eyes-hitl-review]] (common upstream sources for the findings log, in review-and-verification/).
