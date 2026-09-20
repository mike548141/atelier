- ⏳ **Rule-4 cold pass queued — the 2026-09-20 scanner code: `secretscan`
      rewritten to stream, and `pathscan` reading declared resolution
      roots.** Self-authored by the run (its dispatched workers count as the
      run's authorship), queued at landing; the run neither takes nor spawns
      it. *Tier:* Fable, the principal-named review tier — checked at
      selection; a session that cannot honour the bar stops rather than
      takes. *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta — scoped to paths:* `tools/secretscan.py` (`_walk_files`,
      `_iter_numbered_lines`, `_scan_file`, `MAX_MATERIALIZED_FINDINGS` and
      the `Tally` counters, the render/JSON totals) · `tools/memprobe.py`
      (new) · `tools/pathscan.py` (`load_declared_roots`, `_resolves`'
      declared-root anchor, the failure message, the docstring's anchor
      count) · `tools/test_secretscan.py`, `tools/test_memprobe.py`,
      `tools/test_pathscan.py` · `tools/README.md` ·
      `docs/build/REPO-STANDARD.md` (the config pointer). Landed on `main`,
      2026-09-20.
      **The lenses that matter most here:** whether the 64 KiB window overlap
      can drop a match no realistic pattern exceeds (the one genuinely
      open-ended named shape is a JWT), whether the 50,000-finding cap can
      ever change a verdict rather than only a listing, and whether
      per-line `scan_lines` calls preserve every cross-line behaviour the
      whole-file call had.
      *Intent record:*
      [`../../sessions/2026-09-19-0038-queue-run-the-morning-rulings.md`](../../sessions/2026-09-19-0038-queue-run-the-morning-rulings.md).
