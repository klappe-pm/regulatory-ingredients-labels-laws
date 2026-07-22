---
domain: regulatory-ingredients-labels-laws
category: copilot-skills
sub-category: sharepoint
types:
  - skill
date-created: 2026-07-22
date-revised: 2026-07-22
status: DONE
topic: beverage-label-compliance
use-case: copilot-in-sharepoint
visibility: private
aliases:
  - ask questions across documents
  - confirm document version
  - copilot in sharepoint
  - find the current label of record
  - search a sharepoint library
  - sharepoint copilot for labeling
  - sharepoint grounded agent
  - site scoped copilot agent
tags:
  - copilot-skills
  - m365-copilot
  - regulatory-labeling
  - sharepoint
---

# copilot-in-sharepoint

## prompt-summary

How to use Copilot with SharePoint to find the current label of record, ask questions grounded in a document library, and (where your permissions allow) stand up a site-scoped agent so Copilot answers only from a trusted set of files. SharePoint is where the authoritative documents live, so getting Copilot to point at the right library, and knowing when it cannot, is the whole skill.

## use-cases

- You are hunting for the current approved label of record or spec in a SharePoint library.
- You want to ask questions grounded in a specific file or document library without outside knowledge.
- You need to confirm the version and last-modified date of a document before treating it as authoritative.
- You want to stand up a site-scoped agent so your team gets answers only from approved files (see [[copilot-layering-reference]]).
- You are unsure whether agent creation is enabled for you and need to check with IT before relying on it.

## what-copilot-can-do-here

- Find and open files you have permission to see, and summarize a document you reference.
- Answer questions grounded in a specific file or library you point it at.
- With the right permissions, let you create a SharePoint agent scoped to one site or library, so answers come only from those files.

## what-copilot-cannot-do-here

- See files you do not have permission to open; its answers are bounded by your access.
- Guarantee it found the current version. If a library holds several revisions, it may summarize an old one. You confirm the version.
- Create tenant-wide or admin-gated configuration. Site-scoped agents are often self-service; broad publishing needs IT.

## setup

1. Confirm the authoritative documents (approved labels, specs) live in a known SharePoint library you can reach.
2. Make sure version history is on for that library so "current" is unambiguous.
3. For a grounded agent, open the library, look for the Copilot or agent option, and check with IT whether creating one is enabled for you before relying on it (see the checklist in [[copilot-layering-reference]]).

## recipes

### find the current label of record

- Prompt in Copilot Chat: "Find the most recent approved label document for [SKU] in [library or site]. Tell me its file name, version, and last-modified date so I can confirm it is current. If more than one could match, list them; do not pick one silently."
- Always verify the version and date yourself before treating a file as the label of record.

### ask questions across a library

- Reference the library or a specific file with `/`, then ask: "Using only [this file / this library], answer [question]. If the answer is not in these documents, say so; do not use outside knowledge."

### stand up a site-scoped agent (if permitted)

- In the library, create a SharePoint agent grounded on that library so your team asks questions and gets answers only from approved files. Route durable context into it via [[personalization-install-router]], and remember that anyone the agent is shared with sees whatever you put in it.

## guardrails

Copilot's SharePoint answers are bounded by your permissions and are not guaranteed to be the current version; confirm the version and date of any label of record before relying on it. A grounded agent only helps if it points at the trusted library, so keep sources clean and do not put confidential formulas or colleague personal data into an agent that may be shared. When agent creation or grounding is not available, it may be disabled by IT policy; ask rather than assume.

Related: [[copilot-layering-reference]], [[personalization-install-router]], [[market-pull-vs-record-check]], [[copilot-chat-basics]].
