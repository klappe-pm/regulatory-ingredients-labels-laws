---
domain: regulatory-ingredients-labels-laws
category: regulatory-labeling
sub-category: overview
date-created: 2026-07-22
date-revised: 2026-07-22
type: index
status: DONE
aliases:
  - regulatory labeling prompt library
  - prompt library home
tags:
  - regulatory-labeling
  - prompt-library
  - copilot
topic: beverage-label-compliance
use-case: browse-prompt-library
visibility: private
---

# regulatory-labeling

Master index for the regulatory labeling prompt library: a catalog of prompts a regulatory labeling specialist at a US beverage manufacturer runs inside Microsoft 365 Copilot, spanning onboarding setup, intake, content derivation, claims compliance, review and verification, version reconciliation, market monitoring and status reporting, email communication, durable personal and team knowledge, Copilot configuration, app-specific skills, and periodic reflection. Every prompt follows the same section contract (description, when-to-use, what-to-use-for, required-inputs, expected-outputs, how-to-run, output-handling, prompt-text, guardrails) and every compliance-facing prompt enforces human-in-the-loop review, forbids fabrication, cites exact regulatory provisions marked unverified until confirmed, and ends its output with an unverified-draft banner. Default jurisdiction is US FDA; no SKU is treated as a dietary supplement unless stated. New here? Read [[prompt-library-user-guide]] first, then run [[setup-interview]].

## start-here

- [[prompt-library-user-guide]]: how the library works, how to run a prompt in Copilot, and the safety rules. Read this first.
- [[setup]]: a guided interview that builds your personal and team context so Copilot knows who you are and what you work on.
- [[copilot-skills]]: plain-language guides for using Copilot inside Copilot Chat, Excel, Outlook, Word, and SharePoint.

## categories

- [[label-intake]]: normalize a dev brief and formula into a structured intake record, and scope intended claims by regulatory pathway, before any drafting begins.
- [[content-derivation]]: derive the ingredient statement, verify the allergen declaration, and build and rounding-check the Nutrition Facts Panel from the formula.
- [[claims-compliance]]: test nutrient content claims, structure/function claims, prohibited or misleading claims, and "healthy" eligibility against exact provisions.
- [[review-and-verification]]: evaluate a draft against a checklist and run an independent second, human-in-the-loop review.
- [[version-reconciliation]]: catch silent drift between the approved label of record and production copy, downstream propagation, or a press proof.
- [[market-and-reporting]]: compare an in-market label against the approved record, and roll findings into a weekly status report.
- [[communication-email]]: draft, revise, and reply to email in the specialist's voice, and convert threads into decisions and actions.
- [[durable-knowledge]]: capture the specialist's durable communication style, stakeholders, team roles, and current workstreams for Copilot to remember.
- [[copilot-configuration]]: route any durable-knowledge artifact to its correct Copilot layer, grounded in the current M365 personalization and agent layering model.
- [[reflection]]: review your own prompting, find tasks worth turning into reusable assets, and run a monthly usage retro.

## browse

![[bases/all-prompts.base]]

## by category

![[bases/by-category.base]]
