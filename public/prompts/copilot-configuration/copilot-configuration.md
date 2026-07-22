---
domain: regulatory-ingredients-labels-laws
category: copilot-configuration
sub-category: copilot-configuration
date-created: 2026-07-22
date-revised: 2026-07-22
type: index
status: DONE
aliases: []
tags:
  - copilot-configuration
  - regulatory-labeling
topic: beverage-label-compliance
use-case: browse-copilot-configuration
visibility: public
---

# copilot-configuration

Routing durable-knowledge artifacts (see [[durable-knowledge]]) to the correct Microsoft 365 Copilot layer, and the underlying layering map they are routed against. It holds the install router prompt and the static layering reference it is grounded in. This is the one category whose prompt outputs are public: every other category's outputs save privately to `projects/regulatory-labeling/`, while this category's routing outputs save to `public/regulatory-labeling/`. The prompt files themselves all live in this vault regardless of category; visibility describes where outputs save, not protection on the prompt files. This category is Copilot configuration guidance, not label content, and carries no product-specific regulatory information.

## prompts

- [[personalization-install-router]]

## reference

- [[copilot-layering-reference]] (not a prompt; a static reference note)

## workflow

1. Run a durable-knowledge prompt (see [[durable-knowledge]]) to produce the artifact to install.
2. Run the verify-what-is-enabled checklist in [[copilot-layering-reference]] and note which surfaces your tenant has on; ask your IT admin about anything missing before concluding it does not exist.
3. Run [[personalization-install-router]] with the artifact, the enabled-surfaces list, and the layering reference attached; save its output to `public/regulatory-labeling/`.
4. Perform the click-path from the routing output yourself, run its verification step, and when the artifact is later revised, update or remove the installed entry per the maintenance section of [[copilot-layering-reference]].

Up: [[regulatory-labeling]]

![[bases/copilot-configuration.base]]
