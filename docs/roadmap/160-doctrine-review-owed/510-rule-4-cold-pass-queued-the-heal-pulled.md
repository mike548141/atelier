- [ ] 🛑 **Rule-4 cold pass queued: ccarchive's heal pulled (`210/170`,
      MC1).** The run authored this itself. It was queued at landing, and
      the run neither takes it nor spawns a reviewer for it. *Tier:* Fable,
      the principal-named review tier, checked at selection. *Pass type:*
      code cold pass, per `method/REVIEW.md` rule 4. *Delta, scoped to
      paths:* `instruments/ccarchive`, `instruments/ccarchive.test.js` and
      `instruments/man/ccarchive.1`. It landed on `main` on 2026-10-03.
      *Intent record:*
      [`../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`](../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md).
      `[~]` **CLAIMED 2026-10-04 2215 UTC for the review run** (wt: review-1004;
      brief `docs/reviews/2026-10-04-2215-ccarchive-heal-pulled-cold.md`) by a
      Mike-opened `claude-fable-5-1` session ("Do all cold reviews and any other
      work dependent on fable") that authored none of the delta. Shape,
      disclosed per rule 4: reviewer-plus-orchestrator, both seats Fable — this
      session writes the refs-only brief and holds the `.deferred.md` sibling
      outside the worktree; a fresh Fable subagent it spawns forms every finding
      and severity. The sibling, the intent record and prior verdicts stay
      unopened by the reviewer until its phase-1 findings are committed.
      Provenance and exposure go in the verdict.
      - [ ] 🛑 **The pass RAN 2026-10-04 and the cycle stays OPEN — a MAJOR
            stands.** The rule-4 Fable cold pass (taker: a fresh
            `claude-fable-5-1` subagent under a `claude-fable-5-1` orchestrator
            — the shape disclosed in the claim above; the sibling, the intent
            record and prior verdicts opened only after the phase-1 findings
            were committed) returned PASS-WITH-FINDINGS — 3 MAJOR / 6 MODERATE /
            3 minor / 3 note →
            [`2026-10-04-2215-ccarchive-heal-pulled-cold.md`](../../reviews/2026-10-04-2215-ccarchive-heal-pulled-cold.md)
            (sibling folded in and deleted). HL1: pulling the heal fixed the
            reported case, but the skip-path backfill beside it still takes a
            missing manifest entry from the source, so a shorter source can be
            recorded as truth and overwrite an intact mirror at exit 0. Findings
            are the principal's to decide (rule 3); nothing was applied.
      - [ ] 🔧 **Findings built 2026-10-05 in `210/210` (merge `8540a1d`),
            after Mike's rulings walk; the cycle stays open until the
            re-review at `⏳ 160/670` runs.**
