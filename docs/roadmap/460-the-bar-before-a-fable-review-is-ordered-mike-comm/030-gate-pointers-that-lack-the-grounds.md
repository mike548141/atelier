- [ ] **Enforce the bar where a machine can: refuse a review pointer that lacks the
      queue-time grounds** `[M][tool]`. Mike, 2026-11-25, verbatim: *"we need work to fix
      that on the board"*. Step 3 of `460/010`, split out.
      Step 1 found nothing checks a pointer's grounds today, so the bar in `460/020` would
      otherwise be one more judgement a session can skip. **Owed:**
      1. `tools/pointerscan.py` (it already polices `⏳` pointer grammar) refuses a new
         `⏳` pointer, and a new `160/` item, that does not carry the three answers from
         `460/020`, and refuses a second open pointer on a subject that already has an
         unrun one (it says which to widen).
      2. The review planner's ranking step (`instruments/ccfleet`, `queue.ranked`) reads
         the same fields and shows, ranked last and marked, any pass queued before the bar
         with no grounds, so a drain spends on grounded passes first.
      3. Existing pointers are not failed retroactively by the scanner; `460/040` handles
         them.
      **Blocked on:** `460/020` landing (the gate checks what that text defines).
      **Review:** a gate that blocks, so it earns its own pass under the new bar's question
      (3): a gate that reads green while not checking fails silent. Fold it into
      `460/020`'s pass if that is still unrun when this lands.
