- [ ] 🔎 **Two of the three `⏳` pointers on this board have already been taken
      and verdicted, and one of their cycles is CLOSED** — yet both still lead
      with the glyph a future taker greps to find work. The floor-render batch's
      pointer opens `⏳ Rule-4 review queued` and carries
      `- [ ] 🎯 Cycle CLOSED 2026-08-09 (0 MAJOR)` as a folded sub-bullet
      beneath it. The EP-application pointer is the same shape, though its cycle
      legitimately stays open on AP1.
      **Why `pointerscan` is silent, and it is by design rather than by bug:**
      `cycle_findings` makes **order the discriminator** — it flags only when the
      review-has-run evidence stands *before* the claim, on the documented ground
      that "an author states the current state first and the history after", and
      that heuristic was measured as removing three false positives over the
      history. This layout inverts the assumption: the lead states `⏳` while the
      *current* state is CLOSED, so the guard reads a stale pointer as a healthy
      one citing its provenance. The tool's own docstring already admits a
      "stated residual, not defended against" — this is a second, different one.
      🛑 **The risk is not theoretical and the precedent is the same day.** A
      `⏳` with no visible verdict is what LIVE looks like, and C5 was
      **double-run on 2026-08-09** by a session that read exactly that signal
      wrongly — a whole duplicated Fable pass. A closed cycle wearing the queue
      glyph is the inverse trap and costs the same way.
      🤔 **Three shapes, and the choice is not obvious.** (a) A convention that a
      taken pointer loses the `⏳` at verdict-landing, which is bookkeeping
      discipline with no mechanism behind it — the class this board has already
      recorded five times. (b) Teach the detector that a `⏳` **lead** plus
      closed-state evidence anywhere in the item is a contradiction regardless of
      order, accepting whatever false positives the order rule was buying. (c) Give
      a taken-but-open pointer its own glyph, so `⏳` means *untaken* and only ever
      that — which is the cheapest thing for a human grep and the most invasive to
      the vocabulary.
      ✅ **CONFIRMED by probe, 2026-08-18 (scratch board, both directions).**
      The reading above is now measurement: a pointer with the claim in its
      lead and the verdict evidence in a sub-bullet scans clean; the same
      content reordered — evidence before the claim — fires
      `[cycle] says a review is owed while carrying its own verdict` exactly
      as the docstring describes. Two sharpenings the probe adds: on the
      split board the state line is by definition the item's **first** line,
      so a pointer whose lead carries the claim can *never* present
      evidence-first — the order heuristic is structurally unable to fire on
      the lead-claim shape, which is now the house convention for taken
      pointers (the FR, EP, BW and PT pointers all use it); and pointerscan
      is warn-only on both planes, so even a firing finding never blocks.
      The choice between shapes (a)/(b)/(c) above is now priced on confirmed
      behaviour and stays Mike's.
