---
domain: regulatory-ingredients-labels-laws
category: setup
sub-category: index
date-created: 2026-07-22
date-revised: 2026-07-22
type: index
status: DONE
aliases: []
tags:
  - onboarding
  - regulatory-labeling
  - setup
topic: beverage-label-compliance
use-case: browse-setup-prompts
visibility: private
---

# setup

Guided onboarding for a first-time user. Instead of asking you to write documents about yourself, these prompts have Copilot interview you: one question at a time, in plain language, with skip and pause allowed. Your answers become the durable context records that the [[durable-knowledge]] prompts formalize and the [[personalization-install-router]] installs into Copilot.

Run [[setup-interview]] once when you start using this library, then [[setup-refresh]] whenever your role, team, products, or workstreams change (a quarterly pass is a good default).

## prompts

- [[setup-interview]]: the first-run onboarding interview; produces your setup profile record.
- [[setup-refresh]]: a shorter re-interview against your existing profile; produces an updated record and a list of installed entries to update or remove.

## workflow

1. Run [[setup-interview]] in Copilot Chat and save the setup profile record it produces.
2. Feed the record's sections into the four [[durable-knowledge]] prompts to produce the formal context records.
3. Route each record into the right Copilot layer with [[personalization-install-router]].
4. On later changes, run [[setup-refresh]] instead of starting over.

Part of the full library: [[regulatory-labeling]].

![[bases/setup.base]]
