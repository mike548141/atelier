- [x] 🔎 **The paragraph projection (`010/170`) loses two small signals,
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
      - [x] ✅ **Closed 2026-11-09.** In `tools/board.py`: (1) `index_title` no longer
            takes the dashes off a title that opens with a flag (`--list`, `--think`,
            `--no-verify`); a hyphen sheds only when it stands alone. (2) A claim inside
            a closed bold title is cut out of the title and still projects into the claim
            slot. (3) `_leading_glyph` carries a non-flag glyph (🚩 💡 🔑 🎭) ahead of the
            title, without repeating the `✅` a done item's marker already shows. The
            legacy projection (`legacy=True`) is byte-identical until the grace ends
            2026-11-18. Tests: `SmallTitleDefects` in `tools/test_board.py`. The index
            change is 12 lines: nine gain a glyph, three keep their dashes. The README note about
            where a claim goes in a wrapped title is not needed, since a claim anywhere
            in the title no longer shows in it.
  - [x] 🛑 **Held, not landed (queue run d0ca5d24, 2026-11-09 UTC): this reds six of
        the eleven children.** The fix above is built and tested, 108 tests in
        `test_board`, but the probe at landing ran `board --check` in each child's
        checkout with the fixed `board.py`: six go stale that pass today, in the
        hook and in CI, because children float at `floor.yml@main`. The grace of
        `010/170` covers only the older projection. So the code is held on the
        branch `hold-010-180-index-title`, two files only (`tools/board.py`,
        `tools/test_board.py`). **Land it together with `010/190`,** after the
        children have rebuilt, or with a grace of its own if the principal wants
        one sooner. Delete the branch when it lands.
  - [x] ✅ **Landed 2026-11-12 UTC** by session d0ca5d24, on Mike's answer
        "Land now + rebuild (Recommended)" to a question this session wrote
        (an answer, not a ruling). The probe before landing, every repo by
        exit code: without the fix all pass, today and with the clock at
        2026-11-18, so every child had already rebuilt to the current
        projection; with it, six go stale on both planes. Waiting for the
        cut-off could not help, since a child can only rebuild to the new
        projection once it has landed. So it landed, and each of the six
        regenerated its index straight after. Branch deleted.
