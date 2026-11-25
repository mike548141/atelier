- [ ] **Find out why work that should not qualify is getting a Fable review
      ordered, then set a bar a session can check before it queues one**
      `[M][doctrine]`. Mike commissioned this, 2026-11-24. Verbatim:

      > We need to set a clearer bar or definition that work must meet before
      > a fable review is ordered, I am seeing work that simply should not
      > qualify and I dont know if that is a weak doctrine or sessions
      > ignoring the doctrine

      **What the house says today.** `REVIEW.md` § *Whether work earns a
      review at all — calibrate to risk* keys the trigger on commitment, not
      artefact, and names what earns a cold review (first-of-kind or
      structural work, a silent-failure mode, doctrine text, irreversible or
      public actions). It exempts work that is *self-verifying*: tests and
      dogfooding exercise it end to end over already-reviewed machinery, so the
      floor is the review. Rule 4 adds that self-authored doctrine always earns
      a cold spawn. § *Review the design* adds that each durable design record
      carries a review line, a queued pointer or `review: not warranted —
      <grounds>`.

      **First evidence, from the filing session (2026-11-24), not yet a
      diagnosis.** The `160` section holds 41 queued `⏳` passes. Eight of
      them are cold passes on successive changes to one instrument, `ccclose`
      (`870`, `993`, `1010`, `1020`, `1260`, `1350`, `1560`, `1710`); others
      by title are small behaviour fixes to tools already reviewed (`987`
      board sort order, `988`, `992` quiet selftests). On their titles alone
      these look like the self-verifying class the doctrine exempts. The files
      have not been read yet, so that is a lead, not a finding.

      **Both causes look possible; the work is to tell which, by count.**
      - *Weak doctrine:* the bar is a judgement with no test a session can
        apply at the moment it queues. "Doctrine text" is wide enough that
        any wording change to a skill or method file qualifies, and rule 4
        then makes the cold spawn mandatory. The review line is lopsided:
        declining needs written grounds, queuing needs none, so queuing is
        the path of least resistance.
      - *Ignored doctrine:* the self-verifying exemption exists but nothing
        asks for it at queue time, and no gate checks a pointer's grounds.

      **Work owed.**
      1. Sample the queued passes in atelier and across the estate. Classify
         each against today's text: meets the bar, fails it, or the text
         cannot say. The split answers his question with numbers.
      2. Write the bar as a test a session runs before it queues: the
         commitment that will rest on the work, its worst failure, and why
         the tests and floor would not catch that failure. A pointer that
         cannot answer the last part does not queue. Ground the wording in
         the sample, not invented to fill the heading.
      3. Enforce it where a machine can: refuse a pointer that lacks the
         grounds at queue time and at the drain's ranking step.
      4. Bring him the passes that fail the new bar, judged, for one ruling
         on dequeuing them. Nothing is dequeued on the session's own reading.

      **Related:** `430/010` (quality is never traded for budget; this item
      decides whether a review is owed, never how one runs), `440/010` (what
      "the right model for the job" costs), and the review planner's ranking
      gate, where step 3 would live.
      **Review:** the doctrine change in step 2 is self-authored doctrine, so
      it earns a cold pass under rule 4 when written, queued by its author.
      ✅ **Step 1 done 2026-11-25 (session f8dd3843, `atelier-31`, queue run; a read-only
      Opus worker sampled, this session checked).** All 42 `⏳` passes in `160` (40 open, 2
      closed), classified against today's text: **35 meet it** (3 only by the letter: 1470,
      1750, 1760, corrections that count as "doctrine text" because it has no minimum size),
      **4 fail it** (985, 987, 991, 992: loud-failing fixes to reviewed, tested tools, all
      one run's batch of 2026-11-03), **3 the text cannot decide** (1530, 1550, 1730).
      Grounds stated on 29, none on 13; all 4 fails gave *reach* ("every child runs it"),
      which is not one of the text's triggers. He ordered 3 himself (989, 1600, 1820).
      Beside them, `160` holds 70 `🎯` and 18 `🛑` pointers, about 130 owed passes in all.
      **Answer to his question: both, mostly weak doctrine.** The text has no materiality
      floor for "doctrine text"; rule 3 (any validator, gate, template or skill is doctrine
      by function) with rule 4 (self-authored doctrine always earns a cold spawn) overrides
      the self-verifying exemption for every tool, so a session following the text queues;
      one pointer per landing means passes scale with commits, not risk (`ccclose` 8,
      `ccfleet` 4, `board.py` 4, `floor.py` 3; one run queued 14 in a day); nothing says when
      a re-check chain stops; declining needs written grounds and queuing needs none.
      The per-pass table, the patterns and a draft bar (three questions at queue time, a
      never-on-its-own list, one open pass per subject, rule 3 deciding who rules, not
      whether a pass is owed) are in
      [`../../sessions/2026-11-25-1249-work-run-fable-bar-and-fixes.md`](../../sessions/2026-11-25-1249-work-run-fable-bar-and-fixes.md),
      § *Annex*. **Steps 2–4 stay open.** Step 2 changes rule 4 itself, so the draft goes
      to him first (one ask at the run's close), then is written, its cold pass queued,
      and step 4's dequeue list follows from it.
