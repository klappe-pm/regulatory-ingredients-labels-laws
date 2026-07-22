---
domain: regulatory-ingredients-labels-laws
category: content-derivation
sub-category: nutrition-facts-panel
date-created: 2026-07-22
date-revised: 2026-07-22
type: prompt
status: DONE
aliases: []
tags:
  - content-derivation
  - nutrition-facts-panel
  - regulatory-labeling
topic: beverage-label-compliance
use-case: verify-nfp-rounding
visibility: private
---

# nutrition-facts-panel-rounding-check

## description

Verifies FDA rounding rules and %DV computation on every value in a draft Nutrition Facts Panel, producing a per-value verdict and corrected values where needed.

## when-to-use

After [[nutrition-facts-panel-buildout]] has produced a draft NFP, or whenever draft NFP values change and need re-verification before print.

## what-to-use-for

Checking each declared NFP value against the applicable FDA rounding rule and recomputing %DV against the stated DV basis, flagging any value that was rounded or computed incorrectly.

## required-inputs

- Draft NFP values (as currently drafted)
- DV basis used (which Daily Value table/version)

## expected-outputs

- Per-value rounding verdicts (pass/fail/na)
- Corrected values where a fail is found
- Citations for each rounding rule applied

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: content-derivation`, `sub-category: nutrition-facts-panel`, `date-created`/`date-revised` set to the run date, `type: nfp-rounding-review`, `status: REVIEW`, `aliases: []`, `tags: [content-derivation, nutrition-facts-panel, <sku-slug>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: nfp-rounding-review`, `visibility: private`.

File name: `nfp-rounding-review-<sku-slug>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `{private_folder}`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: verify rounding and %DV on every value in a draft Nutrition Facts Panel.

Source of truth: the draft NFP values and the stated DV basis I provide are what is under test; the FDA rounding rules in 21 CFR 101.9 are the standard they are tested against. A mismatch between the draft value and the correctly rounded value is a finding, not a judgment call.

Method:
1. Read the draft NFP values and the DV basis I provide below.
2. For each declared nutrient, identify the FDA rounding rule that applies to its value range (per 21 CFR 101.9) and compute the correctly rounded value from the underlying test data if provided, or re-derive the expected rounding behavior from the declared value if raw data is not given.
3. Recompute %DV for each nutrient against the stated DV basis; flag if the DV basis itself cannot be confirmed current.
4. Produce a findings table with columns: id, field (the nutrient), expected (correctly rounded value/%DV), observed (the draft value/%DV), verdict (pass/fail/na), severity (critical/major/minor), citation (the exact rounding provision), required-action.
5. Produce an aggregate disposition: pass, conditional-pass, or fail, with an explicit list of blocking issues (any fail-severity critical or major finding).

Cite 21 CFR 101.9 for every rounding rule applied. If you cannot confirm the current rounding table or DV values are current, flag it explicitly as a finding rather than asserting correctness.

This is an independent verification pass supporting a human reviewer. It never marks the NFP approved; it produces findings and a disposition for a human to act on.

Do not fabricate a rounding rule, a corrected value, or a %DV figure not derivable from the data and rules provided. Flag anything you cannot resolve from the given data.

Return the complete file content, beginning with the YAML frontmatter block, ready to save at the path I specify, with no commentary outside the file content.

[Paste draft NFP values here]

DV basis: [DV basis / table version]

SKU identifier: [SKU]
```

## guardrails

Human-in-the-loop: findings and disposition support a human sign-off; this prompt never marks the NFP print-ready on its own. Any critical or major finding blocks disposition until corrected and re-checked.

Related: [[nutrition-facts-panel-buildout]].
