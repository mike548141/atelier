- [ ] **No doctrine models a repo-to-repo relationship other than
      doctrine-parent/child.**
  - [ ] 🔑 **Consumer-of-asset.** `REACH.md` § *The credential boundary*
        already distinguishes a "provisioning registry" and "per-consumer
        minted API tokens" as a concept, but ties it to no actual registry —
        a repo that consumes a credential `shed` provisions has no recorded
        relationship anywhere in doctrine. If `shed` rotates or revokes
        something, nothing enumerates who else that touches.
  - [ ] 🔑 **Subject/domain clustering.** Repos group by real-world purpose
        that doctrine inheritance doesn't capture — his own examples: an
        estate-infrastructure group ("shed, docker-heap, homenetwork") and a
        home-automation group, for which he named candidates tentatively
        (*"can't remember there names but hac, numen, kahuranga etc"*) —
        carried here exactly as hedged, not verified or corrected. Whether
        this second group actually shares any doctrine dependency with the
        first, or is genuinely independent, is unknown from atelier's side.
  - [ ] 🤔 **Not scoped to a mechanism.** Candidates, none chosen: a small
        registry file (repo, relationship-type, related-repo) living
        somewhere in the estate (`shed`'s registry pattern is the closest
        existing precedent, per `shed/registry/credentials.json` referenced
        in past session records); or leaving this as prose in each repo's own
        onramp; or deciding it isn't atelier's problem at all since atelier's
        remit is doctrine, not estate topology. That last option is worth
        taking seriously — this item does not assume atelier is where this
        belongs, only that nowhere currently holds it.
  - [ ] 📎 Distinguished from `310/120` (filed the same day): that item is
        about the **pointing-up route** having only one parent shape; this
        item is about relationships that are **not parent/child at all**.
  - [ ] 💬 **Mike's answer, 2026-11-09 (to options queue run 722ac2e2 offered,
        after reading a one-line summary of each of twenty; an answer, not a
        ruling):** *"Approve all 20"* — the recommendation on this item
        stands approved: atelier does not model consumer or subject-cluster relationships; one generic line points at the estate root's registry.
  - [x] ✅ **DONE 2026-11-09 — APPLIED** by queue run 722ac2e2 (a Sonnet
        worker, read by the orchestrator before landing): one generic line in `PROPAGATION.md`. Cold pass
        queued as `160/1160`.
  - [ ] 🔁 **REOPENED 2026-11-27 on the principal's pick**, put by a private child's
        filing session in the question device (options and recommendation were that
        session's), verbatim: *"Reopen 390/010"*. The option he picked read: *"atelier
        models repo groups by subject in general (membership, primary, credential users,
        dependencies), with record location as one part. One coherent model, but about
        2–3× the design work and a bigger cold review, so it lands later. It reverses an
        answer you approved on 2026-11-09."* He picked it over the recommended narrow
        option (record location only). The 2026-11-09 answer above is superseded, kept as
        history; the one generic `PROPAGATION.md` line stays until the model replaces it.
        The record-location part is `320/960`; same root as `320/660`. Owed: a design,
        then its cold pass. Applied by session a2097e54 (`atelier-b2`) on landing `320/960`.
