- [x] **Rename `/atelier:queue-run` to `/atelier:work-run`.** His words,
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
      **No alias.** One was built, then removed before landing: a peer session
      had his pick for old command names the same day, *"Nothing"* (no
      forwarder, no signpost; `450/020`, recorded on `180/210`), so
      `/atelier:queue-run` simply stops existing.
      **Meets `450/020`.** That item (an idea awaiting his confirmation)
      moves every command to *subject, space, action*; its table's
      `queue-run` → `queue run` row now reads `work-run` → `work run`, with
      `work plan` for `180/240`. This rename lands first because he asked for
      it now; the form change is that item's.
      **The name is `/atelier:work run`, his words, 2026-11-24, verbatim:**
      *"no its /atelier:work run"*. `work-run` is the interim skill until
      `450/020`'s overhaul (one skill per subject, the action as its
      argument) lands; that build renames it, and no record should call
      `work-run` the final name.
