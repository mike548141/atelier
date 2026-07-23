# 2026-07-23 · 0959 UTC · Orchestrated queue run — 2 applies + 2 scanner builds + a doctrine capture, with two floor rescues

**Orchestrator:** Opus (Mike-started, model confirmed before dispatch per the
stop-if-wrong-model instruction). **Workers:** 4 Sonnet, each in an isolated
worktree, committed on its own branch and handed back — the orchestrator (Opus)
verified every worker's numbers against merge-base, merged, wired shared config,
and owned all records (zero record conflicts across four merges).

## Brief

Mike's standing queue-run brief: maximise plan use, drain the unclaimed queue,
worktrees for parallel safety, Opus orchestrates + agent tiers at the
orchestrator's discretion, stop if started on the wrong model, be ready for
interruption/limit. Then, after the work: surface any open decisions for Mike
plain-language one-by-one, capture learnings, tidy to close.

## Batch selection

Loose-ends-and-unblockers first, then features near done. **Wave 1** (two
prescriptively-reviewed *applies* — the class three prior runs validated for
Sonnet): apply the wrapscan (S1) and spellscan (S5) cold-review findings — each
unblocks a Mike flip 🎯. **Wave 2** (finish the near-done S1–S5 scanner set —
3/5 built): build S2 (pathscan) and S4 (stampscan), the last two approved
scanners. **Item E inline** (small, disjoint, doctrine-text → Opus seat): the
RECORD.md close-all-clear capture. Deliberately *not* taken: the two ⏳ reviews
this run's builds queued (author≠reviewer), the Mike-blocked 🎯s, and the larger
design strands.

## What landed (per-item close, each pushed before the next)

- **Wave 1 claims** `d8c9d6d`; **A — wrapscan apply** (Sonnet `ceb3fda`, merged
  `191efdd` close): option-A doctrine-surface scope + `.wrapscanignore`, 3 real
  over-wraps fixed, WS2 tightened (structural pipe), WS4 sibling allow-marker
  padding exempt, WS3 accepted-and-documented (reprocessing an unclosed fence
  would false-positive on truncated pasted code), suite 497, gated scope 0.
  Flip precondition now met. **B — spellscan apply** (Sonnet `b910962`, merged
  `4872f07`): SS1 (3 irregular-noun stems dropped), SS2 (macron out-of-scope
  declared), SS3 (allowlisted the CI/SBOM `artifact` term-of-art + OWASP chapter
  names), `finalise` fix, `catalogue` rename in 2 frozen records (article quote
  verbatim). Baseline 71→40; worker **honestly surfaced** that ~36 of the
  remainder are the *general* "produced-thing" `artifact` sense living in frozen
  historical records its bounds didn't touch → new 🎯 for Mike.
- **Item E** `97b4fd2`: RECORD.md's all-clear evidence rule gains a sub-point —
  when a close pushes, the evidence is the **floor at head**, not the local scan.
  Self-authored doctrine ⇒ ⏳ non-author review queued in the same commit
  (landing = queuing, AWA2).
- **Wave 2 claims** `d7b3b56`; **C — pathscan (S2)** (Sonnet `b738f21`, merged):
  standalone advisory scanner for bare-prose/backtick repo-path resolution (the
  half linkscan's markdown-link resolution can't see). Triple-anchor resolution,
  53 tests, honest 174-finding heuristic-noise baseline. **Wired advisory** in
  `ci.yml`. **D — stampscan (S4)** (Sonnet `2fe97f3`, merged): a genuinely new
  mechanism comparing an inlined-floor stamped block to its pinned canonical
  parent region; marker convention wired to the real
  `templates/CLAUDE.md`↔`PROPAGATION.md` floor pair (byte-identical → CLEAN), 46
  tests. **Built but left UNWIRED** — see the floor rescue below. Wave-2 close +
  CI wiring `831ca05`; combined suite 601.

## Two floor rescues — the close-all-clear doctrine, dogfooded the same run it was written

The run **caught the floor red at head twice**, exactly the failure mode item E
names ("scanners green locally ≠ floor green at head"). Both were fixed and the
head floor confirmed green (`gh run watch`) before any all-clear.

1. **Cold-content gate** (`3a829c1`): the per-item `[x]` flips left three
   completed items on the hot path; `sizescan --check` reds on that (the
   current-truth/history split). Harvested all three verbatim to
   `ROADMAP-DONE.md` under a queue-run-0959 section; live ROADMAP keeps only the
   open follow-ons as non-checkbox pointers.
2. **stampscan config error** (`4f637b0`): the *load-bearing* finding of the run.
   stampscan's marker parser recognises stamp markers **anywhere it scans** —
   including prose and code spans that merely *document* the syntax — and a
   stray/unpaired marker is a hard config error (exit 2) that `--warn` does NOT
   suppress. So the advisory `ci.yml` stampscan step let a ROADMAP pointer
   *describing* the markers red the blocking floor. **"Advisory" wiring was not
   actually non-blocking.** Resolution: **unwired stampscan** (kept it built +
   tested + merged for its ⏳ review), neutralised the two prose marker mentions,
   and made "strip fenced/inline code before marker-hunting, like every sibling
   scanner" the explicit precondition to wire. Deliberately did **not** patch the
   just-merged unreviewed tool myself (author≠reviewer) — the fix rides its
   first-of-kind review. pathscan stays wired advisory (genuinely non-blocking).

## Third-seat executor trial — Run 4 (honest: not a clean sweep)

Four Sonnet items. **Three clean, no rework**: the two applies
(prescriptively-reviewed-fix class) and pathscan (fresh-scanner-build class) —
both classes already validated across runs 1–3. **The fourth, stampscan, was
NOT clean**: a genuinely-new mechanism (marker parsing) whose failure mode
(parsing its own documentation) its fixtures didn't cover; the worker flagged
fence-stripping as an "unexercised residual" but did **not** foresee it would red
the floor. The defect surfaced at head and needed an **orchestrator correction**
(unwire). Reading: this *strengthens* the tier-split's safety argument — a
catchable failure was caught by the floor + orchestrator review, exactly where
the split says to spend capability — while it *sharpens* the discriminator. The
guardrail is **floor density, not nominal class**: a fresh build of a *novel
mechanism* has a thinner floor (fixtures can't anticipate an unknown failure
mode) than a fresh build of a *known pattern* (pathscan reused linkscan-shaped
resolution; the applies had prescriptive briefs). So the standing-executor claim
should read "well-floored builds of *known* patterns + prescriptively-reviewed
fixes", and explicitly *not* "any first-of-kind build" — a genuinely novel
mechanism keeps Opus-verify-at-merge earning its keep.

## Economics stop

Stopped after the ready, well-floored, unclaimed atelier-local queue was
drained. What remains open is Mike-blocked (🎯), review-owed (⏳ this run can't
take), fleet-propagation (other repos, at their pin bump), or larger design
strands — none a loose end for this session, and the next coherent build
(codify V1–V7, doctrine) is better cold in a fresh session. Two ⏳ reviews
queued this run; adding a third doctrine item here would grow, not drain.

## Floor at head

Green (`4f637b0`, floor run success): tools suite 601, all scanner selftests OK,
gated scanners (datescan/wrapscan/sizescan `--check` + leak/secret/link) exit 0,
single worktree, 0/0 sync. Four 🎯 decisions surfaced for Mike (below / in
ROADMAP), none silently skipped.
