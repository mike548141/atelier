- [~] 🔎 **Three defects found while adding finding IDs** (claimed 2026-10-05-1946, wt: atelier-qr-115-270) `[S][tools]`.
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
