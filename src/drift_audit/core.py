"""Core stream loading and rolling baselines."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from statistics import median
from typing import Iterable, List


@dataclass
class Channel:
    name: str
    samples: List[float]


def load_manifest(path: str) -> List[Channel]:
    channels: List[Channel] = []
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            values = [float(v) for v in row["samples"].split("|")]
            channels.append(Channel(name=row["channel"], samples=values))
    return channels


def rolling_baseline(values: Iterable[float], window: int = 15) -> List[float]:
    series = list(values)
    if window < 1:
        raise ValueError("window must be positive")
    out: List[float] = []
    for index in range(len(series)):
        start = max(0, index - window + 1)
        out.append(median(series[start : index + 1]))
    return out
