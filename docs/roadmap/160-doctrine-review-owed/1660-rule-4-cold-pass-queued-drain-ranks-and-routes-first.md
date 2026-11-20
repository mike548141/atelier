- [ ] ⏳ **Rule-4 cold pass queued: a drain ranks and routes the whole queue
      before any pass starts — `ccfleet`'s required `queue.ranked` gate and
      the `review-drain` skill's § *Rank and route the whole queue first*.**
      Written by session 64f984ac (Opus 5.5, principal-opened, 2026-11-20
      UTC) on the principal's direct ask, which queues this and does not take
      it or brief it. **Needs a brief.**
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code and doctrine cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `instruments/ccfleet` (`drain`: the
      `queue.ranked` call and refusal; the queue-interface doc),
      `instruments/test_ccfleet.py`, `instruments/ccfleet.example.json`,
      `instruments/man/ccfleet.1`, `skills/review-drain/SKILL.md`: the commit
      that adds this item, on `main`. It lands after `160/1450`'s brief was
      written; that pass's delta does not cover it.
      *What to test hardest:* can any drain path pick a pass before `ranked`
      returns 0 (dry runs, a resume, a restarted driver); is a config with no
      `ranked` refused everywhere it should be and nowhere else (the `run`
      and `drive` subcommands do not need it); does the skill's routing rule
      ("unsure means the dearer route") hold against the principal's rule
      that review quality is never traded for price; is the quote and the
      paraphrase public-safe.
