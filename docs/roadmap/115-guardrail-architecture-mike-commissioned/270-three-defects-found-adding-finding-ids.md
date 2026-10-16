- [ ] 🔎 **Three defects found while adding finding IDs** `[S][tools]`.
      Found 2026-10-05 by the `080` finding-ID worker, and not fixed there:
      1. 🚩 **sizescan's cold-content gate can be silenced by a header
         marker, and its own text says it cannot.** The remedy text and the
         README say neither hatch silences the cold-content gate. In the
         code, an unscoped `sizescan:allow` header exempts the whole file,
         cold content included. This was true before `080`. Either the code
         or the text is wrong. Which one is a question about what the gate
         is for. The gate exists so done work is harvested, not hidden.
      2. The README's pointerscan section says "two guards". There are three
         detectors, because `state` was added by `130/020`.
      3. `test_sizescan.py` and `test_pointerscan.py` call `unittest.main()`
         partway down the file, so running either directly skips every
         class after that line. `unittest discover`, which the floor and CI
         use, imports the module and runs everything, so the suite is
         unaffected. A hand run of the file is not. This is the same class
         as LC3.
      **The work:** 2 and 3 are plain fixes. 1 needs the gate's purpose read
      before choosing between the code and the text.

      ✅ **Parts 2 and 3 done 2026-10-05** (queue run, a Sonnet 5.5 worker;
      `5fb2766`, `b609b4b`). The README's pointerscan section now names all
      three detectors. An AST sweep found **nine** test files, not two, with
      `unittest.main()` partway down. All nine are moved to the end, and a
      direct run of each now matches `python3 -m unittest`. Before, a
      direct run skipped up to half the file: 69 of 142 tests in
      `test_leakscan`, and 23 of 44 in `test_board`. The suites pass (1,811
      and 411). One leftover: `pointerscan.py`'s docstring heading still
      says "TWO FAILURES" over a body that lists three.
      🎯 **Part 1 is a decision, and the evidence points both ways.** The
      commit that rebuilt the gate (`5e68923`) wrote in its docstring, its
      code and its selftest that a `sizescan:allow` header exempts a file
      from *everything*, the cold-content gate included, for a repo that
      keeps a flat log. `.sizescanignore` skips paths wholesale as well. A
      later review fix (`78747fa`, SR1) wrote "none of which silences" into
      the README and the remedy text, and the remedy line contradicts
      itself. **Blast radius measured at zero** across 29 repos: no file
      anywhere carries a `sizescan:allow` header or a `.sizescanignore` hit
      over cold content. So either fix is safe today. It goes to Mike with
      a recommendation at the close.

      ⚖️ **RULED by Mike, 2026-10-05, in his own words.** The question
      offered "allow it, with a reason" (which the session recommended) or
      "never allow it". He answered in free text:

      > Never allow it as I don't want any of my repo's to run a flat running
      > log, they should all being using the new method where the main board
      > (aka roadmap) is a simple list of the work and its state, all the
      > detail that defines the work etc is in a standalone file. I'm not
      > sure what other files / content sizescan is used for.
      > Inline with my ruling that checks (including guards) must fail
      > noisily - When sizescan finds the a violation such as completed work
      > it should report the specific items or lines that sizescan believes
      > are completed and ready to move to the archive to save the AI from
      > infereing that.
      > I specifically do not want artibuary limits like a fixed kb or line
      > count as limits because that is contrary to the purpose

      **What it asks for, as three builds, each subordinate to his words
      above:**
      - **(a)** No hatch silences the cold-content gate. A `sizescan:allow`
        header, a `cold-content` scope and `.sizescanignore` all stop
        exempting it. The blast radius was measured at zero across 29 repos.
      - **(b)** The gate names the specific items or lines it judges done
        and ready to archive, so no session has to infer them.
      - **(c)** No arbitrary size limit. sizescan's *size-advisory* half
        flags files over a fixed line reference (about 300 for the board
        index, about 250 for the session log). On his words, that is
        exactly the kind of limit he does not want. It never fails a build,
        but it prints on every commit.
      🤔 **Owed to Mike before (c) is built:** he said he is not sure what
      else sizescan is used for. The next session explains its two halves
      in plain words, and what removing the size half would lose, before
      that half is removed.
      `[ ]` stays: parts (a) to (c) are owed. This is the next session's
      first pick, beside `280`.

      ✅ **Parts (a) and (b) built 2026-10-16** (`f9ccba8`, merged
      `ccfad42`. A Sonnet 5.5 worker re-dispatched fresh after the 07:35 UTC
      crash, because the first attempt died unfinished and was discarded).
      (a): no allow header, `cold-content` scope or `.sizescanignore` glob
      exempts cold content any more. They still quiet the size advisory,
      and the report names any such hatch as present but unable to exempt.
      (b): each flagged file lists its completed items as `line N: text`,
      capped run-wide in the house way. `--json` carries them too. The
      pointerscan heading leftover is fixed. **Blast radius:** of 30 repos,
      none changes exit code. One was already red before the change, on
      completed items with no hatch involved. 🔎 **Found and fixed in the
      same code:** the `.sizescanignore` count always printed 0, because
      the skip list was never appended to, so the suppression line had
      reported a false zero. Tests: 1,851 Python and 411 Node, all OK. The
      new tests fail on the old module. Review queued at `160/790`.
      🎯 **(c) is still owed, and waits on Mike:** what the size-advisory
      half is for has to be explained to him before it is removed.

      ✅ **(c) answered 2026-10-16, at the close of the queue run:
      remove the size advisory.** The question was asked in the device after
      the explanation owed above. It said what each of sizescan's three
      checks is for, and that removing the length nudge loses the only
      pointer to finished work written as prose, which is then caught only at
      review. Mike picked "Remove it", the recommended option, over two
      alternatives: replacing it with a shape check, or keeping it off
      generated boards only. This is his *answer* to that question. The
      ruling it implements is his 2026-10-05 text above. **The build is
      owed:** remove the size-advisory half (the line references,
      `sizescan:budget=N`, and the advisory output) along with its tests,
      docs and the module docstring's account of it. Keep the cold-content
      and harvest-integrity gates. No exit code changes, because the
      advisory never failed a build. Every child's output changes at its
      next run. Measure that before landing.
