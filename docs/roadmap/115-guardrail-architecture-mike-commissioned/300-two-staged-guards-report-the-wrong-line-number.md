- [~] (claimed 2026-10-16-1501 UTC by queue run abe96d8d, a worker) 🔎 **conflictscan and leakscan report the wrong line number on the
      staged plane** `[S][tools]`. Found 2026-10-16 by the orchestrator's
      own probe while checking `280` before its merge. This is not caused by
      `280`: the old code does it too. Measured: a file whose lines 1–4 are
      committed gets a conflict opener, or an email, staged on line 5. Both
      guards report `c.md:1`. They number a finding by its position among
      the file's *added* lines, not by its line in the file. `secretscan`
      reports the real line, because it tracks each hunk's start. The
      shared reader (`report.staged_added`, from `280`) already yields the
      real line number with each added line. So the fix is to use it, plus
      a test that a finding added below unchanged lines reports its file
      line. A finding still blocks today, but it points the person fixing
      it at the wrong line.
