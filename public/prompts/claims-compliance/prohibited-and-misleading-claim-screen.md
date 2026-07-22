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

Screens marketing and label art copy for prohibited, implied-disease, or unsubstantiated claims, including unauthorized longevity claims, flagging severity and proposing safer alternatives. Imagery is screened only through a written description; undescribed imagery is flagged for human review.

## when-to-use

Any marketing copy or label art copy is drafted or revised and needs a screen before it is finalized, or a claim flagged as ambiguous by [[claims-target-scoping]], [[nutrient-content-claim-review]], or [[structure-function-claim-review]] needs a dedicated prohibited-claim assessment.

## what-to-use-for

Reading marketing copy and label art copy end to end to catch phrases that read as prohibited, implied-disease, or unsubstantiated claims that a claim-by-claim review might miss because they are not phrased as a discrete "claim."

## required-inputs

- Marketing copy
- Label art copy (all on-pack text)
- Written description of label imagery (Copilot screens described imagery only; undescribed imagery needs human review)

## expected-outputs

- Flagged phrases
- Why each is prohibited or risky
- Severity
- Safer alternative phrasing
- List of imagery elements requiring human review

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Attach the marketing copy and label art copy with the paperclip or a `/` file reference (files must be in OneDrive or SharePoint); paste text directly when a file cannot be attached, and always paste the imagery description as text.
3. Copy the entire prompt-text block below, paste it into the chat, and fill every bracketed placeholder before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `prohibited-claim-screen-<sku-slug>.md` in `projects/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder).
5. Review the output yourself. Nothing is final until a person signs off.

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: claims-compliance`, `sub-category: claims`, `date-created`/`date-revised` set to the run date, `type: claim-screen`, `status: REVIEW`, `aliases: []`, `tags: [claims-compliance, claims, <sku-slug>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: prohibited-claim-screen`, `visibility: private`.

File name: `prohibited-claim-screen-<sku-slug>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `projects/regulatory-labeling/`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: screen marketing and label art copy for prohibited, implied-disease, or unsubstantiated claims.

You should have these inputs: (1) marketing copy, (2) label art copy (all on-pack text), (3) written description of label imagery, (4) SKU identifier. If any input is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Source of truth: the marketing copy, label art copy, and imagery description I provide are the artifacts under test; FDA's misbranding and disease-claim framework is the standard.

Method:
1. Read every line of the marketing copy, label art copy, and imagery description I provide below, not just phrases pre-tagged as claims.
2. Flag any phrase that is false or misleading on its face under FDCA 403(a)(1) (21 USC 343(a)(1)) and 21 CFR 1.21 (failure to reveal material facts), both UNVERIFIED.
3. Flag disease-related phrases with split routing: wording framed as disease risk reduction without an authorized health claim under 21 CFR 101.14/Subpart E (UNVERIFIED) is flagged for the health-claim pathway, which this screen does not grant; wording that implies treatment, cure, mitigation, or diagnosis of a disease is a per-se drug claim under FDCA 201(g) (UNVERIFIED), prohibited for a conventional beverage, with no authorization path.
4. Flag any phrase that implies a nutrient content claim without meeting its definition (21 CFR 101.13, 101.65, both UNVERIFIED), and any unsubstantiated longevity or anti-aging outcome, stating why it is unsubstantiated given the evidence provided or its absence.
5. For imagery, evaluate only claims implied by the written imagery description. List every imagery element that is not described or that you cannot evaluate with the flag "imagery requires human review"; never assert that undescribed imagery is clean.
6. For each flagged phrase, state exactly why it is prohibited or risky, citing the specific provision from the list above, and assign severity.
7. Propose a safer alternative phrasing for each flagged item that preserves the marketing intent without the regulatory risk, where one exists; state plainly if no safe rewrite exists and the claim should be dropped.
8. Produce an aggregate disposition with a blocking-issues list of every critical item. Close with the attestation line: "Inputs screened: marketing copy, label art copy, imagery description; skipped: none."

Citation discipline: use only the provisions listed in this prompt. Never invent a provision, subsection, or threshold. Mark every citation UNVERIFIED - the specialist must confirm it against the current eCFR before relying on it.

Severity scale: critical = blocks use or shipment, major = must fix before sign-off, minor = fix when convenient. Aggregate disposition: no-findings-pending-human-review, findings-require-action, or blocked.

This is an independent second set of eyes; it never marks copy approved, and disagreement with a prior review (from the nutrient content claim review, the structure/function claim review, or the healthy claim eligibility check) is a finding to surface, not to silently resolve.

Do not fabricate a legal risk, a provision, or a rewrite that is not a defensible reading of the copy and the cited framework. Flag anything genuinely ambiguous rather than asserting a verdict.

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: claims-compliance
sub-category: claims
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: claim-screen
status: REVIEW
aliases: []
tags:
  - claims-compliance
  - claims
  - [SKU-SLUG]
topic: beverage-label-compliance
use-case: prohibited-claim-screen
visibility: private
---
2. An H1 equal to the output file name without .md: prohibited-claim-screen-[SKU-SLUG]
3. The body specified in the method above.
4. This exact final line:
UNVERIFIED DRAFT - requires review and sign-off by the regulatory labeling specialist; citations unconfirmed against current eCFR.

[Paste marketing copy here]

[Paste label art copy here]

[Paste written description of label imagery here]

SKU identifier: [SKU]
```

## guardrails

Human-in-the-loop: flags and severities support legal/regulatory sign-off; this prompt never approves copy. Every critical-severity flag is a blocking issue until resolved by a human, and every undescribed or unevaluated imagery element stays flagged for human review.

Related: [[nutrient-content-claim-review]], [[structure-function-claim-review]], [[healthy-claim-eligibility-check]].
