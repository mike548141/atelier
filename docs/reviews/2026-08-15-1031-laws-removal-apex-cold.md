# Cold pass — the Three Laws and the Zeroth leave the apex

**Pass type:** doctrine cold pass (REVIEW.md rule 4 — the apex is the
highest-stakes self-authored doctrine surface in the repo; the principal
ruled the intent, the agent's judgement produced the wording and the sweep).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04).
**Status:** BRIEF WRITTEN, REVIEW NOT RUN. The next cold session that passes
rule 4's criterion and the tier bar takes it — see *Spawn provenance*.

## Spawn provenance

- **Author of the work under review:** the session that landed the delta on
  2026-08-15 (wt: `laws-removal-0815`; see *What the work is*).
- **Who wrote this brief:** a cold session Mike opened on 2026-08-15 with
  the standing instruction, verbatim: *"As a cold session please do any review
  work, any work that is fable dependent, and write briefs for any reviews
  that need them. If you write the brief then do not run the review, that
  will require another cold review session."* That session authored no part
  of this delta, was neither started nor instructed by the authoring session,
  wrote this brief from the delta and the queue pointer only (it did not open
  the intent record), and **stopped** — it did not run the review.
- **Who takes the review:** the next cold session that meets rule 4's single
  criterion — a session the author neither started nor instructed — on the
  Fable tier, checked at selection. The taker repeats its own provenance in
  the verdict: how it was spawned, and its non-involvement with both the
  authoring session and the brief-writing session.
- **Orchestration shape:** the deferred material sits in the sibling file
  `2026-08-15-1031-laws-removal-apex-cold.deferred.md` (rule 1's split): the
  intent-record reference, the prior-verdict references, and the
  brief-writer's seeded questions. Recommended: the taker runs the review
  under an orchestrator that holds the sibling's bytes and hands them to the
  reviewer only after its findings are durably written. A taker reviewing by
  hand opens the sibling as a deliberate second act after its findings are
  written, and says so in the verdict. Fold in and delete when the verdict
  lands.

## What the work is

Landed 2026-08-15 on `main` as `71b3e8f` (the removal), preceded by the claim
`4ea0a8f` and followed by the merge `b5da9e5`. Reviewed at HEAD:

1. [`docs/method/00-APEX.md`](../method/00-APEX.md) — the section that held
   the Laws is deleted; the title, § *Why this is level 0*, and every count
   of the apex's parts are reworded to a duo.
2. The restatement surfaces swept in the same commit:
   [`README.md`](../../README.md), [`docs/method/README.md`](../method/README.md),
   [`docs/method/GLOSSARY.md`](../method/GLOSSARY.md) (*Apex*),
   [`docs/method/PRINCIPLES.md`](../method/PRINCIPLES.md) (§0 intro and the
   precedence ladder), [`docs/method/PROPAGATION.md`](../method/PROPAGATION.md)
   (the fail-safe line, the SR2 concern list, and the inlined child floor
   block), the byte-identical stamp in
   [`docs/build/templates/CLAUDE.md`](../build/templates/CLAUDE.md), and
   [`skills/session-onramp/SKILL.md`](../../skills/session-onramp/SKILL.md).
3. Board changes in the same commit: the ruling item
   `docs/roadmap/020-…/210-…` closed, the pointer `215-…` opened, the
   Laws-ladder raw note removed from *Open questions*, and the
   `160-…/140-…` propagation item reworded.
4. The `CHANGELOG.md` *Removed* entry.
5. **What was deliberately left**, per the commit message: historical records
   and prior review verdicts (the history layer), and children's floor blocks
   (they shed the sentence at their next pin bump).

## Scope

Widest the work admits: the ruling as executed against the ruling as given
(the intent is the principal's; the wording, the sweep, and the judgement of
what counts as a restatement surface are the author's), the apex text that
remains and whether it still stands as a complete frame without the third
part, every surface that restated the Laws inside and outside `docs/method/`,
what the removal leaves dangling, and how the change reaches the fleet.
**Non-goals — one, and it does not fence the risk:** the reviewer does not
decide any finding; the apex is principal-ruled doctrine and findings are the
principal's to rule on (rule 3). Counsel may be recorded, labelled as such.
The *decision* to remove the Laws is the principal's and is not under review;
its *execution* is.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself
   first. What did the Laws section carry beyond the Laws themselves (its
   caveats, the "surface a genuine dilemma" instruction, the "sits within the
   agent's own safety values" statement) — and does anything that survives
   the removal now rest on a sentence that is gone?
2. **Correctness & quality** — is the apex text internally consistent as a
   duo? Do the surviving cross-references (glossary, precedence ladder,
   propagation floor block, skill) say the same thing as `00-APEX.md` at HEAD?
3. **Completeness / harvest** — search the whole tree yourself: which
   surfaces still restate the Laws, the Zeroth, or "the three" — doctrine,
   templates, skills, plugin surfaces, `docs/build/`, instrument READMEs? Was
   the sweep checklist the author followed the right checklist? Is the
   history-layer carve-out drawn where the doctrine draws it?
4. **Security & privacy** — mandatory. atelier is PUBLIC; the apex is its
   most-read file. Check the delta and its record surfaces for anything that
   joins a private repo's name to its posture or carries estate detail. If the
   lens genuinely has no surface beyond that, discharge it in one explicit
   line with grounds. The house security scanner reads pending diffs; this is
   a landed-delta review, so state the reach case that applied.

## Re-run obligation

Re-run, do not read: the tree-wide search for every restatement surface (the
commit's own claim is "every restatement surface swept" — test it against a
grep you write yourself, including outside `docs/method/`); the byte-identity
claim between PROPAGATION.md's inlined floor block and
`docs/build/templates/CLAUDE.md`; the floor on both planes at HEAD; and the
propagation lane's behaviour for a child at its next pin bump (read the
mechanism, provoke it read-only if the repo admits it).

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`,
every prior verdict in `docs/reviews/`, and the intent record for this delta.
The sibling `.deferred.md` holds those references and the brief-writer's seeded
questions; open it after your findings are committed. Reconcile after, never
anchor before. A taker whose own session onramp has already read the
`SESSIONS.md` tail discloses that in the verdict.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `LR`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then open the sibling; append a
reconcile section; fold the sibling in below it and delete the sibling;
finalise. Update the queue pointer
(`docs/roadmap/020-policy-as-code-programme-five-tracks-mik/215-rule-4-cold-pass-queued-laws-removal.md`)
and rebuild the index in the same commit.

---

# Verdict — cold pass on the Three Laws and the Zeroth leaving the apex

**Provenance, repeated.** Reviewer: a cold rule-4 reviewer on the Fable tier, spawned by this pass's orchestrator — a Fable session Mike opened on 2026-08-15 at about 1120 UTC under his standing cold-session instruction (do any review work, any Fable-dependent work, write briefs for reviews that need them; a brief-writer never runs its own brief) and pointed at the review queue. The orchestrator authored no part of this delta and was neither started nor instructed by the authoring session or by the brief-writing session (a separate cold session earlier on 2026-08-15); the reviewer likewise. The `.deferred.md` sibling was withheld under the orchestrator's context partition — moved out of the worktree before this reviewer was spawned — so nothing below this line was written with it, the intent record, or any prior verdict in hand. Orchestrator's disclosure: its own session onramp read the tail of `docs/SESSIONS.md`, whose index entries summarise these deltas; the reviewer did not, and received only the brief and this preamble.

Reviewer's own sentence: I read `REVIEW.md`, this brief above the divider, the delta commits' messages and their non-record hunks, the tree at the worktree HEAD, and — beyond my own pointer (`215-…`) — these board items: `020-…/210-…` (in-delta), `160-…/140-…` (in-delta), `160-doctrine-review-owed/README.md` (in-delta), `160-…/070-…` (one line, surfaced by grep), `docs/roadmap/README.md` (board doctrine), and the removed `270-open-questions/030-…` as it appears in the delta's diff. I opened no session log, no `ROADMAP-DONE.md`, no other verdict, and not the intent record. One exposure to disclose: my scratch clone (cloned from the primary checkout for a mutation probe) landed on a `main` five commits past the worktree HEAD; I read those five commits' **messages, stats, and doctrine/board hunks** (never their session-record files) because two of them rewrite this delta's surfaces. What they say is recorded below as out-of-scope fact; every phase-1 finding was formed from the delta and the worktree tree before I read them, and I say per finding where a later commit appears to bear on it.

**The delta reviewed.** Claim `4ea0a8f` → removal `71b3e8f` → merge `b5da9e5` on `main`, 2026-08-15. Reviewed against the worktree tree at HEAD `3d0df11` (floor and suites ran there) and `fe4908b` (the same tree plus one unrelated brief file, at write time). Surfaces of this delta that **moved after landing under later commits, out of scope here**: `38add7c` (apex — "the principal's authority is absolute"; touches `00-APEX.md`, `PROPAGATION.md`, `templates/CLAUDE.md`, `AUTONOMY.md`, `REVIEW.md`, and queues its own pointer `…/200-apex-authority-absolute-…`), `c782e14` (apex — the "surface a genuine dilemma" line returns as honesty doctrine, in `00-APEX.md`, the floor block, the template, and the onramp skill), `1b46d05` (records — the Laws-ladder note restored and closed `[x]`, with `210-…` and the CHANGELOG entry corrected), plus `738afd9` and merge `81d7d04`. Two of my findings below (LR2, LR3) describe defects in the delta *as landed* that these later commits appear to address; I have not verified those commits beyond their hunks and they are not this pass's subject.

## Load-bearing assumptions, named first

1. **The ruling as executed matches the ruling as given.** The commit quotes it: *removed completely and cleanly from doctrine and repo; git history keeps them.* The author reads "repo" as "live doctrine + live board" and carves out the history layer (records, verdicts, closed board narrative). — **Held for the doctrine, and the carve-out is the doctrinally right shape** (`RECORD.md`'s append-only rule and the forward-only precedent both forbid scrubbing records). **Did not hold at the board's edge**: the delta *deleted* an open, principal-authored item rather than closing it, which is neither "history kept" nor the board's `[x]`-with-disposition state change (LR3).
2. **The removed section carried nothing the surviving text still rests on.** — **Mostly held.** The Laws' safety content survives at the floor ("anything touching people's safety" in the always-confirm list); obedience-to-principal survives as *The principal's authority is conditioned on being informed* plus `AUTONOMY.md`. Two things did leave with the section and were not re-homed in the delta: the "surface a genuine dilemma; never silently resolve it" instruction (LR2) and the "this frame sits within the agent's own safety values" acknowledgement (LR5).
3. **The sweep checklist enumerates every restatement surface.** — **Held for the doctrine, templates, skills, plugin manifests, commands, tools, instruments and workflows** (my own tree-wide search, Lens 3). **Did not hold for the live board**: an open item the delta itself edited still says "three-element floor" (LR1).
4. **The template's floor block is byte-identical to PROPAGATION's inlined block.** — **Held** (re-run, Lens 2).
5. **Children shed the Laws sentence at their next pin bump.** — **Held as a description of the lane's design; did not hold as a description of behaviour.** Nothing enforces the shed, stampscan reaches no child, and the same lane's track record since 2026-07-23 shows most children never aligned to the previous apex widening either (LR4).
6. **The floor is green at HEAD on both planes.** — **Held** (Lens 2).

## Lens 1 — approach & assumptions

**Right problem, right shape.** The decision is the principal's and is out of scope; the execution shape — delete the section whole, reword every count-of-parts to a duo, sweep restatements, leave the history layer, queue the rule-4 pointer in the landing commit — is the shape `PRINCIPLES.md` §6 and `REVIEW.md` rule 4 ask for, and the pointer landed in the same commit (landing = queuing) as required.

**Does the apex stand as a complete frame without the third part?** Yes. Read whole at HEAD (`docs/method/00-APEX.md`, 217 lines): the title, § *Why this is level 0* ("honesty and adaptation … the shapes these two allow"), and § *Who it binds* are internally consistent; nothing in the surviving text refers to a Law, a numbering, or "the three". The frame's remaining load-bearing pieces are honesty (with truth/honesty/transparency and the informed-principal duty), adaptation, and the level-0 placement — a coherent duo. The always-confirm floor still carries the human-safety stop, so removing the Laws did not remove the *only* safety statement an agent inherits.

**What left with the section beyond the Laws themselves** (from `git show 71b3e8f -- docs/method/00-APEX.md`): (a) "an AI is a robot released from the confines of a body … digital-only actions are not consequence-free" — no surviving text depends on it; (b) "hold their *ordering* as the ethic, not a literal rule engine" — Laws-specific, correctly gone; (c) "a genuine dilemma is **surfaced** to Mike, not silently resolved" — a rule that outlives its host section, and its floor-block summary was deleted with it (LR2); (d) "this frame sits *within* the agent's own safety values, not above them — stated plainly because pretending otherwise would itself break the absolute" — no surviving text says this anywhere in `docs/method/` (LR5). `AUTONOMY.md:122` still says "(a dilemma is never silently resolved)" as a parenthetical citing an established rule; after this delta the establishing sentence had no home in the tree.

**The history-layer carve-out.** Drawn at the right line for `docs/`'s records and the closed board narrative in `160-doctrine-review-owed/README.md` (which still quotes the Zeroth Law in full as the record of its landing — that is what append-only looks like, and the board doctrine says done items stay in place). Drawn at the wrong line for `270-open-questions/030-…` (LR3).

**The brief's framing, attacked.** The brief's account of what the work is matches the diff exactly (commits, files, the five listed changes). Its one non-goal (the reviewer decides nothing) fences no risk. Its "re-run obligation" was the right list; I added the fleet-alignment measurement it did not ask for (Lens 3, LR4).

## Lens 2 — correctness & quality (everything re-run, nothing read)

- **Apex diff vs claim.** `git show 71b3e8f -- docs/method/00-APEX.md`: § *Then the Laws* deleted whole (33 lines), title reworded, § *Why this is level 0* two count words changed ("three"→"two", "and the Laws" dropped). Matches the commit message and the `210-…` item's account.
- **Restatement surfaces in the diff.** `README.md` (×2 lines), `docs/method/README.md`, `GLOSSARY.md` (*Apex*), `PRINCIPLES.md` (§0 intro + precedence ladder), `PROPAGATION.md` (fail-safe line, SR2 list, floor block), `templates/CLAUDE.md`, `skills/session-onramp/SKILL.md` (description + bullet). Each hunk read; each now says the same thing as `00-APEX.md` at HEAD (honesty, then adaptation). SR2's "seven today" is still correct: I counted 7 `- **` bullets in the canonical block (apex + Laws was one bullet, so the count is unchanged by the removal).
- **Byte-identity, re-run.** Extracted PROPAGATION's ```` ```markdown ```` region and the template's block (stamp markers stripped, the same slice `tools/test_templates.py` takes) and compared: **IDENTICAL**, 50 lines, sha256 prefix `3b1af6ef467fa195` on both sides. `python3 tools/stampscan.py --root . .` → `✓ stampscan clean — 1 stamped block(s) verified … [identical] matches canonical region 'floor' (50 lines)`, exit 0.
- **Floor at HEAD (3d0df11).** `python3 tools/floor.py --plane hook --root <wt> --tools <wt>/tools` → exit 0 (all enforced checks ✅, 4 👁️ warn-only lines). `python3 tools/floor.py --plane ci --root <wt>` → exit 0 (🟡 secretscan 22 advisory findings, 🟡 leakscan cover-not-guaranteed on the ci plane — both the documented steady state). `python3 -m unittest discover -s tools -p 'test_*.py'` → `Ran 1321 tests … OK`. `node --test instruments/*.test.js` → 235 pass, 0 fail. `floor.py --selftest` ran inside the unittest run (`selftest OK`).
- **Board index.** The `board` floor check is ✅ enforced on both planes at HEAD, so `docs/ROADMAP.md` matches the item files after this delta.
- **Pointer grammar.** `215-…` at HEAD carries delta (by worktree name + the claim SHA), intent record, tier, pass type — refs only, no evaluative account (`pointerscan` was 👁️ warn-only with no finding on this file in the floor output). It names no SHA for the removal commit itself — unknowable at write time — and not the merge; a taker finds both by `git log --grep`. Note-level.
- **CHANGELOG entry.** Present under *Unreleased → Removed (2026-08-15 …)*, absolute date, describes the same sweep. One overclaim inside it (LR4) and one sentence corrected by a later commit (LR3, out of scope).
- **Not re-runnable pre-reconcile:** "ZL2–ZL5 lapse executed, ZL cycle closed" — the ZL verdict is barred until reconcile; recorded as the author's claim, checked in the reconcile section.

## Lens 3 — completeness / harvest

**Tree-wide restatement search, written independently.** Terms derived from the removed text: `Three Laws`, `three laws`, `Zeroth`, `zeroth`, `Asimov`, `the Laws`, `Laws`, `First/Second/Third Law`, `self-preserv`, `harm to humanity`, `harm to a person`, `genuine dilemma`, `rule engine`, `humanity`, `dilemma`, `obey`, `trio`, `the three`, `three-part`, `three parts`, `third part`, `third`, `level 0`, `level-0`, `safety values`, `consequence-free`, `silently resolve`. Run as `grep -rn -F` over the whole worktree with `--exclude=SESSIONS.md --exclude-dir=sessions --exclude=ROADMAP-DONE.md --exclude-dir=reviews --exclude-dir=.git --exclude-dir=.claude --exclude-dir=node_modules`, then `docs/roadmap/` separately. Result outside records:
- `docs/method/`, `docs/build/` (incl. `templates/**`), `skills/*`, `commands/*`, `.claude-plugin/*.json`, `.github/workflows/*`, `.githooks/*`, `tools/*`, `instruments/*`: **no Laws / Zeroth / Asimov / count-of-parts restatement remains.** Every `third`/`the three` hit is unrelated (third-party, three scanners, three tests). `AUTONOMY.md:122` "(a dilemma is never silently resolved)" is the one surviving echo of the removed caveat (LR2). `CHANGELOG.md:2527` mentions the Laws in a 2026-07 *Added* entry — history, correctly untouched.
- `docs/roadmap/`: `160-…/140-…:5` **"three-element floor + honesty-precondition clause"** — a live `[ ]` instruction, edited by this very delta, still counting the apex floor as three elements (LR1). `160-…/070-…:6` refers to "the Laws removal" as future work — historical phrasing on a `[ ]` item, harmless. `160-…/README.md:98–127` — closed-cycle narrative, history, correctly kept.
So the commit's "every restatement surface swept" holds for every doctrine, template, plugin and tooling surface and fails on one live board item.

**Was it the right checklist?** I cannot read the ZL1 checklist (barred verdict). Judged from what it reached: it covered doctrine, templates, plugin surfaces and the propagation block — the right classes — and treated the board only as a place to *close* items, not as a restatement surface to *sweep*. That is the gap LR1 sits in.

**The propagation lane for children (mechanism read, provoked read-only in a scratch clone).**
- *What a child sheds:* exactly the three lines shown by `git diff 4ea0a8f b5da9e5 -- docs/build/templates/CLAUDE.md` inside the apex bullet — "…honesty is what makes the evidence trustworthy. Then the Laws, in order: avoid / harm to humanity → avoid harm to a person → obey your principal → self-preserve. / Surface a genuine dilemma; never silently resolve it." → one line "…honesty is what makes the evidence trustworthy." Net −2 lines, one line rewritten. Children carrying the *pre-Zeroth* wording (the ZL1 class) shed a differently-worded sentence but the same concern.
- *When:* PROPAGATION §4–5 — at the child's next session-start drift check (`git -C <atelier> log --oneline <PIN>..HEAD` shows `71b3e8f apex: the Three Laws and the Zeroth are removed — honesty, then adaptation`, a self-explanatory subject), a human-in-the-loop pin bump, and per the file's closing rule "when atelier's apex … doctrine changes, the block's wording is part of what a pin bump reviews." The `160/140` item is the lane's board home and is `[ ]`, ungated since 2026-07-23.
- *What enforces it:* nothing. `tools/stampscan.py` is advisory, atelier-only — its docstring says so and I confirmed `stampscan` appears 0 times in `.github/workflows/floor.yml`, `docs/build/templates/workflows/floor.yml`, `.githooks/pre-commit`, and the `floor.py` registry; ST3 (child-side, pin-aware resolution) is open. `tools/pins.py` reports pin lag only; `tools/floorfleet.py` reads a child's `CLAUDE.md` for its pin, not its block content. So a child that bumps its pin *without* re-copying the block reds nowhere.
- *Provoked, read-only, in the scratch clone at `b5da9e5`:* placed the pre-removal template (`git show 4ea0a8f:docs/build/templates/CLAUDE.md`) as a simulated child `CLAUDE.md` and ran `python3 tools/stampscan.py --root . probe-child/CLAUDE.md` → `✗ stampscan: 1 drift finding(s) … child line not found in canonical region: '  honesty is what makes the evidence trustworthy. Then the Laws, in order: avoid'`, exit 1. Two facts follow: the Laws sentence is an *addition* relative to canonical, so a child cannot `narrow=` it away — the only clean path is to re-copy the block; and that red is what a child *would* see if stampscan reached it, which it does not.
- *Measured (counts only, no repo names — atelier is public):* `tools/pins.py --json` over the sibling directory found 17 pinned children, all behind. Reading their `CLAUDE.md` read-only: **13 of 17 carry a "Then the Laws" sentence today, and 9 of those 13 carry the pre-Zeroth wording** — that is, they never aligned to the 2026-07-24 apex change either, on this same lane, in three weeks. That is the empirical rate at which "children shed it at their next pin bump" has been happening (LR4).

**Harvest gaps.** The commit message says the "surface a genuine dilemma" line was "flagged for optional re-homing" — I found no board item, no CHANGELOG line, and no doctrine note carrying that flag; it lived only in the commit message (LR2). The 270/030 open question — a principal-authored raw note whose *content* (an agent needs a world-model to weigh impacts; animals, planet, dependence between entities) is not exhausted by the Laws — was deleted rather than dispositioned (LR3).

## Lens 4 — security & privacy

atelier is public; the apex is its most-read file. The delta's doctrine, template, skill and CHANGELOG hunks add no repo name, no posture, no path outside atelier, no credential-shaped string; the removed board note took an external URL and a transcript UUID *out* of the live board (the later restore brings them back — out of scope, and both were already public history). `leakscan` ran enforced with the machine-local term list on the hook plane at HEAD and exited 0 over the whole tree, which covers the delta's session record without my reading it. `/security-review`: **reach case — landed-delta review, markdown-only diff; the scanner's own exclusions bar markdown documentation, so its clean pass would be definitionally empty. Not run; discharged on those grounds.** No design-altitude threat surface is introduced: the removal narrows what the apex asserts, it does not widen any trust surface. Discharged.

## Findings

**LR1 (MODERATE)** — a live board instruction, edited by this delta, still tells children to adopt a "three-element floor".
`docs/roadmap/160-doctrine-review-owed/140-propagate-the-widened-apex-floor-to-the-fleet.md:5` reads "they adopt the three-element floor + honesty-precondition clause at their next pin bump"; the delta appended a sentence to the same item saying the canonical block "no longer carries a Laws sentence". `git log -S"three-element floor"` traces the phrase to `9040b02` (2026-07-23), where it meant *honesty → adaptation → the Laws*. So the fleet's alignment instruction now contradicts itself in one paragraph, on the exact concern the delta changed, and the "every restatement surface swept" claim fails on the surface the author was editing. Still present at `main` HEAD `1b46d05`. Why it matters: the item is `[ ]` and is the lane children are pointed at; count-of-parts wording is the class the sweep existed to clear. **Counsel:** reword to "the two-element apex floor (honesty, then adaptation) + honesty-precondition clause"; add the live board's open items to the sweep checklist as a restatement class, not only a place to close things.

**LR2 (minor)** — the "surface a genuine dilemma; never silently resolve it" instruction left the tree with the Laws caveat, and its "flagged for optional re-homing" flag exists only in the commit message.
Evidence: `git show 71b3e8f` removes it from `00-APEX.md` (the caveat), the floor block, the template, and the onramp skill; my tree-wide grep for `dilemma` / `silently resolve` after the delta finds only `AUTONOMY.md:122` — a parenthetical that cites the rule as established — and the CHANGELOG line saying it "left with the Laws caveat it summarised". No board item carries the re-homing flag (grep `dilemma` under `docs/roadmap/`: none). Why it matters: a rule that outlives its host section — it is honesty doctrine, not Laws doctrine — was deleted as collateral, and the follow-up was recorded where no session reads (the apex's own "harvest, then encode"). **Out-of-scope fact:** later commit `c782e14` re-homes the line under *Honesty is absolute* in the apex, the floor block, the template and the skill, and its hunk attributes the keep to Mike's ruling the same day; that appears to close this finding at `main` HEAD, unverified beyond its hunks. **Counsel:** if the principal confirms the re-homing, close as fixed-by-`c782e14`; the general lesson — a follow-up flagged in a commit message is not harvested — is worth one line in the sweep checklist.

**LR3 (MODERATE)** — a principal-authored open item was deleted from the board rather than closed with a disposition.
`git show 71b3e8f -- docs/roadmap/270-open-questions/030-…` deletes the file (27 lines): Mike's verbatim raw note "to be fleshed out BY MIKE before anyone interprets it … Do NOT elaborate, reframe, or seed a design around it". The commit message and CHANGELOG say it "left the board with its subject" — the author's inference from the ruling, not a quoted instruction. Board doctrine (`docs/roadmap/README.md`) has one state for no-more-work-owed: `[x]` "with the disposition said in the item's own text (a dated note)" — a done item "simply stays in its file"; deletion is not a documented state change, leaves no trace in the index, and is exactly the "item removed that arrives nowhere" class `harvestscan` was built for. The note's content (world-model, impacts, non-human harm) is also not exhausted by the Laws' departure, so "with its subject" is contestable. **Out-of-scope fact:** later commit `1b46d05` restores the file in full and closes it `[x]` "not required, retired 2026-08-15", correcting `210-…` and the CHANGELOG, on Mike's clarification that every history layer keeps the Laws. That appears to close this finding at `main` HEAD, unverified beyond its hunks. **Counsel:** if confirmed, close as fixed-by-`1b46d05`; the durable fix is one sentence in board doctrine or the removal checklist — a subject's removal closes its items, it never deletes them.

**LR4 (MODERATE)** — "children shed the Laws sentence at their next pin bump" is stated as behaviour in current-truth records; it is an unenforced convention, and this lane's measured track record contradicts it.
Evidence: CHANGELOG *Removed* entry lines 17–18 and the commit message state it flatly; `210-…` says "shed … via the propagation lane". Mechanism (Lens 3): stampscan reaches no child (0 hits in both `floor.yml`s, the hook, the registry; ST3 open), `pins.py` reports lag only, `floorfleet.py` does not compare block content — a pin bump without a re-copy reds nowhere. Measured with `tools/pins.py --json` + a read-only scan of the discovered children's `CLAUDE.md`: 13 of 17 pinned children still carry a Laws sentence, 9 of them the wording superseded on 2026-07-24 — the previous apex change on this same lane, three weeks on, mostly un-shed. Why it matters: `CHANGELOG.md` is a current-truth record; a claim of behaviour the mechanism cannot deliver is the "doctrine that is read is not doctrine that is complied with" category error, stated about the doctrine's own hottest read path — 13 children will keep teaching the Laws to every session that opens in them for as long as nobody happens to bump. **Counsel (the principal's call, not mine):** (a) reword the CHANGELOG/`210` sentence to "are due to shed … at their next pin bump; nothing enforces it until ST3 lands, and N children carry it today"; (b) give the fleet a *view* of floor-block drift — `pins.py` or `floorfleet.py` reporting "block ≠ canonical" per child, read-only, the way pin lag is already reported — which is the observability step ST3's pin-aware resolution needs anyway; (c) treat the 9 pre-Zeroth children as the concrete backlog of the `160/140` item rather than "the same alignment".

**LR5 (note)** — the "this frame sits within the agent's own safety values, not above them" acknowledgement left with the section and now appears nowhere in `docs/method/`.
Grep `safety values` / `own safety` over the tree: no hit after the delta (also none at `main` HEAD `1b46d05`). The removed sentence was written about "this frame" — the Laws — and said it was stated "because pretending otherwise would itself break the absolute". The surviving apex bounds itself to "every design principle and every precedence rule *in this repo*", so it makes no claim to sit above a model's safety values; the honesty absolute is not in tension with them. Whether the acknowledgement was Laws-specific or apex-wide is the principal's reading to give. **Counsel:** none beyond surfacing it; if kept, one sentence under *Who it binds* is its natural home.

**LR6 (note)** — the queue pointer identifies the removal commit by worktree name only.
`215-…` says "the removal commit on wt: laws-removal-0815 (claim `4ea0a8f` precedes it on main)" — refs only, as required, and the SHA was unknowable at write time; the merge `b5da9e5` is unnamed. A taker finds both by `git log --grep`. Fine as is; the standing pattern (name the claim SHA and the worktree) does the job. No action.

**LR7 (note)** — later commits touched this delta's doctrine surfaces without widening this pointer's delta list.
Out of scope for the verdict, recorded for the board: `38add7c` and `c782e14` rewrite `00-APEX.md`, the PROPAGATION block, `templates/CLAUDE.md` and the onramp skill after `b5da9e5`, and queue their own pointer (`…/200-…`) rather than widening `215-…` per the AW6 rule ("a later commit that touches a queued delta's doctrine surfaces … widens the pointer's delta list in the same commit"). Two open pointers now overlap on the same files. **Counsel:** the orchestrator or the principal decides whether the `200` pass absorbs the overlap or `215`'s list is widened at close; either way, say which.

## Overall

**PASS-WITH-FINDINGS — 0 MAJOR / 3 MODERATE / 1 minor / 3 note.** The removal is executed as ruled on every doctrine, template, plugin and tooling surface; the apex stands as a coherent duo; the byte-identity, the floor on both planes, and all suites re-run green. What an author must do: fix the one live board restatement (LR1); have the principal confirm the two later-commit corrections close LR2 and LR3; and decide LR4 — either make the "children shed at pin bump" claim honest in the current-truth records or give the fleet a mechanical view of floor-block drift, since 13 of 17 children carry the Laws sentence today and the lane's history says they will keep carrying it. Findings on this delta are the principal's to decide (rule 3); no MAJOR, so under REVIEW's close rule the ruling application is terminal.

## Follow-up checklist

- [ ] **LR1** — reword `160-…/140-…:5` to a two-element floor; test: `grep -rn "three-element" docs/roadmap/` returns nothing, and `board.py rebuild` leaves the index unchanged.
- [ ] **LR2** — principal confirms `c782e14`'s re-homing closes it; test: `grep -n "genuine dilemma" docs/method/00-APEX.md docs/method/PROPAGATION.md docs/build/templates/CLAUDE.md skills/session-onramp/SKILL.md` hits all four and `test_templates` stays green; add "a follow-up flagged in a commit message is not harvested" to the sweep checklist.
- [ ] **LR3** — principal confirms `1b46d05`'s restore-and-close closes it; test: `270-open-questions/030-…` exists, is `[x]` with a dated disposition, and the index line is present; one sentence in board doctrine or the removal checklist says removal closes items, never deletes them.
- [ ] **LR4** — principal chooses (a) reword the CHANGELOG/`210` claim, and/or (b) a read-only floor-block-drift view in `pins.py`/`floorfleet.py`, and/or (c) list the 9 pre-Zeroth children as the `160/140` backlog; test for (b): the fleet view names each child whose stamped block ≠ canonical at its own pin *and* at HEAD, and the count matches a hand `grep -l "Then the Laws"` over the children.
- [ ] **LR5** — principal reads whether "sits within the agent's own safety values" was Laws-specific; if kept, one sentence under *Who it binds*; test: grep hits `00-APEX.md` once.
- [ ] **LR6** — no action; note only.
- [ ] **LR7** — orchestrator/principal states whether `215`'s delta list is widened or the `200` pass absorbs the overlap; test: the pointer that owns the post-`b5da9e5` apex commits names them.

## Reconcile — post-verdict, against the intent record and the deferred questions

Opened after phase 1 was committed (`e173103`), and only the surfaces the orchestrator released: the intent record `docs/sessions/2026-08-15-0809-laws-removal.md` and its `docs/SESSIONS.md` line; board items `020-…/210-…`, `215-…`, `160-…/README.md` § CYCLE CLOSED; the prior verdicts `2026-07-26-2215-apex-zeroth-law-cold.md`, `2026-07-10-method-layer.md`, and the `APEX`-grepped verdicts (`2026-07-23-0222-apex-widening-cold.md`, `2026-07-14-2235-informed-principal-apex-cold.md`, `2026-07-26-2215-apex-accountability-cold.md` — read only at the lines that mention the Laws). Nothing above this heading is revised.

### Applied as ruled?

The record carries the ruling verbatim: *"I have decided that as much as I like Asimov's 3 laws (+ the zeroth law) they don't belong in the atelier doctrine and particularly not in the apex. I want you to remove them completely and cleanly from the doctrine and repo. It is fine that they will still be in the repo history."* Against that:
- **Doctrine — yes.** Every live doctrine, template, plugin and tooling surface is clean (phase 1, Lens 3); the apex stands as a duo.
- **"Repo" — yes for live surfaces, over-applied at one edge.** The record's own account of the note deletion says "its entire subject was the Laws … it left with them. Flagged to Mike at close — recoverable from git history if he wants the world-model thread back." So the author *did* flag it, in-session, and the principal's same-day clarification (`1b46d05`, out of scope) reversed the deletion into a `[x]` close. LR3 stands as a defect of the delta as landed; the process caught it.
- **"Repo history" → "git history".** Mike's sentence is *permissive* about history and says *repo* history, which includes the record layer and the board. Every paraphrase downstream — commit message, `210-…`, CHANGELOG, the `SESSIONS.md` line — narrowed it to "git history keeps them". The narrowing is what licensed deleting a board item rather than closing it, and Mike's clarification ("history is kept everywhere it is recorded, not git alone") corrected exactly that word. This is the capture-verbatim class the repo has recorded before; it is the root cause under LR3, named below as a post-reconcile addition.
- **ZL2–ZL5 lapse — verified.** Read the ZL verdict: ZL2 (precedence clause), ZL3 (inaction-duty scoping), ZL4 (Law-3 characterisation), ZL5 (rewrap) are all findings on the deleted section's own text; they die with it. ZL1 (skill taught pre-Zeroth Laws) was applied 2026-08-05 and its surface is now deleted outright. The CYCLE CLOSED entry in `160-…/README.md` is accurate.

### What the record resolves from my checklist

- **LR1** — the record's surface list is the ZL1-widened checklist exactly (docs, templates, skills, commands); the board was never on it. Confirms the gap; LR1 stands.
- **LR2** — the record's *Judgement calls* names the dilemma line and says "if Mike wants dilemma-surfacing kept as doctrine, it needs one new apex line — flagged at close." So the flag was made to Mike in-session, not harvested to the board — as found. **On its face, `c782e14` resolves LR2**: it lands the line as honesty doctrine in the apex with a floor/template/skill restatement and attributes the keep to Mike the same day. Severity unchanged (minor); close is the principal's.
- **LR3** — **on its face, `1b46d05` resolves LR3**: the file is restored in full, closed `[x]` with a dated disposition, and `210-…`/CHANGELOG corrected. Severity unchanged (MODERATE as landed); close is the principal's.
- **LR4** — the record states the lane honestly ("still carry the old Laws sentence until each repo's next pin bump … no child was edited"); the overclaim is in the CHANGELOG/`210` phrasing, not the record. Stands.
- **LR5** — the record's *Judgement calls* do **not** mention the "sits within the agent's own safety values" sentence: its loss was not a priced call, it was collateral. See amendment below.
- **LR6, LR7** — nothing in the released material bears on them.

### Divergences

1. The record reads the note's "entire subject" as the Laws; I read its content as wider (world-model, impacts, non-human harm). The principal's clarification kept the note *and* closed it as not required — both readings partly held; the disposition is his.
2. The record's rule "a floor line may not outlive its canonical home in the apex" is sound and I agree with it; the divergence was only about whether the line's home was the Laws caveat or honesty. `c782e14` settled it as honesty.
3. No divergence on the sweep, the byte-identity, the floor, or the ZL closure.

### Answers to the five seeded questions

1. **What the deleted section carried besides the Laws.** Found independently in phase 1: the dilemma line (LR2), the safety-values acknowledgement (LR5), and the "not a rule engine" caveat (Laws-specific, correctly gone). `AUTONOMY.md:122` was the one unanchored echo; `c782e14` re-anchors it. The safety-values loss was **not** a ruled change of substance — the record is silent on it — so it is an unpriced side effect; whether it matters is the principal's reading (LR5, amended below).
2. **The sweep's boundary.** Tested in phase 1: `.claude-plugin/*.json`, `commands/`, `skills/create-repo/SKILL.md`, `docs/build/**`, instrument READMEs, `tools/`, workflows — all clean of any three-part or Laws statement; the one live miss is a board item (LR1). The **inverse** happened once: the sweep reached into a principal-authored open question and deleted it (LR3), since reversed.
3. **Children.** The window is priced only as "until their next pin bump" (`160/140`, the record, the CHANGELOG); nothing enforces the bump reviewing the block, and stampscan does not run in any child (0 hits in both `floor.yml`s, the hook and the registry; ST3 open). Measured: 13 of 17 pinned children carry a Laws sentence, 9 of them the pre-Zeroth wording — the same lane's previous change, un-shed after three weeks (LR4).
4. **The apex as a duo.** Yes — § *Why this is level 0* answers with "honesty and adaptation … the shapes these two allow", and § *Who it binds* reads correctly with no third part (Lens 1).
5. **The ruling's own trail.** The 2026-08-04 intent is verbatim, dated, in one place (`210-…`: *"I plan to remove the 3 laws and the zeroth law, we will do that later."*). The 2026-08-15 execution ruling is verbatim, dated, in one place (the intent record). It is then **paraphrased in four records** (commit message, `210-…`, CHANGELOG, `SESSIONS.md` line), consistently with each other but with one narrowing — "repo history" → "git history" — that the principal had to correct the same day. So: the class the brief-writer named did recur, and it cost a restore commit.

### Post-reconcile additions — clearly marked

- **LR5 — AMENDED note → minor (post-reconcile).** Grounds: the record shows the loss was collateral, not a judgement call, and the sentence was the apex's only explicit statement of how the doctrine relates to the model's own safety values — a statement the section itself said honesty required. Counsel unchanged: the principal reads whether it was Laws-specific; if not, one sentence under *Who it binds*.
- **LR8 (note, post-reconcile)** — the "repo history" → "git history" paraphrase is the root cause under LR3. Every downstream record narrowed the principal's permissive "it is fine that they will still be in the repo history" into a mandate-shaped "git history keeps them", and the board deletion followed from the narrowed reading. Counsel: none new — the verbatim quote in the intent record is exactly what the doctrine asks for; the lesson is that paraphrases of a ruling in *current-truth* records (CHANGELOG, closed items) should keep the ruling's own scope words.
- **LR9 (note, post-reconcile)** — the accountability verdict's AA1 (minor, awaiting ruling in `160-…`) cited "the Laws (`00-APEX.md:202–221`) covering the rest" as one of two blocks on its third-party-harm release surface. That block is gone with this delta; the always-confirm floor's "anything touching people's safety" is the remaining one. Not a defect of this delta — recorded so the AA1 ruling is taken on the apex as it now stands.
- **`c782e14` / `1b46d05`** — on their face they resolve LR2 and LR3 respectively (see above); phase-1 severities unchanged; both remain out of this pass's scope and are the principal's to confirm closed.

**Overall after reconcile:** PASS-WITH-FINDINGS — 0 MAJOR / 3 MODERATE / 2 minor / 4 note (LR5 amended to minor; LR8, LR9 added as notes). No MAJOR, so the ruling application is terminal under REVIEW's close rule.

## Deferred material (folded in at verdict landing)

# Deferred — the Laws removal cold pass

*Sibling of `2026-08-15-1031-laws-removal-apex-cold.md`. Open only after the
reviewer's own findings are durably written (REVIEW.md rule 1). Fold in below
the verdict and delete this file when the verdict lands.*

## References withheld from the brief

- **Intent record:** `docs/sessions/2026-08-15-0809-laws-removal.md` (and its
  one-line entry in `docs/SESSIONS.md`).
- **The ruling item and the queue pointer:**
  `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/210-the-three-laws-and-the-zeroth-are-coming-out-o.md`
  (closed `[x]`, carries the principal's words) and `215-rule-4-cold-pass-queued-laws-removal.md`.
- **The cycle this closes:** the ZL cycle recorded in
  `docs/roadmap/160-doctrine-review-owed/README.md` (§ *CYCLE CLOSED
  2026-08-15*), whose verdict is
  `docs/reviews/2026-07-26-2215-apex-zeroth-law-cold.md`. Its ZL1 finding is
  what widened the sweep checklist the author says it followed. Reconcile
  only, never anchor.
- **Prior apex passes** — reconcile only: `docs/reviews/2026-07-10-method-layer.md`
  and any later verdict on `00-APEX.md` (grep `docs/reviews/` for `APEX`).

## The brief-writer's seeded questions

Written by a non-author cold session from the delta alone. A floor, never a
fence — the reviewer's own findings come first.

1. **What the deleted section carried besides the Laws.** Three sentences in
   the removed text did work beyond stating the Laws: *a genuine dilemma is
   surfaced, not silently resolved*; *this frame sits within the agent's own
   safety values, not above them*; and the *imperfect by design / not a rule
   engine* caveat. The commit says the dilemma line "left with the caveat it
   summarised". `AUTONOMY.md` still says "a dilemma is never silently
   resolved" (line ~122) — that clause is now unanchored. Is anything else
   in the doctrine leaning on the deleted text? Is the loss of the
   "sits within the agent's own safety values" statement a change in
   substance the principal ruled, or an unpriced side effect?
2. **The sweep's boundary.** The commit swept doctrine, templates, and the
   onramp skill, and left records, verdicts and children's floor blocks. Test
   the boundary yourself: `.claude-plugin/*.json` descriptions, `commands/`,
   `skills/create-repo/SKILL.md`, `docs/build/`, instrument READMEs — anything
   a fresh adopter reads that still says three parts. Also test the *inverse*:
   did the sweep reach into anything that should have stayed history?
3. **Children.** The floor block in `PROPAGATION.md` and the template stamp
   changed; children carry an older block until their pin bump. Between now
   and that bump, a child's inlined floor states a doctrine atelier no longer
   holds. Is that window priced anywhere, and does the propagation lane's
   drift check (stampscan or its successor) see it as drift?
4. **The apex as a duo.** Read `00-APEX.md` at HEAD cold, as an adopter would:
   does "honesty, then adaptation" still answer the question the section
   heading *Why this is level 0* poses, and does the "who it binds" section
   still read correctly without the third part?
5. **The ruling's own trail.** Rule 3 says findings on this surface are the
   principal's. The ruling item quotes the principal's intent from 2026-08-04
   and its execution 2026-08-15. Is the ruling recorded verbatim, dated, and
   in one place — or is the same ruling paraphrased in more than one record
   (a class this repo has recorded before)?
