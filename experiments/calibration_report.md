# Calibration report

Runs on 2026-09-18 with the reference bench data.

| stream | window | drift score | MAE |
| --- | --- | --- | --- |
| temp_a | 15 | 0.104 | 0.18 |
| temp_b | 15 | 0.021 | 0.06 |
| humidity_a | 15 | 0.083 | 0.91 |
| pressure_a | 15 | 0.006 | 0.02 |

The audit flags `temp_a` and `humidity_a` as drifting beyond the 0.05 threshold.
