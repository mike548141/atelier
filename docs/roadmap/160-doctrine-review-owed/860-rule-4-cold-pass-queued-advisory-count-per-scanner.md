- [ ] ⏳ **Rule-4 cold pass queued: the floor's advisory count scoped to its
      scanner, and three more unsoftenable pins (`115/320`).** The run authored this itself (its dispatched worker's
      output counts as the run's authorship). It is queued at landing, and
      the run neither takes it nor spawns a reviewer for it. *Tier:* Fable,
      the principal-named review tier, checked at selection. *Pass type:*
      code cold pass, per `method/REVIEW.md` rule 4. *Delta, scoped to
      paths:* `tools/floor.py`, `tools/test_floor.py` and a comment in
      `tools/licenscan.py`, commit `dc0ed0e` (cherry-picked from the worker's
      `fe4f20d`), landed on
      `main` on 2026-10-16.
      *Intent record:*
      [`../../sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md`](../../sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md).
