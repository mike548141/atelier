- [x] **The unreasoned advisories are already in hand — do not re-file.**
      Eight bare-list `advisory` declarations across six repos carry no reason
      and no expiry (`Baby Brain`, `FoodTracker`, `ec2_builder`,
      `hitchbots_guide`, `homenetwork` `wrapscan`; `docker-heap` `sizescan`;
      `nova` `sizescan` + `wrapscan` + `spellscan`). The board already names
      each one *"pre-C1 declaration, migrate it"*, and **C1b/C2 are claimed and
      in flight** with Mike's `review-by 2026-09-01` horizon already set. Listed
      here only so a later sweep recognises them as covered rather than missed.

      ✅ **Closed 2026-10-05 — a pointer, with no work of its own** (queue run,
      Opus 5.5). This item existed only so a later sweep would recognise these
      declarations as covered. The work is carried by `020/070` (C1b) and
      `020/080` (C2), and by each child's own re-baseline. Closing it removes
      a line that read as open work and was not.
