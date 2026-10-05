- [ ] 🎯 🔎 **Three defects found while adding finding IDs** `[S][tools]`.
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
