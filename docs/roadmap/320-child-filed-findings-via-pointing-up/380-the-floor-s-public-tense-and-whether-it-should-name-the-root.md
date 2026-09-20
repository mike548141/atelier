- [ ] 🎯 **The floor's visibility bullet reads as a one-time check, and may
      name the thing it exists to hide** — two wording proposals on the
      canonical floor region, filed from a private child 2026-09-20 via
      § *Pointing up*. Both concern the same bullet, both are the principal's
      to rule, and neither is a defect the child may fix in its own copy —
      the floor is copied verbatim (2026-09-19), so a child that disagrees
      with the wording has exactly one legitimate move, which is this one.

      **Provenance, because it bears on the weight.** The child carried a
      local reword of this bullet for several weeks. On 2026-08-17 Mike ruled
      **restore canonical *and* hand the wording up** rather than keep a fork.
      The restore landed that day; the hand-up did not, and was found still
      owed on 2026-09-20 during a pin bump. So these are not fresh opinions —
      they are wording a child actually preferred in practice, surrendered on
      a ruling, and owed upstream since.

  - [ ] **(i) "is public" is present tense, and the rule it guards is not.**
        The region reads *"If **this** repo is public, reference the root by
        local-path convention, never by name."* Proposed: *"is **ever made**
        public."*

        The present tense reads as a condition checked **once**, at the
        moment the sentence is read. But the class of repo the bullet most
        needs to bind is the **private-now, public-candidate** child: private
        today, written throughout as if it may go public, precisely so that
        the flip is never blocked by embedded content. For that repo the
        present-tense test returns *false* on every read right up until the
        day it returns true — at which point the content it was meant to keep
        out is already committed, and history is not rewritten here. The rule
        needs to bind to the repo's whole future, not its current state.

        **Not merely hypothetical:** the filing child is exactly this class,
        and its own onramp already states the stricter rule locally — *write
        every file as if it may go public, so that flip is never blocked*.
        The child is obeying a rule the canonical floor does not quite state.

  - [ ] **(ii) Should the region name the estate root by local-path
        convention at all?** The bullet permits referring to the root *"by
        local-path convention, never by name"*. The child's local copy spelled
        that convention out concretely — the permitted **form**, but the path
        it names is also the root's **name**, which is the reconnaissance the
        bullet exists to prevent. A rule whose compliant example discloses the
        thing it protects is a rule with a hole in its illustration.

        The question for the principal is whether canonical should say so
        explicitly — i.e. that the local-path convention is permitted *in the
        abstract* but that spelling the actual path in a public-candidate
        repo defeats it — or whether that is over-reading and the current
        wording is sufficient. **Stated as a question, not a proposed fix:**
        the child does not know which way this should fall, and the tightening
        has a real cost (a rule that forbids naming the path makes the root
        harder to point at for every legitimate reader).

      **What the child did *not* do, stated so it need not be asked.** It did
      not keep the local wording, it did not narrow the floor, and it has not
      written either proposal into its own copy — the region in that repo is
      byte-identical to canonical with placeholder fills only, verified by
      construction on 2026-09-20. Consideration and remediation are atelier's;
      the reporting child stops at this report.
