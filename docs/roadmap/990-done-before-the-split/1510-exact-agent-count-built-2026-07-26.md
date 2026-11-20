- [x] **Exact agent count — BUILT 2026-07-26** (`3b38f3d`, merged `99d43d1`).
  The header carries both figures (`10 agents started · 15 finished`), `--json`
  splits them, and **unknown is distinguishable from zero**. Started reads the
  spawn calls (a ceiling — a skipped or stopped spawn still counts); finished
  reads the sibling `subagents/` directory, one log per agent that actually ran.
  **The reason this had been deferred turned out to be false, and that is the
  part worth keeping.** The item said a directory-sourced count would read zero
  under `--from-archive`, since archive mode resolves a single file. It doesn't:
  ccarchive's `captureClass` allows any `.jsonl` at *any depth*, so `subagents/`
  is mirrored — **92 such directories in the live archive**, and the same session
  renders an identical header live and archived. The deferral was reasoned from
  how the *path resolution* works rather than from what the *archive actually
  contains*, and one `ls` would have settled it. Verified by the orchestrator
  independently before merge, not taken on report.
  - **Two standing rules reconciled**, and the resolution generalises: split the
    field **set** from the field **value**. Both chips print on every run, so a
    side-by-side comparison never has a missing column; where the store never
    said, the second reads `finished unknown` rather than dropping out or
    asserting a zero the evidence doesn't support.
  - **Finished can legitimately exceed started**, and the figures are left
    **unclamped** so the reason stays visible: a nested agent logs into the
    *principal's* directory while the principal's own call count can't see it.
    Confirmed on a real session — `spawnDepth {1: 10, 2: 5}` against a header of
    `10 started · 15 finished`. Clamping would have hidden the nesting.
  - What archive mode *does* lose is each log's `.meta.json` sidecar (not a
    `.jsonl`, so outside the capture allowlist), which carries `agentType`,
    `description` and `spawnDepth`. So the count keys on the logs alone, never on
    the directory's entry count, and a finished-*by-type* breakdown is possible
    live but not archived — deliberately left out.
