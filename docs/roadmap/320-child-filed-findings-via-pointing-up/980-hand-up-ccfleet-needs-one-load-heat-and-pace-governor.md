- [ ] **Hand-up: `ccfleet`'s two big runs, the review drain and the fleet sweep, have no load, heat or pace governor; the old drain kit's gates did not move with the drain.** Reported 2026-11-28 by a private child's queue run, class only <!-- wrapscan:allow: a state line carries the whole state in one line so the index reads true -->

      A hand-up from a private child, under `PROPAGATION.md` § *Pointing up*.
      One finding, from a cold pass. Measured by reading; no incident yet.

      **What was found.** The weekly review drain moved to
      `/atelier:review run` on `ccfleet` on 2026-11-26. The child's earlier
      drain kit carried a load gate, a memory and disk gate, a heat gate
      (the machine's thermal state), and a pace planner that tapers the
      running count so a budget reaches its target shortly before it resets
      while every started review still finishes. None of that moved with the
      drain: `ccfleet` runs a fixed ceiling. A cold pass on the child's drain
      ranking gate rated this MAJOR. For the next drain the child runs its
      old planner read-only as an adviser to `ccfleet`'s ceiling, a stopgap
      the principal accepted while saying, verbatim: *"this seems like a big
      hole in the design and logic that we need to fix properly."*

      **The scope the principal set, verbatim, the same day:** *"Both of
      those are big operations that need things like heat and load
      (CPU/NPU/GPU, memory, storage, network etc) monitoring and pace
      management to scale up and down"*. "Both" are `/atelier:review run`
      and `/atelier:fleet sweep`, which both launch their headless sessions
      through `ccfleet`.

      **Asked:** one governor in `ccfleet`, used by both runs, that
      (a) measures load and heat across CPU, NPU, GPU, memory, storage and
      network; (b) scales the running count up and down from those
      readings, never stopping a session it started; and (c) for the drain,
      paces the running count to a budget target taken from the instance's
      config (the targets and rulings are the child's and stay there).
      Prior art: the old kit's gates and its pace planner with a replay
      test, which the child can hand over on request; a cold pass listed
      open defects in that planner, so it is a starting point, not the
      design. Neither designed nor ruled; the design is the house's call.

      Related: `210/470` (the ccfleet and skill fixes) and `320/970` (the
      kill rule; a heavy run's load is also how a machine gets pushed into
      failure).
