ROOT := $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))
PYTHON ?= python3

.PHONY: help doctor audit audit-strict rebuild-agents test strip-agents strip-hooks strip-specs strip-warp strip-gemini

help:
	@printf 'targets: doctor audit audit-strict rebuild-agents test strip-agents strip-hooks strip-specs strip-warp strip-gemini\n'

doctor:
	@test -f "$(ROOT)/CLAUDE.md"
	@test -f "$(ROOT)/project.yml"
	@test -x "$(ROOT)/scripts/build-agents.py"
	@test -d "$(ROOT)/docs/passoffs"
	@printf 'doctor: passed\n'

audit:
	@$(PYTHON) "$(ROOT)/scripts/audit-markdown.py" --root "$(ROOT)" "$(ROOT)/rules"

audit-strict:
	@$(PYTHON) "$(ROOT)/scripts/audit-markdown.py" --root "$(ROOT)" "$(ROOT)/rules" --strict-frontmatter --strict-h1 --strict-links --strict-headers

rebuild-agents:
	@$(PYTHON) "$(ROOT)/scripts/build-agents.py" --shared-dir "$(ROOT)/agents/shared" --out-dir "$(ROOT)/agents"

test: doctor audit-strict
	@printf 'test: passed\n'

strip-agents:
	@rm -rf "$(ROOT)/agents" "$(ROOT)/.claude/agents"
	@printf 'strip-agents: removed agent templates\n'

strip-hooks:
	@rm -rf "$(ROOT)/.claude/hooks"
	@printf 'strip-hooks: removed project hook templates\n'

strip-specs:
	@rm -rf "$(ROOT)/specs"
	@printf 'strip-specs: removed scaffold specs\n'

strip-warp:
	@rm -f "$(ROOT)/WARP.md"
	@printf 'strip-warp: removed Warp instructions\n'

strip-gemini:
	@rm -f "$(ROOT)/GEMINI.md"
	@printf 'strip-gemini: removed Gemini instructions\n'
