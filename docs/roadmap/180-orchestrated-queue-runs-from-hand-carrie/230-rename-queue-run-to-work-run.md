- [ ] **Rename `/atelier:queue-run` to `/atelier:work-run`.** His words,
      2026-11-24, session b95c0d98, verbatim: *"Also I think we should rename
      the command from /atelier:queue-run to /atelier:work-run or something
      else. Maybe a reference to the board. But to my mind its saying to you
      "Lets do a bunch of work" and most of the time that work will be
      pre-planned things on the board"*. Offered three names, he picked
      *"/atelier:work-run (Recommended)"* (an answer, from options offered).
      **Done 2026-11-24:** the skill moved to `skills/work-run/`, its test to
      `tools/test_work_run_single_source.py`, and every live mention of the
      command (doctrine, the prompt, the plugin manifests, the menu, the
      README, the session-onramp skill, `quotescan`'s docstring) now says
      `work-run`. Records keep the old name: session logs, reviews, board
      items, the census and the changelog's history. The concept keeps its
      doctrine name, *orchestrated queue run*, so `CONCURRENCY.md`'s heading
      and every link to it stand.
      **Owed:** `skills/queue-run/SKILL.md` is an alias that points at the new
      command so his habit does not break. Remove it on or after 2026-12-24.
