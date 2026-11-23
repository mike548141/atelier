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
      - 2026-11-16, slice 1 done (queue run 78ca): `RECORD.md`, `REVIEW.md`
        and `CONCURRENCY.md` censused rule by rule in
        `docs/method/census/2026-11-16-1142-record-review-concurrency.md`.
        158 rules: 19 enforced (11 of them partial), 133 directive-only (35
        with a breach visible in the diff), 6 unenforceable and accepted. The
        file ranks five diff-visible guard candidates for `020/240`. The
        `115/110` map has no file of its own, so `00-APEX.md` and
        `AUTONOMY.md` are owed a written census too. Remaining in
        `docs/method/`: `ACCESS`, `COMMUNICATION`, `CONVENTIONS`,
        `DATA-PROTECTION`, `DOCUMENTATION`, `ECONOMICS`, `EVIDENCE`,
        `GLOSSARY`, `GUARDS`, `MECHANISMS`, `PRINCIPLES`, `PROPAGATION`,
        `REACH`, `SECRETS`, `SIGNING`, `STORAGE`, `TOOLBOX` and
        `docs/method/session-open/`; then the doctrine outside
        `docs/method/` (build docs, ADRs, skills, commands, templates,
        validators). One doctrine defect
        found and not fixed here: `EVIDENCE.md` §17 says nothing inspects a
        session's shell commands, and `tools/modelguard.py` does (census row
        CON21); it is owed its own board item.
      - 2026-11-16, slice 2 done (queue run 78ca): `00-APEX.md`,
        `AUTONOMY.md`, `GUARDS.md` and `PROPAGATION.md` censused rule by rule
        in `docs/method/census/2026-11-16-1204-apex-autonomy-guards-propagation.md`,
        the floor region counted once, in PROPAGATION. 129 rules: 27 enforced
        (19 of them partial), 101 directive-only (36 with a breach visible in
        the diff), 1 unenforceable and accepted. Running total over both
        slices: 287 rules, 46 enforced, 234 directive-only, 7 accepted. The
        `115/110` headline is checked against the tree: APEX still has no
        check; the always-confirm floor has two of eleven stops enforced. The
        file ranks five more diff-visible guard candidates for `020/240`, and
        names three doctrine defects, each owed its own board item and not
        fixed here: visibility declared in two homes with nothing joining them;
        the floor block's stop list differing from `AUTONOMY.md` § *Always
        confirm*; and `PROPAGATION.md`'s parent-enforces-more rule against
        atelier's deliberately atelier-only CI steps. Remaining in
        `docs/method/`: `ACCESS`, `COMMUNICATION`, `CONVENTIONS`,
        `DATA-PROTECTION`, `DOCUMENTATION`, `ECONOMICS`, `EVIDENCE`,
        `GLOSSARY`, `MECHANISMS`, `PRINCIPLES`, `REACH`, `SECRETS`, `SIGNING`,
        `STORAGE`, `TOOLBOX` and `docs/method/session-open/`; then the doctrine
        outside `docs/method/`.
      - 2026-11-16, slice 3 done (queue run 78ca): `EVIDENCE.md`,
        `ECONOMICS.md`, `COMMUNICATION.md` and `DATA-PROTECTION.md` censused
        rule by rule, as they stand after the same day's changes, in
        `docs/method/census/2026-11-16-1220-evidence-economics-communication-data.md`.
        94 rules: 9 enforced (all partial), 81 directive-only (20 with a
        breach visible in the diff), 4 unenforceable and accepted. Running
        total over three slices: 381 rules, 55 enforced, 315 directive-only,
        11 accepted; EVIDENCE §17 is counted twice (EVI24 and `CON21`), so 380
        distinct. The file ranks five more diff-visible guard candidates for
        `020/240`, led by a path filter on the floor workflow, and names a
        before-plane pair (one question per ask; no reference ids in the ask
        box) for `115/100`. Doctrine defects named and not fixed: §17's ground
        (already `115/410`); §19's "pointer still owed" that has landed; §7's
        banned words against `datescan`'s deliberate exclusions; ECONOMICS
        naming the model roster it says stays person-local; DATA-PROTECTION's
        write-then-rename rule with no home. Remaining in `docs/method/`:
        `ACCESS`, `CONVENTIONS`, `DOCUMENTATION`, `GLOSSARY`, `MECHANISMS`,
        `PRINCIPLES`, `REACH`, `SECRETS`, `SIGNING`, `STORAGE`, `TOOLBOX` and
        `docs/method/session-open/`; then the doctrine outside `docs/method/`.
      🔒 CLAIMED 2026-11-16T11:40Z (claimed 2026-11-16-1140, wt: qr-78ca-census) by queue-run
      session 78ca9153 (Opus 5.5, principal-opened).
      🔒 CLAIMED 2026-11-16T11:55Z (claimed 2026-11-16-1155, wt: qr-78ca-census2) by queue-run
      session 78ca9153 (Opus 5.5, principal-opened).
      🔒 CLAIMED 2026-11-16T12:13Z (claimed 2026-11-16-1213, wt: qr-78ca-census3) by queue-run
      session 78ca9153 (Opus 5.5, principal-opened).
      *(claimed 2026-11-23 UTC, session 608d8123, wt: atelier-qr-608d-census4)*
