# Cold pass — seven propagation additions the principal approved in one list

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (self-authored doctrine; one
change is to the floor block every child copies).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** ACT 1 WRITTEN 2026-11-16 UTC (FAIL: 1 MAJOR, 4 MODERATE, 1 minor, 3 notes); act 2
(reconcile) pending the sibling's release. Written 2026-11-09 UTC by session `d16dc612`, a headless
Opus 5.5 brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/1160-rule-4-cold-pass-queued-propagation-doctrine-batch.md`
(barred until phase 2).
**Size:** medium: seven commits, wording only, with a worked-example sweep across nine files and a
change to the stamped floor block; no code.
**Why it earns a review:** Propagation doctrine sets what a child owes the parent and what crosses
between repos, and this repo is public. The worst failure is a route that carries private matter to
a public target, or a floor-block change that strands children.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `722ac2e2`,
  2026-11-09, in its ruling round, and the Sonnet worker it dispatched, which wrote the work (per
  the queue pointer). The author queued this pass and does not take it.
- **Who wrote this brief:** session `d16dc612` (`claude-opus-5-5`), a headless brief-writer started
  on 2026-11-09 by coordinating session `74f2b8cd` (Opus 5.5). `74f2b8cd` built none of this delta
  and forms no finding; its launch prompt was the only instruction, and it carried item numbers, the
  owed-or-not test and house rules, no framing of the work. **Off-tier for review, disclosed: the
  brief-writer forms no finding and writes no severity**, ran no review and used no Fable model.
  Neither was started or instructed by the author. Whoever writes a brief does not run it (the
  principal's rule), so both are barred from this pass.
- **Who reviews:** a session on Fable 5.1 that passes rule 4's criterion, started once the principal
  has approved the Fable pass. **Barred from reviewing:** session `722ac2e2` and every worker it
  dispatched; `d16dc612`; `74f2b8cd`.
- **The principal's approval of this brief:** his request, 2026-11-09, verbatim: *"Check all the
  repo's, any work that requires a fable review but does not have a brief written yet I want you to
  write those briefs then finish this session when thats all done"*. That approves the brief only;
  the Fable gate on the pass is unchanged.
- **Contact, disclosed (rule 4):** the brief-writer had no contact with `722ac2e2` or its workers.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  `skills/review-brief/SKILL.md` and `docs/method/REVIEW.md` whole; the house-form brief
  `docs/reviews/2026-11-06-2027-secretscan-exempt-private-keys-cold.md` lines 1–728, verdict
  included (another surface); the queue pointer whole; the intent records' answer and closing notes,
  by extraction; commit subjects and file lists; the delta's `CHANGELOG.md` entries; the results of
  the re-run lines; parts of the delta's own files at HEAD (outlines, constants, comments). It
  opened no commit message body of this delta, and did not open `docs/SESSIONS.md`, `docs/sessions/`
  or the prior verdict on this subject. Its harness loaded user-level and repo instruction files and
  a memory index, which hold private context this brief does not carry. Everything evaluative is in
  the sibling, by count here: a held-back sibling with one pointer block, 2 questions and 2 facts.

## The acceptance test

*"Approve all 20"*, on 2026-11-09, after reading a one-line summary of each of twenty items,
approving the recommendation on each. The recommendation approved, item by item:
- `320/380`: accept both: "is ever made public", and one sentence that spelling the actual path in a
  public-candidate repo defeats the rule.
- `320/330`: public doctrine names no private child repo in worked examples.
- `310/020`: convention now (a dated pending-upstream marker in every child), tool later.
- `390/010`: atelier does not model consumer or subject-cluster relationships; one generic line
  points at the estate root's registry.
- `310/120`, `310/140`: a general child-to-any-parent route, drafted as one rule; a PR between repos
  carries the filed idea, not the fix; redaction keyed on the target's visibility; an issue where
  there is no write access; a private parent may receive specifics.
- `320/580`: commission a class-only "Splitting a repo" method section, the children's records
  supplied privately.

The offered option's words were written by the authoring session and put to the principal; the
quoted pick is his. Recorded as an answer, not a ruling in his words: where the delta's wording goes
past what he picked, say so. These are claims to test, not settled scope.

## What the work is

Seven commits on `main`, wording only: six additions and a changelog commit. One (`d57ba4cc`)
changes the canonical floor region and the template's stamped copy.

Commits on `main`: `d57ba4cc`, `9c8cb7e7`, `cb742b46`, `4dcdcecf`, `3f3cf5be`, `9ff7f778`,
`38aab8b1`. The landing commit is `38aab8b1`. **Check your tree has it before reading anything:**
`git merge-base --is-ancestor 38aab8b1 HEAD` exits 0, and an orchestrator merges `origin/main` into
the review branch before it spawns.

Delta paths: `docs/method/PROPAGATION.md`, `docs/build/templates/CLAUDE.md`,
`docs/build/REPO-BOUNDARY.md`, `docs/build/README.md`, `docs/method/00-APEX.md`,
`docs/method/CONCURRENCY.md`, `docs/method/ECONOMICS.md`, `docs/method/EVIDENCE.md`,
`docs/method/RECORD.md`, `docs/method/REVIEW.md`, `docs/method/SIGNING.md`, `CHANGELOG.md`. Read
each at HEAD and read each commit body-free, scoped to paths so board records stay barred:

```
python3 tools/coldsweep.py --root . --commit d57ba4cc --path docs/build/templates/CLAUDE.md --path docs/method/PROPAGATION.md
python3 tools/coldsweep.py --root . --commit 9c8cb7e7 --path docs/build/README.md --path docs/method/00-APEX.md --path docs/method/CONCURRENCY.md --path docs/method/ECONOMICS.md --path docs/method/EVIDENCE.md --path docs/method/PROPAGATION.md --path docs/method/RECORD.md --path docs/method/REVIEW.md --path docs/method/SIGNING.md
python3 tools/coldsweep.py --root . --commit cb742b46 --path docs/method/PROPAGATION.md
python3 tools/coldsweep.py --root . --commit 4dcdcecf --path docs/method/PROPAGATION.md
python3 tools/coldsweep.py --root . --commit 3f3cf5be --path docs/method/PROPAGATION.md
python3 tools/coldsweep.py --root . --commit 9ff7f778 --path docs/build/REPO-BOUNDARY.md
python3 tools/coldsweep.py --root . --commit 38aab8b1 --path CHANGELOG.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Commits since the delta on these paths:

```
git log --oneline 38aab8b1..HEAD -- docs/method/PROPAGATION.md docs/build/templates/CLAUDE.md docs/build/REPO-BOUNDARY.md docs/build/README.md docs/method/00-APEX.md docs/method/CONCURRENCY.md docs/method/ECONOMICS.md docs/method/EVIDENCE.md docs/method/RECORD.md docs/method/REVIEW.md docs/method/SIGNING.md CHANGELOG.md
```

At `457615cc` this printed 10 commit(s). Read anything new the same way.

**Claims the work makes (extracted from its own changelog entry and files, not evaluated):**

- The estate-resources bullet reads "is public, or is ever made public", with one sentence on
  spelling the actual path; the canonical region and the template's stamped copy change together;
  children's copies update at their next pin bump.
- `PROPAGATION.md` § *The route* rule 2 reaches doctrine's own prose; worked examples in eight
  method files and the build README say "a private child"; acts done to a repo and the extraction
  origin's provenance citations are left, pending his word.
- `Pending upstream:` is a greppable marker with an ISO date and the parent item or `unfiled`; the
  enumerator is not built.
- `PROPAGATION.md` models only parent and child, with one generic line pointing other relationships
  at the estate root's registry.
- `PROPAGATION.md` § *The same route between any two repos*: a PR files an idea and never the fix,
  redaction keys on the target's visibility, an issue where there is no write access; how the target
  learns a PR arrived is undecided.
- `REPO-BOUNDARY.md` carries a draft § *Splitting a repo* from one hand-up's testimony, with what
  could not be grounded listed.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** the tool that would enumerate pending-upstream markers and the fleet's pin bumps,
except where a claim depends on them.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself, first, and damage each
with a probe or confirm it by re-driving. Ask whether this is the right problem, solved at the right
altitude.
2. **Correctness & quality** — does the work do what its claims above say; honest about done versus
stubbed; any overclaim or silent scope cut, each recorded against the text that makes it.
3. **Completeness / harvest** — every surface that states the rule (V3), one home (V4), no
contradiction with sibling doctrine (V5), tests that would stay green on a broken check, what
already exists that this ignored.
4. **Security & privacy** — mandatory. This delta sets what may cross into a public repo and how.
Weigh the route for leakage at the altitude of its rules. Quote no private child's name or path,
including any found by sweeping history. No code changed, so `/security-review` has nothing to read:
discharge it in one line.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-09 UTC, from the worktree root
at `457615cc`; results are in the sibling. Read exit codes explicitly. Check `uptime` first and run
heavy lines under `nice -n 10`. Python is the `python3` on `PATH` (the tests need 3.10 or later;
`/usr/bin/python3` is 3.9 on this machine and some modules fail at import).

- `nice -n 10 python3 tools/floor.py --plane ci --root .`

## House rules for this run

- **Live systems:** read-only reads of live systems as needed; **no live writes**. A check that
  would need a write is marked NOT RUN in the verdict, with what it would have shown.
- Probes run on scratch copies and synthetic fixtures under your scratchpad only, deleted when you
  finish. Never mutate the worktree's `tools/` or `instruments/`.
- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live: touch nothing outside your worktree and scratchpad.
- Read-only git only, beyond committing this one file at the end of each phase (or handing it to the
  orchestrator to commit).
- Child repos are read-only and counted, never named: quote no child's name, path or excerpt.
- One heavy process at a time; foreground, long timeout. Never run an installed tool by bare name
  from `PATH`: use the worktree's own copy.
- `/security-review` reads the session's pending diff, not this delta. Aim it at the code by
  reproducing the diff in a scratch clone, or discharge it by grounds, never with this brief or its
  sibling dirty. Over markdown its clean pass is empty; weigh it as nothing.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo is
  PUBLIC: quote no secret, placeholder token, email address, child repo name or path.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the
deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the
reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, this brief's sibling
(`2026-11-09-0153-propagation-doctrine-batch-cold.deferred.md`), every delta commit's message body,
the queue pointer
`docs/roadmap/160-doctrine-review-owed/1160-rule-4-cold-pass-queued-propagation-doctrine-batch.md`,
and the intent records beyond their titles:

- `docs/roadmap/310-pointing-up-the-child-to-parent-route/020-nothing-enumerates-what-the-estate-owes-the-house.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/380-the-floor-s-public-tense-and-whether-it-should-name-the-root.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/330-does-the-naming-precedence-reach-doctrines-own-prose.md`
- `docs/roadmap/390-repo-relationships-beyond-the-tree-mike-comm/010-consumer-and-subject-cluster-relationships-have-no-model.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/580-missing-house-rule-splitting-a-repo-has-no-method.md`
- `docs/roadmap/310-pointing-up-the-child-to-parent-route/120-the-route-is-atelier-specific-any-parent-repo-needs-one.md`
- `docs/roadmap/310-pointing-up-the-child-to-parent-route/140-a-pr-as-the-carrier-between-any-two-repos.md`

The delta's docstrings, comments, ADR text, `tools/README.md` and `CHANGELOG.md` entries carry the
author's account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1160-rule-4-cold-pass-queued-propagation-doctrine-batch.md \
  --also-exclude docs/roadmap/310-pointing-up-the-child-to-parent-route/020-nothing-enumerates-what-the-estate-owes-the-house.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/380-the-floor-s-public-tense-and-whether-it-should-name-the-root.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/330-does-the-naming-precedence-reach-doctrines-own-prose.md \
  --also-exclude docs/roadmap/390-repo-relationships-beyond-the-tree-mike-comm/010-consumer-and-subject-cluster-relationships-have-no-model.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/580-missing-house-rule-splitting-a-repo-has-no-method.md \
  --also-exclude docs/roadmap/310-pointing-up-the-child-to-parent-route/120-the-route-is-atelier-specific-any-parent-repo-needs-one.md \
  --also-exclude docs/roadmap/310-pointing-up-the-child-to-parent-route/140-a-pr-as-the-carrier-between-any-two-repos.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, any orchestrator, what you read, the UTC day you ran on),
per-lens answers, V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (each of the seven commits: read body-free
yes/no, findings by id), findings with stable ids (prefix `PRB`: `PRB1`, `PRB2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands and results, children by count only) and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta commits' bodies;
append `### Reconcile` beneath your verdict: per-finding notes against the sibling's questions and
the author's account, any finding formed at reconcile marked as such, and the overall line restated.
Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

Every finding on this delta is the principal's to decide (rule 3): record all, apply nothing.
Counsel per finding is welcome, labelled as counsel and kept beneath it.

---

## Verdict — act 1 (cold pass, 2026-11-16 UTC)

### Provenance (V7, rule 4)

- **Reviewer:** this session, on **Fable 5.1** (`claude-fable-5-1`), the principal-named review
  tier, checked at selection. Ran on 2026-11-16 UTC in the review worktree
  `/Users/mike/worktrees/fable/atelier-160-1160-0757/atelier` at HEAD `532080c5` (the board claim
  commit); `38aab8b1` is an ancestor (`merge-base --is-ancestor` exit 0).
- **Spawn:** a headless orchestrator session (Opus 5.5), itself started by drain session
  `1e053526` (Opus 5.5). Both are rule-4 off-tier orchestrators: they hold the context partition,
  form no finding and write no severity; `1e053526` wrote no brief and no delta. The spawn prompt
  was process only: paths, the brief, the review-log file, the barred set (the brief's rule-2 list,
  with the sibling removed from the worktree until act 1 is committed), load and live-system rules,
  the deliverable's shape and release timing. It carried no question about the delta, no pointer
  to where the risk lives and no request about any finding. Its text is appended to the review
  log, which is folded into this file at the fold. The release message is recorded in act 2.
- **Not started or instructed by** any session the brief bars: `722ac2e2` and its workers,
  `d16dc612`, `74f2b8cd`. No contact with any of them before or during this pass.
- **Approval:** the principal's API-credit drain order of 2026-11-16, verbatim: *"I want to use
  things other than my weekly budget to clear as many fable reviews as possible like using fable
  drain. I thought we could start by using up all the API credits I have."* and *"As always you
  must ensure that nothing harms the integrity or quality of the review process and verdicts, for
  example if the review is done by API it must be as good as running it locally"*.
- **What I read:** this brief whole; `docs/method/REVIEW.md` 25-560; the seven delta commits
  body-free via `coldsweep --commit` (ledger below); the delta files at HEAD at the sections named
  in the log; eight later commits on the three core files, body-free, to know HEAD's state. **Not
  read:** the sibling (absent from the worktree by design; not sought), `docs/SESSIONS.md`,
  `docs/sessions/`, `docs/ROADMAP-DONE.md`, every prior verdict, the queue pointer, the seven
  intent records beyond their titles, every commit body. The onramp's session-log step was
  skipped (rule 2). Child repos were not opened; one live read-only `gh repo view` per kept name
  checked visibility, and the result is reported by count. The brief said 10 commits followed the
  landing on the delta's paths; at `532080c5` there are 69, 14 of them on the three core files.
- **Method record:** the running log at `~/.claude/fable-drain/notes/atelier-160-1160-0757.md`
  holds every command, file and line range in order, with what each showed; it is appended to this
  file verbatim at the fold.

### Lens 1 — approach and assumptions (named by me, then probed)

- **A1. The one-line picks are the scope; the wording may go past them.** Probed each item's
  wording against the pick in the acceptance test. `310/020`, `390/010`, `310/120`+`140` match
  their picks line for line. `320/330` goes past its pick in one direction (it withdraws a naming
  that an earlier text called the principal's ruling, and drops those words: PRB4) and stops short
  in another (it sweeps nine files where the rule it writes says "a public doctrine file": PRB3).
  `320/580`'s pick commissioned a section "the children's records supplied privately"; the delta
  wrote a draft from one hand-up, says the records are owed, and sits in the standard (PRB5).
  `320/380` matched its pick and was then superseded the same day by other work (PRB8).
- **A2. "Redaction keys on the target's visibility" is a safe test.** Damaged: the same delta's
  own `320/380` paragraph (kept at HEAD, PROPAGATION.md:297-305) argues that a present-tense
  visibility test fails on a public-candidate repo, and the delta's own "Splitting a repo" section
  describes content leaving a private repo for a public one. PRB1.
- **A3. The stamped child block is what a child reads.** Confirmed by the delta's own `d57ba4cc`,
  which edited the block for `320/380`; not carried through for `310/020`, whose marker the block
  does not mention. PRB2.
- **A4. The canonical region and the template agree.** Confirmed: `stampscan` reports the
  template's one block identical to region `floor` (105 lines), exit 0.
- **A5. The two children kept by name are public.** Confirmed by live read: both PUBLIC.
- **A6. "A private child" hides the child.** Damaged: `README.md:27` names the extraction-origin
  repo and its product as "the private repo", and the delta leaves the product token in the
  very sentence it veiled (ECONOMICS.md:206-209). PRB3.
- **Right problem, right altitude?** Four of the six are at the right altitude (marker, model
  scope, generic route, the floor's tense). The naming rule is below its altitude: it treats a
  symptom (names in worked examples) while the surfaces that identify the repo are carved out
  "pending his word". The split section is above its grounding.

### Lens 2 — correctness and quality

The changelog's claims reproduce: eight method files plus the build README (counted from the
diff), no tool built, the marker and the generic route as described, the parent-and-child line,
the draft section with its "could not be grounded" list. Honesty is good throughout: every item
says "an answer, not a ruling"; the split section says what it could not ground; the route says
what is undecided. Two overclaims by omission: the naming rule claims its examples "name no
private child repo" while the tree identifies one in one hop (PRB3), and the withdrawal of PU-2's
naming no longer says a ruling is what it withdrew (PRB4). One silent-scope point: the marker's
point-of-use surface was not changed (PRB2).

### Lens 3 — completeness and harvest

V3 sweep: the marker rule has two unswept mirror sites, the stamped block and the template
(PRB2). The naming rule has unswept sites in `DOCUMENTATION.md`, `CONCURRENCY.md` and
`ECONOMICS.md` (PRB3). What exists that the delta ignored: the floor's visibility declaration
(`260/050`, `c4424324`), which gives the generic route a declared visibility to key on instead
of a present-tense read (counsel under PRB1). Index surfaces: `docs/build/README.md:13` describes
`REPO-BOUNDARY.md` in a way the new section does not contradict; `CHANGELOG.md:534-562` records
the same-day supersession of `320/380`.

### Lens 4 — security and privacy

No code changed; `/security-review` reads a pending diff, the worktree carries this brief and the
sibling's deletion, and markdown is outside its reach: discharged, weighed as nothing. At the
altitude of the rules: the generic route's rule 2 is a leak by design on a visibility flip and on
the sender's record (PRB1, MAJOR). The naming sweep adds no new exposure and removes little real
exposure (PRB3). No private child's name, path or excerpt appears in this verdict; the log masks
them too. Nothing in the delta carries a secret or placeholder token.

### The standing checklist

- **V1** — PRB3 (a protection claimed that the tree does not give). Changelog counts: sound.
- **V2** — the one re-run line reproduces (ledger below). `stampscan`: identical. Visibility of
  the two kept names: PUBLIC, live.
- **V3** — PRB2, PRB3.
- **V4** — PRB2 (point-of-use copy not updated). `RECORD.md`'s copy of the naming exception is a
  stamped pointer to PROPAGATION rule 2: sound.
- **V5** — PRB1 (delta disagrees with itself), PRB4, PRB5, PRB6, PRB7. Cross-references checked
  for the rule reached: same-route rule 4 reaches the branch form at 738-741 (sound); rule 3's
  "shape 3 above" reaches hold-and-flag at 678-684 (sound); `320/230` exists and matches the
  silent-skip subject (sound); "the estate root's registry" reaches nothing (PRB6).
- **V6** — lens 4 above; PRB1.
- **V7** — stated above and in the brief.

### Per-commit ledger

| commit | read body-free | findings |
|---|---|---|
| `d57ba4cc` | yes | PRB8 (superseded at HEAD by `e76250cf`); its kept reasoning feeds PRB1 |
| `9c8cb7e7` | yes | PRB3, PRB4 |
| `cb742b46` | yes | PRB2, PRB9 |
| `4dcdcecf` | yes | PRB6 |
| `3f3cf5be` | yes | PRB1, PRB7 |
| `9ff7f778` | yes | PRB5 |
| `38aab8b1` | yes | none; counts verified |

### Findings

Severity scale used: **MAJOR** — followed as written, the rule produces the harm the doctrine
exists to prevent, or a claim that would propagate false; **MODERATE** — the rule misleads or
misses a surface it binds, without producing the harm by itself; **minor** — wording or a
dangling reach; **note** — an observation, nothing owed.

**PRB1 — MAJOR.** *The generic route's redaction test is present-tense and one-sided, and the
delta itself says why that fails.* `PROPAGATION.md:835-840` (§ *The same route*, rule 2): a
private target "may be sent specifics (names, hosts, the sender's own detail), because the
filing publishes nothing to a wider audience". Those specifics land in the target's PR, board
item and history. `PROPAGATION.md:297-305`, written by the same delta and kept at HEAD, argues
that a present-tense visibility test "returns false on every read of a private-now,
public-candidate repo until the day it flips, by which time the content it exists to keep out is
committed". `PROPAGATION.md:318` says the name beside what a repo holds "stays barred" and that
pushed history is for good; `REPO-BOUNDARY.md:83-96`, same delta, describes a private repo's
content moving into a new public repo. So rule 2, followed as written, writes hosts into a
target that the batch's own text expects to go public, with no retraction. Second edge, same
rule: `851-856` has the sender name "where it filed in its own record", keyed on nothing; a
public sender's record then names a private target beside the subject it filed, which is the
join `RECORD.md` § *The record is public* bars. Breaks V5 and lens 4. The pick's words were
"redaction keyed on the target's visibility", so the text matches the pick; the finding is on the
briefing he had when he picked (rule 3: open to challenge on the briefing, by re-briefing).
*Counsel:* key rule 2 on the target's **declared** visibility (`260/050`, the floor's visibility
declaration) **and** no public candidacy on its board; carry specifics by a channel that does not
enter the target's history (the peer channel, or the private estate root) and keep the PR to the
class; add one clause keying the sender's own record on the sender's visibility.

**PRB2 — MODERATE.** *The marker is not on the surface a child reads.* `PROPAGATION.md:687-699`
makes every pending-upstream line and every hold-and-flag note begin `Pending upstream:` with a
date and an item, and rests the whole benefit on one grep. The stamped child block says "hold it
in this repo's record marked owed upstream" (`PROPAGATION.md:197`, `templates/CLAUDE.md:99`,
identical by `stampscan`), with no marker, date or item; the same delta edited that block in
`d57ba4cc` and had the occasion. A child that follows its block writes a line the grep misses,
and the enumerator the convention prepares for will walk nothing. Breaks V3 and V4. *Counsel:*
one clause in the canonical region and the template together, so the fleet picks it up at the
next pin bump; and the same-route rule 3's "with the `Pending upstream:` marker" then reaches a
block that says so.

**PRB3 — MODERATE.** *The naming sweep is partial and the veil it installs is nominal.* The rule
(`PROPAGATION.md:666-676`) binds "a public doctrine file"; the sweep touched nine. Unswept, on
doctrine surfaces, reported by file and line only: `DOCUMENTATION.md:123` (a bearing attributing
a discriminator to the origin repo by name), `:208`, `:238`, `:245`; `CONCURRENCY.md:196` (a
bearing that names the product); `ECONOMICS.md:206-209`, where the sentence the sweep veiled
keeps the product token that `README.md:27` ties to "the private repo" by name, so the veil
lifts in one hop. The carve-out for "provenance citations ... pending his word" leaves
`README.md:20,27` naming the origin as private, which makes every "a private child" beside that
product identifiable. In the other direction, `SIGNING.md:174,199,201` de-named an activation
ladder, which is an "act done to a repo" the rule says is outside it. No new exposure; the claim
"names no private child repo" is stronger than the tree (V1), and the sweep is incomplete (V3).
*Counsel:* put the provenance-citation question to him now, with this finding, rather than
leaving it "pending his word" beside a rule that depends on the answer; until then, say in rule 2
that the veil is forward-only and does not hide the extraction origin.

**PRB4 — MODERATE.** *A recorded ruling was replaced by an answer, and the words recording the
ruling were removed.* Before `9c8cb7e7`, § *The instance* read "named on the principal's ruling
(2026-08-22, PU-2)" and `CONCURRENCY.md`'s bearing "named on the principal's ruling, 2026-08-22
— PU-2". After: "This text named the repo from 2026-08-22, on PU-2 ... withdrawn on 2026-11-09,
`320/330`, by rule 2 above" (`PROPAGATION.md:860-863`) and "named here from 2026-08-22, PU-2,
until `320/330` withdrew it" (`CONCURRENCY.md:138-139`). The text now says a pick replaced
"PU-2's choice"; it no longer says that choice was his ruling. Either the old text was wrong, in
which case the delta should say so, or a fact left the record. `REVIEW.md` rule 3 (AR8) needs the
earlier word in front of him when he decides; whether the 2026-11-09 ask named the ruling is act-2
work on the barred record. *Counsel:* restore "the principal's ruling" to both parentheticals;
if the ask did not name PU-2 as his ruling, re-brief (rule 3).

**PRB5 — MODERATE.** *A section that cites the rule it breaks.* `REPO-BOUNDARY.md:85-96` says
every element is one hand-up's testimony and that "atelier has not re-driven it", citing
`PROPAGATION.md:528-536`: "A hand-up's mechanism claim is re-driven before it becomes house
text ... Before atelier writes a mechanism into a method file it runs the mechanism, and the
record says it did." The section is in the build standard that every boundary decision reads;
"draft" and "checklist to test" do not move it out. The pick commissioned the section with "the
children's records supplied privately"; they were not, and the delta says the extraction and
its cold review are owed. Honest, and still the thing the rule bars. Breaks V5. *Counsel:* keep
the eleven points under a stub marker that says "not house text until re-driven", or hold them
on `320/580` until the records arrive; the "could not be grounded" list is the right shape and
should travel with them.

**PRB6 — minor.** `PROPAGATION.md:469-473` sends other relationships to "the estate root's
registry", which nothing in atelier defines; the only other mention (`:697`) is a wiring
`stampscan` waits on. The pointer reaches no rule (V5's cross-reference test). By design it is
private, so say so: "defined per estate, in its private root". One clause.

**PRB7 — note, formed against HEAD, caused by later work.** Same-route rule 3
(`PROPAGATION.md:841-843`): no write access to the target "means an issue". `3312cdbd`
(`160/300`, after this delta) gives an adopter without access "hold-and-flag, a fork and pull
request, or an issue" (`:495-499`). The two disagree on whether a fork PR is a shape. For the
owner of `160/300`'s application, not this delta's.

**PRB8 — note.** `d57ba4cc`'s floor wording is gone at HEAD: `e76250cf` (`020/050`, the same day)
replaced the estate-resources bullet in both copies and marked the `320/380` note "Superseded".
The note still says the test "now reads ..." as history, with the marker; `CHANGELOG.md:562`
records the change. Nothing owed on this delta.

**PRB9 — note.** The doctrine's own example line (`PROPAGATION.md:693`) matches
`grep -rn 'Pending upstream:'` over atelier's tree. Harmless for a child (its block does not carry
the phrase, which is PRB2's point); worth a word if the enumerator ever walks the parent.

### Overall

**FAIL — 1 MAJOR, 4 MODERATE, 1 minor, 3 notes** (PRB1-PRB9). The MAJOR is one rule that,
followed as written, carries private matter into a target the same batch expects to become
public; the rest are reach and record defects. Every finding is the principal's to decide
(rule 3): recorded, nothing applied.

### Re-run ledger

- `nice -n 10 python3 tools/floor.py --plane ci --root .` — worktree root, load 2.12: exit 0;
  every enforced check green; secretscan 28 and leakscan 3 advisory, reported, not blocking.
- `python3 tools/stampscan.py --root . docs/build/templates/CLAUDE.md docs/method/PROPAGATION.md`
  — exit 0; 1 block identical to canonical region `floor` (105 lines).
- `gh repo view <owner/child> --json visibility,isPrivate`, twice, live and read-only — both
  PUBLIC (children by count).
- `python3 tools/coldsweep.py --root . --commit <sha> --path ...`, seven times as the brief's
  lines — all exit 0, "message body not printed", 0 barred files touched.
- `git merge-base --is-ancestor 38aab8b1 HEAD` — exit 0.
- Over this file after writing: `datescan` exit 0 (0 findings), `leakscan` exit 0 (0 findings);
  `spellscan` and `wrapscan` skip `docs/reviews/` by their ignore files and scanned nothing, so
  width was checked by hand: no verdict line over 100 columns.

Not run: nothing needing a live write was needed. Child repos: not opened.

### Follow-up checklist

- [ ] PRB1: the principal's decision on the generic route's rule 2, re-briefed with the
      contradiction in front of him (`260/050` gives a declared visibility to key on).
- [ ] PRB2: marker clause in the stamped block, canonical region and template together.
- [ ] PRB3: the provenance-citation question put to him; sweep the three unswept files or state
      the veil's limit in rule 2.
- [ ] PRB4: restore "the principal's ruling" at two sites; act 2 checks whether the ask named it.
- [ ] PRB5: stub marker or hold on `320/580` until the children's records arrive.
- [ ] PRB6: one clause.
- [ ] PRB7: hand to `160/300`'s application owner.
- [ ] Act 2: reconcile against the sibling and the barred records; fold the log in.
