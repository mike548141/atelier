- [x] 🎯 **P6 — `rpi` F5: estate-internal context accumulating in public
      records. Mike's ruling owed** (was mis-marked `⏳` — the queue glyph means
      a review is queued for a taker, and what is owed here is a decision;
      re-marked 2026-08-03 on `pointerscan`'s day-one warning). Session logs
      naming sibling repos and their
      scan states; workflow detail published as a matter of course. This repo
      already holds the narrower rule (never join a private repo's *name* to its
      *security posture* — the invariant breached three times); F5 asks the
      wider question: is estate-internal context in a public record **accepted
      transparency** or a records-convention defect? ADR-worthy either way, and
      the ruling binds every repo heading public, not just `rpi`.
      **RULED 2026-08-04 (Mike): it gets the ADR sitting.** An agent drafts
      the ADR with both postures argued and costed (open-estate transparency
      with the name×posture join as the only bar, vs class-level
      estate-internal detail in public records with its writing friction);
      Mike rules in the ADR, nothing changes until then. Work owed: one
      ADR draft item.
      **DRAFTED 2026-08-05** →
      [`2026-08-05-1233-estate-internal-context-in-public-records.md`](../../decisions/2026-08-05-1233-estate-internal-context-in-public-records.md).
      Both postures argued and costed against a measurement of this repo's own
      record, plus a third shape the measurement surfaced (bind by surface, not
      by repo). Three results move the decision: the exposure is ~96% a
      *records* phenomenon and ~4% doctrine, so the friction lands on session
      closes; the narrow join rule is broadly holding and what accumulates is
      the adjacent name × *operational state* band; and retrofit is unavailable
      (pushed history is permanent), so every option binds forward only. F5's
      second half — published internal *workflow* — is restated from the source
      finding, which the earlier harvest here had dropped; it is not symmetric
      with the first half, because publishing method is this repo's purpose.
      **Remaining: Mike's ruling, written into the ADR's Decision + Rejected
      sections (scheduled 2026-08-09 into the dedicated residue ruling
      sitting)** (left deliberately unfilled — a drafter cannot fill them
      without pre-empting the ruling). Whatever doctrine edit acceptance drives
      is self-authored ⇒ rule-4 `⏳` at *that* landing, not this one.
  - [ ] 💬 **Mike's answer, 2026-11-08 (to options session 722ac2e2 offered in
        its ruling round; an answer, not a ruling):** *"Type-only for private
        state"* — the offered option read: a private repo's internal state is
        described by its type only in a public record ("a private child was
        failing a check"); naming a repo in any other context stays allowed.
        The posture the draft ADR calls C. Binds forward only. Applying it
        fills the ADR's Decision and Rejected sections and the doctrine line,
        which is self-authored, so its landing queues a cold pass.
  - [x] ✅ **DONE 2026-11-09 — APPLIED** by queue run 722ac2e2 (a Sonnet
        worker, read by the orchestrator before landing): the ADR's Decision
        and Rejected sections are filled with posture C, marked as his pick
        from offered options, and `RECORD.md` § *The record is public* gains
        the type-only rule for a private repo's state, pointing at the ADR.
        A type that fits only one repo counts as its name (the drafter's
        reading, marked so in the ADR). A scanner could only prompt, never
        block; the name-by-posture registry item can be re-specified that
        way. Cold pass queued as `160/1090`.
