- [ ] 🎯 **PROPOSAL for `GUARDS.md` — *strict where we author, forgiving where
      we read*: the rule that tells an author WHICH of the two to pick**
      `[S][docs]` — filed from a private child 2026-08-18 via § *Pointing up*.
      **Mike's ruling, not an agent's call:** this changes the fourth
      requirement he ruled on 2026-08-17, so it is recorded here as a proposal
      and deliberately not written into doctrine by the session that received
      it.
      **The gap it names.** `GUARDS.md` says every guard declares whether it
      **makes the failure cheap** or **forbids the act**, and that both are
      legitimate — the defect being not saying which. What it does not say is
      **how to choose**, which is the question an author actually faces at the
      moment of building one.
      **The proposed answer, in the filer's own framing:** *the side of the
      boundary the writer is on decides it.* At a construction site inside your
      own code — where you control the writer — **forbid**, because there is no
      recovery to build: a wrong label is already in the reader's hands before
      anyone could notice. At a read site, where the writer is a future build or
      another producer you do not control, **make the failure cheap** and carry
      the unrecognised thing through unlabelled.
      **What it buys, and this is the part worth weighing.** It explains why one
      subsystem can legitimately give *opposite* answers to the same validation
      question without contradicting itself — a classifier that raises on an
      unknown kind at its construction site while its grouping counterpart files
      an unknown kind as `unclassified`. Without the rule that reads as an
      inconsistency, **and a future session would be right to try to "fix" one of
      them** — which is the concrete cost of leaving it unwritten.
      **Provenance worth keeping:** two parallel child sessions arrived at this
      independently on 2026-08-17, which is the >2-instance shape that earns
      promotion rather than a one-off. It has not been checked against the house
      guard board here — whether existing atelier guards obey it, and which
      would fail it, is unmeasured and is part of what a ruling would need.
      **Relationship to `310`:** this is a *child-originated doctrine proposal*,
      the case § *Pointing up* step 1 describes. It arrived as a proposal rather
      than as locally-authored rule text, which is the route working.
