# Cold pass — the opening prompt's template history, for privacy and specific work

**Pass type:** records and privacy cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-18 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
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
