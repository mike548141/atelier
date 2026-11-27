- [x] **Judge every queued pass against the new bar and bring him one dequeue list**
      `[S][ruling]`. Mike, 2026-11-25, verbatim: *"we need work to fix that on the board"*.
      Step 4 of `460/010`, split out.
      Once `460/020` lands, apply it to every owed pass in `160/` (step 1 counted about
      130: 42 `⏳`, 70 `🎯`, 18 `🛑`) and across the estate's queues. For each: keeps,
      folds into another pass on the same subject (name it), or fails the bar. Step 1's
      sample already points at 985, 987, 991, 992, the corrections 1470, 1750, 1760, and
      the per-commit chains on `ccclose`, `ccfleet` and `board.py` as the first candidates.
      **Then:** one plain-language ask to him with the judged list, in one go
      (one question, not one per pass). Nothing is dequeued on a session's own reading.
      **Blocked on:** `460/020` landing.
      **Unblocked 2026-11-26:** `460/020` landed. The round also applies the new fix and
      re-check rule: a queued re-check of fixes whose pass returned no MAJOR (the drain
      code's chain after `RK`, `160/1870` among them) is a candidate to judge.
      **Round run 2026-11-27 (session 4ce066ba, `atelier-c1`; an Opus worker judged, the
      orchestrator spot-checked and corrected).** Of 140 open `160/` items, **45 are passes
      still owed**; 91 already ran and wait on his rulings on findings, not on a pass; 4 are
      not passes (120, 130, 140, 160). Of the 45:
      - **Fails the bar (8):** 985, 987, 992 (briefed; loud fixes or output shape to tested
        tools, reach-only grounds); 1470 (a copy-sync to text 1440 already reviewed); 1530
        and 1550 (tightenings that red on misuse, census found 0 affected); 1750 (factual
        corrections and an output line); 1840 (re-check of fixes from a pass whose worst was
        MODERATE; weaker, since it also asks for a first look at a design never reviewed).
      - **Folds (6):** 1560 into 1710, 1580 into 1500, 1630 into 1490, 1650 into 1540, 1700
        into 1680, 1830 into 1880 (same subject, each pair unbriefed).
      - **Can't tell (2):** 991 (briefed; the record gives reach only), 1760 (the bar's text
        decides it both ways, filed as `460/070`).
      - **Keeps (29),** among them 1460 and 1880 on his own orders, and 1870, which fails the
        re-check rule by name but carries his typed *"run it as part of the drain"*.
      **A correction to the worker's brief:** it was told a briefed pass is no dequeue
      candidate. That was the orchestrator's error, not doctrine: a brief costs Opus and the
      pass costs Fable, and this item names briefed passes (985, 987, 991, 992) as first
      candidates. Briefed passes are judged like any other.
      **Also found:** 1610 and 1620 credit "drain priority: low" to him with no words of his;
      1320 plans a re-check after a 0-MAJOR pass that the new rule no longer owes; dequeuing
      1470, 1530, 1550 or 1750 takes back a pick of his (*"API credit if parity"*,
      2026-11-17, or *"Next drain (Recommended)"*, 2026-11-23), so the ask says so.
      **Next:** the one ask, at this session's close. Nothing is dequeued before his answer.
      💬 **His answers, 2026-11-27 ~01:55 UTC (session 4ce066ba, AskUserQuestion; answers,
      not rulings):** the list, *"Drop 8, merge 6 (Recommended)"* (option text: *"31 reviews
      stay in Monday's drain. Takes back your earlier picks on 4 of them."*); `160/1870`,
      typed, verbatim: *"Release it as per your recommended option - but to clarify we now
      have a better definition than just "are there any major findings""* (his correction
      of the framing is `460/080`); four briefed design passes in a private child for
      features not yet being built, typed, verbatim: *"Run them at the next drain
      (presumably Monday). Reviews of designs unblock the work to create and test the
      feature"*, so they stay queued as they are.
      ✅ **Closed 2026-11-27:** the 8 dropped, the 6 folded and `160/1870` released in the
      commit that applies his answers to `160/`. The unbriefed passes in other repos'
      boards were not judged in this round; only the drain's briefed queue was.
      review: not warranted — board bookkeeping applying his own picks; no rule changed.
