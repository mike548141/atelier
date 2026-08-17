- [x] 🎯 **The posture section, and the fourth requirement it puts on every
      guard** `[M][docs]` — **DELIVERED 2026-08-17** on wt: `posture-0817`
      (claim `e4be7f7`); rule-4 cold pass queued at `040`. Mike commissioned and
      ruled it 2026-08-17.
      **What landed.** `PRINCIPLES.md` **§10 Posture — strength is what you are
      free to do**, carrying his four cases verbatim and four rules: that
      recoverability is what licenses action; that **a control making you
      reluctant to act is failing even while nothing has gone wrong**; that an
      exposure should be shaped to tell them nothing; and that a restore path is
      a claim, so an unexercised one is an assumption in a mechanism's clothes.
      A situation test — **prevention, or cheap failure?** — beside Gate sizing,
      which asks how strict a control should be where this asks the prior
      question. And in `GUARDS.md`, the **fourth requirement** beside his own
      *narrow, noisy, reasoned*: every guard declares whether it makes the
      failure cheap or forbids the act, both legitimate, **not declaring being
      the defect**.
      🔑 **It closes an asymmetry already filed against this estate:** the `why`
      on every registry entry is printed and compared to nothing
      ([`115/130`](../115-guardrail-architecture-mike-commissioned/130-a-guard-reports-whether-its-rule-fired-at-all.md)),
      because there was no standard behind it — the estate demanded a reason for
      *weakening* a guard and none for *building* one. The declaration is that
      standard, from the build side.
      **Two limits written into the rule itself**, so it is not read as a
      licence: a test arriving after the work is grounds to declare, never to
      unwire a working gate on the author's own judgement; and "forbids the act"
      is not a failure grade — much of the floor is deliberately prevention, and
      the requirement makes that visible rather than condemning it.
      **Not done here, deliberately:** the pass over the open guard board
      (`020`), and the detection-and-restore census (`030`, which runs in the
      private estate root).
