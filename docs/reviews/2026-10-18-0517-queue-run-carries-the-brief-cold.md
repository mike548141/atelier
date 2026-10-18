# Cold pass — the queue-run skill carries the run brief, teardown, and the identifiers block

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-18 UTC by an Opus brief-writer;
the pass waits for a cold Fable session that neither the delta's author nor this brief-writer
(nor its orchestrator) started or instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/900-rule-4-cold-pass-queued-queue-run-carries-the-brief.md`.
**Why it earns a review:** this delta decides what every orchestrated queue run reads and does.
`/atelier:queue-run` is the plugin's entry point to the pattern, so the skill, the prompt it now
loads and the `CONCURRENCY.md` passages it anchors to reach every repo that installs the plugin.
The delta also adds a teardown rule that guards workers in flight, a close-out block every
session record now ends with, and a change to how the plugin is versioned. The worst failure is
a run that follows the command faithfully and still skips a rule that lived in only one of
these places, or follows a rule that has drifted between them.

## Spawn provenance

- **Author of the work under review:** one authoring session — a Mike-opened Opus 5.5 queue run,
  session `e1d4097c`, record `docs/sessions/2026-10-18-0001-queue-run-the-plugin-installed.md`
  (barred to the reviewer until phase 2). That one session authored the whole of the `160/900`,
  `160/910` and `160/930` deltas; the pointer names its worktree as `atelier-qr-180-plugin`. The
  brief-writer did not read any landing commit's message body or the intent records, so it
  cannot say which parts a worker drafted.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched on 2026-10-18 by a
  different Mike-opened Opus 5.5 queue run, session `8e498ef1` (worktree
  `atelier-qr-briefs-1018`), which Mike started directly with a bare `/atelier:queue-run`. The
  dispatching run was **neither started nor instructed by the authoring session**, and neither
  it nor the brief-writer authored any of this delta. **Verified from git** (commit times, read
  with `git log --format='%h %cI %s'`): the delta's commits run from `998c35f` (00:09 UTC) to
  `6810b64` (03:50 UTC), and `12e6d9b` (authored 05:00, committed 05:06 UTC) after the
  authoring session's own claim `5eb1750` (04:58 UTC). The dispatching run's own commits are
  `f0d6238` (05:00 UTC) and `a9f11ff` (05:09 UTC), both board claims. Git cannot name a session;
  the session attribution is the dispatching run's account, and two lines of the authoring
  session's record agree with it (it records the dispatching run as "opened by Mike" and
  "watched from here"). One oddity, stated as fact: that record's identifiers line gives its
  window as 2026-10-17 23:59 to 2026-10-18 04:14 UTC, while `12e6d9b` and the watch it records
  both fall after 04:14. **A further fact the reviewer should weigh:** the dispatching run is
  itself a `/atelier:queue-run` session, so it ran under an earlier text of the very skill this
  pass reviews (the record says it loaded the skill as it stood before `180/090`). **Off-tier
  for review, disclosed: the brief-writer forms no finding and writes no severity**, and stops
  after this brief and its sibling.
- ⚠️ **One channel contact, disclosed for the reviewer to weigh** under roadmap `280/040` (the
  cross-session channel can contaminate review independence). After this brief-writing began,
  the authoring session sent the dispatching run's orchestrator one cross-session file-set
  notice: that `ccclose` had changed under that run's `210/290` worker, a request to rebase
  before merging, and a note that `12e6d9b` had landed and `160/900` had been widened to it. The
  orchestrator reports it carried no evaluative content about any delta. The brief-writer never
  saw the notice itself, only the orchestrator's paraphrase of it. This brief's delta list comes
  from the pointer on `origin/main`, read after that widening.
- **Who takes the review:** a cold Fable session, not yet started, passing rule 4's criterion. If
  it runs as reviewer-plus-orchestrator, rule 4's off-tier conditions apply and are disclosed in
  the claim, the pointer and the verdict. The reviewer repeats its own provenance in the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material met before writing):
  - this pass's pointer in full at `origin/main` (refs-only, with a claim line), and its two
    other assigned pointers (`160/910`, `160/930`) in full; the `160/780` pointer in full as a
    shape example, including the summary of its verdict (another pass, on `EVIDENCE.md`);
  - the precedent brief `docs/reviews/2026-10-17-0930-agreement-not-corroboration-cold.md` (ask
    half and the head of its verdict) and its sibling as first committed (`b42f305`) — another
    pass's framing; no other file under `docs/reviews/` was opened;
  - every delta commit's subject, stat and diff through `tools/coldsweep.py --commit`, scoped to
    the delta paths (never a message body), and, at `origin/main`, the whole of
    `skills/queue-run/SKILL.md`, `docs/method/session-open/session-open-prompt.md`,
    `docs/method/session-open/README.md` (whose `180/060` section is `160/940`'s delta, another
    pass) and `tools/test_queue_run_single_source.py`; the plugin manifest; `REVIEW.md` rules
    1–4 and the `review-brief` skill;
  - it wrote the `160/910` and `160/930` briefs first, in the same sitting, on the same authoring
    session's other work;
  - the board item filenames under `180/` and the claim lines (first lines only) of `180/090`;
  - at its orchestrator's request, to check provenance, lines 139–145 and 159 of the authoring
    session's record (a passage on the dispatching run, and the record's identifiers line);
  - its harness-loaded memory index and instruction files, and recent `git log` subjects.

  It did **not** open the three intent records, the other `180/` items, `docs/SESSIONS.md`, the
  rest of `docs/sessions/`, `docs/ROADMAP-DONE.md` or any prior verdict. Its orchestrator passed
  it an instruction set (the pointer, where to read the current text, the prefix check), the
  provenance account above and the paraphrased notice, and no evaluative content about the
  delta. Everything evaluative the brief-writer formed is in the sibling, which holds nine
  questions and three facts.

## What the work is

Landing commits, all 2026-10-18 UTC and all on `main` (diff each on its delta paths; review the
paths at `origin/main`, `4839fd8` or later — the briefing worktree's own checkout is older):

| Commit | UTC | Delta paths named by the pointer |
|---|---|---|
| `998c35f` | 00:09 | `CONCURRENCY.md` § *Orchestrated queue runs* (*Where the doctrine is read from*, the three selection rules, what the report carries, the spend-directive reading, the ask cadence); `skills/queue-run/SKILL.md`; `README.md`; `docs/method/session-open/session-open-prompt.md` |
| `1487e9c` | 00:15 | the *teardown* rule in `CONCURRENCY.md` § *Orchestrated queue runs*, its worktree bullet in § *Integration hygiene*, one sentence in the skill |
| `140a190` | 03:24 | the restored prompt lines in the prompt, `CONCURRENCY.md` and the skill; `version` dropped from `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`; `README.md` |
| `1adf398` | 03:47 | session id first; the identifiers block in `RECORD.md` § *The session log*; prompt, `CONCURRENCY.md` and skill |
| `46320f8` | 03:49 | `RECORD.md`, the identifiers block (PRs, worktrees created) |
| `6810b64` | 03:50 | `RECORD.md`, the identifiers block (board items completed and created) |
| `12e6d9b` | 05:00 | the skill now loads the prompt file and adds nothing; `tools/test_queue_run_single_source.py`; `docs/method/session-open/README.md`; prompt; `README.md` |

The pointer names `6810b64` as "the one after" `46320f8`; that is the next `RECORD.md` commit,
confirmed. One later commit touches a delta path: `bdb1aba` (`RECORD.md`, for `210/300`) is not
in the pointer's delta. Say whether it touches the identifiers block, and whether the delta
should name it. `998c35f` and `140a190` also edit `CHANGELOG.md`; the pointer leaves it out.

**Read each commit body-free:** `python3 tools/coldsweep.py --root . --commit <sha> --path
docs/method --path skills/queue-run --path README.md --path .claude-plugin --path
tools/test_queue_run_single_source.py`. Plain `git show` is barred here: it prints the message
body before the diff, and reading is atomic (rule 1). Keep the `--path` flags: several of these
commits also edit their own intent records and this pass's pointer, which coldsweep does not
bar by default. Board and index edits are not the delta.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, test code and live
behaviour. The lenses organise it; they do not bound it. Non-goals are the only narrowing and
are themselves reviewable.

Probe, at least:

- **What a run actually receives.** Invoke `/atelier:queue-run` in a scratch session (or read
  what the harness hands a skill) and record exactly what text reaches the model: does the path
  form in the skill resolve, in a local-path install and in a GitHub install? Then trace every
  path and pointer the prompt itself gives a run, from a repo that is not atelier.
- **Harvest across `12e6d9b`.** The skill went from a step list to a pointer. Build a table of
  every rule the skill stated before `12e6d9b` (read its text at `12e6d9b^`) and where each now
  lives — the prompt, `CONCURRENCY.md`, another skill, or nowhere.
- **One text, or three.** The prompt, the `CONCURRENCY.md` passages "homed" from it, and the
  skill each state some of the same rules. For each shared rule, which is the home, do the
  copies agree today, and what guards each pair against drift (`EVIDENCE.md` §9;
  `PROPAGATION.md` § *One statement, stamped copies*)?
- **The single-source test.** Does it fail when the skill drifts from the prompt in the ways
  drift actually happens? Mutate a copy of the skill under your scratchpad and re-run it.
- **The prompt as principal-owned text.** `docs/method/session-open/README.md` now says an agent
  changes the prompt only on the principal's say-so, quoted in the commit. Diff the prompt
  across the whole delta (`998c35f^` to `origin/main`) and list every line added, removed or
  reworded. Whether each change had his say-so is reconcile work (the bodies and intent records
  are barred until then); the list is phase-1 work.
- **The teardown rule.** It rests on a harness notice and a terminal marker. Check what the
  harness actually gives an orchestrator, and walk the rule through a crashed worker, a slow
  verifier and a worker that never pushes.
- **The identifiers block.** For each field, where does a closing session get it, and can it get
  it at all (`ccclose`'s output; the transcript)? Run `ccclose` if it is installed and say which
  fields it prints.
- **Versioning by commit.** With `version` gone from both manifests, check what the README now
  says about updates and the pre-commit hook pin against the plugin tooling's real behaviour.
- **Where it reaches.** Surfaces that describe the queue-run pattern, the session open or close,
  or plugin installation — `README.md`, `docs/method/README.md`, the session-onramp and
  review-brief skills, `docs/build/` templates, `CHANGELOG.md`, the plugin manifests — and
  whether any now disagree.

**Non-goals:** the principal's own wording in the prompt, as his text, and his rulings quoted in
the delta. Whether the delta records and applies them faithfully, and every line an agent wrote
around them, are in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Ask whether
   making the command run a principal-owned prompt file is the right way to stop drift, set
   against the cost of the rules that file cannot hold.
2. **Correctness & quality.** Diff every commit on its paths. Check every cross-reference in the
   new text resolves to a passage that says what is claimed. Record the harvest table.
3. **Completeness / harvest.** The *Where it reaches* list, and the harvest table. Is each
   changelog entry accurate to what landed?
4. **Security & privacy** — mandatory. The prompt and the session-open README describe the
   principal's working practice in a public repo: check nothing beyond the recorded exceptions
   is named. The test reads files by fixed relative paths; check it reads nothing outside the
   repo. Treat the prompt as an instruction channel: a file the command runs word for word is a
   prompt-injection surface (OWASP LLM01) — say who can change it and what would catch a hostile
   change. `/security-review` is discharged by grounds for the prose; aim it at the one Python
   file only from a clean tree.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing. The brief-writer ran each line once, against
an export of `origin/main` at `4839fd8` (the coldsweep and `git log` lines from its worktree);
read exit codes explicitly.

- `python3 -m unittest discover -s tools -p test_queue_run_single_source.py -v`
- the coldsweep line above for each of the seven commits — exit 0 and its closing line each time
- `python3 tools/wrapscan.py --root . docs/method/CONCURRENCY.md skills/queue-run/SKILL.md
  README.md docs/method/session-open/session-open-prompt.md docs/method/session-open/README.md
  docs/method/RECORD.md` — at `4839fd8` this exited non-zero on one line; say which and whose
- the same paths through `tools/spellscan.py` and `tools/leakscan.py` (add both manifests to
  the leakscan run); `python3 tools/linkscan.py --root . .`; `python3 tools/stampscan.py --root
  . .`
- `git log --oneline 12e6d9b..origin/main -- <the delta paths>` — each commit named
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`, and `--plane
  hook`), in your own checkout of `origin/main`

## House rules for this run

- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and your scratch
  clone. Never open another `docs/reviews/2026-10-18-*` file — it is another pass's framing.
- No git command that writes in the worktree, beyond committing this one file at the end of each
  phase (or handing it to your orchestrator to commit). Read-only git is fine. Scratch sessions,
  mutated copies and older checkouts go under your session scratchpad, named by your prefix.
- One heavy process at a time, in the foreground; never point a scanner at another repo.
- If you invoke `/atelier:queue-run` as a probe, do it in a throwaway directory with no board,
  and stop it before it claims anything: it is the live command, and a claim it pushes is real.
- `/security-review` reads the session's pending diff, not this delta. Discharge it by grounds,
  or keep the tree clean when you spawn it — never with this brief or its sibling dirty.
- This pass is itself pending while you run it: anything you write to the session log, the
  pointer or a commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. Never quote
  a secret, a placeholder token, an email address or a personal detail — this repo is PUBLIC.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/900-rule-4-cold-pass-queued-queue-run-carries-the-brief.md`,
the sibling `docs/reviews/2026-10-18-0517-queue-run-carries-the-brief-cold.deferred.md`, every
landing commit's message body (read subject, stat and diff only, by the coldsweep line above),
and the whole board directory the intent records sit in — the three intent records (`180/010`,
`180/020`, `180/030`), the items the later commits close (`180/040`, `050`, `070`, `080`, `090`)
and `180/060` (another pass's delta):

- `docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/`

The prompt file, the skill's header comment, the session-open README and the test's docstring
quote the principal and give short reasons; they are the delta, and reading the delta is never
barred.

Sweep with `python3 tools/coldsweep.py --root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/900-rule-4-cold-pass-queued-queue-run-carries-the-brief.md
--also-exclude docs/reviews/2026-10-18-0517-queue-run-carries-the-brief-cold.deferred.md
--also-exclude docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie <pattern>`;
`--include-barred` only with disclosure in the verdict. The author's narrative of why, and the
verdicts that recorded it, are barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses, the probes and the re-run list. Append
your verdict below a `---` divider in THIS file: provenance repeated (how you were spawned, your
tier, what you read), per-lens answers, findings with stable IDs (prefix `QK`: `QK1`, `QK2`, …)
and severities (MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, a re-run ledger (commands and results) and a follow-up checklist. Then STOP and
commit this file before opening the sibling. Edit no other file.

**Phase 2.** Open the sibling. Append `### Reconcile` beneath your verdict: per-finding notes
against its seeded questions and the intent records, any finding formed at reconcile marked as
such, and the overall line restated. Never revise phase-1 text. Fold the sibling in below the
reconcile and delete it.

Findings on doctrine are the principal's to decide (rule 3): record all, apply nothing; counsel
per finding is welcome, labelled as counsel.
