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
      `[~]` **CLAIMED 2026-09-25 0705 UTC for the review run** (wt:
      review-batch-0925; brief
      `docs/reviews/2026-09-25-0715-single-sourced-file-walk-cold.md`) by a
      Mike-opened `claude-fable-5-1` session ("Please deliver all fable
      dependent work, and work that would be best delivered using fable") that
      authored none of the delta. Shape, disclosed per rule 4:
      reviewer-plus-orchestrator, both seats Fable — this session writes the
      refs-only brief and holds the `.deferred.md` sibling outside the worktree;
      a fresh Fable subagent it spawns forms every finding and severity. The
      sibling, the intent record and prior verdicts stay unopened by the
      reviewer until its phase-1 findings are committed. Provenance and exposure
      go in the verdict.
      - [ ] 🎯 **The pass RAN 2026-09-26; the cycle CLOSES on this pass (no
            MAJOR) — what remains is decided into the backlog.** The rule-4
            Fable cold pass (taker: a fresh `claude-fable-5-1` subagent under a
            `claude-fable-5-1` orchestrator — the shape disclosed in the claim
            above; the sibling, the intent record and prior verdicts opened only
            after the phase-1 findings were committed) returned
            PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE · 5 minor · 5 note →
            [`2026-09-25-0715-single-sourced-file-walk-cold.md`](../../reviews/2026-09-25-0715-single-sourced-file-walk-cold.md)
            (sibling folded in and deleted). FW1 (MODERATE, pre-existing, now
            single-sourced): the shared walk's is_file() probe raises
            PermissionError on an unreadable child directory under every Python
            before 3.14 (verified live on 3.9, confirmed from CPython source for
            3.12 and 3.13), so all eleven guards abort with a traceback instead
            of a report; FW3 (MODERATE): no test imports filewalk, so the
            next-correction-is-cheaper claim holds for code but not for proof;
            FW8 (MODERATE): seven of eleven guards silently skip an unreadable
            file and report clean; FW12/FW13 formed at reconcile — the pointer's
            intent record carries no account of this delta. Findings are the
            principal's to decide (rule 3); nothing was applied.
