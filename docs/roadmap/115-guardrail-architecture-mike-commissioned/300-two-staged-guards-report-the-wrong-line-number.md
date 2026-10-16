- [x] 🔎 **conflictscan and leakscan report the wrong line number on the
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

      ✅ **Done 2026-10-16** (1501 UTC queue run, a Sonnet 5.5 worker;
      `f4afb7a`, merged on `main`). On the staged plane both guards now
      number a finding by its real line in the file the commit produces,
      from `report.staged_added`, as secretscan already did. A conflict
      opener staged at line 5 under four unchanged lines reports `:5`; a
      second hunk reports `:26`, not `:2`. New tests fail on the old code:
      four of six, with the two new-file controls passing on both. Output
      is otherwise unchanged, and whole-tree output is byte-identical,
      checked on a fixture that fires as well as on this clean tree. No
      other guard consumes the reader. Suite: 1,897 tests, one failure,
      `test_pins.BoundedMemory`, a timeout at a machine load of about 300
      in a module this change does not touch (the known load class). It is
      re-checked at the close. 🔎 Found and not fixed: conflictscan's
      open-conflict state runs across hunks, filed as `115/310`.
      Review queued at `160/830`.
