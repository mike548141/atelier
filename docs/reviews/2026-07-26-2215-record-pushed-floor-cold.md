# Cold review (rule 4) — RECORD.md: the close all-clear carries the pushed floor run's result

**Subject (refs only):** the sub-point added to `docs/method/RECORD.md`'s
all-clear evidence rule in commit `97b4fd2` (2026-07-23): when a close pushes,
the evidence is the floor at head, not the local scan. Establish the exact
hunk with `git show 97b4fd2 -- docs/method/RECORD.md` and review it at HEAD,
in the context of the whole close rule and its siblings.

**Spawn provenance:** this review was spawned by a non-author taker session the
principal (Mike) opened and pointed at the review queue on 2026-07-26 ("Please
do any review work"); the work's author neither started nor instructed this
review or this reviewer; the taker authored none of the delta and gives the
reviewer refs only, no evaluative account. Session and reviewer tier: Fable
(cold review passes run on Fable — the principal's ruling, 2026-07-26).

**Taker exposure, owned:** the taker read the ROADMAP queue pointer and
SESSIONS index one-liners before writing this stub. Nothing evaluative from
either appears above the divider.

**The reviewer's first acts:** establish what the sub-point claims and why
from the delta and HEAD yourself; name the load-bearing assumptions and attack
surface as your own; run all four lenses at the widest scope
(`docs/method/REVIEW.md`). The heavy lenses: 1 — is pushed-floor-at-head the
right evidence bar, and is the rule *followable* from where it binds (what
does a session do when the head run has not reported yet — does the rule
define an honest waiting state, and is that state usable in practice); 2/3 —
coherence with the rest of RECORD.md's close rule, CONCURRENCY's close
discipline, and any sibling that still teaches local-scan-as-all-clear. A rule
about close hygiene is only as good as its observability at close time —
attack that.

**Re-run obligations:** `python3 tools/floor.py --plane ci` (whole-tree floor
at HEAD) · `python3 -m unittest discover -s tools` ·
`node --test instruments/*.test.js` — and note what the *pushed* floor for
this worktree's branch can and cannot show you, since that boundary is the
rule's own subject. Lens 4: a landed markdown doctrine delta —
`/security-review` reaches only pending diffs and excludes markdown, so
discharge it in one explicit line with grounds.

**Reading discipline (hard):** do not open `docs/ROADMAP.md`,
`docs/SESSIONS.md`, `docs/sessions/**`, any other file in `docs/reviews/`, or
anything under `docs/reviews/withdrawn/`. Do not grep git history for review
commits; confine git archaeology to the delta commit named above. Open the
deferred section below only after your findings are durably written to this
file; then append the reconcile, named as such.

Findings carry stable IDs (**RF1…**) with claim / evidence / counsel; close
with **PASS**, **PASS-WITH-FINDINGS**, or **FAIL** and severity counts.
Self-authored doctrine: REVIEW.md rules 3–4 govern — findings are the
principal's to decide; nothing is applied in this pass.

---

## Deferred — open only after your findings are durably written above

*Intent record:* the capture rode the queue pointer itself rather than a
separate record. Its stated grounding: commit `165c40f` — a 00:47 close had
pushed a 🎯-closed item and left the floor red (reviewscan red since 00:06
plus an un-harvested `[x]`), and the next session inherited the debt to
restore green. `git show 165c40f` is the deferred material.

---

## Reviewer's attack surface (named before any deferred material was read)

*Cold rule-4 reviewer, Fable, 2026-07-26 (UTC). Worktree pinned at HEAD
`9aef298`; sub-point established from `git show 97b4fd2 -- docs/method/RECORD.md`
and `docs/method/RECORD.md:112-122` at HEAD. Git archaeology confined to
`97b4fd2` per the brief; `165c40f` deliberately not opened pre-findings.*

Load-bearing assumptions I will attack, named as my own:

1. **The stated mechanism** — "CI runs checks a local scan does not". The
   floor registry (`tools/floor.py --list`) deliberately serves the *same*
   nine scanners to both planes (ADR 0008's one-registry design), and
   `ci.yml`'s own header says the local hook proves *more* than CI (full
   leakscan vs structural-only). Is the real gap check-coverage, or the
   *tree at scan time vs tree at head* — and does the wording send a fixer
   after the wrong repair?
2. **Followability at close time** — the rule permits "green locally, floor
   run pending". Where is "pending" recorded durably (the all-clear is chat;
   the next session reads SESSIONS.md)? Who owns a pending run that later
   reds? Is the observation mechanism (`gh run …`) findable from the rule?
   Is waiting for a ~2-minute zero-dep run cheap enough that "pending"
   should be the exception, not a coequal branch?
3. **Does the rule fix the grounded harm?** The grounding is inherited debt;
   the rule as written fixes the *overclaim*. A compliant "pending" close can
   still hand the next session the same debt — is that intended residual, and
   is it named?
4. **Portability of "floor at head"** — the rule presumes an every-push floor
   (atelier's, because public). ECONOMICS sanctions trimming a private child's
   floor to main-only; a branch-close there has *no* pushed run to carry.
   Children inherit this rule by pointer (PROPAGATION §floor, template
   CLAUDE.md). Is the rule followable where the run it demands doesn't exist?
5. **Terminology** — "floor" is overloaded: GLOSSARY.md defines *Floor* as the
   inlined doctrine subset; here it means the CI scanner-floor run. Can a cold
   reader resolve the referent?
6. **Reach** — CONCURRENCY's queue-run report inherits this all-clear by
   pointer; per-item closes push mid-run. Does the sub-point bind coherently
   there, or leave a gap between per-item pushes and the end-of-run report?

---

## Verdict — cold rule-4 pass, Fable, 2026-07-26 (UTC)

**Provenance, repeated:** spawned by a non-author taker session the principal
opened and pointed at the review queue on 2026-07-26; the work's author
neither started nor instructed this review. Reviewer ran in a worktree pinned
at HEAD `9aef298`; sub-point established independently from
`git show 97b4fd2 -- docs/method/RECORD.md` and `docs/method/RECORD.md:112-122`.
Reading discipline held: no ROADMAP.md, no SESSIONS.md, no `docs/sessions/**`,
no other `docs/reviews/*` file, nothing under `docs/reviews/withdrawn/`, git
archaeology confined to `97b4fd2`. `165c40f` was not opened before this
verdict was written. Deviations owned at the foot.

### Re-run results

- `python3 tools/floor.py --plane ci --root .` — exit 0, all nine scanners
  green; one non-gating size advisory (`docs/ROADMAP.md` 1582 lines over the
  ~300 reference).
- `python3 -m unittest discover -s tools` — 694 tests, OK.
- `node --test instruments/*.test.js` — 207 pass, 0 fail.
- **Pushed-floor boundary, named (the rule's own subject):** this worktree's
  branch has no upstream and HEAD `9aef2983b95…` has **no CI run**
  (`gh run list --commit <sha>` → empty); the newest observable pushed floor
  is green at `94275e6` (main). So every result above is exactly the rule's
  "green locally" state — this verdict cannot claim "floor green at head" for
  the tree it reviewed, and says so.

### Lens 4 discharge

Landed markdown doctrine delta: `/security-review` reaches only pending diffs
and excludes markdown, so its pass here would be definitionally empty — not
run, weighed as nothing. Reviewed by eye instead: the sub-point introduces no
secret, credential, personal-estate detail, or new attack surface; the commit
refs and timestamps it cites are repo-public facts. Discharged.

### Findings

**RF1 (MAJOR) — the mechanism sentence contradicts the repo's own floor
design.**
*Claim:* `docs/method/RECORD.md:113-115` asserts "CI runs checks a local scan
does not — reviewscan over what the push itself queued, the harvest gate a
pushed `[x]` trips". The repo's artefacts say otherwise. *Evidence:*
`tools/floor.py --list --plane hook` and `--plane ci` serve the identical
nine-scanner registry (ADR 0008's one-registry design); the pre-commit hook
(`tools/pre-commit.sample:65`) runs that registry over the whole tree at
every commit, so reviewscan and the sizescan harvest gate ARE local checks —
a tree carrying an un-harvested `[x]` cannot pass a firing hook. Where the
planes differ, CI is the *weaker* cover: `.github/workflows/ci.yml`'s header
states leakscan runs structural-only in CI and full cover "is where the
pre-commit hook on a real machine" lives. The named example is also off
target in a second way: reviewscan reads decision records only and
deliberately does not lint ROADMAP (`tools/reviewscan.py`, scope note), so "what
the push itself queued" (a `⏳` pointer) is outside its scope as written. The
real gap is *when the check ran and over what tree*: a green observed before
the close's final commits, or on a path where the hook never fired
(`--no-verify`, a hook-less clone — the exact backstop rationale
`docs/method/ECONOMICS.md:143-145` gives for every-push CI). A hook-covered
close cannot exhibit the divergence this sentence describes. *Counsel:* keep
the operative rule (it is right regardless — see "What held"); reword the why
to name tree-state timing and hook-cover gaps. As written it sends a fixer
after "checks missing locally", which cannot be the fix because nothing is
missing, and a wrong why in doctrine propagates to every adopter who reads it.

**RF2 (MINOR) — the pending state has no durable home or owner.**
*Claim:* "or names it as pending" (`RECORD.md:117-118`) is honest but lands
only in the close *message* — and chat is volatile
(`docs/method/CONCURRENCY.md:386-388`); the next session reads the session
index, not the chat. A fully compliant "pending" close whose run then reds
reproduces the grounded harm — inherited debt — minus only the overclaim.
*Counsel:* require the pending state (with the head SHA awaited) to land in
the session entry, so a red run has a discoverable owner rather than a
surprised inheritor.

**RF3 (MINOR) — no named observation mechanism, and waiting is unweighed.**
*Claim:* the rule never says how a session gets the pushed run's result, and
treats "pending" as a coequal branch when the floor is zero-dep and completes
in about two minutes. *Evidence:* no file in `docs/method/`, `docs/build/`,
or `tools/README.md` names `gh run list`/`gh run watch` (grep, 2026-07-26);
demonstrated live in one command — `gh run list --commit <sha>` returned
green for `94275e6`, empty for unpushed `9aef298`. *Counsel:* one sentence
naming the command and making wait-for-the-run the default when the run is
minutes away, with "pending" the honest exception (capacity outage, a close
the principal wants immediately).

**RF4 (MINOR) — "floor at head" is undefined where the inherited rule lands
without an every-push floor.**
*Claim:* children inherit this rule by pointer
(`docs/build/templates/CLAUDE.md:53-57`; `docs/method/PROPAGATION.md:136-138`)
while `docs/method/ECONOMICS.md:146-150` sanctions trimming a private child's
floor to main-only — there a branch-push close triggers no run to carry *or*
await, ever, and both of the rule's branches presuppose one will exist.
*Counsel:* scope the evidence bar to "the strongest run the push actually
triggers", naming the no-run case honestly rather than leaving the child to
improvise.

**RF5 (MINOR) — "floor" resolves to the wrong referent via the glossary.**
*Claim:* `docs/method/GLOSSARY.md:60` defines **Floor** as the inlined
doctrine subset a child carries; the sub-point uses "floor" in the CI
scanner-run sense with no link, so the cold adopter the glossary exists for
resolves the term to the wrong thing. *Counsel:* name it "the CI floor run
(`.github/workflows/ci.yml`)" on first use, or give the glossary the second
sense.

### What held

- **The evidence bar itself (lens 1's core):** pushed-floor-at-head is the
  right bar — it is the apex's claim-never-past-evidence applied at close,
  and the operative instruction survives RF1 untouched.
- **An honest waiting state exists and is phrased usably** ("green locally,
  floor run pending") — RF2/RF3 sharpen it; they do not find it absent.
- **Sibling coherence:** no sibling still teaches local-scan-as-all-clear
  (grep across `docs/method/` and `docs/build/`); `AUTONOMY.md:59`'s
  pre-push secret-scan is a complementary pre-push floor, not a conflict;
  CONCURRENCY's queue-run report inherits this all-clear cleanly by pointer
  (`CONCURRENCY.md:518-519`), so the sub-point reaches orchestrated runs
  without restatement.
- **Placement:** nested under "The all-clear carries its evidence" is the
  correct home — it is that rule's push-case instantiation.
- **AWA2 honoured:** `97b4fd2` lands the rule and queues its rule-4 pointer
  in the same commit (the ROADMAP hunk in the delta) — no unpointed window.
- **Record hygiene:** absolute UTC date, commit-ref grounding, why-dense
  body — house style throughout.

### Verdict

**PASS-WITH-FINDINGS — 1 MAJOR (RF1), 4 MINOR (RF2-RF5).** The rule is
right; its stated mechanism is wrong against the repo's own artefacts, and
doctrine's why-sentences propagate as hard as its rules. Findings are
counsel; the decisions are the principal's (REVIEW.md rules 3-4). Nothing
was applied.

**Deviations owned:** none of substance. One tooling slip during evidence
gathering — a first `gh run list --commit` call used a wrongly-completed
full SHA and was discarded and re-run with `git rev-parse HEAD` before any
conclusion was drawn. The `gh run list` calls were read-only network reads
made to demonstrate the rule's own observability boundary.

## Reconciliation — after opening the deferred section (2026-07-26, UTC)

Deferred material read: the brief's deferred paragraph and
`git show 165c40f` (the fix commit the sub-point cites as grounding). The
withdrawn-directory ban was honoured in this phase too.

- **RF1 sharpened, one sub-claim withdrawn.** Sharpened: `165c40f` confirms
  the incident's red checks were reviewscan and sizescan's cold-content
  gate — both in the shared hook/CI registry — and that the tree stayed red
  through "every push after" 00:06 UTC, so commits kept landing on a
  locally-detectable red: hook cover was not firing on those paths. That is
  RF1's diagnosis (timing and hook cover, not CI-exclusive checks) confirmed
  by the grounding itself; the fix commit even says "both scanners re-run
  green locally". Withdrawn within RF1: my reading of "what the push itself
  queued" as the ROADMAP `⏳` pointer (outside reviewscan's scope) — the
  offender was the billing-state *decision record* missing its
  machine-visible Review line, which is inside reviewscan's scope. The
  example is grounded; that my cold reading went elsewhere is small further
  evidence for the reword counsel, but the "doubly off target" clause of RF1
  is withdrawn. RF1's severity and core claim stand.
- **RF2 sharpened.** `165c40f` shows the inheritor re-derived the debt from
  the red floor alone, roughly an hour on — the unowned-pending shape RF2
  names, now with its grounded instance attached. Unchanged in substance.
- **RF3, RF4, RF5 unchanged.** Nothing in the deferred material bears on
  observability mechanics, trimmed-floor children, or the glossary referent.
- **No findings added.** The deferred paragraph carries no evaluative
  framing beyond what the commit message of `97b4fd2` already stated.

Verdict after reconciliation: **PASS-WITH-FINDINGS — 1 MAJOR, 4 MINOR**
(unchanged).
