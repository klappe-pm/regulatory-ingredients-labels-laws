ROOT := $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))
PYTHON ?= python3

.PHONY: help doctor audit audit-strict regwatch-validate regwatch-smoke regwatch-brief regwatch-briefing rebuild-agents test strip-agents strip-hooks strip-specs

AUDIT_DOCS := \
	"$(ROOT)/docs/plans" \
	"$(ROOT)/docs/reference/reference-README.md" \
	"$(ROOT)/docs/reference/regwatch-troubleshooting.md" \
	"$(ROOT)/docs/reference/mcp.md" \
	"$(ROOT)/docs/reference/environment/environment-README.md" \
	"$(ROOT)/docs/reference/environment/environment-macos-machine-specs.md"

help:
	@printf 'targets: doctor audit audit-strict regwatch-validate regwatch-smoke regwatch-brief regwatch-briefing rebuild-agents test strip-agents strip-hooks strip-specs\n'

doctor:
	@test -f "$(ROOT)/CLAUDE.md"
	@test -f "$(ROOT)/project.yml"
	@test -x "$(ROOT)/scripts/build-agents.py"
	@test -d "$(ROOT)/docs/passoffs"
	@printf 'doctor: passed\n'

audit:
	@$(PYTHON) "$(ROOT)/scripts/audit-markdown.py" --root "$(ROOT)" $(AUDIT_DOCS)

audit-strict:
	@$(PYTHON) "$(ROOT)/scripts/audit-markdown.py" --root "$(ROOT)" $(AUDIT_DOCS) --strict-frontmatter --strict-h1 --strict-links --strict-headers

regwatch-validate:
	@$(PYTHON) "$(ROOT)/scripts/regwatch.py" validate

regwatch-smoke:
	@$(PYTHON) "$(ROOT)/scripts/regwatch.py" validate >/dev/null
	@$(PYTHON) "$(ROOT)/scripts/regwatch.py" coverage >/dev/null
	@$(PYTHON) "$(ROOT)/scripts/regwatch.py" portfolio >/dev/null
	@$(PYTHON) "$(ROOT)/scripts/regwatch.py" impact >/dev/null
	@$(PYTHON) "$(ROOT)/scripts/regwatch.py" beverage >/dev/null
	@$(PYTHON) "$(ROOT)/scripts/regwatch.py" list --upcoming 365 >/dev/null
	@$(PYTHON) "$(ROOT)/scripts/regwatch.py" scan >/dev/null
	@$(PYTHON) "$(ROOT)/scripts/regwatch.py" report --out "$(ROOT)/build/regwatch-report.md" --json "$(ROOT)/build/regwatch-report.json" >/dev/null
	@$(PYTHON) "$(ROOT)/scripts/regwatch.py" brief --cadence daily --out-dir "$(ROOT)/build/regwatch-smoke" >/dev/null
	@$(PYTHON) "$(ROOT)/scripts/regwatch.py" brief --cadence weekly --out-dir "$(ROOT)/build/regwatch-smoke" >/dev/null
	@$(PYTHON) "$(ROOT)/scripts/regwatch.py" ingest >/dev/null
	@$(PYTHON) "$(ROOT)/scripts/regwatch.py" briefing --out "$(ROOT)/build/regwatch-briefing.md" >/dev/null
	@$(PYTHON) "$(ROOT)/scripts/regwatch.py" briefing --tier v1 --since-days 90 --out "$(ROOT)/build/regwatch-briefing-v1.md" >/dev/null
	@$(PYTHON) "$(ROOT)/scripts/regwatch.py" briefing --tier v2 --since-days 90 --out "$(ROOT)/build/regwatch-briefing-v2.md" >/dev/null
	@printf 'regwatch-smoke: passed\n'

regwatch-brief:
	@$(PYTHON) "$(ROOT)/scripts/regwatch.py" brief --cadence weekly --out-dir "$(ROOT)/docs/reports/regwatch-samples"

regwatch-briefing:
	@$(PYTHON) "$(ROOT)/scripts/regwatch.py" briefing --out "$(ROOT)/docs/reports/regwatch-samples/regwatch-fda-beverage-briefing.md"

rebuild-agents:
	@$(PYTHON) "$(ROOT)/scripts/build-agents.py" --shared-dir "$(ROOT)/agents/shared" --out-dir "$(ROOT)/agents" --tools claude-code

test: doctor audit-strict regwatch-validate regwatch-smoke
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
