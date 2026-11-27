- [ ] 🔎 **A hand-up from a private child carried the filer's messaging name, which spells
      the private repo's name, into this public repo, and no floor scanner flagged it**
      `[S][guard]`. Found 2026-11-27 by session 9c5fa72c (`atelier-fa`) landing the
      `210/670` filing, which landed with the name replaced by "a child queue run".
      `PROPAGATION.md` § *The route* rule 2 says the reporter never names itself on any
      surface the filing creates. The PR's floor run was green, and the local hook's
      `leakscan` was clean on the item too: the user-local term list does not carry that
      repo's name, and `namescan` reads only a branch and a title, not an item's text.
      The filing's own commits were pushed before landing, so the name was published
      there; a push cannot be retracted. **Owed:** decide where the guard sits:
      (a) the user-local term list gains every private repo's name (and the session
      messaging names built from them), so `leakscan` catches it on every plane that
      holds the list; or (b) `namescan` reads added item text from a child's filing
      for the estate's private repo names, read from the estate's own list. (a) is the
      smaller change; whether the term list is the right home is the owner's of that
      list. Class only here, by rule 2.
