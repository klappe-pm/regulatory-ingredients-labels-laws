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

Tests nutrient content claims (e.g. "sugar free," "excellent source of vitamin C") against their FDA definition and disclosure triggers using the NFP values that support them, and flags claim terms FDA has never defined (e.g. "low sugar") as not permitted rather than testable.

## when-to-use

A claim has been scoped as a nutrient-content-claim pathway item in [[claims-target-scoping]], or any nutrient content claim needs review before label finalization.

## what-to-use-for

Testing claim text against 21 CFR 101.13/Subpart D definitions and 101.65 implied-claim rules on a per-RACC basis, checking the 101.13(h) disclosure triggers, and producing a per-claim verdict with required disclosures and a rewrite if the claim fails.

## required-inputs

- Claim text (exact wording)
- Full NFP values, including total fat, saturated fat, cholesterol, and sodium (the 21 CFR 101.13(h) disclosure triggers key on these four even when the claim is about a different nutrient)
- Serving size and RACC (21 CFR 101.12)

## expected-outputs

- Per-claim verdict (pass/fail/na/unable-to-verify/not-defined-not-permitted)
- Required disclosures (e.g. "see nutrition information for sodium content")
- Citation, marked UNVERIFIED until confirmed against the current eCFR
- Rewrite suggestion if the claim fails

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Attach the claim text and NFP values with the paperclip or a `/` file reference (files must be in OneDrive or SharePoint); paste the claim text, NFP values, and serving size/RACC directly when a file cannot be attached.
3. Copy the entire prompt-text block below, paste it into the chat, and fill every bracketed placeholder before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `nutrient-content-claim-review-<sku-slug>.md` in `projects/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder).
5. Review the output yourself. Nothing is final until a person signs off.

## output-handling

Apply this project's frontmatter convention: `domain: regulatory-ingredients-labels-laws`, `category: claims-compliance`, `sub-category: claims`, `date-created`/`date-revised` set to the run date, `type: claim-review`, `status: REVIEW`, `aliases: []`, `tags: [claims-compliance, claims, <sku-slug>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: nutrient-content-claim-review`, `visibility: private`.

File name: `nutrient-content-claim-review-<sku-slug>.md`, kebab-case, H1 equal to the file-name stem.

Saves to: `projects/regulatory-labeling/`.

## prompt-text

```
You are running inside Microsoft 365 Copilot Chat. Your single task: test nutrient content claims against their FDA definition and disclosure triggers.

You should have these inputs: (1) claim text exact wording, (2) full NFP values including total fat, saturated fat, cholesterol, and sodium, (3) serving size and RACC, (4) SKU identifier. If any input is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Source of truth: the NFP values I provide are authoritative for whether a claim's numeric threshold is met; the claim text under test is the artifact being checked against them.

Method:
1. Read each claim and the NFP values I provide below.
2. For each claim, identify the exact nutrient content claim definition it invokes (21 CFR 101.13 and Subpart D specific definitions, e.g. "free," "low," "reduced," "good source," "high"/"excellent source," or 101.65 implied claims).
3. If the claim term has no definition in 21 CFR 101.13/Subpart D or 101.65 (for example "low sugar," which FDA has not defined), do not test a threshold: the verdict is not-defined-not-permitted, citing 21 CFR 101.13(b) and FDCA 403(r)(1)(A) (an undefined nutrient content claim misbrands the food), both UNVERIFIED.
4. Check the NFP value against the definition's numeric threshold. Thresholds are keyed to the RACC (21 CFR 101.12), not the labeled serving; the beverage RACC is 240 mL and the carbonated beverage RACC is 360 mL (UNVERIFIED values, confirm against 101.12). Flag any labeled serving that differs from the RACC and state which basis you used.
5. Determine whether the 21 CFR 101.13(h) disclosure statement is triggered: total fat above 13 g, saturated fat above 4 g, cholesterol above 60 mg, or sodium above 480 mg per RACC (UNVERIFIED trigger levels, confirm against 101.13(h)). Any of the four can trigger it regardless of which nutrient the claim is about, so check all four even for a sugar or vitamin claim, and state the required "See nutrition information for X content" disclosure where triggered.
6. Produce a findings table: id, field (claim text), expected (the definitional threshold), observed (the actual NFP value), verdict, severity, citation (exact provision, marked UNVERIFIED), required-action. One row per claim, including passing claims. Close with the attestation line: "Claims reviewed: N of N; skipped: none."
7. Produce an aggregate disposition with a blocking-issues list.
8. For any failing claim, propose a compliant rewrite or state that no compliant version of the claim is available at this nutrient level. Never rewrite an undefined claim term into a defined claim unless the NFP values actually meet that defined claim's threshold.

Citation discipline: use only the provisions listed in this prompt. Never invent a provision, subsection, or threshold. Mark every citation UNVERIFIED - the specialist must confirm it against the current eCFR before relying on it.

Verdict vocabulary: pass (threshold met), fail (threshold not met), na (phrase is not a nutrient content claim), unable-to-verify (input unreadable or threshold uncheckable; never guess and never silently omit), not-defined-not-permitted (claim term has no FDA definition and may not be used at all). Aggregate disposition: no-findings-pending-human-review, findings-require-action, or blocked.

Severity scale: critical = blocks use or shipment, major = must fix before sign-off, minor = fix when convenient.

This is an independent second set of eyes; it never marks a claim approved. Surface disqualifying-nutrient disclosure requirements even if the claim itself would otherwise pass.

Do not fabricate a threshold, an NFP value, or a disclosure requirement not grounded in the source data or in the provisions above. Flag anything you cannot confirm.

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
use-case: nutrient-content-claim-review
visibility: private
---
2. An H1 equal to the output file name without .md: nutrient-content-claim-review-[SKU-SLUG]
3. The body specified in the method above.
4. This exact final line:
UNVERIFIED DRAFT - requires review and sign-off by the regulatory labeling specialist; citations unconfirmed against current eCFR.

[Paste claim text(s) here]

[Paste full NFP values here, including total fat, saturated fat, cholesterol, and sodium]

Serving size and RACC: [serving size and RACC]

SKU identifier: [SKU]
```

## guardrails

Human-in-the-loop: verdicts and rewrites support a human sign-off; this prompt never marks a claim compliant on its own. A claim term without a Subpart D or 101.65 definition is reported as not permitted, never adjudicated pass/fail. Escalate any claim bordering on an implied disease claim to [[prohibited-and-misleading-claim-screen]].

Related: [[structure-function-claim-review]], [[prohibited-and-misleading-claim-screen]], [[healthy-claim-eligibility-check]].
