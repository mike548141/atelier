- [x] **ccarchive: is there any metadata it misses?** — answered 2026-07-22
  (wave-3 queue run, `5ce9f00`): yes. The real hole is `tool-results/`
  sidecars — offloaded tool-output payloads the transcript only points at,
  so the archive can hold dangling references while advertising a complete
  record (≈7% of transcript volume; recommendation: CAPTURE, plus man-page
  honesty about what is excluded regardless). Full classification
  (capture / exclude-and-document / needs-Mike) in
  `sessions/2026-07-22-1050-cc-instruments-questions.md`. Rulings stay a
  live 🎯 on the ROADMAP.
