- [x] **A queued pointer at `240` instructs its own reviewer, and `pointerscan`
      says so** `[XS][docs]` — surfaced 2026-08-17 by a session working elsewhere
      in the tree; **queued, not fixed**, because the pointer is another
      session's and the repair is a judgement about what that author meant to
      say.
      `docs/roadmap/160-doctrine-review-owed/240-rule-4-cold-pass-queued-coldsweep.md`
      carries *"🚩 The reviewer should weigh one thing the author cannot: …"*.
      `pointerscan` reports it as `[grammar] instructs the reviewer` — refs-only
      is the pointer's ceiling, and steering the pass before a brief exists to
      defer the steer is the failure it names. Advisory, so it never blocked the
      commit that wrote it.
      ⏱️ **The cheap moment has passed, which is the point worth keeping.**
      `pointerscan`'s own message says a pointer is fixable in the commit that
      writes it, *"the one moment the fix costs nothing"* — and the finding is
      warn-only, so nothing stopped that commit. This is the third pointer
      grammar instance; the tool exists because restating the rule did not work,
      and it still reports rather than blocks.
      **The judgement the author owns:** whether the weighed consideration moves
      into the intent record (where the reviewer's deferral discipline governs
      when it is read) or the pointer takes a `pointerscan:allow:` with a stated
      reason. Both are legitimate; a third session picking one for them is not.

      ✅ **Closed 2026-09-18 — resolved by its author's own session, not this
      one.** `419fdac` (the SW reconcile, 2026-08-18) rewrote `240` and removed
      the instructing line outright; verified: `git show 419fdac` deletes it,
      `240` no longer contains it, and `pointerscan` is clean at HEAD. The
      author chose neither option named above — the steer simply left the
      pointer. The standing half (`pointerscan` warns, never blocks) is
      unchanged and remains the programme's F1 posture question, not this item's.
