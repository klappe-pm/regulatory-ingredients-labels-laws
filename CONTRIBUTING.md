# contributing

Contributions are welcome for reproducible improvements to the regulatory register, sources, scripts, documentation, and prompt library.

## before-you-submit

- Keep every regulatory claim linked to an authoritative primary source. Clearly label secondary summaries and unverified candidates.
- Do not add personal data, confidential client information, credentials, local paths, raw source bundles, editor settings, or generated runtime state.
- Preserve the human-review boundary. Detection and ingestion can flag candidates, but must not edit curated regulatory records automatically.
- Keep changes focused. Add regression coverage when a bug can recur.

## verification

Run the full local suite before opening a pull request.

```bash
cd /path/to/regulatory-ingredients-labels-laws
make test
```

Prompt changes also require `make prompts-normalize` and `make prompts-sync`. Do not alter a prompt's fenced `prompt` artifact without regenerating the manifests and optional Word export.

## style

Use plain language. Keep regulatory status, evidence quality, and uncertainty explicit. This project provides research support, not legal conclusions or label approval.
