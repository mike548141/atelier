# Cold pass — the review-brief skill on who applies a verdict's findings

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes this pass; a session that cannot honour it stops.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or
instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/580-rule-4-cold-pass-queued-review-brief-rule-3.md`.
**Why it earns a review:** the skill is the point-of-use copy of `REVIEW.md` that a
session loads when it writes or runs a review, here and in every adopter of the
plugin; the changed paragraph says who acts on a verdict, which is the step rules
3 and 4 govern.

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
  message body (the author's own account of why) and diff; the delta file at
  HEAD (head and the changed section); `REVIEW.md` down to § *Whether work earns
  a review*; the ask halves, above the first divider, of two 2026-10-04 briefs as
  format models; filename listings of `docs/reviews/` and `docs/roadmap/`, and
  path greps over `docs/reviews/` that name prior verdicts without reading them;
  and its auto-loaded cross-session memory index (one-line notes, some on review
  independence). Its orchestrator read the `docs/SESSIONS.md` index tail (entries
  through 2026-10-16, including the authoring runs' one-paragraph summaries) and
  the 2026-10-16 session record's close section, and passed this writer nothing
  evaluative beyond the pointer list. What this writer suspects is in the sibling.

## What the work is

Landing commit (diff it; review the path at HEAD):

- `185abfb` (2026-10-03) — skills: review-brief no longer has the author apply
  findings on doctrine (200/100 C10)

Delta path: `skills/review-brief/SKILL.md`, § *Running it and landing the
verdict*. One later commit, `90c42ec` (2026-10-06, 200/050), edited the same
section to add the standing-checklist sentence; it is not this delta, but it sits
in the paragraph you will read at HEAD — attribute by `git blame`.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether the section, read cold by a session that has only the skill, tells it
correctly who applies, who decides and who queues — for every kind of pass. Read
the section at HEAD and diff `185abfb`. Name the section's addressee (the
reviewer running the pass, the author landing it, or both) and test each sentence
against each. Run these cases and record a table: ordinary code reviewed warm by
its author's own spawn (`REVIEW.md` § *When to review*); code that is doctrine by
function (a validator, a CI gate, a template, this skill); a mixed delta (a guard
and the prose that states its rule); an application pass applying decided
findings to doctrine (`REVIEW.md` § *Applying decisions to doctrine*); a terminal
application after a pass with no MAJOR; a pass whose author is the principal (rule
3's distinct-parties premise); a withdrawn pass; an orchestrated pass with an
off-tier orchestrator. For each: who applies, who decides, what is queued, by
whom, and what tag is written.

**Non-goals:** `REVIEW.md` itself (the canonical text the skill compresses); the
content of the checklist sentence `90c42ec` added. Both are read only to judge
whether the delta agrees with them.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   The skill declares itself a stamped, narrowing-free copy of `REVIEW.md` (its
   header comment): test whether the new paragraph compresses the parent, or
   narrows, widens or re-words it — term by term against rules 3–4, lifecycle
   step 4 and the application paragraph.
2. **Correctness & quality.** Every sentence that cross-refers to the change:
   the skill's frontmatter description, § *First*, the lenses list, and the
   deferred-material paragraph after it. Does anything elsewhere in the skill
   still tell a session to apply or close findings itself? Check every cited
   anchor resolves.
3. **Completeness / harvest.** Every other surface that states who applies a
   finding: the child template `docs/build/templates/docs/reviews/README.md`
   (its sentence on this was changed the same day — 160/590's delta), the other
   skills under `skills/`, `commands/`, `docs/method/ECONOMICS.md` (the executor
   seat), `AUTONOMY.md`, and `README.md`. Do they say one thing (V3, V4, V5)? The
   skill ships in the plugin (`.claude-plugin/plugin.json`): is a version or
   `CHANGELOG.md` entry owed for adopters to notice the behaviour change?
4. **Security & privacy** — mandatory. Design altitude: can the new text be read
   to let an author approve or apply its own doctrine finding, or to spawn its
   own doctrine review — the independence failure rule 4 exists for? Code
   altitude: none in the delta (prose). `/security-review` is discharged by
   grounds — a landed prose delta; the session's pending diff is other passes'
   drafts — say so.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- the floor on both planes at HEAD (`python3 tools/floor.py --plane hook --root
  <root> --tools <root>/tools`, then `--plane ci --root <root>`), exit codes read
  explicitly
- `python3 tools/stampscan.py --warn --root . .` — the skill is a stamped copy
- `python3 tools/linkscan.py` over the skill, and `reviewscan`'s `--selftest`
- grep the delta's claims against `REVIEW.md` at HEAD and record each pairing

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
  --also-exclude $Q/580-rule-4-cold-pass-queued-review-brief-rule-3.md \
  --also-exclude docs/reviews/2026-10-16-1550-review-brief-applies-nothing-cold.deferred.md \
  --also-exclude docs/roadmap/200-anti-slop-invariant-registry-promote-rec \
  <pattern>
```

`--include-barred` only with disclosure in the verdict. The delta and the doctrine
it must agree with are never barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, findings with
stable IDs (prefix `RB`: `RB1`, `RB2`, …) and severities (MAJOR / MODERATE /
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

# Verdict — phase 1 (2026-10-17 UTC)

## Provenance, repeated

- **Reviewer:** a fresh `claude-fable-5-1` subagent, prefix `RB`, on the Fable tier rule 4
  names (checked at claim). It authored none of the delta, none of the brief, and none of
  the sibling. It formed every finding and every severity below.
- **Shape:** reviewer-plus-orchestrator, disclosed as rule 4 requires. The orchestrator
  (also Fable) spawned this reviewer, holds the `.deferred.md` sibling outside the tree as
  the context partition, forms no finding, writes no severity, and commits this file. Two
  other reviewers share the worktree on their own brief files; nothing of theirs was read.
- **Worktree:** `/Users/mike/worktrees/atelier-review-1017`, branch `review-1017`, HEAD
  `4eef78e`. No git write was run; the tree's only pending changes are the orchestrator's
  partition (deleted `.deferred.md` paths — nine at the time of this pass, not the
  twenty-one the spawn prompt expected; none opened, none restored) and this file.
- **What was read:** this brief; `skills/review-brief/SKILL.md` at HEAD in full; the
  `185abfb` diff, message and `--stat`; the `90c42ec` diff and message; `git blame` over
  lines 85–108 of the skill; a grep of the skill at `185abfb^` (hits only); `REVIEW.md` in
  full; `docs/build/templates/docs/reviews/README.md` in full; passages of `ECONOMICS.md`,
  `AUTONOMY.md`, `00-APEX.md`, `GLOSSARY.md`, `RECORD.md`, `README.md`,
  `skills/queue-run/SKILL.md`, `tools/test_templates.py`, `tools/floor.py`, the hook, the
  CI workflow, `CHANGELOG.md` headings and greps, and both plugin manifests.
- **Exposure, disclosed:** none of the barred set was opened. Both sweeps ran under
  `coldsweep`'s default bar plus the brief's three exclusions (407 files barred); no
  `--include-barred`. Two sweep hits landed in unbarred board files outside the item
  under review (`160/250`, one closing line; `260/README.md`, one line on a prior batch's
  spawn) and one in `CHANGELOG.md` at line 3001; each was read as a single line, none is
  evaluative of this delta. The reviewer's auto-loaded cross-session memory index
  (one-line notes, some on review independence) was in context, as on every pass.
- `/security-review` was not run: the session's pending diff is the partition and other
  reviewers' drafts, and the delta is landed markdown, which the scanner's own exclusions
  bar. Discharged by grounds under lens 4 below.

## Addressee

§ *Running it and landing the verdict* speaks to the **reviewer** in imperatives
("Reproduce the floor", "Work the lenses", "Land findings", "Close with a verdict"). The
delta's paragraph then switches subject to the **author** in the third person ("the author
may apply", "the author applies nothing"). Each sentence was tested against both readers:
the reviewer learns that it is not the one who applies; the author learns the split. Neither
reader is told the author's handoff (RB2), and the doctrine bullet's rule-4 clause reads
differently to each (RB1).

## Lens 1 — approach and assumptions

Load-bearing assumptions, named first:

- A1 — the skill is a narrowing-free compression of `REVIEW.md` rules 3–4, lifecycle step 4
  and the application paragraph. **Partly false.** The rule-3 half compresses faithfully;
  the rule-4 clause paraphrases the criterion away (RB1); the handoff is absent (RB2).
- A2 — a session that loads only the skill can act correctly at the point of use. **False**
  for the doctrine case: it does not learn to queue (RB2) and can read itself as allowed to
  spawn its own review (RB1).
- A3 — "doctrine by function" is recognisable from the skill alone. **Weak:** examples are
  given, the test is not (RB3).
- A4 — the mirror sites say one thing. **True in content, uneven in coverage** (RB5).

Term-by-term pairing of the delta against `REVIEW.md` at HEAD (line numbers at HEAD):

| Skill sentence (lines 97–107) | `REVIEW.md` | Result |
|---|---|---|
| "Who applies a finding depends on what was reviewed (rules 3 and 4)" | rule 3 (128–147); step 4 carve-out (381–385) | compresses |
| "Ordinary code: the author may apply … record `[fixed]`, `[backlog]` or `[rejected: grounds]`" | step 4 (376–380) | compresses; "a named ROADMAP slice" and "grounds recorded in the verdict file, never silently dropped" fall away — acceptable |
| "A finding fixed but not re-driven is not closed" | step 5 (390–392) | matches |
| "judged by function, not file type, so a skill, template, schema or gate counts" | rule 3 (129–133) | examples kept, the function test dropped — RB3 |
| "the author applies nothing on its own. It records the verdict verbatim." | rule 3 (136–137) | matches; the labelled-counsel permission dropped — RB4 |
| "the principal's to decide, after he has the plain-language account the apex requires" | rule 3 (138–141); `00-APEX.md` 133–140 | compresses; pronoun — RB10 |
| "must come from a cold *spawn*, never from the author's own session (rule 4)" | rule 4 (148, 157–161); § *When to review* (545–551) | **lossy paraphrase; permits what the parent forbids — RB1** |
| *(absent)* the `⏳` pointer, landing = queuing, the applier, the terminal application | rule 4 (163–177); step 1 (360); application paragraph (394–407) | **missing — RB2** |

Scenario table (the brief's eight cases; "skill says" is what a session holding only the
skill would do):

| Case | Who applies | Who decides | Queued, by whom | Tag written | Skill says |
|---|---|---|---|---|---|
| 1 Ordinary code, warm author-spawn | the author | builder/owner (grounds recorded) | the brief's own board pointer; sibling held by the spawner | `[fixed]` / `[backlog]` / `[rejected: grounds]` | ✅ correct |
| 2 Code that is doctrine by function | nobody until the principal rules | the principal, informed | `⏳` by the author, in the landing commit, refs only; the non-author taker writes the brief | none by the author; counsel labelled | ⚠️ applies/decides right; queue absent (RB2); spawn clause lossy (RB1) |
| 3 Mixed delta (guard + its prose) | as 2 — the guard is a rule in code, so the whole delta is doctrine | the principal | as 2 | none | ⚠️ no tie-break between the two bullets; the test that resolves it is absent (RB3) |
| 4 Application pass on decided findings | the applier, preferably neither doctrine's nor verdicts' author | already decided; the application pass's own findings → the principal | `⏳` by the applier, in the application commit, for a non-author | the decided findings' tags, with the ruling noted | ❌ silent (RB2) |
| 5 Terminal application after a no-MAJOR pass | the applier | decided into the backlog | nothing — the cycle closes | as 4 | ❌ silent (RB2) |
| 6 Author is the principal | rule 3 gives nothing; the cold record is the only independence | the principal, on his own work | `⏳` still owed where a non-author reviewer exists | per step 4 | ⚠️ reads circular, no warning (RB7) |
| 7 Withdrawn pass | nobody; outputs preserved under a banner, quarantined | the rejecter, named | the item's `⏳` stands for the redo | none; findings die with the pass | ❌ silent (RB8) |
| 8 Orchestrated, off-tier orchestrator | as 2 | the principal | records committed by the orchestrator; disclosed in claim, pointer and verdict | none | ✅ the V7 line (90c42ec) covers provenance; nothing in the delta contradicts |

## Lens 2 — correctness and quality

- Frontmatter description: makes no claim about applying; consistent.
- § *First*: unchanged by the delta; consistent.
- Lenses list (items 1–5): item 5's "a proof you have not re-run is not one you can close
  on" is verdict-closing language, not finding-applying; consistent. Lens 4's "never run it
  over a brief carrying deferred material before findings are committed" is reviewer
  conduct; consistent.
- Deferred-material paragraph: "fold it into the brief below the verdict and delete it" is
  reviewer conduct on its own record; consistent.
- Nothing elsewhere in the skill still tells a session to apply or close findings itself.
  The pre-delta "applied and re-driven the same session" is gone (grep at HEAD: no hit).
- Anchors: "`REVIEW.md` rules 3 and 4" resolve to numbered items 3 and 4 under
  § *Independence is more than fresh context*; "§ *The standing checklist*" exists at line
  312; "the apex" resolves to `00-APEX.md` lines 133–140. `linkscan` over the skill: clean.
- Honesty of the commit message: "Rule 4 says the review must come from a cold spawn" is
  the same lossy reading the skill now carries (V1 — RB1).

## Lens 3 — completeness and harvest

- `docs/build/templates/docs/reviews/README.md` lines 27–29 carry rule 3 in the same
  shape as the skill (consistent, V5 across the two files). Its closing line 92, "apply
  fixes back on the workhorse seat", survives unconditionally from before — RB5.
- `docs/method/ECONOMICS.md` line 35 and `docs/build/templates/docs/ECONOMICS.md` line
  19: "apply fixes back on the building model / workhorse" with no rule-3 carve-out, while
  § *Triggering reviews* (line 340) carries rule 4's — RB5.
- `skills/queue-run/SKILL.md` lines 83–93: states rule 4's criterion verbatim and is pinned
  by `test_rule4_criterion_phrase_in_both`. The review-brief skill is the one skill that
  paraphrases it — RB1.
- `skills/create-repo`, `skills/session-onramp`, `commands/*`: no who-applies statement;
  nothing to sweep. `AUTONOMY.md` line 82 cites rule 3 in its own context; consistent.
  `README.md` line 96 is a one-line blurb; nothing to sweep.
- Plugin: `.claude-plugin/plugin.json` and `marketplace.json` both at `0.2.0` (unchanged
  since 2026-07-21, `2271a44`); the plugin's source is the repo root, so `REVIEW.md` ships
  beside the skill. `CHANGELOG.md`: no entry for 2026-10-03, no reference to `200/100` or
  `185abfb`; the commit touched no changelog — RB6. No version bump is owed: the changelog's
  own rule keeps everything under *Unreleased* until there is a reason to tag.
- Machine coverage of the stamped copy: `stampscan` verifies one block in the tree (the
  templates floor); the skill's header is a prose comment; `ReviewBriefSkillTest` pins the
  trigger phrase, the lens roster and three evicted phrases only — RB9.

## Lens 4 — security and privacy

- **Design altitude.** The question the brief puts — can the text be read to let an author
  spawn its own doctrine review — is answered **yes**: RB1. Can it be read to let an author
  apply or approve its own doctrine finding — no: "applies nothing on its own" and "the
  principal's to decide, after he has the plain-language account" hold that line.
- **Code altitude.** None: the delta is prose in a markdown skill. OWASP Top 10 / ASVS
  categories (injection, broken access control, insecure design, misconfiguration,
  identification failures, integrity failures, logging, SSRF) have no surface here.
- **`/security-review`:** discharged by grounds — a landed markdown delta the scanner's
  exclusions bar, and the pending diff is other passes' drafts (the SL2 class).
- **Privacy, public repo.** The delta names no person, address or secret. The one
  identity-shaped token is the pronoun for the principal (RB10, style not privacy).

## Standing checklist V1–V7

- **V1** — the commit message's rule-4 restatement is stronger than its evidence (RB1);
  no other overclaim found.
- **V2** — re-run ledger below; the floor on both planes is not run on this pass, by the
  orchestrator's load instruction, and is owed (follow-ups).
- **V3** — the changed rule reached the child reviews README (160/590) but not
  `ECONOMICS.md`, its template copy, or the README's own tail (RB5); rule 4's criterion is
  verbatim on two surfaces and paraphrased on this one (RB1).
- **V4** — the skill points at its one source; the copy is marked but unwatched (RB9).
- **V5** — no contradiction inside the skill; the template README carries a tension between
  lines 27–29 and 92 (RB5).
- **V6** — lens 4 above; discharged with grounds.
- **V7** — provenance stated above and in the brief.

## Findings

**RB1 — MAJOR — rule 4's criterion is paraphrased out of the point-of-use copy.** The
doctrine bullet's last sentence reads "the review itself must come from a cold *spawn*,
never from the author's own session (rule 4)". Rule 4's single criterion is a session the
author **neither started nor instructed**; the skill never states it (grep at HEAD for
"started nor instructed", "neither started", "non-author": no hit), and the skill's only
definition of *cold* (§ *Independence is the core*) is fresh context — "a separate
session, even the same model". A session holding only the skill therefore reads the clause
as satisfied by spawning a fresh background agent with a brief — the author-started,
author-instructed path `REVIEW.md` § *When to review* forbids for self-authored doctrine
("cannot take this path at all") and `ECONOMICS.md` § *Triggering reviews* repeats. The
house already knows this drift class: `tools/test_templates.py`
`test_rule4_criterion_phrase_in_both` pins the exact phrase on two surfaces with the comment
that paraphrase is where the authorship-versus-spawn drift (QR1) hid. The review-brief skill
is unpinned. Attributable to the delta: at `185abfb^` the skill carried no rule-4 sentence
at all. Blast radius is rule 4's own: every adopter session that writes or runs a review
from the skill. *Counsel:* replace the clause with the criterion verbatim — the review comes
from a session the author neither started nor instructed; an author-spawned agent or an
author-scheduled batch fails it — and add the phrase pin to `ReviewBriefSkillTest`.

**RB2 — MODERATE — the author's handoff is unstated: nothing in the skill says who
queues, what, or when.** The skill has no `⏳`, no "queue", no "pointer" (grep at HEAD: no
hit). `REVIEW.md` rule 4 makes the pointer the author's handoff, in the same commit that
lands the work (landing = queuing, the AWA2 window); lifecycle step 1 adds the board
pointer; the application paragraph has the applier queue the next `⏳` in the application
commit and the terminal application close without one; step 4 ticks the pointer once
decided. A session with only the skill lands self-authored doctrine unpointed, which is
the window rule 4 closed, reopened at the point of use. Scenario rows 2, 4 and 5 fail on
this column. *Counsel:* one sentence in the doctrine bullet — the handoff is the `⏳`
pointer (refs only: delta and intent record) in the landing commit, the non-author taker
writes the brief; applying the rulings is itself a doctrine edit, so the applier queues the
next `⏳` in the application commit, and the application after a no-MAJOR pass closes
without one.

**RB3 — minor — doctrine is given by examples, not by rule 3's test.** "(judged by
function, not file type, so a skill, template, schema or gate counts)" keeps the examples
and drops the function — any rule that governs future agent behaviour. A novel artefact (a
hook, a dispatch prompt, a guard's tests, a roadmap item's direction) or a mixed delta
(scenario row 3) cannot be classified from the skill, and the two bullets are framed as
alternatives with no tie-break. *Counsel:* name the test in the parenthesis; the examples
then follow from it.

**RB4 — minor — the author's labelled counsel is dropped, and the reviewer's own
obligation is not addressed to the reviewer.** Rule 3 and step 4 let the author argue its
case per finding, labelled as its position and kept below the reviewer's text; the skill's
"applies nothing on its own. It records the verdict verbatim." reads as silence-only, so
the principal's informed decision loses the author's account of the trade-off. And because
the paragraph's addressee switches from reviewer to author, the reviewer of a doctrine pass
is never told, in its own terms, to record all and apply nothing — words this brief's
*Process* section had to add. *Counsel:* "either party may record counsel per finding,
labelled, below the reviewer's text; the reviewer applies nothing on any pass."

**RB5 — minor (V3) — three mirror lines keep the pre-delta rule without a carve-out.**
`docs/method/ECONOMICS.md` line 35 ("apply fixes back on the building model"),
`docs/build/templates/docs/ECONOMICS.md` line 19 and
`docs/build/templates/docs/reviews/README.md` line 92 ("apply fixes back on the workhorse
seat") are seat statements, so no contradiction — but a reader of any one of them alone
gets "apply fixes back" unconditionally, while the same README's lines 27–29 and the same
`ECONOMICS.md`'s § *Triggering reviews* carry the carve-outs. *Counsel:* a short gloss at
each — on ordinary code; doctrine findings wait for the principal (`REVIEW.md` rule 3).

**RB6 — minor — no `CHANGELOG.md` entry for a behaviour change in a shipped skill.** The
commit touched no changelog; there is no 2026-10-03 entry and no reference to `200/100`.
The adjacent skill change (`90c42ec`, 200/050) has one that names the skill. `RECORD.md`
lists the changelog among a close's tidy-up. No version bump is owed under the changelog's
own *Unreleased* rule. *Counsel:* a *Changed* entry under *Unreleased*, dated 2026-10-03,
saying who applies a finding now depends on what was reviewed.

**RB7 — note — the solo-operator case is unwarned.** Where the author is the principal,
the parent says rule 3 gives nothing and the adopter should know the gap; the skill's
bullet reads circular there and carries no warning. The plugin's adoption model (a human
principal with an agent author) makes this the exception, hence a note. *Counsel:* an
optional half-sentence pointing at the parent's two-terms paragraph.

**RB8 — note — a withdrawn pass has no line.** A session with only the skill whose pass is
rejected is not told that the outputs are preserved under a banner, the `⏳` stands, and
the findings die with the pass. *Counsel:* one pointer sentence to
`docs/reviews/withdrawn/README.md`.

**RB9 — note (V4) — the stamped copy is marked, not watched.** `stampscan` at HEAD
verifies one block in the tree and it is not this skill; `ReviewBriefSkillTest` pins
nothing of rules 3–4. Drift in this paragraph is caught only at review. *Counsel:* pin the
"applies nothing" sentence alongside RB1's phrase pin.

**RB10 — note — an unquoted gendered pronoun for the principal** ("after he has") in a
skill shipped to adopters who become the principal; the parent uses "the principal" in its
own voice and "his" only inside the apex's quoted title. Style, not privacy.

## Overall

**PASS-WITH-FINDINGS — 1 MAJOR · 1 MODERATE · 4 minor · 4 note.** The delta's core
claim — the author applies nothing on self-authored doctrine and the principal decides —
is correct and faithfully compressed. The rule-4 clause it added beside that claim is the
lossy paraphrase the house's own tests already name as the drift class, and the handoff
that makes rule 4 bite is absent. All findings are on doctrine: recorded, nothing applied;
counsel is labelled.

## Re-run ledger

Machine load at the pass's open was 27.57 (one-minute), 81.79 (five-minute), from other
sessions' test runs; the orchestrator's instruction was no test suite and no whole-tree
floor, single-file scanners only, under `nice -n 10`, one at a time, foreground.

| Command (from the worktree root) | Result |
|---|---|
| `python3 tools/floor.py --plane hook --root . --tools ./tools` | **not run under load** (orchestrator's instruction) — owed |
| `python3 tools/floor.py --plane ci --root .` | **not run under load** — owed |
| `nice -n 10 python3 tools/stampscan.py --warn --root . .` | exit 0; 1 stamped block verified (`docs/build/templates/CLAUDE.md:18`, identical); 175 files by `.stampscanignore`; the skill is not a stamped block (RB9) |
| `nice -n 10 python3 tools/linkscan.py --root . skills/review-brief/SKILL.md` | exit 0; clean |
| `nice -n 10 python3 tools/reviewscan.py --selftest` | exit 0; `reviewscan selftest: OK` |
| `coldsweep` (brief's three `--also-exclude`) for the who-applies and spawn-criterion phrasings | exit 0; 15 hits over 630 files, 407 barred; hits tabulated under lens 3 |
| `coldsweep` (same exclusions) for `rejected: grounds` | exit 0; 5 hits; the tag grammar lives in `REVIEW.md` 133/377 and the skill line 100 only |
| `git blame -L 85,108 skills/review-brief/SKILL.md` | lines 95–107 `185abfb`; 88–94 `90c42ec`; 85–87 `8bb9c87` |
| `git show 185abfb^:skills/review-brief/SKILL.md` grep for rule 3 / rule 4 / spawn / principal | no hit — the rule-4 sentence is new in this delta |
| grep of the skill at HEAD for the criterion phrase, `⏳`, "queue", "pointer" | no hit (RB1, RB2) |
| grep of `CHANGELOG.md` for 2026-10-03, `200/100`, `185abfb`; `git show --stat 185abfb` | no entry; no changelog in the commit (RB6) |
| pairing of each delta sentence against `REVIEW.md` at HEAD | table under lens 1 |

Each scanner finished in under ten seconds; load had fallen to 10.66 by the pass's close.

## Follow-up checklist (the principal's to decide; nothing applied)

- [ ] RB1 — criterion verbatim in the skill's doctrine bullet; phrase pin in
      `ReviewBriefSkillTest`.
- [ ] RB2 — the handoff sentence (pointer in the landing commit; applier queues; terminal
      application closes).
- [ ] RB3 — name rule 3's function test in the parenthesis.
- [ ] RB4 — labelled-counsel clause; reviewer-addressed "apply nothing".
- [ ] RB5 — three glosses: `ECONOMICS.md` 35, its template copy 19, the reviews README 92.
- [ ] RB6 — `CHANGELOG.md` *Changed* entry dated 2026-10-03.
- [ ] RB7–RB10 — optional, at the principal's discretion.
- [ ] Run the floor on both planes at HEAD when the machine is quiet; this pass could not.
