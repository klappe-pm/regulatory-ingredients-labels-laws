---
domain: regulatory-ingredients-labels-laws
category: copilot-skills
sub-category: foundations
date-created: 2026-07-22
date-revised: 2026-07-22
type: skill
status: DONE
aliases: []
tags:
  - copilot-skills
  - m365-copilot
  - regulatory-labeling
topic: beverage-label-compliance
use-case: copilot-chat-foundations
visibility: private
---

# copilot-chat-basics

## description

The foundation guide every other skill assumes. It teaches the handful of moves that make Microsoft 365 Copilot Chat useful and safe for a beginner: opening the right (work) Copilot, attaching or referencing your files, writing a prompt that gets a good answer, and reading the reply critically. If you learn only one guide, learn this one.

## when-to-use

Before running any prompt in this library for the first time, and any time Copilot's answers feel vague, wrong, or like it did not see your file.

## what-copilot-can-do-here

- Read files you attach or reference (Word, Excel, PDF with real text, PowerPoint) that live in your OneDrive or SharePoint.
- Draft, rewrite, summarize, compare, and extract from text you give it.
- Work grounded in your Microsoft 365 content when you use the work version of Copilot.

## what-copilot-cannot-do-here

- Save a file for you. It returns text; you copy that text into a file yourself.
- Reliably read a scanned image, a photo of a label, or artwork where the text is outlined (turned into a picture). It may guess and sound confident.
- Look up the current text of a regulation. It works from training data that can be out of date, so every legal citation it gives is unverified until you check it.
- Remember this chat tomorrow unless you deliberately saved something into a durable layer (see [[copilot-configuration]]).

## setup

1. Confirm you are in the work Copilot, not the personal one. Look for your company name or a work-account badge; the work version is the only one allowed to see company files. If unsure, ask your IT contact which URL or app icon is the licensed Microsoft 365 Copilot.
2. Put the files you will use in OneDrive or a SharePoint library, not just on your desktop; Copilot Chat can only reference files that live in Microsoft 365.

## recipes

### attach or reference a file

- Click the paperclip and pick the file, or type `/` and start typing the file name to reference it inline. Wait until Copilot confirms it can see the file before asking your question.
- If a file will not attach, open it, copy the text, and paste it into the chat after your prompt. Say "the text below is the formula" so Copilot knows what it is.

### write a prompt that works

- Say who you are and the single task: "You are helping a regulatory labeling specialist. Your task is to ...".
- Name the inputs and where they are: "I have attached the formula and the approved label."
- Say the output you want: "Return a table with one row per ingredient."
- Add the safety line the library uses: "If anything is missing or unreadable, stop and tell me; do not guess."
- The prompts in this library already do all of this for you. Paste them as written and fill the [BRACKETED] blanks.

### read the answer critically

- Check that Copilot actually used your file: does it quote real values from it? If it speaks in generalities, it may not have read the attachment; re-attach and ask again.
- Treat every regulation citation as unverified. Confirm it against the current eCFR before you rely on it.
- Nothing Copilot returns is approved. A person signs off; Copilot drafts.

## guardrails

Use only the work (licensed) Copilot for anything containing SKU, formula, colleague, or other company information; the personal Copilot is not covered by your company's data agreement. Copilot assists and drafts; it never approves a label, and its legal citations are unverified until a person checks them. When in doubt about what is safe to paste, ask your IT or compliance contact first.

Related: [[copilot-in-excel]], [[copilot-in-outlook]], [[copilot-in-word]], [[copilot-in-sharepoint]], [[copilot-configuration]].
