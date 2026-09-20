- ⏳ **Rule-4 cold pass queued — the single-sourced file walk (`115/080`
      part 1).** Self-authored by the run (its dispatched worker's output is
      the run's authorship); queued at landing, and the run neither takes nor
      spawns it. *Tier:* Fable, the principal-named review tier — checked at
      selection; a session that cannot honour the bar stops rather than takes.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4. *Delta —
      scoped to paths:* `tools/filewalk.py` (new), and the `_walk_files`
      wrapper plus dropped `import os` in
      `tools/{secretscan,leakscan,conflictscan,linkscan,sizescan,datescan,`
      `wrapscan,spellscan,pathscan,licenscan,stampscan}.py`. Landed on `main`,
      2026-09-20.
      **The lenses that matter most here:** whether the byte-identical
      before/after evidence is as strong as it reads, given it was taken on
      one tree whose content may not exercise every skip path — a tree with no
      `dist/`, no `build/` and no broken symlinks would show `licenscan`'s
      parameterisation and the `is_file()` filter as identical by accident
      rather than by correctness; whether `skip_dir_names` being accepted as
      any `Iterable` and coerced with `set()` can be passed something whose
      iteration is not repeatable, since the walk consumes it once per call
      but is itself a generator; whether one shared walk makes the **next**
      correction cheaper in fact or merely in principle, which is this item's
      whole justification and is now testable rather than asserted; and
      whether consolidating the walk while leaving four distinct readers
      copied alongside it leaves the codebase more confusing than either
      endpoint, which is `115/220`'s open question reaching back into this
      delta.
      *Intent record:*
      [`../../sessions/2026-09-20-1053-queue-run-the-loose-ends.md`](../../sessions/2026-09-20-1053-queue-run-the-loose-ends.md).
