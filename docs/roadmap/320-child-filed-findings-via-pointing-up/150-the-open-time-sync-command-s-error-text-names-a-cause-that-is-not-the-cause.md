- [ ] 🤔 **CANDIDATE HOUSE RULE — the prescribed open-time sync command can fail
      spuriously under concurrency, and its error text names a cause that is
      not the cause** — handed up over the cross-session channel, 2026-09-12
      (`PROPAGATION.md` § *Pointing up*, filing shape 2 — the sending session
      declined to file directly and stayed unnamed by design). Class only: no
      repo, host or child filename appears below, and none was offered.
  - [ ] 🔑 **The class.** `git pull --rebase --autostash` — `CONCURRENCY.md`
        line 179, the first thing the floor tells every session to run at
        open — died with `fatal: Cannot rebase onto multiple branches`, then
        succeeded on a later invocation with nothing changed in between. The
        message reads as a config problem. It arrives at session open, the
        point of least context, and the obvious response — go fix the repo's
        rebase/remote config — is wrong.
  - [ ] ✅ **The config is NOT the cause, and this is the load-bearing half.**
        One remote, one fetch refspec, one `branch.<name>.merge`, no `pull.*`
        config, repo in sync at the time of failure. **Measured independently
        by two sessions**, not asserted once and repeated.
  - [ ] 🤔 **The cause offered is a hypothesis, stated as one, and not yet
        proven.** `pull` rebases onto `FETCH_HEAD`, a single file every
        concurrent `fetch` rewrites; two sessions fetching at once could
        plausibly leave it holding more than one ref, which is the state that
        produces this exact message. **No `FETCH_HEAD` capture was taken at
        the moment of failure** — that single read is what would settle it.
        Anyone who hits this should `cat .git/FETCH_HEAD` *before* retrying,
        not after.
  - [ ] 🤔 **Retry-as-remedy is not proven either.** One observed instance
        cleared on a later attempt. That is *a* retry working, not evidence
        that it reliably clears — recorded this way on purpose, because
        "known-flaky, just retry" is how a session ends up looping silently
        against a real failure instead of stopping.
  - [ ] 📎 **Checked against this repository's own file before being called a
        gap**, per § *Pointing up*'s own requirement. `CONCURRENCY.md`
        §§ 78–99 already names two shared surfaces that `git status` never
        flags as "stop" — the shared index (81–93) and shared repository
        *state*, e.g. a rebase in progress (94–99). This finding is neither:
        it is not caught mid-rebase and it is not an index collision. **If the
        hypothesis holds, it would sit beside those two as a third and
        milder case**, distinguished from both by its own worst feature —
        the error text doesn't just fail to warn, it actively names a wrong
        cause, inviting a repair to settings that are already correct.
  - [ ] 🤔 **Why this reads as the house's rather than one child's:** every
        repo in the estate is a sibling checkout opened by parallel sessions
        running this same open-time pull (`CONCURRENCY.md`'s own worktree
        model). If the `FETCH_HEAD` hypothesis holds, the exposure is uniform
        across children, not local to one — but that inference itself has not
        been tested against a second repo's layout, so it is carried as a
        "why it looks structural," not as a second finding.
  - [ ] 📎 **Not claimed, so the item is not read as more than it is.** No
        position taken on wording, on whether `CONCURRENCY.md` should gain a
        third blind-spot bullet or a standalone note, or on what the fix
        would be even if the hypothesis is confirmed (serialising fetches?
        reading `FETCH_HEAD` before trusting the error? something else). No
        parent file edited here. Nothing in either sending session's tree is
        named, quoted or linked — there isn't one to link, by the sender's own
        choice.
  - [ ] ⏳ **Status.** Per § *The route*, a hand-up over the channel is not
        *filed* until an atelier session lands it (`PROPAGATION.md`, filing
        shape 2's own caveat) — this item is that landing. Owed next: a
        `FETCH_HEAD` capture at the moment of a live failure, from whichever
        session hits this again, before the hypothesis can move past 🤔.
