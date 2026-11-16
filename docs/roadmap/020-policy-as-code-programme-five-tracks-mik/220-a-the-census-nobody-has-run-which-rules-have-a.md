- [~] **(a) The census nobody has run: which rules have a forcing function,
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
      - 🔀 Tidied 2026-11-16 (C0499, verified high; Mike approved 2026-11-16):
        not an ask of Mike. A census of which rules have a forcing function
        (lines 1-4) is agent work in atelier; the item asks him nothing. Nothing
        above was changed; the original text is as it was. To revert: delete
        this line (its commit is listed in
        `docs/sessions/2026-11-16-0534-asks-tidy-applied.md`).
      - 🔀 2026-11-16 (C0499): removed the 🎯 marker from this item's first line,
        because this ask is not Mike's (tidy line above). Original: that line
        began `- [ ] 🎯`. To revert: git revert this repo's marker commit (listed
        in `docs/sessions/2026-11-16-0534-asks-tidy-applied.md`).
      🔒 CLAIMED 2026-11-16T11:40Z (claimed 2026-11-16-1140, wt: qr-78ca-census) by queue-run
      session 78ca9153 (Opus 5.5, principal-opened).
