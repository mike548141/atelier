- [ ] 🛑 **Rule-4 cold pass queued: ccarchive's manifest checkpoints and
      stale-entry heal (`210/170`).** The run authored this itself (its
      dispatched workers' output counts as the run's authorship). It was
      queued at landing, and the run neither takes it nor spawns a reviewer
      for it. *Tier:* Fable, the principal-named review tier, checked at
      selection. *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `instruments/ccarchive`,
      `instruments/ccarchive.test.js` and `instruments/man/ccarchive.1`. It
      landed on `main` on 2026-10-03, in merge `0264387`.
      *Intent record:*
      [`../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`](../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md).
      `[~]` **CLAIMED 2026-10-03 0357 UTC for the review run** (wt:
      `atelier-review-430`, branch `review-430-1003`; brief
      `docs/reviews/2026-10-03-0357-manifest-checkpoints-cold.md`)
      by a Mike-opened `claude-fable-5-1` session ("Do all cold reviews and any
      other work dependent on fable") that authored none of the delta and was
      not started or instructed by the authoring run. Shape, disclosed per rule
      4: reviewer-plus-orchestrator, both seats Fable — this session writes the
      refs-only brief and holds the `.deferred.md` sibling outside the worktree
      and outside the harness scratchpad; a fresh Fable subagent it spawns forms
      every finding and severity. Disclosed exposure: the authoring run told
      this session, over the cross-session channel, that the pointer existed
      and named its subject in a phrase; nothing else from it was read. The
      sibling, the intent record and prior verdicts stay unopened by the
      reviewer until its phase-1 findings are committed. Provenance and
      exposure go in the verdict.
      - [ ] 🛑 **The pass RAN 2026-10-03 and the cycle stays OPEN — two MAJORs
            stand.** The rule-4 Fable cold pass (taker: a fresh
            `claude-fable-5-1` subagent under a `claude-fable-5-1` orchestrator
            — the shape disclosed in the claim above; the sibling, the intent
            record and prior verdicts opened only after the phase-1 findings
            were committed) returned PASS-WITH-FINDINGS — 2 MAJOR · 2 MODERATE ·
            4 minor · 2 note →
            [`2026-10-03-0357-manifest-checkpoints-cold.md`](../../reviews/2026-10-03-0357-manifest-checkpoints-cold.md)
            (sibling folded in). MC1 (MAJOR): the heal refreshes the manifest
            from the source, not the mirror; driven, a restored-from-backup
            source makes `--verify` report a mismatch on an intact mirror for
            ever, and a truncate-then-append with a preserved mtime lowers the
            recorded size, slips the 2026-07-17 shrink guard and overwrites the
            good copy with `--verify` green — the ruled F1 re-opened by a side
            door. MC2 (MAJOR, pre-existing, surfaced by a real SIGKILL): mirrors
            are written in place, so a torn archive gets a newer mtime, is never
            re-archived, is backfilled from the source's hash, and makes
            `--verify` crash. MC3–MC4 (MODERATE): the in-loop checkpoint is
            untested; the man page's "every written mirror covered" holds for a
            throw, not a hard kill. The reviewer recovered from the review
            worktree lacking the delta at spawn (MC8); the orchestrator merged
            `main` in mid-pass. Findings are the principal's to decide (rule
            3); nothing was applied.
      - [ ] 🔧 **Findings built 2026-10-05 in `210/210` (merge `8540a1d`),
            after Mike's rulings walk; the cycle stays open until the
            re-review at `⏳ 160/670` runs.**
