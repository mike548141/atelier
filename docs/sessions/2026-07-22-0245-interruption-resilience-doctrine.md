# 2026-07-22 · 02:45 UTC · Interruption resilience — surviving a mid-flight cut

**Trigger.** Mike, thinking aloud about doctrine: four kinds of accidental
interruption keep cutting sessions off mid-work — a Claude session-limit stop; a
network loss / API error (last night's <!-- datescan:allow: date ambiguous across the NZ/UTC boundary; wrapscan:allow: marker-inflated line -->
route out via the RB5009 instead of wifi); a closed or cancelled question
window; a cmd+Q on VS Code. "Are there things we
can do in the doctrine that help?" Ratified drafting all three identified gaps as
one change ("yes do it" / "i.e. all three").

## What the doctrine already carried (~80%)

The four interruptions are **one shape** — work cut off mid-flight, then resumed
or picked up cold. Grounding read before proposing anything:

- `CONCURRENCY.md` — worktrees, commit-small-push-fast, claiming, **orphan-claim
  reclaim** (a session that dies mid-item), every-branch-put-away, stay-in-lane.
- `RECORD.md` § Why this is doctrine — the operating model **assumes cold
  resume** is possible; the record is the substrate that makes it true.
- Precedent — the [2026-07-20 cmd+Q recovery sweep](2026-07-20-1830-cmdq-recovery-sweep.md),
  plus session 45's survival audit (2026-07-12). The scenario had been *handled*
  twice but never *lifted* into method.

## The three gaps closed (delta `9c11525`)

New `CONCURRENCY.md` § **Surviving an interrupted session** — deliberately
separated from the concurrency sections above it (concurrency = another session
clobbering yours; interruption = your own session cut off). It names the seam the
existing doctrine left:

1. **The resume-state carrier doesn't exist at the cut (high).** The session log
   that carries "where I was / what's next" is a *close-time* artefact; an
   involuntary cut never reaches close, so it leaves a clean tree but no intent.
   Fix: per-checkpoint legibility — resumer-followable commit messages (never a
   bare "wip") + an optional in-place claim-line breadcrumb (`… · at: <step>`).
   Framed as the same per-item-close durability the orchestrated-queue-run strand
   already relies on — referenced, not duplicated.
2. **Decision-limbo (medium).** A `🎯` question put only to chat is volatile; a
   dropped window loses it and a resumer can't tell "waiting" from "done". Fix:
   write the open question into the durable record *before* blocking on it.
3. **The recovery procedure wasn't in method (low).** Twice-grounded, so liftable
   per "ground everything". Distilled the sweep checklist (tree / sync / stashes
   / orphan worktrees / reflog-after-close) into a table, plus the resumer's tell
   — **did the last session close clean or die mid-flight?** — and the two lanes
   that hold throughout (orphan-claim reclaim on evidence not a timer; another
   repo's/session's recovery is not yours to run).

**Onramp firing pointer.** `CLAUDE.md` read-order step 4 (SESSIONS.md tail) now
says: a last commit then silence with no closing entry = died mid-flight → run
the sweep. Without this the section would be a rule with no firing condition —
exactly the gap session 46 named for the worktree rule.

## Deliberately not done — flagged for the review

- **Template propagation.** `docs/build/templates/CLAUDE.md` (children's onramp)
  did **not** get the died-mid-flight→sweep pointer. The method doc
  (CONCURRENCY.md) propagates to children on its own; whether the *template
  onramp* should carry the firing pointer too is a propagation call left as an
  open sub-question on the `⏳` roadmap item, for the reviewer/principal to weigh
  rather than the author to decide unilaterally.

## Review status — queued, not spawned

I authored this doctrine, so per `REVIEW.md` rule 4 I neither take nor spawn its
review. Queued the `⏳` **Interruption-resilience cold pass** pointer (delta +
this record) on ROADMAP for a non-author to take. Cycle closes on a no-MAJOR
pass.

## Provenance note

This ran alongside Mike's separate draft (Untitled-1) about orchestrating
parallel queue-run sessions — thematically adjacent (that strand's per-item-close
bullet overlaps Gap 1) but a distinct piece of work; treated as the standalone
doctrine thought it read as, and cross-referenced rather than merged.

## Incident — `git add -A` swept a sibling's worktree gitlink (fixed)

Honesty note (apex): the records commit `b4b5142` was made with `git add -A`,
which grabbed `.claude/worktrees/scope-lens4-app-cold` — the SL1–SL7 cold-pass
session's **live, locked, harness-native worktree, nested inside this repo** — as
an embedded-repo gitlink, and pushed it to `main`. The sibling's work was never
touched (only its gitlink was staged), but a stray submodule entry reached
shared `main`. Fixed forward in `b4b5142`→next: `git rm --cached` the gitlink
(files untouched), gitignore `.claude/worktrees/`, push. The bad gitlink stays
in history (append-only; never rewrite pushed history); HEAD is correct and it
cannot recur. Root cause: the harness places worktrees *inside* the repo tree,
so `git add -A` from any session reaches into every other session's worktree —
the exact stay-in-your-lane breach this session was writing doctrine about. The
mechanical fix (gitignore) now enforces the lane; the discipline lesson —
**stage explicit paths, never `-A`, when worktrees can nest in the tree** —
is saved to memory.

## State at close

- Delta `9c11525` on `main`, pushed; worktree + branch put away.
- ROADMAP: drafting claim `[x]`; `⏳` review pointer queued.
- Sibling `scope-lens4-app-cold` worktree intact + locked; its gitlink now
  untracked and gitignored.
- All three pre-commit scanners green (secret / leak / link); tree clean, 0/0.
</content>
</invoke>
