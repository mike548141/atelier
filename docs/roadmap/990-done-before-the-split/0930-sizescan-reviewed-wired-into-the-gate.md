- [x] **`sizescan` reviewed + wired into the gate** — DONE 2026-07-14. Cold pass
      cleared (PASS-WITH-FINDINGS); F1 (fail-open ancestor-dir MAJOR) fixed +
      live-reproven, F2 (prose-mention self-exempt) fixed (markers header-only),
      F4 dedup fixed; **F3 decided by Mike — index rotation** (`SESSIONS.md`
      tail + `SESSIONS-ARCHIVE.md` growth store; RECORD.md sharpened). Now runs
      `--check` in atelier's `ci.yml` and the child `floor.yml` template (a repo
      that adopts the floor while over-budget reds → the signal to harvest;
      `sizescan:budget=N`/`allow` hatches). Suite 240→247; pinned in
      `test_sizescan.py` + `test_templates.py`.
