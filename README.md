# ASM-master
Master of anti-seizure medications

## Agentic update check

`scripts/agentic_update_check.py` audits `ASM-list.csv` one drug row at a
time. By default it runs through the local Codex CLI and uses the currently
logged-in ChatGPT/Codex account, not an `OPENAI_API_KEY`.

Single-row Codex audit:

```bash
python3 scripts/agentic_update_check.py --row brivaracetam
```

Preview bundle/report generation without a model call:

```bash
python3 scripts/agentic_update_check.py --backend preview --row brivaracetam
```

Reports are written to `pubmed_cache/reports/agentic_update_check/`. The script
does not edit `ASM-list.csv`; it writes findings and an approval template for
review before any future updater applies changes.
