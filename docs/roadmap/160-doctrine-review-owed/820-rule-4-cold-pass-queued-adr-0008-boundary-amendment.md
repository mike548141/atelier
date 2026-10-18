- [ ] 🛑 **Rule-4 cold pass queued: ADR 0008's boundary amendment and the
      ruleset bypass removal (`140/020`, AR1).** The run authored this
      itself. It is queued at landing, and the run neither takes it nor
      spawns a reviewer for it. *Tier:* Fable, the principal-named review
      tier, checked at selection. *Pass type:* doctrine cold pass, per
      `method/REVIEW.md` rule 4, with a live platform read. *Delta, scoped
      to paths:* `docs/decisions/0008-enforcement-is-called-not-copied.md`,
      its section "Amended 2026-10-16", and the `main` ruleset's
      `bypass_actors`, the commit that closes `140/020` on 2026-10-16.
      *Intent record:*
      [`../../sessions/2026-10-16-0703-queue-run-after-the-sizescan-ruling.md`](../../sessions/2026-10-16-0703-queue-run-after-the-sizescan-ruling.md).
      **Brief WRITTEN 2026-10-17, review NOT run** —
      `docs/reviews/2026-10-17-0955-adr-0008-boundary-amendment-cold.md` with a
      `.deferred.md` sibling. Written by an Opus brief-writer that authored none
      of the delta (dispatched by the Mike-opened Fable review session, wt
      atelier-review-1017), on Mike's 2026-10-16 answer that a fresh Opus
      session writes these briefs; its exposure is disclosed in the brief. The
      pass stays queued for a further criterion-passing cold Fable session.
      `[~]` **CLAIMED 2026-10-17 2319 UTC for the review run** (a cloud
      session with no worktree: the container's one checkout, branch
      `claude/review-work-briefs-adj6ad`, landed on `main` by PR before any
      pass runs; brief `2026-10-17-0955-adr-0008-boundary-amendment-cold.md`,
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
      - [ ] 🛑 **The pass RAN 2026-10-17/18 UTC and the cycle stays OPEN — a
            MAJOR stands.** The rule-4 Fable cold pass (taker: a fresh
            `claude-fable-5-1` subagent under a `claude-fable-5-1` cloud
            orchestrator — the shape disclosed in the claim above; the sibling,
            the intent record and prior verdicts opened only after the phase-1
            findings were committed, `52600db`) returned PASS-WITH-FINDINGS —
            1 MAJOR · 3 MODERATE · 4 minor · 1 note →
            [`2026-10-17-0955-adr-0008-boundary-amendment-cold.md`](../../reviews/2026-10-17-0955-adr-0008-boundary-amendment-cold.md)
            (sibling folded in and deleted). BY1 (MAJOR): the amendment's
            residual-exposure sentence is false in the reassuring direction —
            `required_signatures` with no bypass enforces GitHub-verified, not
            trust-listed, proven live by two commits on `main` since the change
            (a GitHub-minted merge and an SSH key absent from
            `allowed_signers` that the house `signscan` rejects), while the
            ruleset's edit history is owner-readable only and the repo's
            machine check reads neither the bypass list nor the signing rule;
            the same overclaim entered the ADR, the commit body and the intent
            record in one close. BY9 (minor) formed at reconcile; BY2 and BY5
            restate AR2 and AR4, still open on `160/090`'s cycle. The live
            ruleset read was made from the container by anonymous API reads.
            Findings are the principal's to decide (rule 3); nothing was
            applied.
