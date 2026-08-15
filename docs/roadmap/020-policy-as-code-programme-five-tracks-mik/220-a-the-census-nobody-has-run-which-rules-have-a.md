- [ ] 🎯 **(a) The census nobody has run: which rules have a forcing function,
      and which do not.** ADR 0008 made enforcement *propagate*; it never
      established what proportion of doctrine is enforced at all. No one has
      enumerated the rules and asked of each: what happens if this is broken,
      and what would see it break? **Scope is *all* doctrine, on
      `REVIEW.md` rule 3's function-not-file-type definition** — any rule
      governing future agent behaviour, whether it sits in prose, an ADR, a
      schema, a validator, a CI gate, or a template or skill that stamps
      behaviour into other repos. `docs/method/` is where the census starts,
      not where it stops. The section above names three forcing-function
      gaps *by hand*, which is the giveaway. The
      recurring finding — a rule nothing enforces gets broken by the agent
      writing about that rule — is on its fifth recorded instance (C5's own
      near-miss, 2026-08-09). Output is a per-rule state: **enforced ·
      directive-only · unenforceable, accepted** — the last reasoned and
      dated to the `GUARDS.md` bar. An unenforceable rule is a lawful
      outcome; an *unexamined* one is the defect.
