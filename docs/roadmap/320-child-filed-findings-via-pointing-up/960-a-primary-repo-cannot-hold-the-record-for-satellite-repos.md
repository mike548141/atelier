- [ ] 🔎 **Hand-up: the house assumes every repo keeps its own record, so one primary
      repo cannot hold the board, session log and changelog for a group of satellite
      repos** `[M][doctrine][tools]`. Handed up by a private child on 2026-11-28, under
      `PROPAGATION.md` § *Pointing up*. The principal asked for it, verbatim: *"this is
      worth extending atelier to govern it properly"*.
    - **What the principal wants.** In a group of coupled repos, one repo is the
      **primary**. It holds the record for the whole group: board, session logs,
      changelog, decisions. The other repos are **satellites**. They keep only what a
      machine or a deploy needs (code, config, their own tests and hooks), and exist
      as separate repos only where that earns its keep. His example: a deploy tool
      that clones one repo of compose files keeps that repo separate, so its token
      reads nothing else. Code stays split by trust domain; the record is joined.
    - **Two use cases he named, by class:**
      1. **An operator's infrastructure group.** A primary plus five satellites,
         one of them public, each with its own board and session log today (the largest has
         about 350 board files and 170 session logs). Work spans the repos most days,
         and facts have sat stranded between two of them for weeks.
      2. **A long-running client engagement.** His words, with the names taken out:
         *"Breaking something like [a long-running client project] into its own repo
         with [the engagement repo] as the primary may make sense over time because
         the project is long running ([years]) and has multiple workstreams with
         different scopes, and work packages within those steams"*. Here the
         satellite may be big enough to want its own board, with the primary holding
         the cross-cutting view. So the model may need both shapes: **record held by
         the primary**, and **primary over satellites that keep their own record**.
         Which one each case wants is open.
    - **What the house says today** (read at `origin/main` 2026-11-28):
      - `docs/build/REPO-STANDARD.md` gives every repo its own `roadmap/`,
        `ROADMAP.md`, `sessions/` and `CHANGELOG.md`.
      - `CONCURRENCY.md` § *Work lands in the repo it changes*: a finder queues into
        **the target repo's own roadmap**; the estate root's board is only the
        fallback for a target with no queue. A satellite with no board by design is
        neither case.
      - The `board` floor check, the session close, `sizescan` and the fleet sweep's
        conformance checks all assume the board and log are in the repo being
        checked.
      - `390/010` (answered 2026-11-09): atelier does not model subject-cluster
        relationships; one generic line points at the estate root's registry. 🤔 This
        filing **revisits that answer** for one relationship, *where a repo's record
        lives*, on the principal's word above.
      - ✅ **The principal's pick, 2026-11-27 ~22:44 UTC** (question device, the
        filing session; options and recommendation were the session's), verbatim:
        *"Reopen 390/010"*. The option he picked read: *"atelier models repo
        groups by subject in general (membership, primary, credential users,
        dependencies), with record location as one part. One coherent model, but
        about 2–3× the design work and a bigger cold review, so it lands later. It
        reverses an answer you approved on 2026-11-09."* He picked it over the
        recommended narrow option (record location only, `390/010` standing).
        So this item is one part of a reopened `390/010`. Applying the reopen
        there (its state line and its section) is atelier's own session's work:
        a hand-up touches only its own item.
    - **What the house would need** (candidates, none chosen):
      - One declared setting in a satellite naming its primary (and which records
        live there), read by every check above, so a satellite with no board is
        conformant rather than red.
      - The *work lands* rule restated for the pair: the change lands in the
        satellite, through its own hooks; the record lands in the primary.
      - A way for a primary's items to name their satellite, so a session working
        the satellite still finds its queue fast (a tag, a section per satellite, or
        a filtered view from `board.py`).
      - A migration path for satellites that already have records: open items move,
        history stays in place or moves. Bulk moves of a record store are a floor
        stop either way.
      - The visibility rule for a public satellite with a private primary: the
        record moving to the private side shrinks what is published; commit
        messages stay public.
      - Cold reviews are unaffected: records are already on `REVIEW.md` rule 2's
        barred list.
    - **Same root as `320/660`** (grouping children into folders): both assume a
      flat set of equal, self-contained children. Worth designing together.
