- [ ] 🔥 **`stampscan`'s verdicts are inverted against the doctrine it enforces
      — a live defect, found once and never fixed.** `PROPAGATION.md` states the
      rule for the exact block `stampscan` reads: the inlined floor is a
      narrowing-free restatement, and each child *may compress but must not
      contradict its source*. So the doctrine **permits compression** and
      **forbids narrowing**. The scanner does the opposite, and the finding
      carries the reproduction: a child that compresses a line goes red for
      drift, because a compressed restatement is neither byte-equal nor an
      ordered subsequence; a child that declares a narrowing and drops lines
      passes clean, because a pure deletion satisfies the subsequence gate.
      Worse than the mechanics: the attribute that grants the green verdict is
      spelled with the parent's own word for *stricter*, so a child author
      declaring it will reasonably believe they are doing the sanctioned thing.
      **Verified at HEAD 2026-08-15** against
      `docs/reviews/withdrawn/2026-07-26-0647-stampscan-s4-cold.md`.
      **Why it is still open:** the pass that found it was rejected in full on
      tier grounds — it ran on the wrong model — and under the withdrawn-review
      convention its findings died with it. See the item below for the
      consequence that has for the convention itself.
      **Scope note:** the accepted pass of the same date caught the neighbouring
      empty-payload hole but not this. Confirmed by search — the accepted
      verdict contains no instance of *invert* or *compress*.
