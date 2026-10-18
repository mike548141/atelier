- [ ] 🎯 **Rule-4 cold pass queued: the staged diff read by its structure
      (`115/280`).** The run authored this itself (its dispatched worker's
      output counts as the run's authorship). It is queued at landing, and
      the run neither takes it nor spawns a reviewer for it. *Tier:* Fable,
      the principal-named review tier, checked at selection. *Pass type:*
      code cold pass, per `method/REVIEW.md` rule 4. *Delta, scoped to
      paths:* `tools/report.py`, `tools/secretscan.py`, `tools/conflictscan.py`,
      `tools/leakscan.py`, their tests and `tools/README.md`, commit
      `39a74b9` and merge `ef75803`, landed on `main` on 2026-10-16.
      *Intent record:*
      [`../../sessions/2026-10-16-0703-queue-run-after-the-sizescan-ruling.md`](../../sessions/2026-10-16-0703-queue-run-after-the-sizescan-ruling.md).
      **Brief WRITTEN 2026-10-17, review NOT run** —
      `docs/reviews/2026-10-17-0930-staged-diff-structure-cold.md` with a
      `.deferred.md` sibling. Written by an Opus brief-writer that authored none
      of the delta (dispatched by the Mike-opened Fable review session, wt
      atelier-review-1017), on Mike's 2026-10-16 answer that a fresh Opus
      session writes these briefs; its exposure is disclosed in the brief. The
      pass stays queued for a further criterion-passing cold Fable session.
      `[~]` **CLAIMED 2026-10-17 2319 UTC for the review run** (a cloud
      session with no worktree: the container's one checkout, branch
      `claude/review-work-briefs-adj6ad`, landed on `main` by PR before any
      pass runs; brief `2026-10-17-0930-staged-diff-structure-cold.md`,
      written 2026-10-17 by a non-author Opus brief-writer under a different
      session) by a Mike-opened `claude-fable-5-1` cloud session ("As a cold
      session please do any review work, any work that is fable dependent, and
      write briefs for any reviews that need them") that authored none of the
      delta and none of the brief, and was not started or instructed by
      either; it opened on `claude-opus-5` and Mike switched it to
      `claude-fable-5-1` before any claim or pass. Shape, disclosed per rule
      4: reviewer-plus-orchestrator, both seats Fable — this session holds the
      `.deferred.md` sibling outside the checkout and outside the harness
      scratchpad, and commits the records; a fresh Fable subagent it spawns
      forms every finding and severity. The sibling, the intent record and
      prior verdicts stay unopened by the reviewer until its phase-1 findings
      are committed. Provenance and exposure go in the verdict.
      - [ ] 🎯 **The pass RAN 2026-10-17/18 UTC; the cycle CLOSES on this pass
            (no MAJOR) — what remains is decided into the backlog.** The rule-4
            Fable cold pass (taker: a fresh `claude-fable-5-1` subagent under a
            `claude-fable-5-1` cloud orchestrator — the shape disclosed in the
            claim above; the sibling, the intent record and prior verdicts
            opened only after the phase-1 findings were committed, `5f3e3b8`)
            returned PASS-WITH-FINDINGS — 0 MAJOR · 5 MODERATE · 2 minor ·
            4 note →
            [`2026-10-17-0930-staged-diff-structure-cold.md`](../../reviews/2026-10-17-0930-staged-diff-structure-cold.md)
            (sibling folded in and deleted). SX1 (MODERATE): the new
            fail-closed path refuses a legitimate diff whenever
            `diff.suppressBlankEmpty=true` meets a fused hunk (via
            `diff.interHunkContext` or `GIT_DIFF_OPTS`, which overrides the
            pinned `--unified=0`), so all three blocking guards exit 2 with a
            message that names no remedy and steers to `--no-verify`; one
            `-c diff.suppressBlankEmpty=false` pin closes both routes. The other
            four MODERATEs are pre-existing holes the delta single-sourced
            without closing. SX11 (note) formed at reconcile; the delta builds
            the 2026-10-04 pass's LN1 counsel and closes its LN5, neither yet
            recorded against those findings. Findings are the principal's to
            decide (rule 3); nothing was applied.
