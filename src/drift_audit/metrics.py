"""Drift and error metrics."""

from typing import Sequence


def mean_absolute_error(predicted: Sequence[float], actual: Sequence[float]) -> float:
    if len(predicted) != len(actual):
        raise ValueError("length mismatch")
    if not actual:
        return 0.0
    return sum(abs(p - a) for p, a in zip(predicted, actual)) / len(actual)


def drift_score(baseline: Sequence[float], observed: Sequence[float]) -> float:
    """Normalised last-point deviation from the baseline."""
    if not baseline or len(baseline) != len(observed):
        raise ValueError("baseline and observed series must match")
    scale = max(1e-9, abs(baseline[0]))
    return abs(observed[-1] - baseline[-1]) / scale
