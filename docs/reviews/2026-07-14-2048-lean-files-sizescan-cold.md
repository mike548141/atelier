# Cold review — lean current-truth files: `sizescan` + RECORD.md roadmap doctrine

**Scope:** commit `47c5ea6` (2026-07-14) — `tools/sizescan.py` + `test_sizescan.py`,
`method/RECORD.md` § "The roadmap" (the current-truth/history split, the growth
dynamic, the harvest-at-close trigger), `tools/README.md` § sizescan, and the
dogfood harvest (`docs/ROADMAP.md` 1091 → 180, `docs/ROADMAP-DONE.md` created).
Review gates wiring `sizescan` into any gate (`ci.yml` / child `floor.yml`
`--check`).

**Reviewer:** Fable, fresh session 2026-07-14; not the author (work authored by
an Opus session, 2026-07-14-1948). Un-briefed pass — no author brief exists.

**Independence note, stated honestly:** the author's four seeded questions live
*inside the ROADMAP queue item itself* (budget defensibility, root-only masking,
line-count-as-proxy, advisory toothlessness), so the reviewer read them at
selection time — they could not be structurally deferred. Mitigation is this
section: the attack surface below was drawn up and committed from the reviewer's
own reading of the code, tests, and doctrine *before* the seeded four are
reconciled; the reconcile happens in the verdict, after. Rule 3 applies
regardless: the doctrine under review is agent-authored, so findings on it are
the principal's to decide, not any agent's.

## Attack surface (reviewer's own, committed before verdict)

Lens 1 — approach & assumptions:

- **A1. Basename-keyed budgeting** assumes the fleet's conventions are the
  world's — a roadmap named `TODO.md`/`BACKLOG.md` is invisible. Acceptable for
  a house tool; is the narrowing stated?
- **A2. The tool has no firing point yet** — the exact no-trigger decay it was
  built to fix. Not in the read order, not in the hook, not in CI. Does the
  doctrine's real trigger (harvest at session close) carry the weight until
  wiring, and is advisory-in-CI a signal anyone will ever see?
- **A3. The append-only SESSIONS index is budgeted as current-truth.** RECORD.md
  says the index is *never rewritten*; sizescan says it must stay ≤250 lines.
  What is the prescribed fix when an already-split index outgrows its budget?
  (atelier's is 75 lines after ~5 days of sessions — this is near-term, not
  hypothetical.)
- **A4. Excluding the growth stores** is right (don't punish the destination),
  but confirm the residual is honestly stated somewhere a reader will meet it.

Lens 2 — correctness (code + record):

- **C1. Absolute-path skip check.** `iter_candidates` tests
  `SKIP_DIR_NAMES & set(p.parts)` on the *absolute* path. A repo checked out
  under any ancestor directory named `sessions`, `reviews`, `decisions`,
  `archive`, `_archive`, or `intake` (e.g. `~/archive/<repo>`) silently skips
  every file — a scan that read nothing reporting clean, the exact fail-open the
  tool's own docstring forbids. Reproduce it. Check whether the sibling
  scanners share the pattern.
- **C2. Whole-file marker matching.** `sizescan:allow` / `sizescan:budget=N`
  match anywhere in the text. A budgeted file that merely *mentions* the marker
  in prose (a roadmap item about sizescan budgets, a CLAUDE.md documenting the
  hatch) silently exempts or re-budgets itself. Per-file blast radius — blunter
  than the sibling scanners' per-line allows. Reproduce it; grep the budgeted
  files at HEAD for near-misses.
- **C3. Re-run every recorded proof:** 24 sizescan tests, the full suite
  ("240 tests OK"), `--selftest`, sizescan + linkscan clean on the harvested
  result, the fleet claim (sharp on ros 3197 / faves 1157, silent on healthy
  repos), and the harvest's **zero-checkbox-lost / verbatim-move** claim —
  verify mechanically against `47c5ea6^`, not by reading the assertion.
- **C4. Smaller checks:** `.sizescanignore` fnmatch `*` crosses `/` (gitignore
  it is not); rglob enumerates `.git`/`node_modules` before filtering (no
  prune); duplicate findings if overlapping paths are passed; explicit
  non-budgeted path scans nothing and prints clean.

Lens 3 — completeness / harvest:

- **H1. The harvest itself:** every checkbox item in the pre-harvest ROADMAP
  accounted for across the post-harvest pair; moved text verbatim; links in
  both files resolve; ROADMAP-DONE's framing doesn't contradict RECORD.md.
- **H2. What the work should have covered:** does the store hint for SESSIONS
  point at a fix that exists for an already-split index (ties to A3)? Does
  CHANGELOG's entry match what shipped? Is the not-wired state consistently
  stated everywhere it matters (code docstring, tools/README, ROADMAP)?

---

*Verdict below, appended after the attack surface was committed and the live
proofs re-run.*
