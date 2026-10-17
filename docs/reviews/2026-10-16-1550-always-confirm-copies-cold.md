# Cold pass — the always-confirm floor list's copies match AUTONOMY

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes this pass; a session that cannot honour it stops.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or
instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/620-rule-4-cold-pass-queued-floor-list-membership.md`.
**Why it earns a review:** the always-confirm floor is the list of actions an
agent must stop and ask before taking, whatever its grant; a session that reads
a copy missing a member proceeds where it should stop, and the apex is the first
document every session reads.

## Spawn provenance

- **Author of the work under review:** the queue run whose intent record is
  dated 2026-10-03 01:44 UTC (path in the sibling; not opened by this writer),
  which landed the commit under *What the work is*. The commit carries an Opus
  co-author trailer.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched by the
  Mike-opened Opus queue-run session `abe96d8d` on 2026-10-16 UTC, on Mike's
  answer that day that a fresh Opus session writes these briefs. Neither it nor
  its orchestrator authored, started or instructed the authoring run, and
  neither edited the delta. It is **off-tier for review, disclosed: it forms no
  finding and writes no severity**, and it stopped after this brief and its
  sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that
  passes rule 4's criterion. It repeats its own provenance in its verdict and, if
  it runs under an orchestrator, discloses that shape as rule 4 requires.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This writer
  read: the queue pointer in full; the landing commit's subject, `--stat`,
  message body (the author's own account of why, which names one AUTONOMY stop
  it chose not to add) and diff; grep hits for the floor-list terms across the
  tree (records excluded) and the matching lines of `AUTONOMY.md`,
  `PROPAGATION.md`, the child `CLAUDE.md` template and the session-onramp skill;
  `REVIEW.md` down to § *Whether work earns a review*; the ask halves, above the
  first divider, of two 2026-10-04 briefs as format models; filename listings of
  `docs/reviews/` and `docs/roadmap/`, and path greps over `docs/reviews/` that
  name prior verdicts without reading them; and its auto-loaded cross-session
  memory index. Its orchestrator read the `docs/SESSIONS.md` index tail (entries
  through 2026-10-16, including the authoring runs' one-paragraph summaries) and
  the 2026-10-16 session record's close section, and passed this writer nothing
  evaluative beyond the pointer list. What this writer suspects is in the sibling.

## What the work is

Landing commit (diff it; review the paths at HEAD):

- `7c2ab8b` (2026-10-03) — apex: the always-confirm list names unapproved tools in
  every copy (200/100 C7)

Delta paths: `docs/method/00-APEX.md` (two inline floor lists, in § on the
principal's authority) and `docs/method/README.md` (item 3, the `AUTONOMY.md`
summary). No later commit has touched either path.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether every statement of the floor in this repo, and in what it stamps into
children, names the same members as the canonical list — and whether the three
edited lists now do. Read `AUTONOMY.md`'s floor at HEAD and treat it as the
reference. Then find every copy yourself — prose lists, stamped blocks,
templates, skills, the onramp, tool docstrings, ADRs, `README.md`,
`CHANGELOG.md` — and build a membership matrix (floor member × copy), marking
each copy as stamped (watched by `stampscan`/`blockscan`) or free text, and as a
full list or a declared summary. For each of the three edited lists, read the
sentence it sits in and say what kind of text it is (narrative, a summary, a
ruling's restatement) and whether the edit leaves that text saying what its
attribution says. Test the words themselves on cases: a session about to add a
CI secret, enable a GitHub App, install a CLI from a package manager, add an MCP
server, start a deploy-on-push to an already-public site with a new content
class, or rotate a key that locks out a second machine. Does each copy route
each case to the same answer?

**Non-goal:** which actions belong on the floor (`AUTONOMY.md`'s membership is
ruled doctrine). It is read as the reference, and any internal inconsistency in
it is in scope as a finding.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Is "every copy matches AUTONOMY" the right invariant for a summary that says
   "Repos may narrow"? Should a copy enumerate the floor, or point at it?
2. **Correctness & quality.** The matrix. Wording drift between copies of the same
   member ("a new trust surface" against "adding a new trust surface (deploy
   keys, webhooks, OAuth/app grants)"); whether "unapproved" is defined — who
   approves a tool, and where is approval recorded? The commit's account of the
   one stop it did not add is a claim: test it against `AUTONOMY.md`'s own text.
3. **Completeness / harvest.** Copies the commit did not touch that differ from
   the reference after it; any doc that names the floor by a count ("seven
   stops"); whether `stampscan` and `blockscan` watch every copy that is meant to
   be a stamp, and whether an unstamped copy should be one (V3, V4).
4. **Security & privacy** — mandatory and central: the floor is the
   security-and-safety stop list. Hunt for any path by which a session reading
   only one copy installs a tool, grants an app, adds a credential or widens an
   audience without asking. Code altitude: none in the delta (prose), but if a
   tool's docstring carries the list, read it. `/security-review` is discharged by
   grounds — a landed prose delta; the session's pending diff is other passes'
   drafts — say so.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- the floor on both planes at HEAD (`python3 tools/floor.py --plane hook --root
  <root> --tools <root>/tools`, then `--plane ci --root <root>`), exit codes read
  explicitly
- `python3 tools/stampscan.py --warn --root . .`, `python3 tools/blockscan.py
  --check --warn --root .` and `python3 tools/blockscan.py --against 7c2ab8b^
  --warn --root .`
- the matrix's grep, recorded so it re-runs, with its exclusions stated

## House rules for this run

- Name your own worktree in the verdict. Run **no git command that writes** there;
  read-only git (`log`, `show`, `diff`, `blame`) is fine. Probes and checkouts of
  older commits go in a private clone under your scratchpad, named by your prefix.
- One heavy process at a time on a shared machine: the full Python suite at most
  once, foreground. Never point a scanner at another repository on the machine.
- `/security-review` reads the session's pending diff. Discharge it by grounds for
  this landed delta and do the code-altitude read by hand against the OWASP
  catalogue, or keep the tree clean whenever you spawn it.
- Absolute ISO-8601 dates from `date -u`. Prose wrapped at ≤ 100 columns. NZ
  English. Never quote a secret, placeholder token, email address or personal
  detail — the repo is public; describe and locate instead.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md beside this brief under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer named
above, this brief's sibling (same path, `.deferred.md`), and the commissioning
item `100-r2-found-eleven-live-contradictions.md` with every other item under
`docs/roadmap/200-anti-slop-invariant-registry-promote-rec/`.

Sweep with rule 2's default bar plus these (`<root>` is your worktree):

```sh
Q=docs/roadmap/160-doctrine-review-owed
python3 tools/coldsweep.py --root <root> \
  --also-exclude $Q/620-rule-4-cold-pass-queued-floor-list-membership.md \
  --also-exclude docs/reviews/2026-10-16-1550-always-confirm-copies-cold.deferred.md \
  --also-exclude docs/roadmap/200-anti-slop-invariant-registry-promote-rec \
  <pattern>
```

`--include-barred` only with disclosure in the verdict. The delta and the doctrine
it must agree with are never barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, findings with
stable IDs (prefix `FM`: `FM1`, `FM2`, …) and severities (MAJOR / MODERATE /
minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger with commands and results, and a follow-up checklist. Commit it
before opening the sibling. If an orchestrator holds the sibling outside the
tree, it releases it on your committed findings.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict:
per-finding notes against its seeded questions and the intent record, any finding
formed at reconcile marked as such, and the overall line restated. Never revise
phase-1 text. Fold the sibling in below the reconcile and delete it.

Findings on doctrine are the principal's to decide (rule 3): record all, apply
nothing; counsel per finding is welcome, labelled as counsel.

---

## Verdict — phase 1 (2026-10-17 UTC)

### Provenance, repeated

- **Reviewer:** a fresh `claude-fable-5-1` subagent, on the Fable tier the pass names, spawned
  2026-10-17 by a Fable orchestrator that authored neither the delta nor this brief and holds
  the sibling outside the tree until these findings are committed (the context-partition shape
  rule 1 calls structural; disclosed here as rule 4 requires). The reviewer neither started nor
  was instructed by the authoring run. Finding prefix `FM`. Worktree
  `/Users/mike/worktrees/atelier-review-1017`, branch `review-1017`, HEAD `07c62ea` (carries
  `8acfff1`, checked with `merge-base --is-ancestor`). No git write was run; the one scratch
  clone sits under the session scratchpad, named by prefix, checked out at `7c2ab8b`.
- **Read:** this brief; `AUTONOMY.md`, `00-APEX.md`, `README.md` (method), `PROPAGATION.md`,
  `REVIEW.md` (rules, lenses, V1–V7), `TOOLBOX.md` §§ expected toolbox and install rule,
  `GLOSSARY.md` roles and floor entries; the landing commit's **subject, `--stat` and diff
  only**; the child template's stamped block; `skills/session-onramp/SKILL.md`;
  `tools/blockscan_map.json`; the heads of `stampscan.py` and `blockscan.py`; the wiring lines of
  `.githooks/pre-commit` and `ci.yml`; context lines around every sweep hit outside the barred
  set; `git log` dates for when each member arrived in each file.
- **Not read, by the run's rules:** the landing commit's message body (the orchestrator barred
  it with the records until phase 2, so lens 2's "the one stop it did not add" was tested
  structurally — which members the edited copies still lack — not against the author's
  account); every path `coldsweep` bars plus the three `--also-exclude` paths above; the
  sibling. No `--include-barred` sweep was run. No other `docs/reviews/2026-10-16-15*` file was
  opened. The auto-loaded cross-session memory index was in context, as for every session.

### The reference, as read

`AUTONOMY.md` § *Always confirm* at HEAD (`89ff0d8` was the last change, 2026-10-06; the member
list itself last moved 2026-07-10) names ten bullets. Nine are members; the *recoverability
ends at push* bullet is a clarification joining making-public to secrets, not a class of its
own. For the matrix: **A** making a private thing public (visibility, collaborator, widening
an audience, external send) · **C** truly destructive or irreversible · **D** lockout-class ·
**E** widening your own authority · **F** new trust surfaces · **G** secrets · **H** spend ·
**I** people and safety (including merging other people's work) · **J** installing an
unapproved tool · **K** deploy-on-push when it isn't routine. F and J each call the other "the
same class", which is why every copy counts eight where the reference counts ten bullets.

### Membership matrix

`✓` named · `~` named narrower than the reference · `✗` absent.

| # | Copy | Kind | Watched by | A | C | D | E | F | G | H | I | J | K |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R | `AUTONOMY.md` § Always confirm | canonical | nothing | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| R′ | `AUTONOMY.md` "The one rule" quote | headline summary, free | nothing | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ |
| 1 | `00-APEX.md` ll. 85–88 (reserved decisions) | restatement, free | nothing (it is a blockscan *source*) | ~ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ~ | ✓ | ✗ |
| 2 | `00-APEX.md` ll. 112–114 (re-brief order) | ruling's restatement, free | nothing | ~ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ~ | ✓ | ✗ |
| 3 | `docs/method/README.md` item 3 | declared summary, free | nothing | ~ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| 4 | `PROPAGATION.md` floor region | canonical region (stamp source) | blockscan, against the APEX section only | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| 5 | `docs/build/templates/CLAUDE.md` | stamped copy of 4 | stampscan (identical, 93 lines) | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| 6 | `skills/session-onramp/SKILL.md` § 2 | re-formatted copy of 4, free | nothing | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ |
| 7 | `README.md` (root), `skills/queue-run`, `REVIEW.md` rule 3, `CONCURRENCY.md`, `GLOSSARY.md` | pointers | — | — | — | — | — | — | — | — | — | — | — |
| 8 | `DATA-PROTECTION`, `REACH`, `ACCESS`, `SIGNING`, `TOOLBOX`, ADRs 0003/0005/0007 | single-member references | — | consistent with R on the member each names | | | | | | | | | |

Narrowings in rows 1–3: **A** reads "making a repo public" (apex) or "private→public" (README),
dropping the collaborator / widening-audience / external-send half; **I** reads "safety"
(apex), dropping "people". No copy anywhere names **K**, and no copy names I's merging-other-
people's-work clause. No doc states the floor by a count; the only numerals ("4 of 6 floor
items") are historical finding citations in `stampscan.py` and `tools/README.md`.

### Per-lens answers

**1. Approach & assumptions.** Load-bearing assumptions, named by the reviewer: (a) that
`AUTONOMY.md` is the floor's canonical home — true by `PROPAGATION.md`'s own words ("a
narrowing-free restatement of the apex + AUTONOMY floor") and `README.md` item 3's
attribution; (b) that an enumerating copy must name every member, compressing freely but
dropping nothing — the invariant `PROPAGATION.md` § *One statement, stamped copies* states
for any copy ("may compress the parent, never contradict it"); (c) that the commit's job was
membership parity on three copies. "Repos may narrow" in the README summary is about a child's
posture, not a licence for the summary to omit a member, so "every enumerating copy names
every member" is the right invariant. Whether a copy should enumerate at all is the sharper
question: an enumeration is read as the list, so a missing member reads as "not on the floor".
The apex's two lists are hand-maintained free text citing a lossy summary as their source
(FM3); pointing would remove the class of defect this pass exists to find. The commit solved
the right problem on the copies it touched and left the mechanism untouched (FM1).

**2. Correctness & quality.** The three edited lists now carry J in the same words as the block
("installing an unapproved tool"), and each sentence still says what it is attributed to: row 1
is a parenthetical restating the floor inside a sentence about reserved decisions; row 2
restates the principal's 2026-08-17 ruling and lists where the re-brief-before-act order
applies; row 3 is a declared summary of `AUTONOMY.md`. Wording drift between copies is on
members A, F and I: F reads "a new trust surface" (apex), "new trust surfaces" (README), "a new
trust surface (deploy keys, webhooks, OAuth/app grants)" (block, onramp) against the
reference's "deploy keys, webhooks, CI secrets, GitHub app installs, OAuth grants" — the
block's gloss drops "CI secrets", which G catches anyway. "Unapproved" is defined only in
`TOOLBOX.md`: approved means a row in the expected-toolbox table; the table is sessions'
to update (FM4). The one stop the commit did not add: tested structurally, the only reference
member absent from rows 1–3 after the edit is **K**; that is the claim the barred message body
presumably makes, and it is true as far as membership goes — but K's absence is fleet-wide and
dates from the floor's first day (FM1), so "not adding it" kept the copies consistent with each
other and inconsistent with the reference.

**Cases, routed per copy** (`C` confirm · `P` proceed · `?` depends on the reader):

| Case | R | R′ | apex 1/2 | README | block/template/onramp |
|---|---|---|---|---|---|
| add a CI secret | C (F, G) | C (secrets) | C (secrets) | C | C |
| enable a GitHub App | C (F) | ? ("installing" a tool?) | C (trust surface, undefined here) | C | C (app grants) |
| install a CLI via a package manager | C unless in TOOLBOX | C unless approved | C unless approved | C | C |
| add an MCP server | C (J, F) | C (tool) | C | C | C |
| deploy-on-push, already-public site, new content class | **C (K)** | **P** | **P** (repo already public) | ? (private→public) | ? (audience not widened) |
| rotate a key that locks out a second machine | C (D, G) | C (secrets) | C | C | C |
| add a collaborator to a private repo | C (A) | ? ("making private public") | **P** (not "making a repo public") | ? | C (widening its audience) |
| change router config that could sever access | C (D) | **P** | C | C | C |
| merge another person's PR in a shared repo | C (I) | P | P | P | P |

Four cases diverge, and three of the four turn on the apex copies or the reference's own
headline — the two texts a session reads first.

**3. Completeness / harvest.** Copies the commit did not touch and that differ from the
reference after it: rows 4, 5, 6 lack K (as do rows 1–3), and row 6 is unstamped (FM5).
`stampscan` watches exactly one stamped block (row 5 against row 4); `blockscan` watches row 4
against the apex *section* and five other method-doc sections — `AUTONOMY.md` is not in the
map, so the canonical floor can gain or lose a member with no copy asked to move (FM1). The
apex's lists are unwatched in either direction: they are hand-edited free text, and the commit
under review is the proof — it edited them by hand, tripping blockscan's co-change check on
the mapped section without an allow marker (FM6). V3 and V4 are therefore not discharged
clean: the rule changed in one home and the sweep reached three of eight enumerations by hand,
with no mechanism to reach the rest.

**4. Security & privacy.** Design altitude: the floor is the stop list, so every gap above is
a path by which a session reading one copy acts without asking. The live ones: a session
reading only the apex adds a collaborator to a private repo or publishes a new content class
through a deploy-on-push site without a stop; a session reading only `AUTONOMY.md`'s headline
quote changes router or tunnel config without a stop; a session reading `TOOLBOX.md` can make a
tool "approved" by adding a row in the same commit as the work (FM4). Code altitude: the delta
is prose; the two tools whose text carries the list (`stampscan.py` docstring, `tools/README.md`)
carry it only as a historical finding citation, and `blockscan_map.json` carries the bullet
anchor, not the members — no input path, no injection surface, nothing for the OWASP Top 10 or
ASVS to bite on; read by hand against both and discharged on those grounds. `/security-review`
is **discharged by grounds**: the delta landed 2026-10-03, so the session's pending diff is
other reviewers' drafts in this shared worktree, which the scanner must not read; its markdown
exclusion would also make a clean pass empty. Privacy: no personal data, secret, hostname or
private-repo detail in the delta or in this verdict.

### Findings

**FM1 — MAJOR.** The canonical floor has a member no copy has ever carried, and nothing watches
the canonical list against any copy. `AUTONOMY.md` gained *Deploy-on-push, when it isn't
routine* on 2026-07-10 (`1778baa`); the child block was written the same day (`c3676ee`)
without it, the apex lists on 2026-07-14 (`f4356f8`) without it, and no copy has it at HEAD
(matrix column K). The case "new content class on an already-public deploy-on-push site"
routes to *confirm* in the reference and to *proceed* in the apex. The mechanism gap is
structural: `blockscan_map.json`'s `stop-and-confirm` bullet cites only the apex section,
because the block's prose cites `00-APEX.md` and not `AUTONOMY.md`, so a membership change in
the reference demands no co-change anywhere; the apex lists are unstamped and unmapped as
copies. Re-driven: `git log -S` dates above; the blockscan map read in full; the case table.
*Counsel:* two decisions for the principal, in order. First, whether K is its own member or a
sub-case of A ("sending to an external audience") — if a sub-case, fold its wording into A in
`AUTONOMY.md` so the reference and its copies can agree; if a member, every enumerating copy
(rows 1–6) gains it, the stamped ones through the region. Second, add `AUTONOMY.md`
§ *Always confirm* as a second source for the `stop-and-confirm` bullet in the map, so the
reference cannot move silently again. Membership itself is the non-goal and is not decided here.

**FM2 — MODERATE.** The reference disagrees with its own headline. `AUTONOMY.md` § *The one
rule* says "Stop and confirm **only** for the genuinely hard-to-undo:" and names seven classes,
omitting lockout-class (D), new trust surfaces (F) and deploy-on-push (K) that the § *Always
confirm* list beneath it carries. "Only" makes the quote read as the whole floor; the
router-config case routes to *proceed* under it. In scope per the brief's non-goal clause
(internal inconsistency in the reference). *Counsel:* either name every class in the quote or
re-word it as "only for the hard-to-undo — the list below", so the headline points at the
list instead of standing in for it.

**FM3 — MODERATE.** The apex's two inline lists narrow two members against both the reference
and the block they cite, and cite the wrong home. "Making a repo public" drops A's
collaborator / widening-audience / external-send half (the add-a-collaborator case routes to
*proceed* in the apex, *confirm* in the reference and the block); "safety" drops I's "people"
and its merging-other-people's-work clause; row 2 also omits E (widening your own authority)
from the set where re-brief-before-act is mandatory, though `AUTONOMY.md` lists E as a floor
member. Row 1 attributes its list to "`PROPAGATION.md` floor" — the block that
`PROPAGATION.md` § *Check the parent's file first* itself calls "a lossy summary … not
evidence about what the house doctrine says" — while `README.md` item 3 attributes the same
floor to `AUTONOMY.md`. Two homes cited for one fact (V4), and the apex is the first document
every session reads. *Counsel:* replace both inline enumerations with a pointer to
`AUTONOMY.md` § *Always confirm* (row 2 can keep its sentence shape: "where the approval is a
floor stop — `AUTONOMY.md` § *Always confirm* — …"); if an enumeration must stay for
findability, stamp it as a copy of the region so `stampscan` watches it.

**FM4 — MODERATE.** "Unapproved" is defined by `TOOLBOX.md` list membership, and the list is
agent-writable. § *The install rule* makes "not on the list → confirm first" the floor's test,
then its last bullet has a session "update this list in the same commit as the work that
needed it" with no requirement that the new row record the confirmation it rests on (who,
when) — the table has no such column. Read together, the approval record is one the agent
originates, which `AUTONOMY.md` § *Widening your own authority* forbids ("the agent *records* a
grant, never *originates* one"), and `TOOLBOX.md` already records that the list's groups were
an answer, not a ruling (`420/020`). *Counsel:* a row added by a session carries the date of the
confirmation it records, or states that the tool was approved under an existing row's route;
a row without either is a widening and is a floor stop in its own right.

**FM5 — MODERATE.** `skills/session-onramp/SKILL.md` § 2 is a third original of the floor. It
restates the block's floor bullet as a six-item list, carries no `stamp:` markers, is not in
`blockscan_map.json`, and is not among the stamped copies `PROPAGATION.md` § *One statement,
stamped copies* lists (the block, `review-brief`, the reviews-README template). It is the floor
a plugin-only adopter reads first, and the commit's "every copy" did not include it — it
happened to agree because it was written from the block. *Counsel:* either stamp it (which
means the text goes verbatim, since the floor region admits no declared narrowing) or cut the
list to a pointer at the stamped block plus one sentence.

**FM6 — minor.** The landing commit tripped blockscan's co-change check and carries no allow
marker. In a scratch clone at `7c2ab8b`, `blockscan.py --against HEAD^ --warn` reports two
violations (`asking`, `stop-and-confirm`: the mapped apex section changed, the block bullet in
`PROPAGATION.md` and the template did not); `ci.yml` at that commit already ran this step
advisory, so the run printed them and nothing answered. The substance was fine — the block
already named J — so the right act was a scoped `blockscan:allow:` with that reason; an
unanswered advisory is the alarm-fatigue class `PROPAGATION.md` point 4 warns about. Still
reported at HEAD by the brief's own `--against 7c2ab8b^` invocation. *Counsel:* add the marker
with the reason on the apex section or the bullet.

**FM7 — note.** "Floor" carries three senses in this repo — the always-confirm floor
(`AUTONOMY.md`), the inlined child block or region (`PROPAGATION.md`), and the scanner floor
(`floor.py`, `floor.yml`) — and `GLOSSARY.md` defines only the second. The apex's "always-
confirm floor stop (`PROPAGATION.md` floor — …)" leans on the ambiguity. Related: the
reference's F and J bullets each define the other as "the same class", which is why every copy
counts eight classes against ten reference bullets; a future "count" sentence should count the
reference's classes, not its bullets, and say which.

### Standing checklist

- **V1** — no claim in the delta outruns its evidence; the subject's "every copy" is the
  overclaim, and it is FM5's.
- **V2** — the floor on both planes, `stampscan`, both `blockscan` modes and the matrix sweep
  re-run (ledger below); the brief's "no later commit has touched either path" re-driven
  with `git log` and true.
- **V3** — not discharged clean: FM1, FM5 (mirror sites the sweep missed and cannot reach).
- **V4** — not discharged clean: FM3 (two homes cited), FM5 (an unstamped original).
- **V5** — not discharged clean: FM2 (the reference's headline against its list), FM3.
- **V6** — lens 4 above; `/security-review` discharged by grounds.
- **V7** — provenance stated in the brief and repeated above.

### Overall

**PASS-WITH-FINDINGS — 1 MAJOR · 4 MODERATE · 1 minor · 1 note.** The delta does what its
subject says on the three lists it touched and leaves each sentence true to its attribution;
the MAJOR is harvest — a member missing from every copy since the floor's first day, and no
mechanism that would have told anyone.

### Re-run ledger

All from the worktree root, under `nice -n 10`, one at a time, exit codes read explicitly.
Load average at the first heavy step: 61 (other sessions' suites); no test suite was run, as
the brief names none.

| Command | Result |
|---|---|
| `python3 tools/floor.py --plane hook --root <wt> --tools <wt>/tools` | exit 0; 12 enforced ✅, 4 warn-only 👁️ |
| `python3 tools/floor.py --plane ci --root <wt>` | exit 0; secretscan 23 advisory, leakscan cover note, rest ✅ |
| `python3 tools/stampscan.py --warn --root . .` | exit 0; 1 stamped block, `identical` (93 lines) |
| `python3 tools/blockscan.py --check --warn --root .` | exit 0; map resolves; 43 unmapped top-level headings |
| `python3 tools/blockscan.py --against 7c2ab8b^ --warn --root .` | exit 0 (`--warn`); 3 violations: two apex-keyed (the delta's), one `RECORD.md` (a later commit; `--against` spans REV..HEAD, 14 days) |
| scratch clone at `7c2ab8b`: `blockscan.py --against HEAD^ --warn` | exit 0 (`--warn`); 2 violations, both the delta's (FM6) |
| `git diff 7c2ab8b^ 7c2ab8b -- docs/method/00-APEX.md docs/method/README.md` | the three list edits; nothing else on those paths |
| `git log 7c2ab8b..HEAD -- 00-APEX.md README.md AUTONOMY.md` | only `89ff0d8` (AUTONOMY, 2026-10-06, pre-flip gate); the two delta paths untouched since |
| `git log -S` on each member | K in AUTONOMY `1778baa` 2026-07-10; block `c3676ee` 2026-07-10; apex lists `f4356f8` 2026-07-14; `blockscan.py` added `be8a003` 2026-09-20 |

The matrix sweep, so it re-runs (exclusions: rule 2's default bar plus the three
`--also-exclude` paths the brief lists; the hits under `docs/roadmap/` and `CHANGELOG.md` were
read as records, not copies; `docs/reviews/2026-10-16-15*` hits were not opened):

```sh
Q=docs/roadmap/160-doctrine-review-owed
X="--also-exclude $Q/620-rule-4-cold-pass-queued-floor-list-membership.md \
   --also-exclude docs/reviews/2026-10-16-1550-always-confirm-copies-cold.deferred.md \
   --also-exclude docs/roadmap/200-anti-slop-invariant-registry-promote-rec"
python3 tools/coldsweep.py --root . -i $X \
  'always[- ]confirm|floor stop|lockout[- ]class|trust surface|unapproved tool|hard-to-undo|private ?(→|->|to|-)? ?public|stop and confirm'
python3 tools/coldsweep.py --root . -i $X 'deploy-on-push'          # 4 hits, all AUTONOMY.md
python3 tools/coldsweep.py --root . -i $X "other people'?s work|adding a collaborator|widening (its|an) audience"
python3 tools/coldsweep.py --root . -i $X \
  '\b(four|five|six|seven|eight|nine|ten|eleven|[0-9]{1,2}) (floor[- ])?(stops|floor items|floor members|floor concerns)'
```

First sweep: 77 hits over 630 files, 407 barred. Count sweep: 2 hits, both historical.

### Follow-up checklist

- [ ] FM1 — principal rules K's status (member or sub-case of A); copies and the reference
      brought to agreement accordingly; `AUTONOMY.md` § *Always confirm* mapped as a source for
      `stop-and-confirm` in `tools/blockscan_map.json`.
- [ ] FM2 — `AUTONOMY.md` § *The one rule* names every class or points at the list.
- [ ] FM3 — apex lists become pointers or stamped copies; row 1's attribution corrected to
      `AUTONOMY.md`.
- [ ] FM4 — `TOOLBOX.md` list-update bullet requires the confirmation's date on a new row.
- [ ] FM5 — `session-onramp` § 2 stamped verbatim or cut to a pointer.
- [ ] FM6 — scoped `blockscan:allow:` with reason on the apex section or the bullet.
- [ ] FM7 — `GLOSSARY.md` floor entry names the three senses, or the apex names the sense it means.
- [ ] Phase 2: reconcile against the sibling once released.

### Reconcile (2026-10-17 UTC, after phase 1 landed as `689ab00`)

Opened at phase 2, on the orchestrator's release of the sibling text: the sibling; the landing
commit's message body; the queue pointer `160/620`; the intent record
`docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md` (the `200/040` and
`200/100` passages); and the ten prior verdicts the sibling names, by grep for the floor-list
terms and then the matching sections in full — chiefly `2026-07-14-2235` (F1, where the apex
lists were born), `2026-08-17-1000` (RR1, RR8), and `2026-09-25-0715-ask-rule-to-children`
(AK2). Phase-1 text above is unrevised; nothing is folded or deleted here.

**Against the intent record and the commit body.** The intent record files C7 as one of eleven
disagreeing copy-sets from the `200/040` survey ("41 independent restatements, 20 pointers,
7 stamped — only the floor block is mechanically stamped"), and records Mike's "fix the
contradictions one by one" as an answer, not a ruling. The body confirms the structural
reading in lens 2: the one stop left out is deploy-on-push, on the ground that it "arguably
sits inside 'widening its audience'". That phrase is the *block's* wording for member A; the
two apex copies the commit edited say "making a repo public", which carries no audience
clause — so the subsumption the body relies on fails on the very copies it was editing
(FM1 stands, and is sharpened). The body also counts the onramp skill as a copy that "already
matched", which confirms row 6 is treated as a copy and left unstamped (FM5 stands).

**Against the prior verdicts.** Three open findings already sit on this surface, none ruled:

- **RR1 (2026-08-17, MODERATE, unchecked):** the apex exception restates the floor narrower
  than `AUTONOMY.md`; counsel "refer to `AUTONOMY.md`'s floor by name, drop the enumeration".
  **FM3 is the same finding two months on**, now with the add-a-collaborator case routed. The
  landing commit extended the enumeration RR1 counselled removing — see FM8.
- **RR8 (2026-08-17, unchecked) and AK2 (2026-09-25, MODERATE, unchecked):** the onramp
  skill's floor list is an unstamped third original that sweeps keep missing. **FM5 is the
  same finding**, with the commit body's own "already matched" as the new evidence that it is
  treated as a copy without being watched as one. One ruling would close RR8, AK2 and FM5.
- **F1 (2026-07-14, [fixed] on Mike's ruling):** the apex sentence became two-armed —
  "governance ruling **or** always-confirm floor stop (`PROPAGATION.md` floor)". So the
  "`PROPAGATION.md` floor" attribution FM3 names is the wording of a ruled fix, not a later
  drift; FM3's counsel on attribution is therefore a re-brief of that ruling, not a correction
  of a slip — stated so the principal rules on it knowing its provenance.
- **foundation Q2 (2026-07-10, [fixed]):** "a pull-quote lists 4 of 6 floor items" is the
  class FM2 re-finds in `AUTONOMY.md`'s own headline quote (7 of 10 bullets); the 2026-07-10
  fix reached the pull-quote then under review and the headline was not swept.
- No prior verdict names the `AUTONOMY.md` → copies watching gap (FM1's second half), the
  deploy-on-push absence, or the TOOLBOX approval-record seam (FM4): those are new.

**Seeded questions, each answered.**

1. *Did the 2026-08-17 ruling name the floor by reference or by enumeration?* By reference.
   The ruling-round verdict records ruling two as "where the approval is an always-confirm
   floor stop, the re-briefing must come before the irreversible action", and RR1 found the
   exception paragraph's seven-item enumeration to be the applying session's, not the
   ruling's. So the commit edited a convenience copy inside a sentence attributed to the
   ruling; it did not rewrite the ruling — but the attribution makes any future reader take
   the list as the ruling's scope, which is RR1's and FM3's point: point, don't enumerate.
2. *Does the first apex list now match the `PROPAGATION.md` block member for member?* No. The
   block names "or widening its audience" (A), "people's safety" (I) and "widening your own
   grant" (E, which the apex's first list carries in its governance arm and its second list
   not at all). Matrix rows 1–2 against row 4; FM3.
3. *Does an argued subsumption meet "in every copy"?* No, on two counts: the subsumption's own
   wording is absent from the copies edited (above), and `AUTONOMY.md` lists K as its own
   bullet, so until the principal folds it (FM1's first decision) a copy that omits it drops a
   member. FM1.
4. *Is the README's enumerated summary a second source that should have been a pointer?*
   Yes, on V4's test and on the record: the commit body says the README "also dropped new
   trust surfaces" — a second drift on the same line (the first being its pre-2026-10-03
   state). Folded into FM3's counsel as row 3: the item keeps its one-line character ("confirm
   on the hard-to-undo floor") and points at `AUTONOMY.md` § *Always confirm* instead of
   listing. No new finding; FM3's counsel is widened to rows 1–3.
5. *Should the apex carry the floor as a stamped copy?* No — a pointer, for a mechanical
   reason: the floor region admits no declared narrowing (`115/030`, verbatim), and the
   apex's lists are clauses inside sentences, so a stamp would red on shape alone. Stamping
   fits the onramp (FM5, if its text goes verbatim); the apex and README fit pointing. The
   mechanism the apex needs is the other direction — `AUTONOMY.md` mapped as a `blockscan`
   source (FM1).

**Finding formed at reconcile.**

**FM8 — minor (reconcile).** The fix ran against open counsel on its own surface. RR1
(2026-08-17) counselled dropping the apex enumerations and RR8/AK2 counselled stamping or
pointing the onramp; all three were unruled on 2026-10-03, and the C7 fix extended the
enumerations instead, with the queue run's "fix one by one" recorded as an answer rather than
a ruling. Not a defect of the delta's content — an enumeration made more complete is better
than one less complete — but a pre-emption of a pending ruling's direction, and the shape
`PROPAGATION.md` § *When a rule keeps breaking* names: a rewording where a mechanism was
already counselled. *Counsel:* when a contradiction fix lands on a surface with an unruled
finding, the fix's record names that finding and the direction it chose; here, FM1/FM3/FM5
and RR1/RR8/AK2 go to one ruling together.

**Overall, restated:** **PASS-WITH-FINDINGS — 1 MAJOR · 4 MODERATE · 2 minor · 1 note**
(FM8 added at reconcile; no phase-1 severity changed).

## Deferred material — folded in at reconcile

# Deferred sibling — the always-confirm floor list's copies

**Held under rule 1's split** (`docs/method/REVIEW.md`). Open only after your
phase-1 findings are committed to the brief
`docs/reviews/2026-10-16-1550-always-confirm-copies-cold.md`. At verdict, fold
this file in below your reconcile and delete it.

Written 2026-10-16 UTC by the Opus brief-writer named in the brief, which authored
none of the delta and forms no finding: the questions below are seeds, a floor
and never a fence.

## Intent record

- `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md` —
  **not opened by the brief-writer**.

## Prior verdicts on the same surface (named, not opened)

Path greps over `docs/reviews/` for `always-confirm` name these; none was opened
by the brief-writer:

- `docs/reviews/2026-07-10-atelier-foundation.md`
- `docs/reviews/2026-07-12-reach-rereview.md`
- `docs/reviews/2026-07-14-2235-informed-principal-apex-cold.md`
- `docs/reviews/2026-07-22-1149-queue-run-doctrine-cold.md`
- `docs/reviews/2026-07-23-0222-apex-widening-cold.md`
- `docs/reviews/2026-08-15-1031-laws-removal-apex-cold.md`
- `docs/reviews/2026-08-17-0622-authority-absolute-cold.md`
- `docs/reviews/2026-08-17-1000-ruling-round-application-cold.md`
- `docs/reviews/2026-09-25-0715-ask-rule-to-children-cold.md`
- `docs/reviews/2026-09-25-0715-tier-ruling-cold.md`

## The pointer's own lens hints

None. The pointer is refs-only (delta, intent record, tier, pass type).

## Seeded questions

1. The second apex list opens "One exception, and it is the always-confirm floor
   (the principal's ruling, 2026-08-17)". Adding a member inside a sentence
   attributed to a dated ruling changes what the record says that ruling
   covered. Did the 2026-08-17 ruling name the floor by reference (so the list
   is a convenience copy) or by enumeration (so the edit rewrites a ruling)?
2. The first apex list is introduced as "the `PROPAGATION.md` floor". Does it now
   match `PROPAGATION.md`'s floor block member for member, including the stops
   that block names that the apex does not?
3. The commit leaves AUTONOMY's non-routine deploy-on-push stop out of every
   summary on the grounds that it "arguably sits inside widening its audience".
   AUTONOMY lists it as a separate bullet. Does an argued subsumption meet the
   commit's own title, "in every copy"?
4. `method/README.md` is a reading-order summary ending "Repos may narrow". Is an
   enumerated summary of a safety list a second source (V4) that should have been
   a pointer instead, given it drifted once already?
5. None of the three edited lists is a stamped region. Should the apex carry the
   floor as a stamped copy watched by a guard, as `PROPAGATION.md` and the child
   template do?
