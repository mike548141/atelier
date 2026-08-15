- [ ] 🎯 **D3 — `signscan` cannot fail CI.** It is invoked with `--warn` on
      both planes, so an unsigned commit produces an annotation and never a
      red. That is the deliberate warn-first rollout state and it has outlived
      its purpose; the flip is Mike's, and it pairs with his key rotations.
