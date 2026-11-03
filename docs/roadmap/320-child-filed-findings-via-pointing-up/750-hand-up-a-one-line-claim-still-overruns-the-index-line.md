- [ ] 🔎 **Hand-up: a one-line claim still overruns the index line, so
      320/730's "keep claims short" option does not work** `[tool]`.
      Handed up from a private child on 2026-10-26 under `PROPAGATION.md`
      § *Pointing up*, measured at a pin bump to `0a2b7a7` (Opus 5.5, no
      reviewer). Evidence for 320/730; stated class-only. Consideration and
      remediation are atelier's; the child stops here.
      **Measured.** The child claimed one item with the shortest claim it
      writes, `(claimed 2026-10-26-1010, wt: doctrine-0a2b7a7)`, on a single
      line, and rebuilt its index with this repo's `tools/board.py` at
      `5139d68`. The projected index line came out at 168 columns against
      the 85-column limit, and the child's enforced `wrapscan` refused the
      commit. The item's link path alone takes most of the width, so no
      claim is short enough. The child rebuilt with `board.py` at
      `6a0ac93` instead, under the grace that ends 2026-11-18.
      **What it changes.** Of the three options 320/730 lists, "keep
      claims short enough for one index line" fails for any child whose
      item paths are long. That leaves exempting the generated index from
      `wrapscan`, or a projection that caps or wraps the claim fragment.
      review: not warranted — a hand-up of one measured finding; the fix is
      atelier's to decide.
