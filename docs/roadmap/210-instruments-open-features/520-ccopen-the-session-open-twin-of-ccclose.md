- [~] **`ccopen`: the session-open twin of `ccclose`, so the prompt's opening
      checks run as code.** The principal, 2026-11-22, verbatim: *"Also do
      the same for anything else that we can build as deterministic code and
      hook into sessions instead of using the prompt. But be mindful in all of
      these changes that I only use the prompt when I think its useful too,
      there are some sessions where I purposely dont want to give some of the
      commands that are in the template prompt"*. So `ccopen` is a command the
      prompt runs, never a hook: a session he opens without the prompt never
      runs it. Read-only (a `git fetch` aside, as `ccclose` check 14), fresh
      from the repo and host, one verdict line. What it reads, each line
      grounded in a prompt line it replaces:
      - **Which kind of session this is** ("Anchor to doctrine first"'s three
        branches): atelier itself, a child (floor block and pin), a repo with
        no doctrine (and which file is its queue), or no repo.
      - **Sync** (`CLAUDE.md` read order step 1): dirty files, ahead/behind
        the remote; a dirty tree is proof someone else is editing.
      - **Live work** ("Assume another session may be live"): `cclive`'s read
        for this repo: sessions, claims, worktrees.
      - **An interrupted predecessor** ("If a session gets interrupted"): last
        commit with no session file after it, `[~]` claims no live session
        holds, linked worktrees and branches left, stashes.
      - **Hand-up PRs open** (read order step 6).
      - **Pin currency** ("If a peer or parent repo … has moved on"):
        `pins.py` for a child, as check 14 reads it.
      - **The newest session files** (read order step 4), named.
      Verdict: ready to start, or recover first (with what). Design doc, man
      page, tests with a fixture per read, as `ccclose` has. A rule-4 cold
      pass is owed on the build.
      *(claimed 2026-11-22 UTC, session 12a41aa2, wt: atelier-qr-12a4-ccopen)*
