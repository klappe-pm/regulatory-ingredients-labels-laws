ROOT := $(patsubst %/,%,$(dir $(abspath $(lastword $(MAKEFILE_LIST)))))
PYTHON ?= python3

.PHONY: help doctor audit audit-strict public-safety-check regwatch-validate regwatch-smoke prompts-normalize prompts-sync prompts-check prompts-docx test

AUDIT_DOCS := \
	"$(ROOT)/public/regwatch/regwatch-troubleshooting.md"

help:
	@printf 'targets: doctor audit audit-strict public-safety-check regwatch-validate regwatch-smoke prompts-normalize prompts-sync prompts-check prompts-docx test\n'

doctor:
	@test -f "$(ROOT)/README.md"
	@test -f "$(ROOT)/LICENSE"
	@test -x "$(ROOT)/scripts/regwatch.py"
	@test -f "$(ROOT)/public/regwatch/regwatch-schema.json"
	@printf 'doctor: passed\n'

audit:
	@$(PYTHON) "$(ROOT)/scripts/audit-markdown.py" --root "$(ROOT)" $(AUDIT_DOCS)

audit-strict:
	@$(PYTHON) "$(ROOT)/scripts/audit-markdown.py" --root "$(ROOT)" $(AUDIT_DOCS) --strict-frontmatter --strict-h1 --strict-links --strict-headers

public-safety-check:
	@$(PYTHON) "$(ROOT)/scripts/public-safety-check.py"

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
	@$(PYTHON) "$(ROOT)/scripts/regwatch.py" newsletter --out "$(ROOT)/build/regwatch-newsletter.md" >/dev/null
	@$(PYTHON) "$(ROOT)/scripts/regwatch.py" export --csv "$(ROOT)/build/regwatch-records-export.csv" --json "$(ROOT)/build/regwatch-records-export.json" >/dev/null
	@printf 'regwatch-smoke: passed\n'

prompts-normalize:
	@$(PYTHON) "$(ROOT)/scripts/normalize-prompt-frontmatter.py"

prompts-sync:
	@$(PYTHON) "$(ROOT)/scripts/sync-prompt-manifests.py"

prompts-check:
	@$(PYTHON) "$(ROOT)/scripts/sync-prompt-manifests.py" --check

prompts-docx: prompts-sync
	@$(PYTHON) "$(ROOT)/scripts/build-prompt-library-docx.py"

test: doctor audit-strict public-safety-check regwatch-validate regwatch-smoke prompts-check
	@printf 'test: passed\n'

