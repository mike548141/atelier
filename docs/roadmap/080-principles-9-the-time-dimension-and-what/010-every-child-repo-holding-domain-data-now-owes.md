- [ ] **Every child repo holding domain data now owes a §9 pass of its own.** The
      obligation propagates by pointer, not by a sweep run from here, so it lands
      when each child is next worked. Two things worth watching, neither yet
      evidenced: whether pointer-delivery is enough for a *retrofit* obligation
      (the pin carries doctrine reliably, but a retrofit needs someone to
      **notice it applies** to data already shipped), and whether the recurrence
      justifies a machine check. Left deliberately untracked per-repo — if
      children turn out to miss it, that absence is the evidence for mechanising,
      and a premature ledger would hide it.
