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
use-case: screen-prohibited-claims
visibility: private
---

# prohibited-and-misleading-claim-screen

## description

Screens marketing and label art copy for prohibited, implied-disease, or unsubstantiated claims, including unauthorized longevity claims, flagging severity and proposing safer alternatives.

## when-to-use

Any marketing copy or label art copy is drafted or revised and needs a screen before it is finalized, or a claim flagged as ambiguous by [[claims-target-scoping]], [[nutrient-content-claim-review]], or [[structure-function-claim-review]] needs a dedicated prohibited-claim assessment.

## what-to-use-for

Reading marketing copy and label art copy end to end to catch phrases that read as prohibited, implied-disease, or unsubstantiated claims that a claim-by-claim review might miss because they are not phrased as a discrete "claim."

## required-inputs

- Marketing copy
- Label art copy (all on-pack text)

## expected-outputs

- Flagged phrases
- Why each is prohibited or risky
- Severity
- Safer alternative phrasing

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: claims-compliance`, `sub-category: claims`, `date-created`/`date-revised` set to the run date, `type: claim-screen`, `status: REVIEW`, `aliases: []`, `tags: [claims-compliance, claims, <sku-slug>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: prohibited-claim-screen`, `visibility: private`.

File name: `prohibited-claim-screen-<sku-slug>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `{private_folder}`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: screen marketing and label art copy for prohibited, implied-disease, or unsubstantiated claims.

Source of truth: the marketing copy and label art copy I provide are the artifacts under test; FDA's misbranding and disease-claim framework is the standard.

Method:
1. Read every line of the marketing copy and label art copy I provide below, not just phrases pre-tagged as claims.
2. Flag any phrase that: implies treatment, cure, mitigation, or prevention of a disease without an authorized health claim (21 CFR 101.14/Subpart E) or drug approval; asserts an unsubstantiated longevity or anti-aging outcome; implies a nutrient content claim without meeting its definition (21 CFR 101.13); or is otherwise likely to mislead a reasonable consumer about the product's health effects or composition.
3. For each flagged phrase, state exactly why it is prohibited or risky, citing the specific provision (21 CFR 101.13, 101.14/Subpart E, 101.65, or general misbranding under the FD&C Act) or stating it is a longevity/disease-adjacent claim with no current authorized pathway.
4. Assign severity: critical (clearly prohibited, blocks release), major (high risk, needs legal/regulatory sign-off), minor (borderline, recommend softening).
5. Propose a safer alternative phrasing for each flagged item that preserves the marketing intent without the regulatory risk, where one exists; state plainly if no safe rewrite exists and the claim should be dropped.
6. Produce an aggregate disposition (pass/conditional-pass/fail) with a blocking-issues list of every critical item.

Cite the exact provision for every flag. If you cannot confirm current regulatory status of a cited provision, flag it explicitly rather than asserting it.

This is an independent second set of eyes; it never marks copy approved, and disagreement with a prior review (from [[nutrient-content-claim-review]], [[structure-function-claim-review]], or [[healthy-claim-eligibility-check]]) is a finding to surface, not to silently resolve.

Do not fabricate a legal risk, a provision, or a rewrite that is not a defensible reading of the copy and the cited framework. Flag anything genuinely ambiguous rather than asserting a verdict.

Return the complete file content, beginning with the YAML frontmatter block, ready to save at the path I specify, with no commentary outside the file content.

[Paste marketing copy here]

[Paste label art copy here]

SKU identifier: [SKU]
```

## guardrails

Human-in-the-loop: flags and severities support legal/regulatory sign-off; this prompt never approves copy. Every critical-severity flag is a blocking issue until resolved by a human.

Related: [[nutrient-content-claim-review]], [[structure-function-claim-review]], [[healthy-claim-eligibility-check]].
