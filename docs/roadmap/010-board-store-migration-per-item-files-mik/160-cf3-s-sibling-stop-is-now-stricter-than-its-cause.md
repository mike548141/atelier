- [ ] 🎯 **CF3's dirty-sibling stop is now stricter than its cause requires —
      relax it, or restate the reason that survives.** Raised by the session
      that built `010/020`, surfaced rather than decided because it is a change
      to standing doctrine, 2026-09-20.

      ## What changed underneath the rule

      CF3 (`CONCURRENCY.md` § *Claiming at a dirty primary checkout*, ruled
      2026-07-20) says: if a *sibling's* item file is dirty, do not claim from
      that checkout — sync, take the next open item, touch nothing. Part of
      why was mechanical: regenerating the index off the **worktree** could
      absorb that sibling's unstaged state line into the file you were about to
      stage, so a wrong `✅` could land on `main` under a green hook. That is
      BS1's second slip.

      `rebuild --from-index` closes exactly that cause. A claimer at a dirty
      primary checkout can now regenerate from the **staged** plane, and a
      sibling's unstaged edit cannot reach the generated file at all.

      ## The relaxation on offer

      A sibling's dirty edit to a **different** item stops being a stop — run
      `rebuild --from-index` and claim — and only a dirty edit to the **exact
      item being claimed** remains one, which is the same-item collision CF3
      already calls positive proof that the other session is queue-active.

      ## The reason that does NOT go away, and is why this is a ruling

      CF3's stop has a second, independent basis the flag does not touch: **a
      dirty sibling item is evidence a peer is queue-active.** Read that way,
      the rule is not about protecting the index at all — it is about not
      claiming into a queue somebody else is visibly working. The flag makes
      the *mechanical* harm impossible; it says nothing about whether claiming
      beside a live peer is wise.

      So the question is which reading CF3 is: an index-safety rule (now
      over-broad, relax it) or a peer-presence rule (unchanged, and its index
      rationale was only ever the lesser half). Both readings are supportable
      from the text, which is itself a finding about the text.

      ## What is at stake either way

      **Relaxing** buys throughput: the flipped prior says to *expect* company,
      so under the current rule a session meeting any dirty sibling item takes
      the next item instead — and with 200+ open items and several sessions a
      night, that is a real and recurring cost paid for a hazard that no longer
      exists. **Not relaxing** keeps a conservative stop whose cost is one
      skipped item and whose benefit is never racing a peer's live queue work.

      ⚠️ Not measured: how often the dirty-sibling case actually fires. Nothing
      records a skipped claim, so the throughput cost above is reasoned, not
      counted — and a ruling that turns on it should say so.
