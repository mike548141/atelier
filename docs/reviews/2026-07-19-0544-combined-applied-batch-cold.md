# Cold review — the applied batch of the combined cold pass (F1–F9 rulings)

**Date**: 2026-07-19 · 0544 UTC · **Status**: brief written, review pending

## Spawn provenance (REVIEW.md rule 4)

This review is spawned by a session Mike opened fresh with "Do any review
work" — a session the applied batch's author (the 0407 pass's taking session,
which applied Mike's F1–F9 rulings) neither started nor instructed. That
applier queued the `⏳` pointer and wrote no brief, per rule 4 and the
applying-decisions clause. This brief is written by the taking session
(Fable), which authored neither the three original deltas, nor the 0407
verdict, nor the applied batch under review. The cold reviewer is a
fresh-context agent spawned by the taker. Claim: `599b631` on `main`; work on
`main` (tree clean, no parallel session).

## Subject (refs only)

**One commit, `9d95644`, reviewed at HEAD** — the application of Mike's
2026-07-19 rulings on the 0407 combined cold pass's findings F1–F9 (F1–F8
fixed, F9 accepted). An application review's special sequencing binds — see
Ask. In-repo delta:

- `docs/method/REVIEW.md` — the F6 enforcement-claim qualification.
- `docs/method/PRINCIPLES.md` — the F8 re-key off the build grammar.
- `tools/sizescan.py` + `docs/build/templates/workflows/floor.yml` — the F5
  gate-class wording change.
- `skills/review-brief/SKILL.md` — the F3 re-key + stamped-copy header.
- `tools/test_templates.py` — the F7 test additions (records claim suite
  267→274 green).
- `CHANGELOG.md`,
  `docs/sessions/2026-07-19-0111-review-trigger-commitment-not-artefact.md`,
  `docs/decisions/2026-07-19-0100-review-trigger-is-commitment-not-artefact.md`
  — the F2/F4 dated correction addenda (originals left standing).
- Hunks in `docs/reviews/2026-07-19-0407-review-trigger-sizescan-combined-cold.md`,
  `docs/sessions/2026-07-19-0407-combined-cold-pass-taken.md`, and
  `docs/SESSIONS.md` — **deferred material**, see the divider rule in Ask.
- ROADMAP restructuring hunks (the queue's state after application).

Machine-local, in scope: `~/.claude/skills/create-repo/SKILL.md` — the F1
stamp-step fix (fill + prove `<atelier-path>` across the whole stamped tree),
recorded as live-proven red and green in a scratch child.

## Ask

Review deep, not fast, all three lenses (`method/REVIEW.md` § What a review
actually checks): approach & assumptions — name and attack the load-bearing
assumptions yourself, as your **first act**; correctness & quality — does each
applied fix do what its ruling asked, any overclaim, any silent scope-cut, any
new defect the new wording introduces; completeness/harvest — did any fix land
short, and what should the application have touched that it didn't. The
framing of this brief is itself attackable.

**Sequencing — the application-review rule (REVIEW.md § Applying decisions to
doctrine), binding.** This delta includes hunks in the prior verdict file, so
rule 2 cannot be fully honoured; the doctrine's stated sequence applies:

1. Commit your own attack surface to the verdict draft **first**.
2. Review the edited doctrine/tools/records at HEAD (everything in the in-repo
   list above **except** the three deferred files) and **commit your findings**.
3. Only then open the deferred material — the 0407 verdict file (its findings,
   rulings, and decision stamps), the applier's session log
   (`2026-07-19-0407-combined-cold-pass-taken.md`), and the `SESSIONS.md`
   index entry — to **reconcile**: check each ruling F1–F9 against what was
   actually applied, and whether the application drifted from, softened, or
   overshot the ruling. Never to anchor. The residual exposure (you will meet
   the rulings' framing at reconcile) is named, not denied.

**Re-run every recorded proof in scope** — a proof you have not re-run is not
a proof you can close on. Recorded proofs include: the tool suite green
(`cd tools && python3 -m unittest` — records claim 274), `sizescan --selftest`,
the four scans clean at HEAD (secretscan, leakscan, linkscan,
`sizescan --check`), the F7 tests actually biting (prove at least one banned
phrase and one pinned invariant fails red when violated — use a scratch copy,
never the live tree), and the F1 claim ("live-proven both ways in a scratch
child": the old two-file grep passes with the reviews README unfilled, the
widened grep catches it, clean after filling) — rebuild that proof yourself in
scratch from the skill's current text.

**Verdict**: append below this file's `---` divider. Stable IDs **G1…** (the
prior pass used F1–F9; don't collide), severity MAJOR / MEDIUM / LOW, per-lens
coverage, spawn provenance repeated, your attack-surface commit named, every
re-run proof listed with its result. Apply **nothing** (rule 3 —
self-authored doctrine): findings go to the principal; the taker will add
non-author counsel but the decisions are Mike's. Cycle close rule: the cycle
closes only when a pass returns no MAJOR, on the principal's ruling; a
no-MAJOR pass here makes the terminal application close without a further
queued pointer.

---

## Deferred — open only after your findings are committed (step 3 above)

- `docs/reviews/2026-07-19-0407-review-trigger-sizescan-combined-cold.md` —
  the prior brief, verdict, taker's counsel, and Mike's decision stamps (the
  rulings you reconcile against).
- `docs/sessions/2026-07-19-0407-combined-cold-pass-taken.md` — the
  taker/applier's own account of the application.
- The `docs/SESSIONS.md` index entry for that session.
- Prior verdicts in `docs/reviews/` — rule 2: reconcile-step only.

---

# Verdict

**Reviewer**: cold-context agent (Fable), spawned 2026-07-19 0547 UTC by the
rule-4 taking session. Spawn provenance: I am a fresh-context agent spawned by
the taker, which was opened fresh by the principal ("Do any review work"); the
applied batch's author (the 0407 taking/applying session) neither started nor
instructed this review. I authored none of the work under review. Written
before opening any deferred material.

## Attack surface — the load-bearing assumptions, chosen cold

- **A1 — the F1 grep actually proves the stamp.** The fix's whole claim is
  that a whole-tree grep replaces a named-file list and "verify like an
  instrument". Attack: run the skill's fenced commands *verbatim* in a scratch
  child — a prove-the-stamp command that itself errors, or whose exit
  semantics invert (grep exits 1 on the *desired* outcome), is a proof in
  prose only. Also rebuild the red/green proof: old two-file grep green with
  `docs/reviews/README.md` unfilled; widened grep red; clean after filling.
- **A2 — the F7 tests bite.** Pins that pass at HEAD prove nothing unless a
  violation turns them red. Attack in a scratch copy: re-introduce each banned
  F3 phrase, strip the stamped-copy/pointer markers, re-add a second stamp
  placeholder, drop the commitment-trigger line — each mutation must fail
  exactly the test that claims to pin it. Also attack the pins' *reach*: do
  the three banned phrases actually cover the retired grammar, or is the ban
  narrower than the drift class it answers?
- **A3 — the applied wording stays narrowing-free.** The review-brief skill
  and the reviews template both claim "may compress the parent, never
  contradict it". Attack: diff their trigger/calibration wording against
  REVIEW.md at HEAD — does the skill's "Earns the full ceremony" list widen or
  harden what the parent leaves to calibration; does any surface still carry
  the artefact grammar the pass retired (beyond the three test-banned
  phrases)?
- **A4 — "originals left standing" is true.** F2/F4 were fixed by dated
  addenda. Attack: confirm from the 9d95644 diff that no pre-existing line of
  the 0111 log, the 0100 record, or the CHANGELOG's earlier entries was
  silently reworded; and that the addenda's own factual claims (link resolves
  by construction; incident repo never carried the file) are checkable and
  check out where verifiable from here.
- **A5 — the F5/F6/F8 rewordings are honest and consistent across surfaces.**
  F5: sizescan module doc and floor.yml comment must state the same edge, and
  sizescan's *behaviour* must be unchanged (wording-only fix — any code drift
  is an overreach). F6: the qualification must match reality — the `review:`
  template artefact must actually be queued and absent. F8: the PRINCIPLES.md
  re-key must not leave stale "every build is measured against" citations
  elsewhere in the repo.
- **A6 — the recorded proofs reproduce at HEAD.** Suite 274 green, sizescan
  --selftest, four scans clean. A proof that fails to reproduce is a finding.
- **A7 — the brief's own framing.** It asserts the delta is one commit at
  HEAD and that machine-local scope is exactly the create-repo skill. Attack:
  check nothing else moved between 9d95644 and HEAD except the claim/brief
  commits, and that no other machine-local surface (the review-brief skill is
  also installed machine-locally?) escaped scope.

## Findings

### G1 — MAJOR · the F1 prove-the-stamp grep is unsatisfiable on the skill's own standard scaffold

- **Anchors**: `~/.claude/skills/create-repo/SKILL.md:118-121` (the fenced
  whole-tree grep, "expect: no hits ANYWHERE (all filled)");
  `docs/build/templates/workflows/floor.yml:106`
  (`# ref: <SHA>   # pin here for reproducible CI; default floats to main`).
- **What**: floor.yml ships a deliberate, stay-unfilled `<SHA>` pin slot in a
  comment (present since `bafeaa3`, long before this batch). Step 3 copies
  floor.yml into **every repo that inherits house doctrine** — the same class
  step 5 stamps. So on a full standard scaffold the widened whole-tree grep
  **always hits** `.github/workflows/floor.yml`, and the fix's green state
  ("no hits ANYWHERE") is unreachable. Reproduced live in scratch: with all
  four stampable placeholders filled in CLAUDE.md, CONTRIBUTING.md and
  `docs/reviews/README.md`, the verbatim grep exits 0 on floor.yml's `<SHA>`.
- **Why it matters**: this is the applied fix for the prior pass's sharpest
  MAJOR, and its failure mode is F1's own class, inverted. A proof command
  whose red is *expected on every scaffold* trains the operator to ignore its
  red — the grep stops proving anything — or invites ad-hoc repair (pinning
  the ref against its intended floating default, or deleting the comment:
  template drift). The recorded "live-proven red and green in scratch" can
  only have gone green on a **partial** tree without floor.yml; my own first
  rebuild made the same omission, steered by step 5's named-file framing —
  which is evidence the trap is systematic, not an unlucky hand-run. The
  queued **fleet re-stamp** inherits it too: every existing child carries the
  line (verified in the `ros` checkout, `.github/workflows/floor.yml:109`),
  so the "unblocked by F1's fix" claim on the ROADMAP item is over-strong —
  the proof step misfires fleet-wide as written.
- **Counsel shape (decision Mike's, nothing applied)**: take the stamp
  vocabulary out of floor.yml's comment (e.g. a token outside the four, or a
  literal example SHA), or make the skill's grep semantics acknowledge the one
  sanctioned standing hit — and pin the invariant mechanically (see G2). The
  grep-the-whole-tree *principle* is right; the template set just violates
  its precondition.

### G2 — LOW · no mechanical pin on the invariant G1 breaks

- **Anchor**: `tools/test_templates.py` (the new `ReviewsTemplateTest` /
  `ReviewBriefSkillTest` classes; `ChildFloorWorkflowTest` beside them).
- **What**: F7 was applied as ruled — the two review surfaces are pinned and
  the pins bite (proven below). But nothing in the suite pins the set-wide
  invariant the F1 proof depends on: *stamp placeholders appear in the
  template set only where the stamp step fills them*. `ReviewsTemplateTest`
  pins one file's placeholder inventory; the floor.yml class pins scanner
  invariants but not placeholder inventory — so floor.yml's `<SHA>` sat
  invisible while the skill's proof command was rewritten around it. One
  whole-set inventory test would have turned G1 red on the suite run.
- **Why LOW**: the ruling as recorded asked for the two surfaces and the
  phrase bans; the applier delivered that. This is harvest, not a broken fix.

### G3 — LOW · the 0820 decision record still carries the unqualified F6 overclaim

- **Anchor**: `docs/decisions/2026-07-18-0820-review-the-design-not-only-the-build.md:52`
  ("**Enforcement is structural**: …").
- **What**: F6 qualified REVIEW.md's "enforcement is structural" to "structural
  in intent … still conventional in fact". The 0111 session log and 0100
  intent record got dated addenda for their disproved claims (F2/F4), but the
  0820 decision record — which states the same enforcement claim REVIEW.md
  just walked back — carries no addendum or pointer, so a reader of that
  record alone still inherits the overclaim. Decision records are
  point-in-time and are not silently re-edited, which is why this is LOW and
  addendum-shaped, not a rewording ask; whether F6's ruling scoped records at
  all is checked at reconcile below.

## Overall result

**PASS-WITH-FINDINGS — 1 MAJOR · 0 MEDIUM · 2 LOW.** Every applied fix except
F1's does what the commit's account of its ruling asked, with no silent
scope-cut found: F3 (skill re-key + marker), F5 (both surfaces, wording-only —
sizescan behaviour unchanged, and the "declared budget" remedy it names is a
real mechanism, `sizescan:budget=N`), F6 (qualification honest; the queued
artefact item exists), F7 (pins bite), F8 (re-key clean; no stale citations of
the old heading outside records), F2/F4 (addenda accurate — the
MODEL-ECONOMICS template target exists, and `ros` has never carried
`docs/reviews/README.md`, verified against its history directly), originals
left standing (all record hunks in `9d95644` are pure additions). F1's fix is
directionally right and its red proof reproduces — but its green is
unreachable on the standard scaffold (G1), so **a MAJOR stands and the cycle
stays open on this pass**; the ruling is the principal's.

## Per-lens coverage

- **Approach & assumptions**: A1–A7 named cold and attacked. A1 broke (G1);
  A2 held after one mutation was redone wrap-aware; A3 held — the skill's
  "Earns the full ceremony" list folds in the parent's own design-review
  grammar, no narrowing found; A4 held (additions only); A5 held (surfaces
  consistent; behaviour unchanged; artefact item queued; no stale citations —
  except the record-side G3); A6 held; A7 held (only the claim/brief/verdict
  commits sit above `9d95644`; the only machine-local skill is create-repo;
  no installed plugin copy of review-brief exists to drift).
- **Correctness & quality**: each fix diffed against the commit's account of
  its ruling; proofs re-run (log below); overclaim found only at F1's proof
  generalisation (G1).
- **Completeness / harvest**: G2, G3; retired-grammar sweep clean outside
  records and the test's own ban list; fleet-facing reach of G1 checked
  against a real child.

## Proof re-run log

| Proof | Result |
|---|---|
| `cd tools && python3 -m unittest` | ✅ Ran 274 tests, OK — matches the recorded 267→274 |
| `sizescan --selftest` | ✅ selftest OK |
| `secretscan --root . .` at HEAD | ✅ clean |
| `leakscan --root . .` at HEAD | ✅ clean |
| `linkscan --root . .` at HEAD | ✅ clean |
| `sizescan --check --root . .` at HEAD | ✅ clean |
| F7 bite — banned phrases ×3 reintroduced (scratch copy) | ✅ each fails `test_old_artefact_grammar_evicted` red |
| F7 bite — pointer marker stripped / second placeholder / trigger line dropped / prose-exemption dropped / skill marker stripped (scratch) | ✅ all five fail red (the prose-exemption mutation needed a wrap-aware edit; the first sed was a no-op, not a weak test) |
| F1 red — old two-file grep with reviews README unfilled (scratch child) | ✅ exits 1, false green reproduced |
| F1 red — widened verbatim grep, same state | ✅ catches both unfilled pointers |
| F1 green — widened grep after filling, three-doc-file tree | ✅ exits 1, no hits |
| F1 green — widened grep on a **full step-3 scaffold** (floor.yml present) | ❌ exits 0 on `floor.yml:106` `<SHA>` — **G1**; the recorded green does not hold on the standard path |

Live tree untouched except this file; all scratch work under the session
scratchpad. Committed before any deferred material was opened.
