---
domain: regulatory-ingredients-labels-laws
category: plan
sub-category: visualization
date-created: 2026-06-22
date-revised: 2026-06-22
type: design
version: 0.1.0
status: DRAFT
aliases:
  - regwatch visualization ideas
tags:
  - dashboard
  - regwatch
  - reporting
  - visualization
---

# regwatch-reporting-visualization-ideas

Reporting and visualization ideas to develop on top of the records database. All
of these read from the `export` output, so none requires new data, only a view.

## What This Covers

Concrete chart and dashboard ideas that turn the normalized records into a
picture a team can scan, ordered roughly by value for the beverage business.

## Visualizations Worth Building

### Deadline Timeline

A horizontal timeline of `effective_date` across obligations, so the team sees
what is coming due and when at a glance. The nearest items (California AB 660 in
2026, the dye phase-out, AB 418 in 2027) anchor the near term.

### Topic and Jurisdiction Heatmap

A grid of topic against jurisdiction, shaded by how many obligations sit in each
cell. It shows where a theme (say synthetic colors) has spread across the state
patchwork and where the federal pressure concentrates.

### Impact Matrix by Product

A grid of Talking Rain products against obligations, shaded by impact severity
from the impact analysis. It answers, in one view, which products carry the most
exposure and which obligations touch the most products.

### Status Funnel

A simple funnel from proposed to enacted to in-force per topic, to show momentum
and flag where a watch item is about to become a hard requirement.

## Tooling Options

- A small standard-library script that emits an SVG or an HTML table straight
  from the export, keeping the no-dependency rule.
- The CSV loaded into a spreadsheet or a business-intelligence tool for an
  interactive dashboard.
- A generated diagram (for example a timeline or a flow) for embedding in the
  briefing or the newsletter.

## Data Source

Every view reads `regwatch export` output (CSV and JSON). Adding the change-event
and per-product tables from the data-model sketch unlocks trend and exposure
views over time.

## Next Steps

- Pick the one or two views the team most wants and prototype them from the
  export.
- Decide whether visuals live in the briefing, the newsletter, or a separate
  dashboard.
