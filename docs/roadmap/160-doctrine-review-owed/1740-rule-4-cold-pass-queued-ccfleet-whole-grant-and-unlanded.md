- [ ] ⏳ **Rule-4 cold pass queued: `ccfleet` launches with the config as
      the whole grant, and reads a clean end that leaves unlanded work as
      UNLANDED (`210/560`).** The change narrows what an unattended session
      may do and decides when a claim is released, both silent-failure
      surfaces, so it earns its own pass (the item says so). The authoring
      session (608d8123, Opus 5.5, a principal-opened queue run, 2026-11-23
      UTC, whose worker wrote the change) queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `instruments/ccfleet`,
      `instruments/test_ccfleet.py`, `instruments/man/ccfleet.1`,
      `instruments/ccfleet.example.json`, `instruments/README.md`,
      `skills/review-drain/SKILL.md`: the commit that closes `210/560`, on
      `main`; widened 2026-11-23 by the commit that moves the review-log
      name to SHA-256 (`115/500` item 5; `instruments/ccfleet`'s
      `review_log` and `pass_log`, and their test).
      *Intent record:*
      [`../210-instruments-open-features/560-ccfleet-cannot-see-inherited-permissions-and-a-kept-worktree-loses-its-claim.md`](../210-instruments-open-features/560-ccfleet-cannot-see-inherited-permissions-and-a-kept-worktree-loses-its-claim.md).
      *What to test hardest:* every path by which a launched session can
      still be granted more than the config says (repo settings, a kept
      hook whose script answers allow, managed settings, the text match
      that drops granting hooks); that no guard hook is lost; the UNLANDED
      verdict against a worktree whose work is pushed on a branch other
      than its own, and against an adopted `--in` worktree.
      *Approval:* none yet; owed to the principal before the pass runs.
      💬 **Answered 2026-11-23 ~19:20 UTC (session 608d8123, AskUserQuestion), his pick:** *"Next drain (Recommended)"*:
      this pass and the other three of run 608d8123 (`160/1740`–`1770`)
      wait for his next weekly drain.
