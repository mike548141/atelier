- [ ] 🎯 **Rule-4 cold pass queued: `ccclose --identifiers` credits on
      evidence (`160/960`), and a peer's edits stop only a claim of the same
      item (`010/160`, `160/260`).** The authoring session (a
      principal-opened Opus 5.5 queue run, session 722ac2e2, 2026-11-09, in
      its ruling round, which dispatched the Sonnet worker that wrote them)
      queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code and doctrine cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `instruments/ccclose`, its tests, design note,
      man page and README entry, `docs/method/RECORD.md`,
      `docs/method/CONCURRENCY.md`, `tools/board.py` (docstring),
      `tools/README.md`, `docs/roadmap/README.md`, the board-store ADR's
      amendment, `CHANGELOG.md` — the commits that close `160/960` and
      `010/160`, on `main`, 2026-11-09.
      *Questions worth the pass's time:* whether a commit can be credited on
      evidence the session did not produce; whether two sessions can still
      both claim one item under the narrower stop.
      *Intent record:* the items named above.
      *Brief:*
      `docs/reviews/2026-11-09-0153-identifiers-on-evidence-and-the-same-item-stop-cold.md`,
      written 2026-11-09 UTC by session `d16dc612`, a headless Opus 5.5
      brief-writer started by `74f2b8cd` (neither may run it); its
      held-back sibling holds one pointer block, 2 questions and 1 fact.
      *Size:* large. The pass waits for his approval of Fable.
      🔒 CLAIMED 2026-11-16T07:10Z by headless orchestrator session (Opus 5.5, a rule-4 off-tier
      orchestrator: it holds the context partition, forms no finding and writes no
      severity), started by drain session 1e053526 (Opus 5.5) under the principal's API-credit
      drain order of 2026-11-16, verbatim: *"I want to use things other than my weekly budget
      to clear as many fable reviews as possible like using fable drain. I thought we could
      start by using up all the API credits I have."* That order is the approval of Fable this
      item waits for. Reviewer: a fresh Fable 5.1 session, tier checked at selection; not
      started or instructed by any barred session (722ac2e2 and its workers, d16dc612,
      74f2b8cd). Sibling held out of the tree until act 1 is committed.
      ✅ PASS RAN 2026-11-16 UTC (Fable 5.1 reviewer; act 1 `004a9bec`, fold below it).
      Verdict: **PASS-WITH-FINDINGS — 0 MAJOR · 2 MODERATE · 3 minor · 4 note** (`IDS1`–`IDS9`).
      No standing MAJOR; no false credit found, and the claim rule holds mechanically. Review,
      sibling and review log:
      `docs/reviews/2026-11-09-0153-identifiers-on-evidence-and-the-same-item-stop-cold.md`.
      🎯 *Owed to the principal (rule 3; every finding is his, nothing applied).* One bulk
      question, the reviewer's counsel as the recommendation:
      - `IDS1` MODERATE: `ccclose`'s new command parse is quadratic over long heredocs (47 s
        at 20,000 lines; real heredocs today are at most 141 lines). Recommend: the
        one-character-class fix (`[ \t]*` for `\s*`) plus a timed 5,000-line test.
      - `IDS2` MODERATE: a `git -C "$W"` or `cd "$W"` commit is never credited, so the house's
        own idiom shows most of a session's commits as unconfirmed, and no surface says so.
        Recommend: resolve the variable as `-F` paths already are; until then name the limit
        on all four surfaces.
      - `IDS3`–`IDS5` minor: the quoted-command claim is stronger than the code; changelog and
        ADR disagree on which records were corrected; CF3 now rewrites a stranger's dirty
        index while the backstop bullet and child template say never. Recommend: fix each as
        the review's counsel says.
      - `IDS6` note, a question for him: a peer's staged line on another item still stops a
        claim (forced by the shared index; committing the whole index would absorb the
        peer's work). Recommend: confirm this one residual stop sits under his "Stop only
        for the same item" answer.
      - `IDS7`–`IDS9` note: branch 2's order of steps is implicit; "one spelling" wobbles in
        `board.py`'s docstring; a session-id commit trailer was never weighed. Recommend: fix
        the first two in passing; weigh the trailer in the design note.
      *Routing:* one atelier session takes the approved `ccclose` fixes (`IDS1`–`IDS3`,
      `IDS9`) and the doctrine wording (`IDS4`–`IDS8`); `IDS5`'s fix also touches the stamped
      child template.
