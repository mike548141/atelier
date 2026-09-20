- [x] 🔥 **`stampscan`'s verdicts are inverted against the doctrine it enforces
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
      🎯→✅ **RULED 2026-09-19 by Mike, via the question device: "Floor copy
      verbatim".** Offered against keeping declared deletions visible but
      red, and against legitimising deletions under a renamed `omits=`. So the
      inlined safety floor is copied word for word: no compression, no
      declared narrowing. `stampscan`'s exact-copy comparison becomes simply
      correct for the floor region. **Owed, together:** (1) doctrine —
      `PROPAGATION.md` drops *"may compress"* for the floor and § *A copy may
      narrow* stops applying to it (a doctrine change, so a rule-4 pointer at
      landing); (2) `stampscan` — `narrow=` on the floor region reds instead of
      passing; (3) the fleet — a child whose floor copy is shortened goes red
      once and restores the canonical text at its next pin bump, which
      `pins`/`floorfleet` should show before it surprises anyone.
      ✅ **DONE 2026-09-20.** (1) Doctrine — `PROPAGATION.md` § *The standard
      child doctrine block* gains a fourth boundary: the floor never narrows,
      and `narrow=` on a `region=floor` stamp reds; the *may compress*
      sentence now says plainly that atelier's own canonical text may
      compress its sources while a child's copy of it is verbatim; § *One
      statement, stamped copies* carries the same carve-out. (2) Scanner —
      `stampscan` reds `narrow=` on the floor, identified by the (`source`,
      `region`) **pair**, because the fixtures and a scaffold legitimately
      reuse "floor" as a generic region name; a byte-equal copy still passes
      and every other drift shape was already red. 6 new unit cases + 2
      end-to-end + 2 selftest cases; no existing test pinned the old passing
      behaviour. (3) Fleet — measured read-only across the siblings: 5 carry
      a floor stamp, 4 already verbatim, **1 declares `narrow=` and goes red
      at its next run**; carried as its own item (`115/200`) rather than
      named here, since atelier is public.
      *review: queued as a code + doctrine cold pass, `160/340`.*
