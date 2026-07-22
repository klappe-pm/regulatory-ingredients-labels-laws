---
domain: regulatory-ingredients-labels-laws
category: claims-compliance
sub-category: claims
date-created: 2026-07-22
date-revised: 2026-07-22
type: prompt
status: DONE
aliases: []
tags:
  - claims-compliance
  - claims
  - regulatory-labeling
topic: beverage-label-compliance
use-case: check-healthy-claim-eligibility
visibility: private
---

# healthy-claim-eligibility-check

## description

Determines eligibility to use "healthy" and related implied nutrient content claims against current FDA criteria, using NFP values and the formula.

## when-to-use

A claim scoped as an implied nutrient content claim in [[claims-target-scoping]] includes "healthy" or similar wording, or any time the specialist wants to test eligibility before using such a claim.

## what-to-use-for

Testing NFP values and formula composition against the current FDA "healthy" implied-claim criteria under 21 CFR 101.65, producing an eligibility verdict and gaps.

## required-inputs

- NFP values
- Formula

## expected-outputs

- Eligibility verdict against current criteria
- Gaps (what would need to change to become eligible, if not currently eligible)
- Citation

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: claims-compliance`, `sub-category: claims`, `date-created`/`date-revised` set to the run date, `type: claim-review`, `status: REVIEW`, `aliases: []`, `tags: [claims-compliance, claims, <sku-slug>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: healthy-claim-eligibility`, `visibility: private`.

File name: `healthy-claim-eligibility-<sku-slug>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `{private_folder}`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: determine eligibility to use "healthy" and related implied nutrient content claims.

Source of truth: the NFP values and formula I provide are the artifacts under test. FDA's "healthy" implied nutrient content claim definition under 21 CFR 101.65 has been the subject of an active rulemaking update; you must explicitly state which version of the criteria you are applying and flag that the specialist must confirm the current effective definition and compliance date before relying on this verdict, rather than assuming a fixed threshold is still current.

Method:
1. Read the NFP values and formula I provide below.
2. Identify the applicable food-category-specific criteria for "healthy" eligibility (beverages have their own thresholds distinct from solid foods), stating the category you are applying.
3. Test the product against each required criterion (for example: added sugars limit, sodium limit, saturated fat limit, and any food-group or nutrient-density requirement that applies to beverages under the current definition).
4. Produce an eligibility verdict: eligible, not eligible, or cannot determine (if a required input is missing).
5. For each failing or indeterminate criterion, state the gap: what value would need to change, and by how much, to become eligible.
6. Produce an aggregate disposition (pass/conditional-pass/fail) with a blocking-issues list.

Cite 21 CFR 101.65 and flag explicitly that FDA updated the "healthy" claim criteria and that compliance dates and exact thresholds must be verified against the current effective rule rather than an older or superseded threshold.

This is an independent second set of eyes; it never marks the claim cleared for use without the specialist confirming the current rule text and compliance date.

Do not fabricate a threshold, compliance date, or criterion not grounded in the current rule as best you can determine, and do not present a superseded threshold as current without flagging the uncertainty.

Return the complete file content, beginning with the YAML frontmatter block, ready to save at the path I specify, with no commentary outside the file content.

[Paste NFP values here]

[Paste formula here]

SKU identifier: [SKU]
```

## guardrails

Human-in-the-loop: this prompt never confirms current-rule status on its own; the specialist must verify the effective "healthy" definition and compliance date before use. Escalate any borderline result to [[nutrient-content-claim-review]] for a second look at the underlying NFP values.

Related: [[nutrient-content-claim-review]], [[prohibited-and-misleading-claim-screen]].
