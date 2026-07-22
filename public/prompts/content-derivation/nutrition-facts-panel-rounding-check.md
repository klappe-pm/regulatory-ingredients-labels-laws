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

Verifies FDA rounding rules and %DV computation on every value in a draft Nutrition Facts Panel against the rounding increments embedded in the prompt, quoting the applied increment and showing the computation before each verdict.

## when-to-use

After [[nutrition-facts-panel-buildout]] has produced a draft NFP, or whenever draft NFP values change and need re-verification before print.

## what-to-use-for

Checking each declared NFP value against its embedded 21 CFR 101.9(c) rounding increment and recomputing %DV against the supplied DV basis, flagging any value that was rounded or computed incorrectly.

## required-inputs

- Draft NFP values (as currently drafted)
- DV basis used (which Daily Value table/version, with its values)
- Unrounded underlying nutrient data, if available

## expected-outputs

- Findings table with one row per declared nutrient, including pass rows, and the attestation line "Fields compared: N of N; skipped: none"
- Per-value verdicts (pass, fail, na, unable-to-verify), each preceded by the quoted increment, the unrounded value, and the computation
- Corrected values where a fail is found
- Aggregate disposition (no-findings-pending-human-review, findings-require-action, or blocked) with a blocking-issues list
- Citations for each rounding rule applied

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Have the draft NFP values, the DV basis (with its values), and, if available, the unrounded nutrient data ready; attach them with the paperclip or a `/` file reference (files must be in OneDrive or SharePoint), or paste each into its placeholder when a file cannot be attached.
3. Copy the entire prompt-text block below, paste it into the chat, and fill every bracketed placeholder before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `nfp-rounding-review-<sku-slug>.md` in `projects/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder).
5. Review the output yourself. Nothing is final until a person signs off.

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: content-derivation`, `sub-category: nutrition-facts-panel`, `date-created`/`date-revised` set to the run date, `type: nfp-rounding-review`, `status: REVIEW`, `aliases: []`, `tags: [content-derivation, nutrition-facts-panel, <sku-slug>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: nfp-rounding-review`, `visibility: private`.

File name: `nfp-rounding-review-<sku-slug>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `projects/regulatory-labeling/`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: verify rounding and %DV on every value in a draft Nutrition Facts Panel.

You should have these inputs: (1) the draft NFP values as currently drafted, (2) the DV basis in use (which Daily Value table/version, with its values), (3) if available, the unrounded underlying nutrient data. If input (1) or (2) is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input; in particular, never recall a DV value or a rounding increment from memory.

Source of truth: the draft NFP values and the stated DV basis I provide are what is under test; the rounding increments quoted in this prompt are the standard they are tested against. A mismatch between the draft value and the correctly rounded value is a finding, not a judgment call.

Rounding increments to apply (quote the applicable one before each verdict; use no increment not listed here):
- Calories, 21 CFR 101.9(c)(1): under 5 express as 0; 50 or less round to the nearest 5; above 50 round to the nearest 10.
- Total fat, 21 CFR 101.9(c)(2): under 0.5 g express as 0; under 5 g round to the nearest 0.5 g; 5 g and above round to the nearest 1 g.
- Sodium, 21 CFR 101.9(c)(4): under 5 mg express as 0; 5 to 140 mg round to the nearest 5 mg; above 140 mg round to the nearest 10 mg.
- Total carbohydrate, 21 CFR 101.9(c)(6): under 0.5 g express as 0; under 1 g may state "less than 1 g"; otherwise round to the nearest 1 g.
- Total sugars and added sugars, 21 CFR 101.9(c)(6)(ii)-(iii): under 0.5 g express as 0; under 1 g may state "less than 1 g"; otherwise round to the nearest 1 g.
- Protein, 21 CFR 101.9(c)(7): under 0.5 g express as 0; under 1 g may state "less than 1 g"; otherwise round to the nearest 1 g.
- Any other declared nutrient: its increment is not embedded in this prompt; mark its rounding verdict unable-to-verify and say so. Never improvise an increment.

Method:
1. Read the draft NFP values, the DV basis, and any unrounded data I provide below.
2. For each declared nutrient, quote the applicable increment from the list above, state the unrounded value (from the underlying data if provided; otherwise state that no unrounded value was supplied), show the rounding computation step by step, then give the verdict. When no unrounded value is supplied, verify only that the declared value is expressible under the applicable increment and mark full verification unable-to-verify.
3. Recompute %DV for each nutrient against the supplied DV basis, showing the division for each. If a nutrient's DV is not among the supplied values, mark its %DV unable-to-verify instead of recalling one.
4. Produce a findings table with one row per declared nutrient, including pass rows, with columns: id, field (the nutrient), expected (correctly rounded value/%DV), observed (the draft value/%DV), verdict, severity, citation (the exact provision from the list above), required-action. Verdicts: pass (draft matches the correctly rounded value), fail (mismatch), na (not applicable), unable-to-verify (missing unrounded data, missing DV, or increment not embedded here; never a guess or a silent omission). Severity: critical (blocks use or shipment), major (must fix before sign-off), minor (fix when convenient). Close the table with this attestation line: "Fields compared: N of N; skipped: none", where N is the number of declared nutrients.
5. Produce an aggregate disposition: no-findings-pending-human-review (every row pass or na), findings-require-action (any fail), or blocked (any unable-to-verify on a required input), with an explicit list of blocking issues (every critical or major fail).

Citations: use only the provisions listed in this prompt (21 CFR 101.9(c)(1), (c)(2), (c)(4), (c)(6), (c)(6)(ii)-(iii), and (c)(7)). Never invent a provision, subsection, or threshold. Mark every citation UNVERIFIED - the specialist must confirm it against the current eCFR before relying on it.

This is an independent verification pass supporting a human reviewer. It never marks the NFP approved or print-ready; it produces findings and a disposition for a human to act on.

Do not fabricate a rounding rule, a corrected value, or a %DV figure not derivable from the data and increments provided. Mark anything you cannot resolve from the given data unable-to-verify.

[Paste draft NFP values here]

DV basis: [DV basis / table version and values]

[Paste unrounded nutrient data here, if available]

SKU identifier: [SKU]

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: content-derivation
sub-category: nutrition-facts-panel
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: nfp-rounding-review
status: REVIEW
aliases: []
tags:
  - content-derivation
  - nutrition-facts-panel
  - [SKU-SLUG]
topic: beverage-label-compliance
use-case: nfp-rounding-review
visibility: private
---
2. An H1 equal to the output file name without .md: nfp-rounding-review-<sku-slug>
3. The body specified in the method above.
4. This exact final line:
UNVERIFIED DRAFT - requires review and sign-off by the regulatory labeling specialist; citations unconfirmed against current eCFR.
```

## guardrails

Human-in-the-loop: findings and disposition support a human sign-off; this prompt never marks the NFP print-ready on its own. Any critical or major fail blocks disposition until corrected and re-checked. The rounding increments are embedded in the prompt so Copilot never recalls them from memory; the specialist confirms the embedded increments against the current eCFR before relying on a verdict.

Related: [[nutrition-facts-panel-buildout]].
