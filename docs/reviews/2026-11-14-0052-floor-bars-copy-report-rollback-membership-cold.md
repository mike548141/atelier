# Cold pass — the board-check bar, the rule-copy report, the archive's rollback check, membership and the transcript review

**Board:** `docs/roadmap/160-doctrine-review-owed/1240-rule-4-cold-pass-queued-board-check-bar-membership-review-cadence.md`
**Status:** BRIEF ONLY, not run. Written 2026-11-14 UTC by session `a2c067e3`, a headless Opus 5.5
brief-writer. Queued, waiting on the principal's explicit approval of Fable work; this brief is not
that approval.

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (floor checks, a
fleet gate and doctrine text that every child inlines are doctrine by function, rule 3).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Size of this pass:** large: about 2,900 changed lines over nine commits, two thirds of them
`tools/floor.py`, `sizescan.py`, `stampscan.py`, `pins.py`, `instruments/ccarchive` and their tests;
the rest doctrine across nine files, two of them stamped copies every child inlines.
**Why it earns a review:** The delta adds two dated gates that turn red across the fleet on
2026-12-09, a fleet-wide comparison of every child's copy of the floor, a tamper check on the one
archive that holds sessions already pruned from the machine, and a change to who counts as a child
at all. The worst failure is a check whose green is read as safe and is not: a rollback the archive
check adopts as current, or a drifted floor copy the report calls clean because it compares the
child against the wrong text. The second worst is the date itself: a gate that reds healthy repos,
or blocks nothing because nothing runs it.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `722ac2e2`,
  2026-11-09, in its ruling round, and the Sonnet worker it dispatched for each commit (per the
  queue pointer). The author queued this pass and does not take it.
- **Who wrote this brief:** session `a2c067e3` (`claude-opus-5-5`), a headless brief-writer started
  2026-11-14 UTC by an estate health sweep, orchestrator session `58027096` (Opus), on the
  principal's instruction that a brief is written for every review known to be owed. Neither wrote
  any of this delta. **Off-tier for review, disclosed: the brief-writer forms no finding and writes
  no severity**, and stops after writing. It ran no review and used no Fable model.
- **Barred from running this pass:** session `a2c067e3` and session `58027096` (whoever writes a
  brief does not run it), and session `722ac2e2` with everything it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `58027096`: the
  item number, the pointer's opening sentence, and the rules of the sweep. It carried no framing of
  the work. The brief-writer had no contact with the author session or its workers.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md`; the queue pointer whole; **the five intent
  records whole** (`160/790`, `160/020`, `160/670`, `160/340`, `200/030`), which carry the prior
  verdicts' headline findings (HX, CM, HD, FV) and the author's account of each application;
  `420/030` whole; the last lines of `160/290`, `160/230`, `160/270` and `020/215`; every delta
  commit body-free through `tools/coldsweep.py --commit`, the doctrine, changelog, README and man
  page hunks in full and the code hunks in part; commit subjects through `git log`; and
  `docs/reviews/2026-11-09-0238-estate-root-reader-side-two-steps-cold.md` and its sibling whole (an
  unrun brief for another pass, read for house form). It opened **no prior verdict file and no
  delta commit's message body**. Its harness also loaded user-level and repo instruction files and
  a memory index, which hold private context this brief does not carry. Everything evaluative it
  formed is in the sibling.

## The acceptance test

The principal's words and answers, printed by these lines. Where the text is his own words it says
so; the rest are labels of options he picked, and the option text around them is the author's and
is barred until phase 2.

```
grep -o '"Bar it;' \
  docs/roadmap/160-doctrine-review-owed/790-rule-4-cold-pass-queued-sizescan-cold-content-hatches.md
grep -o '"Own or control"' \
  docs/roadmap/160-doctrine-review-owed/020-the-child-membership-work-locality-cycle-close.md
grep -o '"Add a local rollback check"' \
  docs/roadmap/160-doctrine-review-owed/670-rule-4-cold-pass-queued-ccarchive-hardening.md
grep -o -e '"The approve the report only option for 1 month and then we move to blocking per option 2"' \
  -e '"Bar both"' -e '"Require a stamp by 9 Dec"' \
  docs/roadmap/160-doctrine-review-owed/340-rule-4-cold-pass-queued-the-floor-verbatim-ruling.md
```

The `160/340` sentence beginning *"The approve the report only option"* is his own words; the other
four are answers. His own words on background jobs (`200/030`) are quoted in full in the delta
itself, `docs/method/TOOLBOX.md` § *Background jobs*, so they need no grep. The doctrine the delta
writes (`GUARDS.md`, `PROPAGATION.md`, `CONCURRENCY.md`, `TOOLBOX.md`, `man ccarchive`) states what
it takes these to authorise. Those statements are the author's claims to test.

## What the work is

Nine commits on `main`, landed 2026-11-09 (NZDT stamps; all UTC the same day):

- **`be217b1a`** — `scanners: bar sizescan's report-only lane, close the floor-stamp bypasses (160/790, 160/340)`.
- **`69fe9c3b`** — `doctrine: state the monthly transcript-mining pass; correct "no background jobs" (200/030)`.
- **`606e6dcf`** — `doctrine: membership is repos the principal owns or controls (160/020)`.
- **`169c194c`** — `changelog: the 160/790, 160/340, 160/020 and 200/030 applications`.
- **`7ba836a6`** — `ccarchive: a local rollback check; --rekey verifies first (160/670 HD1-HD3)`.
- **`4694ec4a`** — `pins: report each child's floor copy against the floor at its own pin (160/340 FV3, FV11)`.
- **`2dd4aafd`** — `doctrine: the floor copy and its sources agree; the fleet report named (160/340, 160/290, 160/230, 160/270, 020/215)`.
- **`4170a804`** — `floor: bar a disabled sizescan from 2026-12-09 too (160/340)`.
- **`d1189996`** — `pins: block an unstamped floor copy from 2026-12-09 (160/340)`.

`4170a804` and `d1189996` landed after the commit that queued this pass (`d98697bf`); the pointer
says the pass's delta includes them. `2dd4aafd` also applies findings from passes the pointer does
not name (`160/290`, `160/230`, `160/270` DR2, `020/215`, and `310/130`, `160/310` HF8 by their
doctrine); its paths are on the pointer's list, so all of it is in scope.

Delta paths, read at each commit and at HEAD:

- `tools/floor.py`, `floorfleet.py`, `report.py`, `sizescan.py`, `stampscan.py`, `pins.py`,
  `allowmarker.py`, and `tools/test_` + each of those names (`test_allowmarker.py` exists but is
  not in the delta)
- `instruments/ccarchive`, `instruments/ccarchive.test.js`, `instruments/man/ccarchive.1`,
  `instruments/README.md`
- `docs/method/GUARDS.md`, `PROPAGATION.md`, `CONCURRENCY.md`, `GLOSSARY.md`, `TOOLBOX.md`,
  `00-APEX.md`, `AUTONOMY.md` (all under `docs/method/`)
- `docs/build/templates/CLAUDE.md`, `docs/build/templates/workflows/floor.yml`,
  `skills/session-onramp/SKILL.md`, `tools/README.md`, `.sizescanignore`, `CHANGELOG.md`

`tools/README.md`, `instruments/README.md` and `.sizescanignore` are outside the pointer's path list
and inside the commits, so they are named here. Two board files are in the commits and left out of
the default read: `docs/roadmap/210-instruments-open-features/190-ccarchive-remove-install-schedule.md`
(a dated correction, `69fe9c3b`) and
`docs/roadmap/020-policy-as-code-programme-five-tracks-mik/210-the-three-laws-and-the-zeroth-are-coming-out-o.md`
(`2dd4aafd`). Name one with `--path` only if your own judgement needs it, and disclose that you did.

First confirm the tree holds the delta, then read each commit body-free:

```
git merge-base --is-ancestor d1189996 HEAD; echo $?
for c in be217b1a 69fe9c3b 606e6dcf 169c194c 7ba836a6 4694ec4a 2dd4aafd 4170a804 d1189996; do
  python3 tools/coldsweep.py --root . --commit $c
done
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). With no `--path`, `coldsweep --commit` leaves the board store out, so these lines never show
the intent records.

Then see what has landed on those paths since. At writing, the line below lists twenty-one later commits,
among them `06248fba` (`floor disabled takes an end date`), `ba55be27` and the scanner-coverage
commits. Read anything that bears on this delta at HEAD the same way:

```
git log --oneline d1189996..HEAD -- tools/floor.py tools/floorfleet.py tools/report.py \
  tools/sizescan.py tools/stampscan.py tools/pins.py tools/allowmarker.py instruments/ccarchive \
  instruments/man/ccarchive.1 docs/method/GUARDS.md docs/method/PROPAGATION.md \
  docs/method/CONCURRENCY.md docs/method/GLOSSARY.md docs/method/TOOLBOX.md \
  docs/method/00-APEX.md docs/method/AUTONOMY.md docs/build/templates \
  skills/session-onramp/SKILL.md tools/README.md .sizescanignore
```

**This is an application review.** Rule 2 cannot be fully honoured: the delta's `CHANGELOG.md`
entries, docstrings and commit subjects carry finding IDs and answer labels from the passes it
applies (HX, FV, CM, HD, AK, RR, DR, LR, HF). Review the code and doctrine at HEAD and commit
findings first; open those verdicts after. The residual exposure is named here, not denied
(`REVIEW.md` § *Applying decisions to doctrine*).

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the author's claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1).

- `sizescan` "enforces the board's design (a short main board, each item's detail in its own
  file)", so the principal's *"Never allow it"* bars its report-only form; "a specific 'never'
  beats the general 'declared and expiring'" (`GUARDS.md`).
- From 2026-12-09 an `advisory.sizescan` declaration, "in either spelling and however reasoned or
  dated", and a `disabled.sizescan` entry are config errors and the floor blocks; until then each
  works and every surface names the date (`floor.ADVISORY_BARRED_FROM`, `DISABLED_BARRED_FROM`,
  `floorfleet`, `--json` `barred_from`). "A repo with no board needs no entry: the check passes on
  an empty tree."
- "No marker and no ignore-file glob exempts" the cold-content gate; a glob over a roadmap "exempts
  nothing, and the run names it inert"; a roadmap under a store-named directory is not read and is
  counted.
- `report.safe_text` neutralises control and format characters in the completed-item listing; "the
  other scanners that echo tracked text still do not use it".
- `stampscan` identifies the floor "by the file the stamp's `source=` resolves to, not by how the
  path is spelled"; a `stampscan:allow` marker inside a floor stamp "is ignored"; "a
  `.stampscanignore` glob can still skip a whole file".
- `pins` compares each child's copy "with the floor *as it stood at that child's pin*", with the four
  placeholders put back; "report-only until 2026-12-09 and fails the fleet check from then", for
  `drift`, `unstamped`, `no-reference` and `malformed`; `skipped` and `unchecked` stay report-only.
- "A repo archived on GitHub is exempt": `pins` asks `gh repo view` "only from the date and only
  about a child that would otherwise fail; if that cannot be established the child is not exempt".
- "Nothing in the child's own CI" reaches a child's floor copy, since `stampscan` cannot resolve a
  child's `source=` (`PROPAGATION.md`).
- `ccarchive`: each save carries a save number "bound to that manifest by its own MAC"; "a number
  that does not check is never believed"; an index behind the local record, the same number over a
  different index, or a vanished index with a record is `rolled-back` and refused (exit 2) or
  reported (exit 1); a volume ahead of the record, or no record, "is adopted"; "it does not guard a
  machine whose own state directory is lost or written to".
- `--rekey` "checks the index under the old key and refuses anything but `verified` (exit 2, nothing
  minted or changed)"; `--accept-unverified` "is the deliberate clear and names the state it
  cleared"; "no sequence of rolls brings them all across under one key".
- Membership: "every repo the principal owns or controls, and works an agent in, is an atelier
  child"; a repo he neither owns nor controls "is outside the rule without a ruling"; exclusions are
  recorded "in the estate root's private records", and the rule makes membership "*decidable* …
  not *enumerable*" (`PROPAGATION.md`).
- "An exemption is re-tested when the rule it departs from moves" (`PROPAGATION.md`); a target with
  no queue falls back to the estate root's board, which "adds no permission to write into a repo"
  (`CONCURRENCY.md`).
- The mining pass runs "on the principal's word, about monthly", files board items and "proposes
  changes and never makes them"; "a cloud schedule would not reach the transcripts"
  (`PROPAGATION.md`, `TOOLBOX.md`).
- The floor region and the template stamp are "byte-identical"; the apex names the floor "by
  reference to `AUTONOMY.md` § *Always confirm*", which holds the list once; the onramp skill is "a
  one-line pointer instead of a third hand-kept copy".
- Census claims in `CHANGELOG.md`: two children declare `advisory.sizescan`; "no repo on the machine
  lists" `disabled.sizescan`.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope,
and a non-goal that fences off the risk is a finding.

**Non-goals:** findings the delta says are not yet decided or not applied (`160/670` HD4–HD16,
`160/340` FV4, FV6, FV8, FV9, the rest of `160/290`, `160/230` and `020/215`), except where the delta
claims otherwise; pass `160/1210`'s subject (the estate-root wording, the reader-side fix and the
two-step ask) beyond DR2 as `2dd4aafd` applies it; `13a5a6b2` (`115/020`), landed the same hour;
whether the principal's picks were the right ones, as distinct from whether the delta does what they
authorised; later commits on these paths except as they change this delta at HEAD.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else. Is
   this the right problem, solved at the right altitude and in the right shape, against the
   acceptance test? A dated gate is a design choice: test what it does on the day, to whom, and who
   runs it.
2. **Correctness & quality.** Re-drive the claims above. Record each overclaim against the text that
   makes it. Drive the dated gates on both sides of 2026-12-09 in a scratch copy rather than reading
   them.
3. **Completeness / harvest.** Every surface that states these behaviours (V3): `--help`, man page,
   README, docstrings, `--json`, the child template, the floor region and its stamped copy; one home
   (V4); no contradiction (V5). Find tests that would stay green on a broken delta by mutating a
   scratch copy.
4. **Security & privacy**, mandatory: at design altitude what this exposes, over-collects or leaks
   by weakness of design (a public parent that points at a private register; a pass that reads
   transcripts and files what it finds); at code altitude the likely vectors for its class
   (tamper and rollback of signed state, terminal-escape injection through echoed tracked text, path
   resolution and case-folding, subprocess calls), checked against an open catalogue (OWASP ASVS or
   the domain's equivalent). Aim `/security-review` at code only from a clean tree, as *House rules*
   says; weigh a clean pass over markdown as nothing.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-14 UTC, from the worktree root,
except the `cd tools` line, and its results are held in the sibling. Read exit codes explicitly.
Check `uptime` first and run the heavy lines under `nice -n 10`, one at a time. Use the `python3`
first on the machine's `PATH` (3.14.6 when written); CI pins 3.12.

```
for t in sizescan stampscan floor pins floorfleet report; do python3 tools/$t.py --selftest; echo "$t $?"; done
cd tools && nice -n 10 python3 -m unittest test_floor test_floorfleet test_report test_sizescan \
  test_stampscan test_pins test_allowmarker; echo $?; cd ..
nice -n 10 node --test instruments/ccarchive.test.js; echo $?
mandoc -T lint -W style instruments/man/ccarchive.1; echo $?
nice -n 10 python3 tools/floor.py --plane ci --root .; echo $?
nice -n 10 python3 tools/pins.py --head; echo $?
```

`pins` reads the child repos on the machine, read-only; report them by count only, never by name or
path. `--head` keeps it offline; without it, `pins` runs `git fetch` in your own atelier checkout,
which is allowed. Children's pins are being bumped by other sessions, so its counts move; read them
as of your run. The `CHANGELOG.md` census claims and any other recorded figure you rely on are
recorded proofs (V2): re-run them read-only and by count. The brief-writer did not re-run those.

## House rules for this run

- **Live systems:** read-only reads as needed; no live writes. `pins` may call `gh repo view` (a
  read) for a child that would fail after the date; that is allowed. Never run `ccarchive` against
  a real archive, real key or real state directory: every `ccarchive` probe uses a scratch home and
  scratch volume under your scratchpad, through the test harness or explicit flags. A check that
  needs a live write is marked NOT RUN, with why. No push, no write to GitHub, no network service
  changed.
- **Never print a secret** or any personal data, and never read a session transcript's content to
  probe the mining-pass doctrine: it is doctrine only, with no code. Probes use scratch copies and
  synthetic fixtures under your scratchpad, deleted when you finish.
- Name your own review worktree in the verdict. It is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad. Child
  repos are read-only and reported by count only, never by name or path.
- **Skip the session-log step of the read order** (`CLAUDE.md` step 4; `REVIEW.md` rule 2). If you
  read it anyway, disclose what you met.
- One heavy process at a time, foreground, with a long timeout. Never run an installed tool by bare
  name from `PATH`: use `python3 tools/<x>.py` or `instruments/<x>` from your worktree.
- `/security-review` reads the session's pending diff, not this delta. Aim it at the code by
  reproducing the diff in a scratch clone, or discharge it by grounds and do the code-altitude read
  by hand, never with this brief or its sibling dirty.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo is
  PUBLIC: quote no secret, email address, private repo name or path, and do not join the estate
  root's name to what it holds.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, this brief's sibling
`docs/reviews/2026-11-14-0052-floor-bars-copy-report-rollback-membership-cold.deferred.md` (a
held-back file; by count: 20 questions, 6 facts), every item under
`docs/roadmap/160-doctrine-review-owed/` beyond its title (the grep lines above excepted), every
delta commit's message body, and these intent records beyond their first line:

- `docs/roadmap/200-anti-slop-invariant-registry-promote-rec/030-r1-the-recurrence-count-has-to-become-mechanic.md`
- `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/215-rule-4-cold-pass-queued-laws-removal.md`
- `docs/roadmap/310-pointing-up-the-child-to-parent-route/130-the-parent-holds-accommodations-the-child-cannot-inherit.md`
- `docs/roadmap/420-when-to-ask-mike-commissioned/030-what-the-722a-ruling-round-left-open.md`

`160/790`, `160/020`, `160/670`, `160/340`, `160/290`, `160/230`, `160/270` and `160/310` are under the
barred folder above. The delta's own docstrings, comments, READMEs, man page and `CHANGELOG.md`
entries carry the author's account of why; they are the delta, and reading the delta is never
barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/200-anti-slop-invariant-registry-promote-rec/030-r1-the-recurrence-count-has-to-become-mechanic.md \
  --also-exclude docs/roadmap/020-policy-as-code-programme-five-tracks-mik/215-rule-4-cold-pass-queued-laws-removal.md \
  --also-exclude docs/roadmap/310-pointing-up-the-child-to-parent-route/130-the-parent-holds-accommodations-the-child-cannot-inherit.md \
  --also-exclude docs/roadmap/420-when-to-ask-mike-commissioned/030-what-the-722a-ruling-round-left-open.md \
  'BARRED_FROM|COPY_BLOCKS_FROM|rolled-back|owns or controls|mining pass'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions and the re-run
list. Append your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, any orchestrator, what you read, the UTC day), per-lens answers, V1–V7 each
answered or discharged with grounds, each load-bearing assumption damaged or confirmed with its
probe, a per-commit ledger (read body-free yes/no, findings by id), findings with stable IDs (prefix
`CB`: `CB1`, `CB2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit bodies;
append `### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The work is doctrine by function, so every finding is the principal's to decide (rule 3): record
all, apply nothing. Counsel per finding is welcome, labelled as counsel and kept beneath it.
