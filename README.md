# regulatory-ingredients-labels-laws

An open, local-first toolkit for tracking food-ingredient and labeling developments. It provides a validated regulatory register, source-change detection, generic beverage impact examples, and a human-review-first Microsoft 365 Copilot prompt library.

This project is reference tooling, not legal advice or label approval. Confirm every regulatory claim against current primary source text with qualified counsel or compliance reviewers.

## quick-start

Requires Python 3.11 or later. The monitoring engine uses only the standard library. Rebuilding the optional Word prompt-library export also requires `python-docx`.

```bash
cd /path/to/regulatory-ingredients-labels-laws
make test
python3 scripts/regwatch.py --help
python3 scripts/regwatch.py validate
```

## what-is-included

- `public/regwatch/`: validated seed register, jurisdiction and source catalogs, generic portfolio sample, and operational guidance.
- `scripts/regwatch.py`: command-line engine for validation, scanning, reports, ingestion candidates, impact analysis, and rendered briefs.
- `public/prompts/`: reviewed prompt source files for a regulatory-labeling workflow. Markdown files are the source of truth.
- `scripts/`: small, dependency-light maintenance tools.

The repository deliberately excludes client materials, source-document bundles, personal data, session handoffs, machine paths, editor settings, and generated runtime configuration.

## regwatch

```bash
cd /path/to/regulatory-ingredients-labels-laws
python3 scripts/regwatch.py validate
python3 scripts/regwatch.py coverage
python3 scripts/regwatch.py scan
python3 scripts/regwatch.py impact --severity act-now
python3 scripts/regwatch.py report --out report.md --json report.json
```

`scan` identifies candidates only. It never edits the curated register. Human reviewers confirm candidates against primary source text before changing regulatory records.

See [the Regwatch guide](public/regwatch/regwatch-README.md) for the data model, output formats, and operating rules.

## prompt-library

Start with [the prompt-library guide](public/prompts/prompt-library-user-guide.md). The Markdown prompts are canonical. After editing one, regenerate and verify derived artifacts:

```bash
cd /path/to/regulatory-ingredients-labels-laws
make prompts-normalize
make prompts-sync
make prompts-check
```

## development

```bash
cd /path/to/regulatory-ingredients-labels-laws
make test
```

`make test` validates Markdown contracts, the Regwatch data model, end-to-end command behavior, and prompt manifests. See [CONTRIBUTING.md](CONTRIBUTING.md) for change requirements and [SECURITY.md](SECURITY.md) for responsible disclosure.
