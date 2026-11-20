- [x] 🚩 **Budget hatches must be grounded — corrected 2026-07-18 (Mike caught
      it).** a declared `sizescan` budget of 320 had been declared on a 319-line file: derived
      from the file's own length, so circular — and the *"raise the budget"* move
      the 2026-07-14 review already ruled *"defers, doesn't resolve"*. The
      hatch's docs never said so; now fixed at the point of use in
      `tools/sizescan.py`.
