- [ ] **Fix the four doctrine causes `460/010` step 1 found: write the bar into the
      review rules** `[M][doctrine]`. Mike, 2026-11-25, on the step-1 answer ("mostly weak
      doctrine, not sessions ignoring it"), verbatim:

      > we need work to fix that on the board

      Grounded in the step-1 sample (42 queued passes; table, patterns and draft in
      [`../../sessions/2026-11-25-1249-work-run-fable-bar-and-fixes.md`](../../sessions/2026-11-25-1249-work-run-fable-bar-and-fixes.md),
      § *Annex*). One change, landed together, so it costs one cold pass, not four. Each
      cause and its fix:

      | Cause found | Evidence | Fix |
      |---|---|---|
      | Queuing needs no grounds; declining does | 13 of 42 pointers give none; the 18 `not warranted` lines are all on hand-ups | **The queue-time test:** a pointer answers (1) the commitment that will rest on the work, (2) its worst failure, (3) why the tests, floor and normal use would not surface that failure. No answer to (3), no pass: the pointer carries `review: not warranted — <grounds>` instead |
      | "Doctrine text" has no minimum size | 1470, 1750, 1760 queued only by the letter | **A materiality floor:** a wording or factual correction that adds no rule, and a sync of a copy to a reviewed or queued source, never earn a pass of their own |
      | Rule 3 + rule 4 override the self-verifying exemption for every tool | "self-verifying" weighed by no live pointer; 985, 987, 991, 992 | **Rule 3 decides who rules on findings, not whether a pass is owed.** A loud-failing fix to a reviewed tool its tests cover (a sort, a format, an output shape, a tightening that reds on misuse) is exempt. "Every child runs it" is reach, not grounds |
      | Passes scale with commits, not risk; re-check chains never stop | `ccclose` 8 passes, `ccfleet` 4, `board.py` 4; one run queued 14 in a day; 1450 → 1790 → 1820 | **One open pass per subject:** a change to a subject with an unrun `⏳` widens that pointer's delta instead of opening a new one. Say when a re-check is owed and when the chain stops |

      **Added 2026-11-26 (session a2aeebc8, `atelier-51`): the same loop, from the fix side.**
      His words, verbatim, on the drain code's chain (`160/1450` → `1800` → `1820` → `1870`):
      *"I worry that we are stuck in a loop of review - fix --review -- fix without proof of actual
      failures i.e. risks rather than issues"*. Asked when a finding should be fixed before the code
      is used again, his typed answer, verbatim: *"Haven't I ruled on this in the past - I thought it
      was written into the doctrine"*. It is not: `REVIEW.md` says when work earns a review and that
      findings on doctrine are his to decide (rule 3), but nothing says when a finding is fixed
      before use or when a re-check of fixes is owed; this item's fourth row is the nearest, and is
      unbuilt. So this item also says when a finding is fixed before use (a proposal for him to
      rule on: a MAJOR or a reproduced failure; the rest recorded until use shows them, as his
      `210/660` answer did) and when fixes earn a re-check. His words decide it, not this text.

      💬 **When it starts, his answer 2026-11-26 (session a2aeebc8, AskUserQuestion; an answer,
      not a ruling), typed, verbatim:** *"In a fresh session"*. So a fresh session builds it; the
      closing session handed him its prompt.

      **Where it lands:** `docs/method/REVIEW.md` (§ *Whether work earns a review at all*,
      rules 3 and 4, § *Review the design*'s review line), the compressed copies in
      `skills/review/brief.md` and the dispatch skeleton, and the `CONCURRENCY.md` landing
      step that writes the pointer. The draft in the annex is the starting text; wording is
      fitted to the rules as they stand.
      **Review:** self-authored doctrine that changes rule 4 itself, so it passes its own
      test: one cold pass, queued by its author at landing, run on Fable when he approves.
      **Feeds:** `460/030` (the gate checks what this writes), `460/040` (the dequeue round
      applies it).
