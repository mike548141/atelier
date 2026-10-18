- [ ] 🔎 **The paragraph projection (`010/170`) loses two small signals,
      and a claim placed inside a wrapped title now shows in the title.**
      Found by the `010/170` worker reading all 297 changed index lines,
      and by the orchestrator at landing. (1) 11 wrapped titles lose a
      leading glyph that is not a board flag (🚩×5, 💡×2, 🔑×2, 🎭, ✅).
      One-line items already render that way, so it is consistent, but
      the signal is gone. (2) `210/180`'s title loses its leading dashes
      (`--list` becomes `list`). An existing strip in `index_title` is now
      reached. (3) A claim fragment inserted on line two *inside* a bold
      title that wraps, as one queue run's claim helper does, now projects
      into the title text as well as the claim slot (`020/150`'s line on
      2026-10-18). **Shapes to weigh:** carry a leading non-flag glyph as
      part of the title; have the strip spare `--`; mask a claim fragment
      out of the title span; and say in the board README where a claim
      goes when the title wraps.
