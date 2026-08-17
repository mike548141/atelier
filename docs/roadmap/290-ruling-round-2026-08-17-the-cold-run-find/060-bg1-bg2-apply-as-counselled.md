- [ ] 🎯 **RULED 2026-08-17 (second sitting, 1045 UTC) — BG1/BG2: "Apply as
      counselled."** Mike chose the recommended option as offered: *one code
      change + a resolution-matrix test; lands with a queued cold pass. Fixes
      the flip-flop and the `python3 /board.py` failure.* The counsel (BG
      verdict, `reviews/2026-08-17-0730-board-generator-child-truth-cold.md`):
      decide the emitted spelling from the **repo** (is `tools/board.py` a
      tracked file of `root`?) rather than from the tool's location; emit the
      hook's **whole** resolution expression (env → git config → in-repo
      `tools/`); and add a test that resolves the hook's expression and the
      emitted one under the same env/config matrix and asserts they agree.
      - [ ] **FUNDED, untaken** — a code change in `tools/board.py` (+
            `test_board.py`, `--selftest`), landing with its own rule-4 code
            cold pass queued in the landing commit. Not applied by the ruling
            session (a cold reviewer session that had just orchestrated the BG
            pass; the fix belongs to a working session). BG3 (the wrapscan
            property) and BG4 (the README/CHANGELOG sweep) ride with it or
            with the next BG ruling — BG3 re-opens the generated-file
            exemption question the author withdrew, and needs Mike's own
            answer.
