- [ ] **A run waits for a quiet machine, skips what waits on him, asks
      at its start or end, and chips at the asks backlog.** Commissioned
      2026-11-24 ~01:25Z, session b95c0d98, his words, verbatim: *"In the
      sessions last night I was using /atelier:queue-run and then adding a
      message as copied below / Consider if this should be built into the
      standard prompt in session-open-prompt or some other way."* The message
      he had added mid-run to session 608d8123 (2026-11-23), verbatim: *"I dont
      want you to get stuck on work you have previously attempted to do but got
      stuck/blocked by needing information or decisions from me. Its fine if
      circumsstances have changed (like a review was run) so there is fresh work
      to do, or ways to do it."* · *"It could be wise to pause for 3 or 4 hours
      until the other sessions work is quieter and then you do your work? Check
      each hour to see if its the right time to start"*.
      His reasons, verbatim:
      - *"I start a new session and it tries to do work that I've told it in a
        recent past session something like I am undecided or not right now. So
        rather than doing other work in the queue it keeps looping on the same
        work and questions etc which is frustrating for me and a waste of time
        and tokens and effort. Equally if a piece of work was previously blocked
        on a review or waiting an answer from me and is now not blocked then its
        great to finish it off."*
      - *"I often run parallel work in the same repos and in different repos.
        And sometimes the load it too high so I was asking it to look at the
        load and if its too high then dont start work. This allows the first
        session(s) so work hard with multiple sub agents etc and not flood the
        computer or cause software failures. My intention with this was not to
        constantly adjust the amount of work whilst inflight like we do with the
        review drain, but to simply not start a sessions work until the other
        sessions have eased off. But not require me to wait around to start it
        manually."*
      - *"If I'm not there I don't want it stuck mid session on questions etc so
        where possible either ask questions right at the start of the session or
        once all the work is completed. We also need to get better at using the
        atelier doctrine when you ask me questions, and ensuring large amounts of
        questions dont build up and not get answered. The latter is hard as it
        takes up my time that I dont have much of and there are a lot of
        questions, but we don't want to assume or give up quality so its a
        matter of chipping away at the questions continuously and keeping on top
        of it."*
      **What exists.** `COMMUNICATION.md` § *When to ask* already sorts a
      question by what it blocks and parks branch-blocking ones to the end
      (`420/010`); the prompt's *Working with me* still says "Ask me ... mid-turn
      or between turns", which pulls the other way. `ccopen` reads the repo,
      not the machine; `cclive` prints the load but judges nothing. `ccfleet`'s
      launch gate is the house's one grounded load number (`max_load` 2 × cores
      on the 1- and 5-minute averages). The board marks 🎯 waiting but has no
      mark for *he was asked and said not now*, so the next session cannot tell
      a parked question from a never-asked one. At filing atelier's board held
      107 open items with 🎯 on the state line (first said as 212, a miscount
      of the index table, corrected at build); last night's triage found 43 of 102 open items waiting
      on his ruling.
      **Evidence it works by hand.** 608d8123 waited two hourly checks (load
      20–24 on 12 cores from other repos' runs), started at load 5, and its
      triage skipped the 🎯 items (`docs/sessions/2026-11-23-1354-*`).
      **His answers, 2026-11-24 (picks from options offered, not rulings):**
      *"All four, as drafted (Recommended)"* and, for the backlog, *"3 oldest
      per session (Recommended)"*. Then, in his own words, verbatim: *"It
      should also ask the questions from the current session"*: the close
      round puts this session's questions first, then the three oldest.
      **Correction at build:** the load threshold is not `ccfleet`'s gate.
      That gate (2 × cores, 1- and 5-minute averages) decides whether a drain
      adds one more pass; last night's 20–24 on 12 cores sat under it, yet
      was the case he wanted to wait out. The start gate is the core count on
      the 5- and 15-minute averages: the point where runnable work exceeds the
      CPUs, a principle and not a measurement, overridable by
      `CCOPEN_MAX_LOAD`.
      **Shape built:**
      1. **The prompt** (his text, changed only on his say-so): run-gating
         questions at the start, the rest at the end; skip what waits on him
         unless something changed; wait for a quiet machine, checking hourly,
         up to four hours; at the end, put the oldest few open asks to him so
         the backlog shrinks every session.
      2. **`ccopen`** gains a machine-load read (busy at the core count, on
         the 5- and 15-minute averages) and a waiting-on-him read: how many
         are parked, and which changed since they were parked.
      3. **The board** gains a parked mark: his answer and date on the item's
         state line, so a parked item is skipped and not re-asked until its
         file or the item it waits on changes.
      4. **`ccclose`** lists the oldest open asks for the end-of-session round.
      ✅ **Built 2026-11-24** by session b95c0d98: the prompt and doctrine
      edits, the legend's PARKED line, and the reads (a Sonnet worker:
      `ccopen` reads 8 and 9, `ccclose` check 16). First real run: load 3.75
      on 12 cores, quiet; 107 open asks waiting, 0 parked, the three oldest
      listed. Cold pass queued as `160/1780`.
      **Owed:** a sweep that marks answers he already gave as "not now" or
      "hold" with a `💤 PARKED` line, so the read sees them; until then every
      open ask reads as never asked. The ages: atelier's item files were added
      by a history replay, so most asks read about 100 days and tie, broken by
      board order.
      **Re-check interval, his words, 2026-11-24, verbatim:** *"I am now
      thinking check ever 20 mins or 30 mins. Either way it should be a
      variable so its easily changeable"* · *"I want long enough that the
      trend has clearly changed rather than a momentary dip, and time for CPU
      and memory cooling etc to take effect"*. Built the same day:
      `CCOPEN_RECHECK_MIN`, default 30 (two turns of the 15-minute average),
      and quiet now needs both the 5- and 15-minute averages under the
      threshold, so a dip is still busy. Rides the `160/1780` pass.
      **Carry on now, his words, 2026-11-24, verbatim:** *"Also I want you to
      carry on with design and build in a fresh session, not wait until the
      fable review is done"*. So the owed sweep (and `180/240`, if he
      confirms) runs in a fresh session he opens, without waiting for
      `160/1780`.
      ~~The parked mark is withdrawn~~ (a misreading, corrected below). His answer, 2026-11-24, verbatim
      (to "which work should the fresh session build: the parked sweep, work
      plan, or both?"): *"You can do the work plan, but that should be done
      at the same time as the other /atelier work I've described in the
      parallel session in this repo. Its just one of the commands being
      changed. I don't want you marking work as "parked" at all, you will
      infere it incorrectly as you have many timtes already in past
      sessions"*. So no sweep, and no session writes `💤 PARKED`; the legend
      and `COMMUNICATION.md` no longer describe it. Work plan moves to
      `450/020`'s build.
      **Owed (a fresh session, design and build, not waiting for
      `160/1780`):** `ccopen` read 9 and `ccclose` check 16 still parse a
      PARKED line nobody will write. Redesign without inference, or remove:
      e.g. list waiting items whose file changed since his last recorded
      answer (a 💬 or ⚖️ line, which records his words and is not a session's
      reading of them), and nothing about what the answer meant. The first
      oldest-asks round also found two of three 🎯 marks stale, so a
      verification of the open 🎯 marks (does each still need him?) would
      shrink the backlog before he spends time on it; it must state its
      evidence per item, as `020/020` and `020/140` now do.
      **The oldest-asks round, as built, puts work that is not a decision.**
      Its first run listed three 🎯 items: two were settled long ago and one
      (`020/040`) was settled by his own stated model, and putting that one
      drew, verbatim, *"Your question does not follow doctrine rules for
      asking questions"*. Owed with the redesign above: every listed ask is
      read and sorted by `COMMUNICATION.md`'s first rule (a record, a
      decision, or find out first) before any reaches him, and only
      decisions are put.
      🛑 **Correction, his words, 2026-11-24, verbatim:** *"You have
      mis-interpreted me AGAIN and in a dangerous way. I can decide some work
      is parked and therefore we need a status for parked work on the board
      and I will do that through a session. What I said no to was you
      scanning the boards and arbitarily deciding that when I said something
      like "not now" in the past means permanently parked as you are prone to
      doing"*. So the `💤 PARKED` status is restored to the legend and
      `COMMUNICATION.md`, written only when he says to park an item, in his
      words; no session infers a park, and no sweep of past answers runs.
      `ccopen` read 9 and `ccclose` check 16 stand as built; the "redesign or
      remove" owed line above is void. What stays owed: the oldest-asks
      round sorts each ask (record, decision, find out first) before any
      reaches him.
      **One old question, from this repo, his words, 2026-11-24, verbatim:**
      *"We need to change this down to just asking one old question, not 3.
      And it must be a question from the repo that the session is running in
      / working on"*. Built the same day: the prompt, `COMMUNICATION.md`, and
      `ccclose` check 16 (shows the one oldest; the board it reads is the
      checkout's own, so another repo's asks cannot appear).
