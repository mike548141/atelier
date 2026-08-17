- [ ] 🎯 **RULED 2026-08-17 (second sitting, 1045 UTC) — BS1: "Wording now +
      fund the staged-plane build."** Mike chose the recommended option as
      offered: *fix the four "cannot drift" sentences to say "on CI; at the
      hook only when worktree and index agree" now; `010/020` (the
      staged-plane check) becomes funded work with the rebuild-from-index
      source flag folded in; the BS cycle CLOSES on the wording; the build
      earns its own review.* Briefed in plain language with the two live
      slips (rebuilt-but-unstaged index; sibling's dirty item line absorbed by
      rebuild) and per-option impacts before the ruling was taken.
      - [x] Wording applied 2026-08-17 on all four surfaces: `tools/board.py`
            docstring, `tools/README.md` headline sentence,
            `docs/method/CONCURRENCY.md` § *On a split board* (with the
            dirty-sibling-is-a-stop sentence, BS1 counsel (c)), and the
            board-store ADR by **appended amendment**, never an edit.
            Self-authored doctrine — its rule-4 `⏳` is queued at
            `160-…/260`.
      - [ ] **`010/020` is FUNDED**: bring `board check` to the staged plane
            (harvestscan's HV4 shape) **and** give `rebuild` a source flag so a
            claimer at a dirty primary regenerates from the index, not the
            worktree; name that flag in CONCURRENCY CF3 when it lands. Code
            cold pass queued at landing by whoever builds it.
      - [ ] **BS cycle state:** CLOSED on the wording per this ruling; BS2–BS14
            still await the round (residue, no MAJOR among them).
