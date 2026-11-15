# Cold pass — `pdlistscan`: in a public repo, personal data stands only where the closed list names it

**Board:** `docs/roadmap/160-doctrine-review-owed/1340-rule-4-cold-pass-queued-pdlistscan.md`
**Status:** ACT 1 and ACT 2 RUN 2026-11-15 UTC on Fable 5.1, verdict FAIL (2 MAJOR, 4 MODERATE,
4 minor, 4 notes; PN13 and PN14 formed at reconcile); sibling folded below the verdict
2026-11-15 UTC. Findings are the principal's to decide. Brief written 2026-11-14 UTC by a headless
Opus 5.5 brief-writer (`cclive` lists it as session `fb2c22e6`). Run under the principal's weekly Fable drain order of
2026-11-16 06:53 NZDT (`/fable-drain`).

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4: self-authored guard code that
enforces doctrine (the closed personal-data list), registered in the floor every child inherits,
turning from warning to blocking on a date in code.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Size of this pass:** medium: one commit, 660 added lines, of which 336 are the scanner, 237 its
tests, 35 its README section, 18 its floor registration, 24 a floor contract test and 11 a
`CHANGELOG.md` entry; plus a comparison against the in-suite test it says it repeats.
**Why it earns a review:** this is the guard on the one thing a public repo cannot take back: a
push of personal data. It is a silent-failure surface. A false negative (a listed string or a
personal-data marker standing where no entry names it, while the scanner reports **clean** and
prints a healthy coverage line) manufactures exactly the confidence the closed list exists to
withhold, and it does so in every child that ever declares itself public, because the floor is
where children inherit it. A wrong scope decision does the same thing wholesale: a public repo the
scanner treats as out of scope says "not in scope" and exits 0. A false positive, from 2027-03-08,
is a red floor no flag in the floor's wiring can soften, and the cheapest way past it is to widen a
list entry, which is a grant only the principal may make. The worst failure is a public repo with
personal data in an unnamed place and a green floor.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `d0ca5d24`,
  2026-11-09 UTC, and the worker it dispatched (per the queue pointer). The author queued this pass
  and does not take it.
- **Who wrote this brief:** a headless brief-writer (`claude-opus-5-5`; `cclive` lists it as session
  `fb2c22e6`), started 2026-11-14 UTC by an estate health sweep, orchestrator session `58027096`
  (Opus), on the principal's instruction that a brief is written for every review known to be owed
  (Mike, 2026-11-14, verbatim: *"include all briefs are written where we know a fable review is
  required"*). Neither wrote any of this delta. **Off-tier for review, disclosed: the brief-writer
  forms no finding and writes no severity**, and stops after writing. It ran no review and used no
  Fable model.
- **Barred from running this pass:** session `fb2c22e6` and session `58027096` (whoever writes a
  brief does not run it), and session `d0ca5d24` with everything it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `58027096`: the
  item number, the pointer's opening sentence, and the rules of the sweep. It carried no framing of
  the work. The brief-writer had no contact with the author session or its worker.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md`; the queue pointer whole; **the intent records
  `160/630`, `320/810` and `260/050` whole**, including the author's landing notes and the summary
  of the earlier verdict that `160/630` carries; **the message body of `6607c0eb`** (met through
  `git show`, before the body-free read); the delta through `git show` and `tools/coldsweep.py
  --commit`; commit subjects through `git log`; the head of the unrun brief
  `2026-11-14-0210-blockscan-subsection-edits-cold.md` and its sibling, the commit that landed them,
  and the session record that commit added, all read for house form; and the first 45 lines of the
  brief `2026-11-09-0153-personal-data-closed-list-cold.md`, opened to learn whether it covered this
  subject (it does not: it is `160/1120`'s pass on the list and its in-suite test). It opened **no
  prior verdict** beyond `160/630`'s summary line. Its harness also loaded user-level and repo
  instruction files and a memory index, which hold private context this brief does not carry.
  Everything evaluative it formed is in the sibling.

## The acceptance test

Three sources, one his order and two his answers, and none of them a design:

- **His words** (2026-11-09, quoted in the module docstring, the floor registry comment and the
  first bullet of `320/810`): *"all six, warnings at first and then move to blocking action. With a
  staggered turn on of each so they dont all hit at once"*. That is the order for the check's
  posture: warn first, then block, on a staggered date.
- **His answer on the rule the check enforces** (2026-11-09, to options a queue run offered; an
  answer, not a ruling): *"Honest claim + only you grant"*: personal data in atelier is listed in
  one place, a test keeps the list matching the files, and in a public repo only he grants a
  personal-data exception, in his own words; a marker is not a grant. The rule's text is
  `docs/build/REPO-STANDARD.md` § *Repo-craft conventions* and `docs/PERSONAL-DATA.md`'s preamble.
- **His answer on private repos** (2026-11-09, same shape): *"Ordering the work is permission"*: in
  a private repo, the principal's order for the work is the grant for the personal data that work
  needs. That is why a private repo is out of scope.
- **His answer on visibility** (`260/050`, 2026-11-09, same shape): *"Yes, with the loud alert"*:
  each repo declares its visibility in its floor config, cross-checked against the platform, and a
  says-private-is-public mismatch is red. The scanner leans on that declaration for its scope.

The scanner's design, its three finding kinds, the `tools/` exemption, the date 2027-03-08 and the
claim that this is "the same check" as `tools/test_personal_data.py` are **the run's choices, not
his**; the delta says the date is. Whether they are the right ones is yours to attack.

## What the work is

One commit on `main`. First confirm your tree has it:

```
git merge-base --is-ancestor 6607c0eb HEAD || echo "MISSING 6607c0eb"
```

Nothing may print. If something does, merge `origin/main` into the review branch before starting,
because a tree without the delta has nothing to review. Read it body-free:

```
python3 tools/coldsweep.py --root . --commit 6607c0eb \
  --path tools/pdlistscan.py --path tools/test_pdlistscan.py \
  --path tools/floor.py --path tools/test_floor.py \
  --path tools/README.md --path CHANGELOG.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic
(rule 1). Always pass `--path`. Review each delta path at HEAD too. One later commit touched the
scanner and its tests, the coverage line (`641f017f`, board `115/130`); read it the same way where
it meets this delta, with `--path tools/pdlistscan.py --path tools/test_pdlistscan.py`. Confirm what
has landed since:

```
git log --oneline 6607c0eb..HEAD -- tools/pdlistscan.py tools/test_pdlistscan.py \
  docs/PERSONAL-DATA.md tools/test_personal_data.py
```

On 2026-11-14 UTC that printed only `641f017f`. Read as context, never as the subject: the list
`docs/PERSONAL-DATA.md`, the in-suite test `tools/test_personal_data.py` the scanner says it
repeats, the marker grammar in `tools/allowmarker.py` and `tools/leakscan.py` (the scanner keeps its
own copy), `.atelier-floor.json`, the floor workflow template a child runs, and the visibility
cross-check `260/050` built (find it in `tools/floor.py`).

## What the delta claims (extracted, not evaluated)

- **Scope by declaration.** Only a repo whose `.atelier-floor.json` says `"visibility": "public"` is
  in scope; any other value, no key or no config is out of scope, says so, and exits 0. An
  unparseable config is a broken scan (exit 2).
- **Three finding kinds:** `no-list` (no `docs/PERSONAL-DATA.md`), `unlisted-marker` (a
  `leakscan:allow:<scope>:` whose scope is a personal-data rule, in a tracked file no entry's
  `May stand in` names), `unlisted-holder` (a string an entry pins under `Data`, in a tracked file
  that entry does not name).
- **"The same check" as `tools/test_personal_data.py`**, moved into the floor so a child that goes
  public inherits it.
- **The mechanism exemption:** `tools/` and `instruments/` are not counted when `tools/leakscan.py`
  exists at the root, "the mark of atelier itself"; a child's `tools/` is read like any other path.
- **The date:** until `PERSONAL_DATA_WARN_UNTIL` (2027-03-08, UTC) a finding warns and exits 0; on
  and after it, it exits 1 unless `--warn`. No flag, environment variable or config key moves the
  date. The floor's hook and CI templates carry no `--warn`; only its advisory form does.
- **What it does not see**, stated: unpinned data (a given name, commit headers), unscoped markers
  (left to the leak scanner), and whether a list entry's reason is good.
- **Probes recorded:** 22 of 22 (21 child checkouts and atelier) exit 0 on the landing day
  (2026-11-09 UTC) and with the date patched to the flip; atelier the only repo in scope, with
  0 findings. Tests: 21 at landing.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour on this machine, including how the date and the scope decision reach a child's floor.
The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** the list `docs/PERSONAL-DATA.md` itself, its entries and the in-suite test, except as
the yardstick this scanner claims to match (their own pass is `160/1120`); the five other checks of
`320/810` and their dates; `260/050`'s visibility cross-check beyond what this scanner relies on;
`641f017f`'s coverage line beyond where it wraps this scanner.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, then attack at least
   these by probe:
   - **A1. Scope.** Keying scope to the declared visibility, with no key meaning out of scope, never
     leaves a public repo unguarded: either every public repo declares, or the visibility
     cross-check turns the gap red. (The queue pointer asks this question directly.)
   - **A2. Parity.** The scanner is the in-suite test's check with nothing lost: the same parser,
     glob reading, personal scopes and exemptions, so a tree the test passes and a tree the scanner
     passes are the same trees. Where it differs, the difference is stated and deliberate.
   - **A3. Marker grammar.** Every marker `leakscan` honours as a personal-data excuse is one this
     scanner sees, and nothing `leakscan` ignores (a mention in a code span, a malformed scope) is
     counted against a repo.
   - **A4. Holders.** Matching a pinned string per line, as an exact substring, finds every tracked
     file that holds it, and the files it skips (binary, over 4 MiB, unreadable, the list itself)
     cannot hold a listed string unseen. (The pointer's second question: whether a listed string in
     a file its entry does not name can be missed.)
   - **A5. The exemption.** `tools/leakscan.py` at the root marks atelier and nothing else, and the
     exemption takes away nothing the in-suite test reads.
   - **A6. The list is read as written.** `parse_list` and `ticks` recover every entry, its pinned
     strings and its places from the real list; a heading or bullet written slightly differently
     fails loud, never by dropping an entry or a place silently.
   - **A7. The date.** It flips on the UTC day it names, on every runner, and on that day the floor
     in a public child turns red for a finding; nothing at run time moves it.
   Ask too whether this is the right problem at the right altitude: a floor scanner that reads a
   repo's own list, versus the list's rule living in the stamped floor block, which `160/630`
   leaves open.
2. **Correctness & quality.** Diff the commit; drive the scanner against scratch repos you build,
   public and not, with lists and markers you write, with the date patched both sides of the flip,
   and through `tools/floor.py` on the hook and CI planes as a child would run it. Record each
   overclaim against the text that makes it: the module docstring, the help text, the README
   section, the floor registry's `why` and `Declares`, the exit-code table and the `CHANGELOG.md`
   entry.
3. **Completeness / harvest.** Every surface that states the date, the exit codes, the scope or the
   `--warn` posture says the same thing (V3, V4, V5). The in-suite test checks things the scanner
   does not (a closed set of entries, a named place that no longer holds its string, a named place
   that matches no file): which of these does a public child need, and is their absence said?
   Tests that would stay green on a broken change: mutate the code in a scratch copy, never the
   worktree. Is a fresh fleet probe before the flip recorded anywhere it will be seen?
4. **Security & privacy** — mandatory. The scanner reads every tracked file in the repo it is
   pointed at, follows what `git ls-files` lists, prints paths and finding details, and runs on CI
   over every push in every child. Check that its output never reprints the personal string it
   found (text and `--json`), that every printed field (path and detail alike) goes through the
   same control and bidi escaping as the rest of the floor's output, that a hostile list (globs,
   very long or many `**`) or a hostile tracked path (a symlink out of the tree, a non-UTF-8 name)
   cannot widen what is read or turn into a crash read as clean, and whether a personal-data marker
   or string can be placed where the scanner cannot see it but a reader of the public repo can.
   Weigh against OWASP ASVS input-handling, output-encoding and data-protection items, checked, not
   recalled. `/security-review` reads the session's pending diff, not this delta: aim it only at a
   scratch clone holding the delta as pending changes, or discharge it by grounds.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once on 2026-11-14 UTC, from the worktree
root, in the foreground, under a load average near 5 on 12 cores; its results are held in the
sibling. Read exit codes explicitly. `python3` on `PATH` is 3.14.6 on this machine.

- `cd tools && python3 -m unittest test_pdlistscan` (a few seconds)
- `cd tools && python3 -m unittest test_personal_data` (the yardstick, under a second)
- `cd tools && nice python3 -m unittest test_floor` (the contract test lives here; about three
  minutes under that load: run it alone)
- `python3 tools/pdlistscan.py --selftest; echo $?`
- `python3 tools/pdlistscan.py --root .; echo $?`, and the same with `--json`
- `python3 tools/floor.py --list --root . | grep pdlistscan`
- The recorded probe: 22 repos by exit code, on the day you run and with the date patched to the
  flip. No command is recorded; rebuild it, read-only, and say where your counts differ and why.

Run the tool from your worktree, never by bare name from `PATH`.

## House rules for this run

**Live systems:** none is needed. Child checkouts on this machine may be **read** for the fleet
probe and for which children declare a visibility; reading the platform's visibility of a repo
(`gh repo view --json visibility`) is a read and allowed. Any probe that would write to a real repo,
board, config or CI is **NOT RUN**: build the case in your scratchpad and say which probes you could
not build.

- Never print a secret or a personal string the scanner is built to find, and name no private repo,
  host, client or private path. This repo is PUBLIC; a child seen in the fleet probe is referred to
  by count or type only.
- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions are live on this machine: touch nothing outside your worktree and scratchpad, and delete
  your scratch repos when you finish.
- No git command that writes in the worktree beyond committing this one file at the end of each
  phase (or handing it to an orchestrator to commit). Never mutate the worktree's `tools/`.
- One heavy process at a time, foreground, long timeout, `uptime` first.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Skip the session-log step of the repo's read order: `docs/SESSIONS.md` is barred (below).
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content —
the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only
after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/` (the `160/1120` brief on the list and the 2026-10-04 personal-data
verdict among them), the queue pointer above, this brief's sibling
`docs/reviews/2026-11-14-0238-pdlistscan-closed-list-cold.deferred.md`, the message body of
`6607c0eb`, the intent record
`docs/roadmap/160-doctrine-review-owed/630-rule-4-cold-pass-queued-pii-by-purpose.md` whole (it
carries the earlier verdict's summary and the author's landing note),
`docs/roadmap/320-child-filed-findings-via-pointing-up/810-build-six-checks-warn-first-staggered.md`
beyond its first bullet (the principal's 2026-11-09 words), and
`docs/roadmap/260-sharing-public-since-2026-07-10-adr-0005/050-p3-the-floor-does-not-know-whether-a-repo-is-p.md`
beyond its opening bullet (the question as filed, with his 2026-07-29 words).

The delta's own text carries the author's account of why (the module docstring above all); it is
the delta, and reading the delta is never barred. The acceptance test above quotes his three
answers, so you need not open the records that hold them.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1340-rule-4-cold-pass-queued-pdlistscan.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/630-rule-4-cold-pass-queued-pii-by-purpose.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/810-build-six-checks-warn-first-staggered.md \
  --also-exclude docs/roadmap/260-sharing-public-since-2026-07-10-adr-0005/050-p3-the-floor-does-not-know-whether-a-repo-is-p.md \
  --also-exclude docs/reviews/2026-11-14-0238-pdlistscan-closed-list-cold.deferred.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, the
assumptions A1–A7 and your own, and the re-run list. Append your verdict below a `---` divider in
THIS file: provenance repeated (how you were spawned, your tier, what you read, the UTC day you ran
on), per-lens answers, the standing checklist V1–V7 each answered or discharged with grounds, each
load-bearing assumption damaged or confirmed with its probe, a commit ledger (`6607c0eb`: read
body-free yes/no, findings by id), findings with stable IDs (prefix `PN`: `PN1`, `PN2`, …) and
severities (MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with
counts, a re-run ledger and a follow-up checklist. Then STOP: act 1 is committed, unrevised,
**before** the sibling is opened.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the commit body; append
`### Reconcile` beneath your verdict: per-finding notes against the sibling and the author's
account, any finding formed at reconcile marked as such, and the overall line restated. Never
revise act-1 text. Then fold the sibling in below the reconcile and delete it.

**Who applies a finding.** `pdlistscan` is guard code that enforces doctrine (judged by function,
`REVIEW.md` rule 3): the author applies nothing on its own, and neither does the reviewer. Record
all; the findings are the principal's to decide, after a plain-language account. Counsel per
finding is welcome, labelled as counsel and kept beneath it.

---

## Verdict — act 1, 2026-11-15 UTC

**Overall: FAIL — 2 MAJOR, 4 MODERATE, 3 minor, 3 notes.** The scanner does what its tests say on
the trees its tests build. On the trees the fleet actually holds, and on lists written in any
shape but atelier's, it reports clean where the closed list is not being kept: two public
children sit outside its scope today with a green floor (PN1), and a list it cannot parse reads
as a list with nothing in it (PN2). Both are the failure the brief names as the worst one.

### Provenance

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named review tier, checked at
  selection. Worktree `/Users/mike/worktrees/fable/atelier-160-1340-1952/atelier`, read-only
  to this session except this file; HEAD `a03e6ae5`.
- **Spawn:** a headless orchestrator session (Opus 5.5), itself started by drain session
  `21a271a5` (Opus 5.5). Both are rule-4 off-tier orchestrators holding the context partition:
  they form no finding and write no severity. Neither wrote the brief, the sibling or the delta.
  The barred sessions are `fb2c22e6`, `58027096` and `d0ca5d24` with everything it started; this
  session was started and instructed by none of them. No contact from the author's chain.
- **Authority for Fable time:** the principal's drain order, `/fable-drain` invoked 2026-11-16
  06:53 NZDT; it lapses at the weekly reset (2026-11-15 23:00 UTC) and a pass already running may
  finish. The brief's "waiting on the principal's explicit approval of Fable work" is met by it.
- **The orchestrator's direction, as received** (process only; no question about the delta, no
  pointer at a risk, no request to revise a finding): the item and worktree paths; read the brief
  and `REVIEW.md`; prefix `PN`; the sibling was removed from the worktree on purpose and is not to
  be sought elsewhere; read `6607c0eb` only through `coldsweep --commit --path`; keep a running
  log of checks and evidence at a named user-local file; write only that log and this file; no
  git write; live systems read-only, a write-needing check marked NOT RUN; `/usr/bin/python3`;
  `nice -n 10`, one suite at a time, `uptime` before heavy steps, children probed sequentially;
  refer to orchestrators by session id and to children by count or type only; append act 1
  below a `---` divider and stop; act 2 arrives by message with the sibling's path.
- **What was read.** The brief whole; `docs/method/REVIEW.md` whole; the delta body-free
  (`tools/coldsweep.py --commit 6607c0eb` with the six `--path`s, and `641f017f` with two); at
  HEAD: `tools/pdlistscan.py`, `tools/test_pdlistscan.py`, `tools/test_personal_data.py`,
  `docs/PERSONAL-DATA.md`, `tools/allowmarker.py`, the marker lines of `tools/leakscan.py`, the
  helpers of `tools/report.py`, `tools/floor.py` (the `Scanner` class, the VISIBILITY docstring,
  `check_visibility`, `github_visibility`, the run loop, `advisory_count_rx`),
  `.atelier-floor.json`, both floor workflow files, the `pdlistscan` and `attribscan` sections of
  `tools/README.md`, `CHANGELOG.md` lines 19–29 and 60–100, `docs/build/REPO-STANDARD.md` lines
  200–226, `docs/build/templates/CLAUDE.md` lines 145–162, the date line of `tools/attribscan.py`
  and the three lines of `tools/namescan.py` that use `pdlistscan`. `floor.py --declarations`
  output, whose `pdlistscan` block says "no verdict has read it" and nothing evaluative.
  `coldsweep` listed the two board-store paths `641f017f` touched by name; neither was opened.
  **Not opened:** the sibling, `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, any
  prior verdict, the four barred board items, the commit body. The onramp's session-log step was
  skipped (rule 2). Every sweep ran through `coldsweep` with the brief's five `--also-exclude`s;
  `--include-barred` was not used.
- **Exposure, disclosed.** The fleet probe put every child's path and name in this session's
  context (not in any record). The harness loaded user-level instruction files and a memory
  index that hold private context; none of it bears on this delta.
- **Environment.** `/usr/bin/python3` is 3.9.6, and the yardstick `tools/test_personal_data.py`
  fails to import on it (`str | None` at line 52 with no `from __future__` import). `python3` on
  `PATH` is 3.14.6, as the brief says; every suite below ran on 3.14.6. `pdlistscan.py` itself
  carries the future import and ran on both.
- **Load:** 5–10 on 12 cores throughout; every suite under `nice -n 10`, one at a time.

### Commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `6607c0eb` (the delta) | yes, `coldsweep --commit`, six `--path`s | PN1–PN12 |
| `641f017f` (coverage line, `115/130`) | yes, two `--path`s | none of its own; PN7 touches it |

Nothing else has landed on the four paths since (`git log 6607c0eb..HEAD -- …` printed only
`641f017f`).

### Re-run ledger

| Line | Result |
|---|---|
| `test_pdlistscan` | 24 tests OK, 5.3 s (also 24 OK on 3.9.6) |
| `test_personal_data` | 11 tests OK, 0.9 s on 3.14.6; import error on 3.9.6 (above) |
| `test_floor`, alone | 255 tests OK, 271 s; the worktree untouched after (`git status`) |
| `pdlistscan.py --selftest` | `selftest OK`, exit 0 |
| `pdlistscan.py --root .` | clean, advisory 0, coverage 1283 files · 188823 lines, exit 0 |
| same, `--json` | `clean: true`, `in_scope: true`, exit 0 |
| `floor.py --list --root . \| grep pdlistscan` | `pdlistscan enforced fleet decl 2/5 …` |
| fleet probe, today | 23 roots (22 children + atelier's main checkout): 23/23 exit 0 |
| fleet probe, date patched to the flip | 21/23 exit 0, **2 exit 1** (PN5) |

The fleet probe was rebuilt as a read-only script over `floorfleet --json`'s child list, one
child at a time, each run twice (the worktree's scanner, then a scratch copy with the date set
to 2000-01-01), with `gh repo view --json visibility` per child. Where my counts differ from the
record: the record had 22 roots and atelier the only repo in scope; today there are 23 roots and
three in scope, because two children have declared `"visibility": "public"` since 2026-11-09.
Each of the two has no `docs/PERSONAL-DATA.md`, so each carries one `no-list` finding that warns
today and blocks at the flip. GitHub says public for four children: those two, and two that
declare no visibility key at all (PN1).

### Lens 1 — approach and assumptions

The problem is the right one: a test in atelier's suite reaches no child, and the floor is where
a child inherits a guard. The altitude is defensible too: the list is per repo, so a floor
scanner reading each repo's own list is the right shape, and the alternative `160/630` leaves
open (the rule living in the stamped floor block) would still need a per-repo list of places.
What the design does not carry is the list's grammar (PN2) and the rule's text (PN4): the
scanner enforces a file shape no document outside atelier's own list states, and a condition
("the file must exist") the standard says the opposite of.

Load-bearing assumptions, named by me and then the brief's, each with its probe:

- **A1. Scope by declaration — DAMAGED, live.** The fleet probe found two children GitHub
  reports public with no `visibility` key: `pdlistscan` prints "not in scope" and exits 0 in
  both. The cross-check does not turn the gap red: `check_visibility` returns a 🟡 partial for
  "nothing declared", by design (`floor.py` docstring: "nothing declared … never block"), and
  `main` calls `github_visibility()` only when `cfg.visibility` is set, so the floor never learns
  those repos are public. Neither half of the assumption holds. → PN1.
- **A2. Parity with the in-suite test — DAMAGED.** Same parser, globs and scopes, but not the
  same exemption or the same reads: the test exempts `tools/` and `instruments/` for markers
  only and reads holders everywhere (PD1 names three `tools/` files); the scanner skips both
  kinds under both prefixes. The scanner also skips files over 4 MiB, which the test does not.
  The three checks the test makes that the scanner does not (closed set, stale place, place
  exists) are not named in "what it does not see". → PN3, PN7.
- **A3. Marker grammar — DAMAGED.** A mention inside a code span is a marker to `pdlistscan` and
  not to `leakscan` (probe P1: `unlisted-marker`); the unscoped form, which `leakscan` honours
  as an excuse for an email or a phone number, is the one form `pdlistscan` never reads (probe
  P2: both scanners clean). Case and underscore differences are inert because `leakscan`'s
  compare is case-sensitive. → PN6.
- **A4. Holders — DAMAGED, minor.** Exact-substring-per-line finds every holder the scanner
  opens; the files it skips can hold the string unseen: a 4.5 MiB text file, a file with one NUL
  byte and a UTF-16 file each held it and the run was clean, with no skipped count on the
  coverage line (probe P8). → PN7.
- **A5. The exemption — DAMAGED.** `tools/leakscan.py` at the root marks any repo that has a
  file by that name: a one-line stub in a public scratch repo switched the scan off over
  `tools/` and `instruments/` (probe P5). It also takes away something the in-suite test reads
  (A2). → PN3.
- **A6. The list is read as written — DAMAGED.** Five shapes (`### PD1 —`, `## PD1—x`,
  `- **Data**: `, `## pd1 —`, an empty list) each parsed to zero entries and the run was clean
  while a stray holder stood in `docs/` (probe P3). Nothing fails loud. → PN2.
- **A7. The date — CONFIRMED.** `warn_only_today` compares the UTC date strictly before the
  constant (`test_the_date_is_read_strictly_before`); a scratch copy with the date in the past
  exits 1 and `--warn` exits 0 (P12); through `floor.py --plane hook` and `--plane ci` on a
  public scratch repo, the real tools gave `rc 0, advisory 2` and the flipped copy `rc 1` on
  both planes; neither template carries `--warn`; the advisory form does. Nothing at run time
  moves it.

### Lens 2 — correctness and quality

The code is small, stdlib-only and readable, and on its own fixtures it is right: the tests
pin scope, the three kinds, the exemption, untracked files, the date, `--warn` and the JSON
shape, and `test_floor` pins the count contract on both sides. Where it departs from its claims:

- **"This is the same check"** (docstring, README, CHANGELOG): not the same exemption, not the
  same reads, and three of the test's checks absent and unsaid (PN3, PN7).
- **"the exemption `tools/test_personal_data.py` makes"** (docstring): the test's exemption is
  for markers only (PN3).
- **"No child declares itself public with a list yet, so today it reads only atelier: 21
  children are out of scope, and atelier is clean"** (README, a live surface) and **"Atelier is
  the only repo in scope"** (CHANGELOG): true on 2026-11-09, false at HEAD on 2026-11-15 (PN5).
- **"an unparseable config … is a broken scan (exit 2)"** (README exit-code table): true for
  JSON that does not parse; a config whose `visibility` is `"Public"` or `"internal"` is read
  as out of scope and exits 0 when the scanner runs alone, while `floor.py` refuses it (PN9).
- The help text, the `why`, the `Declares` block and the exit-code table otherwise agree with
  the code.

### Lens 3 — completeness and harvest

- The date, the exit codes, the scope and the `--warn` posture say the same thing on every
  surface that states them (`pdlistscan.py`, `tools/README.md`, `CHANGELOG.md`, `floor.py`'s
  registry): 2027-03-08 throughout, four weeks after `attribscan`'s 2027-02-08 as stated.
- Of the in-suite checks the scanner lacks, a public child needs the **closed set** most: it is
  what makes a list that parses to nothing fail instead of pass (PN2). The stale-place and
  place-exists checks are hygiene a child can live without; their absence should be said.
- Tests that stay green on a broken change: removing the continuation-line join in
  `parse_list` passes all 24 tests and yields 78 findings on the real list (PN8). Removing the
  `rel == LIST_PATH` skip fails two tests (caught).
- A fresh fleet probe before the flip is recorded nowhere a reader will meet it: the README's
  sentence is a snapshot with no date, and it is already wrong (PN5).
- Harvest: `report.with_id` / `finding_dicts` give ten scanners namespaced finding IDs; this one
  prints `[unlisted-marker]` and emits no `id` (PN11). `leakscan.parse_allow` and
  `allowmarker.blank_code_spans` already exist and are not used (PN6). The mirror sweep: every
  registry scanner but `board` has a README section; the standard and the child template say
  the opposite of the scanner on a missing list (PN4) and do not mention the floor check.

### Lens 4 — security and privacy

Weighed against OWASP ASVS 5.0 (fetched, not recalled: V1 encoding, V2 validation, V5 file
handling, V14 data protection, V16 logging; the items named below).

- **The personal string is never reprinted** (16.5.1, 16.2.5): the text output names the entry
  id and the marker's scope only, and the JSON carries the same fields; probe P11 checked both
  outputs by substring. ✅
- **Output encoding** (16.4.1, log injection): the detail goes through `report.safe_text`; the
  **path does not**, and a path carrying a bidi override reached the terminal raw (P7b). The
  same is true of `leakscan`'s finding line, so this is a floor-wide class, noted here (PN10).
  JSON output is escaped by `json.dumps`.
- **Hostile paths** (5.3.2): a tracked symlink to a file outside the tree is followed and read,
  and a listed string in it is reported by the symlink's path (P6): a widening of what is read,
  bounded by the repo's own commit. Dangling and directory symlinks skip without a crash. A
  non-UTF-8 tracked name could not be built here (APFS refuses it, NOT RUN); by code,
  `tracked()` decodes strictly, so it would raise and `guarded_main` would print a traceback and
  exit 2: fail closed, noisy (PN10).
- **Hostile list** (1.3.12, 5.2.1): forty `**/` segments matched in 0.18 s, correct result; the
  globs are compiled with `re.escape` on every literal; files over 4 MiB are not read (the
  limit that also makes PN7). No ReDoS reachable from the list.
- **Where a reader of the public repo sees what the scanner cannot:** the skipped files of PN7;
  anything under `tools/` or `instruments/` in a repo with a `tools/leakscan.py` (PN3); a line
  excused by an unscoped marker (PN6); any repo GitHub shows public that declares no visibility
  (PN1). These are the privacy findings of this pass; each is a design gap before it is a code
  one.
- **`/security-review`: NOT RUN, discharged by grounds.** It reads the session's pending diff,
  which here is the orchestrator's deletion of the barred sibling, so running it would feed
  deferred material into this pass (the SL2 class); the delta is landed, not pending; and the
  scanner excludes markdown, so its pass over the doc surfaces would be empty.

### The standing checklist

- **V1** No claim stronger than its evidence: breached on four surfaces, PN3 (same check; the
  test's exemption), PN5 (fleet state), PN9 (exit-code table).
- **V2** Re-run every recorded claim: done, ledger above; the fleet probe no longer reproduces
  (PN5); the 21 tests at landing are 24 at HEAD, all green.
- **V3** A changed rule swept to every mirror: the scanner's rule (a public repo must carry the
  list) reached neither `REPO-STANDARD.md` nor the child `CLAUDE.md` template, which say the
  opposite (PN4); the standard does not name the floor check beside "a test keeps it".
- **V4** One fact, one home: `PERSONAL_SCOPES`, `MARKER_RX`, `glob_rx`, `ticks` and
  `parse_list` are a second copy of the yardstick's (declared in the docstring: "the scanner
  keeps its own copy"), and the marker grammar is a third copy beside `allowmarker` (PN6). The
  date has one home with stamped mentions. Noted under PN6; no separate finding.
- **V5** No internal contradiction: the standard says a missing list means no exceptions; the
  scanner says it is a finding (PN4). Cross-references checked for the rule reached:
  `260/050`'s check is in `floor.check_visibility` and does what the docstring says, which is
  less than the brief's A1 assumed (PN1).
- **V6** Security and privacy: lens 4 above; `/security-review` discharged with grounds.
- **V7** Spawn provenance: stated in the brief and repeated above.

### Findings

Severities: MAJOR / MODERATE / minor / note. Each is the principal's to decide (`REVIEW.md`
rule 3: guard code that enforces doctrine); counsel is labelled and kept beneath.

**PN1 — MAJOR. A public repo that declares no visibility is unguarded, and the floor never
reds the gap.** `declared_public` returns false for a missing key, so the scanner says "not in
scope" and exits 0. `floor.check_visibility` returns a 🟡 partial for "nothing declared" and
never red, and `floor.main` asks GitHub only when a declaration exists, so the floor cannot
even see that the repo is public. Live on 2026-11-15: two children GitHub reports public
declare no key; both print "not in scope", exit 0, and have no `docs/PERSONAL-DATA.md` (with
scope forced on a scratch copy, each reports `no-list`). The brief's A1 ("either every public
repo declares, or the cross-check turns the gap red") is false on both halves. The CI plane
already has GitHub's answer for free (the event payload `github_visibility` reads).
*Counsel:* on the CI plane, treat GitHub-says-public as in scope (the floor passes the
scanner `--public`, or the scanner reads `GITHUB_EVENT_PATH` itself), or make "undeclared and
GitHub says public" red in `check_visibility`; on the hook plane, which has no network, the
declaration stays the key and the README should say so plainly.

**PN2 — MAJOR. A list the parser cannot read is a list with nothing in it, and the run is
clean.** `parse_list` keys on `## PDn ` and `- **Field:**` exactly; `### PD1 —`, `## PD1—x`,
`- **Data**: `, `## pd1 —` and an empty file each parsed to zero entries, and a public scratch
repo holding the pinned string in `docs/` reported clean with a healthy coverage line (probe
P3). Nothing fails loud: no stderr, exit 0. The in-suite test's closed set (`EXPECTED_IDS`)
catches this for atelier; the floor has no equivalent, no child has a list yet, and no template
or document outside atelier's own list states the grammar, so the first child list will be
hand-written from `REPO-STANDARD.md`'s prose, which names the fields and not their spelling.
*Counsel:* an in-scope list that parses to zero entries, or an entry with no `Data` or no
`May stand in`, is a broken scan (exit 2, `ConfigError`), not a clean one; print the entry and
pinned-string counts on the coverage line; ship a `docs/PERSONAL-DATA.md` template with
`create-repo`.

**PN3 — MODERATE. The mechanism exemption is wider than the yardstick's, is keyed on a
one-line file, and "the same check" overclaims.** The in-suite test exempts `tools/` and
`instruments/` for markers only and reads holders everywhere (PD1 names three `tools/` files,
which the test holds to account); the scanner skips both kinds under both prefixes, so a listed
string in an unnamed `tools/` or `instruments/` file is seen by atelier's suite and not by the
floor. The key is `tools/leakscan.py` existing: a `# stub` by that name in a public scratch
repo switched the scan off over both prefixes (probe P5). The docstring's "the exemption
`tools/test_personal_data.py` makes" is not what the test makes, and "the same check" (docstring,
README, CHANGELOG) is not the same on reads, exemption or the three checks it lacks (closed set,
stale place, place exists), whose absence "what it does not see" does not state.
*Counsel:* exempt markers only, as the test does; key the exemption on the floor telling the
scanner it is scanning atelier (or drop it and name the fixture files in atelier's list); add
the three missing checks to "what it does not see".

**PN4 — MODERATE. The scanner and the standard disagree on a missing list.**
`REPO-STANDARD.md` § personal data: "A repo with no such file holds no exceptions"; the child
`CLAUDE.md` template: "a repo without that file holds none". The scanner makes the missing file
a finding (`no-list`) that blocks a public repo from 2027-03-08, and returns before reading
anything else, so markers in such a repo are never reported (probe P13; coverage 0 files,
"scanned nothing", `in_scope: true`). Live: both declared-public children carry exactly this
finding and nothing else has been read in either. One of the two texts is wrong.
*Counsel:* if the rule is that a public repo must carry the list even when empty, sweep the
standard and the template and say why (the file is where "none" is written down); if the rule
stays, treat a missing list as zero entries and scan markers anyway. Either way, do not return
before the markers are read.

**PN5 — MODERATE. The recorded fleet state is stale on a live surface, and the flip has no
dated probe ahead of it.** README: "No child declares itself public with a list yet, so today
it reads only atelier: 21 children are out of scope, and atelier is clean"; CHANGELOG: "Atelier
is the only repo in scope". On 2026-11-15: 22 children, two declared public and in scope, each
with one finding that exits 1 with the date patched to the flip. The recorded 22/22 at the flip
is 21/23 now. Nothing on the board or in the README names a probe to run before 2027-03-08.
*Counsel:* the README drops the fleet sentence (a README is not a probe record) or dates it;
a dated fleet probe goes on the board before the flip, as the brief's lens 3 asks.

**PN6 — MODERATE. The marker grammar is a third copy and differs from `leakscan` in both
directions.** (a) A mention inside a code span counts: "Write `leakscan:allow:email: why`" in a
public child's docs is an `unlisted-marker` (probe P1), where `leakscan` blanks code spans
(AM3). In atelier today the two such mentions outside `tools/` sit in `CHANGELOG.md`, a named
place, so no false positive yet. (b) The unscoped form `leakscan:allow: <reason>` exempts every
structural rule in `leakscan`, including `email`, `nz-phone` and the rest of `PERSONAL_SCOPES`
bar `local-term`, and is the one form `pdlistscan` never reads: an email with an unscoped marker
in a public repo passed both scanners with no entry naming the file (probe P2). The docstring
names (b) a non-goal ("the leak scanner's to judge"); the leak scanner judges the shape, not the
grant, so the non-goal fences off the risk the guard exists for. (c) `[a-z0-9,-]` against
`allowmarker`'s `[A-Za-z0-9_-]`: inert, since `leakscan`'s compare is case-sensitive (P14).
*Counsel:* use `leakscan.parse_allow` (already imported by the test and by `namescan`) and
`allowmarker.blank_code_spans`; count an unscoped marker as a personal-data marker when the
line also matches a personal structural rule, or at least print how many stand in unnamed files.

**PN7 — minor. Skipped files can hold a listed string unseen and uncounted.** A 4.5 MiB text
file, a file with a NUL byte and a UTF-16 file each held the pinned string; the run was clean
and the coverage line said "1 tracked file(s) opened" with no skipped count (probe P8). The
yardstick has no size cap. *Counsel:* print `K skipped (binary, oversize)` on the coverage line
and scan oversized text in a streaming pass.

**PN8 — minor. The tests stay green on a broken parser.** Removing the continuation-line join
in `parse_list` passes all 24 tests; against the real list it yields 78 findings, because every
real entry wraps `May stand in`. No fixture wraps a field. *Counsel:* wrap one field in the
fixture `LIST`.

**PN9 — minor. The scanner alone accepts any visibility value silently.** `"Public"`, `"PUBLIC"`
and `"internal"` read as out of scope, exit 0 (probe P10); `floor.py` refuses them as a config
error. The README's own usage lines run the scanner alone. *Counsel:* raise `ConfigError` for a
value outside `floor.VISIBILITIES`.

**PN10 — note. Output and path handling.** Finding paths are printed raw (a bidi control in a
path reached the terminal, P7b); the detail goes through `safe_text`. `leakscan` prints paths
the same way, so this is a floor-wide class. A tracked symlink to a file outside the tree is
read and reported by the symlink's path (P6); a non-UTF-8 tracked name would raise in
`tracked()` and exit 2 with a traceback (by code; NOT RUN, APFS refuses the name).

**PN11 — note. No namespaced finding ID.** Ten scanners use `report.with_id` and
`finding_dicts`; this one prints `[unlisted-marker]` and its JSON has no `id`. `attribscan`
shares the gap, so it is a `320/810`-slice pattern rather than this delta's alone.

**PN12 — note. Altitude.** A floor scanner reading each repo's own list is the right shape;
what the design did not carry across is the list's grammar (PN2) and the rule's text (PN4).
`160/630`'s open alternative would not remove either need.

### Follow-up checklist

- [ ] PN1 — the principal's call on scope: declaration, or GitHub's answer where the plane has
      it. Then `floor.py` and/or `pdlistscan.py`, README, docstring, a test per plane.
- [ ] PN2 — zero-entry and malformed-entry lists fail closed; entry counts on the coverage
      line; a list template for children.
- [ ] PN3 — exemption narrowed to markers and keyed on atelier itself; "same check" and "what
      it does not see" corrected.
- [ ] PN4 — one rule on a missing list, swept to `REPO-STANDARD.md` and the child template;
      no early return before markers are read.
- [ ] PN5 — README fleet sentence removed or dated; a dated fleet probe boarded before
      2027-03-08.
- [ ] PN6 — marker reading through `leakscan.parse_allow` with code spans blanked; a decision on
      the unscoped form.
- [ ] PN7, PN8, PN9 — coverage skipped count; a wrapped fixture field; refuse unknown
      visibility values.
- [ ] PN10, PN11 — floor-wide: path escaping and finding IDs, boarded against the class, not
      this scanner alone.
- [ ] Act 2: open the sibling and the barred records, screen the commit body, append
      `### Reconcile`.

### Reconcile — act 2, 2026-11-15 UTC

Written after act 1 was committed unrevised as `84428ec7` on `main`. Opened at this step: the
held sibling (the orchestrator's release message named its path, a user-local held copy outside
the worktree; "Act 1 is committed and pushed … Act 2 may begin now … You may now read the held
sibling, this one file"), the commit body of `6607c0eb`, the queue pointer `160/1340`, the
intent records `160/630`, `320/810` and `260/050` whole, the 2026-10-04 personal-data verdict
(its heads and PI1/PI2), the head of the unrun `160/1120` brief, the `160/1180` pointer,
`docs/SESSIONS.md` line 355 and the author's session record of 2026-11-09. The author's own
account of this slice is the commit body and the module docstring; the session record names
`pdlistscan` in one list line and says nothing of its design. Nothing in act 1 is revised.

**The sibling.** Fourteen questions and a run ledger; the brief-writer probed none past what it
recorded. Eleven of the fourteen land on findings act 1 formed independently (Q1/Q2 → PN1 and
PN5; Q3/Q4 → PN3; Q5 → PN6; Q6 → PN7; Q9 → PN2; Q10 → PN10; Q11 → the V4 note; Q12, Q13, Q14 →
confirmed, no finding). Two it asked that act 1 did not raise, Q7 and Q8, are taken up below as
findings formed at reconcile, one of them probed. Its fleet count differs from mine by one
declaration (it saw 6 private / 3 public / 12 none on 2026-11-14; I saw 7 / 2 / 12, plus 2 with
no config, across 22 children on 2026-11-15); which root moved is not recoverable from a count,
and nothing turns on it.

**The commit body.** It says "the same check in the floor" (PN3), "22 of 22 exit 0, atelier the
only repo in scope, with 0 findings" (PN5: true on the landing day, false at HEAD), "Tests: 21"
(true then; 24 at HEAD after `641f017f`), and nothing the docstring does not already say. It
carries no account of why a missing list is a finding (PN4) or why an undeclared repo is out of
scope beyond "a repo declaring anything else is out of scope and says so".

Per finding:

- **PN1 (MAJOR) stands.** The sibling's Q1 and Q2 ask the same question from both sides. The
  author's account chose the declaration knowingly: `160/630` records "a scanner that enforces
  the closed list … would need a per-repo visibility key", and `260/050`'s landing note says a
  missing declaration "only warn[s], so no child turns red". Neither record weighs the case the
  fleet now holds, a public repo with no key; `260/050` itself asked for "a stale declaration
  is itself a finding", and an absent one is the stalest. The queued pass `160/1180` carries the
  overlapping question "whether the cross-check can pass while a repo is public"; the principal
  should rule on PN1 with that pointer in front of him, and whichever pass lands first should be
  cited by the other (`REVIEW.md` rule 3, AR8).
- **PN2 (MAJOR) stands.** The sibling's Q9 asks "which way does each failure fall: loud or
  silent"; probe P3 answered: silent, all five shapes. Q4 adds that an empty or reason-less list
  passes; it does. No record states the list's grammar for a child.
- **PN3 (MODERATE) stands.** Q3 is the finding in the brief-writer's words, read from the code
  and unprobed; P5 probed it. The body and README both carry "the same check".
- **PN4 (MODERATE) stands.** No sibling question and no record touches it: `160/630`, `320/810`
  and the body treat a missing list as a finding without noticing the standard's "A repo with no
  such file holds no exceptions". The 2026-10-04 verdict's PI2 route ("in a public repo an
  exception is the principal's to grant … and the list") is what the standard's sentence
  implements, so the scanner's `no-list` is the newer reading and the standard the older; one of
  them has to move, and it is his call which.
- **PN5 (MODERATE) stands, narrowed.** The sibling's Q1 confirms the fleet had already moved by
  2026-11-14. `320/810` carries an open bullet, "What remains: the flips and their probes … Each
  flip needs a fresh fleet probe before its date", so the obligation is on the board, undated.
  What stands is the README's stale fleet sentence on a live surface, and that the bullet names
  no date and no owner. Counsel unchanged.
- **PN6 (MODERATE) stands.** Q5 names the code-span and reason-less cases and says the other
  direction "was not probed"; P2 probed it and found the unscoped form passes both scanners.
- **PN7 (minor) stands.** Q6 is the same finding; it adds the line-wrapped and different-case
  cases, which the yardstick shares and which act 1 left unraised on that ground. Noted, not
  widened.
- **PN8, PN9 (minor) stand.** No sibling counterpart.
- **PN10 (note) stands; Q10's question answered.** `guarded_main` turns the strict-decode error
  into a traceback and exit 2, not into anything read as clean.
- **PN11, PN12 (notes) stand.** `160/630` keeps "whether the rule moves into the stamped floor
  block" open, which is PN12's altitude question, unchanged.

**Formed at reconcile** (from the sibling's Q7 and Q8; marked as such):

**PN13 — minor, formed at reconcile. The hook plane reads the working tree, not the index.**
`read()` opens the path on disk for every file `git ls-files` lists. Probed on a public scratch
repo: a listed string staged in `docs/note.md` and then reverted in the working copy ran
clean, so the commit would carry it unseen by the hook; the reverse (in the working tree, not
staged) was reported against a commit that does not carry it. The CI plane runs on the pushed
tree, which is the commit, so the backstop holds; the hook's cover is the one that is off by one.
The floor registry's comment says "a file named by the list can change without the diff saying
so", which is why the whole tree is read; reading it from the index (`git show :<path>`) on the
hook plane would keep that and close the gap. *Counsel:* on `--staged`, read blobs from the
index as the other hook-plane scanners do.

**PN14 — note, formed at reconcile. Any entry's place licenses any personal-data marker.** The
marker check matches a file against the union of every entry's `May stand in`, so a marker
excusing an email passes in a file named only by the account-name entry. The yardstick does the
same, and in atelier PD1 names `docs/roadmap/**` and `docs/reviews/*.md`, so every personal-data
marker in the record stores passes on PD1's grant. Not a defect in parity terms; a design
question for the list's owner: whether a place licenses a marker for data its entry does not
hold.

**Overall, restated: FAIL — 2 MAJOR, 4 MODERATE, 4 minor, 4 notes** (PN1–PN12 from act 1
unchanged; PN13 minor and PN14 note formed at reconcile). The two MAJORs are the principal's to
decide after a plain-language account; nothing is applied by this pass. The sibling is left in
place for the orchestrator's fold.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-15)

*Released to the reviewer only after its act-1 findings were committed (`84428ec7`); folded here
verbatim (headings demoted two levels) and the sibling file removed, per the brief. The
orchestrator, a headless Opus 5.5 session started by drain session `21a271a5`, formed no
finding and wrote no severity.*

### Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-14-0238-pdlistscan-closed-list-cold.md` (`REVIEW.md` rule 1).
Written 2026-11-14 UTC by the brief-writer (`cclive` lists it as session `fb2c22e6`), which
authored none of the delta. Open this only after act 1 is committed. Everything here is a floor,
never a fence, and none of it is a finding: the brief-writer read the code once and probed none of
these past what is recorded below.

#### The brief-writer's own questions

1. **The fleet has moved since landing.** The docstring, the README section and the commit say no
   child declares itself public with a list, so for now the scanner reads only atelier. On
   2026-11-14 UTC, by a read-only count of `.atelier-floor.json` across this machine's child
   checkouts: 6 declare `private`, 3 declare `public`, 12 declare nothing. Each of the three public
   ones was in scope on 2026-11-14 with one `no-list` finding, warning and exit 0. On 2027-03-08
   each turns red unless a list is written, and a list entry is a grant only the principal makes.
   Is anything set to tell him before the date (A7, V1)? And are the 12 with no declaration all
   truly private (A1)?
2. **No key, no scope.** `260/050`'s cross-check, per its landing note, only warns on a missing
   declaration and is red only for says-private-is-public. So a public repo that never declares
   is out of scope here and only warned about there. Is the pair loud enough for the one breach
   that cannot be retracted (A1)?
3. **The exemption is wider than the test's.** `tools/test_personal_data.py` skips `tools/` and
   `instruments/` only when looking for markers; it reads them for listed strings, and atelier's
   list names files under `tools/` as places. The scanner skips those paths for both kinds. In
   atelier, a listed string added to an unnamed file under `tools/` is caught by the test and not
   by the scanner. Is "the same check" true (A2, A5, V1)?
4. **What the test checks and the scanner does not**: a closed set of entries (the test pins the
   IDs), an entry naming a place that no longer holds its string, a named place that matches no
   tracked file, and every entry carrying `Why held` and `Granted by`. In a child the list is the
   only record of a grant, and an empty or reasonless list passes the scanner. Deliberate, and is
   it said (A2)?
5. **Two marker grammars.** The scanner's `leakscan:allow:([a-z0-9,-]+):` is its own; `leakscan`
   builds its marker from `tools/allowmarker.py` (scope list `[A-Za-z0-9_-]+(,…)*`, optional
   whitespace, a reason that must start with a word or quote character, and code spans blanked so a
   mention is not a marker). So a marker mentioned inside backticks in a doc counts here and not
   there, and a reason-less marker, which `leakscan` treats as a mention, counts here too. The other
   direction (a marker `leakscan` honours that this scanner misses) was not probed (A3).
6. **Per-line, case-sensitive matching.** A pinned string wrapped across a line break (a two-word
   name in reflowed Markdown), or in a different case, is not seen; the in-suite test reads the
   whole text with the same case sensitivity, so the line-wrap case is not new, but is it said
   (A4)? Files over 4 MiB, binary files (a NUL byte), files missing from the working tree and the
   list itself are skipped with nothing reported; the coverage line counts only what was opened.
7. **Which tree the hook reads.** The scanner reads the working-tree copy of each path `git
   ls-files` lists, not the index. On the hook plane, a staged string removed from the working tree
   before committing is not seen, and an unstaged one is reported against a commit that does not
   carry it. The floor's window says "the tracked files … whole tree"; is that the commit (A4)?
8. **Any entry licenses any marker.** A personal-data marker is accepted in a file named by any
   entry's `May stand in`, not only the entry that holds the data the marker excuses. The test does
   the same. With one broad entry (atelier's account-name entry names `docs/roadmap/**` and
   `docs/reviews/*.md`), any personal-data marker in those stores passes. Intended?
9. **The parser fails quiet.** `parse_list` starts an entry only on `## PD<digits> ` (a space after
   the number). A heading written `## PD6:` or `### PD6 —` is not an entry; its bullets are folded
   into nothing, its strings are never checked and its places never license anything. A
   `May stand in` token that is prose (atelier's given-name entry) becomes a glob that matches no
   path. Which way does each failure fall: loud or silent (A6)?
10. **Output escaping.** `render` passes `detail` through `report.safe_text` but prints `f.path`
    raw. A tracked path with a control or bidi character is printed as is. `tracked()` decodes
    `git ls-files -z` output as strict UTF-8, so a non-UTF-8 path raises; does `guarded_main` turn
    that into exit 2 or into something read as clean? A tracked symlink is followed by `read()` out
    of the tree. The detail never echoes the matched string, which looks right.
11. **Duplicated code, two homes.** The scanner carries its own copies of `glob_rx`, `ticks`,
    `parse_list`, `PERSONAL_SCOPES` and `MECHANISM_PREFIXES` from the in-suite test (only the scope
    set is pinned against `leakscan`'s real rules, and only in the scanner's tests). A change to one
    copy reaches the other only by hand (V4).
12. **The date's order.** 2027-03-08 is four weeks after `attribscan`'s 2027-02-08, as stated; the
    other dated slices fall on 2027-01-11, 2027-05-03 and 2027-05-31, and slice 4 has no date. The
    floor's hook and CI templates pass no `--warn`; the advisory template does. The floor registry
    declares the grounding `Unmet` ("no test names the incident"). Worth a line?
13. **The test count.** The commit says 21 tests in `test_pdlistscan`; `def test_` counts 21 at
    `6607c0eb` and 24 at the brief's base (the three later ones are `641f017f`'s coverage tests).
    The floor contract test was "215 total there"; the brief-writer's run reports 255 at its base,
    which includes later commits, so not comparable without a run at `6607c0eb`.
14. **The `CHANGELOG.md` placement.** The entry sits under an empty `blockscan` heading that already
    stood bare before this commit (checked at `6607c0eb~1`), so the bare heading is not this
    delta's; the entry is headed 2026-11-09, the UTC day of the commit (02:52 +1300 on 2026-11-10
    local).

#### What the brief-writer ran, and what it got

All from the worktree root on 2026-11-14 UTC (base `8c06ad60`), foreground, load average about 5
on 12 cores.

- `git merge-base --is-ancestor 6607c0eb HEAD`: exit 0.
- `python3 tools/coldsweep.py --root . --commit 6607c0eb --path …` (the brief's six paths): exit 0,
  738 non-blank lines; the subject and the six-file stat print first.
- `git log --oneline 6607c0eb..HEAD -- tools/pdlistscan.py tools/test_pdlistscan.py
  docs/PERSONAL-DATA.md tools/test_personal_data.py`: `641f017f` only.
- `cd tools && python3 -m unittest test_pdlistscan`: 24 tests, OK, about 5 s.
- `cd tools && python3 -m unittest test_personal_data`: 11 tests, OK, under 1 s.
- `cd tools && nice python3 -m unittest test_floor`: 255 tests, OK, about 171 s. The run printed
  a board-rebuild line; the worktree stayed clean afterwards (`git status --short` empty).
- `python3 tools/pdlistscan.py --selftest`: `selftest OK — pdlistscan`, exit 0.
- `python3 tools/pdlistscan.py --root .`: clean, advisory 0, coverage 1,252 tracked files opened and
  183,447 lines read, exit 0. With `--json`: `clean` true, `in_scope` true, `blocking` false,
  `until` 2027-03-08, no findings.
- `python3 tools/floor.py --list --root . | grep pdlistscan`: one line, `enforced  fleet  decl 2/5`.
- `ls` for `tools/leakscan.py` across this machine's checkouts: one, atelier's own.
- The visibility count and the in-scope run in question 1: the scanner run read-only with `--json`
  against each child that declares public; each exit 0, `in_scope` true, one `no-list`.
- Not run: the 22-repo probe with the date patched to the flip (no recorded command; left to the
  pass), and any probe of questions 2 to 11.
