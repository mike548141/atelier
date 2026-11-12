- [x] 🎯 **Cross-repo session coordination — Mike commissioned, 2026-09-12.**
      His words: *"Find ways to improve how parallel sessions to converse,
      coordinate, share"* and, separately, *"Find better ways to track,
      claim, and coordinate work planned and in progress."*
  - [ ] 🔑 **What exists today is per-repo.** `CONCURRENCY.md` § *The channel*
        (peer messaging, holdings, farewells) and § *Claiming work* (the
        board's tri-state, `[~]`/`⏳` claims committed to `main`) both work
        well **inside one repo's checkout**. Neither says anything about a
        session in one repo knowing what a session in a *different* repo is
        doing, holding, or has claimed.
  - [ ] 🔎 **`310/020` already names half of this from the doctrine-currency
        angle** — "nothing enumerates what the estate owes the house," i.e.
        no instrument answers *which children are behind on doctrine*. This
        item is the sibling question for **work**, not doctrine: no
        instrument answers *what is any session, anywhere in the estate,
        currently claimed on or holding right now* — a session opening
        `shed` has no way to learn a sibling session is mid-flight in
        `docker-heap` even where the two could usefully coordinate (shared
        credential, shared host, shared subject).
  - [ ] 🤔 **Not scoped to a mechanism here.** Candidates worth considering,
        none chosen: a per-estate index a session can poll or subscribe to;
        widening the existing cross-session channel to be estate-wide rather
        than per-repo; or leaving repos independent and only building the
        narrower `310/020` doctrine-currency instrument first, since it is
        smaller and already filed. The choice, and whether this needs new
        machinery versus a convention layered on what exists, is atelier's
        (or Mike's) to make, not assumed here.
  - [ ] 📎 Filed as a new item rather than folded into `360/010` because that
        item is about naming a *launch* before widening its announcement — a
        narrower, already-scoped concern than general cross-repo awareness.
  - [ ] 💬 **Mike's answer, 2026-11-09 (to options queue run 722ac2e2 offered; an answer,
        not a ruling):** *"Build a machine-wide view"* (not the recommended option): a machine-wide view of live work across repos; the one-line open-PR check is in `CLAUDE.md` step 6 already. Not yet designed or built.
  - [x] ✅ **DONE 2026-11-09**, queue run d0ca5d24: `instruments/cclive`, built to
        `instruments/cclive.design.md`, with its own test file and man page. A
        read-only view across every repo under the estate parent: `[~]` claims
        at the newest integration ref, worktrees with last-commit ages, sessions
        and agents with a recently written transcript, and the load average. It
        states its roots, what it skipped and its limits on every run.
        **Stayed out:** open PRs (network; step 6 of the onramp already covers
        them), dirty state, process inspection, and any shared index or channel
        widening: this adds no new shared state. Cold pass not run here; the
        orchestrator queues it.
  - [x] 💬 **`cclive` at session open, 2026-11-12 UTC.** 💬 Mike's pick, 2026-11-12 UTC,
        from options session d0ca5d24 offered: "Every session at open (Recommended)". An
        answer, not a ruling.
        Written into `CONCURRENCY.md`, the `session-onramp` skill, the `CLAUDE.md`
        template and atelier's own `CLAUDE.md`. Children pick up the skill line with
        the plugin and the template line when their onramp is next restamped.
