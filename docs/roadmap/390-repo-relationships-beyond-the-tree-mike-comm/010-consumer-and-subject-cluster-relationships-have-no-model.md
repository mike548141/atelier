- [ ] 🎯 **No doctrine models a repo-to-repo relationship other than
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
