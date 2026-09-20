- [ ] 🎯 **MISSING HOUSE RULE — a check in the same shell invocation as the
      act it guards is not a check, and this house has no rule saying so**
      `[M][doctrine]` — filed from a private child via § *Pointing up*,
      2026-09-20, with a fifth instance produced by atelier's own orchestrating
      session the same evening. The child holds this as its most-cited local
      rule, **ruled by the principal 2026-09-06**; atelier does not hold it at
      all.

      ## The rule as the child carries it

      > **NEVER put a check in the same shell invocation as the act it guards —
      > ANY act, not only a destructive one.** A guard whose output nobody
      > reads before the act is not a guard. Run the check as its own command,
      > read the output, then act.

      The principal's 2026-09-06 ruling **widened his own earlier one**, which
      had said *destructive*. He widened it after the failure recurred four
      more times, one of them a plain `git commit` that destroyed no file at
      all and still swept a live peer's staged work. That widening is the part
      atelier most needs, because the narrow version would not have caught the
      instance below.

      ## Five instances, four the child's and one atelier's own

      1. **`&&`-chained.** The check printed its warning and the chained
         `reset --hard` ran anyway, destroying a live peer's uncommitted file.
      2. **A pipe eats the exit code.** `cmd | tail` reports `tail`'s status,
         so a red gate reads as green.
      3. **A persisting `cd`.** The working directory carries into the next
         command, so the act lands in a repo nobody checked.
      4. **The inverse — a clean index is a claim about the past.** The check
         *was* read, four explicit paths staged and verified, and the commit
         still swept three of a live peer's staged files, because they staged
         theirs in the one-to-four-minute gap while the slow floor ran.
      5. 🔎 **Atelier's own, 2026-09-20, the batched-read variant of (1).** This
         session read `gh pr view 83 --json state,mergedAt` and
         `git push origin --delete <branch>` **in one batched command**, so the
         `state: OPEN, mergedAt: null` that should have stopped the delete
         resolved *after* it. The peer had pushed a commit to that branch in the
         interim, and for about a minute it existed nowhere this session held.
         Recovered from GitHub's retained `refs/pull/<n>/head`; nothing lost,
         and the recovery is luck about a forge's retention policy, not a
         control. **A precondition read in the same command as the act it
         guards is not a precondition.**

      ## Why the nearest existing clause does not cover it

      `CONCURRENCY.md` § *Integration hygiene* carries **"Verify the act, not
      the absence of an error"** — confirm a commit by `git log`, a push by the
      remote ref, a write by the file. That rule is about **after**: did the
      act I intended actually happen. This one is about **before**: did I read
      the gate's answer while I could still not act. They are adjacent and they
      are not the same, and instance (5) passed the existing rule cleanly —
      the delete was verified to have happened. It should not have happened.

      ## The remediation the child reports made the class disappear

      Offered as reported rather than as this item's prescription — commit
      with a **pathspec** on any shared checkout, and land a worktree by
      `git merge --ff-only` from the clean primary rather than by moving refs,
      because that moves ref and tree together. Both are already house practice
      here in part — the pathspec half was adopted mid-run on 2026-09-19 — but
      as tool-specific habits, not as the general rule that explains them.

      ## The ask

      Decide whether atelier adopts the child's rule as house doctrine, and
      where it attaches — it is not obviously CONCURRENCY's, since only two of
      the five instances involve a peer at all; the other three are a lone
      session deceiving itself. `EVIDENCE.md` is the other candidate, on the
      reading that this is a rule about **when a reading counts as evidence**
      rather than about concurrency.

      ⚠️ **What is not established:** whether the class is mechanisable. Nothing
      here inspects a session's shell invocations, and a rule with no forcing
      function is the class `020/220` exists to count. Filed as the defect and
      the ask, deliberately not as the patch.
