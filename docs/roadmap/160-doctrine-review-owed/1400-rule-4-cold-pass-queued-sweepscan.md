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
      📝 BRIEF WRITTEN 2026-11-14 by a headless Opus 5.5 brief-writer (session b769469b,
      started by an estate health sweep, orchestrator session 58027096; neither authored this
      delta): `docs/reviews/2026-11-14-0246-sweepscan-commit-names-files-cold.md`, with its
      `.deferred.md` sibling. The delta is one commit, `f9def52d`; `tools/sweepscan.py` and its
      tests are unchanged at HEAD, and the registry entry has gained a `declares=` block since.
      The transcript measurement and the fleet probe are NOT RUN unless the spawning session
      grants read-only access. Pass size: small. Review NOT run: it waits for a
      criterion-passing cold Fable session and the principal's explicit permission for Fable
      work. Neither named session may run it.
