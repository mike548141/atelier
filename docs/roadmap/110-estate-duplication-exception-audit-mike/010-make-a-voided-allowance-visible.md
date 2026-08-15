- [ ] **Make a voided allowance visible.** The fix above closes the known
      cause; it does not close the class. A marker that parses as nothing is
      indistinguishable from no marker, so the next parser gap will also be
      silent. Cheapest honest answer: when a line carries the marker *string*
      but no allowance is recognised, say so — a one-line "marker present but
      unparseable" note beside the finding, which is where the reader already
      is. Recurrence, not severity, earns the check (`PROPAGATION.md` rung 2);
      this is instance one, so it is queued rather than built.
