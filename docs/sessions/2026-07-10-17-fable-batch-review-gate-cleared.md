# 2026-07-10 · the post-method-review batch review: PASS-WITH-FINDINGS, gate cleared (Fable)

The sweep session 16 briefed, run by a fresh Fable session per the
independence-as-core doctrine (the builder was Opus; the reviewer shares none of
its context). Deep-not-fast as authorised: every in-scope doc read whole, all
three scan sources read line-by-line, the mechanical floor run first, the ros
cross-read done against the live tree.

## What ran

- **Floor first** (brief assumption 13): `leakscan`/`secretscan`/`licenscan`
  `--selftest` all OK; full suite 133 tests OK; live whole-repo runs — leak and
  secret scans clean, **licenscan exit 1** on its own unexempted test fixtures.
- **All 16 assumptions attacked**; seven surfaced findings (4, 6, 9, 11, 13,
  15, 16). Verdict below the divider in
  `docs/reviews/2026-07-10-post-method-review-batch.md`.
- **ros cross-read**: SECRETS' instance content confirmed held (secrets/README
  mint chain, PRINCIPLES §5/§7 bearings); ACCESS' claimed estate access map
  confirmed **not** held (B14); nothing sensitive leaked up.

## The findings that matter most

16 findings B1–B16 — every one carrying an in-repo fix, applied and verified
same session — plus 2 [backlog] strands on the ROADMAP follow-ups item (B14's
instance half, and a REVIEW.md lifecycle line). The two sharpest were honesty defects of exactly
the class this batch itself codified (EVIDENCE §14 / PRINCIPLES §6's
stale-proof case):

- **B1** — session 15's "live-proven clean on atelier" licenscan claim was
  false at the commit that recorded it: the very commit that added the claim
  added the unexempted fixtures that flag. Fixed (`.licenscanignore`, the same
  reasoned exemption both sibling scans already had), ROADMAP + CHANGELOG
  corrected in place, re-proven exit 0. Session-15's entry stays verbatim
  (append-only); the verdict is the correction record.
- **B14** — ACCESS.md and method/README pointed at a consolidated estate access
  map "in ros" that doesn't exist (only scattered posture notes). Wording
  corrected to honest status; ros owes its first consolidated map (backlog —
  sensitive content, a ros session's job).

Tool fixes, each with a proof: **B2** `-only`/`+` SPDX suffix normalisation
(a `GPL-2.0-only` header mis-tiered from high/block to medium/warn; regression
tests added); **B4** both scanners' `--staged` moved `ACM`→`ACMR` — a
renamed-and-edited file's added lines were invisible to the pre-commit hot
path; proven live both directions (old filter: zero diff output on an R095
rename carrying a fixture secret; new filter: secretscan and leakscan both
block); **B5** leakscan `--require-terms` fails closed for automation (a
degraded structural-only pass was exit-0-indistinguishable from full cover);
**B7** tools/README gains "What these scans cannot see" — the triad's stated
residual (multi-line splits, binaries, paraphrase, prose licence headers,
single-case hex). Suite 133→137.

Doctrine fixes: REPO-STANDARD subfolder rule scoped to deployable-artifact
repos (its own sizing table was the counter-evidence, B8) + infra no-gate must
be stated (B9); RECORD gains the comments-say-*why* rule that REPO-STANDARD
pointed at but RECORD never contained (B10); stale templates/licenscan lines
swept (B11); SECRETS gains the honest boundary — master-key **loss** is
redundancy-guarded not re-mintable, person-level vault out of scope by design
(B12, grounded in the ros age-key ⚠ note); ACCESS owns step 5's
gate-before-*power* strengthening and states the one-broad-credential fallback
(B13); EVIDENCE §13 gains the §11/§13 stakes-win tiebreak (B15); REPO-BOUNDARY
gains split-*promptly* (B16).

## Lifecycle judged (second run of brief-on-top/verdict-below)

Worked — a cold session ran the whole brief with zero clarifying questions, and
the pre-named assumptions aimed straight at real defects. One improvement
carried as backlog (not edited now — REVIEW.md is outside this batch's scope,
and stacking unreviewed doctrine edits is what the gate exists to stop): **a
review re-runs every "live-proven" claim inside its scope.**

## Close

All selftests OK, 137 tests OK, all three scans clean on atelier
(`licenscan --expect Apache-2.0` exit 0). ROADMAP gate ticked, Review-owed tags
swept, follow-ups item raised. **The gate is cleared: the create-repo rewire
and further extraction may stack on this batch.**
