- [ ] 🔎 **Dispatch prompts drop two doctrine obligations: the worker's own
      scratch directory, and the terminal marker.** Found reviewing the first
      real `/atelier:queue-run` (session `8e498ef1`, 2026-10-18, `180/110`).
      Of its five dispatches, four named no scratch directory
      (`CONCURRENCY.md` § *Orchestrated queue runs*: "a dispatch prompt names
      an explicit, unique, absolute scratch directory"). Four asked for no
      terminal marker (*teardown*, landed hours before the run). One worker
      had both. The failure the scratch rule exists for happened: a
      brief-writer wrote 50 working files into the orchestrator's own
      scratchpad, and the run closed with them still there. Both rules live
      only in doctrine prose, and nothing an orchestrator copies when it
      writes a brief carries them. **Shapes:** a dispatch-brief skeleton in
      `docs/method/` that `CONCURRENCY.md` points at, holding the fixed
      obligations (worktree, scratch path, foreground verification, explicit
      staging, no push or merge, terminal marker); or a pre-dispatch
      self-check line in the run's loop.
