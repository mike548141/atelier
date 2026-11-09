- [ ] ⏳ **Rule-4 cold pass queued: the commit-message plane: a `commit-msg` hook and `floor.py --plane msg` (`320/810`).** The authoring session (a
      principal-opened Opus 5.5 queue run, session d0ca5d24, 2026-11-09 UTC,
      which dispatched the worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, first of its kind, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `.githooks/commit-msg`, `tools/commit-msg.sample`, `tools/commitmsg.py`, the plane handling and refused flags in `tools/floor.py`, `skills/create-repo/SKILL.md`, `docs/method/GUARDS.md`, `tools/README.md` — the commit that adds the hook, on `main`.
      *Questions worth the pass's time:* whether the fail-closed hook can stop a commit for a reason a user cannot clear; whether a child can pass the boundary through `flags`.
      *Intent record:* `320/810`, `320/550`.
