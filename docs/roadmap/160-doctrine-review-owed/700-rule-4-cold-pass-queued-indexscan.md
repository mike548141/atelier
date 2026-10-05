- [ ] ⏳ **Rule-4 cold pass queued: `indexscan`, the generic index-integrity
      guard (`200/010`).** The run authored this itself (its dispatched
      worker's output counts as the run's authorship). It is queued at
      landing, and the run neither takes it nor spawns a reviewer for it.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4. *Delta,
      scoped to paths:* `tools/indexscan.py`, `tools/test_indexscan.py`,
      `tools/floor.py`, `tools/README.md`, `tools/test_allowmarker.py`,
      `tools/test_mixed_root.py`, and the declaration and allow-marker lines
      in `docs/decisions/README.md`, `instruments/README.md` and
      `docs/SESSIONS.md`, from `8d10487` to the merge that landed it on
      `main` on 2026-10-05. *Intent record:*
      [`../../sessions/2026-10-05-1120-queue-run-closes-and-builds.md`](../../sessions/2026-10-05-1120-queue-run-closes-and-builds.md).
