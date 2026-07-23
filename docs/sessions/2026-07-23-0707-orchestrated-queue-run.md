# 2026-07-23 · 0707 UTC · Orchestrated queue run — 1 fix + 2 first-of-kind reviews

**Orchestrator:** Opus (Mike-started, model confirmed before dispatch per the
stop-if-wrong-model instruction). **Workers:** 1 Sonnet (isolated worktree,
committed on its branch) + 2 Opus cold reviewers (read-only, no worktree).

## Brief

Mike's standing queue-run brief: maximise plan use, drain unclaimed queue,
worktrees for parallel safety, Opus orchestrates + agent tiers at the
orchestrator's discretion, be ready for interruption/limit. Then, after the work:
surface any open decisions for Mike plain-language one-by-one, capture learnings,
tidy to close.

## Batch selection

Chose a batch that **shrinks** open work rather than growing it: two ⏳
first-of-kind scanner reviews (clear the review backlog) + the datescan DSR-apply
(advances Mike's flip 🎯). Deferred the S2/S4 scanner *builds* — they would each
add a new ⏳ review, growing the backlog, and both touch `ci.yml` (merge
contention). Rule-4 clearance for taking the two ⏳ reviews: wrapscan/spellscan
were authored by prior runs; this fresh Mike-started session neither started nor
instructed either build → cold-spawn test passed.

## Claim-first (interruption safety)

Claimed all three on `main` **before** workers landed (`4a3c737`, `[~]` +
taken-markers with rule-4 provenance) so a parallel session sees them taken. Pushed
immediately. Floor green on the claim commit.

## Landed

- **datescan DSR1–DSR8 + re-baseline** (Sonnet, worker `b7b292c` → merged): all
  eight findings applied, docs baseline **60→0**. Detection-logic fixes — DSR2
  plausible-date field gate (kills the `23/26/27` session-number FP), DSR3 `today`
  narrowed to date-adjacent contexts (the dominant noise source; the accepted
  silent-miss trade is declared honestly in-header), DSR4 enclosing-quote-span
  mention detection, DSR5 dash-DMY + a `YYYY-MM-DD-HHMM` lookbehind, DSR6
  indented-code exemption, DSR7 package-relative test import (all three invocation
  forms now green), DSR8 word-boundary allow-marker requiring a non-empty reason.
  Sonnet **caught three further real bugs** the review hadn't named (whole-line ISO
  cue leak, session-ID false-fire, empty `-->` reason) and **declined to guess** an
  un-derivable date (honest `allow`). Orchestrator (Opus) re-ran the suite (58
  datescan + 489 tools) and read the DSR3 logic + header before merge; no rework.
  Still `--warn`, `floor.yml` untouched.
- **wrapscan (S1) first-of-kind review** (Opus cold reviewer; brief
  `docs/reviews/2026-07-23-0707-wrapscan-s1-cold.md`): **PASS-WITH-FINDINGS —
  1 MAJOR / 3 minor / 2 Low**, NOT gate-ready. The MAJOR (WS1) is *gate-scope*,
  not a detection bug: default `docs/**` buries the genuine signal (~15%
  doctrine-prose over-wraps) under 154 deliberate single-line SESSIONS index rows
  (54% of the 287 baseline). Reviewer-preferred fix: scope the gate to the
  doctrine surface + `.wrapscanignore` the record stores. Orchestrator re-verified
  the 40 tests + the 154/287 SESSIONS share.
- **spellscan (S5) first-of-kind review** (Opus cold reviewer; brief
  `docs/reviews/2026-07-23-0707-spellscan-s5-cold.md`): **PASS-WITH-FINDINGS —
  0 MAJOR / 2 minor / 1 Low / 1 nit**, NOT gate-ready. Core spelling-tool safety
  property **proven** (no confident wrong correction; z→s engine verified across
  all 46 noun forms). Found a real latent bug (SS1: `hypothesize`/`jeopardize`/
  `penalize` in `IZE_NOUN_CAPABLE` contradict the docstring's stated exclusion).
  Baseline ~1-in-5 signal — 53 of 68 are `artifact`, mostly the legit CI/SBOM
  term-of-art; ROI weaker than the mining record claimed but not negative.
  license/practice exclusion ruled **permanent** (empirically vindicated).
  Orchestrator re-verified 60 tests, the 68 baseline, and SS1 in-source.

## Decisions surfaced for Mike — all three RULED + applied same session

Walked through one-by-one, plain-language (context / what-it's-for / per-option
impacts), per Mike's brief:

1. **datescan flip → RULED "agree flip it"** (`d24caec`). atelier `ci.yml`
   datescan dropped `--warn` (blocks clean); child `floor.yml` template gained a
   docs-scoped datescan blocking step + selftest for pin-bump adoption. datescan
   is now a **blocking floor scanner**.
2. **wrapscan gate-scope → RULED "option A"** (`efea6a5`). Doctrine-surface scope
   + `.wrapscanignore` the record stores; direction locked for the WS1–WS6 apply.
   Flip stays a Mike go/no-go once clean (not pre-authorised).
3. **spellscan `catalog` → RULED "rename to catalogue"** (`856818e`). House term
   is now "catalogue"; the ~10 hits are real. Live ROADMAP prose renamed; frozen
   mining-record + capture-stream sweep folded into the spellscan apply (backtick
   literals + the source-article quote stay verbatim). Flip stays Mike's once
   spellscan re-baselines.

Only decision 1 had an instant clean payoff (datescan was already re-baselined to
0); 2 and 3 set direction for future apply work, with the flips deferred to
Mike's go/no-go on a clean re-baseline — datescan's proven pattern.

## Learnings captured

- **Third-seat executor trial → Run 3** (this run) added to the ROADMAP record,
  and **Run 2 (0618) reconciled in** — the 0618 session had claimed "run 2" in its
  SESSIONS one-liner but never folded it into the canonical trial record (a V5
  internal-contradiction of the kind the invariant registry targets). Three runs
  now agree (five Sonnet items, zero rework); the reading is *floor density, not
  nominal class* — a well-floored silent-failure task with a prescriptive review
  is safely Sonnet-with-Opus-verify. Enough to promote Sonnet into ECONOMICS as
  the standing executor for well-floored + prescriptively-reviewed classes (a
  self-authored-doctrine edit, rule-4 ⏳ at landing, for a future session).

## Close state

Floor green at head; single worktree (main). Two ⏳ reviews cleared, datescan
flipped to blocking, all three surfaced 🎯 ruled + applied/recorded same session.
Economics stop on new *dispatch*: remaining queue is heavier focused-session
builds (S2/S4 scanners), self-authored doctrine needing a cold spawn (V1–V7
checklist, the Sonnet-executor ECONOMICS promotion the trial now supports), or
Mike-only raw notes (glossary, honesty/truth/transparency, the AI-chat note).
Open follow-ons left in good shape with directions locked: the wrapscan WS1–WS6
apply (option-a scope), the spellscan SS1–SS4 apply (incl. the catalogue sweep),
and both scanners' eventual flips (Mike go/no-go on a clean re-baseline).
