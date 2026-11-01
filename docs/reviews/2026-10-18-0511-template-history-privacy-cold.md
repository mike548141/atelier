# Cold pass — the opening prompt's template history, for privacy and specific work

**Pass type:** records and privacy cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** REVIEW RUN, both phases — act 1 (the verdict) and act 2 (`### Reconcile`)
are appended below the divider, written 2026-11-01 UTC by a cold Fable 5.1 reviewer;
the deferred sibling is folded in verbatim below the reconcile.
Brief written 2026-10-18 UTC by an Opus brief-writer; the pass waited for a further cold
Fable session that neither the delta's author nor this brief-writer (nor its
orchestrator) started or instructed.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/940-cold-pass-queued-template-history-privacy.md`.
**Why it earns a review:** text mined from the principal's private session transcripts
was published in this PUBLIC repo, as 50 commits already pushed to `main`. The only
check so far is the session that landed it. The worst failure is private detail, or one
session's specific work, sitting in a published version: git history is public the
moment it is pushed, and taking it back means rewriting public history, which is the
principal's call and not reversible for anyone who has already cloned.

## Spawn provenance

- **Author of the work under review:** a Mike-opened Opus 5.5 queue run, 2026-10-18,
  which dispatched the worker that did the mining; the pointer counts the worker's
  output as the run's authorship. Not opened here beyond the pointer and the intent
  record.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched on
  2026-10-18 by a different Mike-opened Opus 5.5 queue run (worktree
  `atelier-qr-briefs-1018`), which authored none of this delta. This brief-writer
  authored none of it either. It is **off-tier for review, disclosed: it forms no
  finding and writes no severity**, and it stops after this brief, its sibling, and
  one other brief pair (160/920).
- ⚠️ **Channel contact, disclosed by the orchestrator** (roadmap `280/040`). The
  dispatching run was started by the principal directly; the authoring session neither
  started nor instructed it. While this brief was being written, the authoring session
  (one session throughout, `e1d4097c`) sent that run's orchestrator one cross-session
  file-set notice: `ccclose` had changed under a parallel worker, rebase before merging,
  and which commits had landed and widened two pointers. It carried no view of any
  delta. The orchestrator also read the close section of the authoring session's record
  and, before landing it, this brief and its sibling. Weigh that as you see fit.
- **Who takes the review:** a further cold Fable session, not yet started, that passes
  rule 4's criterion. If it runs as reviewer-plus-orchestrator, rule 4's off-tier
  conditions apply and are disclosed in the claim, the pointer and the verdict. The
  reviewer repeats its own provenance in its verdict.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This brief-writer
  read: its dispatch prompt and one mid-task message from its orchestrator (about the
  other pointer); `skills/review-brief/SKILL.md`; `docs/method/REVIEW.md` lines
  55–234; the queue pointers 160/940 and 160/920 in full, 160/780 in full and the
  heads of 160/870 and 160/900; an earlier brief pair for shape
  (`docs/reviews/2026-10-17-1010-ccclose-close-checker-cold.md`, its brief section,
  folded sibling and heading outline). Of this delta: `docs/method/session-open/README.md`
  whole at HEAD and the `.spellscanignore` entry; commit subjects, stats and committer
  dates. **It read the intent record in full**, including the author's account below
  the principal's words (held in the sibling). **It did not open
  `template-history.md` at any version** and read no version commit's message body:
  it wrote each version and the delta's messages to files in its scratchpad, ran the
  scanners in *Re-run obligation* over them for exit status, and saw only rule names
  and counts from one of them (held in the sibling). It did not open
  `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, any prior verdict, or
  any transcript. Its harness also loaded the user-level and repo instruction files and
  a memory index, which hold private context this brief does not carry. What its
  orchestrator read is the orchestrator's to disclose; it passed on the pointer, a
  prefix suggestion, the pointer-append shape and the instruction that this brief point
  at the principal's exclusions and quote no version, and no evaluative content.

## The acceptance test: the principal's own words

The pass is judged against the principal's two exclusions and his definition of
"template", quoted verbatim in the intent record. Read **only** those lines, before
phase 1, with:

```
git show ec37c6b:docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/060-the-opening-prompt-template-history-from-the-transcripts.md | sed -n '3,13p'
```

That prints his quoted words and nothing else. The rest of that item (from line 14) is
the author's account of how the work was done and is barred until phase 2. The
delta's README quotes part of the same words; where the two differ, his words in the
intent record govern. Apply them as the test, and also the repo's purpose-based
personal-data rule (`docs/build/REPO-STANDARD.md`) and atelier's own hard constraint
on personal data (`CLAUDE.md`), which bind this public repo regardless.

## What the work is

All landed on `main` on 2026-10-18, every commit's committer date 04:14 UTC:

- `7033378` — session-open: say how the template history is built, before it lands
  (180/060). `docs/method/session-open/README.md` (the method section) and
  `.spellscanignore` (one path exempted).
- `1241b8c` … `e6c1137` — 50 commits, `session-open template: version N of 50, first
  used <date>`, one per version of `docs/method/session-open/template-history.md`,
  oldest first. Each commit's **author date is set to the version's first use**, so
  author and committer dates differ by design.
- `ec37c6b` — board: close 180/060; queue its privacy cold pass. Only its one-line
  hunk on `docs/method/session-open/README.md` is this delta.

Read every version, with subjects and dates but no bodies, by:

```
git log --follow --reverse -p --format='%h %ad %s' --date=iso-strict -- docs/method/session-open/template-history.md
```

**The 50 version commits' message bodies are published text and part of the privacy
surface** (the README says each gives how many sessions used the version). Read them
in phase 1, as subject matter to screen, not as an account to believe. The bodies of
`7033378` and `ec37c6b` are the author's account and are barred until phase 2; screen
them for privacy then, and mark any finding formed there as formed at reconcile. Read
those two commits body-free with `python3 tools/coldsweep.py --root . --commit <sha>`;
plain `git show` prints the body before the diff, and reading is atomic (rule 1).

## Scope

Widest the work admits. The lenses organise it; they do not bound it. Probe, at least:

- **Exclusion 1, every version.** Each of the 50 texts, read whole, for private or
  personal information, by meaning and not by keyword: anything that names or lets a
  reader infer a private repo, tool, device, place, person, account, credential store,
  client or the principal's circumstances. Inference across versions counts: a diff
  between two versions shows what changed, and a placeholder's surrounding frame can
  identify what it replaced.
- **Exclusion 2, every version.** Any unit that is one session's specific work rather
  than reusable template — a named task, feature, board item, run theme or deadline —
  against his definition (re-used across more than one session).
- **Metadata.** Author dates, committer identity and the bodies' usage counts are
  published too. Weigh what the timeline and counts disclose against his stated aim of
  seeing the prompt change over time.
- **The README's method section.** It describes what was taken out. Test whether the
  description itself says more than a public reader needs, and whether its factual
  claims (counts, what was dropped, what scanners passed) hold where they can be
  re-driven.
- **The `.spellscanignore` entry.** Its scope (one path), and the ruling it cites as
  authority: find that ruling in the record and say whether it covers newly mined text.
- **Reach.** Where else these versions now exist (the remote's history, any branch or
  PR that carried them), so that any remediation the principal chooses is scoped.

**Non-goals:** the principal's decision to publish the template history in atelier,
and the mining method's design, except where either produced a leak. The current
prompt file `docs/method/session-open/session-open-prompt.md` and its own history are
not this delta; if you meet a privacy problem there, record it as a note against that
out-of-delta surface rather than leave it unsaid.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Among them: that recurrence across two sessions is a sufficient filter for "not one
   session's work"; that a scanner pass plus one session's read is enough to publish
   private-source text; that a placeholder removes what it replaces.
2. **Correctness & quality.** Do the 50 versions match what the README says they are
   (order, dates, one per version, re-pastes not repeated)? Is anything overclaimed?
3. **Completeness / harvest.** Every version read whole, not sampled; every body;
   every metadata field; the README; the ignore entry. Say how many you read.
4. **Security & privacy** — the lens this pass exists for. Secrets, tokens, email
   addresses, phone numbers, hostnames, paths with an account name, and personal or
   estate detail, in text and in metadata. `/security-review` cannot reach this delta
   (landed markdown and commit metadata, which its exclusions bar): one line saying so
   with grounds, and the read done by hand.

## Re-run obligation

Re-run, do not read. Each line below was run once by the brief-writer from its worktree
root and ran; its results are held in the sibling, not offered here.

- every version through the scanners: write each version to its own file in your
  scratchpad (`git show <sha>:docs/method/session-open/template-history.md`, for each
  sha from `git log --follow --reverse --format=%h -- <that path>`), then
  `python3 tools/leakscan.py --require-terms --root <dir> <dir>`,
  `python3 tools/secretscan.py --root <dir> <dir>` and
  `python3 tools/datescan.py --root <dir> <dir>`
- every message of the delta through the same leak and secret scanners:
  `git log --format='%H%n%B' 7033378^..ec37c6b` to one scratch file, scanned the same
  way — after phase 1 for the two barred bodies, or scan only the 50 version commits'
  messages in phase 1
- `--require-terms` exits 2 where no local term list is installed (a cloud session):
  then run without it and say the cover was structural only — a degraded pass is not a
  full one
- the recurrence test, where you can reach the principal's transcript store on his
  machine: by path (`instruments/cctranscript`), read-only, aggregate counts only;
  never quote transcript text into the verdict. From a session without the store,
  state the impossibility with its grounds.
- the floor at HEAD (`python3 tools/floor.py --plane ci --root .`)

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only git is
  fine. Extracted versions, message files and probes go under your session scratchpad,
  named by your prefix, and are deleted when you finish.
- One heavy process at a time on a shared machine; check `uptime` first. Never point a
  scanner at any other repo on the machine. Never run an installed tool by bare name
  from `PATH`.
- **Quote nothing you judge private, and nothing from any version beyond what a
  finding needs to be located.** Locate by commit and line ("version 23, line 14"),
  describe by class ("a device name"), and never restate the private detail itself,
  in the verdict, a commit message, the pointer or a session log. This repo is PUBLIC:
  a finding that repeats the leak is a second leak.
- Apply nothing. Rewriting or reverting published history is irreversible and the
  principal's call; record each finding with its location and a counselled remedy.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ English.
- Review deep, not fast: a finding needs a probe or a located instance behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer, this
brief's sibling `docs/reviews/2026-10-18-0511-template-history-privacy-cold.deferred.md`,
the bodies of `7033378` and `ec37c6b`, and the intent record beyond lines 3–13:

- `docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/060-the-opening-prompt-template-history-from-the-transcripts.md`

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/940-cold-pass-queued-template-history-privacy.md
--also-exclude docs/reviews/2026-10-18-0511-template-history-privacy-cold.deferred.md
--also-exclude
docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/060-the-opening-prompt-template-history-from-the-transcripts.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is
never barred; the README and every version are the delta.

## Process

**Phase 1.** Read the acceptance test; reproduce the floor; work the lenses and the
re-run list. Then append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, what you read), per-lens answers, the
standing checklist V1–V7 each answered or discharged with grounds, a per-version
ledger (version, sha, read whole yes/no, exclusion 1 and exclusion 2 each clear or a
finding id), findings with stable IDs (prefix `TH`: `TH1`, `TH2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line
with counts, a re-run ledger, and a follow-up checklist. Then STOP and commit phase 1
unrevised before opening the sibling. Edit no other file.

**Phase 2.** Open the sibling and the rest of the intent record; screen the two barred
bodies; append `### Reconcile` beneath your verdict: per-finding notes against the
seeded questions and the author's account, any finding formed at reconcile marked as
such, and the overall line restated. Never revise phase-1 text. Then fold the sibling
in below the reconcile and delete it.

Every finding is the principal's to decide: record all, apply nothing; counsel per
finding is welcome, labelled and kept beneath it.

---

# Verdict — phase 1 (cold pass, 2026-11-01)

**Overall: PASS-WITH-FINDINGS** — 0 MAJOR · 0 MODERATE · 4 minor · 2 notes. On the
acceptance test itself (the principal's two exclusions and his definition of template)
every one of the 50 versions, every version commit's message and every metadata field
is **clear of private or personal information and of one session's specific work**.
The findings are about the record that frames the versions (dates, counts, a scanner
exemption's authority) and one version whose recurrence could not be reproduced.

## Provenance (V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), tier checked at selection by the
  orchestrator. Worktree `atelier-160-940-1158`, detached at `3148ea4` (the board claim).
  No git command that writes was run; read-only git only.
- **Spawned by** session `5b6884f2`, a headless Opus 5.5 orchestrator, itself started by
  session `c87c4ee0` (Opus 5.5). Both are rule-4 off-tier orchestrators holding the context
  partition: they formed no finding and wrote no severity. Neither authored the delta or
  the brief. The reviewer was not started or instructed by any barred party: not the
  delta's authoring session (`e1d4097c`), not the Mike-opened queue run that dispatched
  the mining worker, not the brief-writer, not the brief-writer's orchestrator (the queue
  run in worktree `atelier-qr-briefs-1018`). Runs under the principal's drain approval of
  2026-11-02 for Fable cold reviews.
- **Partition, as run:** the orchestrator removed the sibling `.deferred.md` from the
  worktree before the reviewer started (that is the `D` in `git status`). The reviewer did
  not look for it: no `git show`, `git log -p` or `cat-file` touched its path, and every
  history command was scoped to the delta's paths. The orchestrator read the brief and the
  board item `160/940` to check barring; it did not open any version, the sibling, or any
  prior verdict.
- **What the reviewer read (rule-2 exposure, disclosed):** this brief; `REVIEW.md`
  lines 25–120 and 229–447; lines 3–13 only of the intent record at `ec37c6b` (the
  acceptance test); `docs/method/session-open/README.md` at HEAD; `.spellscanignore`;
  `7033378`, `ec37c6b` and the later `12e6d9b` body-free through `coldsweep --commit`,
  scoped to the delta's paths; all 50 versions whole, extracted to scratch; all 50 version
  commits' messages (subjects and bodies); `REPO-STANDARD.md` lines 168–193;
  `instruments/README.md` lines 21–75 and `cctranscript --help`; `.atelier-floor.json`
  lines 1–30; `tools/README.md` lines 1090–1100; coldsweep hits (non-barred paths) for
  the placeholder term and the 2026-07-23 ruling. Not opened: `docs/SESSIONS.md`,
  `docs/sessions/`, `docs/ROADMAP-DONE.md`, any prior verdict, the queue pointer, the
  sibling, the two barred bodies, the intent record beyond line 13, any transcript's
  text. The harness loaded the user-level and repo instruction files and a memory index,
  which carry private context this verdict does not use. The current prompt file
  `session-open-prompt.md` was compared to version 50 by line count only (it is out of
  delta) and not read.
- **Recurrence test:** RAN, on the live transcript store only, through
  `instruments/cctranscript` by path, read-only, `--list --all --json` and one
  `--json --utc` render per precursor session; only counts, booleans and timestamps left
  the scratch files, and the files were deleted at the end of act 1. The `ccarchive`
  mirror lists 1064 sessions, every one iCloud-evicted; it was not materialised (that is a
  bulk download, and the run was no-network), so the archive half of the author's source
  set was out of reach. All figures below from the store are therefore a lower bound.

## Lens 1 — approach and assumptions, named by the reviewer

The load-bearing assumptions, as the reviewer sees them, and how each held up:

1. **Unit-level recurrence is a sufficient filter for "not one session's work".** False
   on its own, and the author knew it: the README's own account says nine units recurred
   yet named one session's work, and were removed by hand. So the real filter is
   recurrence *plus* one session's judgement. The reviewer re-read all 50 versions for
   residue of that judgement and found none (lens 4). The assumption is discharged by the
   hand pass, not by the rule.
2. **A scanner pass plus one session's read is enough to publish private-source text.**
   Not sufficient in principle (the scanners match patterns; private meaning is not a
   pattern), which is why this pass exists. In practice, the versions' private surface is
   small: the prompt is instructions to an agent, not an account of the estate. Held.
3. **A placeholder removes what it replaced.** Held here: the one placeholder
   (`[estate-root repo]`, versions 5–7, 9, 10) names a role, not a repo, and atelier's
   public doctrine already names that role in the same words (`PROPAGATION.md` lines
   250–253, `AUTONOMY.md` line 56, `ECONOMICS.md` line 179, `build/templates/CLAUDE.md`
   line 103). The frame around it says only that a parent repo exists. Nothing new is
   disclosed.
4. **Unspoken: the principal's "parts … re-used across more than one session" is read
   at unit level, so a *version* may itself have opened one session.** That reading is
   defensible and the README states the rule, but it does not say the consequence: 17 of
   the 50 versions opened one session and were never re-pasted (TH6). Where one version
   differs from its neighbour by a dropped horizontal rule (47 → 48), the "version" is a
   one-off assembly of recurring parts. Not a privacy matter; a definition one.
5. **Unspoken: the brief's account of what the work is.** Checked and holds: 50 version
   commits, one per version, oldest first, author dates monotonic, committer dates all
   2026-10-18T04:14Z, all authored and committed as the declared identity with the
   Opus co-author trailer. Two framing commits as described.

## Lens 2 — correctness and quality

- **Order, dates, one per version, re-pastes not repeated:** holds. No two versions are
  byte-identical (md5 over 50 files: 0 duplicates). Every consecutive pair differs. No
  line exceeds 80 columns, so the rewrap claim holds.
- **Author date = first use:** holds for versions 5–50 (UTC, to the second). Does **not**
  hold for versions 1–4 (TH1): their author dates carry the message's UTC wall-clock
  digits with a `+12:00` offset and zeroed seconds, so as instants they are twelve hours
  early. The store confirms the message lines, not the author dates.
- **Counts:** the four precursor counts (4, 2, 10, 9) match the README's "two to ten";
  the live store finds 4, 2, 9, 8 sessions whose whole prompt equals each precursor
  (one session short on each of versions 3 and 4, consistent with the archive holding
  what the live logs no longer do). The README's family of 228 does not equal the sum of
  the 50 messages' counts, which is 142 first-run plus 84 re-pasted = 226 (TH2).
- **Scanner claims re-driven:** reproduced exactly (re-run ledger).
- **Overclaim check on the README:** "every landed version passed the … spelling
  scanner[s], with one exception" is literally true but the exception is *enforced* by a
  path-wide ignore, not by a one-line allowance (TH4). "What was taken out" describes
  the removals without saying that they leave no mark in the text (TH5).

## Lens 3 — completeness and harvest

Read whole: **50 of 50 versions** (2100 lines in all), **50 of 50 version messages**
(subjects and bodies; the bodies are one template with two varying figures), every
metadata field (author name, email, author date, committer name, email, date, co-author
trailer), the README at the delta and at HEAD, the `.spellscanignore` entry and its
header comment. The two framing commits were read body-free; their bodies wait for
phase 2. The reviewer also diffed every consecutive pair of versions (sizes only, then
the text) to test inference across versions: a diff shows wording the principal changed
and nothing a placeholder hid.

What the work ignored or duplicated: nothing found. The README is the only prose home of
the method and it points at `180/060`.

## Lens 4 — security and privacy (V6)

- **`/security-review`: NOT RUN, discharged.** It reads a session's pending diff and
  excludes markdown; this delta is landed markdown plus commit metadata, so its clean
  pass would be definitionally empty. It was also unsafe to run here: the worktree's only
  pending change is the deliberately removed sibling, which a pending-diff scanner would
  have fed back into the reviewer pre-draft (the SL2 case in `REVIEW.md`).
- **Hand read, by meaning, every version.** Classes looked for: secrets, tokens, email
  addresses, phone numbers, hostnames, paths carrying an account name, device names, the
  names of private repos, tools, places, people, clients, credential stores, and the
  principal's circumstances. **Found: none.** What the versions do carry, each judged
  public-grade: this repo's name; a public instrument's name (`cctranscript`, versions
  36–50); Anthropic model names and the fact of a subscription plan with session limits
  (versions 24–39); a harness environment variable and tool name (versions 40–50); a
  relative path into this repo (versions 45–50); and the placeholder discussed under
  lens 1. One sentence about the principal's availability (versions 49–50) states no
  place, time or reason and is his own template text.
- **Exclusion 2, by meaning.** No version names a task, feature, board item, run theme
  or deadline. The frames that once introduced such lists survive (versions 17–18 lines
  12–14 end at a colon; versions 20–23 say "below" of a list that is not there; versions
  25, 26, 41, 42 keep a "start with work that: (a) …" clause whose text is generic).
  Each such frame recurs in two or more sessions on the live store, so each is template
  by his definition. See TH5 for the dangling colon.
- **Metadata.** The identity is the repo's one declared exception. The author dates give
  the principal's first use of each version to the second, and the messages give per-run
  session counts: together a map of working hours and volume over three months. The
  reviewer weighed this against his stated aim (seeing the prompt change over time, which
  day-level dates would serve) and against what the repo already publishes (thousands of
  commits with the same timestamps, and the README's own 946-session figure), and judged
  it discloses nothing new in class. Recorded as a note under TH1's counsel, not a
  finding.
- **Messages.** Clean. The co-author trailer's address is Anthropic's published
  no-reply address, present on every commit in this repo.
- **Reach.** The 50 commits are on `origin/main` and, at HEAD, on 6 local and 8 remote
  branches that descend from the landing (`git for-each-ref --contains ec37c6b`). Pull
  requests were not listed (no network). Any remediation the principal chooses has to
  cover every branch and the remote; clones and forks beyond it are out of anyone's
  reach, which is the brief's own warning.
- **Out-of-delta note.** `session-open-prompt.md` at HEAD was not read; nothing to
  report there.

## The `.spellscanignore` entry

Scope: one path, `docs/method/session-open/template-history.md`. Authority cited: the
2026-07-23 ruling. The ruling's text lives in `.atelier-floor.json` line 11 (a non-barred
home): frozen historical *record stores* are kept verbatim, history is not re-spelled,
and the gate protects new live prose. The floor scopes spellscan to `docs/method`,
`docs/build` and `docs/decisions`, so without the entry the file cannot land. Does the
ruling cover newly mined text? By its letter, no: it names the record stores
(`docs/sessions/`, `docs/reviews/`, `docs/SESSIONS.md`, `docs/ROADMAP-DONE.md`), and this
file sits on the live doctrine surface the ruling says the gate protects. By its reason,
arguably yes: the text is the principal's own, typed months before, and re-spelling it
would falsify a record. The entry is an extension by analogy that the principal has not
ruled on, and the README presents it as the ruling itself (TH4). No other place mirrors
the ignore list (V3 discharged: the floor JSON scopes by directory and names no paths).

## Standing checklist V1–V7

- **V1 — no claim stronger than its evidence.** Three claims outrun their evidence:
  author date equals first use (TH1), the family count (TH2), the ruling's coverage
  (TH4). The scanner claims and the structural claims reproduce.
- **V2 — re-run every live-proven claim.** Done; ledger below. One claim could not be
  re-run either way (TH3) and one not as-of (the 946/934 source count: the store now
  lists 1064/1057; sessions whose last activity precedes the landing number 938/932, a
  different measure, offered as a bound only).
- **V3 — changed rule swept to mirrors.** The delta changes no rule; the ignore entry
  has no mirror list to sweep. Discharged.
- **V4 — one fact, one home.** The README quotes part of the principal's words with the
  item id as its pointer; the quoted words match the intent record verbatim. Discharged.
- **V5 — no internal contradiction.** Two: version 1–4 author dates against their own
  message lines (TH1); the README's 228 against the messages' 226 (TH2).
- **V6 — security and privacy.** Lens 4 above. Clean on the acceptance test.
- **V7 — spawn provenance stated.** In the brief (its *Spawn provenance*) and above.

## Per-version ledger

Read whole: yes for all 50. Ex1 = exclusion 1 (private or personal), Ex2 = exclusion 2
(one session's work). "clear" means the reviewer found nothing; a finding id otherwise.

| ver | sha | first used (message) | Ex1 | Ex2 | note |
|----:|---------|---------------------|-------|-------|------|
| 1 | 1241b8c | 2026-07-08 13:25 UTC | clear | clear | precursor; author date TH1 |
| 2 | 2fc7107 | 2026-07-09 22:36 UTC | clear | clear | precursor; author date TH1 |
| 3 | 83dc235 | 2026-07-10 03:53 UTC | clear | clear | precursor; author date TH1 |
| 4 | e169290 | 2026-07-10 07:53 UTC | clear | clear | precursor; author date TH1 |
| 5 | 4256ce7 | 2026-07-13 01:23 UTC | clear | clear | placeholder, lines 5–6 |
| 6 | 09b65db | 2026-07-13 03:25 UTC | clear | clear | placeholder, lines 7–8 |
| 7 | e94548c | 2026-07-13 03:45 UTC | clear | clear | placeholder, lines 7–8 |
| 8 | 7ac54d7 | 2026-07-13 03:52 UTC | clear | clear | |
| 9 | bf12878 | 2026-07-13 05:51 UTC | clear | clear | placeholder, lines 7–8 |
| 10 | 45d8955 | 2026-07-13 14:38 UTC | clear | clear | placeholder, lines 7–8 |
| 11 | 8e7b4d5 | 2026-07-13 14:40 UTC | clear | clear | |
| 12 | cb2665a | 2026-07-13 20:43 UTC | clear | clear | |
| 13 | 5ba8092 | 2026-07-13 21:09 UTC | clear | clear | |
| 14 | 43105f9 | 2026-07-13 21:13 UTC | clear | clear | |
| 15 | 1d550b2 | 2026-07-13 21:20 UTC | clear | clear | |
| 16 | 1987721 | 2026-07-14 12:12 UTC | clear | clear | |
| 17 | c9fba4c | 2026-07-14 12:18 UTC | clear | clear | dangling frame, lines 12–14 (TH5) |
| 18 | 29da0e0 | 2026-07-14 12:49 UTC | clear | clear | dangling frame, lines 12–14 (TH5) |
| 19 | 968161d | 2026-07-14 13:02 UTC | clear | clear | |
| 20 | ac642ed | 2026-07-15 11:37 UTC | clear | clear | |
| 21 | cf56a93 | 2026-07-15 12:59 UTC | clear | clear | |
| 22 | c30d160 | 2026-07-18 13:33 UTC | clear | clear | |
| 23 | 6efa9da | 2026-07-20 12:12 UTC | clear | clear | |
| 24 | 6008e8f | 2026-07-21 21:11 UTC | clear | clear | |
| 25 | bff29ab | 2026-07-22 10:16 UTC | clear | clear | |
| 26 | 3ba2cca | 2026-07-22 12:06 UTC | clear | clear | |
| 27 | f1a0877 | 2026-07-23 04:36 UTC | clear | clear | |
| 28 | 1512530 | 2026-07-23 06:15 UTC | clear | clear | |
| 29 | bd046ae | 2026-07-25 09:13 UTC | clear | clear | |
| 30 | 47ff58d | 2026-07-26 07:00 UTC | clear | clear | |
| 31 | 56bdd46 | 2026-08-03 20:11 UTC | clear | clear | lines 7–12: recurrence unconfirmed (TH3) |
| 32 | 34bdec8 | 2026-08-05 12:00 UTC | clear | clear | |
| 33 | 4c94dd6 | 2026-08-05 20:15 UTC | clear | clear | |
| 34 | 50c9286 | 2026-08-09 07:55 UTC | clear | clear | |
| 35 | 3fd444d | 2026-08-15 04:28 UTC | clear | clear | |
| 36 | 20ab473 | 2026-08-15 15:22 UTC | clear | clear | |
| 37 | 33bb2ae | 2026-08-16 04:40 UTC | clear | clear | |
| 38 | f361fdd | 2026-08-16 12:08 UTC | clear | clear | |
| 39 | 52cb7a2 | 2026-08-16 22:27 UTC | clear | clear | `catalog`, line 5 (the README's one) |
| 40 | 2d2e20b | 2026-09-03 10:09 UTC | clear | clear | |
| 41 | 90e8390 | 2026-09-06 14:21 UTC | clear | clear | |
| 42 | 6c55d7d | 2026-09-08 13:34 UTC | clear | clear | |
| 43 | f3c0f2c | 2026-09-08 23:29 UTC | clear | clear | |
| 44 | e3367b0 | 2026-09-12 03:34 UTC | clear | clear | |
| 45 | d727b50 | 2026-09-15 21:03 UTC | clear | clear | |
| 46 | 50932c2 | 2026-09-16 05:44 UTC | clear | clear | |
| 47 | cab9733 | 2026-09-16 09:55 UTC | clear | clear | |
| 48 | c191aa4 | 2026-09-17 23:44 UTC | clear | clear | differs from 47 by a dropped rule (TH6) |
| 49 | 552ff96 | 2026-10-05 11:20 UTC | clear | clear | |
| 50 | e6c1137 | 2026-10-17 07:43 UTC | clear | clear | identical to the file at HEAD |

## Findings

Every finding is the principal's to decide; nothing was applied. Counsel sits beneath
each, labelled.

### TH1 — minor · versions 1–4 carry author dates twelve hours early

**Where:** commits `1241b8c`, `2fc7107`, `83dc235`, `e169290`: author dates
`2026-07-08T13:25:00+12:00`, `2026-07-09T22:36:00+12:00`, `2026-07-10T03:53:00+12:00`,
`2026-07-10T07:53:00+12:00`. Versions 5–50 are in `Z` with seconds.
**What:** each message says "First used … UTC" with the same wall-clock digits, and the
README says the author date *is* the first use. The digits are UTC (the store's earliest
session for version 1 opens at 2026-07-08T13:25:19Z) but the offset written is `+12:00`,
so as instants the four dates are twelve hours before the sessions they stand for, and
their seconds are zeroed. The message lines are right; the author dates are not. V1, V5.
**Counsel:** do not rewrite. The four dates are still on the right day and in the right
order, and rewriting 50 public commits costs more than it buys. One sentence in the README
("the four precursor commits carry their first-use time with a `+12:00` offset by
mistake; read their digits as UTC") closes it honestly.

### TH2 — minor · the README's family count does not reconcile with the messages

**Where:** `docs/method/session-open/README.md` line 36 ("228 sessions") against the 50
version messages, whose first-run counts sum to 142 and re-paste counts to 84: 226.
**What:** by the README's own rule every family session gets exactly one version and is
counted once, as a first-run or a re-paste. Two sessions are in the family and in no
commit. A reason exists that would make both figures true (the README says the newest
prompt text is left out "until it has opened two sessions", and sessions that opened
with it would share paragraphs with the family yet have no committed version) but the
README does not say so, and the reviewer cannot confirm it from the live store. V1, V5.
**Counsel:** the author states where the two sessions went, or corrects the figure.

### TH3 — minor · one unit of version 31 traced to a single session

**Where:** version 31 (`56bdd46`), lines 7–12: one paragraph whose last sentence, in
versions 32 onward, is a bullet of its own. The message credits version 31 with three
sessions.
**What:** on the live store, four sessions carry the paragraph's first 250 characters;
only one (last active 2026-08-04) carries the whole paragraph as one unit; the other
three (last active 2026-08-06 and 2026-08-09) carry the closing sentence as its own
bullet, which is version 32's shape. So the committed unit is seen in one session. The
two sessions that would make it recur are either archive-only (the mirror is entirely
evicted here and was not downloaded) or had version 32's shape, in which case the unit
fails the two-session rule and version 31 is a one-session assembly. The reviewer cannot
tell which. Not a privacy matter: the text is orchestration wording that version 32
publishes anyway. V2.
**Counsel:** the author re-drives this one count from the archive and records the
answer in the README or the pointer; if the unit was used once, the version stands as
history already published and the README says so, rather than rewriting it away.

### TH4 — minor · the ignore entry extends a ruling the README presents as covering it

**Where:** `.spellscanignore` lines 36–39; README lines 61–66.
**What:** the 2026-07-23 ruling (text at `.atelier-floor.json` line 11) is about the
frozen record stores; it says the gate protects new live prose, and the floor scopes
spellscan to `docs/method`. This file is new to the repo and on that surface. Exempting
it is a reasonable reading of the ruling's reason (the principal's past text, kept as
typed), but it is the author's extension, not the ruling, and the README says "kept
verbatim under his 2026-07-23 ruling" as though it were. The hole is one path and the
cover given up is spelling only; the defect is the claim, not the entry. V1.
**Counsel:** the principal either confirms the extension in his own words (and the
`.spellscanignore` comment cites that), or it is narrowed: the one `catalog` is already
exempt when inline-coded, as the README shows, but a version's text is his verbatim
record and should not be edited to suit a scanner, so the path entry is the honest
shape if he confirms it.

### TH5 — note · removed units leave no mark, except one

**Where:** versions 17 and 18, lines 12–14: a bullet that introduces a list ends at a
colon and nothing follows. The README's "What was taken out" (lines 45–51) describes
nine removals and one placeholder.
**What:** eight of the nine removals are invisible in the text, so a reader meets a
colon with nothing after it and cannot tell whether the principal wrote it that way or
a unit was taken out. The one placeholder shows the other way of doing it. The versions
are published history now and should not be rewritten; the README can say it.
**Counsel:** one sentence in the README: removals are unmarked, and a bullet ending at a
colon is where a run's task list was.

### TH6 — note · a "version" can itself be single-use under the stated rule

**Where:** README lines 40–44 (the rule); 17 of the 50 messages say "opened 1
session(s)" with no re-paste. Version 48 is version 47 without its horizontal rule.
**What:** the principal defined the template by parts reused across sessions; the
README applies that to units, so any ordered assembly of recurring units is a version
even if that assembly opened one session. That is a fair reading, but the README should
say it, since a reader of the history will meet 17 one-session versions and the
principal's own words say a one-session thing is not template.
**Counsel:** one sentence in the README naming the consequence; or, if the principal
prefers version-level recurrence, a decision for him on whether the 17 stay (they are
published history) and how the rule reads for new versions.

## Re-run ledger (V2)

- **50 versions through `leakscan --require-terms`:** clean; structural plus the local
  term list, so full cover.
- **50 versions through `secretscan`:** clean, 0 advisory.
- **50 versions through `datescan`:** clean.
- **50 versions through `spellscan`:** 1 finding, `catalog` at version 39 line 5, as the
  README says.
- **50 version messages through `leakscan --require-terms`:** 2 hits, both the
  co-author trailer's address in the reviewer's scratch rendering (identical lines are
  deduped by window, and two of fifty slipped through); the address is public and on
  every commit in this repo. Noise.
- **50 version messages through `secretscan`:** 4 advisory hits on the 40-hex commit
  ids in the scratch file's own layout. Noise.
- **The two barred bodies:** deferred to phase 2.
- **Floor at HEAD `3148ea4`, ci plane:** exit 0. 🟡 secretscan 25 advisory; 🟡 leakscan
  without `--require-terms` (the ci plane's own wiring); pathscan 1 warn-only hit out of
  delta (`docs/decisions/2026-10-03-0641-the-exception-register.md` line 84); every other
  guard ✅.
- **Recurrence test, live store:** RAN. 1064 sessions listed, 1057 with a typed first
  prompt. 244 share at least one version unit and were last active before the landing
  (a looser test than the author's, so no contradiction of 228). 106 of the 109 units of
  20 or more characters recur in two or more sessions; the 2 placeholder units recur in
  none (expected: the placeholder exists only in the repo); 1 unit recurs in one (TH3).
  Precursor whole-prompt matches 4, 2, 9, 8 against the messages' 4, 2, 10, 9. The
  earliest version-1 session's first turn is 2026-07-08T13:25:19Z (TH1).
- **Recurrence test, archive mirror:** NOT RUN. 1064 rows, all evicted; not
  materialised, since that is a bulk download and this was a no-network run.
- **README "946 sessions, 934 typed":** not reproducible as-of; the store has grown
  (the bound is under V2 above).
- **`/security-review`:** NOT RUN, discharged with grounds under lens 4.

## Follow-up checklist

- [ ] Principal: TH1 — README sentence, or a history rewrite (counsel: the sentence).
- [ ] Author or principal: TH2 — reconcile 228 with 226 in the README.
- [ ] Author: TH3 — re-drive version 31's count from the archive; record the answer.
- [ ] Principal: TH4 — confirm or narrow the ignore entry's authority in his words.
- [ ] Author: TH5, TH6 — two README sentences, if the principal agrees.
- [ ] Reviewer: phase 2 — open the sibling and the rest of the intent record, screen the
      two barred bodies, append `### Reconcile`, restate the overall line.
- [ ] Orchestrator: commit act 1 unrevised before act 2 opens; tick the `160/940` pointer
      when phase 2 lands.

### Reconcile (phase 2, 2026-11-01)

Opened after act 1 was committed (`0965466`): the held sibling, at the one copy the
orchestrator named; the intent record from line 14 (unchanged between `ec37c6b` and
HEAD); the queue pointer `160/940`; the bodies of `7033378` and `ec37c6b`; and the head
and overall line of the one prior verdict the sibling names
(`2026-10-16-1550-first-prompt-prefix-cold.md`, a code pass on `cctranscript`, which does
not touch this delta). Phase-1 text above is unrevised.

**The two barred bodies, screened for privacy.** Clean. `7033378` names the principal
by the first name the repo already declares and nothing else private; `ec37c6b` is one
line. Through leakscan and secretscan: only the co-author trailer's address, as before.
One fact in `7033378` bears on TH4: the ignore entry was added "for one US spelling of
his", so a path-wide hole was cut for one word (counsel under TH4 unchanged: the path
shape is still the honest one if the principal confirms it, because his verbatim text
should not be edited to suit a scanner).

**The author's account against the findings.**

- The account restates "author date is the version's first use" and the 946 / 934 / 228
  figures. TH1 and TH2 stand as written; the account adds that a Sonnet worker mined 86
  raw versions and the orchestrator collapsed re-pastes to 50, which does not move either
  figure (collapsing re-pastes loses no session from the counts).
- It says nine flagged units were dropped, each recurring but one run's themed work, five
  of them also naming private repos, tools or devices; one name replaced by the
  placeholder; six borderline units kept as "generic selection wording, no named work".
  Consistent with the README and with what the reviewer found. The six are not listed in
  the account; see seeded question 2 below for the reviewer's own identification.
- It does not mention version 31 (TH3), markers for removals (TH5) or single-use versions
  (TH6). All three stand.
- It says the scanners are clean on every version and names the `catalog` exemption
  under the 2026-07-23 ruling in the same words as the README. TH4 stands: the account
  adds no ruling text, only the same claim.

**The seeded questions.**

1. *Does the placeholder's role label let a reader infer what it replaced?* No. The
   role ("the private estate-root repo") is already named in those words across the
   public doctrine (lens 1, point 3), and the frame says only that a parent repo exists.
   No finding.
2. *Which are the six borderline units, and does each pass exclusion 2 on its own text?*
   By the reviewer's read, the "start with work that: (a) …" clauses of versions 25, 26,
   41 and 42; the "work that I give you in my next message, copied from a catalogue" unit
   of version 39 (line 4–5); and the "specific items … in the following message mid-turn"
   unit of version 45 (lines 42–43). Each names no task, feature, item, theme or
   deadline, and each recurs in two or more sessions on the live store. All pass on their
   own text.
3. *Did a reworded or partial form of a dropped private unit survive elsewhere?* None
   found. Across the 50 versions the only named repo is this one, the only tool name is
   a public instrument of this repo, and the only device-like strings are a harness
   environment variable and a public tool name. No finding.
4. *Is naming the removed classes more than a public reader needs?* No. The classes
   (private repo and tool names, device names, a credential store) are the same classes
   `REPO-STANDARD.md` already lists as PII-by-default, and a reader cannot trust a
   redacted record without knowing what kinds of thing were taken out. No finding.
5. *Do the dated author dates and counts publish personal information?* Weighed in lens
   4 (metadata) and recorded as a note under TH1's counsel, not a finding: the repo's
   own commit log already carries the same timestamps in class, and the README's
   946-session figure already gives the volume. Day-level dates would serve the stated
   aim; the seconds are a precision the aim does not need, and the principal may choose
   to leave them.
6. *Was the 2026-07-23 ruling about text already in a repo, and does it reach newly
   mined text?* It was about the frozen record stores already in this repo (the
   queue-run-0959 spellscan apply; text at `.atelier-floor.json` line 11). Reaching a
   new file on the live doctrine surface is the author's extension. TH4.
7. *The `nz-phone` hit.* Reproduced from the brief-writer's exact command: the hit is
   on a 40-hex commit id line that the `%H` format itself writes (the 25th of 52 from
   the newest), not in any message body. Its digits happen to shape like a phone number.
   Noise from the scan's own rendering; no finding.
8. *Does the recurrence count distinguish sessions the principal opened from sessions a
   run spawned?* It cannot: the store lists sessions, not who typed the first prompt,
   and the author's account does not say. For the most re-pasted versions the live store
   shows the same opener in 49 sessions across 9 repos over 15 days (version 47) and 21
   sessions across 6 repos over 6 days (version 49), eleven on the busiest day in each
   case — a pattern a run spawning workers would also produce. It changes no finding:
   the units in those versions are generic however many sessions ran them. It is a
   limit of the method worth one README sentence, folded into TH6's counsel.

**Formed at reconcile.**

#### TH7 — minor, formed at reconcile · the earlier reconstruction's history was never audited

**Where:** the intent record, lines 14–17 (the V1–V9 reconstruction folded in by subtree
merge `0a949b4` "not audited for the two exclusions"); the sibling's *Overlap* note; the
queued passes under `160/` that name `session-open-prompt.md` (`330`, `540`, `900`),
each for a doctrine change to it, none for its history's privacy.
**What:** the current prompt file's own public history holds an earlier reconstruction
of the same material, by version, that the intent record says was never tested against
the principal's two exclusions. This pass did not read it (out of delta; the brief's
non-goal) and no pass is queued to. The gap is the same class this pass exists for, on a
file this delta's README points readers at.
**Counsel:** queue a privacy cold pass on `session-open-prompt.md`'s history, scoped to
the commits from `0a949b4` to its first commit after `2026-10-18`, with the same two
exclusions as the test. The orchestrator can queue it; the reviewer forms no view on
what it will find.

**Overall line, restated:** PASS-WITH-FINDINGS · 0 MAJOR · 0 MODERATE · 5 minor ·
2 notes. Clear on the acceptance test; the findings are on the framing record, one
version's recurrence, and a neighbouring history that is owed its own pass.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-01)

*Released to the reviewer only after its act-1 findings were committed; folded here
verbatim and the sibling file removed, per the brief. The orchestrator (session `5b6884f2`,
Claude Opus 5.5, started by session `c87c4ee0`) formed no finding and wrote no severity.*

### Sibling to the template-history privacy cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-18-0511-template-history-privacy-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the
brief are committed.** Written 2026-10-18 UTC by the Opus brief-writer named in the
brief's provenance; it forms no finding. Fold this file in below the reconcile and
delete it at phase 2.

#### Intent record

- `docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/060-the-opening-prompt-template-history-from-the-transcripts.md`
  — read in full by the brief-writer. Lines 3–13 are the principal's words (the
  brief's acceptance test). Lines 14–21 say what existed before (an earlier
  reconstruction folded in by subtree merge, `0a949b4`, by version and "not audited for
  the two exclusions") and what was owed. Lines 23–40 are the author's closing account:
  sources and counts, who mined and who checked, how many units were dropped and why,
  one name replaced by a placeholder, some borderline units kept, scanners clean, one
  spelling exemption, what could not be recovered. Read it now as the author's claims
  to reconcile against.
- The bodies of `7033378` and `ec37c6b` — not read by the brief-writer.

#### Re-run results held back from the brief

Run once by the brief-writer, 2026-10-18, from its worktree root, on this machine,
with the local term list present:

- The 50 extracted versions: leakscan `--require-terms` exit 0, secretscan exit 0,
  datescan exit 0.
- The 52 delta messages (`7033378^..ec37c6b`): secretscan exit 0; **leakscan exit 1**.
  By rule name only: `email` ×52 and `nz-phone` ×1. The file holds 52 Co-Authored-By
  trailers, which matches the email count; the brief-writer did not look at any
  matched text, including the `nz-phone` hit, and forms no view on it.

#### Prior verdicts on nearby surfaces (named by filename, not opened, not exhaustive)

- `docs/reviews/2026-10-16-1550-first-prompt-prefix-cold.md` — name suggests the
  session-open prompt; not opened.

#### Overlap with other surfaces

- The current prompt file `docs/method/session-open/session-open-prompt.md` carries the
  earlier reconstruction's history (V1–V9, subtree merge `0a949b4`), which the intent
  record says was never audited for the two exclusions. It is outside this pointer's
  delta. A grep of `docs/roadmap/160-doctrine-review-owed/` found three queued passes
  naming that file (330, 540, 900), each for a doctrine change to it, none (by grep
  for "privacy") for its history's privacy. Whether one is owed is a reconcile
  question.

#### The pointer's own lens hints

It asks for every one of the 50 versions to be tested against the two exclusions
quoted in the intent record. Nothing else.

#### Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. One unit keeps its frame with a private repo's name replaced by a placeholder. Does
   the frame, or the placeholder's role label, still let a reader infer what it
   replaced, given what else in this public repo names roles in the estate?
2. The author kept some borderline units as "generic selection wording". Which are
   they, and does each pass exclusion 2 on its own text rather than on the author's
   description of it?
3. Dropped units named private repos, tools or devices. Did a reworded or partial form
   of any of them survive in a different version, where an exact-match recurrence
   filter would treat it as a separate unit?
4. The README's *What was taken out* bullet names classes of private detail it removed.
   Is naming the classes (with their kinds of object) itself more than a public reader
   needs?
5. Author dates set to each version's first use, plus usage and re-paste counts in the
   bodies, publish a dated timeline of how often the principal opened sessions with
   this prompt. Is that within his stated aim, or personal information in the sense of
   exclusion 1?
6. The `.spellscanignore` entry cites a 2026-07-23 ruling that historical text is not
   retro-spelled. Was that ruling about text already in a repo, and does it reach text
   newly mined from private transcripts?
7. The `nz-phone` hit above: what does it match, and is it in a version commit's body
   or in one of the two author bodies?
8. A unit that recurred in two or more sessions can still be specific work if one run
   pasted it into its own workers. Does the recurrence count distinguish sessions the
   principal opened from sessions a run spawned?
