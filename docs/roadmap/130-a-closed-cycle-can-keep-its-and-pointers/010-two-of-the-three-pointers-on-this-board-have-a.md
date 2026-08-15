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
      ⚠️ **Stated honestly: this is a reading of the detector's docstring plus a
      clean exit code, not a probe.** Nobody has reordered the item to confirm the
      guard fires the other way round. Confirm before pricing a fix. The pointers
      belong to a session that has since closed, so the lane is free.
