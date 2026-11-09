- [ ] ⏳ **Rule-4 cold pass queued: `sweepscan`, commits name their files, warn-only with no date (`320/060`).** The authoring session (a
      principal-opened Opus 5.5 queue run, session d0ca5d24, 2026-11-09 UTC,
      which dispatched the worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/sweepscan.py`, `tools/test_sweepscan.py`, its registry entry in `tools/floor.py` — the commit that adds it, on `main`.
      *Questions worth the pass's time:* whether `GIT_INDEX_FILE` is a reliable signal on every commit path; whether the marker can be set and forgotten.
      *Intent record:* `320/060`, `320/810`.
