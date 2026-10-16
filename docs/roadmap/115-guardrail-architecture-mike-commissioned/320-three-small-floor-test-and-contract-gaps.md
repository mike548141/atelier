- [ ] 🔎 **Three small gaps in the floor's tests and count contract**
      `[S][tools]`. Found 2026-10-16 by the `290` worker, not fixed there:
      1. `tools/test_floor.py` (its head comment, about lines 14–18) says
         only the prose-hygiene checks may re-baseline. sizescan,
         publishscan and now licenscan have advisory forms. `floor.py`'s own
         docstring already carries the correction (AP2); the test comment
         does not.
      2. `floor.py`'s selftest (about lines 2007–2012) pins only secretscan,
         leakscan, linkscan and reviewscan as checks a child cannot soften.
         conflictscan, board and licenscan are not pinned there. Check
         whether `test_floor.py` covers them before adding anything.
      3. `ADVISORY_COUNT_RX` matches any `advisory: N finding(s)` text, so
         the board's advisory count rests on each scanner's wording rather
         than on a scanner-specific prefix. Two scanners now print it.
      **The work:** 1 is a plain fix. 2 and 3 need a check first.
