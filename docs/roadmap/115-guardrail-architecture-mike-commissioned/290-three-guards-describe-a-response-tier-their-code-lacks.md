- [x] 🔎 **Three guard descriptions disagree with their own code**
      `[S][tools]`. Found 2026-10-16 by the `090` audit and checked against
      the code before filing. Not fixed in passing:
      1. **licenscan promises a warn tier that does not exist.** Its
         docstring (`licenscan.py:35-38`) and its README section say a
         permissive-into-permissive mix, or an unknown declaration, is a
         *warn*: "friction, never a silent pass". In the code,
         `compatibility()` returns `warn`, which becomes a `medium` finding,
         and every finding counts toward exit 1
         (`report.exit_code(len(rep.findings))`, `licenscan.py:726`). So a
         "warn" blocks. Either the text or the code is wrong. Which one is
         a question about the guard's posture.
      2. **pathscan's docstring says it is not in the registry**
         (`pathscan.py:15-20`). It has been registered since 2026-08-05
         (`floor.py`, `tools/README.md`, `ci.yml`). This is a plain fix.
      3. **floor.py says boundary checks have no advisory form "by
         design".** publishscan is a boundary check, and it carries one, as
         an adoption aid rather than a severity tier (the comment beside it
         says so). The general sentence needs that exception.
      **The work:** 2 and 3 are plain fixes. 1 needs the posture read
      before choosing between the code and the text. It is the cheapest
      second dial on the board (`090`).

      ✅ **Part 1 answered 2026-10-16, at the close of the queue run: make
      the warning real.** The device question offered two options: make
      mild findings report without blocking, or reword the text to say
      everything blocks. Mike picked "Make the warning real", the
      recommended option. That is his *answer*, recorded as such. **The
      build is owed:** licenscan's `warn` verdicts (`medium` severity:
      permissive-into-permissive mixes and unknown declarations) report
      without blocking. `high` findings (no licence, incompatible) still
      block. Follow secretscan's advisory pattern: a distinct report block,
      exit 0 for advisory-only, and the advisory count on the board. Check
      the blast radius across the children, where the change can only turn
      a red green. Parts 2 and 3 (the docstrings) are still plain fixes,
      unclaimed. The whole item is now buildable.

      ✅ **Done 2026-10-16, all three parts** (1501 UTC queue run, a Sonnet
      5.5 worker; `e3e8a4f`, merged on `main`; the orchestrator read the
      diff and corrected two dates at the merge).
      1. licenscan's warn is real. Each finding carries a response worked
         out from its severity: `high` blocks as before, `medium` reports in
         its own advisory block at exit 0. The tier is opt-in, so a severity
         not named advisory blocks. `licenscan advisory: N finding(s)` prints
         on every run, zero included, and the floor board reads it as it
         reads secretscan's. `--json` gains `blocked`, `counts` and a
         per-finding `response`. A child still cannot soften licenscan.
      2. pathscan's docstring says it has been a registry entry since
         2026-08-05.
      3. floor.py's "no advisory form by design" names publishscan's
         adoption-aid exception.
      New tests fail on the old code (8 of 9, 3 of 3, and the pinned
      literal). **Blast radius, 29 repos, scanner view:** 6 go from exit 1
      to exit 0 on one advisory each, 2 stay at exit 1 on one `high`
      finding each, 21 are clean on both, none goes green to red. Suite:
      1,903 tests, one failure, the known `test_pins.BoundedMemory` load
      timeout (load 55–157). 🔎 Found, not fixed, filed as `115/320`: a
      stale "only the prose-hygiene checks may re-baseline" comment in
      `test_floor.py`, an unsoftenable-scanner selftest that pins only four
      of the seven, and an advisory-count regex that matches any scanner's
      wording. Review queued at `160/840`.
