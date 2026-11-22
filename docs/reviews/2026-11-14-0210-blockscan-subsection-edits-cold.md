# Cold pass — `blockscan` reads edits inside mapped sub-sections, warning until 2027-01-11

**Board:** `docs/roadmap/160-doctrine-review-owed/1320-rule-4-cold-pass-queued-blockscan-subsections.md`
**Status:** RUN 2026-11-22 UTC on Fable 5.1, both acts — PASS-WITH-FINDINGS (0 MAJOR,
4 MODERATE, 7 minor, 6 notes; three formed at reconcile). Sibling folded below the verdict;
reviewer's log opened at the end. Brief written 2026-11-14 UTC by a headless Opus 5.5
brief-writer (`cclive` lists it as session `99821c6a`).

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4: self-authored guard code, the
first of six staggered checks that turn from warning to blocking on a date in code.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Size of this pass:** small to medium: one commit, about 430 added lines, of which 207 are the
scanner, 199 its tests, 29 its README section and 13 a `CHANGELOG.md` entry.
**Why it earns a review:** `blockscan` is the guard that keeps the doctrine a child inherits (the
floor block in `PROPAGATION.md` and the scaffold template) in step with the method docs it
summarises. It is a silent-failure surface twice over. A false negative leaves a doctrine edit
unpropagated while every check reads green, which is the exact gap this change closes; a false
positive, or a finding on the wrong bullet, becomes a red CI on 2027-01-11 that no flag can soften,
and the cheapest way past it is an allow marker that then hides real drift. The worst failure is a
check that reports **clean** over a subsection edit it claims to see, or one that, on its date,
blocks honest work and trains its readers to reach for the marker.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `d0ca5d24`,
  2026-11-09 UTC, and the worker it dispatched (per the queue pointer). The author queued this pass
  and does not take it.
- **Who wrote this brief:** a headless brief-writer (`claude-opus-5-5`; `cclive` lists it as session
  `99821c6a`), started 2026-11-14 UTC by an estate health sweep, orchestrator session `58027096`
  (Opus), on the principal's instruction that a brief is written for every review known to be owed
  (Mike, 2026-11-14, verbatim: *"include all briefs are written where we know a fable review is
  required"*). Neither wrote any of this delta. **Off-tier for review, disclosed: the brief-writer
  forms no finding and writes no severity**, and stops after writing. It ran no review and used no
  Fable model.
- **Barred from running this pass:** session `99821c6a` and session `58027096` (whoever writes a
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
  `320/340` and `320/810` whole**, including the author's landing notes; **the message body of
  `6a4eeee2`** (met through `git show`, before the body-free read); the delta through
  `git show` and `tools/coldsweep.py --commit`; the later `641f017f` change to `blockscan.py`
  body-free; the CI step; commit subjects through `git log`; and the unrun brief
  `2026-11-14-0158-cclive-machine-wide-live-work-cold.md` and the head of its sibling, read for
  house form. It opened **no prior verdict** and no session record. Its harness also loaded
  user-level and repo instruction files and a memory index, which hold private context this brief
  does not carry. Everything evaluative it formed is in the sibling.

## The acceptance test

Two sources, one his and one not:

- **His words** (2026-11-09, quoted in `tools/README.md` and the module docstring, and in the first
  bullet of `320/810`): *"all six, warnings at first and then move to blocking action. With a
  staggered turn on of each so they dont all hit at once"*. That is the order for the check's
  posture: warn first, then block, on a staggered date.
- **The defect it closes:** the rule compares only the lines between a mapped heading and the next
  heading of any level, so an edit inside an unmapped subsection of a mapped section changes
  nothing it can see. The intent record `320/340` found this by running the rule over its own
  sitting's doctrine commits, and records that the non-recursive slice exists for a reason: in
  `00-APEX.md` a section and its own subsection answer to *different* bullets.

The design (derive membership from the heading tree, by nearest mapped ancestor, rather than map
each subsection or add an opt-in `recursive: true`) and the date 2027-01-11 are **the run's
choices, not his**; the delta says so itself. Whether they are the right ones is yours to attack.

## What the work is

One commit on `main`. First confirm your tree has it:

```
git merge-base --is-ancestor 6a4eeee2 HEAD || echo "MISSING 6a4eeee2"
```

Nothing may print. If something does, merge `origin/main` into the review branch before starting,
because a tree without the delta has nothing to review. Read it body-free:

```
python3 tools/coldsweep.py --root . --commit 6a4eeee2 \
  --path tools/blockscan.py --path tools/test_blockscan.py \
  --path tools/README.md --path CHANGELOG.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic
(rule 1). Always pass `--path`: the board commits that closed `320/340` and queued this pass are
barred until phase 2. Review each delta path at HEAD too. One later commit touched the scanner, an
unrelated coverage line (`641f017f`, board `115/130`, which wraps the new-side reader); read it the
same way where it meets this delta. Confirm what has landed since:

```
git log --oneline 6a4eeee2..HEAD -- tools/blockscan.py tools/test_blockscan.py \
  tools/blockscan_map.json .github/workflows/ci.yml
```

On 2026-11-14 UTC that printed only `641f017f`. Read `tools/blockscan_map.json`, the two
`blockscan` steps in `.github/workflows/ci.yml` and the mapped method docs as context: they are
what the check runs over.

## What the delta claims (extracted, not evaluated)

- **The gap is closed on both co-change planes.** `--staged` and `--against` compare every unmapped
  `##`-or-deeper subsection whose nearest mapped ancestor is the mapped heading; `--check` has
  nothing to compare.
- **The apex case still holds.** A subsection mapped to another bullet, or one beneath such a
  subsection, answers to that bullet alone, by the same nearest-ancestor reading `check_unmapped`
  uses.
- **Same remedies as a violation**: move the bullet in both the floor region and the template, or a
  reasoned `blockscan:allow` marker in the changed subsection or either new bullet. Both bullets
  moving reports `moved`, not a finding.
- **A separate finding kind**, `subsection`, so the two can be counted and judged apart.
- **A subsection added or removed in the commit counts as changed.** A mapped heading new in the
  commit is left to the direct rule.
- **The date**: until `SUBSECTION_WARN_UNTIL` (2027-01-11, UTC) the finding warns and exits 0; on
  and after it, it exits 1. No flag, environment variable or map key moves the date, and `--warn`
  does not soften it, so the CI step `--against HEAD^ --warn` turns red on that date.
- **`--json`** carries a `subsection` block (count, blocking, until), and `clean` turns false only
  from the date.
- **Atelier-only**, outside `tools/floor.py`'s registry: a child has no map, so a child's exit is
  unchanged.
- **Probes recorded:** 21 of 21 child checkouts exit 2 before and after; replayed over atelier's
  doctrine history, 14 of 124 commits would have warned, all real subsection edits; tests include
  the day of the turn.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour on this machine, including how the date reaches CI. The lenses organise it; they do not
bound it. Anything not named a non-goal is in scope.

**Non-goals:** the five other checks of `320/810` and their dates (their own passes are owed or
done); the direct co-change rule as it stood before this commit, except where the new check leans
on it or inherits its wiring; `641f017f`'s coverage line beyond where it wraps this delta's reader.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, then attack at least
   these by probe:
   - **A1.** The nearest mapped ancestor is always the bullet a subsection edit answers to: no edit
     fires on the wrong bullet, fires twice, or fires on none.
   - **A2.** Keying a subsection by its heading text and its occurrence under one parent identifies
     the same subsection on the old and new sides, so a rename, reorder, insertion or duplicate
     heading neither hides a change nor invents one.
   - **A3.** Heading detection (fences, levels, setext, indentation) is the same in the new reader
     as in the rule's own slice and in `check_unmapped`, so the three agree on what a subsection
     is.
   - **A4.** `--against HEAD^` on CI sees every commit that reaches `main`, so on 2027-01-11 a
     subsection edit cannot land green.
   - **A5.** The date flips on the UTC day it names, on every runner, and nothing at run time moves
     it.
   - **A6.** Deriving membership from the headings is better than either candidate the item named.
   Ask too whether this is the right problem at the right altitude: is a dated, unsoftenable
   block the right shape for a check whose remedy is a hand-moved bullet?
2. **Correctness & quality.** Diff the commit; drive the scanner against scratch repos with a
   scratch map and scratch docs you build, on both planes, with the date patched both sides of the
   flip. Record each overclaim against the text that makes it: the module docstring, the help
   text, the README section, the exit-code table and the `CHANGELOG.md` entry.
3. **Completeness / harvest.** Every surface that states the date, the exit codes or the `--warn`
   posture says the same thing (V3, V4, V5). Tests that would stay green on a broken change:
   mutate the code in a scratch copy, never the worktree. Is a fresh fleet probe before the flip
   recorded anywhere it will be seen?
4. **Security & privacy** — mandatory. The scanner reads git objects at a revision the caller
   names, prints heading text and map paths, and runs on CI over every push. Check that the new
   finding's detail goes through the same control and bidi escaping as the rest of the output,
   that a hostile heading or map entry cannot widen what is read or printed, and whether a
   subsection-only edit is a new way past the guard. Weigh against OWASP ASVS input-handling and
   output-encoding items, checked, not recalled. `/security-review` reads the session's pending
   diff, not this delta: aim it only at a scratch clone holding the delta as pending changes, or
   discharge it by grounds.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once on 2026-11-14 UTC, from the worktree
root, in the foreground, under a load average near 5 on 12 cores; its results are held in the
sibling. Read exit codes explicitly. `python3` on `PATH` is 3.14.6 on this machine.

- `cd tools && python3 -m unittest test_blockscan` (about 35 s under that load)
- `python3 tools/blockscan.py --selftest; echo $?`
- `python3 tools/blockscan.py --root . --check; echo $?`
- `python3 tools/blockscan.py --root . --against HEAD^ --warn; echo $?`, and the same with `--json`
- The recorded probes: the 21-child exit-2 probe and the 124-commit replay. Neither command is
  recorded; rebuild both, and say where your counts differ and why.

Run the tool from your worktree, never by bare name from `PATH`.

## House rules for this run

**Live systems:** none is needed. Child checkouts on this machine may be **read** for the fleet
probe; any probe that would write to a real repo, board or CI is **NOT RUN**: build the case in
your scratchpad and say which probes you could not build.

- Never print a secret, and name no private repo, host, client or private path. This repo is
  PUBLIC; a child seen in the fleet probe is referred to by count or type only.
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

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, the queue pointer above, this brief's sibling
`docs/reviews/2026-11-14-0210-blockscan-subsection-edits-cold.deferred.md`, the message body of
`6a4eeee2`, the intent record
`docs/roadmap/320-child-filed-findings-via-pointing-up/340-blockscans-map-cannot-see-a-subsection.md`
beyond its opening paragraph (the defect as found), and
`docs/roadmap/320-child-filed-findings-via-pointing-up/810-build-six-checks-warn-first-staggered.md`
beyond its first bullet (the principal's 2026-11-09 words).

The delta's own text carries the author's account of why (the module docstring above all); it is
the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1320-rule-4-cold-pass-queued-blockscan-subsections.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/340-blockscans-map-cannot-see-a-subsection.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/810-build-six-checks-warn-first-staggered.md \
  --also-exclude docs/reviews/2026-11-14-0210-blockscan-subsection-edits-cold.deferred.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, the
assumptions A1–A6 and your own, and the re-run list. Append your verdict below a `---` divider in
THIS file: provenance repeated (how you were spawned, your tier, what you read, the UTC day you ran
on), per-lens answers, the standing checklist V1–V7 each answered or discharged with grounds, each
load-bearing assumption damaged or confirmed with its probe, a commit ledger (`6a4eeee2`: read
body-free yes/no, findings by id), findings with stable IDs (prefix `SU`: `SU1`, `SU2`, …) and
severities (MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with
counts, a re-run ledger and a follow-up checklist. Then STOP: act 1 is committed, unrevised,
**before** the sibling is opened.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the commit body; append
`### Reconcile` beneath your verdict: per-finding notes against the sibling and the author's
account, any finding formed at reconcile marked as such, and the overall line restated. Never
revise act-1 text. Then fold the sibling in below the reconcile and delete it.

**Who applies a finding.** `blockscan` is guard code that enforces doctrine (judged by function,
`REVIEW.md` rule 3): the author applies nothing on its own, and neither does the reviewer. Record
all; the findings are the principal's to decide, after a plain-language account. Counsel per
finding is welcome, labelled as counsel and kept beneath it.

---

## Verdict — act 1, 2026-11-22 UTC

### Provenance

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named review tier, checked at
  selection. Ran 2026-11-22 20:56–21:20 UTC in the review worktree
  `/Users/mike/worktrees/fable/atelier-160-1320-2054/atelier` at HEAD `f68a9393`, read-only but
  for this file and a private work log (appended at the fold).
- **How spawned:** by a headless per-pass orchestrator, session `b5776fd4` (Opus 5.5), itself
  started by drain session `eca14b23` (Opus 5.5). Both are rule-4 off-tier orchestrators: they hold
  the context partition and commit records, form no finding and write no severity. Neither wrote
  the brief or the delta. The reviewer was not started or instructed by `99821c6a`, `58027096` or
  `d0ca5d24`. The Fable approval is the principal's drain order of 2026-11-23 NZDT, verbatim:
  *"Start a fable drain or whatever it is called now. Target 100% of weekly budget by 11.30am NZT
  todat"*.
- **Partition honoured:** the sibling `.deferred.md` was removed from the worktree before the pass
  began and was not sought in history, other checkouts or scratch. `docs/ROADMAP-DONE.md`,
  `docs/SESSIONS.md`, `docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer,
  the message body of `6a4eeee2`, `320/340` beyond its opening paragraph and `320/810` beyond its
  first bullet were not opened. `--include-barred` was not used.
- **What was read:** this brief; `docs/method/REVIEW.md` § *The standing checklist* and § *What a
  review owes* (lines 400–470, 760–830); the delta `6a4eeee2` body-free through `coldsweep
  --commit --path` ×4; the four later commits on the scanner's paths the same way (`641f017f`,
  `c6b1432e`, `734930ef`, `1d9be0fc`; the brief saw one on 2026-11-14, there are four now);
  `tools/blockscan.py` whole at HEAD; `tools/test_blockscan.py` fixture and the delta's two test
  classes; `tools/blockscan_map.json`; `.github/workflows/ci.yml` lines 1–40, 75–77, 198–229;
  `tools/README.md` § blockscan at HEAD; the `CHANGELOG.md` entry; `tools/leakscan.py:1281`;
  the permitted openings of `320/340` and `320/810`; `docs/ROADMAP.md` (grep only); the ASVS 5.0
  chapter V1 text (lens 4). Interpreters: the suite and the tool ran on Python 3.14.6 by absolute
  path (`/Library/Frameworks/Python.framework/Versions/3.14/bin/python3`, the brief's PATH
  `python3`); `--check` was also run under `/usr/bin/python3` 3.9.6 (same output, exit 0).

### The acceptance test, answered

- **His words** — warn first, then block, staggered: built. A `subsection` finding exits 0 before
  2027-01-11 UTC and 1 on and after it, `--warn` or not; nothing at run time moves the date (A5).
- **The defect** — an edit inside an unmapped subsection of a mapped section now fires on both
  co-change planes, on the nearest mapped ancestor, and the apex case still answers to its own
  bullet (A1, probes P2 and P15). Replayed over history, the author's 14 commits reproduce exactly,
  every one a real `###` edit beneath a mapped `##` (ten under PROPAGATION § *Pointing up*, four
  under CONCURRENCY § *The channel*), the first of them the very edits `320/340` found.
- **Where it falls short:** the claim that the CI step turns red on the date holds only for the
  last commit of a push (SU1); the tool's own `--check` report still tells a reader the edit is
  invisible (SU2); and on the flip day, with the step's `--warn`, the output says "not blocking
  this build" and exits 1 (SU3). None is a false negative in the check itself.

### Lens 1 — approach and assumptions

- **A1 (nearest mapped ancestor; never wrong, twice or none).** Confirmed by probe: an unmapped
  `###` under a mapped `##` fires the `##`'s bullet only (P2); a `####` under an unmapped `###`
  under a mapped `##` fires the `##`'s bullet (P15); a `####` under a mapped `###` fires that
  `###`'s bullet, not the enclosing `##`'s (delta test). One nuance: the real map ties `### The
  principal's authority…` to two bullets, so a `####` beneath it fires twice, once per bullet
  (P1), exactly as the direct rule does for that shared section. Consistent, not wrong; counts
  inflate.
- **A2 (keyed by heading text and occurrence).** Damaged in the small. A rename with the body
  unchanged yields two findings, both worded "changed" (P3); inserting a same-named subsection
  before an existing one yields two, one for the untouched body that slid to occurrence 1 (P5); a
  reorder with bodies unchanged is invisible (P4), which is defensible. No case hid a real change.
  The key ignores level, so a `###` and a `####` with the same text under one parent share a key:
  not probed in the real docs, where no such pair exists. SU8.
- **A3 (one notion of a heading across the three readers).** Not true, latently. `extract_section`
  (the direct rule's slice) is fence-blind and cuts at any `#`-leading line; `_headings` (used by
  `check_unmapped` and the new `_subsections`) is fence-aware and drops level 1. Probe P6: a
  fenced `## fake` inside a mapped section, then an edit after the fence, is clean on both the
  direct rule (slice ends at the fence) and the sub-section check (no subsection owns it). On the
  real docs all twelve mapped slices end where the fence-aware reader puts the next heading, and
  PROPAGATION.md's two fence-blind heading-like lines (134, 376) sit outside every mapped slice,
  so the gap is not live today. Pre-existing class (b) of the docstring; SU11.
- **A4 (`--against HEAD^` on CI sees every commit that reaches `main`).** False. `ci.yml` runs on
  every push with `fetch-depth: 0`, and `HEAD^` is the pushed head's parent, so a push of two or
  more commits is checked only for its last. Probe P12: a subsection edit in commit 1 of a
  two-commit push, an unrelated commit 2 → `--against HEAD^` exit 0 clean; `--against HEAD~2`
  exit 1. The direct rule inherits the same blind spot; the delta's text ("turns red on that date")
  rests on it. SU1.
- **A5 (flips on the UTC day, nothing moves it).** Confirmed. `_utc_today()` is
  `datetime.now(timezone.utc).date()`; the constant is compared with `<`; grep finds no flag,
  environment variable or map key reaching it; tests patch `_utc_today` only. The one input is the
  runner's clock. Note: `render_human` reads the clock again (`today=None`), so at the midnight
  boundary the header and the exit code could disagree (P14; SU13).
- **A6 (heading-derived membership beats the two candidates).** Confirmed on the evidence: the 14
  historical hits were all under headings nobody had mapped, so an opt-in or a per-subsection map
  would have missed every one until someone widened it; the derived form has no map to go stale.
- **Altitude.** The right problem: the gap `320/340` found was real and recurrent (14 of the
  commits that could be replayed). The shape is where this pass has a reservation: from 2027-01-11
  the *derived* signal (an edit beneath a cited section) blocks CI while the *direct* signal (an
  edit to the cited section's own lines) stays `--warn` advisory. On that day editing `### The
  route` reds the build and editing `## Pointing up`'s own paragraph does not. The author discloses
  the split ("whose flip stays a separate ruling") and is right that the direct rule is not one of
  the six; the inversion is still his to look at. SU5.

### Lens 2 — correctness and quality

- The sub-section logic is sound where probed: nearest mapped ancestor (P2, P15), both-bullets-
  moved → `moved` (test and M8 caught), one side moved → finding naming the other (test), marker
  in the subsection (test) or in a bullet (P9) → `skipped`, bare marker exempts nothing (test),
  added and removed subsections count (tests), `--against` plane live (test and M9 caught), date
  strictly before (test and M4 caught), hostile heading text escaped on both outputs (P10).
- **Overclaims, against the text that makes them:**
  - Module docstring THE DATE and `CHANGELOG.md`: "in `.github/workflows/ci.yml`'s `--against
    HEAD^ --warn` step" / "so the CI step … turns red on that date" — only for a push's last
    commit (SU1).
  - `check_unmapped` docstring (blockscan.py:587–591) and the `--check` trailer (910–912): "an
    edit under an unmapped subsection is invisible to the co-change rule" / "An edit under one of
    these is invisible to the co-change rule" — no longer true for the "under mapped" rows on
    `--staged` and `--against` (SU2).
  - blockscan.py:1123: "(--warn: advisory only — not blocking this build.)" printed when a
    violation and a blocking `subsection` finding coexist under `--warn`, exit 1 (SU3).
  - `CHANGELOG.md` and the `320/810` first-bullet record: "replayed over … 124 doctrine
    commits" — the 14 reproduce; the 124 does not (SU9).
  - README § exit codes, help text, constant comment: accurate as far as probed.
- Quality notes: `_subsections` re-parses the whole doc twice per (bullet, source) pair; the
  mapped docs are small, so this is cosmetic. `_render_base`'s "N mapped section(s) checked"
  counts subsection `moved`/`skipped` notes as sections; cosmetic.

### Lens 3 — completeness and harvest

- **Surfaces stating the date or posture (V3, V4, V5):** `blockscan.py` (docstring, constant,
  help, exit table), `tools/README.md` § blockscan, `CHANGELOG.md`, `attribscan.py`'s "four weeks
  after blockscan's sub-section date" and the `320/810` first bullet agree on 2027-01-11, UTC, no
  flag, `--warn` does not soften. One fact, one home: the date is the constant and every prose copy
  names it. Unswept: `ci.yml`'s step name and comment still read "advisory" (SU4); the `--check`
  trailer and `check_unmapped` docstring still read "invisible" (SU2).
- **Tests that stay green on a broken change (mutation on a scratch copy, 18 tests each):**
  M1 fence handling removed from `_headings` → survived: `test_a_fenced_heading_does_not_cut_a_
  subsection_short` fences a level-1 line, which `_headings` drops regardless, so it proves
  nothing about fences (SU6). M2 occurrence counting dropped → survived. M3 bullet-marker
  exemption removed → survived. M5 line number off → survived. M6 JSON `until` wrong →
  survived. M7 nearest MAPPED ancestor replaced by nearest ancestor → survived: a false-negative
  mutation (a `####` under an unmapped `###` would go unreported) no test catches (SU7). Caught:
  M4 (`<=`), M8 (`moved` on one side), M9 (`--against` guard inverted).
- **A fresh fleet probe before the flip:** his shape in `320/810`'s first bullet is "Probe every
  child before each flip". Nothing in the readable index (`docs/ROADMAP.md`, grep for the date,
  "flip", "probe") schedules one, and nothing visible schedules a look at who owns the 14 "under
  mapped" headings before they start blocking (SU14). The barred records may hold it; act 2 checks.

### Lens 4 — security and privacy (mandatory)

- **New output goes through the same controls:** `_render_subsections` passes `source_path` and
  `detail` through `_safe`; `detail` embeds heading text via `!r`. Probe P10 (a heading carrying
  U+202E and ESC): human output shows `‮\x1b`, JSON is encoder-escaped, no raw control or
  bidi character on either. `f.bullet` prints unescaped in both the new and the old renderers; it
  is a map key, in-repo data, the same exposure the direct rule always had.
- **Can a hostile heading or map entry widen what is read or printed?** No new path: headings only
  become dictionary keys and text; the map's paths go through the unchanged `git show <rev>:<path>`
  readers and the `--check` plane's existing outside-root refusal (CU6). The delta adds no
  subprocess argument, no file write and no new input source.
- **Is a subsection-only edit a new way past the guard?** The opposite: it closes one. The ways
  still past it are the inherited ones: a multi-commit push on CI (SU1), text after a fenced
  heading-like line in a mapped section (SU11), a second `#` title (documented), and the unwired
  hook plane (documented WIRING RESIDUAL).
- **Pre-existing, disclosed:** `--against REV` is passed to git as `REV:path` with no
  `--end-of-options`, so `--against=--output=<file>` reaches git as an option (P11; it failed only
  because the target name ends in `:docs/…`). The flag predates the delta; its one caller is
  `ci.yml` with `HEAD^`. SU12.
- **ASVS, checked not recalled** (OWASP ASVS 5.0, chapter V1 *Encoding and Sanitization*, fetched
  from the project's repository 2026-11-22): 1.1.2 (output encoding or escaping "as a final step
  before being used by the interpreter") — met for the terminal and JSON contexts by `_safe` and
  the encoder; 1.2.5 (protect against OS command injection, parameterised OS calls) — the calls
  are argument lists, not shells, and the one option-injection seam is P11, pre-existing. The
  chapter has no explicit bidi/control-character requirement; `_safe` goes beyond it.
- **`/security-review`:** discharged by grounds. It reads this session's pending diff, which is
  only the partition's deletion, and this session cannot point it at a scratch clone. Grounds: the
  delta introduces no new input source, subprocess argument or write, and the one new output path
  was probed directly (P10).

### The standing checklist

- **V1** — three claims stronger than their evidence: the CI red on the date (SU1), the `--check`
  "invisible" wording in reverse (SU2), the 124 denominator (SU9).
- **V2** — every re-run line re-run (ledger below); the 21-child and 124-commit probes rebuilt.
- **V3** — swept: README, CHANGELOG, docstring, help, exit table, attribscan's cross-reference.
  Missed: `ci.yml` step name and comment (SU4); `check_unmapped` docstring and trailer (SU2).
- **V4** — the date has one home (`SUBSECTION_WARN_UNTIL`); prose copies name the constant.
- **V5** — contradictions: tool output versus tool behaviour (SU2, SU3); `clean` means two things
  (SU10). Cross-references checked for the rule reached: the constant comment's "the shape of
  leakscan's `TYPE_LEVEL_UNTIL`" reaches `leakscan.py:1281`, a dated constant of the same shape
  (fixed by `734930ef` from a name that no longer existed); "`attribscan` 2027-02-08" is 28 days
  on; "CU5, CU10 of the 160/430 pass" is a prior verdict, barred until act 2.
- **V6** — lens 4 above; `/security-review` discharged by grounds.
- **V7** — stated above and in the brief.

### Commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `6a4eeee2` | yes (`coldsweep --commit --path` ×4) | SU1–SU10, SU13, SU14; SU11–12 inherited |
| `641f017f` | yes (coverage wrapper only) | none |
| `c6b1432e` | yes (one docstring name) | none |
| `734930ef` | yes (constant comment cross-reference) | none; fixes a dangling name |
| `1d9be0fc` | yes (map heading rename) | none |

### Findings

- **SU1 — MODERATE.** On CI, `--against HEAD^` compares only the last commit of a push, so a
  subsection edit in an earlier commit of the same push lands green on and after 2027-01-11
  (probe P12: two-commit push, exit 0; `HEAD~2`, exit 1). The docstring and `CHANGELOG.md` say
  the CI step "turns red on that date". Inherited from the direct rule's wiring, not introduced
  here, but the delta's blocking claim and the brief's A4 rest on it. Not MAJOR because the check
  itself has no false negative; the plane it runs on does. *Counsel:* compare against the push's
  base (`github.event.before`, or the merge-base with the target on the PR plane), or say in the
  docstring and CHANGELOG that CI reads one commit per push.
- **SU2 — MODERATE.** The `--check` trailer ("An edit under one of these is invisible to the
  co-change rule", blockscan.py:910–912) and `check_unmapped`'s docstring (587–591) are false
  for the 14 "under mapped" rows the new check now reads on `--staged` and `--against` (P13). On
  the flip day a reader of `--check` is told the edit is invisible while `--against` reds. V5.
  *Counsel:* split the report: "under mapped" rows are now checked (warning until the date), the
  rest remain unseen.
- **SU3 — MODERATE.** With `--warn` (the CI step's flag), a violation and a blocking `subsection`
  finding together, the output prints "(--warn: advisory only — not blocking this build.)" and
  exits 1 (P8; blockscan.py:1123 gates on violations and `--warn` only). On the exact day the step
  starts failing, its last line says it is not. *Counsel:* gate the trailer on `not
  subsection_blocks` too, or print the blocking line last.
- **SU4 — minor.** `ci.yml`'s step name "blockscan --against HEAD^ (co-change — advisory,
  atelier-only)" and its comment say advisory with no mention that the step blocks for
  `subsection` findings from 2027-01-11. A mirror site unswept (V3). *Counsel:* one clause in the
  step name or comment, with the date.
- **SU5 — MODERATE (design, for the principal).** From 2027-01-11 the derived signal (an edit
  beneath a cited section) blocks CI while the direct signal (an edit to the cited section's own
  lines) stays advisory. Disclosed by the author as a separate ruling; the ordering is still
  inverted. *Counsel:* either bring the direct rule's flip forward to the same date, or hold the
  subsection flip until the direct rule's date is ruled, so the stronger signal never blocks later
  than the weaker.
- **SU6 — minor.** `test_a_fenced_heading_does_not_cut_a_subsection_short` fences a level-1 line
  (`# not a heading`), which `_headings` drops whether or not it honours fences; mutation M1
  (fence handling removed) passes it. *Counsel:* fence a `##`- or `###`-leading line.
- **SU7 — minor.** Test gaps the mutations expose: M7 (nearest *mapped* ancestor replaced by
  nearest ancestor — a false negative for a `####` under an unmapped `###` under a mapped `##` —
  survives; the code is right, P15), M2 (duplicate headings), M3 (marker in a bullet exempting a
  subsection edit), M5 (reported line), M6 (JSON `until`). *Counsel:* one test each; M7 first.
- **SU8 — minor.** A rename of an unmapped subsection with its body unchanged reports two
  findings worded "changed"; inserting a same-named subsection before an existing one reports two,
  one for the body that slid to occurrence 1 (P3, P5). The key also ignores heading level. Noise,
  not a miss. *Counsel:* word a one-sided key as added or removed, and consider keying by
  (level, text, occurrence).
- **SU9 — minor.** "Replayed over … 124 doctrine commits, 14 would have warned" (`CHANGELOG.md`,
  `320/810`): the 14 reproduce exactly; no reconstruction yields 124 (183 commits touch a mapped
  file before the delta; 130 have every mapped file on both sides; 77 run clear of a config error
  with the delta's map). The record states a denominator it does not define. *Counsel:* record the
  commit set or the command.
- **SU10 — note.** `--json` `clean` is true for a pre-date `subsection` finding (exit 0) but false
  for a `violation` under `--warn` (also exit 0): two meanings of `clean` under the two warn
  postures. Documented in the README; a consumer of `clean` learns nothing of the warning.
- **SU11 — note (pre-existing).** `extract_section` is fence-blind; `_headings` is fence-aware.
  Text after a fenced heading-like line inside a mapped section is invisible to both the direct
  rule and the sub-section check (P6). Not live in the current docs (a3 probe). Class (b) of the
  docstring, now with a second reader that disagrees with the first.
- **SU12 — note (pre-existing).** `--against REV` reaches git as `REV:path` without
  `--end-of-options`; an option-shaped REV is parsed as an option (P11). The flag's only caller is
  `ci.yml`. *Counsel:* `git show --end-of-options <spec>`.
- **SU13 — note.** `_main` computes `subsection_blocks` from one clock read and `render_human`
  takes another (`today=None`); across midnight UTC the header could say warning while the exit
  is 1. *Counsel:* pass the same `today` to both.
- **SU14 — minor.** Nothing visible schedules the pre-flip fleet probe his shape asks for ("Probe
  every child before each flip", `320/810` first bullet) or a look at who owns the 14 "under
  mapped" headings before 2027-01-11; the only probe on record is the build-day one. The barred
  records may carry it; act 2 reconciles.

**Overall: PASS-WITH-FINDINGS — 0 MAJOR, 4 MODERATE (SU1, SU2, SU3, SU5), 6 minor (SU4, SU6,
SU7, SU8, SU9, SU14), 4 notes (SU10–SU13).** The check does what the defect needed and the
principal ordered; what falls short is the plane it runs on, the words around it, and the tests
that would hold it there.

### Re-run ledger

| Line | Result |
|---|---|
| unit tests (`discover -s tools -p test_blockscan.py`, 3.14.6) | 58 OK, 45.4 s, exit 0 (53 + 5) |
| `blockscan.py --selftest` | selftest OK, exit 0 |
| `blockscan.py --root . --check` | exit 0; 61 unmapped, 14 under mapped; 7 files · 4541 lines |
| `blockscan.py --root . --against HEAD^ --warn` | clean, exit 0 |
| same with `--json` | `clean` true, `subsection` {0, false, 2027-01-11}, exit 0 |
| `--check --warn` under `/usr/bin/python3` 3.9.6 | exit 0, same output |
| 21-child probe, rebuilt (read-only) | 22 of 22 exit 2 before and after, both modes |
| 124-commit replay, rebuilt (map as of `6a4eeee2`) | 14 fire, all real; 183 / 130 / 77, not 124 |

All re-runs niced, foreground, one heavy process at a time; load 7–13 on 12 cores throughout.
Scratch copies and repos deleted.

### Follow-up checklist

- [ ] SU1: decide the CI comparison base (push base or merge-base) or state the one-commit limit.
- [ ] SU2: reword the `--check` trailer and `check_unmapped` docstring for the rows now checked.
- [ ] SU3: gate the `--warn` advisory trailer on no blocking `subsection` finding.
- [ ] SU4: sweep `ci.yml`'s step name and comment with the date.
- [ ] SU5: the principal rules on the order of the two flips.
- [ ] SU6, SU7: fence a `##` line in the fence test; add the M7, M2, M3, M5, M6 tests.
- [ ] SU8: word one-sided keys as added or removed.
- [ ] SU9: record the replay's commit set.
- [ ] SU14: schedule the pre-flip fleet probe and an owner for the 14 "under mapped" headings.
- [ ] Act 2: reconcile against the sibling and the barred records; fold; record who applies.

Who applies: none of the above is the author's or the reviewer's to apply (`REVIEW.md` rule 3,
guard code); all are recorded for the principal after a plain-language account.

### Reconcile — act 2, 2026-11-22 UTC

Act 1 was committed unrevised by the orchestrator (`8f3c698a`) before anything below was opened.
Opened for act 2: the held sibling; the message body of `6a4eeee2`; the queue pointer `160/1320`;
`320/340` and `320/810` whole; and, of the prior verdicts, only the 2026-10-03 pass that defines
CU5 and CU10, to check the docstring's cross-reference. Not opened: `docs/sessions/`,
`docs/SESSIONS.md`, `docs/ROADMAP-DONE.md`, any other prior verdict. Act-1 text above is unchanged.

**Against the author's account** (commit body, the close note on `320/340`, slice 1 of `320/810`):
every claim it makes was already checked in act 1 — the nearest-ancestor design, the apex case,
the date and `--warn` posture, 21 of 21 children, 14 of 124, "including the day of the turn". The
body adds one figure act 1 did not see, "53 in test_blockscan (+19)"; see SU17. The docstring's
"CU5, CU10 of the 160/430 pass named that gap" reaches the rule it names: CU10 there reads
"`--staged` and `--against` stay blind to a subsection-only edit", the exact gap this delta closes
(CU5 is the `#`-title body, a neighbouring blind spot). Cross-reference sound.

**Per finding, against the sibling's ten questions:**

- **SU1** ↔ Q5: agree on the multi-commit push. One disagreement: the sibling says a subsection
  edit "on the second-parent side of a merge" lands green; `HEAD^` is the first parent, so a true
  merge commit's first-parent diff carries every merged change — only a fast-forward (no merge
  commit) reduces to the multi-commit case probed in P12. Q5 also asks whether "blocking" that is a
  red CI after the push, never a refused commit (the hook plane is unwired, WIRING RESIDUAL),
  matches his *"move to blocking action"*. That is his to say; the record should state what
  blocking reaches. Stands, MODERATE.
- **SU2, SU3, SU4, SU6, SU7** — not raised by the sibling or the author's account. Stand.
- **SU5** ↔ Q6 (adjacent): the author's account is consistent with act 1 — "his order was the
  check", "the date is the run's choice". The inversion stands as a design question for him.
- **SU8** ↔ Q2 and Q3: agree. Two additions, both confirmed: for a removed subsection the printed
  line is the old file's (`old_body[0]`), shown against the new path; and the marker on a removal
  can sit only in a bullet (probe Q3a exit 1 without one, Q3b `skipped` with one in the template
  bullet), so the README's "in the changed subsection" option is moot for a removal. Stands,
  minor; the counsel extends to saying so.
- **SU9** ↔ Q10: agree; the author's account records no command. Stands.
- **SU10–SU13** — stand. Q1 (one edit, two findings) is answered by P1 and P8 in act 1: the two
  kinds are reported and counted apart by design, and the heading-mapped-by-two-bullets case fires
  once per bullet as the direct rule always has. Intended; counted honestly.
- **SU14** ↔ Q9: `320/810` whole does record the obligation, twice, as open `[ ]` sub-items
  ("Each flip needs a fresh fleet probe before its date"; the five dates listed). So the duty is
  written, in a record act 1 could not read, but nothing dated or mechanical surfaces it before
  2027-01-11. The `320/340` close notes also show the exposed set growing (12 subsections under
  mapped sections on 2026-10-03, 14 on 2026-11-22). Stands, minor, reworded: recorded, undated,
  ungated.
- **Q4** (a parent that changes level) ↔ A1: probed at reconcile. An unmapped `###` promoted to
  `##` takes its `####` out of the mapped tree; both are reported as changed under the bullet they
  left (Q4a, exit 1), never under a wrong one. A mapped heading changing level is a stale-heading
  config error, exit 2 (Q4b): fail-safe. A1 stands confirmed; no new finding.

**Findings formed at reconcile** (marked as such; none changes the act-1 severities):

- **SU15 — minor, formed at reconcile** (sibling Q8). The `CHANGELOG.md` entry is headed
  2026-11-10; the commit is `2026-11-10T02:55:39+13:00`, which is `2026-11-09T13:55:39Z`, and the
  board (`320/340`, `320/810`) records 2026-11-09. `CONVENTIONS.md` keeps time "UTC at rest; local
  on presentation". One landing, two dates (V4, V5). *Counsel:* head the entry 2026-11-09.
- **SU16 — note, formed at reconcile** (sibling Q6). The docstring's "this check was ordered
  blocking by the principal, on a date" attributes the dated shape to him; his words order
  warn-then-block, staggered, and name no date, and the same paragraph says the date is the
  run's. The reader is not misled on the date, only on who chose a dated constant (V1).
  *Counsel:* "ordered blocking by the principal; the date is the run's".
- **SU17 — note, formed at reconcile** (sibling Q7). The commit body says "53 in test_blockscan
  (+19)"; counted by `def test_` at `6a4eeee2~1` and `6a4eeee2`: 35 → 53, so +18, as `320/810`
  records. Record-only (V1).

**The sibling's own runs**, where they overlap act 1: all agree (58 tests OK; selftest OK;
`--check` exit 0; `--against HEAD^ --warn` clean, coverage 4,371 lines on 2026-11-14 against 4,541
now, the docs having grown). Its duplicate-heading measurement (none in any mapped doc) matches
act 1's reading that the A2 cases are latent.

**Overall, restated: PASS-WITH-FINDINGS — 0 MAJOR, 4 MODERATE (SU1, SU2, SU3, SU5), 7 minor
(SU4, SU6, SU7, SU8, SU9, SU14, SU15), 6 notes (SU10, SU11, SU12, SU13, SU16, SU17); 17 in all,
SU15–SU17 formed at reconcile.** Who applies: unchanged — none of it is the author's or the
reviewer's to apply; all is recorded for the principal after a plain-language account.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-22)

*Released to the reviewer only after its act-1 findings were committed (`8f3c698a` before the
rebase onto `main`); folded here verbatim (headings demoted two levels) and the sibling file
removed, per the brief. The orchestrator (a headless Opus 5.5 session, `b5776fd4`, started by drain
session `eca14b23`, itself Opus 5.5) held the partition, formed no finding and wrote no severity.*

### Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-14-0210-blockscan-subsection-edits-cold.md` (`REVIEW.md` rule 1).
Written 2026-11-14 UTC by the brief-writer (`cclive` lists it as session `99821c6a`), which
authored none of the delta. Open this only after act 1 is committed. Everything here is a floor,
never a fence, and none of it is a finding: the brief-writer read the code once and probed none of
these past what is recorded below.

#### The brief-writer's own questions

1. **One edit, two findings.** When a mapped section's own lines and one of its subsections both
   change with the bullet unmoved, the direct rule reports a `violation` and the new check a
   `subsection`. Before the date and with `--warn`, neither blocks; from the date the second blocks
   alone. Is the double report intended, and is it counted honestly? The same question for a heading
   mapped by two bullets: `_subsection_findings` runs once per bullet per source.
2. **The occurrence key.** Subsections are keyed `(heading text, nth under this parent)`. A new
   subsection inserted ahead of an existing one with the same text shifts every later index, and a
   renamed subsection reads as one removed and one added (two findings for one edit). For a removed
   subsection the printed line number is the old file's, shown against the new path. No mapped doc
   held a duplicate heading on 2026-11-14 (measured), so the duplicate case is latent (A2).
3. **The allow marker on a removal.** For a removed subsection the body text is empty, so the
   marker can sit only in a bullet. The README says the marker may sit "in the changed subsection";
   is that true for a removal?
4. **A parent that moves.** If a mapped heading changes level, or an unmapped heading between two
   mapped ones changes level, subsections can change their nearest mapped ancestor between the old
   and new sides. Does that report a change to every migrated subsection, under the wrong bullet?
5. **What "blocking" reaches.** The only wiring is CI's `--against HEAD^ --warn`. `HEAD^` is the
   tip's first parent, so a subsection edit in any commit of a push other than the last, or on the
   second-parent side of a merge, lands green after the date. And with no hook-plane wiring (the
   docstring's WIRING RESIDUAL), blocking means a red CI after the push, never a refused commit.
   Does that match his words *"move to blocking action"* (A4)?
6. **Whose order the date is.** The docstring says the check "was ordered blocking by the principal,
   on a date"; the same text, the README and the CHANGELOG say the date is the run's choice. His
   words order warn-then-block, staggered, and name no date. Is "ordered blocking … on a date" an
   attribution stronger than his words (V1)?
7. **Test count.** The commit body says 53 tests "(+19)"; the `320/810` slice note says "18 new,
   53 total". Measured by counting `def test_` in `tools/test_blockscan.py`: 35 at `6a4eeee2~1`,
   53 at `6a4eeee2`, 58 at the brief's base. So +18; the body's +19 looks off by one (V1).
8. **The CHANGELOG date.** The entry is headed 2026-11-10; the commit is 2026-11-10 02:34 +1300,
   which is 2026-11-09 13:34 UTC, the date the board records. `CONVENTIONS.md` keeps dates at rest
   in UTC. A local date in a record?
9. **The flip's own probe.** `320/810` says each flip needs a fresh fleet probe before its date.
   Nothing the brief-writer found surfaces that probe ahead of 2027-01-11 (no dated item or gate
   reads it). Is the warn period doing its job if nobody is told it is ending?
10. **The 124-commit replay.** No command is recorded for it, so "14 of 124, all real subsection
    edits" cannot be re-run as written. Which 124, and judged real by whom?

#### What the brief-writer ran, and what it got

All from the worktree root on 2026-11-14 UTC (base `2c1f0296`), foreground, load average about 4
to 5 on 12 cores.

- `git merge-base --is-ancestor 6a4eeee2 HEAD`: exit 0.
- `python3 tools/coldsweep.py --root . --commit 6a4eeee2 --path …` (the brief's four paths):
  exit 0, 607 non-blank lines; the subject and the four-file stat print first.
- `cd tools && python3 -m unittest test_blockscan`: 58 tests, OK, about 34 s.
- `python3 tools/blockscan.py --selftest`: `selftest OK`, exit 0.
- `python3 tools/blockscan.py --root . --check`: exit 0.
- `python3 tools/blockscan.py --root . --against HEAD^ --warn`: clean, coverage 7 files and 4,371
  lines, exit 0. With `--json`: `clean` true, `subsection` `{count 0, blocking false, until
  2027-01-11}`. The base commit touched no mapped doc, so this shows the wiring runs, not that the
  check fires.
- The brief's `coldsweep` sweep line: exit 0 (with a warning that the sibling path matched no file,
  because the sibling was not yet written).
- Duplicate heading text in each mapped doc, by a throwaway script over `tools/blockscan_map.json`:
  none in any of the six mapped docs.
- Not run: the 21-child probe and the 124-commit replay (no recorded commands; left to the pass).

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

*Orchestrator, at the fold: one token replaced for the public repo, the local root that holds the
child checkouts, now `<checkouts-root>`; nothing else changed.*

# Review log — atelier 160/1320, blockscan subsection edits cold pass

Reviewer: Fable 5.1 (claude-fable-5-1). Orchestrator b5776fd4 (Opus 5.5) under drain session
eca14b23 (Opus 5.5). Review worktree: /Users/mike/worktrees/fable/atelier-160-1320-2054/atelier
(HEAD f68a9393). Log opened 2026-11-22 20:56 UTC. Commands, files and evidence only.

## Act 1

- 20:56 UTC `uptime`: load 10.09 / 10.53 / 11.08 on 12 cores. `git status --short`: only the
  expected ` D docs/reviews/...deferred.md` (partition). `merge-base --is-ancestor 6a4eeee2 HEAD`:
  present (printed nothing).
- `git log --oneline 6a4eeee2..HEAD -- tools/blockscan.py tools/test_blockscan.py
  tools/blockscan_map.json .github/workflows/ci.yml` → FOUR commits, not the one the brief saw on
  2026-11-14: 1d9be0fc (map: renamed session-log heading), 734930ef (board/leakscan: adoption
  graces), c6b1432e (propagation: floor bundle, 320/370), 641f017f (coverage line, 115/130).
  To read body-free where they meet the delta.
- Interpreters: PATH python3 = 3.14.6 (/Library/Frameworks/...); /usr/bin/python3 = 3.9.6.
  Tool runs use the worktree path, never bare name. Decision on which interpreter: below.
- Read brief in full (lines 1–264) and REVIEW.md lines 400–470 (V1–V7) and 760–830 (verdict shape).
- Read body-free via coldsweep (`--commit 6a4eeee2 --path` ×4): 4 files, +430/−18. Then the four later
  commits the same way: 641f017f (coverage wrapper `_Coverage`, wraps read_new; +41 test lines),
  c6b1432e (one docstring bullet name), 734930ef (constant comment: leakscan `BINARY_GRACE_UNTIL`
  → `TYPE_LEVEL_UNTIL`), 1d9be0fc (map: RECORD.md session-log heading renamed). None changes the
  sub-section logic. Read `tools/blockscan.py` 1–1293 at HEAD, `tools/test_blockscan.py` 1–130
  (fixture) and the delta's test classes, `tools/blockscan_map.json` whole, `ci.yml` 1–40, 75–77
  (checkout fetch-depth 0), 198–229 (the two blockscan steps, `--check --warn` and `--against HEAD^
  --warn`, step names say "advisory").
- Allowed openings read: 340's opening paragraph (the defect as found: `### The route` and
  `### Report without harming the parent` edits reported clean); 810's head and first bullet (his
  words; the six checks; "Probe every child before each flip").
- `grep -rln "2027-01-11\|SUBSECTION_WARN_UNTIL"` (records excluded): CHANGELOG.md, tools/README.md,
  tools/blockscan.py, tools/test_blockscan.py, tools/attribscan.py. ci.yml does NOT state the date.
- leakscan.py:1281 `TYPE_LEVEL_UNTIL = datetime.date(2026, 11, 20)` exists → the constant comment's
  cross-reference (after 734930ef) reaches a real constant of the same shape. ✓
- `blockscan --check --root <worktree>` (10:00, load 7.6): exit 0; 61 unmapped headings, 14 of them
  "under mapped" (1 in 00-APEX.md, 6 in CONCURRENCY.md § The channel, 7 in PROPAGATION.md § Pointing
  up); coverage 7 files · 4541 lines. The trailer prints "An edit under one of these is invisible to
  the co-change rule." → CANDIDATE: after this delta that sentence is false for the 14 "under mapped"
  rows on `--staged`/`--against`; `check_unmapped`'s docstring (blockscan.py:587–591) says the same.
  Rule: V5 (the work agrees with itself); lens 2 overclaim-in-reverse (tool output understates what
  it checks, on the surface a reader uses to learn the posture).
- Commit-set counts at 6a4eeee2 for the "124 doctrine commits" replay: 6 mapped docs 179 (176
  no-merges, 169 first-parent); +template 183/180; all docs/method 348. None equals 124; denominator
  to be reconstructed by probe (see replay below).
- CANDIDATE (A4): ci.yml runs `--against HEAD^` on every push; `HEAD^` of a linear multi-commit push
  is only the last commit's parent... wait, no: HEAD^ IS the previous commit, so only the LAST commit
  of the push is compared. An earlier commit in the same push that edited a subsection is never
  compared on CI (the direct rule has the same gap; the delta's blocking claim rests on it). To
  probe in scratch. fetch-depth: 0 so HEAD^ resolves.
- CANDIDATE (lens 1, altitude): from 2027-01-11 the derived/weaker signal (subsection edit) blocks
  CI while the direct rule (edit to the mapped section itself) stays `--warn` advisory. Author
  discloses ("whose flip stays a separate ruling") but the inversion is for the principal.
- CANDIDATE (V3): ci.yml step name and comment say "advisory" with no mention that the step turns
  blocking for `subsection` findings on 2027-01-11.
- RE-RUN 1 (21:02 UTC, load 7.5): `nice -n 10 /Library/Frameworks/Python.framework/Versions/3.14/bin/python3
  -m unittest discover -s <worktree>/tools -p test_blockscan.py` → Ran 58 tests in 45.4 s, OK, exit 0.
  (Brief said 53 at build; 641f017f added the 5 CoverageLine tests.) Interpreter: 3.14.6 by absolute
  path, as the brief names PATH python3 = 3.14.6; also ran `--check --warn` under /usr/bin/python3
  3.9.6 → exit 0, same output (the tool's "system python3" claim holds).
- RE-RUN 2: `blockscan.py --selftest` → "selftest OK", exit 0.
- RE-RUN 3: `--root <worktree> --check` → exit 0 (above). RE-RUN 4: `--against HEAD^ --warn` → clean,
  exit 0; `--json` → clean true, subsection {count 0, blocking false, until 2027-01-11}, exit 0.
- RE-RUN 5 (replay): scratch helper replay.py (scratch copy of the delta's tools, map as of
  6a4eeee2) ran check_costaged for every commit before 6a4eeee2 touching any of the 7 mapped files
  (c^ vs c; read-only `git show`). 183 candidates: 77 ran clean of config errors, 106 hit a config
  error (map did not resolve at that commit: stale-heading/missing-bullet/missing-region, or a
  mapped file absent). **14 commits** carry ≥1 `subsection` finding, every one a `###` beneath a
  mapped `##` (PROPAGATION § Pointing up ×10 commits; CONCURRENCY § The channel ×4): the author's 14
  REPRODUCES. The denominator 124 does NOT: 183 candidates; 130 where all 7 files exist on both
  sides; 77 ran without config error. Run took 3 m 39 s niced.
- RE-RUN 6 (fleet): fleet_probe.sh over every `<checkouts-root>/*/.atelier-floor.json` except atelier → 22
  children (author counted 21 on 2026-11-09; one more carries the floor file now). All 22: exit 2
  with the delta's blockscan AND the pre-delta blockscan, both `--check --warn` and `--against HEAD^
  --warn` (no map). Claim holds; count differs by the fleet's growth, not the tool. Read-only.
- PROBES (scratch repo, probes.py/probes2.py, two-bullet map mirroring the real `###` mapped to two
  bullets; date patched via `_utc_today`; scratch repo deleted at end):
  P1 `####` under the `###` mapped to two bullets → 2 findings (stop, ask): fires once per bullet,
     as the direct rule does for a shared section. Consistent; counts inflate. note.
  P2 unmapped `###` under mapped `##` → 1 finding, apex only. A1 holds.
  P3 rename-only of an unmapped subsection (body unchanged) → 2 findings (old name "changed", new
     name "changed"); the detail says "changed", not removed/added. minor (A2).
  P4 reorder-only of two subsections → clean, exit 0. Reorder invisible; bodies unchanged. note.
  P5 same-named subsection inserted BEFORE the old → 2 findings; occurrence index shifts the old
     body onto key n=1. minor (A2).
  P6 fenced `## fake` inside a mapped section, edit AFTER the fence before the next heading →
     exit 0, CLEAN. extract_section (fence-blind) ends the direct slice at the fenced line;
     _subsections (fence-aware) owns no subsection there. Latent gap, pre-existing class (b).
  P6b fenced `###` inside an unmapped subsection, edit after it → finding. Fence rule works there.
  P7 second `#` title inside a mapped section, edit under it → clean. Documented class (c).
  P8 violation + subsection + `--warn` ON the date → exit 1 AND prints "(--warn: advisory only —
     not blocking this build.)" (blockscan.py:1123 gates on violations/warn only). CONFIRMED.
  P9 marker in the region bullet only → `skipped`, exit 0. Documented remedy works.
  P10 subsection heading with U+202E and ESC → escaped in human output (`‮\x1b`), no raw
     bidi/ESC in human or JSON output. Lens 4 holds for the new detail.
  P11 `--against=--output=<file>` → git receives `--output=<file>:<path>` as an OPTION; failed only
     because the target name ends in `:docs/...` (no such dir). Option injection reaches git; the
     flag predates the delta and its only caller is ci.yml (`HEAD^`). Pre-existing; note.
  P12 two commits pushed together, subsection edit in the FIRST → `--against HEAD^` exit 0 clean;
     `--against HEAD~2` exit 1. CONFIRMED: CI compares only the push's last commit (A4 fails).
  P13 `--check` prints "An edit under one of these is invisible to the co-change rule" for the
     "under mapped" rows the new check now reads. CONFIRMED (V5).
  P14 `_main` calls `render_human(findings)` with today=None → header and exit code read the clock
     separately (midnight boundary). note.
  P15 `####` under UNMAPPED `###` under mapped `##` → fires apex. Code right; untested (M7).
- MUTATIONS (mutate.py, scratch copy, 18 tests of the two new classes per run, ~14 s each):
  M1 fence handling removed from `_headings` → SURVIVED: test_a_fenced_heading... fences a level-1
     line, which `_headings` drops regardless, so the test proves nothing about fences.
  M2 occurrence counting dropped → SURVIVED (no duplicate-heading test).
  M3 bullet-marker check removed (body only) → SURVIVED (no bullet-marker subsection test).
  M4 `<` → `<=` → CAUGHT (10 failures).  M5 line +7 → SURVIVED (no line assertion).
  M6 json `until` wrong → SURVIVED.  M7 nearest-MAPPED-ancestor → nearest ancestor → SURVIVED
     (a false-negative mutation: no `####`-under-unmapped-`###` test).
  M8 `moved` on one side → CAUGHT.  M9 `--against` guard inverted → CAUGHT.
- A3 on the real docs (a3_real.py): all 12 mapped slices end where the fence-aware reader puts the
  next heading; PROPAGATION.md has 2 fence-blind heading-like lines (134, 376), both outside any
  mapped slice. P6's gap is latent today, not live.
- Lens 4 ASVS check: fetched OWASP ASVS 5.0 chapter V1 (raw GitHub, 2026-11-22): 1.1.2 output
  encoding as the final step before the interpreter; 1.2.5 OS command injection / parameterised
  calls; no explicit bidi requirement. Mapped to P10 (met) and P11 (pre-existing seam).
- `docs/ROADMAP.md` grep for "2027-01|before the flip|before each flip|re-probe|fleet probe": no
  hit → SU14 (nothing visible schedules the pre-flip probe). Barred records may hold it; act 2.
- README blockscan section at HEAD (line 2655, 2663) still carries the delta's text; 50 commits
  touched README/CHANGELOG since, none changed the blockscan wording except attribscan's
  cross-reference "four weeks after blockscan's sub-section date" (README:502).
- 21:14–21:25 UTC: Status line updated; act-1 verdict appended below `---` (14 findings: SU1–SU14;
  0 MAJOR, 4 MODERATE, 6 minor, 4 notes; PASS-WITH-FINDINGS). Gates over the brief: datescan exit 0
  clean; reviewscan exit 0 (sibling split intact); spellscan and wrapscan exit 0 but ignore
  docs/reviews by their ignore files (scanned nothing) → width checked by awk, lines >100 rewrapped
  to ≤100. `git status`: only ` M` the brief and the expected ` D` sibling. No git write run.
- Left out and why: `/security-review` skill not run (reads this session's pending diff = the
  partition deletion only; discharged by grounds in the verdict). No live write of any kind. The
  heading-level collision (`###` vs `####` same text) not probed in the real docs (none exists).
- Scratch: tools_copy/, tools_old/, replay.py, fleet_probe.sh, probes.py, probes2.py, mutate.py,
  a3_real.py in the session scratchpad; scratch git repos were deleted by the probe scripts.
  Scratchpad to be removed at the fold.
- ACT 1 complete; waiting for the orchestrator to release the sibling's path.

## Act 2 (released by the orchestrator after act-1 commit 8f3c698a)

- Opened: the held sibling (10 questions + the brief-writer's runs); `git log -1 --format=%B
  6a4eeee2`; queue pointer 160/1320; 320/340 whole; 320/810 whole; docs/reviews/2026-10-03-0158-
  cover-switch-unmapped-headings-cold.md lines 417–424 and 449–456 only (CU5, CU10). Not opened:
  docs/sessions, docs/SESSIONS.md, docs/ROADMAP-DONE.md, other prior verdicts.
- Q7 check: `git show <rev>:tools/test_blockscan.py | grep -c '^    def test_'` → 35 at
  6a4eeee2~1, 53 at 6a4eeee2, 58 at HEAD → +18; commit body says +19 (SU17, note).
- Q8 check: `git log -1 --format=%ci 6a4eeee2` → 2026-11-10 02:55:39 +1300 = 2026-11-09T13:55:39Z;
  CHANGELOG heading 2026-11-10; CONVENTIONS.md row "Time: UTC at rest" (SU15, minor).
- Q3/Q4 probes (probes3.py, scratch repo deleted): Q3a removed subsection → exit 1; Q3b marker in
  template bullet only → skipped, exit 0. Q4a unmapped ### promoted to ## → its #### and itself
  reported as changed under the OLD bullet (apex), exit 1, no wrong bullet. Q4b mapped ### demoted
  → stale-heading ×2, exit 2 (fail-safe).
- Sibling Q5's "second-parent side of a merge lands green" judged wrong: HEAD^ is the first parent,
  so a merge commit's first-parent diff carries the merged side; only a fast-forward reduces to P12.
- 810 whole records "Each flip needs a fresh fleet probe before its date" as open [ ] items → SU14
  reworded (recorded, undated, ungated), severity unchanged.
- Appended `### Reconcile`; Status line updated. Final: 0 MAJOR, 4 MODERATE, 7 minor, 6 notes (17);
  SU15–SU17 formed at reconcile. Gates: datescan, reviewscan run after the append (results in the
  terminal record); width check by awk ≤100. No git write; sibling not folded or deleted by me.
- Scratch left for the orchestrator's fold/cleanup: the session scratchpad (tools_copy/, tools_old/,
  *.py helpers, fleet_probe.sh). No scratch git repo remains (each probe script removed its own).
- datescan re-run after fixing 'today' → '2026-11-22' on the SU14 reconcile line: clean, exit 0; width ≤100 confirmed.
