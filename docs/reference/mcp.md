---
domain: engineering
category: reference
sub-category: mcp
date-created: 2026-05-20
date-revised: 2026-05-20
type: reference
status: active
aliases:
tags:
  - mcp
  - project-config
---

# mcp

Project-shared MCP server declarations belong in `.mcp.json` at the project
root. User-specific MCP state belongs outside the project in `~/.claude.json`.

Start from `.mcp.example.json` and commit only shared server declarations that
the whole project needs. Do not commit credentials, OAuth state, local cache
files, or machine-specific paths.
