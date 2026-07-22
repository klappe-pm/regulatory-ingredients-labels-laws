---
domain: regulatory-ingredients-labels-laws
category: copilot-skills
sub-category: word
date-created: 2026-07-22
date-revised: 2026-07-22
type: skill
status: DONE
aliases: []
tags:
  - copilot-skills
  - m365-copilot
  - regulatory-labeling
  - word
topic: beverage-label-compliance
use-case: copilot-in-word
visibility: private
---

# copilot-in-word

## description

How to use Copilot inside Word to draft and edit the documents a labeling specialist produces: label copy decks, regulatory memos, and review write-ups, plus comparing two versions of a document. Word is a comfortable place to draft, but comparing long documents is a task where Copilot silently misses things, so this guide points you to the dedicated comparison prompts for anything that matters.

## when-to-use

Drafting or tightening a memo or copy deck, reformatting a document, or getting a first look at what changed between two versions.

## what-copilot-can-do-here

- Draft a document from a prompt or an outline, and rewrite for tone, length, or clarity.
- Summarize a long document and pull out key points.
- Reformat, restructure headings, and produce a clean version of messy text.
- Give a first-pass look at differences between two documents you provide.

## what-copilot-cannot-do-here

- Be trusted to catch every difference between two labels or specs. It can miss a changed field and still sound thorough. For label-of-record versus production copy, use [[production-vs-documented-comparison]], which forces a field-by-field check with a completeness count.
- Verify regulatory content it writes. Citations in a memo are unverified until you check them.
- Track who approved what. Approval is a human step recorded outside the draft.

## setup

1. Open the document in Word (web or desktop) with your work account.
2. Open Copilot from the ribbon (Draft with Copilot, or the Copilot icon in the margin).
3. Turn on Track Changes before you let Copilot edit an existing document, so every change is visible and reversible.

## recipes

### draft a memo or copy deck

- Prompt: "Draft a [memo / copy deck] for [purpose]. Use these points: [PASTE POINTS]. Keep it factual; do not add regulatory claims or citations I did not give you."
- Copilot drafts the structure; you supply and verify any regulatory content.

### tighten or reformat

- Select the text, then prompt: "Rewrite this to be clearer and shorter without changing the meaning or any number, name, or citation." Review with Track Changes on.

### first-look document compare

- Prompt: "Compare document A and document B and list what changed. This is a first look only; I will run a full field-by-field comparison separately."
- Then run the real comparison with [[production-vs-documented-comparison]] or [[change-propagation-audit]] for anything that affects a label. Do not treat Copilot's in-Word diff as complete.

## guardrails

Copilot in Word is a drafting and first-look aid. It is not a reliable document comparator for compliance-critical files; use the dedicated comparison prompts, which enforce exhaustive checks. Keep Track Changes on so every edit is visible, supply and verify all regulatory content yourself, and remember that approval is a human step recorded outside the document.

Related: [[production-vs-documented-comparison]], [[change-propagation-audit]], [[copilot-chat-basics]].
