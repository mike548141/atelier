- [x] **`ccclose` takes over the close checks the session-open prompt still
      asks for in words.** The principal, 2026-11-22, verbatim: *"I want you to
      look at everything in the lastest version of the prompt in
      session-open-prompt.md and look at what would be more effectively built
      into ccclose rather than being in the prompt"*. The read (session
      `12a41aa2`), line by line against `ccclose.design.md` § 7, 9 and 15:
      - **Already built, so the prompt's words only repeat it:** the standard
        close (commit, push, session log, board, claims, worktrees, branches,
        PRs, floor, review owed: checks 1 to 9 and 11) and the identifiers
        block (`--identifiers`, a separate run).
      - **Every ask, not only close-shaped ones.** "review all of my prompts
        … both at the turn and mid-turn, and make sure you have done
        everything I asked in full". § 9 lists only prompts that match close
        keywords: on the session that wrote this item it printed "none found"
        over three real asks. List every turn and mid-turn prompt with its
        cctranscript ref; the session answers each done, queued (item id) or
        not done.
      - **Every question put to the principal.** "Review your replies in each
        turn to capture open actions, questions, decisions you asked of me"
        and "questions to ask me later in a way that ensures future sessions
        will find them". Nothing reads the session's own side today. List each
        `AskUserQuestion` with its answer or none, and each reply line that
        carries a 🎯 or ⏳ call-out; an unanswered one is ⚠️ until a board item
        written in the window names it.
      - **Other repos the session touched.** "everything you've touched".
        The identifiers block prints "Other repos: fill in by hand". Read the
        repos from the transcript (cwd, `cd`, `git -C`, worktree paths) and
        run the repo checks on each.
      - **Other live sessions.** "any other live sessions have what they need
        from you". List what `cclive` lists for the same repos, as ⚠️ to
        answer, never a fail.
      - **The identifiers block in the default run**, so the close is one
        command.
      - **Launched work still running** is already its own item, `210/460`;
        build the two together or in that order.
      **Stays in the prompt** (judgement, which a tool cannot read): the
      summary by topic, the plain-language walk-through of each open
      decision, and whether the learnings reached the record (§ 11).
      Once built, the prompt's close section can shrink to "run ccclose until
      it says ready, answer what it lists, then summarise and walk me
      through": his text, so only on his words. A rule-4 cold pass is owed on
      the build (Fable, on his approval).
      *(claimed 2026-11-22-0248 UTC, session 12a41aa2, wt: atelier-ccclose-460-480; the principal: "Build both now (Recommended)")*
      **The prompt edit, the principal mid-build, verbatim:** *"Whatever gets
      built into ccclose should be remvoed from the prompt but I want to
      understand that before you change the prompt template"*. So once the
      build lands: show him each prompt line that goes, what in ccclose now
      does its job, and the resulting text; change the file only after he has
      it in hand and says go.
      **Built 2026-11-22** (session 12a41aa2; its Sonnet worker): every
      prompt, turn and mid-turn, listed with its ref (`[close]` tags the old
      keyword hits); every `AskUserQuestion` with its answer, and the
      session's 🎯/⏳ lines; other repos touched, each run through the repo
      checks; other live sessions in those repos. The identifiers block
      already ended the default run (`210/300`). Cold pass queued: `160/1710`.
      **Owed, and why this stays open:** the prompt edit, on the terms above.
      The lines ccclose now answers, for the walk-through: the standard-close
      list in *Ending the session*; "review all of my prompts and your
      replies … everything I asked in full"; "Review your replies in each turn
      to capture open actions, questions, decisions"; "Run ccclose and make
      sure everything is ready"; and, since `210/490`, "Open by printing this
      session's ID". What stays: the summary by topic, the plain-language
      walk-through, whether the learnings reached the record.
      **Prompt edited 2026-11-22**, after the walk-through above was put to
      him line by line with the new text in full; his pick, verbatim: *"Make
      the change (Recommended)"*. The close section is replaced as shown, and
      the session-ID line at the top goes (`210/490` does its job).
