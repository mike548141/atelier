# Cold pass — the worktree venv sentence follows STORAGE

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus brief-writer;
the pass waits for a further cold Fable session that neither the delta's author nor this
brief-writer (nor its orchestrator) started or instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/550-rule-4-cold-pass-queued-worktree-venv.md`.
**Why it earns a review:** the substrate bullet is what a session reads when it takes a worktree;
it now tells that session how to get a working environment there, and an environment that
quietly runs the wrong tree's code is a silent-failure mode.

## Spawn provenance

- **Author of the work under review:** the 2026-10-03 queue run that landed the commit below; its
  intent record is the session file dated 2026-10-03 0144 UTC that the pointer names (not opened
  by the brief-writer). The commit's trailer names an Opus model.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched by the Mike-opened
  Opus queue-run session `abe96d8d` on 2026-10-16, on Mike's answer of that date that a fresh Opus
  session writes these briefs. Neither it nor its orchestrator authored the delta or was started
  or instructed by its author. **Off-tier for review, disclosed: it forms no finding and writes no
  severity**, and stops after this brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, passing rule 4's
  criterion. If it runs as reviewer-plus-orchestrator, the off-tier conditions of rule 4 apply and
  are disclosed in the claim, the pointer and the verdict. The reviewer repeats its own provenance
  in the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material met before writing): the seven queue
  pointers it was assigned (160/500, 520–570; refs-only, each ending in the orchestrator's claim
  line); the seven landing commits' subjects, `--stat` lists, full message bodies (the author's
  account) and diffs on the delta paths; `docs/method/REVIEW.md` in full; the ask halves of two
  2026-10-04 briefs as templates; HEAD text of the neighbouring surfaces named in *Scope*; single
  grep-hit lines from unrelated board items and old `CHANGELOG.md` entries; filenames (not
  contents) of prior verdicts; and its own cross-session memory index. It did not open the intent
  record, the commissioning board item, `docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md` or any prior verdict. Its orchestrator read the `docs/SESSIONS.md` index
  tail (entries through 2026-10-16, including the authoring run's one-paragraph summary) and the
  2026-10-16 session record's close section, and passed no evaluative content beyond the pointer
  list. Everything evaluative the brief-writer formed is in the sibling.

## What the work is

Landing commit (diff it on the delta path; review at HEAD, `2e2da81` or later):

- `347ebe2` (2026-10-03) — concurrency: worktrees don't share an external venv any more
  (200/100 C4)

Delta path: `docs/method/CONCURRENCY.md`, § *The substrate*, the first bullet under the
`git worktree add` example.

## Scope

Widest the work admits; the lenses organise it, they do not bound it. Non-goals are the only
narrowing and are themselves reviewable.

Probe, at least:

- **Fidelity to STORAGE.** `docs/method/STORAGE.md` § *The one gotcha* keeps venvs outside a
  synced folder *if a working copy must live in one*, with a parenthetical that in-repo `.venv`
  is now the norm for this estate. Does the bullet restate that faithfully — condition, scope
  (this estate or every adopter) and date — or promote an estate fact to general doctrine?
- **"Makes its own, or points at the primary's explicitly."** Drive both options in a scratch
  clone with a small Python project: one installed editable into the primary's `.venv`, one
  installed normally, one with a console script. From a linked worktree using the primary's
  interpreter, which source tree does an import or a test run load? Repeat with the worktree's
  own fresh venv. Record what each option actually does.
- **The retained clause.** "Worktrees live outside iCloud to avoid sync churn": is that still the
  reason after the estate left iCloud, and does `~/worktrees/…` match where the harness's native
  worktree support puts worktrees (see this repo's `.gitignore` and CONCURRENCY's own references
  to native support)?
- **Reach.** Which repos does the bullet bind? Check what atelier's own `tools/` and
  `instruments/` need to run, and whether the guidance is exercised anywhere it is stated.

**Non-goal:** STORAGE's move away from synced folders (already doctrine); the bullet's agreement
with it is the subject.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Ask whether a
   one-line fix to a stale sentence left the bullet's other claims standing on old grounds.
2. **Correctness & quality.** Diff `347ebe2`. Record the venv probe results as a table: option,
   project shape, which tree's code ran.
3. **Completeness / harvest.** Every other site that tells a session where a venv lives or how a
   worktree gets one: STORAGE, `docs/method/TOOLBOX.md` (venv-installed CLIs),
   `docs/build/REPO-STANDARD.md` and `docs/build/templates/gitignore`, the create-repo and
   session-onramp skills. Which still describe the shared external venv?
4. **Security & privacy** — mandatory. Pointing one checkout at another's environment executes
   code installed from that other checkout. Say whether that matters for any reading of the
   bullet, or discharge it in one line with grounds. `/security-review` is discharged by grounds.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- the venv probe above, in a private scratch clone, never against a live checkout or its venv
- `git log -S 'external venv' --oneline` to find every site that carried the old claim
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`)

## House rules for this run

- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and your scratch
  clone. Never open another `docs/reviews/2026-10-16-1510-*` file — it is another pass's framing.
- No git command that writes in the worktree, beyond committing this one file at the end of each
  phase (or handing it to your orchestrator to commit). Read-only git is fine. Probe projects,
  venvs and linked worktrees go in a private clone under your session scratchpad, named by your
  prefix; remove what you created.
- One heavy process at a time: the full Python suite at most once, in the foreground; never point
  a scanner at another repo on the machine.
- `/security-review` reads the session's pending diff, not this delta. Discharge it by grounds, or
  keep the tree clean when you spawn it — never with this brief or its sibling dirty.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. Never quote
  a secret, a placeholder token, an email address or a personal detail — this repo is PUBLIC.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/550-rule-4-cold-pass-queued-worktree-venv.md`, the sibling
`docs/reviews/2026-10-16-1510-worktree-venv-cold.deferred.md`, the landing commit's message body
(the author's account; read subject, stat and diff only), and the commissioning item
`docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md`.

Sweep with `python3 tools/coldsweep.py --root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/550-rule-4-cold-pass-queued-worktree-venv.md
--also-exclude docs/reviews/2026-10-16-1510-worktree-venv-cold.deferred.md --also-exclude
docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is never
barred; the author's narrative of why, and the verdicts that recorded it, are.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Append your verdict
below a `---` divider in THIS file: provenance repeated (how you were spawned, your tier, what you
read), per-lens answers, findings with stable IDs (prefix `WV`: `WV1`, `WV2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands and results) and a follow-up checklist. Then STOP and commit this file
before opening the sibling. Edit no other file.

**Phase 2.** Open the sibling. Append `### Reconcile` beneath your verdict: per-finding notes
against its seeded questions and the intent record, any finding formed at reconcile marked as
such, and the overall line restated. Never revise phase-1 text. Fold the sibling in below the
reconcile and delete it.

Findings on doctrine are the principal's to decide (rule 3): record all, apply nothing; counsel
per finding is welcome, labelled as counsel.

---

# Verdict — phase 1 (2026-10-17 UTC)

## Provenance, repeated

- **Reviewer:** a fresh `claude-fable-5-1` subagent (Fable, the principal-named review tier —
  on tier, no off-tier disclosure needed), spawned 2026-10-17 by a Fable orchestrator running the
  2026-10-17 rule-4 batch. Neither the reviewer nor its orchestrator authored the delta
  (`347ebe2`, a 2026-10-03 queue run) or this brief (an Opus brief-writer, 2026-10-16), and
  neither was started or instructed by either author. Rule 4's criterion is met.
- **Worktree:** `~/worktrees/atelier-review-1017`, branch `review-1017`, HEAD `92ca3de`
  (`347ebe2`, `2e2da81` and `8acfff1` all verified ancestors with `merge-base --is-ancestor`).
  Read-only to this reviewer except this file; no git write command was run.
- **Context partition in force:** the sibling `.deferred.md` and its twenty siblings were moved
  out before spawn; the barred set (prior verdicts, `docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md`, the queue pointer, the commissioning item, the landing commit's
  message body) stayed closed. The commit was read as subject, `--stat` and diff only.
- **What was read:** the delta at `347ebe2` and at HEAD; `STORAGE.md` in full; `REVIEW.md`
  §§ Independence, four lenses, re-run, standing checklist, lifecycle; `TOOLBOX.md`,
  `REPO-STANDARD.md`, `templates/gitignore`, `.gitignore`, `commands/worktree.md`,
  `tools/worktree.py` (docstring, iCloud guard, harness-path matching), `tools/README.md`
  (worktree rows), ADR 0006 (browser-fetch venv), both READMEs' STORAGE lines, the
  `session-onramp` and `create-repo` skills' worktree mentions, `.githooks/pre-commit`,
  `tools/floor.py --help`, `.github/workflows/ci.yml`, `.atelier-floor.json`.
- ⚠️ **Exposure, disclosed:** one plain `grep -rn` for worktree-command references (run outside
  `coldsweep`) printed five `docs/SESSIONS.md` *index* lines — the 2026-07-10 worktree-tooling,
  2026-07-12 concurrency-triggers, 2026-07-20 recovery-sweep, 2026-07-21 plugin and 2026-08-05
  cold-pass entries. None concerns this delta or its author's run; nothing below rests on them.
  `docs/ROADMAP.md:277` (the pointer's one-line title) also surfaced in a sweep. Every other
  tree search ran through `coldsweep` with the three `--also-exclude` paths; `--include-barred`
  was **not** used. The session scratchpad is shared with sibling reviewers (their prefix
  directories are visible); none was opened.

## Lens 1 — approach and assumptions

Load-bearing assumptions, named before the probe:

- **A1.** A worktree does not inherit the primary's gitignored `.venv`. *(True — a fresh linked
  worktree lists `.git .gitignore pyproject.toml src tests`, no `.venv`.)*
- **A2.** "Makes its own" and "points at the primary's" are interchangeable ways to get a
  working environment. *(False for every shape probed except a flat-layout import from the
  worktree's cwd — WV1.)*
- **A3.** Worktrees are a thing that "live outside iCloud" at `~/worktrees/…`. *(True only of
  the manual path and `tools/worktree.py`; the harness-native path this same section
  recommends nests at `.claude/worktrees/` inside the primary checkout — WV2.)*
- **A4.** "The norm is an in-repo `.venv`" is a doctrine statement. *(It is an estate fact
  STORAGE holds as a parenthetical under a conditional rule; the bullet imports the fact and
  drops the condition — WV3.)*

Was the one-line fix made on old grounds? Partly. The venv half of the old sentence was
replaced; the location half was kept verbatim, and the new second sentence ("since the estate
left iCloud") retires the reason the first sentence still gives. A reader is told worktrees live
outside iCloud *to avoid sync churn* and, in the next breath, that the estate is no longer in
iCloud. The bullet now carries a reason that does not apply and a location that is not where the
recommended tooling puts them.

## Lens 2 — correctness and quality

The diff of `347ebe2` on the delta path is five lines: it deletes "the external venv is shared
across them, which is what you want" and adds the dated STORAGE citation, the no-carry statement
and the two options. Three claims, three results:

| Claim | Result |
|---|---|
| estate left iCloud 2026-07-14, in-repo `.venv` the norm | matches `STORAGE.md` lines 18 and 59 verbatim in substance and date |
| a worktree does not carry the primary's gitignored `.venv` | **verified** — fresh worktree carries no `.venv` |
| a worktree "makes its own, **or points at the primary's explicitly**" | **the second option runs the wrong tree's code** — table below |

**Venv probe** (private scratch clone under the reviewer's scratchpad `WV/`; Python 3.14.6;
a `pkgwv` project with `src/` layout and a `pkgflat` project with the package at the repo root,
each with a console script and a unittest; the primary marked `TREE="PRIMARY"`, the linked
worktree committed with `TREE="WORKTREE"`; every command run from the worktree's cwd):

| Layout | Environment used | Invocation | Tree whose code ran |
|---|---|---|---|
| src | primary `.venv`, `pip install -e .` | `python -c "import pkgwv"` | PRIMARY |
| src | primary `.venv`, editable | `python -m unittest discover` | PRIMARY |
| src | primary `.venv`, editable | console script | PRIMARY |
| src | primary `.venv`, editable | `source …/activate`, then import | PRIMARY |
| src | primary `.venv`, editable | `source …/activate`, then console script | PRIMARY |
| src | primary `.venv`, editable | `.venv` symlinked to the primary's | PRIMARY |
| src | primary `.venv-normal`, `pip install .` | import / unittest / console script | PRIMARY (a site-packages snapshot taken at install time) |
| flat | primary `.venv`, editable | `python -c "import pkgflat"` | WORKTREE (cwd shadows the install) |
| flat | primary `.venv`, editable | `python -m unittest discover` | WORKTREE |
| flat | primary `.venv`, editable | console script | **PRIMARY** |
| flat | primary `.venv`, editable | `activate`, then console script | **PRIMARY** |
| flat | primary `.venv`, editable | import with cwd elsewhere | PRIMARY |
| src | worktree's **own** `.venv`, editable | import / unittest / console script | WORKTREE |

Reading: with a `src/` layout — the shape the editable installs STORAGE names as estate
machinery produce — *every* way of pointing at the primary's venv runs the primary tree's code,
including the test run, which passes green against code the worktree never contained. With a
flat layout the result is split: imports and tests see the worktree, the console script sees the
primary — a session can watch its tests pass on its edits and its CLI ignore them. Only the
worktree's own venv runs the worktree in every row. The three readings of "explicitly"
(interpreter path, `activate`, symlink) behave identically, so wording cannot rescue the option.

## Lens 3 — completeness and harvest

- `git log -S 'external venv'` finds the phrase entering at the scaffold commit (`4dce8cd`,
  in both CONCURRENCY and STORAGE), leaving STORAGE at `c6d66c8` (2026-07-14) and leaving
  CONCURRENCY at `347ebe2`. No other live surface carried it. A `coldsweep` for the old
  sentence's fragments and for `~/.venvs` hits only STORAGE's conditional rule. **The literal
  sweep is complete.**
- Sites that tell a session where a venv lives or how a worktree gets one: STORAGE (updated
  2026-07-14, conditional rule kept); TOOLBOX (venv-installed *CLIs* under a user-local path —
  a different object, consistent); REPO-STANDARD line 97 and `templates/gitignore` (ignore
  `.venv/` — consistent); `commands/worktree.md`, `tools/worktree.py`, `tools/README.md`
  (location only, no environment step — WV6); the `create-repo` and `session-onramp` skills
  (no venv guidance at all). None still describes the shared external venv.
- Sites that still describe the *iCloud topology* the bullet now cites as retired: `README.md`
  lines 61–62 and `docs/method/README.md` line 42 — WV4.
- **Reach.** atelier itself exercises none of this: `tools/` is stdlib-only (its `.gitignore`
  says so; the import census finds only stdlib and in-repo modules), `instruments/` is `node:`
  only, and the one venv atelier does build (browser-fetch, ADR 0006) is deliberately
  *external* at a cache path and shared across every checkout — so inside this repo the
  deleted sentence was the true one and the new one is unexercised. The bullet binds every child
  that reads CONCURRENCY through the doctrine block; children were not opened (house rule).
  STORAGE's own text ("editable installs" as estate machinery) says the WV1 shape is the
  estate's shape — WV5.

## Lens 4 — security and privacy

- **Design altitude.** Pointing a worktree at the primary's venv executes code installed from
  the primary checkout — with an editable install, the primary's *live files*, which a parallel
  session may be editing uncommitted. That is an integrity exposure of the OWASP A08 shape
  (software and data integrity: running code you did not check out), but it crosses no trust
  boundary — same user, same machine, the same trust class the pre-commit hook already assigns
  to its tools directory. It is therefore recorded as the correctness finding WV1, not as a
  security finding; no recurrence-prevention step beyond WV1's counsel is owed.
- **Code altitude.** None: the delta is five lines of markdown. Injection, XSS, authn/z, secret
  handling and input paths do not arise.
- **Privacy.** The delta carries a date, a doc name and generic paths; no person, host, email
  or estate detail. This verdict quotes none either.
- **`/security-review` — discharged by grounds.** It reads the session's pending diff, which
  here is other reviewers' drafts and the partition's sibling deletions, not this landed delta;
  and its exclusions bar markdown, so a clean pass would be definitionally empty. Not run.

## Standing checklist V1–V7

- **V1** — the bullet claims an option works that the probe shows runs the wrong tree → WV1.
  Its other two claims are evidenced (STORAGE, the fresh-worktree listing).
- **V2** — the delta records no "live-proven" claim; the floor was re-run on both planes at
  HEAD (ledger below) and the probe re-drove the bullet's operational claim.
- **V3** — the venv claim's mirrors are swept clean; the imported iCloud fact is not → WV4.
- **V4** — the bullet is a stamped copy (dated, cites STORAGE) of STORAGE's fact: acceptable
  shape. The `~/worktrees` location fact lives in four places (CONCURRENCY, the command, the
  tool, its README), pre-existing and mutually consistent — discharged.
- **V5** — the bullet contradicts its own section on where worktrees live → WV2.
- **V6** — lens 4 above.
- **V7** — provenance stated in the brief and repeated above.

## Findings

**WV1 — MAJOR.** *"…or points at the primary's explicitly" steers a session into running the
primary checkout's code while believing it runs its own.* Proven above: for a `src/`-layout
project with an editable or normal install, 9 of 9 invocations from the worktree — import,
`unittest`, console script, under interpreter path, `activate` and symlink alike — executed the
PRIMARY tree; for a flat layout the console script did while imports did not. The bullet offers
the option as an equal alternative with no condition and no warning, which is exactly the
silent-failure mode the brief's "why it earns a review" names. *Counsel (not applied):* make
"makes its own" the rule; permit pointing at the primary's only when the project itself is not
installed into that venv (dependencies only), and say in the same breath that entry points and
console scripts resolve to the primary regardless — or drop the option and point at STORAGE for
the one-liner (`python3 -m venv .venv && pip install -e .`).

**WV2 — MODERATE.** *The retained clause stands on grounds the next sentence retires, and names
a location the recommended path does not use.* "Worktrees live outside iCloud (`~/worktrees/…`)
to avoid sync churn" is followed by "since the estate left iCloud". The reason no longer applies
to the estate, and the location is only the manual / `tools/worktree.py` base: the harness-native
worktrees this same section tells sessions to take "by default" (lines 50–52, 66–68) nest at
`.claude/worktrees/<branch>/` *inside* the primary checkout — `.gitignore` line 20, ten ignore
files and `tools/worktree.py` lines 510 and 536 all say so. Where a worktree lives is therefore a
property of the primary's location, not of worktrees. For an adopter whose working copy is in a
synced folder, following § The trigger violates § The substrate's first clause. *Counsel:* state
the invariant that is actually true — a worktree lives wherever its base is; keep `.git` indices
out of synced folders (STORAGE's gotcha, `worktree.py`'s guard) — and note the two bases.

**WV3 — minor.** *The bullet imports STORAGE's estate fact and drops STORAGE's condition.*
STORAGE's rule is conditional — *if a working copy must live in a synced folder*, the venv lives
outside it — with the in-repo norm as a dated parenthetical for this estate. The bullet's only
scope word is "the estate"; an adopter in a synced folder reads CONCURRENCY, not the
parenthetical, and learns the in-repo norm as doctrine. *Counsel:* one clause — "(outside a
synced folder; STORAGE's gotcha applies otherwise)".

**WV4 — minor.** *Two index summaries still describe the topology the bullet calls retired.*
`README.md` lines 61–62 ("iCloud = backup/offline … keep churn out of iCloud") and
`docs/method/README.md` line 42 ("iCloud backup") summarise STORAGE as it stood before
2026-07-14. Outside the delta path, inside the mirror surface of the fact the delta leans on
(V3). *Counsel:* re-summarise both to STORAGE's current three-location table.

**WV5 — note.** *The guidance is unexercised where it is stated.* atelier needs no venv
(stdlib `tools/`, `node:`-only `instruments/`), and its one venv (browser-fetch) is external by
ADR 0006 and shared across checkouts by design — the deleted sentence's shape. The bullet is
written for children with editable-installed projects, which STORAGE says exist; this pass could
not open them. Recorded so the reach is honest, not as a defect in the sentence.

**WV6 — note.** *The doctrine's mechanical form does not carry the new rule.* `tools/worktree.py
start`, `/atelier:worktree` and the `git worktree add` one-liner above the bullet all stop at the
checkout; none creates or mentions an environment, so the "makes its own" step the bullet now
requires is left to memory — the failure the tool's own docstring says it exists to remove.
*Counsel:* after WV1 is decided, have `start` print the one-liner (or run it when a
`pyproject.toml` is present) rather than add a second prose site.

## Overall

**PASS-WITH-FINDINGS — 1 MAJOR · 1 MODERATE · 2 minor · 2 note.** The cycle stays open
(REVIEW § lifecycle: it closes when a pass returns no MAJOR). All findings are on doctrine and
are the principal's to decide; nothing was applied.

## Re-run ledger

All runs 2026-10-17 UTC from the worktree root, heavy steps under `nice -n 10`, one at a time;
load average 5–12 before each.

| Step | Command | Result |
|---|---|---|
| CI-plane floor at HEAD | `python3 tools/floor.py --plane ci --root . --json` | exit 0; 16 checks rc 0; secretscan 23 advisory (the expected advisory tier), all others 0 |
| hook-plane floor at HEAD | `python3 tools/floor.py --plane hook --root . --json` | exit 0; 16 checks rc 0, 0 advisory |
| old-claim history | `git log -S 'external venv' --oneline` | `88f9925` (the briefs), `347ebe2`, `c6d66c8`, `4dce8cd` — no other live site |
| barred-aware sweeps | `python3 tools/coldsweep.py --root . [-i] --also-exclude ×3 <pattern>` for `venv`, worktree-location terms, old-sentence fragments | 396 files excluded as barred each run; hits listed under lens 3; `--include-barred` not used |
| venv probe, stage 1 | scratch `WV/probe-setup.sh`: src-layout project, primary `.venv` (editable) and `.venv-normal` (regular), linked worktree with a different tree marker | built; worktree carries no `.venv` |
| venv probe, stage 1b | scratch `WV/probe-setup2.sh`: flat-layout project, primary `.venv` (editable), linked worktree | built |
| venv probe, stage 2 | scratch `WV/probe-run.sh` | the 19-row table under lens 2 (`WV/probe-results.txt`) |
| ancestry | `git merge-base --is-ancestor` for `347ebe2`, `2e2da81`, `8acfff1` | all ancestors of HEAD `92ca3de` |
| not run, by rule | full Python suite; `node --test`; `/security-review` | the brief's re-run list does not name the suites; the scanner is discharged under lens 4 |

Scratch artefacts (clones, venvs, worktrees) live only under the reviewer's scratchpad `WV/`
directory and are left for the orchestrator's sweep.

## Follow-up checklist

- [ ] WV1 — ruling owed: drop or condition "points at the primary's"; if kept, name the
      deps-only condition and the console-script caveat.
- [ ] WV2 — ruling owed: restate the location clause as a property of the base, naming both
      bases (`~/worktrees` manual; `.claude/worktrees/` harness-native).
- [ ] WV3 — ruling owed: add the synced-folder condition or a pointer to STORAGE's gotcha.
- [ ] WV4 — re-summarise STORAGE in `README.md` and `docs/method/README.md`.
- [ ] WV5 — no action; record only.
- [ ] WV6 — after WV1: teach `tools/worktree.py start` the environment step, or decide not to.
- [ ] Application of the rulings is a doctrine edit and earns its own cold pass (REVIEW
      § Applying decisions); this pass returned a MAJOR, so the cycle stays open.

### Reconcile (phase 2, 2026-10-17 UTC)

Opened after phase 1 was committed (`fc70ff5`): the sibling's text (relayed verbatim by the
orchestrator), the landing commit's message body, the commissioning item (`200/100`, C4), the
intent record (the 2026-10-03 0144 UTC queue-run session) and the two prior CONCURRENCY verdicts
the sibling names. The three-cues and harvest briefs of this batch stayed closed. Phase-1 text
above is unchanged.

**Against the seeded questions.** All three seeds and three of the six phase-1 findings
coincide; the findings were formed and committed before the seeds were read, so the overlap is
convergence, not steering. The three findings outside the seeds (WV4, WV5, WV6) are where this
pass added to the floor.

- *Seed 1* (the primary's venv imports the primary's source; name it or drop the option) ↔
  **WV1**. Converged, and the phase-1 probe answers the seed's conditional: not "could", but
  did — 9 of 9 src-layout invocations and every console script in both layouts. The seed's
  either/or is the counsel already recorded; the pass does not choose between them (rule 3).
- *Seed 2* (an estate fact presented as doctrine, unconditionally) ↔ **WV3**. Converged; the
  severity stays minor. The scope word "the estate" is present, so this is a dropped condition
  rather than a false claim, and the harm is bounded to adopters still in a synced folder.
- *Seed 3* (the retained first sentence stale; harness-native worktrees under `.claude`) ↔
  **WV2**. Converged, and the pass grounds the second half the seed only gestures at:
  `.gitignore` line 20, ten ignore files and `tools/worktree.py` lines 510 and 536 place the
  harness-native path inside the primary, and § The trigger's "take a worktree by default"
  points sessions at exactly that path.

**Against the intent record and the commissioning item.** The commissioned fix was C4 of the
eleven contradictions: *make the bullet agree with STORAGE*. The item's close note and the
commit body describe two edits — drop the shared-external-venv claim, add the no-carry
consequence. Both re-verified true in phase 1. Neither record mentions the two-option sentence
("makes its own, or points at the primary's explicitly"): that clause went beyond the recorded
intent and carries no decision or reasoning anywhere in the record. The intent record itself
holds no C4-specific account beyond the batch line ("each fixed separately with its own pass");
the commit body is the author's only narrative. The author's framing — a stale-layout
correction — explains the shape of the defect: it corrected the venv half and reached for a
practical consequence without re-driving it, and left the location half as found.

**Against the two prior verdicts.** `2026-07-11-concurrency-put-away.md` and
`2026-07-20-1355-concurrency-flip-cold.md` contain no line on venvs, iCloud, `~/worktrees` or
the substrate bullet: this bullet has never been under review before. WV2's stale clause is
therefore not a regression past a prior pass; it is first-time cover.

**Finding formed at reconcile.**

**WV7 — note (formed at reconcile).** *The clause that carries the MAJOR is undocumented
scope.* The commissioning item records the fix as "follows STORAGE … and adds the consequence: a
worktree does not inherit the gitignored `.venv`"; the commit body says the same. The
"makes its own, or points at the primary's explicitly" sentence appears in neither, so the
option WV1 found defective was added without a recorded reason — a claim without its test
(PRINCIPLES §6). Recorded for the pattern, not as a second count against the sentence; it
sharpens WV1's counsel toward dropping the option rather than conditioning it, since there is
no stated purpose to preserve.

**Overall, restated:** **PASS-WITH-FINDINGS — 1 MAJOR · 1 MODERATE · 2 minor · 3 note.** The
reconcile changed no phase-1 severity; it added one note. The cycle stays open on WV1.

## Deferred material — folded in at reconcile

# Sibling to the worktree-venv cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-16-1510-worktree-venv-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-16 UTC by the Opus brief-writer named in the brief's provenance; it
forms no finding. Fold this file in below the reconcile and delete it at phase 2.

## Intent and commissioning records

- Intent record: `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md` —
  **not opened by the brief-writer**.
- Commissioning item: `200/100` C4, in
  `docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md`
  — **not opened by the brief-writer**.
- The landing commit's message body (read by the brief-writer): it says the bullet described the
  iCloud-era layout, that STORAGE made in-repo `.venv` the norm when the estate left iCloud, and
  that the new text adds the consequence a session meets in practice.

## Prior verdicts on these surfaces (named by filename grep, not opened, not exhaustive)

No verdict carries the old "external venv" phrase. Nearest CONCURRENCY substrate passes by name:
`docs/reviews/2026-07-11-concurrency-put-away.md`,
`docs/reviews/2026-07-20-1355-concurrency-flip-cold.md`.

## The pointer's own lens hints

None. The pointer is refs-only; its last sub-bullet is the brief-writer's orchestrator's claim.

## Overlap with sibling passes of this batch

`docs/method/CONCURRENCY.md` is also the subject of the three-cues pass (§ *The trigger*) and the
harvest pass (the closing-litany bullet). Different sections; sequence them if one runner takes
several.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. "Or points at the primary's explicitly" re-admits the sharing the old text recommended. With
   an editable install, the primary's venv imports the primary's source, so a worktree's tests
   could run the wrong tree and pass. Should the bullet name that, or drop the option?
2. STORAGE's rule is conditional on a synced working copy; the bullet states "the norm is an
   in-repo `.venv`" unconditionally, with an estate-history date, in a doctrine file adopters
   read. Is that an estate fact presented as house doctrine?
3. The retained first sentence still gives iCloud sync churn as the reason worktrees live in
   `~/worktrees/`, after the estate left iCloud, while harness-native worktrees land in a
   worktrees folder under the repo's own `.claude` directory (per this repo's `.gitignore`). Did
   the fix leave the bullet's other half stale?
