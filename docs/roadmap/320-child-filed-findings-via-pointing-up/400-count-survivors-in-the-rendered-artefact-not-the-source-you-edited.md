- [ ] 🔎 **CANDIDATE HOUSE RULE — verify a figure correction in the RENDERED
      artefact, not in the source you edited: a partially applied correction
      reads worse than an unapplied one** `[S][doctrine]` — offered by a
      private child 2026-09-20 over the peer channel, as possibly relevant to
      atelier rather than as a defect here. Filed on that basis, with the
      atelier-side applicability assessed below rather than assumed.

      ## The child's instance

      A figure correction was landed across the sources of a generated
      document pack. A lane doing the work **correctly declined to edit two
      files outside its assigned set** — the right call under work-locality —
      and nothing afterwards closed the gap. The rendered output then stated
      **both the old and the new figure**, in one artefact, at once. It was
      found by reading the rendered pack after landing, not by any check.

      🔑 **Why that is worse than not correcting at all.** An uncorrected
      figure is consistently wrong and a reader can discount it wholesale. A
      *half*-corrected one is internally contradictory, so a reader cannot
      tell which number to trust and the artefact impeaches itself. The child's
      stated check: **count survivors in the rendered artefact, not in the
      source you edited.**

      ## Does it reach atelier? Partly, and not where it first appears to

      **Not via the generated index.** `docs/ROADMAP.md` is regenerated whole
      from `docs/roadmap/` on every change, so a correction in an item file
      propagates completely or not at all — there is no partial-render state
      for `board.py` to leave behind. That is the obvious candidate and it is
      **not** the exposure.

      **Yes via figures repeated across surfaces**, which atelier does
      constantly and has a recorded history of getting wrong. A measurement
      typically lands in an item file, a session record, and a commit message,
      and nothing regenerates any of those from a common source — they are
      three hand-written copies of one number. The house already knows this
      class: the fleet-rollout item (`010/030`) carries its own warning that
      its figures *"have been wrong in both directions before"* and names three
      it got wrong low, `faves` alone out by 4,421 lines, alongside a rule not
      to adjust such a figure by intuition but to sweep. That is the same
      defect the child describes, arrived at from the other direction — and
      atelier's version has no rendered artefact to read, which makes it
      *harder* to catch rather than easier.

      **A live instance from the session that filed this.** The E9 measurement
      (`020/160`) — 333 findings before, 49 after — was written into an item
      file, a session record and a commit message in three separate acts. Had
      any one of them been corrected later, nothing would have found the other
      two.

      ## The ask

      Decide whether this earns a line, and where. Candidates, not a design:
      **(a)** a rule that a figure appearing on more than one surface is
      corrected by sweep and the sweep is stated, which is `010/030`'s local
      practice promoted to doctrine; **(b)** a check — grep the corrected
      figure's *old* value across the records after any correction, which is
      mechanisable and cheap and would have caught the child's case and every
      atelier instance; **(c)** nothing, on the grounds that
      `roadmap-figures-wrong-both-ways` is already known and restating it
      louder is the failure mode `rule-grammar-before-enforcement` warns about.

      ⚠️ **Not established:** how often atelier actually half-corrects a figure.
      The class is known and recorded; the *rate* is not, and (b)'s value
      depends on it. One live instance was created by this very session and
      nobody has swept the records for others.
