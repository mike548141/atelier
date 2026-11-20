- [x] (2026-08-03: built, pointerscan landed) **FUNDED (Mike, 2026-07-28) — mechanise the `⏳` pointer grammar.**
      Unclaimed on purpose: this is the work that closes the finding directly
      above, and it wants a session that did not write the breach.

      **A correction to carry, because it changes where this goes.** The first
      sketch said "`reviewscan` is the natural home". It is not, and the
      premise was never checked before being written down — the same shape as
      the two false blockers this programme already records. `reviewscan`
      **explicitly refuses to lint ROADMAP sections**, and that refusal is a
      recorded decision (the 2026-07-18-0820 record), on the grounds that a
      lint demanding structure under every roadmap heading fires on prose and
      gets trained away. Honouring that rejection is in its module docstring.
      The tool that *already* parses `⏳` list items in `ROADMAP.md` is
      **`sizescan`** (`_LIVE_ITEM`, for harvest integrity), and
      `harvestscan.is_pointer()` already isolates pointers from work items —
      two existing building blocks rather than a new tool.

      **First question the work must answer, not assume:** is this the same
      rung the 0820 record rejected? Arguably not — that rejection was about
      demanding a field under *every roadmap heading*, whereas this binds only
      the `⏳` item type, of which there are rarely more than three at a time
      and whose form is formulaic by definition. But that argument is the
      author's, it is exactly the kind that has been wrong here before, and it
      should be tested rather than inherited.

      **What is actually mechanisable.** "A field outside {delta, intent
      record, tier}" sounds crisp and is not detectable — the failure is
      *evaluative* content, which is judgement. What the three real instances
      share is narrower and testable: a **seeded question** or an explicit
      **instruction to the reviewer**. Instance 1 carried *"Aim a reviewer at
      the one real trade … Is that right for a security floor?"*; instance 3
      carried *"the pass's first question is whether …"*. A question mark
      inside a `⏳` item, plus a short phrase list of reviewer-direction
      forms, catches all three.

      **Acceptance corpus — located, not assumed.** Instance 3 is recoverable
      as a pair (`ff8080b` wrote it, `7ca1f1d` stripped it), which gives a
      must-flag and a must-stay-silent version of the same pointer. **Instance
      1 is still LIVE in this file** — the ADR 0008 entry's *"Aim a reviewer
      at the one real trade … Is that right for a security floor?"* — so the
      guard has a real specimen to prove itself against on day one, and a real
      finding to fix. Instance 2 was not located this session; find it or
      record that it could not be found, rather than inheriting "two" on
      faith. **A boundary specimen joined the corpus by the FG6 ruling
      (Mike, 2026-08-03):** the F1 pointer carried *"Design/intent pass per
      REVIEW.md §…"* — an instruction to the reviewer, but a procedural one
      (pass type), not evaluative and not a seeded question. Whether
      pass-type is a lawful fourth field beside {delta, intent record, tier}
      is this build's to settle, decided on the corpus rather than pre-ruled.

      🔎 **And that live specimen already breaks the obvious scoping.** The
      ADR 0008 entry carries a reviewer agenda but is marked `[ ]`, with
      "review owed" *mid-body* rather than in its lead — so a guard scoped to
      the `⏳` marker alone would miss the one instance still standing.
      `harvestscan.is_pointer()` has the same limit (marker, or lead-6-words).
      Settle the scope before the detector: **what makes an item a
      queued-review pointer** is the prior question, and getting it wrong
      makes the check cover nothing while reporting clean — this programme's
      organising defect, which it would be embarrassing to reproduce in the
      guard against reproducing failures.

      **A second detector rides the same scope decision — the stale pointer
      (Mike, 2026-08-03).** The grammar check above asks *what may a pointer
      say*; the same parse answers *is the pointer still true*. An item
      claiming a review is owed while a matching `docs/reviews/` verdict
      exists is a mechanically detectable contradiction. Raised by a `ros`
      session as atelier's call, correctly — the guard is shared-floor, not
      child-local. It needs the same prior question settled and reuses the
      same two building blocks, so this is one build, not two; splitting it
      would make a third original of *what makes an item a queued-review
      pointer*.

      **The count was wrong on first telling, and the corrected count does
      not clear the threshold.** The raising session said four instances and
      read that as past promote-at-three. A sweep of this file found
      **five** — all in § *Doctrine — review-owed*, all from **one commit**
      (`98cef9e`, the nine-pass queue take), which prepended verdicts to nine
      items and stripped the stale wording from only four. One occurrence
      with five residues is not five recurrences: the ladder's threshold is
      **not** met, and the case for wiring rests on the detection being
      near-free once the scope is settled. Recorded this way so a later
      session does not inherit "past the threshold" on faith.

      **The residue named a sharper defect than the one detected.** All five
      said "review queued" when the review had run and what was owed was
      Mike's *ruling*. Existence-of-verdict catches the contradiction; reading
      the cycle states — owed → reviewed → ruled → applied → closed — says
      which state the item is actually in. Which of the two the guard carries
      is the build's to settle. **Acceptance corpus:** the five were cleaned
      in the commit adding this paragraph, giving a must-flag/must-stay-silent
      git pair in the same shape as instance 3's, rather than a live specimen.

      **Advisory first**, whatever the scope: a pointer is fixable in the same
      commit that writes it, so the warning lands at the one moment it costs
      nothing.
