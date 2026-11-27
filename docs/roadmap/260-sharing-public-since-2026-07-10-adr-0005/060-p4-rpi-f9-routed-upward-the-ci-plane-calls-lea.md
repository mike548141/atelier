- [x] **P4 — `rpi` F9, routed upward: the ci plane calls `leakscan` without
      🔒 Claimed by session 9c5fa72c (`atelier-fa`, Opus 5.5), principal-opened by
      `/atelier:work run`.
      (claimed 2026-11-27-0915, wt: atelier-qr-9c5f-smallfixes)
      `--require-terms`.** Every child's CI run therefore self-reports "cover not
      guaranteed". The fix belongs in atelier's registry, not any child — it
      pairs with Track D's registry work; the design question is whether CI can
      carry a term list at all (the list lives in `~/.claude/`, outside every
      repo, which is why the ci plane was left structural-only in the first
      place). If it cannot, the honest fix is a rendering change so "structural
      only" stops reading like a defect.
      ✅ **Done 2026-11-27 (queue run 9c5fa72c, a Sonnet worker).** Settled the
      design question by the item's own fallback: CI cannot carry the term
      list (it is machine-local by design, `SECRETS.md`), so the fix is the
      rendering, and `--require-terms` is not added to CI. Measured first,
      running the registry's ci line from the tree: the floor printed `🟡
      leakscan enforced (cover not guaranteed — the ci plane does not pass
      --require-terms)`, and `leakscan` on a host with no list printed `⚠ no
      local term list found ... Set $ATELIER_LEAKSCAN_TERMS ... for full
      cover`; the registry and the `ci` plane text in `tools/floor.py` already
      declared the design, the output did not. Changed: on the ci plane the
      note now reads `structural-only by design on the ci plane — it never
      passes --require-terms (the term list is machine-local, so a runner
      holds none); full cover is the hook plane's`; the same omission on any
      other plane keeps `cover not guaranteed`, since there it is a gap.
      `leakscan`'s own warning adds that the absence is expected on a CI
      runner. The 🟡 and every exit code are unchanged (the 🟡 is the EP3
      ruling: identical output for materially different cover is the claim).
      Tests: `tools/test_floor.py` (the pinned wording, a ci-plane test, a
      test that another plane still says gap) and `tools/test_leakscan.py`.
      *Seen, not changed:* `leakscan` still prints its `⚠` on a runner; making
      it quiet there would mean detecting CI, which is a behaviour change, not
      a wording one.
      review: not warranted — a wording change to an already-reviewed floor
      line and a warning string; nothing blocks or exempts differently, the
      exit codes are pinned by the same tests, and a wrong string is loud in
      every child's run.
