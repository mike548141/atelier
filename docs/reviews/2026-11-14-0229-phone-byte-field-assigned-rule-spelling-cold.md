# Cold pass — `nz-phone` passes a bracketed byte field, and secretscan's assigned-value rule takes two spellings

**Board:** `docs/roadmap/160-doctrine-review-owed/1370-rule-4-cold-pass-queued-phone-byte-field-rule-spelling.md`
**Status:** BRIEF ONLY, not run. Written 2026-11-14 UTC by a headless Opus 5.5 brief-writer
(`cclive` lists it as session `c8eba849`). Queued, waiting on the principal's explicit approval of
Fable work; this brief is not that approval.

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
`docs/reviews/2026-11-14-0229-phone-byte-field-assigned-rule-spelling-cold.deferred.md` (a held-back
file; by count: 11 questions, 6 facts), every item under `docs/roadmap/160-doctrine-review-owed/`
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
