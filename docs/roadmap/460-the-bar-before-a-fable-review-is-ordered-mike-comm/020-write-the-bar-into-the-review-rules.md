- [x] **Fix the four doctrine causes `460/010` step 1 found: write the bar into the
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
      🔒 CLAIMED 2026-11-26T11:53Z (claimed 2026-11-26-1153, wt: atelier-460-020) by session
      4ccec293 (`atelier-56`, Opus 5.5), principal-opened by `/atelier:work run` with this item as
      its brief.
      ✅ **Landed 2026-11-26 (session 4ccec293, `atelier-56`).** `REVIEW.md` § *Whether work
      earns a review at all* now carries the bar (three questions in the intent record, no
      answer to the third means no pass), the never-on-its-own list, rule 3 as who rules
      rather than whether, one open pass per subject (with two exceptions: a briefed pass,
      or one he approved on its own terms or ordered), and his order outranking the test.
      A new section, *When a finding is fixed before use, and when fixes earn a re-check*,
      quotes his three sentences above and the 2026-07-13 stop. Rules 3 and 4, lifecycle
      step 4, the stop paragraph and the review line point at both. Compressed copies
      follow in `ECONOMICS.md`, `skills/review/brief.md`, `CONCURRENCY.md`'s landing step
      and the dispatch skeleton.
      **His "Haven't I ruled on this in the past":** partly. On 2026-07-13 he ruled that a
      review cycle closes at the first pass with no MAJOR, and that a MAJOR count not
      falling means stop and ask him. It was written for applying findings to doctrine
      only, so the drain code's chain never met it: under it, that chain closes at the
      `RK` pass (0 MAJOR, 2026-11-25), and three passes ran after it with a fourth queued.
      Nothing said when a finding is fixed before use; the new section does, from his
      2026-11-26 words.
      **Beyond his words, for him to confirm (asked at this session's close):** carrying the
      2026-07-13 stop from doctrine to code; and fixing two kinds of risk before use without
      evidence (a first occurrence that is itself irreversible, and a silent failure, whose
      evidence is a probe). The text marks the second as the repo's reading.
      **Review grounds (the bar, answered for this change):**
      1. *Commitment:* every session's decision whether to queue a cold pass, and whether a
         finding is fixed before use; rule 4 itself.
      2. *Worst failure:* the bar lets a change whose failure is silent or irreversible go
         unreviewed, or the fix rule leaves a real defect in use as a "risk".
      3. *Why the floor misses it:* no test reads what doctrine means; a bar set too loose
         fails silent, since unreviewed work looks the same as reviewed work.
      **Review:** queued as `160/1880` in the landing commit, a pass of its own as he
      ordered; it runs on Fable only when he approves.
