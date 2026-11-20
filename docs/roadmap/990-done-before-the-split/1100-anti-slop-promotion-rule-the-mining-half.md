- [x] **Anti-slop promotion rule — the mining half** — done 2026-07-22
  (wave-2 queue run, `84fb112`): 330 findings across all 47 review files
  clustered into 5 scanner candidates (S1 wrap-hygiene — the class that
  shipped three cycles running; S2 named-path-resolves; S3 UTC dating; S4
  template stamp-drift; S5 NZ spelling, carried on ROI) + 7
  verifier/checklist candidates (V1 overclaim-vs-evidence the largest
  cluster at ~30 — validating the doctrine, not exposing a gap),
  below-threshold classes named, already-enforced classes credited, and one
  ⚠️: fail-open/detector-edge (~23) kept recurring *after* the selftest
  floor — "harden tools/ tests", not "solved". Record:
  `sessions/2026-07-22-1036-invariant-candidates.md`.
