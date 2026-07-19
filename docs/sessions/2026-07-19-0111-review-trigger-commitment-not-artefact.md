# 2026-07-19 · 0111 UTC · the review trigger is commitment, not artefact — fixing the framing upstream

Mike quoted back a line from the previous session's diagnosis — *"when a rule
keeps getting broken despite being written down, suspect its framing before its
enforcement"* — and named what he liked about it:

> "We should fix the source of the problem upstream rather than adding more and
> more mitigations downstream to mitigate the problem."

He also asked whether the `⏳` cold review queued on `30c9cd9` had run. **It had
not** — no verdict file exists for it, and the queue pointer is still open. Eight
commits had landed since, none of them the review.

## What the previous session got right, and where it put the fix

The 2026-07-18 change diagnosed the defect correctly: every formulation of the
review-scope rule was phrased around *a change*, and that grammar presupposes the
work already exists, so an agent holding a design never saw itself in the text.

Then it wrote the diagnosis into `method/REVIEW.md` and stopped. A sweep of
`method/` and `build/templates/` found what that left standing.

## The two findings

**The correction never reached the artefacts that carry it.**
`build/templates/docs/reviews/README.md` — stamped by `create-repo` into every
child, and the file an agent actually reads when deciding whether to queue a
review — still carried a trigger list that was 3-for-3 diff-shaped, and still
named *"a doc line"* on its not-review-worthy list. `REVIEW.md` cites that
template as one of the three places "the correct rule already sat" when the `ros`
session broke it. It was not the correct rule; it was the broken one, and it
propagates by template into the whole fleet.

**That file was an unmarked fork — the actual upstream defect.**
`templates/CLAUDE.md` carries a header saying *"this is a stamped copy, not a
second source"* and names its canonical origin. The reviews template carried no
such marker: it pointed up for the *lifecycle* while silently restating the
*trigger* and the *brief format* as its own. A second source, unmarked, free to
drift — the N-copies shape `PROPAGATION.md` explicitly rejects, reproduced inside
the doctrine that forbids it.

The tell that yesterday's fix was downstream: correcting the grammar needed
patches in five places, and the *next* correction would need five more. That was
the plan on the table before Mike's steer.

## What changed

1. **`method/REVIEW.md` — the trigger re-keyed on commitment, not artefact.**
   *Whether **work** earns a review at all*; the question is now *what will come
   to rest on this once it is trusted*, which parses the same holding a
   paragraph, a plan, or a patch. The design-holder is inside the grammar at the
   point of asking instead of being rescued by a later section.
2. **The downstream explanation shrank.** The *Review the design* section's
   "why the framing was the trap" paragraph existed to rescue a reader the
   wording had already turned away; it now hands the correction upstream and
   carries the transferable rule instead — framing before enforcement.
3. **The reviews template converted from fork to pointer.** Gains the
   stamped-copy header, naming `REVIEW.md` canonical and recording the
   2026-07-18 drift as the worked example of why. Trigger becomes the one
   commitment question plus a thin floor; calibration is explicitly the parent's
   call. Brief format made fillable by unbuilt work (`Build`→`Subject`,
   `Real-world check`→`Grounding`). *"A doc line"* is gone from the carve-out,
   replaced by its opposite: prose is not routine by virtue of being prose.
4. **`MODEL-ECONOMICS.md` + `templates/CONTRIBUTING.md`** re-nouned, pointing at
   `REVIEW.md` for the trigger rather than implying their own.

**Honest measurement:** the diff is **+89/−47** — net *larger*, not smaller. The
thing that shrank is the number of independent statements of the trigger rule:
**four → one**, with three pointers. That is the metric that matters here, and
claiming a line-count win would be the wrong claim.

## Concurrency — caught mid-turn

The session started on a clean tree. Partway through, `sizescan` reported
`ROADMAP.md` at 297 lines when it had read 310 minutes earlier — a file this
session had not touched. `git status` then showed another session's **staged**
changes across `ROADMAP.md`, `ROADMAP-DONE.md`, `SESSIONS.md`, a session file and
`tools/sizescan.py`: live, mid-commit.

Recovery per `CONCURRENCY.md`: the four edited files were disjoint from theirs, so
the diff was captured as a patch, `main` restored to their changes alone, and the
work moved to worktree `atelier-review-trigger-commitment`. Floor clean there
(linkscan, leakscan, sizescan, 12 template tests).

## Owed, and deliberately not done

- **The `⏳` ROADMAP entry needs its delta extended** to name these four files so
  the cold reviewer sees one delta, not two. Not done here: the queue is edited
  in place on `main` (`CONCURRENCY.md` § Claiming work), and `main` was mid-commit
  in another session.
- **The structural remedy the 2026-07-18 change promised still has no artefact.**
  No ADR template, decisions README or ROADMAP template carries a `review:`
  field, so the templates keep manufacturing the blank the rule calls a bug. This
  session's decision record carries the line by hand as the worked example;
  the template change is queued rather than made, to keep this delta reviewable
  as one thing.
- **No review spawned.** Self-authored doctrine, and this delta's author is the
  prior delta's applier ⇒ REVIEW rule 4 in full: pointer queued, no brief
  written, the non-author taker writes it and takes both deltas together.
