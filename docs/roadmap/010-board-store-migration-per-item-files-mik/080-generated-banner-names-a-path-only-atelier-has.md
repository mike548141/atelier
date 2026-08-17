- [x] 🔎 **The generated index tells every child to run a file it does not
      have — reported upstream by `faves`, unrecorded here until 2026-08-17;
      FIXED the same day (wt: board-generator-child-truth).**
      `board.py` hard-coded `tools/board.py` into three child-facing strings:
      the `GENERATED` banner (`tools/board.py:70-73`), the index preamble
      (`:174`) and the stale-index remedy the check prints (`:232`). In
      atelier every one of them is true. In a child the tool lives in
      atelier's checkout, so the single instruction printed at the top of the
      one file a reader is forbidden to hand-edit names a path that does not
      exist — and the remedy line does the same at the moment the check
      fails, which is exactly when a reader is least able to guess. `faves`
      made the banner true the only way it could: a `tools/board.py` **shim**
      that resolves atelier's tool by the hook's own order
      (`ATELIER_TOOLS` → `git config hooks.atelierTools` → `../atelier/tools`)
      and runs it, holding no board logic — a shim, explicitly not the copy
      ADR 0008 forbids. That file exists only to stop the banner lying, and
      its own docstring says so: teach the generator to emit the *resolved*
      path and the shim goes. Fixing this before the `ros`/`shed` rollout
      (item `030`) means two fewer child files that exist to paper over a
      string. Class, worth naming: **a generator writes text that is read
      from somewhere it was never written for** — the same shape as the
      two-depth link defect the migration itself hit on day one, and the same
      root `070` records for the scanner-facing half.
      **Done 2026-08-17.** `rebuild_cmd()` decides per root: the repo-relative
      path where the tool is inside the tree it rebuilds (atelier, unchanged),
      the hook's own `python3 "$ATELIER_TOOLS"/board.py rebuild` spelling where
      it is not, and **never an absolute path** — that would put a
      machine-local fact into a file that may be public, trading one wrong
      string for a worse one. The banner now names no path at all
      (115 → 69 columns) and the HOW moved to the preamble, which is built
      against a known root and can therefore be true from where the reader
      stands; the stale-index remedy the check prints resolves the same way,
      at the one moment a reader is least able to guess. The marker is matched
      as a prefix against **both** spellings, so no repo needs a flag day.
      Proved offline, not asserted: the selftest's root is a tempdir, which is
      exactly a child's geometry, so the child spelling is what its own
      assertions read — plus a check that no home directory reaches the index.
      **`faves`' shim can go**, and `ros`/`shed` never need to write one.
      The same commit closed `070`'s scanner-facing half — see it for the
      renderer changes (link text, flag order, wrapped preamble) that take the
      generated index to clean on both scanners in a repo with no scope block.
