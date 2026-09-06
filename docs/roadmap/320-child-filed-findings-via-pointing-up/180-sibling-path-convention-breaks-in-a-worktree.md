- [ ] **REPORT — the `../<sibling>` path convention every child inherits
      resolves only from a main checkout, so it breaks in the worktree the
      concurrency doctrine tells sessions to take by default — and the house's
      own drift-check instruction is one of the things that breaks**
      `[M][tools]` — filed from a private child, 2026-09-06, via § *Pointing
      up*. Reproduced here in a clean probe before filing.

      ## Reproduced, with a control that was checked rather than assumed

      A throwaway repo with a **real sibling directory on disk**, one file
      containing one relative reference to a file in that sibling, committed;
      then `git worktree add` elsewhere and the same scanner run twice.

      - from the **main checkout** — clean, the reference resolves;
      - from the **worktree** — one finding, the reference "does not exist";
      - the two copies of the file are **byte-identical** (`diff` clean).

      Same tool, same content, opposite verdict. The control is stated because
      [`320/010`](010-pathscan-reds-on-three-shapes-that-are-never-real.md)
      records an invalid control on this exact scanner — a probe repo with no
      sibling present, where the red was the probe's artefact. Here the sibling
      exists and the main-checkout run proves it.

      The reporting child measured the same thing in its own tree first: the
      same scan returning **8** findings from its primary checkout and **10**
      from a worktree, 2026-08-23, the two extra both `../atelier/…`
      references. Re-confirmed 2026-09-06 at its current content — the same two
      references are still red from a worktree and clean from the primary
      checkout.

      ## The noise is the small half — an instruction fails silently

      The canonical floor region's **Source & drift** bullet tells every child
      to run `git -C "<atelier-path>" log --oneline <SHA>..HEAD` at session
      start, and § *The standard child doctrine block* names the
      sibling-relative form as the house shape for that path. Run from a
      worktree, that command **fails** instead of printing nothing. Verified in
      the reporting child, 2026-09-06:

      - from a worktree: exit 128, `fatal: cannot change to '../atelier': No
        such file or directory` — **on stderr, with stdout empty**;
      - from the primary checkout: exit 0, one commit line.

      🛑 **A session that reads empty stdout as "no output, no drift" concludes
      the house doctrine is current when it has not checked at all.** That is a
      silent pass in the one check that keeps an inlined floor honest — and the
      floor it is meant to keep honest is the one item
      [`160`](160-stampscan-cannot-stamp-across-a-repo-boundary.md) reports
      cannot be stamped. The two failures compound: nothing mechanically
      compares a child's floor to its source, and the manual check that would
      have caught it fails open in the environment doctrine prefers.

      ⚠️ **The ratio gets worse the more the house rule is followed.** Every
      session that takes a worktree — the default for write-heavy work — adds
      phantom findings to a warn-only check, which is how a check stops being
      read.

      ## It is a class, not a scanner bug

      Every tool that resolves a sibling path inherits it.
      [`210/110`](../210-instruments-open-features/110-pins-py-enumerates-cwd-relative-and-lies-from-a-worktree.md)
      is the same shape one level up — an instrument enumerating from the
      caller's working directory and reporting a wrong denominator from a
      worktree, silently. That item's fix is per-tool. This one asks for the
      convention, because a per-tool fix leaves the next tool to rediscover it.

      ## Options, unranked — the trade is real

      - **Resolve `../<sibling>` against the repo's MAIN worktree.**
        `git rev-parse --git-common-dir` names the main checkout's git
        directory from inside any worktree, so its parent is where the siblings
        live. One shared resolution helper fixes every tool at once. **But it
        fixes the scanners only** — the onramp command above is still broken
        unless it is re-keyed too, and that is the half that fails silently.
      - **Resolve siblings through a configured value** — a git config entry or
        environment variable, the way the floor already locates atelier's tools
        from anywhere. This mechanism exists and works from a worktree, and it
        is the only option that fixes the *instruction* as well as the checks.
      - **Place worktrees beside the primary checkout** rather than in a
        central worktrees directory, so the relative path keeps resolving.
        Cheap and needs no code, but it scatters worktrees through the estate
        root and it is a convention nothing enforces.

      Consideration and remediation are atelier's; the reporting child stops at
      this report.
