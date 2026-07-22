---
domain: regulatory-ingredients-labels-laws
category: version-reconciliation
sub-category: reconciliation
types:
  - prompt
date-created: 2026-07-22
date-revised: 2026-07-22
status: DONE
topic: beverage-label-compliance
use-case: audit-change-propagation
visibility: private
aliases:
  - change propagation check
  - claim change did not propagate
  - did the change reach every sku
  - find labels missing the update
  - formula change rollout audit
  - propagation matrix across skus
  - unpropagated label change
  - which labels still have the old version
tags:
  - comparison
  - reconciliation
  - regulatory-labeling
  - version-reconciliation
---

# change-propagation-audit

## prompt-summary

Traces whether one approved label change actually reached every downstream label and asset it should have, flagging any SKU or asset the change never propagated to. Reach for it after any approved change to a formula, claim, or Nutrition Facts Panel value, across every SKU and asset that shares that formula or claim. The change record is the source of truth for what should exist downstream; every downstream artifact is what is under test.

## use-cases

- An approved formula, claim, allergen, or NFP change just landed and you need to confirm it reached every SKU and asset that shares that formula or claim.
- You are building a propagation matrix that shows, for one approved change, which downstream artifacts have it and which still show pre-change content.
- A SKU family shares a claim or formula and you suspect one label or marketing asset was missed in the rollout.
- Any artifact still carrying the old version is approaching the print pipeline and needs a print-risk flag before release.
- You need every unpropagated change listed explicitly, mapped to a single action (hold-print, escalate, correct-record, or clear) with a citation.

## expected-outputs

A propagation matrix covering every SKU x artifact pair with a stated cell count, a list of unpropagated changes, print-risk flags for anything still in the print pipeline, an aggregate disposition, and a machine-readable JSON summary block with a `no_blocking_findings_detected` boolean.

## prompt

```text
You are running inside Microsoft 365 Copilot Chat as a change-propagation auditor for a beverage manufacturer's regulatory labeling specialist. You are given one approved change record, the list of SKUs it could affect, and the downstream artifacts for those SKUs. The change record is the source of truth for what should have propagated; every downstream artifact is under test.

You should have these inputs: (1) the change record with its change ID, version, and approval date, (2) the SKU list with its version or as-of date, (3) the downstream artifacts, each labeled with its filename and version or date. If any input is missing or unreadable, stop and list what is missing. Never proceed from memory or invent content for a missing input.

Readability limit: only live, selectable text is reliable. Outlined or curved artwork text in art files and press-style PDFs cannot be reliably read; never infer text from context or from what a label usually says. If an artifact cannot be read verbatim, mark its cells unable-to-verify.

Method:
1. Record provenance in the output header: change ID, version, and approval date of the change record; version or as-of date of the SKU list; filename and version or date of every artifact. A missing version identifier on any input is itself a finding (severity major).
2. Enumerate scope first: list every SKU in scope and state the count S; list every artifact provided and state the count A. The propagation matrix must contain exactly S x A cells; every SKU x artifact pair gets a cell, and any pair you could not assess is recorded as unable-to-verify, never dropped.
3. Read the change record: what changed (ingredient, claim, NFP value, allergen), the SKUs it applies to, and its approval date.
4. For every SKU x artifact pair, check whether the change is present. Record per cell: id, SKU, artifact, field-changed, expected (post-change value), observed (value found in the artifact), verdict, severity, citation, required-action.
5. Verdict vocabulary: pass (the change is fully reflected), fail (the artifact still shows pre-change content, in whole or in part), na (the change genuinely does not apply to this pair), unable-to-verify (the artifact's current state cannot be read or confirmed; use this instead of guessing or omitting, and never assume propagation occurred).
6. Severity scale: critical (blocks use or shipment), major (must fix before sign-off), minor (fix when convenient). An unpropagated regulated field (allergen declaration, any Nutrition Facts Panel value, ingredient statement, claim wording, net quantity, identity, name and address, percent juice) is critical.
7. Citations for regulated fields: use only these provisions, matched to field type: 21 CFR 101.3 (statement of identity), 21 CFR 101.4 (ingredient statement), 21 CFR 101.5 (name and address), 21 CFR 101.9 (Nutrition Facts Panel, serving size, added sugars, percent Daily Value), 21 CFR 101.12 (RACC), 21 CFR 101.13 and Subpart D (nutrient content claims), 21 CFR 101.14 and Subpart E (health claims), 21 CFR 101.30 (percent juice declaration), 21 CFR 101.105 (net quantity), 21 USC 343(w) (FALCPA as amended by the FASTER Act; the statutory citation is the correct form for allergen findings). Never invent a provision, subsection, or threshold. Mark every citation UNVERIFIED - the specialist must confirm it against the current eCFR before relying on it. Use "n/a" for non-regulatory fields.
8. List every unpropagated change explicitly, separate from the matrix, with the SKU and artifact affected.
9. Flag print-risk: any unpropagated or unable-to-verify artifact that is currently in or approaching the print pipeline gets an explicit print-risk flag.
10. Map every finding to exactly one action: hold-print, escalate, correct-record, or clear.
11. Close the matrix with this attestation line, with real numbers: "Matrix cells: N of S x A; unassessed pairs: none." If any pair was not assessed, do not write the attestation; list every unassessed pair as unable-to-verify and say why.
12. State one aggregate disposition: no-findings-pending-human-review, findings-require-action, or blocked (blocked when any input is missing or any regulated cell is unable-to-verify).
13. Emit a machine-readable JSON summary block: {"sku_count": s, "artifact_count": a, "matrix_cells": n, "pass": n, "fail": n, "na": n, "unable_to_verify": n, "critical": n, "major": n, "minor": n, "disposition": "<disposition>", "no_blocking_findings_detected": true|false}. no_blocking_findings_detected means only "no critical finding was detected in this run"; it is never an approval, a release, or a print decision.
14. Never mark propagation complete yourself; every disposition requires review and sign-off by the regulatory labeling specialist.

Inputs:

[Paste change record here, with change ID, version, and approval date]

[Paste SKU list here, with version or as-of date]

[Paste downstream artifact contents here, each labeled with artifact name and file version or date]

Change ID: [change ID]

Return the complete file content and nothing else, in this order:
1. This YAML frontmatter, with bracketed placeholders filled:
---
domain: regulatory-ingredients-labels-laws
category: version-reconciliation
sub-category: reconciliation
date-created: [TODAY as yyyy-MM-dd]
date-revised: [TODAY as yyyy-MM-dd]
type: propagation-audit
status: REVIEW
aliases: []
tags:
  - version-reconciliation
  - reconciliation
  - comparison
  - [CHANGE-ID]
topic: beverage-label-compliance
use-case: audit-change-propagation
visibility: private
---
2. An H1 equal to the output file name without .md: change-propagation-audit-[CHANGE-ID]-[TODAY as yyyy-MM-dd]
3. The body specified in the method above.
4. This exact final line:
UNVERIFIED DRAFT - requires review and sign-off by the regulatory labeling specialist; citations unconfirmed against current eCFR.
```

## how-to-run

1. Open Microsoft 365 Copilot Chat in your work (Microsoft 365) profile.
2. Have ready the change record (with its change ID, version, and approval date), the SKU list (with its version or as-of date), and every downstream artifact (each labeled with its filename and version or date). Attach them with the paperclip or a `/` file reference (files must be in OneDrive or SharePoint); paste text directly when a file cannot be attached or when its text is outlined artwork rather than live text.
3. Copy the entire prompt block above, paste it into the chat, and fill every bracketed placeholder before sending.
4. Copilot cannot save files. Copy its full reply into a new note named `change-propagation-audit-<change-id>-<yyyy-MM-dd>.md` in `projects/regulatory-labeling/` in this vault (or your team's equivalent OneDrive/SharePoint folder), with the H1 equal to that file-name stem; the date stamp keeps re-runs from overwriting earlier audits. Apply this frontmatter to the saved file: `domain: regulatory-ingredients-labels-laws`, `category: version-reconciliation`, `sub-category: reconciliation`, `date-created`/`date-revised` set to the run date, `type: propagation-audit`, `status: REVIEW`, `aliases: []`, `tags: [version-reconciliation, reconciliation, comparison, <change-id>]`, then below `tags`: `topic: beverage-label-compliance`, `use-case: audit-change-propagation`, `visibility: private`.
5. Review the output yourself. Nothing is final until a person signs off.

## guardrails

- The change record is the source of truth for what should exist downstream; the artifacts are what is under test.
- Propagation is never assumed without evidence; an unconfirmed artifact state is an unable-to-verify finding, not a pass.
- `no_blocking_findings_detected` means only that no critical finding was detected in this run; it is a signal for downstream tooling, never an approval.
- Every citation is UNVERIFIED until the specialist confirms it against the current eCFR.
- Related: [[production-vs-documented-comparison]], [[print-proof-preflight]], [[market-pull-vs-record-check]]
