# Cold pass — `nz-phone` passes a bracketed byte field, and secretscan's assigned-value rule takes two spellings

**Board:** `docs/roadmap/160-doctrine-review-owed/1370-rule-4-cold-pass-queued-phone-byte-field-rule-spelling.md`
**Status:** PASS RAN, acts 1 and 2 written 2026-11-15 UTC by a Fable 5.1 cold reviewer under a
rule-4 off-tier orchestrator (verdict below the divider: PASS-WITH-FINDINGS; after reconcile
0 MAJOR, 1 MODERATE, 4 minor, 5 note, YB1–YB10; YB9 and YB10 formed at reconcile). The deferred
sibling is folded in below the reconcile and its file removed (2026-11-15 UTC). Brief written
2026-11-14 UTC by a headless Opus 5.5 brief-writer (`cclive` lists it as session `c8eba849`), run
under the principal's weekly Fable drain order of 2026-11-16 NZDT.

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4 (the queue pointer's own words).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Size of this pass:** small: one commit, 6 files outside the board store, 236 lines added and 8
removed. `tools/leakscan.py` +33/−1, `tools/secretscan.py` +37/−5, 145 lines of new tests,
`tools/README.md` +3/−2, `CHANGELOG.md` +18.
**Why it earns a review:** both changes narrow what a publish-safety scanner blocks, in a public
repo whose scanners every child floats on at `main`. A guard that narrows silently is the worst
failure this house has: a real phone number that now reads as a byte field, or a marker spelling
that now exempts a line it used to leave red, passes the floor green, and a green floor is read as
"safe to publish". Publication cannot be retracted.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `d0ca5d24`,
  2026-11-09 UTC, and the worker it dispatched, which wrote the commit (per the queue pointer). The
  author queued this pass and does not take it.
- **Who wrote this brief:** a headless brief-writer (`claude-opus-5-5`; `cclive` lists it as session
  `c8eba849`; `$CLAUDE_SESSION_ID` was unset), started 2026-11-14 UTC by an estate health sweep,
  orchestrator session `58027096` (Opus), on the principal's instruction that a brief is written for
  every review known to be owed (Mike, 2026-11-14, verbatim: *"include all briefs are written where
  we know a fable review is required"*). Neither wrote any of this delta. **Off-tier for review,
  disclosed: the brief-writer forms no finding and writes no severity**, and stops after writing.
  It ran no review and used no Fable model.
- **Barred from running this pass:** session `c8eba849` and session `58027096` (whoever writes a
  brief does not run it), and session `d0ca5d24` with everything it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `58027096`: the
  item number, the pointer's opening sentence, and the rules of the sweep. It carried no framing of
  the work. The brief-writer had no contact with the author session or its worker.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md`; the queue pointer whole; **both intent records
  whole**, including the author's landing notes (the line ranges barred below); the unrun brief for
  `160/1300` and its sibling (read for house form). It read the delta's four non-test files
  body-free through `coldsweep`, the two new test classes' names only, `tools/test_allowmarker.py`
  lines 568–585, and `.leakscanignore`. It read **no commit message body** and opened **no prior
  verdict file**. Its harness also loaded user-level and repo instruction files and a memory index,
  which hold private context this brief does not carry. Everything evaluative it formed is in the
  sibling.

## The acceptance test

Both changes answer findings that child repos filed before the work. There is no answer or ruling
of the principal's on either; test whether the delta needed one. Print the filings, from the
worktree root:

```
sed -n '1,27p' docs/roadmap/320-child-filed-findings-via-pointing-up/850-hand-up-leakscan-nz-phone-fires-on-bracketed-hex-byte-strings.md
sed -n '1,21p' docs/roadmap/320-child-filed-findings-via-pointing-up/840-hand-up-secretscan-finding-name-and-rule-list-disagree.md
```

Each filing ends with a **Done means** paragraph. That is the acceptance test: `320/850` asks that
the rule no longer match the byte-field shape, with tests in both directions; `320/840` asks that
the two names reconcile "either way", so the count, the marker grammar and the header comment
agree, with a test that a marker exempting a line is never counted as naming no rule. `320/850`'s
"possible rule" is the filer's proposal, explicitly "the house's to judge": test the shape the
delta chose, not only whether it copied the proposal.

## What the work is

One commit on `main`, authored 2026-11-09 UTC (stamped 2026-11-10 NZDT):

- **`57719bfa`** — `scanners: bracketed byte fields are not phones; one name for the assigned-value
  rule (320/850, 320/840)`.

Read it body-free: `python3 tools/coldsweep.py --root . --commit 57719bfa` (subject, stat and diff,
never the body; board files left out). Plain `git show` prints the body before the diff, and
reading is atomic (`REVIEW.md` rule 1), so it is barred. Check first that your tree has the delta:
`git merge-base --is-ancestor 57719bfa HEAD` exits 0. The pointer names the bound as "the commit
that closes `320/850`, on `main`"; this brief pins it to `57719bfa`. Record the pin in your
verdict's scope.

Delta paths (the pointer's list, which matches the commit):

- `tools/leakscan.py`: `_phone_inside_hex_byte_field`, wired into the `nz-phone` validator beside
  `_phone_inside_hex_digest`.
- `tools/secretscan.py`: `ASSIGNED_RULE`, `RULE_ALIASES`, `canonical_rule`, `_scope_exempts`,
  `ALL_RULES` built from the aliases, `assigned_off` in `scan_lines`, the header comment's marker
  grammar, and the `--disable` help.
- `tools/test_leakscan.py` (`PhoneInsideBracketedByteField`) and `tools/test_secretscan.py`
  (`AssignedRuleHasTwoSpellings`). Both test files sit in `.leakscanignore`, so their fixtures are
  never scanned by leakscan.
- `tools/README.md` (the secretscan escape-hatch paragraph) and `CHANGELOG.md` (the 2026-11-09
  *Fixed* entry).

**The files have moved since.** Nine later commits touch these paths; list them with
`git log --oneline 57719bfa..HEAD -- tools/leakscan.py tools/secretscan.py tools/test_leakscan.py tools/test_secretscan.py tools/README.md`.
The brief-writer checked that the two new code regions are byte-identical at landing and at
`d3293d93` (the `_phone_inside_hex_byte_field` body; `secretscan.py` from `ASSIGNED_RULE =` to
`ALL_RULES`). Two later commits matter beside them: `49f3d407` gives leakscan a commit-message
plane (`--messages`), which this validator now also serves, and `641f017f` changes the scanners'
coverage line. Judge the delta as landed and as it stands at HEAD.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the author's claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1).

- **Byte field.** A match is a byte field, not a phone, "when it lies wholly inside `<` ... `>` and
  the bracketed text is an even-length run of hex digits and nothing else".
- "Only the exact bracket form is exempt, so the rule keeps reach everywhere else": a separator,
  `+` or paren means it is "not a hex run"; "an odd-length run is not whole bytes"; "a bracketed
  all-digit run of exactly ten characters that IS the match is the one unseparated mobile shape
  that is also a whole number of bytes (five), so it is kept as a phone".
- The byte field is "eight to sixteen hex digits" and "falls under the digest guard's 16-character
  floor".
- The changelog: "A bracketed number with a separator, an odd-length run, and a bracketed
  unseparated ten-digit number still flag."
- **Two spellings.** "Both are accepted in BOTH places (`RULE_ALIASES`), so a marker, a `--disable`
  flag and the 'naming no rule' count all read the one list, `ALL_RULES`, and a marker that exempts
  a line is never counted as naming no rule."
- "Findings, JSON and the tally breakdown keep `assigned-secret`", and the changelog's "a typo
  still is" counted.
- `_scope_exempts`: "Case-sensitive, exactly as before."
- `canonical_rule` is "identity for every rule with one spelling, and for a name that is no rule
  at all".
- **Fleet effect.** "No exit code moved in any of 30 child checkouts, probed old against new"; one
  child's 64 per-line allow-markers "are now unused".

## Scope

The widest the work admits: intent, decisions, assumptions, the code, the test code, the docs, and
real-world behaviour: both scanners run against crafted inputs and against this tree. The lenses
organise it; they do not bound it. Anything not named a non-goal is in scope, and a non-goal that
fences off the risk is a finding.

**Non-goals:** the digest guard `_phone_inside_hex_digest` and the `nz-phone` regex themselves
(their own earlier passes), except where this delta's guard interacts with them; the shared
allow-marker grammar in `tools/allowmarker.py` (`160/480`), except where the second spelling
reaches through it; the case-sensitivity mismatch between the count and the match, which the
author records as not changed, except whether leaving it is safe; the child's removal of its 64
markers, which is the child's work.

## The four lenses — run all four

1. **Approach and assumptions** (most important). Is "wholly inside angle brackets, even-length
   hex" the right test for a byte field, or the shape of one fixture? Is a structural exemption
   the right answer at all, against the per-line markers the child already had? Is accepting both
   spellings the right reconciliation, against renaming one, given that a marker that matched
   nothing before can now exempt?
2. **Correctness and quality.** Does each claim above hold when run? Does the ten-digit exception
   cover every real NZ number the `nz-phone` regex can match, unseparated, inside brackets, at
   every length the regex admits? Does every reader of a rule name (`--disable`, the marker, the
   count, the tally, the JSON, the dedupe) agree on the two spellings?
3. **Completeness and harvest.** Every mirror of the rule names and the bracket rule (V3): the
   README's rule lists for both scanners, the skills and templates that name `assigned`, the floor
   config children pass `--disable` through, the allow-marker tests. Other scanners with the same
   finding-name versus rule-list split. Whether the 30-checkout probe reached every plane the
   scanners run on, including the new commit-message plane.
4. **Security and privacy** — a must. Both changes narrow a publish gate: find an input that now
   passes and should not. A real phone number is personal data; a marker that newly exempts a
   credential line is a leak path. This repo is public: check the delta and its tests carry no real
   number or credential, and that the fixtures are fictional. `/security-review` can reach the
   Python diff: aim it at `57719bfa`'s two scanner files, as the floor under this lens and never its
   discharge, and only after your findings are committed (this brief has a held-back sibling).

## Load-bearing assumptions to attack

Each is a falsifiable claim. Damage it with a probe or confirm it by re-driving; never by reasoning
alone. Build any phone-shaped probe input from parts at run time, in your scratchpad: a literal one
committed anywhere outside the leakscan-ignored test files is refused by the rule under review.

- **YA1.** No real NZ phone number, written unseparated inside angle brackets, passes as a byte
  field: every length the `nz-phone` regex admits is either odd or is caught by the ten-digit
  exception.
- **YA2.** A real number padded or adjoined by hex characters inside the brackets is not a shape
  that occurs in text a publish gate should catch.
- **YA3.** The bracket test cannot be satisfied by text outside a byte field: an email header, an
  HTML or XML tag, a URL in angle brackets, a markdown autolink, a generic type parameter.
- **YA4.** The new guard does not change any verdict outside angle brackets, on any plane leakscan
  runs on (tree, staged, commit message).
- **YA5.** Every reader of a secretscan rule name resolves `assigned` and `assigned-secret` to the
  same rule, and no reader still compares against the short spelling alone.
- **YA6.** A marker in the short spelling exempts exactly what one in the long spelling does, and
  nothing more: no other rule, no entropy finding the dedupe would otherwise have kept.
- **YA7.** No child or consumer depended on the short spelling exempting nothing, so newly honouring
  it widens no exemption the fleet relies on being inert.
- **YA8.** The 30-checkout old-against-new probe measured what the claim says, and would have shown
  a narrowing had there been one.

## Re-run list (V2)

The brief-writer ran every line once on 2026-11-14 UTC at `d3293d93`, from the worktree root unless
it says otherwise; each exited 0. Re-run them; a line that no longer reproduces is a finding.

```
git merge-base --is-ancestor 57719bfa HEAD
python3 tools/coldsweep.py --root . --commit 57719bfa
python3 tools/leakscan.py --selftest
python3 tools/secretscan.py --selftest
cd tools && python3 -m unittest test_leakscan.PhoneInsideBracketedByteField test_secretscan.AssignedRuleHasTwoSpellings
cd tools && python3 -m unittest test_leakscan test_secretscan test_allowmarker
```

The two named classes ran 18 tests in under a second; the last line ran 758 tests in about 60 s. To test the behaviour
before the delta, read the tools from a scratch checkout of its parent
(`git worktree add <scratch> 57719bfa~1`), never by editing your review tree.

The delta's recorded proof (V2): "no exit code moved in any of 30 child checkouts, probed old
against new", with the per-child marker counts in the intent records' landing notes (barred until
phase 2). The child checkouts are not in this repo. **That re-run is NOT RUN unless the session
spawning you provides read-only child checkouts**; if it does, run both scanners' parent and HEAD
copies over them read-only, report by exit code and finding count only, and name no child. If it
cannot be re-run, say so and weigh the claim as unverified.

**Live reads:** none. This pass needs no live system and no network beyond the git remote.

## House rules for this run

- **Live systems:** none. No push from a child, no write to GitHub other than your own commits
  here. A check that would need one is marked NOT RUN.
- Name your own review worktree in the verdict. It is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad.
- **Skip the session-log step of the read order** (`CLAUDE.md` step 4; `REVIEW.md` rule 2). If you
  read it anyway, disclose what you met.
- One heavy process at a time, foreground, with a long timeout. Never run an installed tool by bare
  name from `PATH`: use `python3 tools/<x>.py` from your worktree.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo is
  PUBLIC: quote no secret, phone number, email address, private repo name or path, and name no
  child repo. Describe a probe's phone shape in words (its length and prefix class), never by its
  digits.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, this brief's sibling
`docs/reviews/2026-11-14-0229-phone-byte-field-assigned-rule-spelling-cold.deferred.md` (folded
below the verdict at phase 2, the file removed; by count: 11 questions, 6 facts), every item under `docs/roadmap/160-doctrine-review-owed/`
beyond its title, every commit's message body, and these records beyond the `sed` ranges in *The
acceptance test*:

- `docs/roadmap/320-child-filed-findings-via-pointing-up/850-hand-up-leakscan-nz-phone-fires-on-bracketed-hex-byte-strings.md`
  (line 28 onward)
- `docs/roadmap/320-child-filed-findings-via-pointing-up/840-hand-up-secretscan-finding-name-and-rule-list-disagree.md`
  (line 22 onward)

The delta's own `CHANGELOG.md` entry, docstrings and header comment carry the author's account of
why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/850-hand-up-leakscan-nz-phone-fires-on-bracketed-hex-byte-strings.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/840-hand-up-secretscan-finding-name-and-rule-list-disagree.md \
  'byte.field|RULE_ALIASES|ASSIGNED_RULE|canonical_rule|assigned-secret|naming no rule'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions, YA1–YA8 and
the re-run list. Append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, any orchestrator, what you read, the UTC day), the pinned bound,
per-lens answers, V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-claim ledger, findings with stable IDs (prefix `YB`:
`YB1`, `YB2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit body;
append `### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The work changes publish-safety scanners the fleet floats on, written by a queue run; findings go
to the principal with the verdict, in plain words, and none is applied by the session that built
the work (rule 4). Counsel per finding is welcome, labelled as counsel and kept beneath it.

---

## Verdict — act 1, cold pass on Fable 5.1, written 2026-11-15T20:12Z

**Overall: PASS-WITH-FINDINGS** — 0 MAJOR · 2 MODERATE · 3 minor · 3 note. Both changes do what
the filings asked and narrow the gates only on shapes nobody writes as text; the two MODERATE
findings are about what the record can show, not about a real number or credential that now
passes. Act 1 is written before the sibling was opened and is not revised after.

### Provenance (rule 4; V7)

- **Reviewer:** this session, on Fable 5.1 (`claude-fable-5-1`), the principal-named review tier,
  checked at selection.
- **Spawn:** a headless per-pass orchestrator (Opus 5.5), itself started by drain session
  `21a271a5` (Opus 5.5), under the principal's weekly drain order (`/fable-drain`, 2026-11-16
  06:53 NZDT; the approval lapses at the reset, 2026-11-15 23:00 UTC; a pass running at the reset
  may finish). Both are rule-4 off-tier orchestrators: they hold the context partition, commit the
  records, form no finding and write no severity. Neither wrote the brief, the sibling or the
  delta. This session was not started or instructed by `c8eba849` (brief-writer), `58027096` (the
  sweep that started it), `d0ca5d24` (the author's queue run) or anything it started.
- **The spawn prompt, in substance** (process only; it carried no question about the delta and no
  pointer to where the risk lives): the worktree path, read-only but for the brief; the brief and
  review-log paths; that the sibling was removed from the tree and the barred list holds until act
  1 is committed, with the held path to be sent afterwards; the load rules (every test under
  `nice`, one suite at a time, foreground); no commit, no live write, no other file; the
  public-repo naming rules; the verdict's shape and the finish lines. It stated that no child
  checkouts are supplied, so the 30-checkout re-run is NOT RUN and the claim is weighed as
  unverified, which is the brief's own direction.
- **Review worktree:** `/Users/mike/worktrees/fable/atelier-160-1370-1957/atelier` at `cd7baa44`;
  the only dirty entry is the sibling's deletion, by design. A scratch worktree of the parent
  (`57719bfa~1` = `a9c58551`) sat under the session scratchpad for old-against-new probes and is
  removed at the end of act 1.
- **Read:** this brief whole; `docs/method/REVIEW.md`; the two filings' acceptance ranges only
  (`320/850` lines 1–27, `320/840` lines 1–21); the delta body-free (`coldsweep --commit
  57719bfa`, exit 0: three board files left out, no barred file touched); at HEAD,
  `tools/leakscan.py`, `tools/secretscan.py`, `tools/allowmarker.py`, both changed test files and
  `tools/test_allowmarker.py`; `docs/method/GUARDS.md` § *Fail noisy, then subtract*;
  `tools/README.md`; `.leakscanignore`; the board index `docs/ROADMAP.md` lines naming `160/990`
  and `160/1370`. The session-log step was skipped. No commit body, no prior verdict and no
  sibling were opened.
- **Disclosed exposure:** one hand-written mirror grep (not `coldsweep`) printed three lines of
  the `160/1370` pointer (its title, its two "questions worth the pass's time", the brief's path)
  and three of the `160/990` pointer. The two questions are this brief's YA1 and YA6 in substance
  and steered no finding. The brief's prescribed `coldsweep` line then ran (exit 0; 739 files
  excluded as barred). The harness also loaded user-level and repo instruction files and a memory
  index, which hold private context this verdict does not carry.
- **Contact:** none from any author or brief-writer session.
- **Review log**, open by the principal's 2026-11-16 word: the drain's notes directory holds
  `atelier-160-1370-1957.md`, every check and its result, in plain words.

### Scope and the pinned bound

Pinned to **`57719bfa`** (`git merge-base --is-ancestor 57719bfa HEAD` exits 0), judged as landed
and as it stands at HEAD `cd7baa44`. The two code regions the brief names (the
`_phone_inside_hex_byte_field` body; `secretscan.py` from `ASSIGNED_RULE =` to `ALL_RULES`) hash
identically at the landing commit and at HEAD, and the two wiring lines (the `or` in the
`nz-phone` validator; `assigned_off`) are present at HEAD. Nine later commits touch the paths, as
the brief says. The non-goals are accepted as named, with one correction to their grounds (YB7).

### Assumptions named first (lens 1), then attacked

- **A1.** A device dump never renders a phone number as its decimal digits inside the brackets:
  a stored number is hex of ASCII or BCD, which lands either outside the regex (a twenty-hex run
  matches no phone) or under the digest guard. Confirmed by construction.
- **A2.** Exempting by container (angle brackets, hex, even length) rather than by value is safe
  because no publication surface writes a real number inside angle brackets with nothing but hex
  beside it. Probed (YA2, YA3): the escape shapes exist and none is text anyone writes; held, with
  a wording finding (YB4).
- **A3.** Replacing counted per-line markers with a structural exemption is consistent with
  `GUARDS.md` rule (b). Damaged: YB2.
- **A4.** Accepting both spellings is the one non-breaking reconciliation: renaming the flag
  breaks every child's `--disable assigned`; renaming the finding breaks every `assigned-secret`
  marker. Confirmed: the parent refused `--disable assigned-secret` (exit 2) and exempted a
  long-spelling marker while counting it as naming no rule, which is the filed defect.
- **A5.** A short-spelling marker can only have been written to exempt, so honouring it widens
  nothing unintended. Confirmed in this tree (none outside the tests); unverifiable in children.

### Per-lens answers

**Lens 1 — approach.** The byte-field test is the shape of the filing's fixture, generalised just
enough: it keys on the one container a device dump uses and on whole bytes, and it keeps every
separated, signed or parenthesised form. Against the alternative the child already had (64 reasoned
markers, each counted in the tally), the exemption trades noise for visibility: the dropped
matches are counted nowhere (YB2). On the spelling question the delta chose the only answer that
breaks neither the fleet's flags nor the child's markers (A4); the cost is one rule under two names
in `ALL_RULES`, carried by one table. The fleet effect is argued from exit codes, which cannot
show the thing the argument is about (YB1).

**Lens 2 — correctness.** Every runnable claim holds (ledger below). The ten-digit exception
covers exactly the real-number lengths: of the all-digit lengths the regex admits, eight, nine and
ten, nine is odd, ten is kept when it is the whole bracket, and eight is no complete NZ number
(YB5 asks that this be said). It does not cover a ten-digit mobile with hex letters adjoining it
inside the brackets, nor a nine-digit number plus one hex letter: both now pass (YB4). Every
reader of a secretscan rule name agrees on the two spellings: the `--disable` check, the
`assigned_off` switch, the marker's inert count, the exemption compare, the tally and the JSON all
resolve through `RULE_ALIASES` or `ALL_RULES`; `_active_named` compares `NAMED` names only, which
the alias does not touch. Case is where they still disagree (YB3).

**Lens 3 — completeness.** Mirrors: the header comment, the `--disable` help, the README's
escape-hatch paragraph and the changelog carry the two spellings; no skill, template or floor file
in this repo names the `assigned` rule; the README has no per-rule leakscan table, so no mirror of
the bracket rule is owed there. Other scanners: leakscan's marker names are its finding names plus
`local-term` and `diagnosis-key`, by design; datescan, linkscan and spellscan print the same inert
count through `allowmarker` and have no `--disable`, so no second split of this class exists. The
30-checkout probe is not in this repo (NOT RUN); the commit-message plane shares `scan_text` and so
the validator, but the parent has no `--messages`, so the fleet probe cannot have covered it.

**Lens 4 — security and privacy.** Both gates narrow; the inputs that now pass were sought and
found (YA2, YA3): an all-digit eight-digit run inside a bracket, a ten-digit mobile with hex
letters adjoining it inside the bracket, a nine-digit number plus one hex letter, two such fields
side by side, and an all-digit generic-type parameter. None is a shape a person writes a number in;
a real number in a dump is encoded past the regex (A1). Every separated, signed, parenthesised,
one-sided, header, autolink and `0x` form still flags, and nothing outside a complete bracket moved
(YA4, 21 synthetic lines and the whole tree). On the secretscan side a short-spelling marker now
exempts one rule's findings on its own line and nothing else (YA6), and the only lines it can
newly clear carry a reasoned marker naming the rule. Fixtures: the leakscan tests use the
555-pattern mobile and sequential-digit landline shapes; the secretscan test reuses the suite's
existing synthetic token; both test files are in `.leakscanignore`; the whole tree scans clean at
HEAD with the parent's scanner and with HEAD's. **`/security-review`: NOT RUN**, with grounds: it
reads the session's pending diff, which in this worktree is the sibling's deletion (its text would
print as removed lines) and this verdict, while the Python delta is landed, not pending.

### Load-bearing assumptions (YA1–YA8)

- **YA1 — damaged as worded, no number lost.** The regex admits all-digit lengths 8, 9 and 10.
  Bracketed exactly: 9 flags, 10 flags, 8 is exempt (it was flagged at the parent). Eight is even
  and outside the ten-digit exception; no complete NZ number has eight digits. *Probe:* old/new
  scan of each length.
- **YA2 — held, with an overbroad published claim.** A ten-digit mobile with two hex letters
  adjoining it (either side, or one each side) passes; a nine-digit number plus one hex letter
  passes; a ten-digit mobile plus one hex letter (odd) flags. None is a text shape (YB4). *Probe:*
  old/new scan.
- **YA3 — held.** An email `Message-ID`, a `tel:` autolink, an HTML-tag-like bracket, plus,
  paren, dashed and spaced forms, one-sided brackets, template placeholders of nine and ten
  digits, and `0x`-prefixed runs all flag as before. Two adjacent fields and an all-digit generic
  parameter now pass; neither is text. *Probe:* old/new scan.
- **YA4 — confirmed.** 21 synthetic lines without a complete bracket: 0 moved. Whole tree, the
  parent's leakscan against HEAD's, `--json`: both clean, identical sets. `--messages` shares
  `scan_text`; a smoke run over five messages ran. *Probe:* corpus; tree; `--messages
  HEAD~5..HEAD`.
- **YA5 — confirmed for spelling.** Library and CLI: both spellings disable the rule; both exempt
  as a marker; a typo is refused (`--disable`, exit 2) or counted (marker). Case: `Assigned` is
  refused at the CLI; a mixed-case marker is counted as naming a rule yet exempts nothing (YB3).
  *Probe:* library and CLI, both trees.
- **YA6 — confirmed.** A line with an assigned secret and a separate entropy token: the short
  marker clears the assigned finding only; the entropy finding was dropped by the dedupe at both
  parent and HEAD, marker or not. `assigned` collides with no `NAMED` name; `canonical_rule` is
  identity for all 19 single-spelling rules. *Probe:* old/new scan.
- **YA7 — unverified.** No `secretscan:allow:assigned` marker in this tree outside the tests;
  children not supplied. A child with such a marker on a red line would have been red in CI
  already, which bounds the exposure. *Probe:* tree grep.
- **YA8 — NOT RUN**, and the measure is questioned (YB1). No probe possible here.

### Per-claim ledger

Each claim is the delta's own, from *The claims the delta makes* above.

- *A byte field is a match wholly inside `<`…`>`, even-length hex and nothing else.* Holds as
  coded.
- *Only the exact bracket form is exempt; separator, `+` and paren break the run; an odd run is
  not whole bytes.* Holds.
- *A bracketed all-digit run of exactly ten that IS the match is kept as a phone.* Holds, exact
  span only; adjoined hex defeats it (YB4).
- *The field is eight to sixteen hex digits, under the digest guard's 16-character floor.* Holds
  for 8–14; a sixteen-run was the digest guard's already (YB5).
- *Changelog: a separator, an odd run and a bracketed unseparated ten-digit number still flag.*
  Holds for the exact-span ten-digit form only (YB4).
- *Both spellings accepted in both places; one list; an exempting marker is never counted inert.*
  Holds (probe, CLI, JSON).
- *Findings, JSON and the tally keep `assigned-secret`; a typo still counts.* Holds.
- *`_scope_exempts` is case-sensitive, exactly as before.* Holds, and so the count and the match
  still split on case (YB3).
- *`canonical_rule` is identity for every one-spelling rule and for a non-rule.* Holds.
- *No exit code moved in 30 child checkouts; one child's 64 markers are now unused.* NOT RUN;
  weighed unverified; the exit-code measure cannot show a narrowing (YB1).

### Standing checks V1–V7

- **V1.** Three claims outrun their evidence: the fleet proof (YB1), the changelog's ten-digit
  sentence (YB4), the docstring's range and silence on eight (YB5).
- **V2.** Every re-run line reproduces (ledger below). The fleet re-run is NOT RUN.
- **V3.** Swept: header comment, help text, README, changelog carry the change; no skill,
  template or floor file names the rule; no leakscan per-rule table exists to mirror. Discharged.
- **V4.** `RULE_ALIASES` is the one home; `ALL_RULES` derives from it; the README's restatement is
  prose at the point of use. Discharged.
- **V5.** One internal slip (the "sixteen" in the docstring, YB5); the code comments cite
  `320/850` and `320/840`, and the rule reached in each is the filing's "Done means". The
  `allowmarker.names_no_rule` docstring says the scanners lower-case compare; secretscan does not
  (YB3).
- **V6.** Lens 4 above; `/security-review` discharged with grounds.
- **V7.** Stated above.

### Findings

**YB1 — MODERATE (V1, lens 1; YA8).** The delta's fleet proof is "no exit code moved in any of
30 child checkouts, probed old against new". A child that floats green on the floor is green before
and after whatever this guard waves through: a line that moves from flagged-and-marked to unflagged
changes no exit code, and a line that moves from red to green changes it only if it was the child's
last red line. So the measure as published cannot show the narrowing it is cited against. The
second half of the claim (64 markers now unused) is a marker-count measure, which can show it, and
suggests the author also counted; but the published proof is the exit code. Weighed as unverified
here. *Counsel:* record the fleet probe as a per-child, per-rule finding diff under `--json` with
markers honoured and again with them ignored, and list the lines that moved; that is the proof the
changelog sentence needs. To be reconciled against the landing notes in act 2.

**YB2 — MODERATE (lens 1; `GUARDS.md` rule (b)).** The byte-field exemption is a silent
subtraction. The regex forms the match, the validator drops it, and no counter anywhere records
that it happened: the tally has `note_marker` and `note_unknown_scope` only, so leakscan's output
for "no phone shapes" and "forty phone shapes waved through as byte fields" is the same line.
Rule (b) asks every guard to print what it suppressed and by which mechanism, and the delta
replaced 64 counted, reasoned markers with zero visible count. The house frames `VALIDATORS` as
part of a rule's definition ("not one of the shapes we ruled out"), which fits a Luhn check; this
guard rules a shape out by its *surroundings*, which is what an allowance does. The digest guard
(`320/470`) set the precedent and its own pass has not returned (YB7). *Counsel, the principal's to
rule:* either count validator drops per rule in the suppressed line (one `note_` method and one
`continue` branch), or record, once, that shape validators are definition and not allowance, so
the next guard of this kind inherits a decision rather than a precedent.

**YB3 — minor (lens 2; the `320/840` acceptance test, "agree").** The count and the match now
agree on spelling and still disagree on case. `allowmarker.names_no_rule` lower-cases both sides,
so a marker spelt `Assigned-Secret` or `ASSIGNED` is counted as naming a rule, while
`_scope_exempts` compares case-sensitively, so the same marker exempts nothing and the line stays
red. That is the filed defect's class in the other direction: the tally says every marker names a
rule while one is inert. It fails closed, so the gate is not narrowed, and the author recorded the
choice to leave it; the `names_no_rule` docstring, which says "as the scanners that lower-case
compare", is wrong for secretscan. *Counsel:* lower-case in `_scope_exempts` or make the inert
count case-sensitive for this scanner; either is one line, plus a test in the direction the delta's
invariant test does not run (counted as known ⇒ exempts).

**YB4 — minor (V1; YA2).** The changelog says "a bracketed unseparated ten-digit number still
flag[s]". The code keeps it only when the ten digits are the whole bracket; with hex letters
adjoining it inside the brackets (two on one side, or one each side) it passes, and a nine-digit
number plus one hex letter passes. The docstring is exact ("that IS the match"); the changelog and
the filing-facing sentence are not, and no test pins the adjoined-hex ten-digit case in either
direction. The shapes are not text anyone writes, so this is wording and a missing pin, not a
leak. *Counsel:* one clause in the changelog and one test each way.

**YB5 — minor (V1, V5).** Two slips in the docstring. It gives the field as "eight to sixteen hex
digits" that "fall under the digest guard's 16-character floor"; a sixteen-run is at the floor and
was exempt before this delta, so the new guard's range is eight to fourteen. And it never says why
an even eight-digit all-digit run is safe to drop: it is the filing's very shape and the delta's
own fixture, and the reason (no complete NZ number has eight digits; the regex's three-digit tail
admits one) is the load-bearing sentence a future reader of YA1 needs. *Counsel:* two sentences.

**YB6 — note (lens 3).** A leakscan marker left on a line the guard now clears is neither used
nor reported: `by_marker` is empty for it and it is not "naming no rule", because the rule exists.
So the child learns its 64 markers are dead only by a count falling. Pre-existing class, not this
delta's; recorded because the delta is the first change to create such markers in bulk.

**YB7 — note (brief framing).** The non-goal fences the digest guard off as having "its own
earlier pass". The board index shows that pass (`160/990`) claimed with no verdict, so the
precedent this guard copies is unreviewed, and YB2's question is open for both. This pass does not
depend on it; the wording should.

**YB8 — note (polish).** `--disable assigned,assigned-secret` prints "2 rule(s) disabled" for one
rule; and the README's new sentence nests one parenthesis inside another. Neither changes a
verdict.

### Re-run ledger (V2)

| Line | Result |
|---|---|
| `git merge-base --is-ancestor 57719bfa HEAD` | exit 0 |
| `coldsweep.py --root . --commit 57719bfa` | exit 0; subject, stat and diff only |
| `leakscan.py --selftest` | selftest OK |
| `secretscan.py --selftest` | selftest OK |
| the two named classes | 18 tests, OK |
| `unittest test_leakscan test_secretscan test_allowmarker` | 758 tests, OK, 74 s under `nice` |
| 30-checkout old-against-new fleet probe | NOT RUN: no child checkouts supplied |

Every test ran under `nice -n 10`, one suite at a time, in the foreground. Live systems: none
touched; none needed.

### Follow-up checklist

- [ ] YB1: reconcile against the landing notes in act 2; if the per-child counts there are
      finding-level, downgrade to a wording finding on the changelog sentence.
- [ ] YB2: the principal's ruling on counting validator drops, or on recording validators as
      definition; carry the same question into `160/990`.
- [ ] YB3: case in `_scope_exempts` or in the inert count; fix the `names_no_rule` docstring;
      add the converse test.
- [ ] YB4: changelog clause; two tests on the adjoined-hex ten-digit shape.
- [ ] YB5: two docstring sentences (range; why eight is safe).
- [ ] YB6–YB8: notes for the owner; no action required by this pass.
- [ ] Act 2: open the sibling and the barred records; screen the commit body; `### Reconcile`.

Counsel is labelled as counsel throughout and sits beneath its finding; every finding is the
principal's to decide (rule 3), and none is applied by the session that built the work (rule 4).

### Reconcile — act 2, written 2026-11-15T20:19Z

Opened after act 1 was committed unrevised (`fa2bfe2e`): the held sibling (11 questions, 6 facts,
as the brief counted), the two filings' landing notes (`320/850` from line 28, `320/840` from line
22), the `160/1370` pointer whole, and the commit body of `57719bfa`. The `160/990` brief, the
digest guard's own pass, still reads BRIEF ONLY in this tree, so there is no prior verdict to
reconcile against. Act-1 text above is unchanged; where a finding's weight moves, it moves here.

**The author's account, screened.** The commit body and the landing notes carry more than the
changelog does: the fleet probe is reported as "no exit code moved **and no finding appeared**"
(`320/850`) and "no finding changed" (`320/840`), so a finding-count measure sat beside the exit
code; the one child's `nz-phone` marker count fell from 70 to 6; the "naming no rule" count fell
12, 10 and 4 to 0 in the three children that carried the long-spelling marker; "no child carries a
marker in the short spelling, so nothing newly exempts anything"; and the case mismatch is recorded
as deliberately "not changed". The body gives the exact-span ten-digit rationale ("would be a false
negative on a real number") and the worker's identity. Nothing in it contradicts the delta or the
act-1 reading of it.

**The sibling's six facts** agree with the act-1 probes point for point: fact 1 is YA1's eight-digit
pass; fact 2 is YA2's adjoined-byte pass; fact 3 is YA4's one-sided bracket; fact 4 is the
`test_allowmarker` real-scope case (YB10 below); fact 6 is the dedupe-then-exempt order YA6 relied
on. Fact 5 left one check open: `tools/test_secretscan.py` is in `.secretscanignore` (line 12), and
secretscan over that file at HEAD reports it suppressed by the ignore, exit 0.

**Per finding, against the sibling's questions and the author's account.**

- **YB1 — moves from MODERATE to minor at reconcile.** Sibling Q11 asked the same question. The
  author's record answers half of it: the probe compared finding counts ("no finding appeared", "no
  finding changed") and marker counts, not exit codes alone, and the marker-count fall (70 to 6) is
  the measure that can show a narrowing. What stands: the changelog published only the exit-code
  sentence (V1); the 64 lines that moved from marked to unflagged are not listed or said to have
  been inspected (the child marked them as byte fields when it added the markers, which is fair
  evidence, but it is the child's, not the probe's); and the planes probed are not named, so the
  commit-message plane, which the parent lacks, cannot have been covered. *Counsel stands:* name
  the planes and the measure in the changelog; list moved lines next time.
- **YB2 — stands, MODERATE.** Sibling Q7 asks the cost of a structural exemption every child
  inherits against 64 markers in one child. The author's account does not weigh it against rule
  (b); it reports the marker count falling as the fleet effect, which is the only visibility the
  change leaves. The principal's ask in act 1 stands as written.
- **YB3 — stands, minor.** The author recorded the case split as "not changed", as the brief's
  non-goal said. The ask stands: fail-closed is safe, and the count is still wrong about an inert
  marker, in the class the filing complained of.
- **YB4 — stands, minor.** Sibling Q4 and fact 2 are the same shape. The author's rationale covers
  the exact-span case only and is silent on the adjoined-byte case; the changelog sentence remains
  broader than the code.
- **YB5 — stands, minor.** Sibling Q3 asked which lengths were checked and against what source;
  the account names ten only. Act 1 supplies the missing sentence (eight is no complete NZ number).
- **YB6 — stands, note.** The author detected the dead markers by the count falling, as the note
  predicts; nothing reports them as dead.
- **YB7 — stands, note.** Confirmed: the digest guard's brief has no verdict in this tree.
- **YB8 — stands, note.**

**Findings formed at reconcile** (marked as such; neither changes the overall line):

- **YB9 — note, formed at reconcile (sibling Q8).** A narrower reconciliation existed: accept the
  short spelling in `--disable` only (so no child's floor flag breaks) and compare markers against
  the finding name alone, which fixes the count and widens no marker grammar. The delta widened the
  marker grammar too. By the author's own fleet measure the widening is empty today (no child
  carries a short-spelling marker), so this is a choice for the principal, not a defect: two
  accepted marker spellings for one rule, or one. Act 1's A4 stands as the reason the delta's choice
  is at least non-breaking.
- **YB10 — note, formed at reconcile (sibling Q9, fact 4).** `tools/test_allowmarker.py` used a
  short-spelling marker as its "real scope" case before the delta, asserting that a marker names a
  real rule while that marker exempted nothing. The delta made the assertion true by behaviour
  without touching the test, and no record says the test's meaning was re-read. No other test
  encodes the old split (the suite's other markers use the finding name). *Counsel:* one comment on
  that case naming `320/840`, so the next reader knows why it holds.

**Sibling questions not already covered.** Q5: answered by YA3 (held). Q6: the guard walks over hex
characters, not digits, so adjoined hex letters widen the run (YA2); at the boundary the digest
guard decides sixteen and above first, the new guard covers even runs of eight to fourteen, and a
fifteen-run is odd and flags, so there is no gap and the overlap at sixteen is harmless. Q10:
answered by YA6, with the author's account agreeing (no child carries the short spelling). Q1 and
Q2, the pointer's own: no real number passes in any shape a person writes (YA1–YA3, with YB4 and
YB5 as the wording owed); the second spelling exempts exactly what the first does (YA6).

**Overall, restated: PASS-WITH-FINDINGS.** Act-1 tally 0 MAJOR · 2 MODERATE · 3 minor · 3 note;
after reconcile, 0 MAJOR · 1 MODERATE (YB2) · 4 minor (YB1, YB3, YB4, YB5) · 5 note (YB6–YB10).
Every finding is the principal's to decide (rule 3); none is applied by the session that built the
work (rule 4). The sibling is left for the orchestrator to fold.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-15)

*Released to the reviewer only after its act-1 findings were committed (`fa2bfe2e` before the
rebase onto `main`); folded here verbatim (headings demoted two levels) and the sibling file
removed, per the brief. The orchestrator (a headless Opus 5.5 session started by drain session
`21a271a5`, itself Opus 5.5) held the partition, formed no finding and wrote no severity.*

### Held back — `nz-phone` passes a bracketed byte field, and secretscan's assigned-value rule takes two spellings

Opened only once the reviewer's own findings are durably written (`REVIEW.md` rule 1). A floor,
never a fence. Written by the brief-writer (`cclive` lists it as session `c8eba849`), which did not
author the delta. Nothing here is a finding: these are questions, and facts read off the machine.

#### The pointer's own questions

1. Can a real number pass as a byte field?
2. Can the second spelling exempt a line it should not?

#### The brief-writer's questions

3. The guard's test is that the whole bracketed run is even-length hex. The `nz-phone` regex admits
   tails of three or four digits, so it matches unseparated shapes of more than one length (fact 1).
   Is every even length it admits a real NZ number shape or not? The ten-digit exception answers one
   length only. Which numbering-plan lengths did the author check, and against what source?
4. The ten-digit exception holds only when the match IS the whole bracketed run. A real number with
   one adjoining hex byte inside the same brackets passes (fact 2). Is that shape ever how a number
   is written (a padded field, a number followed by a check byte, a pasted dump of a contact
   record)? If never, say why; if sometimes, is the exception drawn in the right place?
5. Angle brackets also wrap email addresses, URLs, markdown autolinks, and XML and HTML tags. Can any
   of them leave an even-length run of decimal digits as the whole bracketed text? A bare number in
   angle brackets in prose or a template placeholder?
6. The guard scans outward over hex characters from the match, not over digits. Does a run like a
   phone number with hex letters adjoining it inside brackets still behave as the docstring says?
   Does the digest guard, run first, already decide every case the new guard was meant for at
   sixteen characters, so the two guards overlap or leave a gap at the boundary?
7. The child reported eight-to-sixteen-digit fields from one tool's dumps. Is the fix the narrowest
   that answers it, against an exemption tied to that dump format (the property line around the
   brackets), or against the per-line markers the child already carried? What is the cost of a
   structural exemption every child inherits, against 64 markers in one child?
8. Before the delta, a marker in the short spelling exempted nothing and was counted as naming a
   rule; a marker in the long spelling exempted the line and was counted as naming no rule. The
   delta makes both exempt. Is "either way" in the filing's *Done means* satisfied by widening, when
   renaming the count's list to the long spelling would have fixed the count and widened nothing?
9. `test_allowmarker.py` used a short-spelling marker as its "real scope" case before this delta
   (fact 4): a test asserting a marker names a real rule while that marker exempted nothing. Did the
   delta re-read that test's meaning, and does any other test still encode the old split?
10. The dedupe drops an entropy finding on any line that also has a named or assigned finding, and
    the marker check runs after the dedupe (fact 6). With a scoped marker naming the assigned rule
    on a line that also carries a high-entropy token elsewhere on the line, does the entropy
    finding vanish with the assigned one? Was that true before the delta for the long spelling, and
    does the short spelling now extend it?
11. The fleet probe is "by exit code across 30 child checkouts". An exit code cannot move for a
    narrowing on a child that was already green, or on a finding that is advisory. Did the probe
    compare finding sets as well, and across which planes? Did it include the commit-message plane,
    which landed after this delta (`49f3d407`)?

#### Facts read off the machine

Read 2026-11-14 UTC at `d3293d93`, by building inputs from parts in a scratch script and running
`leakscan.scan_text` over them. No phone-shaped literal is written here, by design.

1. Inside angle brackets with nothing else, an unseparated landline-prefixed shape of eight digits
   (the regex's three-digit-tail form) **passes**; the nine-digit form **flags**.
2. An unseparated ten-digit mobile-prefixed shape alone in brackets **flags**. The same shape
   followed inside the brackets by one more byte, either two digits or two hex letters, **passes**.
3. A byte field and a separate unbracketed number on the same line: the number still **flags**. A
   bracket opened and not closed before an eight-digit shape: **flags**.
4. `tools/test_allowmarker.py` line 572 at `57719bfa~1` (from `6d26b058`, the same day) uses
   `secretscan:allow:assigned: real` as the real-scope case in
   `test_each_rule_matching_scanner_counts_a_typo_and_not_a_real_scope`; it reads the same at HEAD.
5. `tools/test_leakscan.py` and `tools/test_secretscan.py` are both listed in `.leakscanignore`, so
   leakscan never reads their fixtures; secretscan's own exemption for its test file was not
   checked.
6. In `secretscan.scan_lines`, `_dedupe_same_span` runs first (an entropy finding is dropped on any
   line holding a `named` or `assigned`-kind finding), then `_scope_exempts` drops findings a marker
   covers. At the parent, the exemption test was `scope in ("", f.rule)`.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

Appended by drain session 21a271a5 at its close (2026-11-16): this pass ran
before the fold step that appends the log, so the log stayed in a
user-local file. Text below is the reviewer's, unedited.

# Review log: atelier 160/1370 cold pass (phone byte field; assigned-rule spelling)

Reviewer: Fable 5.1, spawned by a headless per-pass orchestrator under drain session 21a271a5.
Worktree: /Users/mike/worktrees/fable/atelier-160-1370-1957/atelier (read-only except the brief).
Rule: checks and evidence only; no secrets, no phone digits, no live captures.

## Act 1

- 2026-11-15T19:59:05Z log opened; brief read in full; REVIEW.md read next
- Tree: HEAD cd7baa44; only the sibling's deletion dirty (by design). `git merge-base --is-ancestor 57719bfa HEAD` exit 0: pin confirmed.
- Nine later commits touch the delta paths (list matches the brief's claim of nine).
- Load at start: averages 7.4/10.8/9.9 on this laptop; all tests will run niced, one at a time.
- Read the delta body-free via `coldsweep --commit 57719bfa` (exit 0; 3 board files left out, 0 barred files touched). Message body not seen.
- Read the two filings' acceptance ranges only (320/850 lines 1-27; 320/840 lines 1-21).
- Re-runs (niced, sequential): leakscan --selftest OK; secretscan --selftest OK; the two named classes 18 tests OK; full three-module line exit 0 (count in full3.log).
- Scratch worktree of the parent (57719bfa~1 = a9c58551) added under the scratchpad for old-vs-new probes.
- Code reads: leakscan validator skips are NOT tallied (Tally has note_marker and note_unknown_scope only); the --messages plane calls scan_text so shares VALIDATORS; secretscan readers of a rule name found at: --disable unknown check (ALL_RULES), _active_named (NAMED names only), assigned_off (RULE_ALIASES keys), names_no_rule (ALL_RULES, case-insensitive), _scope_exempts (canonical, case-sensitive), tally.note_marker(f.rule) and JSON by_allow_marker_rule (finding name).
- Mirror sweep: README secretscan paragraph updated by the delta; README has no per-rule leakscan table naming nz-phone (no mirror owed there); no skill/template/.github file names the `assigned` rule; no `secretscan:allow:assigned` marker in the non-test tree; test_allowmarker already used the short spelling as a "real" scope.
- Full three-module line: Ran 758 tests, OK (74 s niced).
- Probe (scratchpad probe.py, inputs built from parts; old = parent a9c58551, new = HEAD):
  - YA1: regex admits all-digit lengths 8 (landline prefix), 9 (both classes), 10 (mobile). Bracketed exactly: 9 -> flagged old and new; 10 -> flagged old and new; 8 -> flagged old, EXEMPT new. No complete NZ number is 8 digits, so no real number lost, but the brief's YA1 wording ("odd or caught by the ten-digit exception") is false for 8; the delta's own test pins the 8-digit field as passing, and the filing's shape is that length.
  - YA2: 10-digit mobile with 2 hex letters adjoined inside the brackets -> exempt new; 9-digit (either class) + 1 hex letter -> exempt new; 10-digit + 1 hex (odd) -> still flags. Changelog's "a bracketed unseparated ten-digit number still flags" holds only for the exact-span form; the docstring says "that IS the match" (precise).
  - YA3: email msgid, tel: autolink, html-tag-ish, plus/paren/dashed/spaced forms, one-sided brackets, template placeholders (9 and 10), 0x-prefixed runs: all unchanged (still flag). Generic-type shape with an 8-digit all-digit parameter and adjacent `<f><f>` fields: now exempt (not realistic text).
  - YA4: 21-line synthetic corpus without a complete bracket: 0 moved. Whole tree, parent vs HEAD leakscan --json: both clean, 0 findings, identical sets. --messages plane calls scan_text, so shares VALIDATORS; smoke on HEAD~5..HEAD ran (0 findings in 5 messages).
  - leakscan marker on a now-exempt byte field: by_marker={} (the marker is unused and uncounted; not counted as naming no rule either).
  - YA5: library + CLI: `assigned` and `assigned-secret` both disable the rule at HEAD (parent refused the long form, exit 2); `Assigned` refused exit 2 both trees (fail closed); typo refused both. Marker: short spelling exempts at HEAD (inert at parent, and parent counted it as a REAL scope: unknown=0); long spelling exempts in both, parent counted it as naming no rule (the filing's defect); typo counted 1 both. Mixed-case marker `Assigned-Secret`: not exempt at HEAD, counted 0 naming no rule (count is case-insensitive via allowmarker.names_no_rule, match is case-sensitive via _scope_exempts). Same for `ASSIGNED` (both trees).
  - YA6: two-token line (assigned secret + separate entropy token): entropy dropped by dedupe in both trees with or without a marker; the short marker exempts only the assigned-secret finding. No widening beyond the aliased rule. `assigned` collides with no NAMED name; canonical_rule is identity for every single-spelling rule; alias values are in ALL_RULES.
  - JSON: by_allow_marker_rule keys the short marker under `assigned-secret` at HEAD.
- YA7: no `secretscan:allow:assigned` marker in atelier's non-test tree; children not supplied -> unverified.
- YA8: NOT RUN (no child checkouts). Shape concern: exit code cannot show a line moving from marked/flagged to unflagged in a child that was green before and after.
- Lens 3: leakscan's own marker names vs STRUCTURAL: marker set adds `local-term` and `diagnosis-key` by design (BY_NAME includes withdrawn rules); no finding-name/rule-list split there. datescan/linkscan/spellscan print the same "naming no rule" count via allowmarker; they have no --disable. README 824-831 all <= 95 columns.
- Disclosure: my hand-written mirror grep (not coldsweep) printed three lines of the 160/1370 pointer (1, 9, 13: the title, the pointer's two "questions worth the pass's time", the brief path) and three of the 160/990 pointer (3, 18, 21). Both questions are already the brief's YA1 and YA6 in substance; they steered no finding. The prescribed coldsweep line then ran clean of barred paths (exit 0, 739 files excluded).
- /security-review: NOT RUN. It reads the session's pending diff; here that is the deleted sibling (its text would print as removed lines) and my own brief edit, and the Python delta is landed, not pending.
- Board index (not an item file): 160/990, the digest guard's own cold pass, shows `[~] ⏳` (claimed, no verdict), so the brief's non-goal "their own earlier passes" rests on a pass not yet returned.
- Code regions hash identically at 57719bfa and HEAD (byte_field body f3020eddbd15; alias region 9eb5ba935ea5).
- Act 1 verdict appended to the brief 2026-11-15T20:12Z: PASS-WITH-FINDINGS, 0 MAJOR / 2 MODERATE (YB1 fleet-proof measure; YB2 silent validator subtraction vs rule (b)) / 3 minor (YB3 case split count-vs-match; YB4 changelog ten-digit sentence overbroad, no adjoined-hex test; YB5 docstring range and silence on eight) / 3 note (YB6 dead markers uncounted; YB7 non-goal rests on 160/990 pending; YB8 polish). Status line updated.
- Gates over the brief: datescan, spellscan, wrapscan, leakscan, linkscan, reviewscan all exit 0.
- Scratch parent worktree removed and pruned; probe captures deleted; probe.py and full3.log kept in the scratchpad (no phone digits in either).
- Act 1 complete; sibling not opened. Waiting for the held path.
- 2026-11-15T20:17:24Z tables in the verdict reflowed to wrapped lists (same words); verdict has 0 lines over 100 columns; six gates re-run, all exit 0. ACT 1 SAVED; stopping until the held path arrives.

## Act 2

- Orchestrator released the held sibling path after committing act 1 (fa2bfe2e). Read: the sibling (11 questions, 6 facts, matching the brief's count); 320/850 line 28+ and 320/840 line 22+ (the author's landing notes); the 160/1370 pointer whole; the commit body of 57719bfa; the 160/990 brief's Status line (still BRIEF ONLY in this tree, so no prior verdict on the digest guard to reconcile against).
- Author's account adds, beyond the changelog: "no finding appeared" (850) / "no finding changed" (840) across the 30 checkouts, i.e. a finding-count measure beside the exit code; the one child's nz-phone marker count fell 70 -> 6; the "naming no rule" count fell 12, 10, 4 -> 0 in three children; "No child carries a marker in the short spelling"; the case mismatch recorded as "Not changed". Commit body: co-authored by the worker (Sonnet 5.5); tests 409 + 266 OK; the exact-span ten-digit rationale ("would be a false negative on a real number").
- Sibling facts 1-6 agree with my probes (fact 1 = eight passes; fact 2 = adjoined byte passes; fact 3 = one-sided bracket flags; fact 4 = test_allowmarker's real-scope case; fact 6 = dedupe-then-exempt order).
- Fact 5 closed: tools/test_secretscan.py is in .secretscanignore (line 12); secretscan over it at HEAD exit 0, suppressed by the ignore.
- Reconcile appended 2026-11-15T20:19Z. YB1 moves MODERATE -> minor (the author's notes carry finding-count and marker-count measures beside the exit code; what stands is the changelog's weaker sentence, no listing of the 64 moved lines, planes unnamed). YB2-YB8 stand. Formed at reconcile: YB9 note (a narrower reconciliation existed: short spelling in --disable only; the widening is empty across the fleet by the author's measure); YB10 note (test_allowmarker's real-scope case made true by behaviour, not re-read). Sibling Q5, Q6, Q10 answered from act-1 probes; no boundary gap between the two guards (even 8-14 new; 15 odd flags; 16+ digest).
- Reconciled tally: 0 MAJOR / 1 MODERATE / 4 minor / 5 note. Overall PASS-WITH-FINDINGS restated.
- 2026-11-15T20:21:06Z reconcile: 0 lines over 100 columns; six gates exit 0; act-1 text byte-identical to fa2bfe2e (pure append). Sibling not folded, nothing deleted: the orchestrator folds. ACT 2 SAVED.
