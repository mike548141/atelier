- [ ] 🎯 **§ *Pointing up* only names atelier as a parent — Mike commissioned,
      2026-09-12.** His words: *"Find better ways for sessions working on
      child repos to feed back ideas, problems or whatever to 'parent' repos
      like atelier to consider and act upon. Similarly a child repo of shed
      wanting to add a credential or something back to shed."*
  - [ ] 🔑 **Checked against `PROPAGATION.md` before filing, per § *Pointing
        up*'s own requirement.** § *Who is a child* defines child-of-**atelier**
        only; every worked example in § *The route*, § *Report without harming
        the parent* and board section `320` is a child handing a doctrine
        problem up to atelier specifically. Nothing generalises the pattern to
        a different parent with a different subject matter.
  - [ ] 🔎 **`shed` is the concrete case that shows the gap is real, not
        hypothetical.** `shed` is itself described elsewhere as the estate's
        private root and carries its own registry (e.g. `shed/registry/`) and
        its own children/consumers — a repo that mints a new credential, or
        wants one registered, has a genuine parent to report to, and that
        parent is not atelier. Today that repo has no route: § *Pointing up*'s
        machinery (file in the parent's board, three filing shapes, "carry the
        class never the child's specifics", the channel's hand-up law) is
        written for a **public** parent receiving a **doctrine** problem —
        `shed` is a **private** parent receiving an **asset-registration**
        request, and neither of those two differences is addressed by copying
        the existing route verbatim.
  - [ ] 🤔 **What would need to change, not decided here:** whether "carry the
        class, never specifics" still applies when the parent itself is
        private and can safely receive specifics (it likely relaxes); whether
        "a board item under `docs/roadmap/`" is still the filing surface, or
        whether a private parent wants a different one (a registry PR, an
        issue, a request file); whether the three filing shapes (direct write,
        channel hand-up, hold-and-flag) still exhaust the reachable cases for
        a private parent the reporting session may not have write access to.
  - [ ] 📎 **Not claimed as identical to the existing route** — filed as a new
        item under this section, not folded into `310/100` ("the route
        assumes a reachable parent and a channel"), because that item is
        about reachability of *atelier specifically*, while this one is about
        the route's shape being atelier-specific in the first place.
