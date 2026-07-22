---
domain: regulatory-ingredients-labels-laws
category: review-and-verification
sub-category: hitl-review
types:
  - prompt
date-created: 2026-07-22
date-revised: 2026-07-22
status: DONE
topic: beverage-label-compliance
use-case: second-eyes-review-artifact
visibility: private
aliases:
  - cross check review findings
  - double check a prior review
  - human in the loop review
  - independent re-review
  - second eyes review
  - second pair of eyes label check
  - two stage review
  - verify prior review citations
tags:
  - hitl-review
  - regulatory-labeling
  - review-and-verification
---

# second-eyes-hitl-review

## prompt-summary

Runs a two-stage second-eyes review over a prior review's output: stage-a re-derives findings from the artifact and the source of truth in a fresh chat without seeing the prior review, and stage-b compares the two findings sets, verifies the prior review's citations, and recommends (never makes) a human sign-off decision. Reach for it after any review or checklist pass has produced a finding set, and before a human reviewer signs off on the artifact. This is not an independent human review: both stages run on the same model, driven by the same user, in the same Microsoft 365 tenant as the first pass, so correlated errors (a shared misreading, a shared fabricated citation, a shared blind spot) will not be caught. It supplements, and never replaces, review by a second person.

## use-cases

- A prior review or checklist pass (including [[checklist-template-evaluation]]) has produced a finding set, and a human reviewer is about to sign off on the artifact.
- You want the prior review's findings cross-checked for agreements, disputes, and missed issues against an independently derived pass.
- You need every citation the prior review used verified against the documented source of truth (approved label of record with version and effective date, formula, substantiation file).
- You want residual risk stated explicitly and a recommended next step (ready-for-human-decision, escalate, or re-review) for the human reviewer.
- You accept that this supplements, but does not replace, a second person's review, since both passes share the same model, user, and tenant.

## expected-outputs

- Stage-a: an independently derived findings table with a completeness attestation.
- Stage-b: agreements, disputes, and missed-issue tables; a citation-verification list covering every citation the prior review used, with unconfirmable citations listed as residual risk; an explicit residual-risk summary; and a recommendation that is exactly one of ready-for-human-decision, escalate, re-review. Never an approval.
- A closing UNVERIFIED DRAFT line on each stage's output.

## prompt

### stage-a-independent-findings

Run this in a fresh chat with only the artifact and the source of truth attached. Do not attach the prior review.

```text
You are running inside Microsoft 365 Copilot Chat as a reviewer re-deriving findings for a beverage manufacturer's regulatory labeling specialist. This is stage-a of a two-stage second-eyes review: you derive findings from scratch, without seeing any prior review. If a prior review's output is attached to or pasted into this chat, say so and stop; using it would anchor your findings and defeat the purpose of this stage.

You should have these inputs: (1) the artifact under review for [SKU-OR-ARTIFACT-NAME] (attached or pasted), (2) the documented source of truth, including the approved label of record with its version and effective date, the formula, and the substantiation file as applicable (attached or pasted). If any input is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Citation discipline: never invent a provision, subsection, or threshold. Mark every citation UNVERIFIED - the specialist must confirm it against the current eCFR before relying on it.

Method:
1. Check the artifact against the source of truth field by field and derive your own findings.
2. Build a findings table with one row per checked field, including pass rows. Columns: id, field, expected, observed, verdict, severity, citation (exact provision where the field is regulatory, marked UNVERIFIED, otherwise "n/a"), required-action.
3. Verdict values: pass (the source of truth confirms the field), fail (the source of truth refutes it), na (the field does not apply), unable-to-verify (the input needed is missing or unreadable; never guess and never silently omit the row).
4. Severity values: critical (blocks use or shipment), major (must fix before sign-off), minor (fix when convenient).
5. Close the table with this attestation line: "Fields checked: N of N; skipped: none".
6. Never mark the artifact approved; never fabricate a citation, a threshold, or a figure.

Return only the findings table and the attestation line, followed by this exact final line:
UNVERIFIED DRAFT - requires review and sign-off by the regulatory labeling specialist; citations unconfirmed against current eCFR.
```

### stage-b-comparison

Run this in another new chat, with the prior review, the artifact, and the source of truth attached, and the stage-a findings pasted in where marked.

```text
You are running inside Microsoft 365 Copilot Chat as a second-eyes comparator for a beverage manufacturer's regulatory labeling specialist. This is stage-b of a two-stage second-eyes review: you compare an independently derived findings set (stage-a, produced in a fresh chat) against a prior review's findings. The documented source of truth (approved label of record, formula, substantiation file as applicable) is authoritative; both reviews are claims to test against it, and the artifact under review is what both were checking.

You should have these inputs: (1) the stage-a findings table (pasted below), (2) the prior review's output, findings and disposition (attached or pasted), (3) the artifact under review for [SKU-OR-ARTIFACT-NAME] (attached or pasted), (4) the documented source of truth, including the approved label of record with its version and effective date, the formula, and the substantiation file as applicable (attached or pasted). If any input is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Stage-a findings:
[PASTE STAGE-A FINDINGS TABLE HERE]

Citation discipline: never invent a provision, subsection, or threshold. Mark every citation UNVERIFIED - the specialist must confirm it against the current eCFR before relying on it.

Method:
1. Compare the stage-a findings to the prior review's findings, item by item.
2. Classify each item as: agreement (both reach the same verdict), dispute (verdicts differ; state both verdicts and why, with citation), or missed (an issue one pass found that the other did not surface).
3. Present the three groups as tables with columns: id, field, stage-a-verdict, prior-verdict (where applicable), severity (critical = blocks use or shipment, major = must fix before sign-off, minor = fix when convenient), citation (exact provision where regulatory, marked UNVERIFIED), required-action.
4. Verify every citation the prior review used against the attached source of truth. List every citation you cannot confirm from the attached materials as residual risk, marked UNVERIFIED; never silently accept or drop a citation.
5. State an explicit residual-risk summary: what could still be wrong even after both passes, including unconfirmable citations, unable-to-verify items, and this structural limit: both passes ran on the same model, driven by the same user, in the same tenant, so errors shared by both passes are not caught here and a second person's review is still required.
6. End with a recommendation that is exactly one of: ready-for-human-decision (all findings, disputes, and risks are fully listed for the specialist to decide on), escalate (a critical finding or unresolved dispute needs a second person or regulatory counsel), re-review (an input was missing or unreadable, or stage-a was not run in a fresh chat). Never state the artifact is approved; the sign-off decision belongs to a human.
7. Never fabricate a citation, a threshold, or a figure.

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: review-and-verification
sub-category: hitl-review
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: second-eyes-review
status: REVIEW
aliases: []
tags:
  - review-and-verification
  - hitl-review
  - [SKU-SLUG]
topic: beverage-label-compliance
use-case: second-eyes-review-artifact
visibility: private
---
2. An H1 equal to the output file name without .md: second-eyes-review-[SKU-OR-ARTIFACT-SLUG]-[TODAY as yyyy-MM-dd]
3. The body specified in the method above.
4. This exact final line:
UNVERIFIED DRAFT - requires review and sign-off by the regulatory labeling specialist; citations unconfirmed against current eCFR.
```

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Have ready the prior review's output (findings and disposition), the artifact under review, and the documented source of truth (approved label of record with version and effective date, formula, substantiation file). Attach files with the paperclip or a `/` file reference (files must be in OneDrive or SharePoint), or paste text directly when a file cannot be attached. Do not attach or mention the prior review in the stage-a chat; that would anchor the re-derivation and defeat the point of a second pass.
3. Stage-a runs in a FRESH chat with only the artifact and the source of truth attached: copy the stage-a prompt block above into that chat, fill every bracketed placeholder, send, and copy Copilot's full reply. Stage-b runs in another new chat with the prior review, the artifact, and the source of truth attached: copy the stage-b prompt block above, paste the stage-a findings where marked, fill the remaining placeholders, and send.
4. Copilot cannot save files. Copy the stage-b reply into a new note named `second-eyes-review-<sku-or-artifact-slug>-<yyyy-MM-dd>.md` in `projects/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder); set the output frontmatter `type: second-eyes-review` and `status: REVIEW`, and keep the stage-a reply pasted inside it as its own section if you want the full trail. The date in the file name means re-runs never overwrite an earlier review.
5. Review the output yourself. The recommendation is input to your decision; nothing is signed off until a person signs off, and true independence still requires a second person.

## guardrails

- This prompt never approves. The recommendation vocabulary is closed (ready-for-human-decision, escalate, re-review) and cannot express approval or sign-off; a human makes the sign-off decision.
- Independence is procedural, not real: stage-a must run in a fresh chat without the prior review attached, and even then both passes share the same model, user, and tenant, so correlated errors will not be caught. This supplements, never replaces, a second person's review.
- Stage-b verifies every citation the prior review used against the attached source of truth; any citation that cannot be confirmed is listed as residual risk, never silently accepted.
- Any uncertainty is surfaced explicitly as residual risk rather than resolved silently. Never fabricate a finding, citation, threshold, or figure.
- Related: [[checklist-template-evaluation]], a common upstream input; [[production-vs-documented-comparison]].
