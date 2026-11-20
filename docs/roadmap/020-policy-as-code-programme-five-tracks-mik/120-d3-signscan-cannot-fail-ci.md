- [x] 🎯 **D3 — `signscan` cannot fail CI.** It is invoked with `--warn` on
      both planes, so an unsigned commit produces an annotation and never a
      red. That is the deliberate warn-first rollout state and it has outlived
      its purpose; the flip is Mike's, and it pairs with his key rotations.
      - 🔀 Tidied 2026-11-16 (C0333, verified high; Mike approved 2026-11-16):
        merged. This is the same decision as
        [`170/010`](../170-build-layer-open-strands/010-code-signing-standard-across-the-fleet.md)
        lines 4-7, the flip of signscan from warn to block, which is Mike's and
        waits on the same key rotations. `170/010` carries the gate history, so
        it is the home: track the flip there. Nothing above was changed; the
        original text is as it was. To revert: delete this line (its commit is
        listed in `docs/sessions/2026-11-16-0534-asks-tidy-applied.md`).
      ✅ **Closed 2026-11-20 UTC by queue run 08cd3b95 as merged:** per the
      tidy line above (approved 2026-11-16), the decision lives in `170/010`,
      which stays open with the flip. Nothing here is lost; nothing is decided.
