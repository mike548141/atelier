- [ ] 🔎 **Hand-up: the floor's *Estate resources* bullet covers facts —
      don't re-derive, don't copy down — and says nothing about the two
      behaviours the principal keeps having to ask for: drawing on the
      estate root's access before asking him to act at a provider, and
      writing the resulting change back to the root** `[S][doctrine]`.
      Filed from a private child (the estate root itself), 2026-10-11, under
      `PROPAGATION.md` § *Pointing up*. Class only.
      **Evidence, as the root records it.** The principal, 2026-09-07,
      verbatim apart from two names replaced: *"it has been a common
      recurring problem that I have to keep reminding repo's outside of
      [the estate root] (like [a child]) to use the access that [the estate
      root] repo holds to build what it needs to (rather than asking me to do
      the work manually) and to update or record changes into [the estate
      root] repo. That is an issue we need to do better on no matter which
      option I choose."* The same day a child session fixed two tunnel
      hostnames only after he said *"You do all of it, access is in the
      [estate root] repo for CF"* — then did it exactly right: minted a
      scoped child credential with the root's own tool and handed the
      registry entry back. Separately, nine registry facts from one child's
      deploy work sat unrecorded in the root for thirteen days, discoverable
      only from the child's tree. **The child that needed the reminder
      already carried the *Estate resources* bullet**, which is the
      measurement that the bullet as written does not produce the
      behaviour.
      **The gap.** The bullet says where estate facts live and forbids
      re-deriving or copying them. It does not say: (a) before a session
      asks the principal to do anything at a provider by hand, it checks the
      root for an existing credential or a mint path and uses it; (b) any
      change to estate state — a credential minted, a hostname added, a plan
      changed, a tool adopted — is recorded in the root, by the child's own
      commit where its lane allows, otherwise by a hand-over; and "asked the
      principal to do it manually" is a recorded exception with a reason,
      never the default.
      **What the root has done on its side** (no doctrine needed for it): it
      now carries a one-command, read-only discovery surface over its
      registry — per provider, what access exists, what it may do, where the
      secret lives (by name), and how to draw on it or mint a scoped child,
      ending with the write-back reminder. That makes (a) cheap to obey; it
      does not make it a rule.
      **Not proposed here:** the wording, and whether (a) and (b) belong in
      the floor bullet, in `REACH.md` (which governs which stores the agent
      may draw on, not *whether to check before asking*), or in
      `PROPAGATION.md`'s estate-root section. The ruling round decides.
      **Acceptance test, the principal's own:** he stops having to remind
      children. Count the reminders in his own turns before and after.
