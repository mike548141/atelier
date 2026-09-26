- ⏳ **Rule-4 cold pass queued — the scratch-space clause: a worker's worktree
      isolates the repo and not the scratchpad, so the dispatch prompt carries
      the obligation.** Self-authored by the run that measured it; queued at
      landing, and the run neither takes nor spawns it. *Tier:* Fable, the
      principal-named review tier — checked at selection; a session that cannot
      honour the bar stops rather than takes. *Pass type:* doctrine cold pass,
      per `method/REVIEW.md` rule 4. *Delta — scoped to paths:*
      `docs/method/CONCURRENCY.md` § *Orchestrated queue runs*, the paragraph
      following *What a worker inherits is bounded*. Landed on `main`,
      2026-09-20.
      **The lenses that matter most here:** whether a prompt obligation is the
      right instrument at all when no check can see a worker's scratch writes,
      given `370`'s own finding that an unenforced rule is the class this
      estate keeps re-breaking; whether the clause's stated expiry — spent if
      the harness namespaces scratch per agent — is a real condition a future
      reader can evaluate, or an escape hatch; and whether the grounding is
      strong enough for the claim's width, given that the measurement covers
      one harness on one machine on one day; and whether the clause's retained
      provenance note earns its place, given that the artefacts it rests on
      were **wrongly attributed for about an hour and the first published
      version of the clause rested on that error** — the reviewer should treat
      the corrected attribution as itself a claim to check, not a settled fact
      restored.
      *Intent record:*
      [`../../sessions/2026-09-20-1053-queue-run-the-loose-ends.md`](../../sessions/2026-09-20-1053-queue-run-the-loose-ends.md).
      `[~]` **CLAIMED 2026-09-25 0705 UTC for the review run** (wt:
      review-batch-0925; brief
      `docs/reviews/2026-09-25-0715-scratchpad-clause-cold.md`) by a Mike-opened
      `claude-fable-5-1` session ("Please deliver all fable dependent work, and
      work that would be best delivered using fable") that authored none of the
      delta. Shape, disclosed per rule 4: reviewer-plus-orchestrator, both seats
      Fable — this session writes the refs-only brief and holds the
      `.deferred.md` sibling outside the worktree; a fresh Fable subagent it
      spawns forms every finding and severity. The sibling, the intent record
      and prior verdicts stay unopened by the reviewer until its phase-1
      findings are committed. Provenance and exposure go in the verdict.
      - [ ] 🛑 **The pass RAN 2026-09-26 and the cycle stays OPEN — a MAJOR
            stands.** The rule-4 Fable cold pass (taker: a fresh
            `claude-fable-5-1` subagent under a `claude-fable-5-1` orchestrator
            — the shape disclosed in the claim above; the sibling, the intent
            record and prior verdicts opened only after the phase-1 findings
            were committed) returned PASS-WITH-FINDINGS — 1 MAJOR · 3 MODERATE ·
            3 minor · 3 note →
            [`2026-09-25-0715-scratchpad-clause-cold.md`](../../reviews/2026-09-25-0715-scratchpad-clause-cold.md)
            (sibling folded in and deleted). SK1 (MAJOR): the harness hands each
            reviewer the orchestrator's own scratchpad, so a sibling held there
            is one read away from any reviewer and the clause's harm model omits
            the read surface that bears on the doctrine's highest-stakes review
            shape — this batch's orchestrator moved its siblings out on reading
            the finding; SK10 (note) formed at reconcile. Findings are the
            principal's to decide (rule 3); nothing was applied.
