- [x] **`floorfleet --remote` now checks the tracked shim.** Hooks used to be
  untracked, so the remote plane could say nothing about them. `.githooks/pre-commit`
  is a repo file now, so a new `shim:` column reports whether it exists and routes
  through the registry (`current`) rather than naming scanners itself (`legacy`) —
  and because it is a fact about the **repo**, `--remote` carries it as a genuine
  estate-wide claim. Proven live: **all 13 children `shim:current` on the remote
  plane**, which nothing could previously assert.
  - **The two facts are deliberately kept apart, in separate columns and separate
    footers.** `shim:` travels with a clone; `hook:` (whether `core.hooksPath`
    actually points at it) never does. Blurring them would let a reader over-claim
    on the remote plane, which is the exact failure the column exists to avoid. A
    test pins that both footers appear and stay distinct.
  - **The residual shrank rather than closed**, and the module docstring was
    rewritten to say so: it read "`--remote` cannot help: hooks are not in the
    repo", which stopped being true when the shim became tracked. It is now
    "whether *this clone* points at the shim is unknowable remotely" — real, but
    much smaller. CI stays the backstop for exactly that last step.
  - 21 floorfleet tests (was 16); `--json` carries `shim` via `asdict` unchanged.
    Original item text: **`floorfleet --remote` could check the tracked hook, and currently doesn't.** Hooks used to be untracked, so the remote plane could say nothing about them — but `.githooks/pre-commit` is now *in the repo*. The remote plane could verify the tracked shim exists and is the current one, leaving only `core.hooksPath` (genuinely per-clone) unknowable. A small change that moves a chunk of the hook question from "machine-local only" to "answerable estate-wide".
