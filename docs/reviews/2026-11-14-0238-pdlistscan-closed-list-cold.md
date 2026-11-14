# Cold pass — `pdlistscan`: in a public repo, personal data stands only where the closed list names it

**Board:** `docs/roadmap/160-doctrine-review-owed/1340-rule-4-cold-pass-queued-pdlistscan.md`
**Status:** BRIEF ONLY, not run. Written 2026-11-14 UTC by a headless Opus 5.5 brief-writer
(`cclive` lists it as session `fb2c22e6`). Queued, waiting on the principal's explicit approval of
Fable work; this brief is not that approval.

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
