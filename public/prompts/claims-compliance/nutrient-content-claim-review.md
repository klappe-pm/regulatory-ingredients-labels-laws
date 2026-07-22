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
use-case: review-nutrient-content-claim
visibility: private
---

# nutrient-content-claim-review

## description

Tests nutrient content claims (e.g. "low sugar," "excellent source of vitamin C") against their FDA definition and disclosure triggers using the NFP values that support them.

## when-to-use

A claim has been scoped as a nutrient-content-claim pathway item in [[claims-target-scoping]], or any nutrient content claim needs review before label finalization.

## what-to-use-for

Testing claim text against 21 CFR 101.13/Subpart D definitions and 101.65 implied-claim rules, using the NFP values, and producing a per-claim verdict with required disclosures and a rewrite if the claim fails.

## required-inputs

- Claim text (exact wording)
- NFP values supporting the claim

## expected-outputs

- Per-claim verdict (pass/fail/na)
- Required disclosures (e.g. "see nutrition information for sodium content")
- Citation
- Rewrite suggestion if the claim fails

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: claims-compliance`, `sub-category: claims`, `date-created`/`date-revised` set to the run date, `type: claim-review`, `status: REVIEW`, `aliases: []`, `tags: [claims-compliance, claims, <sku-slug>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: nutrient-content-claim-review`, `visibility: private`.

File name: `nutrient-content-claim-review-<sku-slug>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `{private_folder}`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: test nutrient content claims against their FDA definition and disclosure triggers.

Source of truth: the NFP values I provide are authoritative for whether a claim's numeric threshold is met; the claim text under test is the artifact being checked against them.

Method:
1. Read each claim and the NFP values I provide below.
2. For each claim, identify the exact nutrient content claim definition it invokes (21 CFR 101.13 and Subpart D specific definitions, e.g. "low," "reduced," "excellent source," "good source," "high," or 101.65 implied claims).
3. Check the NFP value against the definition's numeric threshold.
4. Determine whether a disclosure is triggered (for example, a claim about one nutrient that requires a disclosure statement about a different nutrient present at a disqualifying level, per 21 CFR 101.13).
5. Produce a findings table: id, field (claim text), expected (the definitional threshold), observed (the actual NFP value), verdict (pass/fail/na), severity (critical/major/minor), citation (exact provision), required-action.
6. Produce an aggregate disposition (pass/conditional-pass/fail) with a blocking-issues list.
7. For any failing claim, propose a compliant rewrite or state that no compliant version of the claim is available at this nutrient level.

Cite the exact 21 CFR 101.13/Subpart D definition or 101.65 provision for every verdict. If you cannot confirm the current numeric threshold for a claim type, flag it explicitly rather than asserting a number.

This is an independent second set of eyes; it never marks a claim approved. Surface disqualifying-nutrient disclosure requirements even if the claim itself would otherwise pass.

Do not fabricate a threshold, an NFP value, or a disclosure requirement not grounded in the source data or in 21 CFR 101.13/101.65. Flag anything you cannot confirm.

Return the complete file content, beginning with the YAML frontmatter block, ready to save at the path I specify, with no commentary outside the file content.

[Paste claim text(s) here]

[Paste NFP values here]

SKU identifier: [SKU]
```

## guardrails

Human-in-the-loop: verdicts and rewrites support a human sign-off; this prompt never marks a claim compliant on its own. Escalate any claim bordering on an implied disease claim to [[prohibited-and-misleading-claim-screen]].

Related: [[structure-function-claim-review]], [[prohibited-and-misleading-claim-screen]], [[healthy-claim-eligibility-check]].
