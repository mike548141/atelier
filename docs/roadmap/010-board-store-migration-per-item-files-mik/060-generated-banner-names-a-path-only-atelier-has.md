- [~] 🔎 **The generated index tells every child to run a file it does not
      have — reported upstream by `faves`, unrecorded here until 2026-08-17.**
      (claimed 2026-08-17-0549, wt: board-generator-child-truth)
      `board.py` hard-codes `tools/board.py` into three child-facing strings:
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
      two-depth link defect the migration itself hit on day one.
