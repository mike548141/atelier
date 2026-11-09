- [ ] ⏳ **Rule-4 cold pass queued: `namescan`, private names in branch names and commit titles, warn-first (`160/360` NP2, `320/810`).** The authoring session (a
      principal-opened Opus 5.5 queue run, session d0ca5d24, 2026-11-09 UTC,
      which dispatched the worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/namescan.py`, `tools/test_namescan.py`, its registry entry in `tools/floor.py` — the commit that adds it, on `main`.
      *Questions worth the pass's time:* whether its name sources can leak through the check itself; whether a private repo's own name in its own history is correctly out of scope.
      *Intent record:* `160/360`, `320/810`.
