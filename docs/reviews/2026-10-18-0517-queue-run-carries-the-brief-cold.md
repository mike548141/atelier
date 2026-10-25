# Cold pass — the queue-run skill carries the run brief, teardown, and the identifiers block

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass.
**Status:** PASS-WITH-FINDINGS — acts 1 and 2 written 2026-10-25 UTC by a Fable 5.1 reviewer;
1 MAJOR · 6 MODERATE · 4 minor · 3 notes (QK1–QK14), all the principal's to decide (rule 3).
Brief written 2026-10-18 UTC by an Opus brief-writer; the deferred sibling is folded at the foot.
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

---

# Verdict — phase 1 (cold), written 2026-10-25 UTC

**Status:** PHASE 1 WRITTEN, phase 2 (reconcile) not yet run. **Overall: PASS-WITH-FINDINGS —
2 MAJOR · 6 MODERATE · 2 minor · 2 notes** (QK1–QK12). Findings on doctrine are the
principal's to decide; nothing is applied here.

## Provenance (REVIEW.md rule 4, V7)

- **Reviewer:** a Claude Fable 5.1 subagent (`claude-fable-5-1`), the principal-named review
  tier, checked at selection. Spawned by session `52e11d15` (Claude Opus 5.5), which
  orchestrates, holds the context partition, forms no finding and writes no severity. That
  session authored neither the delta nor this brief, and was not started or instructed by
  session `e1d4097c` (the author) or `8e498ef1` (the brief-writer's run). The pass was launched
  under the principal's approval of Fable work for the week ending 2026-10-25 23:00 UTC.
- **Worktree:** `~/worktrees/atelier-cold-160-900`, branch `atelier-cold-160-900`, based on
  `origin/main` at `7d58404`. The only file written is this one.
- **Context partition:** the `.deferred.md` sibling was removed from the tree before I started
  (git shows it as a held deletion) and is held by the orchestrator. I did not look for it, did
  not open git history for it, and did not list any scratch directory.
- **What I read:** this brief and `REVIEW.md` in full; every delta path at HEAD; each of the
  seven landing commits, plus `bdb1aba`, `880334a` and `9d65b6a`, body-free through
  `tools/coldsweep.py --commit` with the brief's `--path` flags (and `CHANGELOG.md` added);
  the skill at `998c35f^` and `12e6d9b^` (file blobs, not commit messages); the prompt's
  whole-delta diff; `CONCURRENCY.md` §§ *Integration hygiene* and *Orchestrated queue runs*;
  `RECORD.md` § *The session log*; `README.md` § *Install as a Claude Code plugin*;
  `tools/test_templates.py` (the queue-run class); `commands/install-hook.md`;
  `.githooks/pre-commit`; `.github/workflows/ci.yml`; `.atelier-floor.json` (scopes). No
  session log, no prior verdict, no board item under `180/`, no pointer, no `ROADMAP-DONE.md`.
  No `--include-barred` sweep was run.
- **Read outside the worktree, disclosed:** the harness's plugin records (`installed_plugins.json`,
  `known_marketplaces.json`, the cached plugin copy's manifest and skill header), the git state
  of the local clone the marketplace was added from (branch, head, `git status`, and the diff
  of its one uncommitted prompt line), and two pages of the public Claude Code plugin docs
  (manifest reference; loading reference). Nothing private is quoted below.
- **Live probes, disclosed:** I invoked the live `/atelier:queue-run` skill twice through the
  harness's Skill tool, once bare and once with a probe string as its argument, to record what
  text reaches the model. I took no action on it and claimed nothing. I ran `ccclose
  --identifiers` read-only against this worktree.
- **Interruption, disclosed:** the orchestrator reports the host rebooted twice and this
  process was cut at about 2026-10-25 20:37 UTC, after the probes and re-runs below and before
  anything was written here; scratch files were wiped. Results marked *(before the cut)* were
  observed then and are reported as observed; the mutation probe of the single-source test
  (QK9) was re-run after the cut in a fresh scratch directory under `/private/tmp`.

## Lens 1 — approach and assumptions

Load-bearing assumptions I named before reading the delta's own account:

- **A1 — "the command runs the file" means the model reads the file.** True in mechanism, not
  in guarantee: the harness hands the model the skill text (header comment included) with
  `${CLAUDE_PLUGIN_ROOT}` substituted to an absolute path, then appends the typed text as an
  `ARGUMENTS:` line. It does not inline the prompt. One further tool call by the model fetches
  it; a model that skips the read runs on a skill that holds no rules at all (QK4).
- **A2 — the file the command reads is the file that was reviewed.** False today for a
  local-path install: the harness loads the plugin in place from the clone's working tree, and
  that tree's prompt differs from `origin/main` (QK1).
- **A3 — the doctrine anchor the prompt gives resolves wherever the command runs.** False in a
  GitHub-only install and in any checkout not sitting beside a directory named `atelier` (QK3).
- **A4 — the harness tells the orchestrator when a worker has stopped.** `RECORD.md` itself
  records the notice as conditional (QK6).
- **A5 — the delta's commits each left the floor green.** False at `12e6d9b` (QK2).
- **A6 — a change to the prompt without the principal's say-so would be caught.** Nothing
  mechanical reads the say-so, and the commit body it lives in is exactly what a cold reviewer
  is barred from reading until phase 2 (QK1, QK5).

**Is running a principal-owned prompt file the right way to stop drift?** It removes the
skill↔prompt seam completely, and that was the ruling. It does so at three costs the delta
does not state: (i) the command carries none of doctrine's safety pins unless his file carries
them — which it did not for the 16 minutes between `12e6d9b` and `880334a`, and does now only
because `9d65b6a` wrote doctrine into his file on his ruling, inverting `CONCURRENCY.md`'s own
"point at it, never restate it" line for that file; (ii) a new seam opens between the working
tree and the reviewed text, with no guard (QK1); (iii) doctrine that now lives in his file
(the four stops, the rule-4 criterion) can only follow a doctrine change on his say-so, and
`test_templates.py` will red the floor until it does. Counsel: keep the design; guard the new
seam (QK1 counsel) and give the anchor a path that resolves in both installs (QK3 counsel).

## Lens 2 — correctness and quality

- Every cross-reference in the new text resolves: `ECONOMICS.md` § *The orchestrated-run tier
  split* (line 279), `PROPAGATION.md` § *One statement, stamped copies* (816), `EVIDENCE.md`
  §9 (117), `CONCURRENCY.md` § *Integration hygiene* and *teardown*. The one dangling
  reference (`ECONOMICS.md` § *Know which pool*, which no longer exists) was in the skill at
  `12e6d9b^` and went with the rewrite.
- `12e6d9b` landed red (QK2). `bdb1aba` does touch the identifiers block (the `ccclose`
  sentence) and the delta should name it, with `880334a` and `9d65b6a` (QK11).
- The harvest table is at QK4; the prompt's whole-delta line list is at QK5.
- The single-source test passes at HEAD and guards only the skill side of the seam (QK9).

## Lens 3 — completeness and harvest

- Surfaces that describe the pattern, checked: `README.md` (agrees; one over-general sentence,
  QK8), `docs/method/README.md` (does not mention `session-open/` at all, QK10), the
  `session-onramp` skill (one-line mention, agrees), the `review-brief` skill (no mention),
  `docs/build/` templates (no mention), `CHANGELOG.md` (accurate except the `998c35f` entry,
  QK5), both manifests (agree), `instruments/README.md` and `ccclose` (agree).
- Changelog accuracy: `140a190`, `1adf398`, `12e6d9b`, `9d65b6a` entries match what landed.
  `998c35f`'s entry says "two lines brought back into line with later rulings"; the commit
  removed nine units of the prompt and added two paragraphs (QK5).

## Lens 4 — security and privacy

- **Threat enumeration for the prompt as an instruction channel (OWASP LLM01).** The command
  executes a Markdown file word for word. Who can change what runs: (a) anyone who can land a
  commit on `main` (public repo); (b) on a machine with a local-path install, any process
  running as the user, including any agent session with the clone as its working directory,
  with no commit at all; (c) for a GitHub install, whoever's commit `/plugin update` fetches —
  the README says plainly this can include doctrine whose review is pending. What catches a
  hostile change: the pre-commit scanners (which judge shape, not intent — QR4), the four
  phrase pins in `test_templates.py` (an edit that keeps those four phrases passes), the
  single-source test (reads the skill, never the prompt's content), and a human reading the
  diff. Nothing runs between an uncommitted edit and the next session start. The delta names
  none of this; absent enumeration is the finding (QK1).
- **Privacy.** The prompt and the session-open README name no person beyond the principal's
  first name and no device, host or private repo; the README's template-history section names
  counts and dates of his sessions, which is `160/940`'s delta and its recorded exception.
  `leakscan` clean on every delta path and both manifests (ledger).
- **The Python file.** `tools/test_queue_run_single_source.py` is 46 lines of stdlib: two
  fixed in-repo paths derived from `__file__`, no argument, no network, no subprocess, no
  write. It cannot read outside the repo. Reviewed by hand.
- **`/security-review` — discharged by grounds.** My tree is not clean: it carries the held
  deletion of the deferred sibling, and a pending-diff scanner would read that deletion's
  content — the SL2 hazard the brief warns of. Aiming it at one file from a clean tree was
  therefore not available to me. Its clean pass on Markdown would be definitionally empty in
  any case.

## Findings

### QK1 — MAJOR — the command runs the working tree, and nothing guards that seam

**Observed.** The harness resolved `${CLAUDE_PLUGIN_ROOT}` to the local clone the marketplace
was added from and reported the skill's base directory inside that clone, not the cached copy
(`installed_plugins.json` still records the cache at version `0.2.0`, installed 2026-10-18
00:08 UTC, one minute before `998c35f`). The Claude Code loading reference confirms it: a
plugin from a local-path marketplace "loads its current source files at every session start,
whatever its version string says", and "your edits to the source directory take effect at the
next session start". That clone's prompt file is dirty: `git status` shows it modified, one
inserted line (a blank line between the two closing paragraphs — benign in content), file
mtime 2026-10-20/21 local time, and it differs from `origin/main`. So every queue run invoked
on that machine since the edit has run text that no commit, hook, CI run, test or review has
seen. The prompt's own sentence "(`/atelier:queue-run` runs exactly this file, so the command
and this text cannot differ)" is true of the working tree and false of the reviewed text.

**Why MAJOR.** The design's whole claim is "one text"; it holds between the command and the
file, and the delta moved the drift, un-named, to the file-versus-reviewed-text seam, which
has no guard and sits on a file the command executes as the principal's own brief. The
observed divergence is one blank line; the mechanism is proven.

**Counsel.** (a) Make the command's first act a check that the file it loaded equals the
committed one (`git diff --quiet -- <prompt>` from the plugin root), naming any drift in the
opening report rather than running it silently. (b) Mechanise the say-so rule: a commit that
touches the prompt must carry a marked trailer with his quoted words, checked by a floor
scanner, so the rule has a home a machine reads. (c) State the threat model in the session-open
README in three lines, so the next reader meets it rather than discovers it.

### QK2 — MAJOR — the delta's last commit landed with the floor red, and the repair is
### outside the pointer's delta

**Re-run.** `tools/test_templates.py` against complete exports of each tree, `python3 -I -m
unittest discover -s tools -p test_templates.py`: at `12e6d9b^` **OK (44)**; at `12e6d9b`
**FAILED, 6 failures**, all in `QueueRunSkillTest` — `test_marked_as_stamped_copy`,
`test_points_at_both_canonical_homes`, `test_skill_names_every_stop_condition`,
`test_rule4_criterion_phrase_in_both`, `test_chain_pin_in_both`,
`test_item_text_never_overrides_in_both`; at `880334a` **OK (44)**; at `9d65b6a` **OK (44)**.
The `12e6d9b` skill dropped the stamped-copy marker, the `ECONOMICS.md` pointer, the four
stop names, the rule-4 phrase, the chain pin and the never-overrides pin, and at that commit
the prompt carried none of them either, so the command as loaded from `main` between 05:06
and 05:22 UTC on 2026-10-18 carried no safety pin at all. `880334a`'s subject says it
("main's floor was red"); `880334a` restored the rails into the skill and `9d65b6a` moved them
into the prompt on the principal's ruling and rewrote the test to read skill plus prompt.

**Why MAJOR.** A doctrine commit landed red on the public mainline, and the pointer's delta
ends on that state: a review that honoured the pointer as written would have reviewed a
command that never held and would not have read the two commits that made it hold. The CI
floor exists so that this is caught before landing; it was not.

**Counsel.** Widen the pointer's delta to `880334a` and `9d65b6a` (and `bdb1aba`, QK11) before
phase 2; and treat "landed red" as its own lesson for `RECORD.md`'s floor-at-head rule — the
rule covers the close, and this was a mid-run push.

### QK3 — MODERATE — the doctrine anchor resolves only beside a sibling clone named `atelier`

The prompt anchors a run to `../atelier/docs/method/CONCURRENCY.md`. `pathscan` (warn-only)
flags it at HEAD on both planes. From a child repo it resolves only when a checkout named
`atelier` sits beside it; in atelier itself only when the checkout directory is so named; in a
GitHub-only install it resolves nowhere. `CONCURRENCY.md` holds the fallback ("else the
plugin's bundled copy, which is as old as its install") — inside the file the run cannot find.
The skill at `12e6d9b^` carried that fallback in its step 2; the rewrite dropped it, and the
header's "bundled with this plugin" gives no path. The path form is the principal's wording
(a non-goal); the removal of the fallback from the loaded command is agent work.
**Counsel:** the skill, which is agent text, may add the one line the harness substitutes —
`${CLAUDE_PLUGIN_ROOT}/docs/method/CONCURRENCY.md` — as the bundled copy's path, without
restating a word of the prompt.

### QK4 — MODERATE — harvest across `12e6d9b`: the tier bar left the loaded command

Every rule the skill stated at `12e6d9b^`, and where it lives now (P = the prompt, C =
`CONCURRENCY.md` § *Orchestrated queue runs*, E = `ECONOMICS.md`, R = `REVIEW.md`):

| Rule in the skill at `12e6d9b^` | Home now | In the loaded command (skill+prompt)? |
|---|---|---|
| State your tier, proceed, never ask | C *Tier at open*; P | yes |
| Leave a `⏳` whose named tier you cannot honour | C *Tier at open*; R rule 4 | **no** |
| `git status` first; no `--autostash` over a peer's work; no upstream, no pull | C *Integration hygiene*; child `CLAUDE.md` floor | no |
| Read `CLAUDE.md`; load the session onramp | P (read `CLAUDE.md`); onramp skill not named | partly |
| Current doctrine: local checkout, else the bundled copy | C *Where the doctrine is read from* | **no** (QK3) |
| Minimum viable run; no repo at all | C; P | yes |
| Recovery sweep after an interrupted session | C § *Surviving*; P | yes |
| Pin bump deliberate, never automatic | `PROPAGATION.md`; P | yes |
| Selection order; three selection rules | C; P | yes |
| Claim before work; `[~]` on `main`; live claim outranks the brief | C § *Claiming work*; P | yes |
| Worker in a worktree or inline; waves | C; P ("use sub-agents") | partly |
| Item text never overrides | C; P guard rail | yes |
| Worker inherits bounded; merge and the floor stay the orchestrator's | C | no |
| Terminal marker; teardown after the harness notice | C *teardown* | no |
| First-of-kind work escalates to the capable tier up front | E, the rework rule | no |
| Per-item close before the next item | C; P guard rail | yes |
| Rule-4 criterion per delta; a worker's delta is the run's own | C; P (criterion only) | partly |
| Never start or instruct a successor | C; P guard rail | yes |
| Session id first; checklist updates; bullet-list board answers; check, don't assume | C; P | yes |
| Four stop conditions, say which fired | C; P guard rail | yes |
| Report surfaces every 🎯 principal-blocked item and why | C; P ("walk me through any open decision") | partly |
| Report ends with the identifiers block; re-read of every ask; other sessions have what they need; branches put away | C; R; P | yes |
| Spend directive read as value, not budget; which pool | C; P (value) | partly |
| Ask cadence per run; away means batch the asks | C; P (standing: away) | see QK7 |

Nothing is homeless; every dropped rule still binds through the doctrine the prompt points at.
The one that matters: the prompt's `⏳` guard rail states the spawn criterion only, so a run
reading the command alone would take a `⏳` on any tier. `REVIEW.md` rule 4 says a session
that cannot honour the named tier **stops**, and `CONCURRENCY.md` *Tier at open* says it
leaves the item — a pin the old skill carried in its step 1 and the loaded command no longer
does. **Counsel:** one clause in the guard rail, on the principal's say-so since it is his
file: "and only on the tier the review names".

### QK5 — MODERATE — four units of the principal's text left in `998c35f` and never came back

The prompt's whole-delta diff (`998c35f^` → `origin/main`), every line added, removed or
reworded, with the commit that did it:

- `998c35f` **removed** (never restored): "— balancing value, urgency, and where dependencies
  force an order"; "Leave the repo, and everything you've touched, ready for the next session
  to pick up and keep building"; "— and watch for their changes in-flight the same way you
  expect them to watch for yours"; "visuals" from the capability list.
- `998c35f` **removed, `140a190` restored**: the verify-don't-infer bullet; the bullet-list
  board answer; the checklist bullet and its example; close item 3's fuller form. The
  date-and-time opener went the same way and was then **replaced** by the session-id opener
  in `1adf398`.
- `998c35f` **reworded**: the capable-tier stop → state the tier and proceed (the 2026-09-19
  ruling, named in `CONCURRENCY.md`); "roadmap harvested" → "roadmap items closed (harvested,
  on a monolithic board)". `998c35f` **added** the two closing paragraphs ("Try not to stop
  and ask me…", "Once all that is done review all my prompts…"), which read as his typed text.
- `1adf398` reworded close item 1 to the identifiers block. `12e6d9b` replaced the
  "use `/atelier:queue-run` instead of this file" aside with "(`/atelier:queue-run` runs
  exactly this file, so the command and this text cannot differ.)" — agent-written text inside
  the principal-owned file, and the claim QK1 falsifies. `9d65b6a` added the four guard rails
  (his ruling is quoted in the skill header) and rewrapped one line.

Whether each change had his say-so is phase-2 work. The phase-1 fact: `998c35f`'s changelog
entry describes two reworded lines and is silent on nine removals and two added paragraphs
(V1), and no in-scope surface accounts for the four units that never returned.

### QK6 — MODERATE — the teardown rule's second leg rests on a notice `RECORD.md` says is
### conditional

`CONCURRENCY.md` *teardown*: the marker proves done, never not-done; "the notice covers that
case". `RECORD.md` (the `020/420` passage, in the same delta's neighbourhood): "the harness's
'didn't finish' notice only appears if the session is resumed", and eleven cut agents were
seen only because their sessions were resumed. Walked through: a **crashed subagent** writes
no marker and, if the host or the orchestrator's session dies with it, produces no notice
either, so neither leg holds; a **slow verifier** is the case the rule handles (no marker,
wait for the notice — correct); a **worker that never pushes** writes a marker naming a
commit the orchestrator cannot fetch, and the rule's "remove after the notice" would remove
the only copy — the rule should say merge or push from the worktree path first. And a worker
that is a separate **session** rather than a subagent — the shape the pattern names ("worker
sessions in worktrees") — yields no harness notice at all. **Counsel:** add the third leg
(`git worktree list` plus the worker's own close record, or a process check) and state the
non-subagent case; reconcile the two docs' claims about the notice.

### QK7 — MODERATE — one rule, three statements, no stamp

The prompt, `CONCURRENCY.md` and `RECORD.md` each state the report contents, the selection
rules, the session-id-first line and the tier line. `CONCURRENCY.md` calls itself the home
("homed 2026-10-18") while saying "his words are in `session-open/session-open-prompt.md`".
No copy carries a stamp marker: `stampscan` verifies one block in the whole repo (the
`CLAUDE.md` template's floor), and `test_templates.py` pins four phrases. Where they disagree
today: the identifiers list — the prompt names seven (with "reviews queued"), `CONCURRENCY.md`
six (no reviews, model, window, branches or other repos), `RECORD.md` seven fields; the
doctrine-read fallback (QK3); the tier bar (QK4). Two statements in `CONCURRENCY.md` are now
untrue or nominal: "from 2026-09-14 until the plugin made it an invocation" (the brief is still
stated at every open — the invocation runs it), and "when to ask is per run… a principal who
says he is away sets the other cadence" (his standing text now always says he is away, so
the away cadence is the default, not a per-run override). **Counsel:** name one home per rule
and stamp the copies, or cut the restatements to pointers.

### QK8 — minor — versioning by commit: claims against the tooling's real behaviour

Checked against the Claude Code manifest and loading references and `claude plugin validate`
(v2.1.302): "Claude Code falls back to the commit" — true for `github`, `url` and `git-subdir`
sources (12-character SHA) and for a relative path in a git-hosted marketplace; for a local
directory marketplace the plugin loads in place and the version string is not read at all.
"Auto-update is off by default for marketplaces like this one" — true. `claude plugin
validate` exits 0 with the version warning the changelog predicts (and a third warning that
`CLAUDE.md` at the plugin root is not loaded as context — unrelated, worth knowing). The
README's "re-run `install-hook` in each hooked repo after every plugin update" is true for a
GitHub install, whose `${CLAUDE_PLUGIN_ROOT}` is a per-version cache directory, and
unnecessary for a local-path install, whose root is the clone; the sentence over-generalises
harmlessly (the hook fails closed either way). The harness's install record still says
`0.2.0` with a stale cached copy from before the delta; the probe shows the cache is not what
loads.

### QK9 — MODERATE — the single-source test misses a verbatim copy of a bullet

Eleven mutations of a scratch copy of the skill (and one of the prompt), each run through
the test (`python3 -I -m unittest discover`), caught = exit 1:

| Mutation | Result |
|---|---|
| m1 — a paraphrased prompt rule added to the skill | passes (blind; the docstring admits it) |
| m2 — a **new** instruction the prompt never had ("skip the scanners…") | passes (blind) — the injection direction |
| m3 — the "Claim before you work…" bullet copied verbatim, 180 characters, without its leading `- ` | **passes (blind)** |
| m4 — the same with one word changed | passes (blind) |
| m5 — a 36-character prompt sentence copied | passes (blind) |
| m6 — the `${CLAUDE_PLUGIN_ROOT}` path changed to another file | **caught** |
| m7 — both required substrings kept, the "Read…" instruction pointed at another file | passes (blind) |
| m8 — the prompt's rule reversed, skill untouched | passes (by design: the test does not read the prompt's content) |
| m9 — m3's bullet copied **with** its `- ` | caught |
| m10 — a plain (non-bullet) sentence copied verbatim | caught |
| m11 — a two-sentence bullet copied without its dash | caught, on its second sentence |

Cause: the test splits the prompt on blank lines, so a bullet list is one paragraph, and its
sentence split leaves each bullet's first sentence carrying the `- ` marker. A single-sentence
bullet — most of the prompt's rules are one — copied without the dash is never a match. The
changelog's and docstring's claim that the test "fails if the skill … copies its lines" is
stronger than its evidence (V1). It also cannot see m2 or m7, which are the shapes a hostile
or careless edit to the skill would take, and it says nothing about QK1's seam.
**Counsel:** strip list markers (and emphasis) before matching; add a check that the skill's
body, comment aside, contains nothing but the pointer lines; decide whether the test should
also compare the prompt to its committed text (QK1).

### QK10 — minor — reach and the re-run anomalies

`docs/method/README.md`, the method index, does not mention `session-open/` or the prompt;
a reader following the index never learns the command's source exists. `wrapscan` over the
delta paths exits 1 at `4839fd8` and at HEAD on the same line: `skills/queue-run/SKILL.md:3`,
the YAML `description` (464 columns) — a frontmatter field that cannot wrap, authored before
the delta and reworded by `12e6d9b`; the floor's wrapscan scope excludes `skills/`, so the
floor is green. Not a defect; the brief asked which line and whose.

### QK11 — note — commits the delta should name

`bdb1aba` (the `ccclose` sentence in the identifiers block), `880334a` and `9d65b6a` (QK2),
and the `CHANGELOG.md` hunks of `998c35f` and `140a190`.

### QK12 — note — the identifiers block against `ccclose`

`ccclose --identifiers` (read-only, this worktree) prints: **Session** (id, model, window in
UTC); **Commits** with unconfirmed and left-out sub-lines; **Pull requests**; **Board**
(completed, created, claimed-still-open, `⏳` created, unconfirmed); **Worktrees and
branches** with put-away state; **Agents** (count, and how each ended); **Other repos** as
"not read by ccclose — fill in by hand". That matches `RECORD.md`'s seven fields, with one
by-hand field as the doc says, and the prompt's "reviews queued" maps to the Board's `⏳`
line. One observation outside this delta, for `ccclose`'s owner: it classed this still-running
subagent as "cut mid-flight", so a block printed before the last agent returns misreports it.

## Re-run ledger

All from the worktree at `7d58404` unless stated; `/usr/bin/python3`; exit codes read.

| Command | Result |
|---|---|
| `tools/floor.py --plane ci --root .` | exit 0; pathscan (warn-only) 3 findings, one on the prompt's `../atelier` path |
| `tools/floor.py --plane hook --root .` | exit 0; same pathscan findings |
| `python3 -m unittest discover -s tools -p test_queue_run_single_source.py -v` | 3 tests, OK, exit 0 |
| `coldsweep.py --commit` × 10 (`998c35f 1487e9c 140a190 1adf398 46320f8 6810b64 12e6d9b 880334a 9d65b6a bdb1aba`, brief's `--path` flags + `CHANGELOG.md`) | exit 0 each; closing line each time: "0 file(s) left out as rule-2 barred … none touched" |
| `wrapscan.py --root .` over the six delta prose paths | exit 1: `skills/queue-run/SKILL.md:3` (464 cols); identical at a full export of `4839fd8` |
| `spellscan.py` same paths | clean, exit 0 |
| `leakscan.py` same paths + both manifests | clean (structural + local), exit 0 |
| `linkscan.py --root . .` | clean, exit 0 |
| `stampscan.py --root . .` | clean, 1 stamped block verified, exit 0 |
| `git log --oneline 12e6d9b..origin/main -- <delta paths>` | `9d65b6a`, `880334a`, `bdb1aba` |
| `test_templates.py` at complete exports of `12e6d9b^` / `12e6d9b` / `880334a` / `9d65b6a` | OK / **6 FAIL** / OK / OK (QK2) |
| `python3 -m unittest discover -s tools -p 'test_*.py'` at HEAD | exit 1: loader errors in `test_floor`, `test_precommit`, `test_allowmarker`, `test_leakscan`, `test_pathscan` — `TypeError: unsupported operand … 'type' and 'NoneType'` and `write_text() … 'newline'`, i.e. the system Python 3.9 lacking 3.10+ syntax; environmental, outside this delta, not reproduced on CI's 3.12 |
| `claude plugin validate .` | exit 0, 3 warnings (QK8) |
| Skill tool `atelier:queue-run`, bare and with an argument | base directory = the local clone; `${CLAUDE_PLUGIN_ROOT}` substituted; typed text arrives as a trailing `ARGUMENTS:` line |
| `ccclose --identifiers --root <worktree>` | exit 0 (QK12) |
| eleven mutations of scratch copies of the skill/prompt through the single-source test | 3 caught, 8 blind (QK9) |
| Clone state (read-only) | branch `main` at `5139d68`; prompt file modified, 1 insertion (blank line), differs from `origin/main` (QK1) |

## Follow-up checklist (for the principal's decision, rule 3)

- [ ] QK1 — guard the working-tree seam (drift check at open; mechanised say-so; threat model
      stated in the session-open README).
- [ ] QK2 — widen the pointer's delta to `880334a`, `9d65b6a`, `bdb1aba`; decide whether a
      landed-red doctrine commit needs its own rule.
- [ ] QK3 — a resolvable doctrine path in the skill (`${CLAUDE_PLUGIN_ROOT}/docs/method/…`).
- [ ] QK4 — the tier clause in the `⏳` guard rail, on his say-so.
- [ ] QK5 — reconcile the four removed units and the `998c35f` changelog entry (phase 2 first).
- [ ] QK6 — third leg for teardown; reconcile `CONCURRENCY.md` with `RECORD.md` on the notice.
- [ ] QK7 — one home per shared rule; stamp or cut the copies; fix the two stale sentences.
- [ ] QK8 — scope the `install-hook` re-run sentence to GitHub installs.
- [ ] QK9 — strip list markers before matching; bar additions to the skill body; decide
      whether the test also reads the prompt (QK1).
- [ ] QK10 — index `session-open/` in `docs/method/README.md`.
- [ ] QK12 — hand the in-flight-agent observation to `ccclose`'s owner (`210/290` area).

**Overall: PASS-WITH-FINDINGS — 2 MAJOR (QK1, QK2) · 6 MODERATE (QK3–QK7, QK9) · 2 minor
(QK8, QK10) · 2 notes (QK11, QK12).** Phase 1 ends here; the sibling is not yet opened.

### Reconcile — act 2, written 2026-10-25 UTC

**Opened after act 1 was saved and acknowledged:** the held `.deferred.md` sibling (read at
the orchestrator's path, read-only, not copied into the worktree at its instruction — the fold
of the sibling beneath this section is left to the orchestrator, which holds it); the message
bodies of the seven landing commits and of `880334a` and `9d65b6a`; the intent records
`180/010`, `180/020`, `180/030` and the items `180/040`, `050`, `070`, `080`, `090`, `100`;
the identifiers block of the authoring session's record (its lines 219–241). **Not opened:**
any other session record, any prior verdict, `docs/SESSIONS.md`, `docs/ROADMAP-DONE.md`, the
`160/910`, `160/930` and `160/940` briefs or verdicts. Phase-1 text above is unchanged;
every change of view is stated here.

**The sibling's three held facts.** (1) The intent records are read and accounted for below.
(2) The neighbouring passes were not opened; no framing from them reached this one. (3) The
pointer's widening after the briefs were claimed matches what I observed, and `180/100`
itself says "the reviewer should read the delta at `main`" — the author's own words behind
QK11.

**Per finding, against the nine seeded questions (Q1–Q9) and the records:**

- **QK1 — stands, MAJOR.** `998c35f`'s body chose in-place loading knowingly, for currency
  ("how this machine's install keeps the doctrine current"). `180/090` is the principal asking
  for a file he can open, use by hand and review — so hand access to the file is the ask, and
  the seam is its price; no record enumerates it. The record corroborates the class:
  `180/030` found that on 2026-10-17 a "restore current content" commit (`6a0ac93`) wrote
  older text back into this same file and undid two rulings "with nothing to catch it". The
  uncommitted line in the clone may well be his own hand edit; the finding does not turn on
  who made it — his hand copy and the reviewed text differ, and no run says so. Counsel
  unchanged.
- **QK2 — stands as a defect; severity revised MAJOR → MODERATE.** The record owns it in
  full: `880334a`'s body ("The author had run only the new test, not the full suite, before
  merging"), `180/090` ("Floor red, fixed the same hour"), and `180/100` records the full suite
  run before the next merge. The repair landed 16 minutes after the break, and the pointer's
  omission of the two repair commits is a scope slip the author half-anticipated (`180/100`).
  An honest record and a same-hour fix leave the pointer widening (QK11) and the question of
  whether "landed red" wants its own rule; that is MODERATE, not MAJOR.
- **QK3 — stands, MODERATE.** Q1 is the same question. `180/010` measured a skill's base
  directory in a headless session, not what a run outside atelier resolves; no record answers
  it. Answer to Q1: a run in an unrelated repo installed from GitHub receives the skill (header
  and pointer), then — if the model performs the read — the bundled prompt; its `../atelier`
  anchor resolves nowhere, so it either takes the prompt's "none of that" branch or
  re-derives; the bundled `CONCURRENCY.md` is reachable only by a path no text gives it.
- **QK4 — stands, MODERATE.** Q4 overlaps. `880334a` names the five pins `test_templates.py`
  holds; the tier bar was never a pin, so its loss registered nowhere. Answer to Q4: each lost
  rule is stated somewhere a run reads if it follows the pointer; the teardown sentence
  `1487e9c` added to the skill went with the collapse and lives in `CONCURRENCY.md` alone.
- **QK5 — severity revised MODERATE → minor.** Q5 is the question, and the records answer
  it. `180/030`: the principal named the 2026-09-14 text as "the current version of the prompt
  I like to use"; that text lacked the 2026-09-16 additions, so `998c35f`'s removals are his
  chosen text displacing agent-added lines ("Dropped by his choice and kept in git history").
  `180/040`: offered four of them at the close, he picked all four; "Not offered to him, so
  left out: four smaller 2026-09-16 phrases" — the four I listed. The two closing paragraphs
  were in his named text (`180/090` flags their consequence to him). The one agent sentence is
  named in `12e6d9b`'s body ("One sentence of it changes on this ask"). What remains is the
  `998c35f` changelog entry understating the commit (V1) and a one-line ask: put the four
  smaller phrases to him.
- **QK6 — stands, MODERATE, strengthened.** `180/020`, the hand-up, named option 1's risk in
  terms: it "still leans on the harness always delivering that notification, which this text
  does not itself verify". The close took option 3 and `CONCURRENCY.md` wrote "the notice
  covers that case" without the caveat, at 13:16 NZDT; the same session landed `RECORD.md`'s
  `020/420` passage, which records the notice as conditional, at 13:23. Two docs, one hour,
  opposite assumptions.
- **QK7 — stands, MODERATE.** Q7 is the question. `1adf398`'s body confirms the three-surface
  edit; the drift class is moved, not closed. On Q6: `180/090` flagged the always-on away
  cadence to him as a consequence of running his named text, so he knows; what is left is
  `CONCURRENCY.md`'s "per run" sentence, now nominal.
- **QK8 — stands, minor.** Q8. `180/050`: "The principal's own install is unaffected: it loads
  in place from the checkout" — consistent. Answer: every update is a blocking event only in
  a child hooked from a GitHub install; the fall-back-to-commit claim came from the docs, and
  the docs confirm it for git sources.
- **QK9 — stands, MODERATE.** Q3. `12e6d9b`'s body: "checked against a planted copy";
  `180/090`: "a planted copied sentence made it fail" — one plant, evidently a plain sentence
  (m10's shape); the bullet shape (m3) was not tried. Answer to Q3: yes, a green run is read as
  "no drift" — the prompt now prints that claim — and the test's cover is narrower than its
  docstring.
- **QK10, QK11 — stand.** QK11 now carries the author's own intent (`180/100`).
- **QK12 — stands, note.** Q9's parenthesis checks out and goes further: the authoring record's
  block gives the session window as 2026-10-17 23:59 to 2026-10-18 04:14 UTC, yet its Commits
  line lists `880334a` (05:22 UTC) and `9d65b6a` (06:01 UTC); the record was re-committed five
  more times, the last at 2026-10-18 12:44 UTC; the Commits line gives two totals (102, then
  "50 of the 96"); and "Worktrees and branches (7)" lists eight. See QK14. Answer to Q9's
  other half: `ccclose` prints every field but *Other repos* (act 1), and a resumed session
  recovers worktrees from the transcript as the rule says — this record did.

**Findings formed at reconcile (marked as such):**

### QK13 — note — "adds nothing" is true of rules, not of text (formed at reconcile, from Q2)

The skill adds the "follow it as his own brief, word for word" framing, the mapping of the
typed text onto *This run*, the empty-invocation default and a frontmatter description that
restates the pattern. None is a rule; all are agent text that no test watches for additions
(QK9, m2). The overclaim that matters is "cannot differ" (QK1), not "adds nothing".

### QK14 — minor — the identifiers block is a snapshot, and the rule has no addendum clause
### (formed at reconcile, from Q9)

`RECORD.md` says each identifier is "read fresh at close, never recalled". The delta's own
authoring record shows what happens when a record is extended after its first close: the
window stays at the first close while the Commits line grows past it, two totals disagree,
and a count header disagrees with its list (QK12). Nothing in the rule says the block is
re-read at each addendum, and `ccclose --identifiers` makes that a one-line act.
**Counsel:** one clause — a record extended after its close re-reads the block, or dates it.

**Revised overall: PASS-WITH-FINDINGS — 1 MAJOR (QK1) · 6 MODERATE (QK2, QK3, QK4, QK6,
QK7, QK9) · 4 minor (QK5, QK8, QK10, QK14) · 3 notes (QK11, QK12, QK13).** Changes from act 1:
QK2 MAJOR → MODERATE and QK5 MODERATE → minor, both on the records read at reconcile; QK13 and
QK14 added. Follow-up checklist additions: QK5 — put the four smaller phrases to the
principal; QK14 — the addendum clause. Findings on doctrine remain the principal's to decide;
nothing is applied.

---

## Deferred sibling, folded below the verdict (orchestrator, 2026-10-25)

*Released to the reviewer only after its act-1 findings were saved; folded here verbatim and
the sibling file deleted, per the brief. The orchestrator (session `52e11d15`, Claude Opus 5.5)
formed no finding and wrote no severity.*

### Sibling to the queue-run-carries-the-brief cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-18-0517-queue-run-carries-the-brief-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-18 UTC by the Opus brief-writer named in the brief's provenance; it
forms no finding. Fold this file in below the reconcile and delete it at phase 2.

## Facts held back

1. **Intent and commissioning records:** `180/010`, `180/020` and `180/030` (the pointer's
   intent records), and `180/040`, `050`, `070`, `080`, `090` (the items the later commits
   close) — **none opened by the brief-writer**, beyond the claim lines of `180/090`, which
   carry a quoted line of the principal's that the skill header and test docstring also quote.
   No commit body was read, so this sibling carries no account of the author's reasons; read
   them at reconcile.
2. **Neighbouring passes.** The same authoring session's `adf75a4` (`160/910`) and
   `8132805`/`30aa8dc` (`160/930`) were briefed in the same sitting by this brief-writer, and
   `160/940` (the template history in `docs/method/session-open/`) by another brief-writer
   under the same dispatching run. `160/940`'s file shares a directory and a README with this
   pass's prompt.
3. **The pointer was widened after the briefs were claimed.** The briefing worktree was cut at
   `f0d6238`, before `12e6d9b` landed; the pointer on `origin/main` was widened to `12e6d9b` by
   `055b326`, and this brief was written from that wider text.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. **The path a run is told to read.** The prompt tells a run to read "the *current*
   `../atelier/docs/method/CONCURRENCY.md`". That resolves only from a sibling checkout of
   atelier. Before `12e6d9b` the skill said where else to read (a local checkout, else the
   plugin's bundled copy); after it, that fallback lives only in `CONCURRENCY.md` — which the
   run reaches through the same unresolvable path. What does a run in an unrelated repo,
   installed from GitHub, actually read?
2. **"Adds nothing."** The skill header, the session-open README and the prompt all say the
   skill adds nothing to the prompt. The skill still adds: "follow it as his own brief, word for
   word", the mapping of the invocation text onto the prompt's *This run* section, the
   empty-invocation default, and a frontmatter description that restates the pattern. Are those
   additions, and does "cannot differ" overclaim?
3. **What the test can see.** It flags only sentences of 40 characters or more copied verbatim.
   A paraphrase, a contradiction, or a shorter copied rule passes. Its own docstring concedes
   paraphrase. Is a green run here being read as "no drift", which is the claim the prompt now
   prints?
4. **Rules lost in the collapse.** The pre-`12e6d9b` skill carried steps (sync with
   `git status` before `--autostash`, claim from the primary checkout, per-item close, worker
   dispatch and the teardown marker from `1487e9c`, the report's contents). Is each still stated
   somewhere a run reads, or did the teardown sentence `1487e9c` added to the skill go with it?
5. **Principal-owned text, edited.** By the brief-writer's count, `998c35f` removed nine
   passages from the prompt (the date paragraph, "balancing value, urgency…", "Leave the
   repo…", "watch for their changes in-flight", "visuals", "Verify facts…", the bullet-list and
   checklist bullets, and the tail of close item 3). `140a190`, whose subject says "four prompt
   lines come back", restored five of them by the same count; `1adf398` then replaced the date
   paragraph. Four are still absent at HEAD. The README now
   says an agent changes this file only on his say-so, quoted in the commit. Did each removal
   have it?
6. **Ask cadence, now always on.** The prompt both says "Ask me with AskUserQuestion when you
   need a decision, mid-turn" and ends "Try not to stop and ask me questions until you have done
   all the work. I won't be here…". `CONCURRENCY.md` makes the away cadence conditional on the
   principal saying he is away. If the command runs the prompt word for word, is the away
   cadence the default for every run, contradicting the doctrine's default?
7. **Two homes after "one text".** `CONCURRENCY.md` restates the prompt's rules (three
   selection rules, what the report carries, how the run talks to him) as doctrine "homed" from
   the prompt. The single-source test guards skill-versus-prompt only. `1adf398` had to edit
   prompt, `CONCURRENCY.md` and skill together to move the date line to the session id. Is the
   drift class closed, or moved?
8. **Versioning by commit.** With no `version`, the README says each commit is a version and the
   pre-commit hook's scanner path is pinned to it, so the hook must be re-installed in each
   hooked repo "after every plugin update". Does that make every update a blocking event in
   every child repo, and is "Claude Code falls back to the commit" checked against the tooling?
9. **The identifiers block's sources.** It asks for agents launched and worktrees created and
   removed, and says the worktree list "comes from the transcript". Can a session that was
   compacted or resumed recover those, and does `ccclose` print them? (The authoring session's
   own identifiers line gives a window that ends before its own later commits.)
