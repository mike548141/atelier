- [x] 🔎 **Three small gaps in the floor's tests and count contract**
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

      ✅ **Done 2026-10-16** (1501 UTC queue run, a Sonnet 5.5 worker;
      `fe4f20d`, cherry-picked to `main` as `dc0ed0e` after the
      orchestrator read it).
      1. `test_floor.py`'s head comment now mirrors `floor.py`'s docstring.
      2. conflictscan, board and licenscan were pinned nowhere as checks a
         child cannot soften. All seven are now pinned in the selftest and
         in `test_floor.py`, with a test that a child asking to soften any
         of them is a config error.
      3. The advisory-count read was fooled within one scanner's output,
         not across scanners: a file named like the count line made the
         board read its number off a blocking finding line. The pattern is
         now per scanner and whole-line, and the last match wins.
      New tests fail on the old code. Suite: 1,922, OK. Left out of scope:
      publishscan is in neither "can re-baseline" list though it has an
      advisory form. Review queued at `160/860`.
