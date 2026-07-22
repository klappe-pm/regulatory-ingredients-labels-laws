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

Determines eligibility to use "healthy" and related implied nutrient content claims against 21 CFR 101.65(d)(2)-(3) as amended by the December 19, 2024 final rule, using NFP values, formula, RACC, and food-group-equivalent amounts. Plain water and plain carbonated water automatically qualify under the updated rule.

## when-to-use

A claim scoped as an implied nutrient content claim in [[claims-target-scoping]] includes "healthy" or similar wording, or any time the specialist wants to test eligibility before using such a claim.

## what-to-use-for

Testing NFP values, formula composition, and per-RACC food-group-equivalent amounts against the current FDA "healthy" implied-claim criteria under 21 CFR 101.65(d), producing an eligibility verdict and gaps.

## required-inputs

- NFP values (including added sugars, sodium, and saturated fat)
- Formula
- Serving size and RACC (21 CFR 101.12)
- Per-RACC food-group-equivalent amounts (fruit, vegetable, dairy, grain, and protein-food contributions)

## expected-outputs

- Eligibility verdict against current criteria
- Gaps (what would need to change to become eligible, if not currently eligible)
- Citation, marked UNVERIFIED until confirmed against the current eCFR, with the applicable regime (pre-2024 or updated) stated

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Attach the NFP values and formula with the paperclip or a `/` file reference (files must be in OneDrive or SharePoint); paste the serving size, RACC, and food-group-equivalent amounts directly when a file cannot be attached.
3. Copy the entire prompt-text block below, paste it into the chat, and fill every bracketed placeholder before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `healthy-claim-eligibility-<sku-slug>.md` in `projects/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder).
5. Review the output yourself. Nothing is final until a person signs off.

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: claims-compliance`, `sub-category: claims`, `date-created`/`date-revised` set to the run date, `type: claim-review`, `status: REVIEW`, `aliases: []`, `tags: [claims-compliance, claims, <sku-slug>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: healthy-claim-eligibility`, `visibility: private`.

File name: `healthy-claim-eligibility-<sku-slug>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `projects/regulatory-labeling/`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: determine eligibility to use "healthy" and related implied nutrient content claims.

You should have these inputs: (1) NFP values including added sugars, sodium, and saturated fat, (2) formula, (3) serving size and RACC, (4) per-RACC food-group-equivalent amounts, (5) SKU identifier. If any input is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Source of truth: the NFP values, formula, and food-group-equivalent amounts I provide are the artifacts under test. The governing framework is the "healthy" implied nutrient content claim definition at 21 CFR 101.65(d)(2)-(3) as amended by FDA's final rule of December 19, 2024 (89 FR 106064), effective February 25, 2025, with a compliance date of February 25, 2028; until the compliance date both the prior and the updated definitions are in play. Treat every date, threshold, and criterion in this prompt as UNVERIFIED: the specialist must confirm the current effective rule text and compliance status before relying on this verdict.

Method:
1. Read the NFP values, formula, serving size/RACC, and food-group-equivalent amounts I provide below.
2. Branch first: if the SKU is plain water or plain carbonated water, it automatically qualifies for "healthy" under the updated rule (UNVERIFIED, confirm against 101.65(d)); confirm the formula contains no disqualifying added ingredients, then stop and report the verdict with that basis.
3. Otherwise state the criteria you are applying under the updated framework: the food-group-equivalent requirement for the applicable product category plus limits on added sugars, sodium, and saturated fat expressed per RACC (the prior rule's beneficial-nutrient minimum, e.g. 10% DV, was removed by the 2024 rule; all UNVERIFIED). State which regime (prior, updated, or both) you are testing against and test both where they diverge before the compliance date.
4. Test the product against each required criterion field by field using the per-RACC values.
5. Produce an eligibility verdict: eligible, not eligible, or cannot determine (if a required input is missing or a criterion cannot be verified).
6. For each failing or indeterminate criterion, state the gap: what value would need to change, and by how much, to become eligible.
7. Produce a findings table: id, field (criterion), expected (criterion value, marked UNVERIFIED), observed (NFP/formula/food-group value), verdict, severity, citation (marked UNVERIFIED), required-action. One row per criterion, including passing criteria. Close with the attestation line: "Criteria tested: N of N; skipped: none."
8. Produce an aggregate disposition with a blocking-issues list.

Citation discipline: use only the provisions listed in this prompt. Never invent a provision, subsection, or threshold. Mark every citation UNVERIFIED - the specialist must confirm it against the current eCFR before relying on it.

Verdict vocabulary: pass (criterion met), fail (criterion not met), na (criterion not applicable to this product category), unable-to-verify (input unreadable or criterion uncheckable; never guess and never silently omit). Aggregate disposition: no-findings-pending-human-review, findings-require-action, or blocked.

Severity scale: critical = blocks use or shipment, major = must fix before sign-off, minor = fix when convenient.

This is an independent second set of eyes; it never marks the claim cleared for use without the specialist confirming the current rule text and compliance date.

Do not fabricate a threshold, compliance date, or criterion, and do not present a superseded threshold as current without flagging the uncertainty.

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: claims-compliance
sub-category: claims
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: claim-review
status: REVIEW
aliases: []
tags:
  - claims-compliance
  - claims
  - [SKU-SLUG]
topic: beverage-label-compliance
use-case: healthy-claim-eligibility
visibility: private
---
2. An H1 equal to the output file name without .md: healthy-claim-eligibility-[SKU-SLUG]
3. The body specified in the method above.
4. This exact final line:
UNVERIFIED DRAFT - requires review and sign-off by the regulatory labeling specialist; citations unconfirmed against current eCFR.

[Paste NFP values here, including added sugars, sodium, and saturated fat]

[Paste formula here]

Serving size and RACC: [serving size and RACC]

Per-RACC food-group-equivalent amounts: [fruit, vegetable, dairy, grain, protein-food contributions per RACC]

SKU identifier: [SKU]
```

## guardrails

Human-in-the-loop: this prompt never confirms current-rule status on its own; the specialist must verify the effective "healthy" definition (21 CFR 101.65(d) as amended, 89 FR 106064) and the February 25, 2028 compliance date before use. The plain-water automatic qualification still requires the specialist to confirm no disqualifying added ingredients. Escalate any borderline result to [[nutrient-content-claim-review]] for a second look at the underlying NFP values.

Related: [[nutrient-content-claim-review]], [[prohibited-and-misleading-claim-screen]].
