- [ ] 🎯 **Decide the cheap rules first — naming and announcing — and treat
      anything stronger as a separate question that needs its own evidence.**
  - [ ] **Rule 1, and it is nearly free: name what you launch on a shared host.**
        A container, background process or scheduled job started on a machine a
        peer can see carries an owner marker in its name. 🔎 **The proof is in the
        commissioning incident:** `media-split-Photos` and `elegant_williams` were
        the *same tool* doing the *same job*, and a peer's census attributed the
        first correctly and reported the second as "neither is mine". The only
        difference was that one had been named and the other was left to docker's
        random-name generator.
    - [ ] 🔑 **The marker must say WHOSE, not merely be distinctive.** The peer
          that hit this put it best: *"a random name is indistinguishable from an
          orphan."* `elegant_williams` is perfectly unique and tells a reader
          nothing, so an unowned long-running job reads as **litter** — and the
          tidy-minded response to litter is to clear it away. The failure mode
          being guarded against is not a confused peer; it is a **helpful** one
          killing a multi-hour job. A distinctive name does not fix that. An
          owner-bearing one does.
    - [ ] Worth deciding what the marker actually is — a name prefix is enough for
          docker, but a bare `sh` process on a host has nowhere obvious to carry
          one. Do not over-specify; a convention that covers containers and
          long-running scripts is most of the value.
  - [ ] **Rule 2: the open-of-session announcement covers non-git claims.**
        Today it is a file set. It should also name the **hosts** being worked on,
        any **long-running job** in flight and roughly how long it has left, any
        **shared remote file** the session rewrites, and any **live service** whose
        restart would hurt. Same principle as the file set — a claim says what,
        never which files — so this stays short.
  - [ ] **Rule 3, and this is the one that needs thought: a long job's claim must
        outlive its session.** `CONCURRENCY.md` already says *"a message reserves
        nothing; only a pushed artefact does"*, which is correct and is not
        actually about git — a claim has to live in the shared medium, durably,
        where a peer will look. Off-repo that medium is the host. A marker file
        beside the work is the obvious form.
    - [ ] ⚠️ **Stale markers are the failure mode**, and they are worse than no
          marker because they teach people to ignore markers. Whatever is chosen
          needs an answer for the session that dies holding one — a timestamp a
          peer can judge, a pid to check, or a documented way to break it.
  - [ ] 🛑 **Do NOT design a locking protocol.** The house already carries a lesson
        about guards that produce more noise than signal, and a distributed lock
        for a household estate would be over-built and quietly abandoned the first
        time it was inconvenient. Decide rules 1 and 2, ship them, and revisit only
        on evidence that they were not enough.
  - [ ] 🔎 **One surface deserves its own line because its failure is disguised:
        a rate-limited API.** Two sessions probing the same login inside the same
        window produce `Invalid credentials` and a lockout, which reads as a
        *credential* problem, not a *concurrency* problem — and sends whoever hits
        it hunting in entirely the wrong place. It happened in the commissioning
        incident, twice over, for two different reasons.
