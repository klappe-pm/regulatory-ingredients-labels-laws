ROOT := $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))
PYTHON ?= python3

.PHONY: help doctor audit audit-strict regwatch-validate regwatch-brief rebuild-agents test strip-agents strip-hooks strip-specs

AUDIT_DOCS := \
	"$(ROOT)/docs/plans" \
	"$(ROOT)/docs/reference/reference-README.md" \
	"$(ROOT)/docs/reference/mcp.md" \
	"$(ROOT)/docs/reference/environment/environment-README.md" \
	"$(ROOT)/docs/reference/environment/environment-macos-machine-specs.md"

help:
	@printf 'targets: doctor audit audit-strict regwatch-validate regwatch-brief rebuild-agents test strip-agents strip-hooks strip-specs\n'

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

regwatch-brief:
	@$(PYTHON) "$(ROOT)/scripts/regwatch.py" brief --cadence weekly --out-dir "$(ROOT)/docs/reports/regwatch-samples"

rebuild-agents:
	@$(PYTHON) "$(ROOT)/scripts/build-agents.py" --shared-dir "$(ROOT)/agents/shared" --out-dir "$(ROOT)/agents" --tools claude-code

test: doctor audit-strict regwatch-validate
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
