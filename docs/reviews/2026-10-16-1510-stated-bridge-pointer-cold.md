# Cold pass — SECRETS' stated-bridge pointers repointed to PRINCIPLES

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus brief-writer;
the pass waits for a further cold Fable session that neither the delta's author nor this
brief-writer (nor its orchestrator) started or instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/570-rule-4-cold-pass-queued-stated-bridge-pointer.md`.
**Why it earns a review:** SECRETS makes a standing credential, and a store with no read trail,
acceptable only as a named bridge; the citation is how a reader finds what a bridge obliges. A
citation that lands on the wrong rule, or misses a site, leaves that obligation unfindable. A
small delta: keep the review proportionate.

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

- `338ff6d` (2026-10-03) — secrets: the stated-bridge rule lives in PRINCIPLES, so point there
  (200/100 C6)

Delta path: `docs/method/SECRETS.md`, two citations — one closing the paragraph on standing
credentials as a tracked debt, one in the detection duty about a store with no read trail.

## Scope

Widest the work admits; the lenses organise it, they do not bound it. Non-goals are the only
narrowing and are themselves reviewable.

Probe, at least:

- **Fit at each site.** Read the cited rule in `docs/method/PRINCIPLES.md` (§7, *Codify before you
  converge; a hand-action is only a stated bridge*) and say, per SECRETS site, what kind of thing
  the site calls a bridge and whether the cited rule obliges what that site needs. Compare any
  other candidate home — for example §5's *Secure by default*, which refers to "the same 'stated
  bridge' grammar §7 gives".
- **The old home.** Confirm by search that `docs/method/DATA-PROTECTION.md` holds no such rule at
  HEAD, and say whether it ever did (`git log -S`).
- **Every site.** List every occurrence of "stated bridge" and every `DATA-PROTECTION.md`
  citation in SECRETS and its neighbours (`ACCESS.md`, `AUTONOMY.md`, `PRINCIPLES.md`,
  `GLOSSARY.md`). For each, say which rule it means and whether its citation (or lack of one)
  takes a reader there.
- **Citation form.** The new citations quote a phrase and name a file, with no section number or
  anchor. Is the quoted phrase verbatim, and would the citation survive the heading's rewording?

**Non-goal:** the stated-bridge doctrine itself; where SECRETS points for it, and whether that
place says what SECRETS relies on, is the subject.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Ask whether
   "the stated-bridge rule" is one rule with one home, or a grammar used in several places.
2. **Correctness & quality.** Diff `338ff6d`. Record the per-site table from *Scope*.
3. **Completeness / harvest.** The sweep above; a mis-cited rule found once is a class to sweep.
4. **Security & privacy** — mandatory. SECRETS is security doctrine. Say whether a reader who
   follows each citation ends up knowing that a standing credential must stay listed, dated and
   tightened, not merely tolerated. No code surface: `/security-review` is discharged by grounds.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `grep -n -i 'stated bridge\|stated-bridge\|DATA-PROTECTION' docs/method/*.md`, read in full
- `git log -S 'stated-bridge rule' --oneline` across the tree
- `python3 tools/linkscan.py --root . .` and `python3 tools/pathscan.py --root . .`
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`)

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
`docs/roadmap/160-doctrine-review-owed/570-rule-4-cold-pass-queued-stated-bridge-pointer.md`, the
sibling `docs/reviews/2026-10-16-1510-stated-bridge-pointer-cold.deferred.md`, the landing
commit's message body (the author's account; read subject, stat and diff only), and the
commissioning item
`docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md`.

Sweep with `python3 tools/coldsweep.py --root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/570-rule-4-cold-pass-queued-stated-bridge-pointer.md
--also-exclude docs/reviews/2026-10-16-1510-stated-bridge-pointer-cold.deferred.md
--also-exclude
docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is never
barred; the author's narrative of why, and the verdicts that recorded it, are.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Append your verdict
below a `---` divider in THIS file: provenance repeated (how you were spawned, your tier, what you
read), per-lens answers, findings with stable IDs (prefix `BR`: `BR1`, `BR2`, …) and severities
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

# Verdict — phase 1 (2026-10-17 10:27 UTC)

## Provenance, repeated

- **Reviewer:** a fresh `claude-fable-5-1` subagent (Fable tier, the principal-named review tier;
  checked at selection against the brief's tier line). Spawned 2026-10-17 by a Fable orchestrator
  running the 2026-10-17 review batch from a user-local prompt file; that orchestrator authored
  neither the delta nor this brief, and holds the sibling out of reach until phase 1 is committed.
  Neither the reviewer nor its orchestrator was started or instructed by the delta's author (the
  2026-10-03 queue run) or by the brief-writer. Rule 4's criterion is met; no off-tier condition
  applies.
- **Worktree:** `/Users/mike/worktrees/atelier-review-1017`, branch `review-1017`, HEAD `07c62ea`,
  which carries `8acfff1` (verified with `merge-base --is-ancestor`). Read-only to me except this
  file; no git write run. No scratch clone was needed — every probe ran against HEAD and
  read-only history.
- **What I read:** this brief; the delta commit's subject, `--stat` and diff on
  `docs/method/SECRETS.md` (body not opened); `SECRETS.md` in full at HEAD; `PRINCIPLES.md` §5
  and §7, the trade-off table and the heading list; `ACCESS.md` steps 2–7; `GLOSSARY.md`
  headings and entry list; `REVIEW.md` § *The standing checklist*; `DATA-PROTECTION.md` headings;
  scanner usage lines in `.githooks/pre-commit`, `.github/workflows/ci.yml` and `tools/floor.py`;
  `tools/linkscan.py`'s docstring. Grep hits only from `CHANGELOG.md` (two 2026-07-23 entries) and
  the generated `docs/ROADMAP.md` index line that carries the queue pointer's title (the title
  this brief already states; nothing evaluative).
- **Exposure, disclosed:** `git log -S` on the tree listed the *subjects* of three record commits
  (two reviews-folder commits and one records commit) alongside the delta; none was opened. No
  barred path was opened; coldsweep ran without `--include-barred`.

## Lens 1 — approach and assumptions

Load-bearing assumptions, named first:

1. That "the stated-bridge rule" has a single home. **Probed:** it is a *grammar* with one home and
   many applications. The home is `PRINCIPLES.md` §7's bullet *Codify before you converge; a
   hand-action is only a stated bridge* (line 265). §5's *Secure by default* explicitly borrows it
   ("the same 'stated bridge' grammar §7 gives a hand-action"), the trade-off table restates it
   twice (*Codified or hand-done?*, *Standing or ephemeral credential?*), `ACCESS.md` step 5 applies
   it to the one-broad-credential fallback, and SECRETS applies it at four sites. So pointing
   SECRETS at PRINCIPLES is right, and pointing at §7 is right for the grammar's name.
2. That §7's rule obliges what each SECRETS site needs. **Probed, partly false:** §7 offers two
   shapes — a *logged, temporary* bridge carrying a follow-up to codify, or a *documented permanent
   exception where codifying is genuinely unsafe*. None of SECRETS' four bridges is a hand-action
   awaiting codification, and none is permanent because codifying is *unsafe*; each is a gap the
   *platform or technology* imposes (no JIT grant; a length cap; a transcription constraint; no
   read trail). The obligation SECRETS actually relies on — name it, list it, keep tightening it,
   never let it be the silent steady state — is stated for exactly these cases in §5 (the
   credential bullet's *Honest pattern*; Zero Trust's *name the gap … a stated, tracked debt, not a
   silent miss*). §7 gets a reader to the grammar; §5 is where the credential case is spelled out.
   See BR2.
3. That the old citation once pointed somewhere real. **Probed, false:** `DATA-PROTECTION.md` has
   never held the word "bridge" in any revision (`git log -i -S bridge` on that path returns
   nothing). The 2026-07-10 citation was wrong from birth, so this delta corrects a defect, not a
   move.
4. That the delta swept its class. **Probed, false:** one site survives. See BR1.

## Lens 2 — correctness and quality

Diff of `338ff6d` on the delta path: two hunks, each replacing a `DATA-PROTECTION.md` citation with
a `PRINCIPLES.md` one. Hunk 1 (line 76) adds a quoted phrase; hunk 2 (line 270) names the file
only. The quoted phrase *a hand-action is only a stated bridge* is verbatim against PRINCIPLES
line 265. Both new citations resolve to a file that holds the rule. Correct as far as they go.

**Per-site table** (every "stated bridge" in SECRETS and its neighbours at HEAD):

| Site | What it calls a bridge | Cited home | Takes a reader to the rule? |
|---|---|---|---|
| SECRETS:76 (delta) | a standing credential the platform can't make JIT — a debt to shorten | `PRINCIPLES.md` + verbatim §7 phrase | Yes: the phrase is searchable and lands on §7. The credential case itself is in §5, uncited (BR2). |
| SECRETS:158 (**not** in delta) | a platform-imposed length cap, recorded beside the mint procedure | `DATA-PROTECTION.md` | **No.** That file has never held it (BR1). |
| SECRETS:167 (not in delta) | break-glass transcription-optimised minting, "like any imposed cap" | none — chains to :158 | No: the chain ends at the wrong file (BR1). |
| SECRETS:270 (delta) | a store with no read trail — a limitation weighed at store choice | `PRINCIPLES.md`, bare | File-level only: no phrase, no §; a reader searches 584 lines for "bridge" (BR3). |
| PRINCIPLES:183 (§5) | opening any new surface | "grammar §7 gives" | Yes, by § number. |
| PRINCIPLES:265 (§7) | a live hand-fix before codification | — (the home) | — |
| PRINCIPLES:572, 575 | hand action; standing credential | implicit (§5 cited at :575) | Yes, same file. |
| ACCESS:72 | the one-broad-credential fallback | none | Only if the reader already knows the term (BR4). |

Every remaining `DATA-PROTECTION.md` citation in SECRETS (lines 59, 280, 297, 345) and in ACCESS
(lines 11, 15, 40, 55, 61, 101) names a rule that file does hold (smallest irreplaceable set,
verified restore, read before write, encode the gate, sensitive topology); none is a bridge
citation. The miss is confined to the bridge class.

## Lens 3 — completeness and harvest

Tree sweep (`coldsweep`, barred set plus the three `--also-exclude` paths): ten hits for
"stated bridge" over 641 files — the eight doctrine sites tabled above, two `CHANGELOG.md` entries
and the roadmap index line. No skill, template or README mirrors the SECRETS text, so there is no
child-facing copy to sweep (V3 beyond the three doctrine files: nothing to bite on). A second sweep
for a `DATA-PROTECTION.md` citation within 40 characters of "bridge" returned zero hits because
SECRETS:157–158 breaks across a line; the line-by-line grep in the re-run ledger is what found it.
The class the brief predicted — a mis-cited rule found once — has exactly one unswept member.

## Lens 4 — security and privacy (mandatory)

- `/security-review`: **discharged by grounds.** It reads this session's pending diff, which is
  the other two reviewers' drafts and the orchestrator's partition, not this delta; and the delta
  has no code surface (two prose citation strings in a doctrine file).
- Hand read against OWASP: the Top 10 categories (A01–A10) have nothing to bite on in a citation
  change. The OWASP *Secrets Management* cheat sheet SECRETS itself cites is the relevant catalogue:
  its audit-trail leg is the one SECRETS:270 qualifies as a named limitation, so the security
  question is whether that qualification stays reachable. It does at file level (BR3 for the
  anchor).
- The brief's question — does a reader following each citation end up knowing that a standing
  credential must stay **listed, dated and tightened**, not merely tolerated? From SECRETS:76 →
  §7: *logged* (listed), *carrying a follow-up* (tightened), and §7's own "undated hand-state is a
  future lie" (dated) — yes, though phrased for a hand-action, and the credential-specific wording
  sits one section earlier in §5. From SECRETS:270 → bare `PRINCIPLES.md`: only if the reader
  searches. From SECRETS:158 → `DATA-PROTECTION.md`: **no** — the obligation is unfindable from
  that site, which is the exact defect the commit set out to remove.
- Privacy: the diff carries no personal data; `leakscan` and `secretscan` are clean at HEAD (floor
  ledger below). This verdict quotes no secret, token, address or person.

## Standing checklist V1–V7

- **V1** — the commit subject's claim "the stated-bridge rule lives in PRINCIPLES" is true and
  re-driven (§7 line 265 at HEAD); its implied claim that SECRETS now points there is two-thirds
  true (BR1). Discharged with the finding.
- **V2** — no "live-proven"/"verified" claim in the delta; the old home's emptiness and the phrase's
  verbatim status were re-driven rather than read. Discharged.
- **V3** — the changed citation was not swept to every site in the same file (BR1); no mirror site
  exists outside `docs/method/`. Finding recorded.
- **V4** — SECRETS:70–76 restates §5's *tracked debt to shorten, not a resting state* verbatim,
  unstamped; pre-existing since 2026-07-10, outside the delta (BR5, note).
- **V5** — SECRETS now cites two different files for one grammar (BR1). Finding recorded.
- **V6** — lens 4 above. Discharged with grounds.
- **V7** — provenance stated in the brief and repeated above. Discharged.

## Findings

**BR1 — MODERATE. One of three `DATA-PROTECTION.md` bridge citations in SECRETS was left
standing.** `docs/method/SECRETS.md:157–158` still reads "An imposed cap is a stated bridge
(`DATA-PROTECTION.md`)", and line 167 chains to it ("like any imposed cap") with no citation of
its own. `DATA-PROTECTION.md` has never contained the word "bridge" in any revision, so a reader
who follows that citation finds nothing — the defect the commit named in its subject persists at
the minting site, and SECRETS now disagrees with itself about where the grammar lives (V3, V5).
*Probe:* `grep -n -i 'stated bridge\|stated-bridge\|DATA-PROTECTION' docs/method/*.md`;
`git log -i -S bridge -- docs/method/DATA-PROTECTION.md` → empty; `git log -S 'An imposed cap is
a stated bridge'` → added 2026-07-22 (`caa85fe`), untouched by `338ff6d`. *Counsel:* repoint
line 158 in the same form the principal settles for the other two sites (BR3), which also
repairs line 167 by its chain.

**BR2 — minor. The cited rule's two shapes do not include the shape SECRETS uses.** §7 licenses
a bridge that is *temporary pending codification* or *permanent because codifying is unsafe*.
SECRETS' four bridges are permanent-until-the-platform-changes: nothing is awaiting codification
and nothing is unsafe to codify. The obligation SECRETS relies on for these — stated reason, on a
list, kept tightening, weighed at technology choice — is written for the credential case in §5
(*Honest pattern*; Zero Trust's *name the gap*), which the delta does not cite. A reader at §7
can wrongly conclude a standing credential is a temporary bridge owing a codification follow-up.
*Probe:* read of §5 lines 180–219 and §7 lines 265–275 against SECRETS lines 70–76, 157–158,
167–168, 268–271. *Counsel:* cite both — §7 for the grammar's name, §5 for the credential and
name-the-gap cases. Whether §7's bullet should itself name the platform-imposed shape is a
doctrine question outside this pass's non-goal; it is the principal's to raise as a board item.

**BR3 — minor. Citation form: one site is anchored by a quotable phrase, the other by nothing,
and neither by the § number PRINCIPLES promises to keep stable.** SECRETS:270 cites bare
`PRINCIPLES.md`. SECRETS:76 quotes a verbatim phrase with no section. PRINCIPLES §7's own preface
says "positions here are stable so §N citations hold", and SECRETS already cites PRINCIPLES by
number at line 15 (§10). Neither scanner guards the new form: `linkscan` checks Markdown links and
`#fragment` anchors, `pathscan` only that `PRINCIPLES.md` exists, so a reword of the §7 heading
would silently orphan the phrase citation and nothing would ever catch the bare one. *Probe:*
`tools/linkscan.py` docstring; `linkscan` and `pathscan` runs below (clean on the delta either
way). *Counsel:* `PRINCIPLES.md §7` plus the phrase at every SECRETS bridge site, matching line 15's
house form.

**BR4 — note. "Stated bridge" is a load-bearing term with no glossary entry.** Eight sites across
three doctrine files use it; `GLOSSARY.md` (18 entries) does not define it, and `ACCESS.md:72` uses
it with no citation at all. Outside the delta; recorded as harvest for the principal.

**BR5 — note. A verbatim restatement without a stamp.** SECRETS:72 repeats PRINCIPLES §5's "tracked
debt to shorten, not a resting state" word for word (since `85d3573`, 2026-07-10), and the §5
trade-off row at PRINCIPLES:576 says it a third time. One fact, three homes, none stamped (V4).
Outside the delta; recorded as harvest.

## Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 1 MODERATE · 2 minor · 2 note.**

The two citations the delta touched are correct and resolve; the delta's own class is one site
short of swept, which is the one finding that leaves an obligation unfindable.

## Re-run ledger

All from the worktree root, one at a time, under `nice -n 10`; machine load 8–51 during the run.

| Command | Result |
|---|---|
| `git show --stat` + `git show -- docs/method/SECRETS.md` on `338ff6d` (subject, stat, diff) | 4 files; 2 hunks on the delta path, as the brief describes |
| `grep -n -i 'stated bridge\|stated-bridge\|DATA-PROTECTION' docs/method/*.md` | 24 lines; the bridge hits tabled above; SECRETS:157–158 found |
| `git log -S 'stated-bridge rule' --oneline` | 5 commits: `85d3573` (added), `338ff6d` (removed), three record commits (subjects only) |
| `git log -i -S bridge -- docs/method/DATA-PROTECTION.md` | empty — never held it |
| `git log -S 'An imposed cap is a stated bridge' -- docs/method/SECRETS.md` | `caa85fe` 2026-07-22 only |
| `coldsweep --root . <3 × --also-exclude> -i 'stated[ -]bridge'` | 10 hits / 641 files; 396 barred files excluded; no `--include-barred` |
| `coldsweep … 'DATA-PROTECTION\.md.{0,40}bridge\|bridge.{0,40}DATA-PROTECTION'` | 0 hits (line break at SECRETS:157–158 defeats a single-line pattern; see grep above) |
| `python3 tools/linkscan.py --root . .` | clean, exit 0 |
| `python3 tools/pathscan.py --root . .` | 70 findings, exit 1 — none on `docs/method/`'s delta files; warn-only on both planes |
| `python3 tools/floor.py --plane ci --root .` | exit 0: 12 enforced checks green (secretscan 23 advisory, non-blocking; leakscan clean); 4 warn-only checks reported, pathscan 2 findings off the delta |
| hook plane | not re-run by me: it reads the staged index, which holds the orchestrator's partition, not this delta; it binds at the orchestrator's commit of this file |
| Python suite / node tests | not run — the brief's re-run list does not name them, and the delta touches no code |

## Follow-up checklist (principal's; nothing applied)

- [ ] BR1 — repoint `SECRETS.md:158` (and by chain :167) from `DATA-PROTECTION.md` to PRINCIPLES.
- [ ] BR3 — settle the citation form (`§7` + phrase counselled) and apply it at all four SECRETS sites.
- [ ] BR2 — add the §5 cross-cite at the credential and no-read-trail sites; decide whether §7's
      bullet should name the platform-imposed shape (board item if so).
- [ ] BR4 — a `GLOSSARY.md` entry for *stated bridge*; a citation at `ACCESS.md:72`.
- [ ] BR5 — stamp or dedupe the three copies of *tracked debt to shorten, not a resting state*.
- [ ] Phase 2: reconcile against the sibling once this file is committed.
