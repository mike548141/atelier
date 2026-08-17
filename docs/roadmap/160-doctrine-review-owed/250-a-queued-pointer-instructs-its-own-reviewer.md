- [ ] **A queued pointer at `240` instructs its own reviewer, and `pointerscan`
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
