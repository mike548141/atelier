- [ ] 🎯 **`shed` and client-data repos rely on an "always confirm" floor rule,
      not an enforced control.** His words: *"We need better ways to protect
      data like that in shed, and client data repo's. In particular to make
      sure they are never published publicly or shared to unauthorised
      people."*
  - [ ] 🔑 **What already exists, checked before filing.** `AUTONOMY.md`
        § *Always confirm* names "making a private thing public" (visibility
        flip, adding a collaborator, external distribution) as a standing
        confirm-first floor, verifiable against `gh repo view --json
        visibility`. `DATA-PROTECTION.md` § *Other people's data is not yours
        to risk* directs: hold the minimum, never widen exposure, never move
        it somewhere less protected. Both are **directive**, not enforced —
        they bind by an agent choosing to follow them, not by a mechanism
        that would stop the action if it didn't.
  - [ ] 🔎 **This is the same class as the policy-as-code programme
        (`020/`, approved 2026-07-27), applied to one high-stakes case.**
        That programme's whole premise, in his own words recorded there, is
        *"all doctrine to be enforced i.e. policy as code... also directive"*
        — repo visibility and unauthorized sharing of `shed`/client-data repos
        is arguably the highest-consequence instance of exactly that gap,
        since the failure (a private repo made public, or shared to the
        wrong person) is not reversible the way a bad commit is.
  - [ ] 🤔 **Not scoped to a mechanism.** Candidates, none chosen: a
        pre-push/pre-share check that reads a repo's declared visibility
        class and refuses an action that would widen it without an explicit
        override; a GitHub org policy or branch/repo setting outside agent
        control entirely (the strongest form, since it doesn't rely on the
        agent at all); or a periodic audit that lists every repo's actual
        visibility and collaborator list against what it's declared to be,
        catching drift rather than preventing it. The three differ sharply in
        strength and cost, and the choice is not made here.
  - [ ] 📎 **Distinguished from `030/050` and `030/040`** (structural leakscan
        reds, secret findings in service config, both open) — those are about
        *content already exposed*; this is about the *repo-visibility and
        sharing action itself*, upstream of content.
