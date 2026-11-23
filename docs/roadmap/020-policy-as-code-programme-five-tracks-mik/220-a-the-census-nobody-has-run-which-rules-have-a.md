- [ ] **(a) The census nobody has run: which rules have a forcing function,
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
      - 2026-11-23, slice 4 done (queue run 608d8123): `ACCESS.md`,
        `CONVENTIONS.md`, `DOCUMENTATION.md`, `GLOSSARY.md`, `MECHANISMS.md`
        and `PRINCIPLES.md` censused rule by rule in
        `docs/method/census/2026-11-23-1559-access-conventions-documentation-glossary-mechanisms-principles.md`.
        106 rules: 5 enforced (all partial), 99 directive-only (60 with a
        breach visible in the diff, 17 of them in a shape a scanner could
        read), 2 unenforceable and accepted. Running total over four slices:
        487 rules (486 distinct), 60 enforced, 414 directive-only, 13
        accepted. Five more guard candidates ranked for `020/240`, led by a
        weak-hash constructor check (PRI25; `instruments/ccfleet`'s SHA-1
        log suffix breaches PRINCIPLES §5 today). Doctrine defects named and
        not fixed: DOCUMENTATION principle 6 binds "as a review question"
        nothing asks; no `--json` payload carries the version field
        "versioned like an API" implies; PRINCIPLES' opening and precedence
        still say §1–9 with §10–11 present; GLOSSARY's "stated bridge" points
        at a §7 that covers one sense only. Remaining in `docs/method/`:
        `REACH`, `SECRETS`, `SIGNING`, `STORAGE`, `TOOLBOX` and
        `docs/method/session-open/`; then the doctrine outside
        `docs/method/`.
      - 2026-11-23, slice 5 done (same run): `REACH.md`, `SECRETS.md`,
        `SIGNING.md`, `STORAGE.md`, `TOOLBOX.md` and
        `docs/method/session-open/` in
        `docs/method/census/2026-11-23-1651-reach-secrets-signing-storage-toolbox-session-open.md`.
        73 rules: 19 enforced (14 partial), 54 directive-only (12 with a
        breach visible in the diff), none accepted. Running total over five
        slices: 560 rules (559 distinct), 79 enforced, 468 directive-only, 13
        accepted. **`docs/method/` is now censused once, end to end.** Not
        re-swept: 16 commits have touched slice 1–3 files since; `AUT17`
        wants re-grading (partly enforced by a session hook now); slice 4's
        `PRI8` is wrong for `instruments/browser-fetch` (ADR 0006's
        addendum). Guard candidates for `020/240`, led by a check over
        `allowed_signers` itself and a TOOLBOX-table completeness check
        (8 of 13 instruments unlisted). Defects filed as `115/510`; the
        signing finding as `115/520`. **Remaining:** the doctrine outside
        `docs/method/`: `docs/build/` and its templates; root `CLAUDE.md`,
        `SECURITY.md`, `README.md`; `docs/decisions/`; `skills/` and
        `commands/`; the validators' own stated rules; and
        `docs/PERSONAL-DATA.md`.
      - 2026-11-23, slice 6 done (same run): `docs/build/` (README,
        `REPO-BOUNDARY.md`, `REPO-STANDARD.md`, the 24 template files) and
        the root `CLAUDE.md`, `SECURITY.md` and `README.md`, in
        `docs/method/census/2026-11-23-1730-build-boundary-standard-templates-root-files.md`.
        68 rules: 25 enforced (19 partial), 43 directive-only (19 with a
        breach visible in the diff), none accepted. Running total over six
        slices: 628 rules (627 distinct), 104 enforced, 511 directive-only,
        13 accepted. Guard candidates for `020/240`, led by workflow
        hygiene (SHA-pinned actions and a declared `permissions:` block:
        the `ci-python.yml` and `ci-static.yml` templates declare none, so
        a child seeded from them takes the default token permissions).
        Defects filed as `115/530`. **Remaining:** `docs/decisions/`;
        `skills/`, `commands/` and the plugin manifests; the validators'
        own stated rules; `docs/PERSONAL-DATA.md` and the index rules.
      - 2026-11-23, slice 7 done (same run): `docs/decisions/` (README,
        ADRs 0001–0008, twelve dated records), the six skills with their
        bundled prompts, the four commands, both plugin manifests and the
        menu skill, in
        `docs/method/census/2026-11-23-1813-decisions-skills-commands-plugin.md`.
        116 new rules (most skill text folds into earlier rows): 45
        enforced (34 partial), 71 directive-only (15 with a breach visible
        in the diff), none accepted. Running total over seven slices: 744
        rules (743 distinct), 149 enforced, 582 directive-only, 13
        accepted. Guard candidates for `020/240`, led by a CHANGELOG line
        required with any change to `skills/`, `commands/` or the plugin
        manifests (17 of the last 40 such commits have none). Defects
        filed as `115/540`. **Remaining:** the validators' own stated rules
        (the floor registry, scanner docstrings, `tools/README.md`,
        `instruments/README.md`, the `ccfleet` man page);
        `docs/PERSONAL-DATA.md`; atelier's `docs/roadmap/README.md` and
        `docs/reviews/README.md`.
      - 2026-11-23, slice 8 done (same run): `tools/floor.py`'s contract
        and its 21 registry entries, `tools/README.md`,
        `docs/PERSONAL-DATA.md` and `docs/roadmap/README.md`, with a
        census-wide summary, in
        `docs/method/census/2026-11-23-1836-validators-personal-data-roadmap-summary.md`.
        109 new rules: 99 enforced (36 partial), 9 directive-only, 1
        accepted. **Running total over eight slices: 853 rules (852
        distinct), 248 enforced (147 partial), 591 directive-only, 14
        accepted; 29.1% enforced, 20.8% without the validators' own
        rows.** 203 directive-only rules show their breach in the diff;
        the largest clusters: append-only records and their shape;
        authority, grants and allowances; landing companions (a change to
        a governed surface carries its companion line); workflow and
        registry hygiene. Defects filed as `115/550`. **Remaining:**
        slice 9, `instruments/README.md` and `instruments/man/ccfleet.1`;
        then a re-sweep of slices 1–3 and the re-grades later slices
        named (`AUT14`, half of `AUT15`, `AUT17`, `PRI8`), the
        `*.design.md` notes and the scanner docstrings.
