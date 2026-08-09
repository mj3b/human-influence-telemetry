# Reproducible Figures

The v0.6.5 research-integrity figure is generated from the audited claim map.

```bash
python scripts/run_research_integrity_audit.py
python scripts/run_research_integrity_audit.py --check
```

The generator writes derived CSV data, an SVG figure, the audit result, its narrative report, and a figure manifest. The check mode compares regenerated content with the committed files and fails on drift.
