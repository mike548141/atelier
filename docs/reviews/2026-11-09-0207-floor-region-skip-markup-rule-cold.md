# Cold pass — `pathscan` skips a child's inlined floor region, and `conflictscan` reports tool-call markup as an advisory

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4 (a guard or a rule is doctrine by
function, rule 3).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** PASS RAN, acts 1 and 2 complete, folded 2026-11-22 UTC — PASS-WITH-FINDINGS (0 MAJOR,
2 MODERATE, 5 minor, 3 note), by a Fable 5.1 reviewer under orchestrator session `e55d14f5`
(drain session `eca14b23`), on the principal's drain order of 2026-11-23 NZDT. The sibling is folded
below the verdict. Every finding awaits the principal's decision (rule 3). Brief written 2026-11-09
UTC by session `d4a0fcf3`, a headless Opus 5.5 brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/997-rule-4-cold-pass-queued-floor-region-skip-and-markup-rule.md`.
**Size of this pass:** medium: two commits, about 280 lines across two scanners that reach every
child's next CI run.
**Why it earns a review:** Both scanners reach every child's next CI run. The worst failure is a
broken path or a leaked markup line passing because a skip or an advisory tier covers more than it
says.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `4c65083c`,
  2026-11-03, and the Sonnet worker it dispatched, which wrote the code (per the queue pointer). The
  author queued this pass and does not take it.
- **Who wrote this brief:** session `d4a0fcf3` (`claude-opus-5-5`), a headless brief-writer started
  2026-11-09 UTC by coordinating session `74f2b8cd` (Opus 5.5), on the principal's request to brief
  every owed pass. Neither wrote any of this delta. **Off-tier for review, disclosed: the
  brief-writer forms no finding and writes no severity**, and stops after writing. It ran no review
  and used no Fable model. `74f2b8cd` built none of these subjects and forms no finding; its launch
  prompt is the brief-writer's only instruction.
- **Barred from running this pass:** session `d4a0fcf3` and session `74f2b8cd` (whoever writes a
  brief does not run it, the principal's rule), and the author session named above with everything
  it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `74f2b8cd`: the
  item numbers, the rules of the run, and the statement that it built none of these subjects. It
  carried no framing of the work. The brief-writer had no contact with the author session or its
  workers.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md` and `docs/method/REVIEW.md` whole; the board
  item whole; the intent records' opening part and every line naming the principal or a landing
  account; every delta commit body-free through `tools/coldsweep.py --commit`; commit subjects
  through `git log`; `docs/reviews/2026-11-06-2027-secretscan-public-pem-spans-cold.md` whole,
  **including that pass's verdict and folded sibling** (a different subject, read for house form),
  the acceptance-test section and the status and overall verdict lines of
  `docs/reviews/2026-10-26-0928-g3-grace-metadata-sets-cold.md` (the counts only), and the opening
  30 lines of board item `160/980`; three lines of `docs/SESSIONS.md` and the opening of
  `docs/sessions/2026-11-06-2022-fable-passes-850e.md`; the results of the re-run lines below. It
  did **not** open any other prior verdict or any delta commit's message body. Its harness also
  loaded user-level and repo instruction files and a memory index, which hold private context this
  brief does not carry. Everything evaluative it formed is in the sibling.

## The acceptance test

No record the brief-writer read carries a ruling of the principal's on either design. Judge each
against its own hand-up's stated problem (barred below until phase 2) and `docs/method/GUARDS.md`;
the delta's docstrings state what it takes the problem to be.

## What the work is

- **`24ac5b8`** — `pathscan: skip a child's inlined floor region, which stampscan checks (320/610)`.
- **`92dd817`** — `conflictscan: report tool-call markup saved into a written file, as an advisory
  (320/490)`.

Delta paths, read at each commit and at HEAD:

- `tools/pathscan.py`, `tools/test_pathscan.py`, `tools/conflictscan.py`,
  `tools/test_conflictscan.py`, `tools/floor.py`, `tools/test_floor.py`, `tools/README.md`,
  `.conflictscanignore`, `CHANGELOG.md`

First confirm the tree holds the delta, then read each commit body-free:

```
git merge-base --is-ancestor 92dd817 HEAD; echo $?
python3 tools/coldsweep.py --root . --commit <sha> --path tools/pathscan.py --path \
  tools/test_pathscan.py --path tools/conflictscan.py --path tools/test_conflictscan.py --path \
  tools/floor.py --path tools/test_floor.py --path tools/README.md --path .conflictscanignore
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). The commit also touches board records; those are barred until phase 2, so always pass `--path`.

Then see what has landed on those paths since, and read anything new the same way, only as far as it
bears on this delta at HEAD: `git log --oneline 92dd817..HEAD -- tools/pathscan.py
tools/test_pathscan.py tools/conflictscan.py tools/test_conflictscan.py tools/floor.py
tools/test_floor.py tools/README.md .conflictscanignore`.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the author's claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1).

- The skip applies "exactly where the canonical source is NOT in the tree"; where it is, "the
  stamped copy there can be checked against the tree, and it still is".
- The text between the markers is "copied word for word" and `stampscan` checks it, so it is not
  silent.
- "Markers count only outside a fence"; "an unterminated begin skips to end of file; stampscan
  reports that as malformed".
- A test pins pathscan's copy of stampscan's markers in step.
- Tool markup is "reported and counted … but never gating", and the flip to blocking "is one edit".
- "Everything above about the four conflict shapes is unchanged and still blocks."
- `clean` is now false for advisory findings while `blocked` tracks the exit code.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope,
and a non-goal that fences off the risk is a finding.

**Non-goals:** the tool-markup rule's flip to blocking (`320/780`); `conflictscan`'s merge-conflict
shapes as reviewed earlier.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else. Is
   this the right problem, solved at the right altitude and in the right shape, against the
   acceptance test?
2. **Correctness & quality.** Re-drive the claims above. Record each overclaim against the text that
   makes it.
3. **Completeness / harvest.** Every surface that states this behaviour (V3); one home (V4); no
   contradiction (V5). Find tests that would stay green on a broken delta by mutating a scratch
   copy.
4. **Security & privacy**, mandatory: at design altitude what this exposes, over-collects or leaks
   by weakness of design; at code altitude the likely vectors for its class, checked against an open
   catalogue (OWASP ASVS or the domain's equivalent). Aim `/security-review` at code only from a
   clean tree, as *House rules* says; weigh a clean pass over markdown as nothing.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-09 UTC, from the worktree root,
in the foreground or under `nice`; its results are held in the sibling. Read exit codes explicitly.
Check `uptime` first and run the heavy lines under `nice -n 10`. Use the `python3` first on the
machine's `PATH`.

```
python3 -m unittest discover -s tools -p test_pathscan.py
python3 -m unittest discover -s tools -p test_conflictscan.py
python3 tools/pathscan.py --selftest
python3 tools/conflictscan.py --selftest
python3 tools/conflictscan.py --root . . --json
nice -n 10 python3 -m unittest discover -s tools
```

## House rules for this run

- **Live systems:** read-only reads of live systems as needed; no live writes. A check that needs a
  write is marked NOT RUN, with why. No push, no write to GitHub, no network service changed.
- **Never print a secret** or any personal data. Probes use scratch copies and synthetic fixtures
  under your scratchpad, deleted when you finish.
- Name your own review worktree in the verdict. It is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad. Child
  repos are read-only and reported by count only, never by name or path.
- One heavy process at a time, foreground, with a long timeout. Never run an installed tool by bare
  name from `PATH`: use `python3 tools/<x>.py` or `instruments/<x>` from your worktree.
- `/security-review` reads the session's pending diff, not this delta. Aim it at the code by
  reproducing the diff in a scratch clone, or discharge it by grounds and do the code-altitude read
  by hand, never with this brief or its sibling dirty.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo is
  PUBLIC: quote no secret, email address, private repo name or path.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, this brief's sibling (a held-back file, now folded below the verdict under *Deferred sibling*; by
count: 7 questions, 0 facts), every other item under `docs/roadmap/160-doctrine-review-owed/` beyond
its title, every delta commit's message body, and these intent records beyond their first line:

- `docs/roadmap/320-child-filed-findings-via-pointing-up/610-the-floor-names-a-path-no-child-can-resolve.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/490-tool-call-markup-leaks-into-written-files-and-no-scanner-sees-it.md`

The delta's own docstrings, comments, README, design note and `CHANGELOG.md` entries carry the
author's account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/610-the-floor-names-a-path-no-child-can-resolve.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/490-tool-call-markup-leaks-into-written-files-and-no-scanner-sees-it.md \
  'floor_region_skipped|_FenceState|TOOL_CLOSE_RX|TOOL_OPEN_RX|tool-markup|advisory_over_cap'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions and the re-run
list. Append your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, any orchestrator, what you read, the UTC day), per-lens answers, V1–V7 each
answered or discharged with grounds, each load-bearing assumption damaged or confirmed with its
probe, a per-commit ledger (read body-free yes/no, findings by id), findings with stable IDs (prefix
`FK`: `FK1`, `FK2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit bodies;
append `### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The work is doctrine by function, so every finding is the principal's to decide (rule 3): record
all, apply nothing. Counsel per finding is welcome, labelled as counsel and kept beneath it.

---

## Verdict — act 1, cold pass run 2026-11-22 UTC

**Overall: PASS-WITH-FINDINGS — 0 MAJOR, 2 MODERATE, 4 minor, 2 note.** Both scanners do what
their tests say on the shapes they name; the two MODERATE findings are on what the delta *says*
licenses its two softenings (a checker that does not run where the skip applies; a deferment with
no end date), not on the code's behaviour.

### Provenance (rule 4, V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named tier, checked at selection.
- **Spawn chain:** started by headless per-pass orchestrator session `e55d14f5` (Opus 5.5), itself
  started by drain session `eca14b23` (Opus 5.5), under the principal's weekly drain order of
  2026-11-23 NZDT, verbatim: *"Start a fable drain or whatever it is called now. Target 100% of
  weekly budget by 11.30am NZT todat"*. Both are rule-4 off-tier orchestrators: they hold the
  context partition, form no finding and write no severity. Neither wrote the brief or the delta;
  `eca14b23` wrote no brief and no delta and started no brief-writer for this pass. I was not
  started or instructed by `d4a0fcf3`, `74f2b8cd` or `4c65083c`, nor by anything `4c65083c` started.
  No contact from any author or brief-writer reached me during the pass.
- **Orchestrator direction, recorded by the receiver:** process only — paths, the barred set, the
  log's location and shape, load rules, what I may write, the two-act sequence and the release
  message to come. It carried no question about the delta, no pointer to where risk lives and no
  request about any finding. The spawn prompt is in the review log appended at the fold, verbatim,
  under *Spawn prompt*.
- **Review tree:** `/Users/mike/worktrees/fable/atelier-160-997-2004/atelier` at HEAD `755185a9`,
  read-only to me except this file. The `.deferred.md` sibling shows as deleted there on purpose;
  I did not look for it anywhere. Scratch probes ran in the session scratchpad and were deleted.
- **What I read (rule 2):** this brief whole; `docs/method/REVIEW.md` and `docs/method/GUARDS.md`
  whole; the two delta commits body-free through `coldsweep --commit` with `--path` on the nine
  delta paths (the board files the commits touch were left out); the delta files at HEAD;
  `tools/stampscan.py` lines 1–60, `tools/pins.py`, `tools/floorhook.py`, `tools/floor.py`,
  `tools/allowmarker.py`, `tools/report.py` and `tools/estate.py` where the probes needed them;
  `docs/build/templates/CLAUDE.md`; board item `320/780` whole (the brief's non-goal, not barred);
  `git log --oneline` subjects on the delta paths since the landing (neutral subjects; none reads
  as an account of this delta). I skipped the session-log step and opened no file under
  `docs/sessions/`, `docs/reviews/` (other than this brief), `docs/SESSIONS.md` or
  `docs/ROADMAP-DONE.md`, no other `160/` item beyond its title, no commit body, and neither
  `320/610` nor `320/490` beyond its first line. The brief's `coldsweep` sweep ran as written
  (exit 0, 63 hits over 748 files, 1017 barred files excluded) and showed `320/780`'s title. My
  harness also loaded user-level and repo instruction files and a memory index, which hold private
  context this verdict does not carry; nothing in them concerns this delta.
- **Interpreters:** the brief's six re-run lines used the `python3` first on `PATH` (3.14.6), as
  the brief says; every other command used `/usr/bin/python3` (3.9.6). Heavy runs were niced and
  run one at a time; `uptime` load was 5.5–10.6 during the pass.
- **Date of the pass:** 2026-11-22 UTC (20:06Z to the time of writing).

### Method

The full step-by-step record (every command, file and line range, and what it returned) is the
review log appended at the fold. In order: brief → REVIEW.md and GUARDS.md → both commits
body-free → HEAD files → my own assumptions A1–A5 (below) → the facts behind each (stampscan's
wiring, the floor registry, pins/floorhook, dated-grace precedents, the ignore-file grammar) →
probes P1–P4 (synthetic child; regex cost; seven mutations on a scratch copy with a control; a
count-only estate probe) → the six re-run lines → this verdict. Left out: child repos' records and
any live network system (the subject is two local scanners; nothing live bears on it).

### Lens 1 — approach and assumptions, named first

- **A1 — "stampscan checks the floor region in a child, so skipping it is not silent."** DAMAGED.
  `stampscan` is wired `--warn` in atelier's own `ci.yml` only (`tools/stampscan.py` lines 15–33:
  "deliberately NOT in the `floor.py` registry, NOT in the reusable `floor.yml`, and NOT in the
  pre-commit hook"; `grep stampscan tools/floor.py` → nothing; `floor.yml` absent). A child's copy
  is checked by `pins --floor` (atelier-side, or by hand) and `floorhook` (warn-only SessionStart);
  neither runs on a child's hook or CI plane (`grep -rn "pins.py|--floor|floorhook"
  docs/build/templates .github/workflows` → nothing). `pins` blocks only from 2026-12-09. → FK1.
- **A2 — "the skip hides only what it must."** CONFIRMED today, by construction not by guard: the
  region names one unresolvable path (`method/TOOLBOX.md`); the skip hides exactly one finding in
  each of 22 stamped repos and none in 7 unstamped (P1, P4). Nothing pins that inventory. → FK6.
- **A3 — "the regexes recognise the leak the rule exists for."** CONFIRMED for the closers: the
  estate's tracked files hold `</content>` ×2 and `</invoke>` ×1 and no other closing-tag shape
  (P4), all caught (one repo, 3 advisories). NOT GROUNDED for the openers: 0 instances, no cited
  incident, and no negative test pins the shape set (M4 survives). → FK5.
- **A4 — "an undated in-tool advisory is a deferment with no expiry."** CONFIRMED. No date
  constant in `conflictscan.py`; ten sibling grace periods carry one; `320/780` is event-dated on
  a probe nobody is scheduled to run. → FK2.
- **A5 — "the text at HEAD agrees with the code."** DAMAGED in three places of `conflictscan.py`;
  `pathscan.py`'s text agrees with its code. → FK3.

Right problem, right altitude? Both are real defects with real corpus instances (one spurious
warning per child; three leaked lines in one child today). The pathscan fix is at scanner altitude
where a narrower, parent-side fix exists (FK6, counsel); the conflictscan fix is the right shape
(a fifth line rule in the scanner that already walks every tracked file), softened in the one way
the registry allows a never-softenable check to be, with the softening's end left open (FK2).

### Lens 2 — correctness and the delta's claims, re-driven

| Claim (brief § *The claims*) | Result | Evidence |
|---|---|---|
| Skip applies exactly where the canonical source is NOT in the tree | holds, by filename only | `floor_region_skipped` = `not (root/FLOOR_SOURCE).is_file()`; M3 caught; FK8 |
| Region text is checked by `stampscan`, so not silent | overclaim | A1; FK1 |
| Markers count only outside a fence; unterminated begin skips to EOF | holds | tests `marker_inside_a_fence`, `fence_inside_the_region`, `unterminated_begin`; M2 caught |
| Unterminated begin is reported as malformed | holds via `pins`, not `stampscan` | `pins.check_copy` → `('malformed', 'stamp:begin at line 19 was never closed…')` |
| A test pins pathscan's regex copy to stampscan's | holds | `test_regexes_and_floor_identity_match_stampscan` |
| Tool markup reported and counted, never gating | holds | `report.exit_code(blocking_total)`; M6 caught; JSON re-run `blocked: false` |
| The flip to blocking "is one edit" | overclaim | two `blocks=False` sites + selftest filter + four tests + README/CHANGELOG; FK3 |
| Four conflict shapes unchanged and still block | holds | 88 tests OK; `_line_finding` lines 383–402 unchanged; selftest exit 1 on markers |
| `clean` false for advisory, `blocked` tracks exit | holds | `test_json_shape_carries_blocking_and_advisory_counts`; comment at 779–780 |

### Lens 3 — completeness and harvest

Surfaces that state each behaviour (V3): pathscan docstring step 1b, `floor_region_skipped`,
`_FenceState`, `tools/README.md` § *A child's inlined floor is not scanned*, `CHANGELOG.md`;
conflictscan docstring § *A fifth shape*, the `TOOL MARKUP` comment, `tools/README.md` § *A fifth
shape, advisory*, `CHANGELOG.md`, `floor.py`'s registry comment. No template, skill or `method/`
doc states either (grep), so there is no second home to drift (V4); the stamp regex copy is a
stamped copy pinned by test. Tests that stay green on a broken delta: M4 and M5 (lens 1 A3; FK5).
Harvest: `allowmarker`'s dated-grace pattern (`MALFORMED_GRACE_UNTIL`) and `pins`'s
`COPY_BLOCKS_FROM` were available and not used (FK2); the parent-side allow-marker route was
available and not weighed in the text (FK6).

### Lens 4 — security and privacy

Design altitude: neither scanner collects or transmits anything new; both read tracked files they
already read. The advisory excerpt prints at most 100 characters of a line that begins with a tag,
and `.conflictscanignore` names two file paths already public in this repo. Code altitude, checked
against OWASP ASVS V5 (input validation) for this class — a text scanner over untrusted repo
content: no shell or eval from content; the ignore file is reasoned or exit 2; one regular
expression has super-linear backtracking on crafted input (FK4, measured in P2); `TOOL_CLOSE_RX`
and `TOOL_OPEN_RX` are linear (3.2 ms on a 4 MB rest). `/security-review` discharged with grounds:
it reads the session's pending diff, which in this worktree is the removed sibling and this brief,
not the landed delta; and its exclusions bar markdown, so a clean pass over the doc half would weigh
nothing. The code-altitude read was done by hand as above.

### The standing checklist

- **V1** — three claims stronger than their evidence: FK1, FK3, FK5.
- **V2** — all six re-run lines re-run (ledger below). `CHANGELOG.md`'s "exactly one finding fewer
  in each child that stamps the floor" re-run over 29 repos: true (22 × 1, 7 × 0). `320/780`'s
  "8 in three children" re-probed: now 3 in one.
- **V3** — swept; no mirror site missed (lens 3).
- **V4** — one home each; the regex copy is stamped and pinned.
- **V5** — FK3 (three self-contradictions in `conflictscan.py`). Cross-reference checked for the
  rule reached, not the file found: pathscan's "`stampscan` checks it" reaches a file that holds no
  rule running in a child (FK1).
- **V6** — lens 4 run; `/security-review` discharged with grounds.
- **V7** — provenance stated above and in the brief.

### Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `24ac5b8` pathscan floor-region skip (320/610) | yes, `coldsweep --commit` with `--path` | FK1, FK4, FK6, FK8 |
| `92dd817` conflictscan tool-markup advisory (320/490) | yes, same | FK2, FK3, FK5, FK7 |

### Findings

Every finding is the principal's to decide (rule 3; both scanners are doctrine by function). I
applied nothing. Counsel is labelled and kept beneath each.

**FK1 — MODERATE — The skip's stated licence is a check that does not run where the skip
applies.** `tools/pathscan.py` (step 1b, `floor_region_skipped`, `_FenceState`), `tools/README.md`
and `CHANGELOG.md` all say the region is skipped because "`stampscan` checks it against the
canonical copy", and that an unterminated begin "is not silent" because stampscan reports it.
`stampscan` runs `--warn` in atelier's own CI and nowhere else (`stampscan.py` 15–33; absent from
`floor.py`; `floor.yml` does not exist). On the planes where the skip applies — every child's hook
and CI — nothing checks the region at that moment; the check that does exist (`pins --floor`,
`floorhook`) is atelier-side or session-start, warn-only until 2026-12-09, and absent from the child
template's CI. GUARDS § *Before building a check*: the fact that licenses the skip ("that text is
checked elsewhere") is outside pathscan's window and, as named, false. What limits the harm, and
why this is not MAJOR: pathscan is itself `--warn` in every child (`floor.py` 1030–1039), so the
skip retires one warning line per child rather than a gate, and the region names one unresolvable
path today (P1, P4). *Counsel:* name the real checker and its tier in the three surfaces
("`pins --floor` / `floorhook`, warn-only, blocking from 2026-12-09, run from atelier"), or put
the floor-copy check on the child planes before the text claims it.

**FK2 — MODERATE — The tool-markup advisory is a deferment with no end date.** The docstring
(lines 83–100) and comment (295–302) say "for now", "once the estate is clean", and route the end
to `320/780`, whose done-condition is a probe that nobody is scheduled to run ("Re-run the same
probe to see which are still open"). GUARDS § *Acceptance and deferment*: "Deferment … carries a
reason **and an expiry** … a deferment that cannot lapse is an acceptance that never admitted what
it was"; § *Ruled 2026-11-09*: "a lowering with no end date is not a lowering this model allows."
The estate's other graces carry a printed date (`allowmarker.MALFORMED_GRACE_UNTIL`,
`pins.COPY_BLOCKS_FROM`, `blockscan.SUBSECTION_WARN_UNTIL`, `attribscan`, `namescan`, `pdlistscan`,
`quotescan`, `leakscan`, `board`, the `sizescan` bar in `floor.py`). The brief's non-goal (the flip
itself) does not fence this: the question is the shape of the softening as landed, not when it
flips. The corpus has moved towards the flip since (3 advisories in one repo now, from 8 in three
on 2026-11-06). *Counsel:* a `TOOL_MARKUP_BLOCKS_FROM` date on the `pins` pattern, printed on the
advisory count line so every child sees it, tests patching `_utc_today`; the date is the
principal's to set.

**FK3 — minor — `conflictscan.py` contradicts itself at HEAD (V5).** Lines 153–154 ("no `--warn`
— this check has no advisory form, so there is nothing to soften to") sit directly above line 155
("0 clean, or advisory (tool-markup) findings only"). Lines 220–221 ("Every finding here blocks
(conflictscan has no advisory tier), so one counter is enough") sit directly above the second
counter, `advisory_over_cap` (225). Lines 97–98 call the flip "one edit (the `blocks=False`
arguments …)", line 301 "one line (`blocks=True` at the call site)"; there are two sites (348–352,
354–357) and the flip also turns the selftest's `if f.blocks` filter (849), four tests
(`test_it_never_blocks…`, `test_json_shape…`, `test_blocking_and_advisory…`,
`test_reasoned_ignore_glob…`), the README and the CHANGELOG. `_line_finding`'s docstring (372–373)
still says it decides "a conflict-marker finding". *Counsel:* one tidy of the stale sentences;
state the flip as what it is.

**FK4 — minor (security, robustness) — The copied stamp regex is quadratic on crafted input, and
the delta puts it on every child's hook and CI.** `_STAMP_BEGIN_RX`'s
`narrow=(?P<narrow>.+?)…\s*-->` backtracks quadratically on `narrow=` followed by a long interior
whitespace run: measured through
`_FenceState(True).is_content`, 10 000 spaces → 413 ms, 40 000 → 7 031 ms; a 256 KiB window
(`LINE_WINDOW_BYTES`, `pathscan.py:841`) is minutes. `line.strip()` neutralises a trailing run,
not an interior one. The branch is reached only with `skip_floor=True`, which is exactly every
child (atelier: 0.0 ms). It needs a line opening `<!-- stamp:begin source=… region=… narrow=`,
so a crafted or badly mangled marker; pathscan is warn-only, so CI slows rather than reds, and a
hook commit stalls. The pattern is stampscan's (pinned equal by test), so the fix lands in both.
*Counsel:* check `stripped.endswith("-->")` before matching, or capture `narrow=` greedily with an
end anchor; keep the pin test.

**FK5 — minor — The two opener shapes are ungrounded and the shape set is pinned one way only.**
The comment (288, 293–294) says "The same leak can carry an opening line of a call" with no
incident cited; across 29 repos' tracked text there are 0 lines matching `<invoke name=` or
`<parameter name=` (P4), against 3 for the closers. GUARDS § *What every check declares*:
"Grounding and replay: each incident by reference, and for each the test that replays it." And a
mutant that also matches `</parameter>` passes the whole suite (M4): `test_anything_not_exactly_
the_shape_is_clean` lists no closing tag of another name, so nothing pins which closers are *not*
the shape. *Counsel:* cite the opener incident or mark the openers as speculative; add the nearest
non-shapes (`</parameter>`, a namespaced closer) to the negative test.

**FK6 — minor — The skip is wider than the one line that needs it, and nothing pins the
inventory.** GUARDS rule (a): the narrowest level and scope that covers the case. The region is 111
lines; one names an unresolvable path. Any path the floor later names — including a child-relative
one a child should hold — is hidden too, and no test asserts what the skip hides. A narrower route
was available and the text does not weigh it: the docstring says "the child cannot silence the
finding without drifting from the canonical text", which is true of the child and not of the
parent — a reasoned `pathscan:allow` on the canonical floor line travels verbatim into every copy,
is line-scoped, and needs no scanner change. *Counsel:* either route; if the skip stays, a test
that scans the canonical region as a child and asserts the hidden set is exactly
`{"method/TOOLBOX.md"}`, so the floor's next path edit has to update it.

**FK7 — note — `.conflictscanignore` exempts two whole files from both rules to quiet one advisory
line each.** The file declares the cost (lines 3–5) and the reason (append-only records,
`RECORD.md` 58, 312), which meets GUARDS (c). It is the widest mechanism available for a finding
that does not block; the alternative was two standing advisories on the board until the flip.
Recorded for the principal; no counsel.

**FK8 — note — Canonical-source identity is by filename.** `floor_region_skipped` treats any repo
holding a `docs/method/PROPAGATION.md` as holding the canonical source (and scans the region), and
any repo without one as a child. A child with a same-named file of its own gets the spurious
warning back; GUARDS § *Where a guard recognises its own work by a convention* asks that the
convention be stated where the guard lives. The docstring half-states it ("it IS atelier (or a
repo carrying the canonical source)"). *Counsel:* one sentence naming the convention.

### Overall

**PASS-WITH-FINDINGS — 0 MAJOR, 2 MODERATE (FK1, FK2), 4 minor (FK3–FK6), 2 note (FK7, FK8).**

### Re-run ledger (brief § *Re-run obligation*; `python3` = PATH 3.14.6; niced; one at a time)

| Line | Exit | Result |
|---|---|---|
| `python3 -m unittest discover -s tools -p test_pathscan.py` | 0 | Ran 172 tests, OK |
| `python3 -m unittest discover -s tools -p test_conflictscan.py` | 0 | Ran 88 tests, OK |
| `python3 tools/pathscan.py --selftest` | 0 | selftest OK |
| `python3 tools/conflictscan.py --selftest` | 0 | selftest OK |
| `python3 tools/conflictscan.py --root . . --json` | 0 | `clean: true`, `blocked: false`, counts 0/0, 2 files by ignore glob, 1763 files / 336 382 lines; two `allowmarker` notes on stderr about unparseable fixture markers in `test_conflictscan.py` (pre-existing, not this delta) |
| `nice -n 10 python3 -m unittest discover -s tools` | 0 | Ran 3382 tests in 1163 s, OK (second attempt; the first was cut off by a run-time limit under load 20 with no result line, and does not count) |

### Follow-up checklist (for the principal's decision; nothing applied)

- [ ] FK1 — name the real checker in three surfaces, or wire the floor-copy check onto the child
      planes.
- [ ] FK2 — a dated end to the tool-markup advisory, printed on every run.
- [ ] FK3 — tidy `conflictscan.py`'s stale sentences.
- [ ] FK4 — make the `narrow=` capture linear in both copies.
- [ ] FK5 — ground or mark the opener shapes; pin the negative shapes.
- [ ] FK6 — pin the hidden inventory, or move the allowance to the canonical line.
- [ ] FK7, FK8 — record only.
- [ ] Act 2: reconcile against the sibling (7 questions, 0 facts) and the commit bodies.

### Reconcile (act 2, 2026-11-22 UTC)

Read after act 1 was committed (`072e3f2a`): the held sibling (7 questions, 0 facts, the
brief-writer's re-run results), the two commit bodies, both intent records whole, the `160/997`
pointer, and the one prior record the sibling names
(`docs/reviews/2026-10-16-1510-expected-toolbox-cold.md`, the pass on the floor sentence that
introduced the path; it holds nothing on the child-side resolution). Act-1 text above is unrevised.

**The brief-writer's re-run results against mine.** Same six lines, same exits. Counts have grown
with the tree since 2026-11-09 (154 → 172 pathscan tests, 84 → 88 conflictscan, 2 643 → 3 382 in
the full suite, 1 167 s → 1 163 s). Its note that the system Python 3.9.6 cannot import four test
modules (`str | None` at module level) explains why the brief fixes `python3` to the PATH 3.14; the
two module suites and the mutations I ran on 3.9.6 imported fine, so nothing in the ledger depends
on that.

**Per seeded question.**

1. *Keys on the file's absence; a child with its own `docs/method/PROPAGATION.md`, or a parent
   that deletes it.* Found independently as **FK8** (note). The author's account (commit body,
   docstring) states the convention half-way; nothing names it as a convention. Unchanged.
2. *Who checks the skipped block if stampscan is warn-only or disabled in a child; "not silent" on
   every plane?* Found independently as **FK1** (MODERATE), and the answer is sharper than the
   question: `stampscan` does not run in a child on any plane; the checkers are `pins --floor` and
   `floorhook`, atelier-side or session-start, warn-only until 2026-12-09. The commit subject and
   body ("which stampscan checks") repeat the overclaim. Unchanged.
3. *A child's own text inside the markers, with a bad path, skipped silently; does stampscan run on
   every file pathscan does?* Partly **FK6**; and one new fact: `pins` and `floorhook` read only the
   child's root `CLAUDE.md` (`pins.py` lines 5, 88, 148 of `floorhook.py`), while pathscan skips a
   floor block in *any* file. Counted read-only across the 29 repos: 22 stamps in root `CLAUDE.md`
   and **9 more files in 8 repos** carry the floor stamp elsewhere; pathscan now skips those and no
   runner compares them. → **FK10, formed at reconcile.**
4. *`clean` false for advisories: did it keep its meaning?* Before the delta `clean` ⇔ exit 0;
   now `clean` can be false at exit 0. The docstring's "keeps its meaning — nothing found at all" is
   a redefinition in effect. No in-tree consumer reads conflictscan's JSON `clean` (grep of
   `tools/`, `instruments/`, workflows), and the README and CHANGELOG announce `blocked` and
   `counts`. No finding; recorded as answered.
5. *The ignore entries exempt two frozen records from the conflict-marker check too; proportionate?*
   **FK7** (note), unchanged. The body's "records are history and are not rewritten" is the stated
   ground; `RECORD.md` 58 and 312 carry the append-only principle.
6. *`TOOL_CLOSE_RX` on an indented or fenced quote; `TOOL_OPEN_RX` unanchored at the end — does the
   doctrine about this tool start a line with `<parameter name=`?* Tested and measured: an indented
   quote is clean by test (`test_anything_not_exactly_the_shape_is_clean`); the intent record and
   this brief quote the tags mid-line or in backticks; the JSON re-run over this tree found 0
   advisories and the estate count found 0 column-0 opener lines anywhere. No finding. (Act 1's
   **FK5** stands on the other side of the same regexes: the openers are ungrounded.)
7. *Can a flood of advisory findings consume the shared materialisation budget, so a real conflict
   marker is counted but never listed?* Yes, by construction: `Tally.take_finding_slot` draws both
   tiers from one `_materialized` counter (lines 240–252), so after 50 000 advisory findings a
   later conflict marker goes to `findings_over_cap` — it still moves the exit code to 1 and prints
   the over-cap line, but its path and line are never listed. `test_cap_counts_advisory_overflow_
   separately` pins exactly this split. Pathological (fifty thousand leaked lines first), and the
   gate still fires. → **FK9, formed at reconcile.**

**Against the author's account (commit bodies, intent records).** Both bodies say the floor skip
was *option 3* of `320/610`; the record also offered *option 2*, the allow-marker carried in the
canonical text, and neither the body nor the record says why 3 was chosen over 2 — this is FK6's
counsel, known to the author and not weighed in writing. Both bodies repeat "one edit" (FK3) and
"which stampscan checks" (FK1). The `92dd817` body's "children float at floor@main" is the blast
radius FK2 rests on. The `320/490` record names the real leak shape (`</content>` then
`</invoke>`), which the estate count confirmed, and proposes the two opener shapes without an
instance (FK5). The `320/610` record confirms pathscan is warn-only in children ("It is warn-only
there, so nothing blocks"), the mitigation that keeps FK1 out of MAJOR. Nothing in the records
changes any act-1 severity.

**FK9 — note, formed at reconcile — One materialisation budget for two tiers.** After 50 000
advisory findings a real conflict marker is counted, blocks, and is not listed by path. *Counsel:*
a separate budget per tier, or let blocking findings pre-empt an advisory slot.

**FK10 — minor, formed at reconcile — A floor stamp outside root `CLAUDE.md` is skipped by
pathscan and compared by nobody.** `pins`/`floorhook` read root `CLAUDE.md` only; the skip applies
to any file; 9 such files exist in 8 repos today. *Counsel:* either confine the skip to the file the
checkers read, or have `pins --floor` walk every stamped file.

**Overall, restated: PASS-WITH-FINDINGS — 0 MAJOR, 2 MODERATE (FK1, FK2), 5 minor (FK3–FK6,
FK10), 3 note (FK7, FK8, FK9).** Every finding is the principal's to decide (rule 3); nothing
applied.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-22)

The text below is the brief's `.deferred.md` sibling, verbatim, held out of the review tree until
the reviewer's act 1 was committed (`49427c4d` on main) and released to the reviewer for
act 2 only. Orchestrator session `e55d14f5` folded it here unchanged and removed the sibling file;
it forms no finding and assigns no severity. The sibling's own headings are kept as written.

# Sibling to the floor-region-skip-markup-rule cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-09-0207-floor-region-skip-markup-rule-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-11-09 UTC by the brief-writer, session `d4a0fcf3` (Opus 5.5), named in the
brief's provenance; it forms no finding and assigns no severity. Fold this file in below the
reconcile and delete it at phase 2.

## Re-run results held back from the brief

Run once by the brief-writer, 2026-11-09 UTC, from the worktree root at `b1f9499`, machine load
averages 10 to 22 throughout:

- `python3 -m unittest discover -s tools -p test_pathscan.py`: exit 0 (Ran 154 tests).
- `python3 -m unittest discover -s tools -p test_conflictscan.py`: exit 0 (Ran 84 tests).
- `python3 tools/pathscan.py --selftest`: exit 0 (selftest OK — pathscan).
- `python3 tools/conflictscan.py --selftest`: exit 0 (selftest OK — conflictscan).
- `python3 tools/conflictscan.py --root . . --json`: exit 0 (}).
- Full suite, `nice -n 10 python3 -m unittest discover -s tools`, Python 3.14.6: 2,643 tests, OK,
  exit 0, 1,167 s. An earlier run on the system Python 3.9.6: 2,307 tests, 4 import errors
  (`test_floor`, `test_floorfleet`, `test_personal_data`, `test_precommit`: a module-level `str |
  None` annotation) and 1 timeout under load (`test_spellscan.BoundedMemory`, which passed alone on
  3.14).

## Prior records on nearby surfaces (named by filename, not opened unless the brief says so, not exhaustive)

- `docs/reviews/2026-10-16-1510-expected-toolbox-cold.md`

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. The skip keys on the file's absence: a child that holds a `docs/method/PROPAGATION.md` of its
   own, or a parent that deletes it. Does the test then flip for reasons nothing states?
2. Who checks the skipped block if `stampscan` is warn-only or disabled in a child? The docstring
   says "not silent": is that true on every plane and for a child that disables it?
3. A child's own text placed inside the stamp markers, with a bad path: skipped silently. An
   unterminated `stamp:begin` near the top of a long file skips the rest. Does stampscan run on
   every file pathscan does?
4. `clean: not findings and not blocking_total and not advisory_total`: the docstring says `clean`
   keeps its meaning. Did it? A consumer gating on `clean` sees a new false.
5. The `.conflictscanignore` entries exempt two frozen records from conflict-marker checks too,
   which the comment names. Is that hole proportionate, given the rule is advisory and an
   allow-marker cannot be added?
6. `TOOL_CLOSE_RX` needs the whole line; an indented or fenced quote of the markup? `TOOL_OPEN_RX`
   has no end anchor: prose or docs that start a line with `<parameter name=`? The doctrine about
   this tool does that.
7. The cap accounting (`advisory_over_cap`): can a flood of advisory findings consume the shared
   materialisation budget, so a real conflict marker is counted but never listed?

## Facts held back from the brief

None.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

# Review log — atelier 160/997, floor-region skip + tool-markup advisory (cold pass)

Reviewer: Fable 5.1 (claude-fable-5-1), tier checked at selection. Spawned by orchestrator session
e55d14f5 (Opus 5.5), itself started by drain session eca14b23 (Opus 5.5); both off-tier rule-4
orchestrators holding the context partition, forming no finding, writing no severity. Neither wrote
the brief or the delta. Not started or instructed by d4a0fcf3, 74f2b8cd or 4c65083c.
Review tree: /Users/mike/worktrees/fable/atelier-160-997-2004/atelier (HEAD 755185a9).
Brief: docs/reviews/2026-11-09-0207-floor-region-skip-markup-rule-cold.md.
Scratchpad for probes: the session scratchpad only; deleted at finish.
All commands run from the review tree with `git -C` / absolute paths; `/usr/bin/python3` unless a
re-run line says `python3` (noted per line).

## Act 1

### Step 1 — orientation (2026-11-22T20:06Z)
- Read the brief whole (lines 1–212). Barred list noted: ROADMAP-DONE, SESSIONS, docs/sessions/,
  prior verdicts, the .deferred sibling (shown deleted in the tree; expected, not sought), other
  160/ items beyond title, delta commit bodies, the two 320/ intent records beyond line 1.
- `uptime`: load 5.55 (16 GB laptop, several passes running). Heavy lines will run under nice.
- `git status --short`: only ` D` of the sibling. `git rev-parse HEAD` = 755185a9.
- `git merge-base --is-ancestor 92dd817 HEAD` exit 0; same for 24ac5b8 exit 0. Delta is in HEAD.
- Reading docs/method/REVIEW.md (835 lines) whole for verdict shape and V1–V7; docs/method/GUARDS.md
  (780 lines) whole as the acceptance-test yardstick the brief names.

### Step 2 — the delta, body-free (2026-11-22T20:10Z)
- `/usr/bin/python3 tools/coldsweep.py --root . --commit 24ac5b8 --path <the 9 delta paths>`: exit 0;
  subject + stat + diff of 4 files (CHANGELOG.md, tools/README.md, tools/pathscan.py,
  tools/test_pathscan.py); 2 board files left out by default; body not printed. Read whole.
- Same for `--commit 92dd817`: exit 0; 7 files (.conflictscanignore, CHANGELOG.md, tools/README.md,
  tools/conflictscan.py, tools/floor.py, tools/test_conflictscan.py, tools/test_floor.py); 3 board
  files left out by default (incl. the 160/997 pointer and the 320/490 intent record). Read whole
  from the saved tool output. coldsweep's note: `--path` for files a commit did not touch printed a
  "matched no changed file" note; harmless.
- `git log --oneline 92dd817..HEAD -- <8 delta paths>`: about 80 commits touch these paths since the
  landing (shared tool files; e.g. 115/130 coverage lines, 160/xxx applications). None by subject is
  a follow-up to 320/610 or 320/490. So I review the delta AS IT STANDS AT HEAD (755185a9), reading
  the HEAD files, and use the two commit diffs to know what the delta introduced.
- Read docs/method/REVIEW.md whole (verdict shape, rules 1–4, V1–V7, method-record requirement) and
  docs/method/GUARDS.md whole (narrow/noisy/reasoned/declared; acceptance vs deferment; "a repo may
  lower a check's response only with a written reason and an end date"; a guard that cannot
  recognise the state it exists to detect is not a guard; evidence window).

### Lens 1 — my own load-bearing assumptions, named before probing
A1. (pathscan skip) "stampscan checks the floor region in a child, so skipping it is not silent"
    holds only if stampscan (a) runs in a child's CI, (b) can reach the canonical text there, and
    (c) is enforced, not advisory/disabled. To probe: floor.py registry, stampscan.py child path.
A2. (pathscan skip) The skip is whole-region, keyed on the root lacking docs/method/PROPAGATION.md.
    Probe: what else the region could hide (child-relative paths), and a child holding a same-named
    file of its own.
A3. (conflictscan markup) The regexes recognise the leak the rule exists for. The opener matched is
    `<parameter name=` but the closer matched is `</content>`, not `</parameter>`; the harness's real
    tags may carry a namespace prefix. Probe: tag shapes present in tracked files across the estate
    (count only), and the delta's own fixtures.
A4. (conflictscan markup) An undated in-tool advisory tier is a deferment with no expiry. Probe:
    GUARDS § Acceptance and deferment; the house's dated-grace precedents (leakscan G3, blockscan,
    allowmarker MALFORMED_GRACE_UNTIL).
A5. (both) Comments/docstrings at HEAD agree with the code (V5). Probe: read HEAD files.

### Step 3 — HEAD reads and the facts behind A1–A5 (2026-11-22T20:12Z to 20:20Z)
- Read tools/conflictscan.py whole at HEAD (894 lines). Delta code at HEAD: lines 83–100 (fifth
  shape docstring), 153–157 (exit codes), 220–225 (Tally cap counters), 285–307 (TOOL_* constants),
  318–324 (Finding.blocks), 332–358 (advisory_count_line, _tool_markup_finding), 361–367 (_record),
  403 (_line_finding falls through to tool markup), 637–699 (render), 773–798 (totals, JSON, exit).
- Read tools/pathscan.py lines 730–830 at HEAD (stamp regex copy, floor_region_skipped, _FenceState
  with in_region) and grep of `skip_floor` sites (lines 1302–1323: scan_text/scan_file derive it from
  root). pathscan has no --staged mode: whole tree on both planes (floor.py 1014–1030), and its
  registry entry is `--warn` on hook, ci AND advisory (floor.py lines 1030–1039 by grep): pathscan is
  warn-only in every child. So the skip removes a WARNING line, never a block.
- Read tools/stampscan.py lines 1–60: "REVIEWED, WIRED ADVISORY IN ATELIER ONLY … deliberately NOT in
  the floor.py registry, NOT in the reusable floor.yml, and NOT in the pre-commit hook … any
  scaffolded child that ran this scanner would exit 2". `grep -n stampscan tools/floor.py` → no hits.
  `.github/workflows/ci.yml:198–199` runs it `--warn` in atelier only. So A1(a) is FALSE as worded:
  stampscan the scanner never runs in a child. What does check a child's floor copy: tools/pins.py
  (`pins --floor`, `check_copy` lines 288–304, uses stampscan.find_stamp_blocks/evaluate_block as a
  library; COPY_MALFORMED in FLOOR_FINDINGS, line 760) run from atelier or by hand, and
  tools/floorhook.py (warn-only SessionStart hook, lines 3–17, 215–228). No child-side CI plane runs
  either: `grep -rn "pins.py|--floor|floorhook" docs/build/templates .github/workflows` → nothing;
  `floor.yml` does not exist at the repo root (ls). pins blocks only from COPY_BLOCKS_FROM
  2026-12-09 (pins.py:186), and only when someone runs it.
- Re-drove the "malformed is not silent" claim through the runner children have:
  `pins.check_copy("t", <template with its stamp:end removed>, floor_region_at(W,"HEAD"))` →
  ('malformed', 'stamp:begin at line 19 was never closed with a stamp:end before end of file').
  A one-line edit inside the region → 'drift'. The template's OWN copy → 'drift' (detail: unfilled
  placeholders <SHA>, <atelier-path>, <visibility check>, <visibility fact>, and the heading line not
  in the canonical region); that is the template, not a child, and stampscan runs --warn on it.
- GUARDS facts used: § Acceptance and deferment (a deferment carries a reason AND an expiry;
  "a deferment that cannot lapse is an acceptance that never admitted what it was"); § Ruled
  2026-11-09 ("a lowering with no end date is not a lowering this model allows"; line marker and
  ignore glob stay acceptances); § Where a guard recognises its own work by a convention; § Before
  building a check (evidence window); § What every check declares (grounding and replay: each
  incident by reference, with a test that replays it).
- Dated-grace precedents in tools/ (grep `_UNTIL|_FROM = `): attribscan ATTRIBUTION_WARN_UNTIL
  2027-02-08; blockscan SUBSECTION_WARN_UNTIL 2027-01-11; namescan NAME_WARN_UNTIL 2027-05-03;
  pdlistscan PERSONAL_DATA_WARN_UNTIL 2027-03-08; quotescan QUOTE_WARN_UNTIL 2027-05-31; leakscan
  TYPE_LEVEL_UNTIL / DOCUMENT_UNTIL 2026-11-20; allowmarker MALFORMED_GRACE_UNTIL 2026-12-09; pins
  COPY_BLOCKS_FROM 2026-12-09; floor.py sizescan bars 2026-12-09; board FULL_FORM_ACCEPTED_UNTIL
  2026-12-04. conflictscan's tool-markup tier: no date constant (grep of conflictscan.py for
  `date(`/`UNTIL`/`FROM`: none). Board item 320/780 (read whole; not barred) is event-dated ("once
  no child's tree carries the leak"), probed 2026-11-06: 8 findings in three children.
- allowmarker.load_ignore_globs (lines 504–523): an ignore glob is "a whole path, every rule,
  indefinitely"; optional `review-by:` (110/060, lines 540+). conflictscan's marker is unscoped
  (`marker_rx(ALLOW_MARKER)`, line 185; docstring 188–196 says one rule per line, so no scope).
- Brief's coldsweep sweep (exact command from the brief, run from the worktree): exit 0, 63 hits over
  748 files, 1017 excluded as barred. Hits are the delta's own files, CHANGELOG, README, ROADMAP line
  440 (320/780's title), 320/780 and 115/220 items, leakscan/secretscan/linkscan siblings. Nothing
  barred was opened. The sweep showed me 320/780's title and two fragments; I then read that item
  whole, which the brief does not bar.
- RECORD.md grep (`append-only|rewritten`): lines 58, 312 state the append-only principle for
  records, which the .conflictscanignore stanzas rely on.

### Step 4 — probes (synthetic fixtures in the scratchpad; children read-only, counts only)
P1 (A2, what the skip hides): copied docs/build/templates/CLAUDE.md into a scratch "child" root and
  ran `pathscan.scan_text` with skip_floor=False then True. OFF: 9 missing-path findings; ON: 8. The
  region spans template lines 19–129; the ONLY finding inside it is ('method/TOOLBOX.md', 124). So
  today the whole-region skip hides exactly one line's path, as the docstring says.
P2 (regex cost, lens 4): timed pathscan._STAMP_BEGIN_RX (identical to stampscan's by the pin test)
  on `<!-- stamp:begin source=a region=b narrow=` + N spaces + `z` through `_FenceState(True)
  .is_content`: N=10000 → 413 ms, N=40000 → 7031 ms (quadratic; `.+?` then `\s*-->`). Trailing
  whitespace is neutralised by `line.strip()`; an interior run is not. pathscan's LINE_WINDOW_BYTES is
  256 KiB (pathscan.py:841) so one crafted line costs on the order of minutes. With skip_floor=False
  (atelier itself) the same line costs 0.0 ms, because _in_floor_region is not called. TOOL_CLOSE_RX
  on a 4 MB rest: 3.2 ms (linear).
P3 (mutations; scratch copy of tools/ at HEAD, `diff -q` proved identical before each run; each run
  `nice -n 10 /usr/bin/python3 -m unittest discover -s <scratch>/tools -p <file>`; file restored
  from HEAD after each):
  M1 pathscan: ignore source/region identity → FAILED 1 (test_other_region_or_source_is_not_skipped).
  M2 pathscan: never leave the region → FAILED 3 (continuation window, fence inside region, same path
     outside). M3 pathscan: skip everywhere → FAILED 1 (canonical_source_in_tree). All three caught.
  M4 conflictscan: TOOL_CLOSE_RX widened to also match `</parameter>` → only the control failure
     (below): SURVIVES. The tests do not pin which closing tags are NOT the shape.
  M5 conflictscan: drop `is_final_window` on the closer → SURVIVES (behaviour-neutral for a bare
     closer: an overlong line never has an empty rest; untested but harmless).
  M6 conflictscan: advisory counted in the exit code → FAILED 3 (never_blocks, json_shape, control):
     caught. M7 sanity (closer blind on line 2) → FAILED 11: the suite reaches the shapes.
  CONTROL: unmutated scratch copy → FAILED 1: test_absolute_staged_path_is_refused, because the
  scratch dir is not inside a git repo (refusal text differs). In the worktree the same suite is OK
  (step 5). So M4 and M5's single failure is the control's, not the mutation's.
P4 (estate, counts only; script estate_probe.py in the scratchpad, `nice -n 10`): 29 git repos
  beside atelier's main checkout (via tools/estate.py), 22 carry the floor stamp. Tag-shape lines in
  tracked text files across all 29: `</content>` 2 (1 repo), `</invoke>` 1 (1 repo), `</parameter>`
  0, namespaced closers 0, `<invoke name=` 0, `<parameter name=` 0, namespaced openers 0, closer with
  trailing text 0. pathscan findings hidden by the skip (forced off minus derived): exactly 1 in each
  of the 22 stamped repos, 0 in each of the 7 unstamped; no errors. conflictscan at HEAD over each
  repo: unexempted tool-markup advisories {3} in one repo, 0 elsewhere; blocking findings 0
  everywhere. (320/780 recorded 8 in three repos on 2026-11-06; two have since cleaned or exempted.)
  No path, repo name or line was printed.

### Step 5 — the brief's re-run lines (2026-11-22T20:18Z, PATH python3 = 3.14.6, niced, sequential)
- test_pathscan.py: exit 0, Ran 172 tests OK (17.4 s). test_conflictscan.py: exit 0, Ran 88 OK
  (16.1 s). pathscan --selftest: exit 0 "selftest OK — pathscan". conflictscan --selftest: exit 0
  "selftest OK — conflictscan". conflictscan --root . . --json: exit 0; clean true, blocked false,
  counts {blocking 0, advisory 0}, suppressed {0 by marker, 2 files by ignore glob}, coverage 1763
  files / 336382 lines; stderr carried two allowmarker notes ("allow-marker present but
  unparseable … `conflictscan:allow`" and "`conflictscan:allow:`"), sourced to the test fixture at
  test_conflictscan.py:286 and a bare mention; pre-existing allowmarker behaviour, not this delta.
- Full suite `nice -n 10 python3 -m unittest discover -s tools`: started 20:22Z; result below.
- floor.py 2872–2887: the advisory count is read from the scanner's stdout whenever
  `advisory_count` is set, on any plane, and skipped on exit 2. Not a finding.

### Step 6 — verdict written (2026-11-22T20:4xZ)
- Appended act 1 to the brief below a `---` divider: provenance, method, lenses, A1–A5, V1–V7,
  per-commit ledger, FK1–FK8, overall, re-run ledger, follow-ups. Overall PASS-WITH-FINDINGS,
  0 MAJOR / 2 MODERATE / 4 minor / 2 note.
- Criteria used per finding: FK1 GUARDS § Before building a check (licensing context inside the
  window) + V1/V5; FK2 GUARDS § Acceptance and deferment + § Ruled 2026-11-09; FK3 V5; FK4 OWASP
  ASVS V5 input validation (regex backtracking) + measured cost; FK5 GUARDS § What every check
  declares (grounding and replay) + M4; FK6 GUARDS rule (a) narrowest scope; FK7 GUARDS (c),
  recorded; FK8 GUARDS § convention is a shared invariant.
- Non-findings, with evidence: the four conflict shapes unchanged (lines 383–402; 88 tests; selftest
  exit 1 on markers); exit code tracks blocking only (M6 caught; JSON re-run); fence/region
  interplay (tests + M2); the regex copy pinned (test_regexes_and_floor_identity_match_stampscan);
  the CHANGELOG's estate measurement (P4: 22×1, 7×0); the closer shapes match the estate's real
  leaks (P4: 3 lines, all caught); allow-marker on a closer line exempts and is counted
  (test_reasoned_allow_marker…); the ignore file is reasoned (load_ignore_globs); /security-review
  discharged with grounds (pending diff is the sibling removal and this brief).

### Spawn prompt (verbatim, as REVIEW.md rule 4 asks the reviewer to record)
```
You are the cold reviewer for one rule-4 Fable review pass in the atelier repo.

WHO YOU ARE
- Item: atelier board `160/997` (docs/roadmap/160-doctrine-review-owed/997-rule-4-cold-pass-queued-floor-region-skip-and-markup-rule.md — you may read only its title, per the brief's barred list).
- Worktree (your review tree): "/Users/mike/worktrees/fable/atelier-160-997-2004/atelier". Use absolute paths and `git -C "<worktree>"` everywhere; never `cd`. Paths may contain spaces: double-quote every path in every shell command.
- Brief: "/Users/mike/worktrees/fable/atelier-160-997-2004/atelier/docs/reviews/2026-11-09-0207-floor-region-skip-markup-rule-cold.md". Read it in full first and follow it, plus "docs/method/REVIEW.md" in the worktree for the verdict shape.

PROVENANCE (state this in your verdict)
- You are Fable 5.1, tier checked at selection. You were spawned by headless per-pass orchestrator session e55d14f5 (Opus 5.5), itself started by drain session eca14b23 (Opus 5.5). Both are rule-4 off-tier orchestrators: they hold the context partition, form no finding and write no severity. Neither wrote the brief or the delta. Session eca14b23 wrote no brief and no delta and started no brief-writer for this pass.
- The brief bars sessions d4a0fcf3, 74f2b8cd and 4c65083c (with everything 4c65083c started). You were not started or instructed by any of them.
- You run under the principal's weekly drain order of 2026-11-23, verbatim: "Start a fable drain or whatever it is called now. Target 100% of weekly budget by 11.30am NZT todat".

THE PARTITION
- The brief's `.deferred.md` sibling was removed from the worktree on purpose (the worktree shows it as deleted; that is expected). Do not look for it in git history, other checkouts, scratchpads, tmp or anywhere else, and do not run `git show`/`git diff`/`git log -p` on it. It is released to you only after act 1 is committed. Honour every other barred-reading line in the brief too (use `tools/coldsweep.py` as the brief says).

WHY THE LOG EXISTS (principal, 2026-11-16, verbatim): "The main reason I prompted this earlier in the session is a review must have irrefutable integrity to promote trust in the reviwers verdict. So its reasoning and methdology are as important as its verdicts. Within the realms that calude will allow noting the model extraction limitations". So your log records the method: what you examined, in what order, for which lens, what you left out and why, every check with its exact command or file and line range, and for each finding and non-finding the evidence and the criterion that decides it, enough for a third party to re-run the method and reach the same verdict. Where the harness won't let part of it be written, manage the limit as atelier `docs/method/AUTONOMY.md` § "A limit the tooling imposes is managed, never fatal" says.

REVIEW LOG (principal, 2026-11-16: a review's work must be open and checkable once it is complete)
- Keep a running work log at "/Users/mike/.claude/fable-drain/notes/atelier-160-997-2004.md". It is the one file outside the brief you may write. Commands, files and evidence only. As you work, append: each step you took (the command run, or the file and line range read) and what it showed; each candidate finding with that evidence and the rule or requirement it breaks; each item you checked and found sound, with that evidence. Enough detail that someone else could repeat the steps. It is the audit trail of the review and what you read first if you are interrupted; the verdict itself goes only in the brief. No secrets or live captures in it. Write act 1 entries before the sibling is released.
- It is private while the pass runs and is appended verbatim to the brief at the fold, in a PUBLIC repo: write no private repo name or path, no session name, no estate fact, no email address in it.

WHAT YOU MAY WRITE
- The review log above, and otherwise only the brief file:
  - act 1 appended below a `---` divider, in the shape the brief's Process section sets (finding prefix `FK`);
  - an updated Status line in the brief (never "fold-in owed");
  - keep the file's own column width (prose wrapped at ≤ 100 columns), absolute dates only, ISO-8601 in your own prose; verbatim source text that trips a date gate takes a `datescan:allow` marker. Run the repo's date/wrap scanners on the brief before finishing (e.g. `/usr/bin/python3 tools/datescan.py` and `tools/wrapscan.py` from the worktree; check their --help for the right form).
- Do not edit any other file in the worktree.

WHAT YOU MUST NOT DO
- No commit, no push, no write to GitHub. The orchestrator commits.
- No GUI apps. Use `/usr/bin/python3` (macOS has no `timeout`), or `python3` where the brief's re-run lines say so (note which you used). Never run an installed tool by bare name from PATH.
- Never print a secret or personal data. Exercise tools on scratch copies or synthetic fixtures under your own scratchpad, and delete them when you finish; leave no captures in scratch.
- LIVE SYSTEMS: read-only reads of live systems are allowed as the review needs them (principal, 2026-11-09, verbatim: "reads of live systems is fine as needed, Reviews that need writes should be de-priortised"). A read means nothing on the target changes; if a verb's effect is unsure, treat it as a write. NO live writes of any kind; a check that would need one is marked NOT RUN with the reason. Allowlist fields before printing (provider reads can carry credentials); never dump a user, key or certificate object raw.
- Child repos are read-only and are reported by count only, never by name or path.

LOAD (the principal's instruction is to keep this 16 GB laptop from crashing; several passes run at once)
- Check `uptime` before heavy runs. Run any test suite under `nice -n 10`, one suite at a time, single process (no xdist, no `-n auto`, no parallel runners), in the foreground with a long timeout. Prefer the targeted tests a finding needs over the whole suite; run the full-suite re-run line once, niced.

PUBLIC REPO
- atelier is PUBLIC. In the brief and the log, refer to orchestrators by session id only ("drain session eca14b23", "orchestrator session e55d14f5"). Never write a session NAME, a private repo's name or path, or any estate fact.

HOW TO FINISH
- Act 1: after writing your verdict into the brief and your log entries, STOP and end your reply with: the overall verdict, the tally (counts by severity), the brief path, and the exact line "ACT 1 SAVED".
- You will then receive a message releasing the sibling's held copy for act 2. Do act 2 exactly as the brief's Process says (### Reconcile under your verdict, never revising act-1 text), but do NOT fold the sibling into the brief and do NOT delete any file: the orchestrator does the fold. End act 2 with the restated overall line and the exact line "ACT 2 SAVED".
```

### Step 7 — scanners over the brief; the full-suite line (2026-11-22T20:36Z to 20:4xZ)
- `/usr/bin/python3 tools/datescan.py --root . <brief>`: clean, 1 file / 479 lines read, 0 advisory.
  `wrapscan.py` and `spellscan.py`: the brief is excluded by `.wrapscanignore` / `.spellscanignore`
  (docs/reviews), so they covered nothing; my own wrap was checked by character count: after the
  divider no non-table line exceeds 100 characters (one was 101 and was re-wrapped). `reviewscan.py`:
  "1 review brief(s) keep deferred material out of the brief"; no finding.
- Status line replaced (ACT 1 WRITTEN …; never "fold-in owed").
- Full suite, first attempt (20:22Z, load 9.9 rising to 20.7): moved to the background at the
  600 s foreground limit and killed at the background limit with no `Ran` line, so NOT a result.
  Second attempt started 20:42Z, `nice -n 10 python3 -m unittest discover -s tools`, one process,
  40-minute allowance; result recorded below when it returns.
- Full suite, second attempt: `nice -n 10 python3 -m unittest discover -s tools` from the worktree,
  one process, started 20:42Z, finished 21:01Z: "Ran 3382 tests in 1163.497s", "OK", exit 0. Ledger
  row filled. Capture deleted; the scratchpad holds nothing of mine.
- Act 1 complete at 2026-11-22T21:02Z. Overall PASS-WITH-FINDINGS — 0 MAJOR, 2 MODERATE (FK1, FK2),
  4 minor (FK3–FK6), 2 note (FK7, FK8). Waiting for the sibling's release for act 2.

## Act 2 (2026-11-22T21:0xZ, after act 1 was committed as 072e3f2a)
- Released sibling read whole (the orchestrator's held copy, read-only): 7 seeded questions, 0 facts,
  the brief-writer's re-run results (154/84 tests then; 2 643 full suite on 3.14.6; 3.9.6 import
  errors in four test modules), one prior record named.
- `git log -1 --format=%B 24ac5b8` and `92dd817`: bodies read. Both say "option 3 of the item" and
  "which stampscan checks" / "one edit"; 92dd817 says "children float at floor@main".
- Read whole: docs/roadmap/320-…/610-…md (options 1–4 offered; verified at HEAD 2026-10-16: pathscan
  warn-only in children); docs/roadmap/320-…/490-…md (real shape `</content>` then `</invoke>`;
  proposed openers without an instance); the 160/997 pointer; grep of
  docs/reviews/2026-10-16-1510-expected-toolbox-cold.md for toolbox/pathscan/child (its pathscan
  line is a re-run line; nothing on child resolution).
- Facts for the questions: `grep -n CLAUDE.md tools/pins.py` (lines 5, 52, 88, 102, 140, 152) and
  tools/floorhook.py (5, 24, 148, 207): both read the child's root CLAUDE.md only. `grep` for a
  consumer of conflictscan's JSON `clean` across tools/, instruments/, workflows: none (hits are
  selftest temp dirs and prose). Count-only probe across the 29 repos: 22 floor stamps in root
  CLAUDE.md, 9 in other files across 8 repos.
- Appended `### Reconcile` beneath the act-1 verdict: per-question notes, author's account screened,
  two findings formed at reconcile (FK9 note: one materialisation budget for both tiers, pinned by
  test_cap_counts_advisory_overflow_separately; FK10 minor: a stamp outside root CLAUDE.md is
  skipped by pathscan and compared by nobody). Act-1 text untouched. Overall restated:
  PASS-WITH-FINDINGS — 0 MAJOR, 2 MODERATE, 5 minor, 3 note.
- datescan over the brief after the append: clean. Width: no non-table line over 100 characters.
- Sibling not folded, nothing deleted (the orchestrator folds). Scratchpad holds only the
  orchestrator's own commit-claim.log; nothing of mine remains.
