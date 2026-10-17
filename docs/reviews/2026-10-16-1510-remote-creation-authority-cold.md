# Cold pass — REPO-STANDARD's remote-creation authority

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus brief-writer;
the pass waits for a further cold Fable session that neither the delta's author nor this
brief-writer (nor its orchestrator) started or instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/530-rule-4-cold-pass-queued-remote-creation-authority.md`.
**Why it earns a review:** it changes what authorises an agent to create a remote repository — an
act on the boundary between "push to the owner's own remotes" (granted) and widening an audience
(the floor) — in the standard every new repo is built to.

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

- `96ffaa3` (2026-10-03) — build: a new remote needs the principal's ask, not 'push is
  recoverable' (200/100 C2)

Delta path: `docs/build/REPO-STANDARD.md`, step 5 of *Process — a new repo*. A later commit,
`1ffefc7`, edited other parts of the same file (another pass's subject); check it did not move
step 5.

## Scope

Widest the work admits; the lenses organise it, they do not bound it. Non-goals are the only
narrowing and are themselves reviewable.

Probe, at least:

- **Which text is the parent.** Step 5 now matches `skills/create-repo/SKILL.md` step 7. Establish
  from `docs/method/PROPAGATION.md` which of the two is canonical, how a parent/child disagreement
  is meant to be resolved (and what holds in the interim), and who decides it. Search the
  doctrine and `docs/decisions/` for any principal ruling on remote creation, either way.
- **AUTONOMY's classes.** `docs/method/AUTONOMY.md` grants push to the owner's own remotes and puts
  making a private thing public, and new trust surfaces, on the floor. Where does creating a remote
  sit? Does AUTONOMY say it, and does step 5 agree with what AUTONOMY says or leaves unsaid?
- **"The principal's ask itself."** Case table: the principal asks for "a new repo" with no
  mention of a remote; a queue run takes a board item that says "create repo X"; standardising an
  existing repo that has no remote; a local experiment later promoted; the instance profile's
  default visibility set to public; an owner account that is an organisation, not the operator.
  For each: does step 5 tell the session whether to proceed, confirm, or stop?
- **The steps after.** Step 6 sets delete-branch-on-merge "on the new remote", and the visibility
  fact is stamped into the child. What happens to both while a confirmation is pending or refused?
- **The cross-reference.** "`skills/create-repo` step 7 says the same": verify the claim, and
  whether anything keeps the two in step when either is renumbered.

**Non-goal:** whether creating a remote should need confirmation at all is the principal's call;
whether the text gives a session one clear answer, and agrees with its neighbours, is the subject.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Ask whether the
   change took "the more careful reading" on authority the doctrine actually gives, and whether
   "the principal's ask" is something a session can determine from what it holds.
2. **Correctness & quality.** Diff `96ffaa3`. Run the case table and record it.
3. **Completeness / harvest.** Every other site that states who may create a remote or the "push
   is recoverable" reasoning: AUTONOMY, the create-repo skill's other steps, the session-onramp
   skill, `README.md`, the templates, the PROPAGATION floor region. Which still say the old thing?
4. **Security & privacy** — mandatory. A remote is an audience surface: wrong default visibility,
   the wrong owner account, a remote created before a scan has run on the first commit. Say whether
   step 5 and its neighbours keep each closed. No code surface: `/security-review` is discharged by
   grounds.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `git log -S 'push is recoverable' --oneline` across the tree, to find every site that ever
  carried the old reasoning and whether each was swept
- `python3 tools/stampscan.py --warn --root . .` and `python3 tools/pathscan.py --root . .`
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`)

Do not create any remote, even a scratch one, to test the rule.

## House rules for this run

- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and your scratch
  clone. Never open another `docs/reviews/2026-10-16-1510-*` file — it is another pass's framing.
- No git command that writes in the worktree, beyond committing this one file at the end of each
  phase (or handing it to your orchestrator to commit). Read-only git is fine. Older checkouts go
  in a private clone under your session scratchpad, named by your prefix.
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
`docs/roadmap/160-doctrine-review-owed/530-rule-4-cold-pass-queued-remote-creation-authority.md`,
the sibling `docs/reviews/2026-10-16-1510-remote-creation-authority-cold.deferred.md`, the landing
commit's message body (the author's account; read subject, stat and diff only), and the
commissioning item
`docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md`.

Sweep with `python3 tools/coldsweep.py --root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/530-rule-4-cold-pass-queued-remote-creation-authority.md
--also-exclude docs/reviews/2026-10-16-1510-remote-creation-authority-cold.deferred.md
--also-exclude
docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is never
barred; the author's narrative of why, and the verdicts that recorded it, are.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Append your verdict
below a `---` divider in THIS file: provenance repeated (how you were spawned, your tier, what you
read), per-lens answers, findings with stable IDs (prefix `RM`: `RM1`, `RM2`, …) and severities
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

## Provenance (repeated, V7)

- **Reviewer:** a fresh `claude-fable-5-1` subagent — the tier the principal names for cold
  passes (rule 4, ruling 2026-08-04) — spawned 2026-10-17 by a Fable orchestrator that authored
  neither the delta nor this brief, and that holds the `.deferred.md` sibling outside this
  reviewer's reach until these findings are committed (the context partition, rule 1). The
  orchestrator forms no finding and writes no severity. The brief was written 2026-10-16 by an
  Opus subagent, disclosed off-tier above; it formed no finding either.
- **Author of the work:** the 2026-10-03 queue run that landed `96ffaa3`. This reviewer was not
  started or instructed by it and had never seen the delta before this pass.
- **Worktree:** `/Users/mike/worktrees/atelier-review-1017`, branch `review-1017`, HEAD
  `f611b3b` (`8acfff1` confirmed an ancestor by `merge-base --is-ancestor`). Read-only to this
  reviewer except this file; no git write was run. The 21 `D` entries for
  `docs/reviews/2026-10-16-15*.deferred.md` in `git status` are the orchestrator's partition,
  not this pass's doing.
- **What was read:** `96ffaa3` by subject, `--stat` and the diff on the delta path only (body
  unread); `1ffefc7` by subject, stat and hunk headers; `docs/build/REPO-STANDARD.md`,
  `skills/create-repo/SKILL.md` and `instance.yaml.example`, `docs/method/REVIEW.md`,
  `AUTONOMY.md`, `PROPAGATION.md` (§ layer-override, § who is a child, § one statement, the
  floor region), `00-APEX.md` lines 80–125, `ACCESS.md` head, `PRINCIPLES.md` § 6 sweep list,
  ADRs 0003 and 0005, `docs/build/templates/CLAUDE.md`, `CHANGELOG.md` lines 2749–2758, the
  board item `320/370` (a child-filed report; not in the barred set), the hook, `ci.yml` and
  `tools/floor.py` for invocations. Historical diffs were read only on non-barred paths
  (`17ccbde` REPO-STANDARD; `bbdeece` templates, PROPAGATION, CHANGELOG; `2271a44` skills).
- **What was not read:** the sibling, the queue pointer, the commissioning item `200/100`,
  `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, any prior verdict, any other
  `2026-10-16-15*` brief, any landing commit's message body. Every sweep ran through
  `tools/coldsweep.py` with the three `--also-exclude` paths the brief lists; **no
  `--include-barred` sweep was run.** One incidental exposure to disclose: `git log -S`
  listed `f88bace` and `88f9925` by subject and `--stat` (the briefs batch and the R2 survey
  commit, whose stat names a session file and the commissioning item); subjects and filenames
  only, no content opened.
- **Load discipline:** machine load 21–29 throughout; every scanner ran under `nice -n 10`,
  one at a time, foreground. No test suite was run (the brief's re-run list names none).

## Lens 1 — approach and assumptions

Load-bearing assumptions, named first and then tested:

- **A1 — REPO-STANDARD is the parent and the skill is its delivery copy.** Both texts say so
  (REPO-STANDARD § *What lives elsewhere*: the skill "inherits from this doctrine rather than
  re-encoding it"; the skill's own header: atelier "is the source of truth"). True — but the
  history runs the other way. `17ccbde` (2026-07-10) wrote step 5 with "push is recoverable";
  `bbdeece` the same day re-anchored the *skill's* step to the principal's ask (CHANGELOG
  line 2755) and did not touch REPO-STANDARD; `2271a44` (2026-07-21) carried that wording into
  `skills/create-repo/SKILL.md`; the parent kept the opposite until `96ffaa3` (2026-10-03). So
  for 85 days the child was stricter than the parent, which PROPAGATION's interim rule (the
  stricter reading wins) handled correctly, and the delta resolved it in the parent, which is
  the right place. The delta did take the more careful reading — but it took it *from the
  child* and cites the child as its warrant ("step 7 says the same"): the parent pointing down
  for truth (RM7).
- **A2 — "the principal's ask" is something a session can determine from what it holds.**
  Not as written: neither text says which channel counts (RM3).
- **A3 — once asked, creating a private remote on the owner's account sits inside the granted
  class.** AUTONOMY never says so; it grants *push to the owner's own remotes* and puts
  `gh repo delete` on the floor, which is the real reason "push is recoverable" was the wrong
  ground — a created remote is one the agent cannot remove alone. Nowhere stated (RM4).
- **A4 — a remote created private has no audience.** False when `remote.account` is an
  organisation (RM6).
- **A5 — the default visibility is private.** Only while the profile says so (RM1).
- **A6 — after step 5 a remote exists.** The delta's own confirm branch breaks it (RM5).

The brief's account of the work held up: the delta is nine lines on one step, nothing else in
`96ffaa3` touches live doctrine (the other three paths are board records), and `1ffefc7`
edited lines 167–191 of the same file only, moving step 5 by line number, not by position.
The non-goal is sound: whether confirmation should be required is the principal's, and this
verdict stays off it.

## Lens 2 — correctness and quality

The diff was read at `96ffaa3` and at HEAD; the text is unchanged since landing. The claim it
makes — "push is recoverable" covers only the push — is correct and an improvement. The case
table, run against step 5 and step 7 together:

| Case | Step 5 (REPO-STANDARD) | Step 7 (skill) | One clear answer? |
|---|---|---|---|
| "Make me a repo for X" — no remote mentioned | "when they asked for a repo *with a remote*"; a bare ask is not clearly that ⇒ reads as confirm | "they invoked create-repo; a repo on their own account is what they asked for" ⇒ proceed | **No — the two sites differ on the commonest case** (RM2) |
| Queue run takes a board item "create repo X" | silent on whose ask a board item is | silent | No (RM3) |
| Standardise an existing repo with no remote | confirm (named) | confirm (named); § standardise says "offer the push" | Yes |
| Local experiment later promoted | confirm (named) | confirm (named) | Yes |
| Profile `visibility: public` | "private by default"; publishing is a floor action | same prose; but the command runs `--<remote.visibility>` | **No — the mechanics open what the prose closes** (RM1) |
| `remote.account` is an organisation | silent | silent; owner check exists only for *existing* repos | No (RM6) |
| Confirmation refused ⇒ no remote | step 6 and the stamp presuppose one | `<owner/repo>` "(once the remote exists)"; the stamp proof cannot pass | No (RM5) |

Honesty: no overclaim inside the delta's own sentences except "says the same" (RM2); no silent
scope-cut.

## Lens 3 — completeness and harvest

`git log -S 'push is recoverable'` names six commits. Where the old reasoning lived and what
became of each: `17ccbde` introduced it in REPO-STANDARD step 5 (swept by the delta);
`bbdeece` removed it from the skill's step (the sweep that missed the parent); `2271a44`
carried the skill's corrected wording into `skills/`; `f88bace` and `88f9925` are records
(the R2 survey and the briefs batch — barred, subjects only); `96ffaa3` is the delta. The
cold sweep at HEAD finds the phrase in three live places: CHANGELOG (history, correct), the
delta (quoting it to reject it) and the skill (same). **No live surface still states the old
reasoning.** The two "recoverable" lines that remain — the floor block's "everything
recoverable — commit/push/PR included — just proceed" and § standardise's "Commit (recoverable
— proceed)" — are correctly scoped to commit and push, not creation. `README.md`, the
session-onramp skill, the `commands/`, the templates and `docs/build/README.md` carry no
remote-creation rule at all. Over PRINCIPLES § 6's sweep surfaces (`docs/`, `skills/`,
`commands/`, templates, children's floor blocks) the sweep is complete.

What exists and the work ignored: board item `320/370`, filed from a child on 2026-09-20,
already reports that the floor's `<owner/repo>` / `<visibility fact>` line has no admissible
fill for a repo with no remote. The delta's confirm branch manufactures exactly that repo and
does not point at the item (RM5). AUTONOMY, the home of proceed/confirm classes, was not
touched and remains silent on remote creation (RM4).

## Lens 4 — security and privacy

`/security-review` **discharged by grounds**: it reads this session's pending diff, which is
other reviewers' drafts, not this landed delta; and the delta is markdown, outside its file
class, so a clean pass would be definitionally empty. The read was done by hand at design
altitude against OWASP Top 10 (2021) as analogues for a non-code surface:

- **A05 security misconfiguration — wrong default visibility.** Step 5's prose closes it
  ("private by default"; publishing is a floor action). The one mechanical path to creation
  reads visibility from a standing profile value whose schema calls it "default visibility for
  new repos" and nothing says `public` there still stops at the floor per repo. **Open** (RM1).
- **A01 broken access control — wrong owner account.** A private repo under an organisation
  account is readable by that organisation's members from its first push: an audience at
  birth, which AUTONOMY's floor names ("adding a collaborator or widening an audience").
  Neither text distinguishes a personal from an organisational `remote.account` at creation;
  the only owner check guards *existing* repos. **Open** (RM6).
- **A02/A09 — a remote created before a scan has run on the first commit.** The skill's
  step 6 wires the fail-closed hook before step 7's commit, so the delivery vehicle keeps it
  closed. REPO-STANDARD's own process (steps 1–6) never wires a hook: step 5 commits and
  creates the remote with no scan gate named before it. The hook appears in the standard only
  as the thing `floor.yml` backstops. By the canonical text alone the gate is **open** (RM8).
- `delete-branch-on-merge` (step 6) has no security surface. No secret, personal detail or
  private-repo name is introduced by the delta.

## Findings

**RM1 — MAJOR — a profile that says `public` reaches `repo create --public` with no stop.**
Step 5 and step 7 both say publishing "is always a floor action". The skill's only creation
command is `<remote.host> repo create … --<remote.visibility>`, substituted from
`~/.atelier/instance.yaml`, whose schema (`instance.yaml.example` line 21) describes the key as
"default visibility for new repos" and admits `public` without comment. AUTONOMY says the floor
holds "standing grants notwithstanding" and that "yes, publish this" is not "publish things
like this from now on" — a standing `public` default is the second sentence. PRINCIPLES § 6:
"a new surface opens closed." The `<visibility fact>` stamp text is given only in its private
form. The delta's floor sentence does not reach the command, the schema, or the stamp. Lens 4
(V5, V6). *Counsel:* either make the key private-only (drop `public` as a value, so a public
repo is always a per-repo floor stop after creation), or state in the schema comment and in
step 7 that `public` in the profile is a default the floor still interrupts per repo, with the
public form of the visibility fact given.

**RM2 — MODERATE — "step 7 says the same" is not true of the test, only of the examples.**
Step 5 grants authority "when they asked for a repo *with a remote*" and says to confirm if the
ask "did not clearly include a remote". Step 7 grants it on invocation: "they invoked
create-repo; a repo on their own account is what they asked for". For a bare "make me a repo"
— the commonest ask — step 7 proceeds and step 5 reads as confirm. Both texts agree on the two
named exceptions, which is why the delta could believe they match. V1, V5. *Counsel:* pick one
test and state it once (RM7 says where); the principal decides which.

**RM3 — MODERATE — "the principal's ask" names no channel, so a session cannot tell whether
it holds one.** A queue run takes a board item saying "create repo X"; a subagent is handed a
prompt by an orchestrator; a roadmap slice was written by an agent. Each is an ask, none is
necessarily the principal's. The house already distinguishes the principal's own words from an
agent's framing elsewhere (00-APEX § the principal's authority; REVIEW rule 3's author /
principal split); step 5 and step 7 use "the principal's ask" as if it were self-evident. Lens
1. *Counsel:* say what counts (his words, or his answer in the question device, naming the
remote) and what does not (an agent-written item or prompt), and ask for the record of it.

**RM4 — MODERATE — an autonomy class has been decided in REPO-STANDARD, and AUTONOMY is
silent.** AUTONOMY says of itself "the rest of this doc is where the line falls"; its *always
proceed* list grants commit, push and PRs on the owner's own remotes, and its floor lists
`gh repo delete`. Creating a remote appears in neither list. Step 5 now rules it (proceed on
the ask, confirm when unclear) in the build standard, and REPO-STANDARD's own "Private-first"
bullet sends the reader to AUTONOMY for the class. No principal ruling on remote creation was
found in any non-barred surface: the CHANGELOG's "re-anchored to Mike's ask" (2026-07-10)
names the ask as the *ground*, not a ruling *about* it. The asymmetry that actually decides
the class — the agent may create a remote but may not delete one — is stated nowhere. V4.
*Counsel:* one line in AUTONOMY, under whichever list the principal rules, naming the
asymmetry; step 5 and step 7 point to it instead of restating.

**RM5 — MODERATE — the confirm-refused branch is a dead end both texts walk into.** If the
principal says "no remote", step 6 ("on the new remote") has no object; the floor block's last
bullet needs `<owner/repo>` and `<visibility fact>`, which step 7 fills "once the remote
exists"; and step 5's mechanical proof — `grep` for the placeholders, "expect: no hits
ANYWHERE" — cannot pass, so the session either leaves the stamp unproven or invents a fill.
The house already holds this defect as board item `320/370` (filed from a child 2026-09-20:
"a declared placeholder in the floor has no admissible fill for a repo with no remote"); the
delta creates the case in the parent's own process and does not point at it. Lens 3 harvest,
V5. *Counsel:* the fix belongs in `320/370`'s ruling; until then step 5 should say what a
remote-less repo stamps and that step 6 is skipped.

**RM6 — MODERATE — an organisation-owned remote is an audience at birth, and nothing says
so.** `remote.account` may be an organisation. A private repo there is readable by its members
from the first push, which is AUTONOMY's "adding a collaborator or widening an audience" —
floor. Step 5's "private by default" treats private as audience-free; the only owner check in
either text ("don't standardise a third-party repo") guards existing repos. Lens 4.
*Counsel:* when the account is not the operator's personal one, treat creation as
audience-widening and confirm, or have the principal rule that the profile's account choice
is the standing grant.

**RM7 — minor — two originals, a downward pointer, and a by-number cross-reference nothing
guards.** Step 7 is a full restatement, not a stamped copy (no `stamp:` marker; `stampscan`
verifies one block in the tree, the templates' floor). The parent cites the child for
corroboration, which PROPAGATION says the parent never does. "Step 7" is a step number;
`linkscan` and `pathscan` resolve paths, not steps, so a renumbering breaks the reference
silently. The grounding is this delta's own history: the 2026-07-10 sweep fixed the skill and
missed the standard for 85 days. V3, V4. *Counsel:* one statement in the home RM4 names; both
steps carry a one-line pointer, or a stamped copy.

**RM8 — MODERATE — REPO-STANDARD's new-repo process creates the remote with no scan gate
named before the first commit.** Steps 1–6 never wire the pre-commit hook; the hook exists in
the standard only as the thing `floor.yml` backstops (file-set entry, lines 116–117). The
skill's step 6 does wire it, fail-closed, before step 7 — so the vehicle is safe and the
canonical text is not. AUTONOMY: "run a secret-scan before pushing content that could carry
one." Lens 4 (the brief's "a remote created before a scan has run"). *Counsel:* a step in the
standard between commit and remote — or before commit — naming the hook, so the vehicle
inherits the order rather than supplying it.

**RM9 — note — the "Private-first" convention grounds a live default on a superseded ADR.**
REPO-STANDARD line 191–192 cites `decisions/0003`, whose status is "superseded by 0005" and
whose subject was atelier's own visibility. The live default's actual homes are the profile
schema and step 5. Not the delta's doing; recorded because the delta's sentence sits six
lines from it and a reader checking grounds lands on a dead decision.

## Overall

**PASS-WITH-FINDINGS — 1 MAJOR · 6 MODERATE · 1 minor · 1 note.** The delta is a correct
correction and should stand: the old ground was wrong, the sweep of it is complete, and the
parent now holds the resolution. The findings are about what the sentence vouches for and what
it leaves unsaid at the audience boundary — the one place this doctrine cannot afford a gap.
All nine are the principal's to decide (rule 3); nothing has been applied.

## Re-run ledger

| Command (from the worktree root, `nice -n 10`) | Result |
|---|---|
| `date -u`; `git rev-parse HEAD`; `git merge-base --is-ancestor 8acfff1 HEAD` | 2026-10-17 09:58 UTC; `f611b3b`; ancestor confirmed |
| `git show --stat` / diff of `96ffaa3` on `docs/build/REPO-STANDARD.md` | 9 lines on step 5; text identical at HEAD |
| `git show --stat 1ffefc7`; hunk headers on REPO-STANDARD | one hunk at lines 167–191; step 5 not moved |
| `git log -S 'push is recoverable' --oneline` | 6 commits: `88f9925 96ffaa3 f88bace 2271a44 bbdeece 17ccbde` (ledger in lens 3) |
| `coldsweep 'push is recoverable'` (+3 `--also-exclude`) | 3 hits (CHANGELOG, step 5, step 7); 396 files barred; exit 0 |
| `coldsweep` remote-creation pattern | 11 hits; every one examined above; exit 0 |
| `coldsweep` confirmation / floor-action pattern | 11 hits; none states a remote-creation rule beyond the two steps; exit 0 |
| `python3 tools/stampscan.py --warn --root . .` | clean; 1 stamped block verified identical; exit 0 |
| `python3 tools/pathscan.py --root . .` (brief's bare form) | 70 findings, exit 1 — none on the delta path; the registry runs pathscan `--warn` on both planes |
| `python3 tools/floor.py --plane ci --root .` | **exit 0**: 12 enforced checks green; secretscan 23 advisory (entropy class, expected); pathscan 2 warn-only findings, both unrelated to the delta |
| `/security-review` | discharged by grounds (lens 4) |
| Python / node test suites | not run — not in the brief's re-run list; load 21–29 |

## Follow-up checklist

- [ ] RM1 — principal rules whether `visibility: public` stays a profile value; schema comment,
      step 7 and the public form of the visibility fact follow the ruling.
- [ ] RM2 / RM7 — one statement of the authority test, in the home RM4 settles; both steps
      point to it.
- [ ] RM3 — define what counts as the principal's ask for a remote and what record it leaves.
- [ ] RM4 — one AUTONOMY line on remote creation, naming the create/delete asymmetry.
- [ ] RM5 — fold the remote-less case into `320/370`'s ruling; step 5 names it meanwhile.
- [ ] RM6 — rule the organisation-account case.
- [ ] RM8 — a hook-wiring step in REPO-STANDARD's process before the remote.
- [ ] RM9 — re-ground "Private-first" on a live home.
- [ ] Phase 2: open the sibling, reconcile, orchestrator folds and deletes it.
