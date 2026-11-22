# Cold pass — `pathscan` skips a child's inlined floor region, and `conflictscan` reports tool-call markup as an advisory

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4 (a guard or a rule is doctrine by
function, rule 3).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** ACT 1 WRITTEN 2026-11-22 UTC — PASS-WITH-FINDINGS (0 MAJOR, 2 MODERATE, 4 minor,
2 note), by a Fable 5.1 reviewer under orchestrator session `e55d14f5` (drain session `eca14b23`),
on the principal's drain order of 2026-11-23 NZDT. Act 2 (reconcile against the sibling and the
commit bodies) follows once act 1 is committed. Every finding awaits the principal's decision
(rule 3). Brief written 2026-11-09 UTC by session `d4a0fcf3`, a headless Opus 5.5 brief-writer.
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
verdict in `docs/reviews/`, this brief's sibling
`docs/reviews/2026-11-09-0207-floor-region-skip-markup-rule-cold.deferred.md` (a held-back file; by
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
