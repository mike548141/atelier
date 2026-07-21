# Cold pass — REVIEW.md scope mandate + security & privacy lens 4 (deltas `f9db922` + `a059e49`)

- **Date/time**: 2026-07-21 2158 UTC
- **Spawn provenance (rule 4)**: taken from the ROADMAP `⏳` queue by a session
  Mike spawned with "Please do any review work" (Fable). The taker authored
  neither delta, none of the files they touch, and no record of the authoring
  session. Claim landed on `main` (`3909d76`) before review work started; this
  brief is taker-written in wt: review-scope-lens4-cold-pass. The review run
  itself is a fresh-context subagent spawned by the taker — a spawn the
  author neither started nor instructed, so the criterion holds through both
  hops.
- **Named exposure (the taker's, not the reviewer's)**: before writing this
  brief the taker read the author's intent record
  (`docs/sessions/2026-07-21-2147-review-scope-security-lens.md`) in full —
  including the author's own account of the gap audit and a framing note
  addressed to this cycle — and both delta commit bodies. That is author
  framing the taker cannot un-read. Mitigation, per rule 1's shape: the
  taker's seeded questions sit **below the divider**, the reviewer is a
  separate cold context that has read none of that material, and everything
  above the divider is refs and mechanics only. The brief's framing remains
  attackable.
- **Deferred material (reviewer opens only after its own findings are
  durably drafted)**: the seeded questions below the divider; the intent
  record named above; the commit bodies of `f9db922` and `a059e49`; prior
  verdicts in `docs/reviews/` (notably the 2026-07-15 and 2026-07-19 cycles
  the delta's text cites).

## What the work is (refs only)

Deltas `f9db922` + `a059e49` (2026-07-21), reviewed as one, at worktree HEAD:

- `docs/method/REVIEW.md` — a scope paragraph above the lens list (*What a
  review actually checks*), a fourth lens, and a sentence naming a harness
  scanner inside it.
- `docs/method/README.md` — one summary-line change.
- `docs/build/templates/docs/reviews/README.md` — the child-floor template
  carrying corresponding text.

In scope at HEAD: those files, plus every other surface that states, counts,
or relies on the lens structure or review scope — templates, skills, method
docs, ROADMAP conventions — per the delta's own scope rule. The review runs
under the doctrine as amended: all four lenses, applied to the text that
defines them.

## Why it earns a review

Self-authored doctrine by function (rule 4): these paragraphs govern every
future review in this repo and, via the child template, every repo on the
fleet floor — the widest blast radius in the operating model. Worst failure
modes: a scope or lens rule that is uncostable in practice and gets
appeased rather than followed; an instruction that cannot actually be
executed as written (a tool named where it cannot run); a narrowing escape
left open in the very text that was meant to close narrowing escapes.

## Reviewer instructions

1. Read this brief **down to the divider and stop**. Read the repo: the
   three delta files at HEAD in full, `git show f9db922 a059e49` **with
   `--format=` so the author's commit bodies stay unseen**, and whatever
   siblings your own attack surface demands.
2. Name the load-bearing assumptions yourself as your first act (lens 1);
   run all four lenses as the amended text defines them — this review is
   also the first live execution of the rules under review, and any point
   where you cannot comply as written is itself a finding.
3. Re-run every live-proven claim in scope. Where lens 4's scanner
   instruction applies, execute it or discharge it exactly as the text
   directs, and report how that went as evidence.
4. Draft findings with stable IDs (SL1, SL2, …) and severities
   (MAJOR/MEDIUM/LOW), durably written to
   `docs/reviews/drafts/2026-07-21-2158-scope-lens4-findings-draft.md`,
   **before** opening the deferred material. Then open it, reconcile —
   never anchor — and produce the verdict: per-lens answers, findings,
   follow-ups, and a repeat of the spawn provenance above.

Non-goals: the conduct of the 2026-07-21 authoring session (its record is
deferred context, not the work); re-litigating rulings Mike has already
made in prior closed cycles (attack how this delta *encodes* them, not the
rulings themselves); the reviewscan/review-line machinery closed in the
0913 cycle.

---

## Deferred — the taker's seeded questions (a floor, never a fence)

- **SQ1 — unbounded scope vs "scoped and short".** The new mandate says
  scope is the widest the work admits and non-goals are the only legitimate
  narrowing; *When to review* still requires every review to stay "scoped
  and short". Can a reviewer honour both, or does the pair train sessions to
  write sweeping non-goals to make reviews finishable? Note who writes the
  non-goals in a warm (non-rule-4) brief: the author. Is "non-goals are the
  only legitimate narrowing" an escape hatch in exactly the wrong hands?
- **SQ2 — lens 4's cost calibration.** "A must on every review" plus
  "checked, not recalled" against OWASP: what does this cost on a
  ten-minute doc review? Is the one-line discharge shape well-enough
  defined to stay honest (who judges "genuinely no surface"?), or will it
  become the reflex stamp that hollows the lens?
- **SQ3 — the scanner instruction's executability.** Claude Code's
  `/security-review` reviews *pending changes on the current branch*. A
  rule-4 cold pass reviews an already-committed delta on a clean tree; a
  design-time review has no diff at all. Does the instruction as written
  misfire in the two review shapes this repo most actually runs? What did
  it do when *you* executed it per instruction 3?
- **SQ4 — stale lens arithmetic.** The delta chose "lens 4" to keep 1–3
  references valid. Sweep the repo (and templates/skills that ship to
  children) for "three lenses", "all three", lens counts in prose, and any
  place the lens list is restated but not updated.
- **SQ5 — "where possible" as an escape.** Real-world behaviour must be
  exercised live "where doing so is possible". Is there any test or burden
  attached to a claim of impossibility, or does "wasn't possible" become
  the new "no source code"?
- **SQ6 — child-floor fidelity.** Does the template sentence actually
  compress the parent without narrowing (scope, all four lenses, the
  scanner clause), and does anything in it break for a child repo whose
  harness has no `/security-review`?
