# docs/CLAUDE.md

#agent-context


Documentation under `docs/` uses project-local frontmatter, relative links,
and concise status-oriented prose. Keep passoffs in `docs/passoffs/`.

Current document paths resolve through `.pointer` files. Read the pointer,
resolve its single relative path from the pointer file's directory, then read
the target document. The active pointers are:

| Pointer | Resolves to |
|---|---|
| `passoffs/LATEST.pointer` | Latest passoff |
| `plans/ACTIVE-DELIVERY-PLAN.pointer` | Current delivery plan |
| `reports/BEVERAGE-BRIEFING.pointer` | Current beverage briefing |
| `reports/BEVERAGE-DECK.pointer` | Current beverage deck source |
