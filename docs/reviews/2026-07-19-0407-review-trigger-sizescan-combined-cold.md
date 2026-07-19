# Cold review — the review-trigger/design-review deltas + the sizescan doctrine deltas (combined pass)

**Date**: 2026-07-19 · 0407 UTC · **Status**: brief written, review pending

## Spawn provenance (REVIEW.md rule 4)

This review is spawned by a session Mike opened fresh with "Do any reviews, use
a worktree" — a session the deltas' authors neither started nor instructed. The
authors (two Opus sessions, 2026-07-18 and 2026-07-19, one of which also
authored the sizescan gate split) queued the `⏳` pointer and wrote no brief,
per rule 4. This brief is written by the taking session (Fable), which authored
none of the deltas under review. The cold reviewer is a fresh-context agent
spawned by the taker. Claim: `d43ca75` on `main`; work in worktree
`fable-cold-pass`.

## Subject (refs only)

Three doctrine deltas, queued as **one pass**. Review the named files **at
HEAD** (`d43ca75`) — later records commits amended wording, so the diffs are
how the deltas arrived, HEAD is what is binding.

1. **`method/REVIEW.md` § "Review the design, not only the build"** + the
   review-line convention. Commit `30c9cd9`. Intent record (deferred — see
   divider rule): `docs/decisions/2026-07-18-0820-review-the-design-not-only-the-build.md`.
   A sibling application exists in the private `ros` repo at `ros@55d0d51`
   (`~/.pets/ros`: `CLAUDE.md` + ROADMAP review policy) — in scope at your
   discretion; findings about it stay repo-generic in this public file.
2. **The trigger re-key + fork→pointer conversion.** Commit `4c17f59`:
   `method/REVIEW.md` (§ "Whether work earns a review at all"),
   `build/templates/docs/reviews/README.md`, `method/MODEL-ECONOMICS.md`,
   `build/templates/CONTRIBUTING.md`. Intent record (deferred):
   `docs/decisions/2026-07-19-0100-review-trigger-is-commitment-not-artefact.md`.
   A same-day records follow-up widened the delta (`REVIEW.md` intro,
   `method/PROPAGATION.md` enforcement clause) — those lines are in scope at
   HEAD.
3. **The sizescan doctrine deltas**: the grounded-budgets rule in
   `tools/sizescan.py`'s module doc, the `GATED` tripwire/advisory gate split
   (+ `tools/test_sizescan.py`), and the
   `build/templates/workflows/floor.yml` comment rewrite. ⚠️ Provenance fact
   you need to locate the delta: this code entered history inside `4fb09a7`,
   a *different* session's records commit that absorbed it from a shared tree —
   that commit's message does not describe it (acknowledged in `b33f072`).

Also before this pass, from the queue: **rule on the open question** whether
`method/PRINCIPLES.md`'s header ("every build is measured against") keeping the
build grammar is a defect the commitment re-key should have caught, or
correctly out of scope (design principles bind at design time).

## Ask

Review deep, not fast, all three lenses (`method/REVIEW.md` § What a review
actually checks): approach & assumptions — name and attack the load-bearing
assumptions yourself, as your **first act**; correctness & quality —
overclaims, silent scope-cuts, honesty of the records; completeness/harvest —
what the deltas should have covered and didn't, what they duplicated or
ignored. The framing of this brief, including its account of what the work is,
is itself attackable.

**Sequencing (rules 1–2, binding):**

1. Commit your own attack surface to your verdict draft **first**.
2. Only then open anything below the divider (the intent records, the authoring
   sessions' log entries) and any prior verdict files — to reconcile, never to
   anchor.

**Re-run every recorded proof in scope** — a proof you have not re-run is not a
proof you can close on. Recorded proofs include: the tool suite green
(`cd tools && python3 -m unittest` — records claim 267), the template drift
test (`tools/test_templates.py`), both live sizescan gate behaviours (a gated
file over budget → exit 1; a judgement doc over budget → `[advisory]`, exit 0 —
scratch fixtures are fine), the scans clean at HEAD (secretscan, leakscan,
linkscan, sizescan), and the claim that the stamped reviews-template pointer
resolves in a `create-repo`-shaped child (the old template's relative link is
recorded as having been broken in every stamped child — verify the new wiring,
don't assume it).

**Verdict**: append below this file's `---` divider. Stable IDs (F1…), severity
MAJOR / MEDIUM / LOW, per-lens coverage, spawn provenance repeated, your
attack-surface commit named, every re-run proof listed with its result. Apply
**nothing** (rule 3 — self-authored doctrine): the findings go to the
principal; the taker will add author-independent counsel but the decisions are
Mike's. Cycle close rule: this cycle closes only on a no-MAJOR pass plus the
principal's ruling.

---

## Deferred — open only after your attack surface is committed

Author-side evaluative accounts (the authors seeded no questions; these records
carry their framing):

- `docs/decisions/2026-07-18-0820-review-the-design-not-only-the-build.md`
- `docs/decisions/2026-07-19-0100-review-trigger-is-commitment-not-artefact.md`
- `docs/sessions/2026-07-19-0111-review-trigger-commitment-not-artefact.md`
  (author's log + a Fable retrospective addendum — the retrospective is itself
  an author-adjacent account, not a cold verdict)
- `docs/sessions/2026-07-18-1655-fleet-file-size-sweep-ros-shed.md` (the
  sizescan deltas' authoring session; its 1830 and tripwire addenda)
- Prior verdicts in `docs/reviews/` (notably `2026-07-14-2048-lean-files-sizescan-cold.md`
  — the grounded-budgets rule's origin) — rule 2: reconcile-step only.

---

# Verdict

**Reviewer**: cold-context agent (Fable), spawned by the rule-4 taking session.
Attack surface written and committed 2026-07-19 ~0404 UTC, before any deferred
material (intent records, authoring sessions' logs, prior verdicts, the brief's
below-divider section) was opened.

## Attack surface — the load-bearing assumptions I will attack (chosen cold)

Named from the brief's top section, `method/` docs, and the subject files/diffs
at HEAD only.

1. **The grounding narrative's internal consistency.** `REVIEW.md`'s
   enforcement paragraph still asserts the 2026-07-18 `ros` session broke the
   rule "while the correct rule sat in three places it had access to" — yet the
   follow-on delta (`4c17f59`) established one of those places (the stamped
   reviews template) carried the *broken* diff-shaped formulation. Does the
   doctrine's own grounding story survive its own later findings at HEAD?
2. **"Enforcement is structural" as a claim.** The review-line convention is
   itself prose: no template carries the field (admitted, queued), no scanner or
   CI checks for the line. Is "structural" an overclaim of the same class the
   apex forbids — and does atelier's *own* record-keeping since `30c9cd9`
   comply with the rule it wrote?
3. **The consolidation claim** ("four independent statements → one, plus three
   pointers"). Sweep `method/` + `build/templates/` at HEAD for residual
   artefact-shaped trigger grammar the re-key missed beyond the queued
   PRINCIPLES.md header.
4. **Fork→pointer actually achieved?** The template's new header bans restating
   the parent's trigger list — then the file restates a four-bullet trigger
   list. Is this a pointer with a thin floor, or a re-marked fork still free to
   drift? And does any line *narrow* the parent (its own "narrowing-free"
   claim)?
5. **The `<atelier-path>` pointer wiring.** The recorded claim is that the old
   relative link was broken in every stamped child and the new wiring resolves.
   Verify in a create-repo-shaped child: does the skill actually fill the
   placeholder, and does anything mechanical (linkscan, close-out grep) guard
   it?
6. **The remedy-class split's core premise** — "obeying the gate cannot damage
   content" for ROADMAP/SESSIONS. An all-open roadmap (ros's 125 open items is
   the live case) has nothing to relocate: the lossless remedy does not exist
   for it, so the gate's teeth *can* demand rewording or a budget hatch. Is the
   doctrine honest about that case, or does the class claim overreach?
7. **Gate mechanics at the edges.** GATED keyed by basename: interaction with
   `sizescan:budget=N` overrides (a gated file with a declared budget still
   gates?), `sizescan:allow`, `.sizescanignore`, ROOT_ONLY, the JSON schema
   change (new `gated` field — any consumer assumptions?), and whether the
   fail-safe exit-2 paths survived the change.
8. **Every recorded proof re-runs.** Suite green (records claim 267), template
   drift test, live gate behaviours both classes (gated over → exit 1;
   judgement doc over → `[advisory]`, exit 0), the four scans clean at HEAD,
   the stamped pointer resolving in a child. A proof that fails to reproduce is
   a finding.
9. **The budgets' own grounding.** The module doc demands class-grounded
   budgets and forbids deriving from current length — do the DEFAULT_BUDGETS
   and the new normative text meet the doc's own standard, and is the one-sided
   (no thinness floor) design defensible rather than merely asserted?
10. **The PRINCIPLES.md header question.** Rule it against PRINCIPLES' own
    first sentence ("The design doctrine for all technical work") and §1's
    design-time cases — does the header's build grammar contradict the file's
    own scope, and was deferring it to this pass correct?
11. **The pass structure itself (the brief is attackable).** Three deltas in
    one pass risks dilution; the sizescan delta has *no honest describing
    commit* (silent-absorbed into `4fb09a7`, whose message describes different
    work) — is "review the files at HEAD" sufficient mitigation, and is the
    absorb's acknowledgement mechanism adequate? Also: the combined pass's
    authors overlap (the 07-19 trigger delta's author is the 07-18 delta's
    applier; the sizescan text is the same session cluster) — does the one-pass
    fold weaken rule 4's independence in any way the brief hasn't named?
12. **Self-compliance of this very cycle.** Does the live queue/records trail
    since `30c9cd9` carry the review lines the new rule demands (the ⏳
    pointer, the ROADMAP items, the CHANGELOG entries), or is the repo already
    manufacturing the blank it declared to be the bug?

## Overall result

**PASS-WITH-FINDINGS — 3 MAJOR · 3 MEDIUM · 3 LOW.** Stated plainly, not
rounded: the doctrine *content* of all three deltas survives attack — the
commitment re-key, the design-review section, and the tripwire/advisory gate
split are the right fixes, and the gate split is live-proven sound. What does
**not** survive is part of the verification record: two recorded proofs fail to
reproduce (F1, F2), both attached to the fork→pointer conversion, and the
consolidation claim is false at HEAD (F3). Under the close rule (no-MAJOR), the
cycle stays open. Nothing has been applied — rule 3: these findings go to the
principal.

## Findings

### F1 — MAJOR — the stamped pointer does not resolve in a create-repo-shaped child, and the recorded verification claim is false
**Anchor**: `docs/build/templates/docs/reviews/README.md:19` (and `:64`);
`~/.claude/skills/create-repo/SKILL.md:113`.
**What**: The template now carries `<atelier-path>` in two places. create-repo
step 5 fills that placeholder only in `CLAUDE.md` and CONTRIBUTING's hook
lines, and its mechanical prove-the-stamp grep is scoped to
`CLAUDE.md CONTRIBUTING.md` — I built a child in scratch following the skill's
letter: the grep reports the stamp proved while `docs/reviews/README.md` still
carries both placeholders unfilled. Nothing else catches them: they sit in code
spans, so linkscan never sees them. The recorded claim ("create-repo
placeholder wiring verified, not assumed: the skill's close-out grep catches
unfilled `<atelier-path>`", `4fb09a7`) does not reproduce for this file.
**Why it matters**: this was the delta's headline propagation fix, and the
queued fleet re-stamp will distribute the defect. Every future child is born
with a non-resolving pointer behind a green check — the same broken-wiring
class the delta claimed to fix, now with a false "verified" on the public
record.

### F2 — MAJOR — the old link was not broken: "resolved to a file no child has" is false
**Anchor**: `docs/build/templates/docs/MODEL-ECONOMICS.md:1` (the disproving
artefact); recorded claim in `4fb09a7`'s message; the brief's own account
("recorded as having been broken in every stamped child").
**What**: The old template's `../MODEL-ECONOMICS.md` link resolves to
`docs/MODEL-ECONOMICS.md` — and the template set itself ships
`templates/docs/MODEL-ECONOMICS.md` (the per-repo short version), so the link
resolved **by construction** in every stamped child. Verified in the fleet: all
three children carrying the old README also carry the target, stamped in the
same scaffold commit. It also resolves inside atelier's own tree, which is why
linkscan was always green on it.
**Why it matters**: a "broken in situ, not just stale" claim was minted in the
retrospective, committed to a public record, and repeated into this review's
brief — and it is false. The *doctrinal* case for the pointer conversion (the
local file is a fork; point up to the canonical parent) was sound on its own;
the false factual claim was unnecessary and is exactly the
claim-stronger-than-evidence class the apex names. Net effect with F1: the
conversion replaced a resolving link with a non-resolving placeholder, and the
record asserts the reverse.

### F3 — MAJOR — the consolidation claim is false at HEAD: `skills/review-brief` still states the old trigger
**Anchor**: `skills/review-brief/SKILL.md:3` (also `:9`, `:12`, `:14`).
**What**: The delta's honest-measure claim is "independent statements of the
trigger rule — four to one, plus three pointers". At HEAD a fifth independent
statement stands in the repo's own plugin skill, entirely in the old artefact
grammar: "Use when **a change** earns a review" (description), "First: does
this **change** even earn a review?", "whether **a change** earns a review at
all", and "**The build** makes the claim" — the exact phrase `4fb09a7`
corrected in REVIEW.md's intro. The `4c17f59` sweep scoped itself to `method/`
+ `build/templates/` and never looked at `skills/`.
**Why it matters**: the plugin is doctrine that travels as behaviour — the
widest propagation surface the repo has — and it is unmarked as a copy (no
stamped-pointer header), the same unmarked-fork shape the delta condemned. A
design-holder reading the skill still concludes "no review". The framing trap
the principal's ruling named is alive at the exact point of use the
rule-grammar lesson says to fix.

### F4 — MEDIUM — the records misattribute the ros incident to the stamped template
**Anchor**: `CHANGELOG.md:21`–`27`; `4c17f59`'s message.
**What**: `4c17f59` asserts "REVIEW.md cites that very template as one of the
three places 'the correct rule already sat' when the ros session broke it on
2026-07-18… It was not the correct rule." REVIEW.md's three places
(`docs/method/REVIEW.md:275`–`277`) are the repo's own review policy, REVIEW.md
itself, and session memory — and the sibling record (`ros@55d0d51`) names them
explicitly as the repo's ROADMAP review-policy clause, atelier REVIEW.md, and
session memory. The incident repo has **never carried**
`docs/reviews/README.md` (verified against its history). The drifted-fork
finding is real — in the three children that have the file — but the template
cannot have misled the session the narrative hangs it on, and CHANGELOG's "the
one an agent actually reads when deciding whether to queue a review… the
reason the 2026-07-18 amendment never reached the fleet" inherits the
overreach.
**Why it matters**: the fork→pointer conversion's grounding story is
embellished beyond its evidence in two public records, and it contradicts both
REVIEW.md's own text and the sibling repo's account of the same incident.

### F5 — MEDIUM — "a red never demands rewording, only a move" is contradicted by the repo's own live case
**Anchor**: `tools/sizescan.py:43`–`47`; `docs/build/templates/workflows/floor.yml:133`–`136`.
**What**: The gate-class premise is that ROADMAP/SESSIONS always have a
lossless relocation remedy, "so a red never demands rewording, only a move".
The repo's own ROADMAP records the counterexample it already lives with
(`docs/ROADMAP.md:225`–`228`): a child roadmap red on ~125 **open** items —
nothing is harvestable, no move exists, and the sanctioned end-state is a
standing red gate (or a class-grounded budget). A permanently red `--check`
gate in child CI normalises red — alarm fatigue is the cost the tripwire
framing exists to avoid. Secondary: SESSIONS' own store hint for a flat log
("split to an index + `docs/sessions/` detail") is a restructure that authors
new index prose, not a pure move.
**Why it matters**: the split itself is right and live-proven; the categorical
wording overclaims its class. The honest statement is "the remedy is a move in
the overwhelming case; where a file is legitimately all-current, ground a
budget or accept a standing red" — which the module doc's budget paragraph
already half-says, while the gate bullet and floor.yml say "never".

### F6 — MEDIUM — "Enforcement is structural" overclaims at the point of read
**Anchor**: `docs/method/REVIEW.md:269`.
**What**: The review-line convention is enforced by nothing: no ADR template,
decisions README, or ROADMAP template carries the field (admitted —
`CHANGELOG.md:40`–`44`, `docs/ROADMAP.md:53`–`58`), and no mechanical check
looks for the line's presence in any record. Until the artefact lands, the
remedy is one more written rule — the exact class ("a doctrine that is read is
not a doctrine that is complied with") the same paragraph invokes against
writing it a fourth time.
**Why it matters**: the gap is honestly stated in CHANGELOG and ROADMAP, but a
reader inheriting REVIEW.md alone — which is how doctrine propagates — is told
enforcement is structural when, at HEAD, it is aspirational. The heading
should carry the qualification until the templates do.

### F7 — LOW — the template's header bans what its body then does, and nothing mechanical pins either
**Anchor**: `docs/build/templates/docs/reviews/README.md:5`–`8` vs `:23`–`33`;
`tools/test_templates.py` (no coverage).
**What**: The header instructs "Do NOT restate atelier's trigger list here";
the body then carries a four-bullet trigger list whose bullets 2–4 are carried
over from the old fork. Marked and narrowing-free-bound, so materially better
than before — but it remains trigger content that can drift when the parent's
trigger next changes, and the repo's proven countermeasure for exactly this
class (test_templates' character-for-character block-sync test for
templates/CLAUDE.md) was not extended: nothing pins this file's header,
placeholders, or floor.
**Why it matters**: the drift channel the header narrates is still guarded by
prose alone; the delta had the precedent one file over.

### F8 — LOW — PRINCIPLES.md header: ruled a genuine defect of the same class, correctly deferred to this pass
**Anchor**: `docs/method/PRINCIPLES.md:1` (also `:3`).
This is the queued ruling — see "Ruling on the PRINCIPLES.md header" below.

### F9 — LOW — the sizescan delta's provenance is permanently misattributed in history; acknowledged, but the pattern repeated
**Anchor**: commits `4fb09a7`, `e89c827`.
**What**: The gate split (+tests, +floor.yml comment) entered history inside a
records commit whose message describes different work (the silent-absorb — a
hazard CONCURRENCY.md:43 names), and the grounded-budgets paragraph rode
`e89c827`, a roadmap+sessions commit that at least names the withdraw action.
Neither normative change got a doctrine-titled commit. The mitigations are
real — the ⚠️ provenance note in the ⏳ pointer, the acknowledgement commit,
review-at-HEAD — so this lands LOW, but blame/bisect on `tools/sizescan.py`
now points at a commit whose message disowns the change, and the same
records-commit-carries-doctrine shape occurred twice in two days.

## Ruling on the PRINCIPLES.md header (the queued question)

**Ruled: a genuine defect of the artefact-grammar class — and the deferral was
correct.** Evidence: the header ("the doctrine every **build** is measured
against") is narrower than the file's own first sentence ("The design doctrine
for **all technical work**"), and than its own content — §1 carries
design-time cases ("Design the unhappy path too"; "half the value of an
approach review is catching a happy-path-only build"). With review now an
input to building, designs are measured against these principles before any
build exists; the header's grammar excludes exactly the reader the commitment
re-key brought inside. Line 3 ("A **build** that violates one of these…") has
the same defect. Was it "a defect the re-key should have caught"? Yes — the
`4c17f59` sweep's declared scope covered `method/`, and this file is in it; it
was caught a session later by the retrospective and correctly queued rather
than quietly re-nouned (substantive, self-authored, cycle open — the right
call). Counsel, decision the principal's: re-key line 1 (e.g. "the doctrine
every piece of work is measured against") and line 3 ("Work that violates…"),
as one hunk of the findings application.

## Per-lens coverage

- **Lens 1 — approach & assumptions**: twelve assumptions named cold and
  attacked (attack-surface commit `75b36a8`). Upheld: the commitment re-key
  (the trigger genuinely parses artefact-free at HEAD in `method/` +
  `build/templates/` — sweep found no residual there beyond the queued
  PRINCIPLES header); the design-review section's when-in-lifecycle claim; the
  remedy-class *split* itself; the one-sided signal; the grounded-budgets
  rule (the defaults meet the doc's own class-grounding standard). Broken:
  the wiring premise (F1), the old-link premise (F2), the swept-everything
  premise (F3), the never-demands-rewording premise (F5), the
  enforcement-is-structural premise (F6).
- **Lens 2 — correctness & quality / honesty of the records**: every recorded
  proof re-run (log below); two fail to reproduce (F1, F2); records
  embellishment (F4); wording overclaims in doctrine text (F5, F6). The
  4fb09a7 "months after" overclaim correction was verified as applied at HEAD
  in both places.
- **Lens 3 — completeness / harvest**: the sweep missed `skills/` (F3); the
  block-sync drift-test precedent not extended to the converted template (F7);
  the review-line convention still has no artefact (tracked, F6); the
  PRINCIPLES header correctly queued (F8); the absorb acknowledged (F9). Also
  noted, no finding: children that carry the old README keep a local
  MODEL-ECONOMICS short-fork the template set still ships — whether that file
  should itself become a stamped pointer is unexamined by these deltas and
  belongs on the harvest list.

## Proof re-run log

| Recorded proof | Result |
| --- | --- |
| Tool suite green, records claim 267 | ✅ `Ran 267 tests … OK` (`cd tools && python3 -m unittest`) |
| Template drift test (`tools/test_templates.py`) | ✅ 12/12 OK (none cover the reviews template — F7) |
| `sizescan --selftest` | ✅ selftest OK (includes the new gate-split check) |
| Live: gated file over budget under `--check` | ✅ exit 1, `[gate]`, gated-first ordering (scratch fixture) |
| Live: judgement doc over budget under `--check` | ✅ exit 0, reported `[advisory]` (scratch fixture) |
| Live: judgement doc over budget, bare run | ✅ exit 0 |
| Live: missing path fail-safe | ✅ exit 2 |
| Live: gated file exceeding its own declared `sizescan:budget` | ✅ still gates, exit 1 |
| JSON output carries the `gated` field | ✅ (additive; no in-repo JSON consumer of sizescan) |
| secretscan · leakscan · linkscan · `sizescan --check` at HEAD | ✅ all four clean, exit 0 |
| Stamped reviews-template pointer resolves in a create-repo-shaped child | ❌ FAILS — placeholders unfilled by the skill's steps; the skill's prove-the-stamp grep passes anyway (F1) |
| Old template's relative link "broken in every stamped child" | ❌ FAILS to reproduce — the link resolves in all three children that carry the file, and the template set ships the target (F2) |

## Spawn provenance (repeated, rule 4)

This review was spawned by the taking session (Fable), which took the ⏳
pointer queued on `main` and authored none of the deltas; that session was
opened fresh by the principal ("Do any reviews, use a worktree") — a session
the deltas' authors neither started nor instructed. The cold reviewer is a
fresh-context agent spawned by the taker; its attack surface was committed
(`75b36a8`) before any deferred material was opened. I note the one residual
honestly: the reviewer cannot independently verify the taker's account of its
own spawning from inside the worktree — the provenance trail above is the
brief's, consistent with the claim commit on `main`.
