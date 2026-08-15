- [ ] 🎯 **The E7 leakscan cycle CLOSED 2026-08-09 (0 MAJOR); LK1–LK6 + a
  G2 reach note await Mike's ruling round.** The rule-4 Fable cold pass
  (taker: a Mike-spawned session, claimed 0815 UTC) returned
  PASS-WITH-FINDINGS — 0 MAJOR / 1 MODERATE / 2 minor / 3 note; every
  re-run reproduced (53 → 114 → 119, 122 at HEAD; full tools suite 1210
  green; both planes live-probed with a scratch term list; the hard
  constraint held — counts and classes only, no machine-local term
  anywhere) →
  [`reviews/2026-08-09-0826-e7-leakscan-build-cold.md`](../../reviews/2026-08-09-0826-e7-leakscan-build-cold.md).
  Notable: LK1 (MODERATE, reviewer argues MAJOR) — a scoped allow-marker
  with a malformed scope segment backtracks and re-parses as the unscoped
  all-structural form, silently exempting co-located structural leaks the
  author never named; latent (no in-tree marker triggers it), bounded (the
  term layer held in every probe), and unpriced by the 2026-08-04 ruling —
  it breaks the ruling's *narrow* intent while honouring its letter. LK6
  (post-reconcile) — the docstring's "a path has no inline marker hatch" is
  falsified by probe. *Delta:* `tools/leakscan.py` +
  `tools/test_leakscan.py` + `tools/leakscan-terms.example.txt` + the
  CHANGELOG entry (landed 2026-08-06) + the 2026-08-09 scoped-marker
  follow-up. *Intent record:*
  [sweep record](../../sessions/2026-08-03-2050-leakscan-pii-sweep.md) + the
  2026-08-04 E7 ruling in [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md)
  § *E7 built*.
