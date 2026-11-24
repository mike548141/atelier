- [ ] ⏳ **Rule-4 cold pass queued: a run's start gates, the parked mark,
      the asks backlog, and the rename to `work-run` (`180/220`, `180/230`).**
      The principal's session-open prompt changed, two doctrine files gained
      rules, the board gained a mark, and `ccopen` and `ccclose` gained reads
      every session runs, so it earns its own pass. The authoring session
      (b95c0d98, Opus 5.5, principal-opened, 2026-11-24 UTC, whose Sonnet
      worker wrote the instrument change) queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* doctrine and code cold pass, per `method/REVIEW.md`
      rule 4.
      *Delta, scoped to paths:* `docs/method/session-open/session-open-prompt.md`,
      `docs/method/COMMUNICATION.md` § *When to ask*,
      `docs/method/CONCURRENCY.md` § *Orchestrated queue runs* (the two
      bullets on when to ask and the quiet-machine start),
      `docs/roadmap/README.md` (the `💤 PARKED` legend), `instruments/ccopen`,
      `instruments/ccclose`, their tests, design notes and man pages,
      `skills/work-run/` (no alias for the old name), and the rename's
      sweep: the commits citing `180/220` and `180/230`, on `main`, since
      `69dbeb3b`.
      *Intent record:*
      [`../180-orchestrated-queue-runs-from-hand-carrie/220-a-run-waits-for-a-quiet-machine-and-skips-what-waits-on-him.md`](../180-orchestrated-queue-runs-from-hand-carrie/220-a-run-waits-for-a-quiet-machine-and-skips-what-waits-on-him.md),
      [`../180-orchestrated-queue-runs-from-hand-carrie/230-rename-queue-run-to-work-run.md`](../180-orchestrated-queue-runs-from-hand-carrie/230-rename-queue-run-to-work-run.md).
      *What to test hardest:* that each prompt edit says what his picks and
      his own words on the items approved, and no more; that the load
      threshold is a principle and not a measurement, and that the gate
      blocks only the start; that "changed since parked" cannot miss an
      answer he gave (a park woken late is a re-ask; a park never woken is
      lost work); that the oldest-asks check can never stop a close; that
      the rename left no live surface naming the old command and touched no
      record.
      *Approval:* none yet; owed to the principal before the pass runs.
      💬 **Answered 2026-11-24 ~02:20 UTC (session b95c0d98, AskUserQuestion), his pick:** *"Next weekly drain (Recommended)"*:
      this pass waits for his next weekly drain.
      **Widened 2026-11-24 (session 523be3be, `180/250`):** the oldest-asks
      round this pass covers was withdrawn on his words the same day
      (`85da9586`: the prompt's close step, `COMMUNICATION.md` § *When to
      ask*, `ccclose` check 16 removed, `ccopen` and its man page). Review
      the round as it now stands: withdrawn.
