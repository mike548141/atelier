# Brief — publishscan application cold pass (rule 4)

- **Work under review:** the `publishscan` application delta — commit
  `c85285b` (`tools/publishscan.py`, `tools/test_publishscan.py`), which
  applied Mike's rulings PB1–PB4 from the 2026-08-02 publishscan cold pass.
- **Review shape:** application review (REVIEW.md § *Applying decisions to
  doctrine*). Sequence honoured: the edited code and tests are reviewed at
  HEAD and findings committed **before** the prior verdict
  (`2026-08-02-2313-publishscan-cold.md`) is opened; the verdict is then read
  to reconcile the application against the rulings. The residual exposure —
  the delta's commit message carries the author's one-paragraph account of
  PB1–PB4 — is named, not denied.
- **Spawn provenance (rule 4):** taken from the ROADMAP `⏳` queue by a
  session Mike spawned with a generic "do any work that requires Fable,
  including reviews" — the worked example in REVIEW.md rule 4. This session
  authored neither the scanner, the verdicts, nor the application; the
  application's author (the 2026-08-02 taker session) spawned nothing here.
  Reviewer tier: Fable.
- **Disclosed exposure:** the mandated session onramp (SESSIONS.md tail)
  included the author session's addendum summarising the application
  ("any-depth matching, enforced `# reason`, `--root` rebasing") before this
  taker could choose not to read it. Named here so the verdict is auditable;
  the detail below that summary was met cold.
- **Scope:** the full commitment — the code, the tests (reviewable on the
  same footing), the live behaviour (re-run, not read), and whether the
  application is faithful to rulings it implements (checked at reconcile).
  Non-goals: the scanner's original design (reviewed 2026-08-02; its cycle's
  findings are Mike's rulings, not re-litigated here) — but a ruling whose
  application *introduces* a new defect is in scope.
- **Lenses:** all four (approach/assumptions · correctness/quality ·
  completeness/harvest · security/privacy). Review deep, not fast.

---
