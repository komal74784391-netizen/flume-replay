# Flume Replay

Status: **Released** - v1.2.0 (2026-10-02)

Deterministic replay of recorded edge streams.  The library preserves ordering,
timestamps and per-record metadata so that replay runs can be compared exactly.

## Layout

- `src/flume_replay/replay.py` - reader, replayer and checkpoints
- `data/sample_streams.json` - two short example streams
- `experiments/throughput.md` - throughput experiment notes
