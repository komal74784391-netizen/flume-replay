"""Replay recorded streams with deterministic ordering."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Dict, Iterator, List


@dataclass
class Record:
    offset: int
    payload: Dict
    recorded_at: str


def load_stream(path: str, stream_name: str) -> List[Record]:
    with open(path, encoding="utf-8") as handle:
        raw = json.load(handle)
    rows = raw["streams"][stream_name]
    return [Record(offset=r["offset"], payload=r["payload"], recorded_at=r["recorded_at"]) for r in rows]


def replay(records: List[Record]) -> Iterator[Record]:
    for record in sorted(records, key=lambda item: item.offset):
        yield record


def checkpoint(records: List[Record], offset: int) -> Dict:
    return {
        "offset": offset,
        "remaining": sum(1 for record in records if record.offset > offset),
    }
