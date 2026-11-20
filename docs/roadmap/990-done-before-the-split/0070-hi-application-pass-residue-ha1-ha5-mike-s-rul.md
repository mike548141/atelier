- [x] **HI application-pass residue — HA1–HA5, Mike's ruling** — five
  findings from the terminal pass
  ([`reviews/2026-07-22-0943-hi-application-cold.md`](../../reviews/2026-07-22-0943-hi-application-cold.md)),
  decided into the backlog per the close rule; rule 3 makes them Mike's.
  HA1 (M): the HI-F1 bypass conflates growth stores with non-content dirs —
  a vendored `ROADMAP-DONE.md` under `node_modules/` or `.venv/` reds
  `--check` (probed live); counsel: split `SKIP_DIR_NAMES` into store vs
  non-content sets, bypass only the former. HA2 (M): the unclosed-fence fix
  narrows its fail-open, doesn't close it (count=0 demo); counsel:
  delimiters unbalanced at EOF ⇒ recount the whole file with fences
  ignored. HA3 (L): CI surfaces cold-content-only. HA4 (L): template
  legend overclaim. HA5 (L): RECORD.md antecedent drift.
  *review: not warranted — the cycle's terminal pass reviewed the
  surrounding text; HA1/HA2 land with their own red-leg tests through the
  standing floor.*
  **RULED 2026-07-22 (Mike): "accept your recommendation on all of them" —
  HA1–HA5 [fixed]** as counselled, applied + re-proven same day (suite
  319→323 green, both probes re-driven, red leg reds exactly the four new
  tests); decision stamps in
  [`reviews/2026-07-22-0943-hi-application-cold.md`](../../reviews/2026-07-22-0943-hi-application-cold.md).
