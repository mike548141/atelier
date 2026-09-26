# 2026-09-25 · 0705 UTC — Review batch: every queued rule-4 pass, in one run

**Tier:** Fable 5.1 (`claude-fable-5-1`) orchestrating; twenty Fable 5.1
reviewer subagents, one per pass. Both seats on the principal-named tier, so
rule 4's off-tier clause was not invoked; the reviewer-plus-orchestrator shape
was disclosed in every claim line, every brief and every verdict anyway.

**Commission.** Mike, 2026-09-24: *"Please deliver all fable dependent work,
and work that would be best delivered using fable."* An earlier sitting on
2026-09-20 had prepared the batch's brief data under his standing prompt, then
stopped at his 11:00 NZT cut-off without claiming anything (recorded then as a
user-local hand-off, not in this repo).

**Onramp.** Tree clean at `548b706`, 0/0 with origin. A peer session was live
in a separate worktree filing a hand-up from a child; untouched throughout. The
2026-09-20 run's detail file existed with **no `SESSIONS.md` index entry and no
closing block** — an interrupted session; the index line is added by this
close (see *Records*), the content left as the cut left it.

## Shape

The 2026-08-09 / 2026-08-15 pattern, run at full width:

1. **One claim commit on `main`** from the primary checkout (`74f2f98`): all
   twenty `⏳` pointers gained a `[~]` CLAIMED sub-bullet naming the brief in a
   code span, the shape, and the reviewer's non-exposure. Pushed before any
   brief existed.
2. **Worktree** at `/Users/mike/worktrees/…` (outside the repo, so no gitlink
   hazard), branch `review-batch-0925`.
3. **Twenty refs-only briefs** generated from one template (`c4b9cd0`,
   merged `a1aacf6` before the first spawn): landing commits, delta paths,
   scope, four lenses with per-pass probes, re-run list, house rules for a
   shared worktree, and a deferral section carrying the `reviewscan` allow
   marker. Every evaluative account — intent records, prior verdicts, the
   pointer's own *lens that matters* paragraph (the author's framing), and
   the brief-writer's seeded questions — went to a `.deferred.md` sibling
   that was **never committed**.
4. **Reviewers in four waves** (7 doctrine · 6 mixed · 4 code · 3 code),
   sharing the worktree read-only, running no git writes, probing in scratch
   clones. Phase 1: verdict appended below the divider, stop. Orchestrator
   commits it unrevised, releases the sibling by message. Phase 2: reconcile
   appended, never revising phase-1 text. Orchestrator folds the sibling in,
   marks the pointer, rebuilds the board, merges `--no-ff` to `main`, pushes.
   Twenty per-pass closes; the last merge is `63ae645`.

## Outcomes

| Pass | Item | Overall | Cycle |
| --- | --- | --- | --- |
| AR | 160/090 AP rulings applied | FAIL — 2 MAJOR · 2 MODERATE · 2 minor · 2 note | OPEN |
| BA | 160/260 BW rulings applied | 1 MAJOR · 1 MODERATE · 4 minor · 2 note | OPEN |
| DR | 160/270 DA rulings applied | 1 MAJOR · 1 MODERATE · 1 minor · 6 note | OPEN |
| PV | 160/280 PU rulings applied | 0 MAJOR · 1 MODERATE · 3 minor · 1 note | closed |
| AK | 160/290 ask rule to children | 0 MAJOR · 2 MODERATE · 1 minor · 4 note | closed |
| RU | 160/300 report-up duty | 1 MAJOR · 7 MODERATE · 3 minor · 1 note | OPEN |
| HF | 160/310 0918 hand-up fixes | 0 MAJOR · 4 MODERATE · 6 minor · 2 note | closed |
| RC | 160/320 0918 registry code | FAIL — 1 MAJOR · 2 MODERATE · 6 minor · 6 note | OPEN |
| TR | 160/330 tier ruling | 0 MAJOR · 3 MODERATE · 6 minor · 2 note | closed |
| FV | 160/340 floor verbatim | 0 MAJOR · 3 MODERATE · 4 minor · 4 note | closed |
| SP | 160/350 secretscan stream, pathscan roots | 0 MAJOR · 4 MODERATE · 5 minor · 2 note | closed |
| NP | 160/360 naming precedence | 0 MAJOR · 3 MODERATE · 4 minor · 3 note | closed |
| BL | 160/370 bounded guard layer | 0 MAJOR · 2 MODERATE · 6 minor · 5 note | closed |
| SK | 160/380 scratchpad clause | 1 MAJOR · 3 MODERATE · 3 minor · 3 note | OPEN |
| SG | 160/390 staged-plane check | 0 MAJOR · 3 MODERATE · 6 minor · 3 note | closed |
| HP | 160/400 harvestscan prefix filter | 1 MAJOR · 0 MODERATE · 5 minor · 3 note | OPEN |
| LW | 160/410 linked-worktree skip | 0 MAJOR · 2 MODERATE · 5 minor · 3 note | closed |
| FW | 160/420 single-sourced file walk | 0 MAJOR · 3 MODERATE · 5 minor · 5 note | closed |
| CC | 210/130 ccmail build | 1 MAJOR · 4 MODERATE · 6 minor · 2 note | OPEN |
| PW | 300/040 PT rulings applied | 0 MAJOR · 2 MODERATE · 5 minor · 3 note | closed |

Totals: 10 MAJOR · 52 MODERATE · 86 minor · 62 note across twenty verdicts.
"Closed" means the cycle terminates on this pass (no MAJOR) and what remains
is decided into the backlog; "OPEN" means a MAJOR stands. **Every finding is
the principal's to decide (rule 3); nothing was applied.** Each verdict file
carries its findings, its reconcile against the intent records, and the folded
sibling; each pointer carries the pass's outcome line.

## The ten MAJORs, in one line each

- **AR1** — ADR 0008's 2026-08-23 amendment says `main` has no ruleset and
  signing is warn-first; a ruleset with deletion, non-fast-forward and
  required-signatures rules has been active since 2026-08-09. The ADR every
  child inherits misstates its own control clause. **AR8** (at reconcile) —
  see the verdict.
- **BA1** — the 2026-09-20 rewrite of CONCURRENCY § *On a split board* deleted
  the dirty-sibling stop sentence, ruled twice, and pointed at a CF3 that does
  not carry it.
- **DR1** — the "reached him" rule branches on a display state a session
  cannot observe; under focus mode the default reproduces DA1's
  extracted-approval shape. A rule-3 challenge on the briefing behind DA1.
- **RU1** — the stamped floor bullet carries the four no-harm rules and omits
  the class-only privacy rule, so a private child following its block can name
  itself on four irretractable surfaces.
- **RC1** — `conflictscan --staged` and `leakscan --staged` parse only a
  literal `+++ b/` header; under `diff.noprefix` they scan nothing and exit 0.
  Live-proven green on a staged conflict marker and a staged email.
- **SK1** — the harness hands every reviewer the orchestrator's own scratchpad,
  where this batch's siblings sat; the rule-1 "structural" partition was one
  read away from any reviewer. (Siblings moved out of the scratchpad on
  reading it; the exposure window is disclosed in the batch's commits.)
- **HP1** — harvestscan's exact rewrite rebuilds its survivor index once per
  watched file, so on the split board it is slower than the quadratic pass it
  replaced; exactness itself holds on every probe.
- **CC1** — the ccmail credential-route ruling omits the delegation grant's
  domain-wide blast radius and the cloud CLI's plaintext refresh token; a
  rule-3 challenge on the briefing.

## What the batch found about itself

- **The hook's `datescan` is tree-wide on the hook plane.** One close was
  blocked by a relative-time word in another reviewer's unfinished draft;
  retried clean once that reviewer finished. Known from 2026-08-09, still true.
- **Seven concurrent full-suite runs contend.** Three reviewers saw
  memory-probe timeouts that pass alone; two had the harness background a
  foreground suite run past the tool's limit. Recorded per verdict as
  environmental, and the pushed floor is the all-clear.
- **Sweep hygiene needs `--also-exclude` for every barred board item.** Five
  reviewers disclosed fragments of barred items surfacing from a first sweep;
  each says what it saw and that no finding rests on it. Later waves were told
  up front.
- **The mid-batch relocation of the siblings** answers SK1's counsel (b) in
  the reviewer's own words: no disk-held shape is structural in this harness.

## Records

- `docs/SESSIONS.md` gains this entry and a **recovery-added index line for
  the 2026-09-20 run**, whose detail file was committed without one; three
  passes (BA8, FW12, HP9) record that the file also carries no account of
  three of the four items it claimed. The content is left as the cut left it.
- The review worktree is removed and its branch deleted; every commit is on
  `main`. Two peer worktrees for child hand-ups were live and untouched.

## Owed by the principal

🎯 **A ruling round on 210 findings, ten of them MAJOR**, in the twenty
verdict files under `docs/reviews/2026-09-25-0715-*`. The nine OPEN cycles
(AR, BA, DR, RU, RC, SK, HP, CC — AR carrying two) block their application
passes until ruled; the eleven closed ones decide into the backlog. RC1 and
AR1 are the two a reader should meet first: one is a silent-green in two
enforced guards on every commit under a common git config, the other a
security-control clause inherited by every child that is wrong at HEAD.
