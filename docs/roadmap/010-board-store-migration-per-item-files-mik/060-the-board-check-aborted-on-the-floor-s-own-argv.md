- [x] 🔥 **`board` aborted on the floor's own argv — FIXED 2026-08-17.** The
      registry renders `check --root <root> {scope}`, and argparse cannot bind
      positionals that an intervening optional has split into two runs, so the
      trailing scope path fell out as "unrecognized arguments" and `board.py`
      exited 2 before doing any work. The `paths` argument was added to absorb
      exactly that and never could. Because `board` is registered **enforced
      with no advisory form**, the failure did not degrade — it blocked: the
      hook plane went red in atelier itself and in every child the floor
      invoked, on an argument the floor had rendered for itself. Live at
      `66ff846`, reproduced in both atelier and `derry-hill`, and it is the
      reason `derry-hill`'s split-board adoption could not commit at all.

      Fixed by parsing with `parse_known_args` and rejecting only unknown
      *options*, which is the contract `paths` always stated: the board's
      location is fixed at `docs/roadmap/`, so a scope argument is rightly
      ignored — but it has to be ignored, not fatal. Pinned by three tests in
      the class `FloorArgv` (the floor's exact rendered argv runs; the absorbed
      scope does not silently turn `check` into `rebuild`; an unknown option is
      still exit 2) plus three cases in `--selftest`, so the offline proof
      covers it too. Suite 1,324 green; floor green both planes in atelier and
      in `derry-hill`.

      **This falsifies a load-bearing claim in the open cold pass.** The
      board-store review (`reviews/2026-08-15-1030-board-store-migration-cold.md`)
      recorded "floor green both planes with `board` enforced" as verified
      under attack. It was green *in the session that measured it* and red for
      any invocation through the registry — so the check the migration's whole
      integrity argument rests on had never actually run via the floor. Carry
      this into the BS ruling round: it belongs beside BS1, which is the same
      shape one layer up — a hook-plane guarantee asserted in four places and
      not true in practice.
