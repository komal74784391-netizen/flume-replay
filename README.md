# Signal Drift Audit

Status: **Released** - v1.0.0 (2026-09-30)

A toolkit for auditing slow drift in long-horizon sensor meshes.  It ingests
multi-channel time series, estimates baseline behaviour with a robust rolling
median, and reports per-channel drift scores.

## Implementation

- `src/drift_audit/core.py` - stream loading and rolling baseline estimation
- `src/drift_audit/metrics.py` - drift score and error metrics
- `data/manifest.csv` - example stream manifest
- `experiments/calibration_report.md` - calibration experiment notes

## Quick start

```bash
python -m drift_audit.core data/manifest.csv
```

## Citation

Cite the NRS 2027 proceedings entry if you use this toolkit.
