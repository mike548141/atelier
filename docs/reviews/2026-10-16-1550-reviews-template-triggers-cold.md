# Cold pass — the child reviews template's trigger list carries REVIEW's classes

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes this pass; a session that cannot honour it stops.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or
instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/610-rule-4-cold-pass-queued-template-review-triggers.md`.
**Why it earns a review:** the list decides, in every child created from the
template, which work earns a review at all; a class missing from it is work no
child reviews, and a class added wrongly is ceremony every child pays.

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
  message body (the author's own account of why) and diff, and the same for the
  previous commit on the same file (160/590's delta); the template file at HEAD
  in full; the review-brief skill's frontmatter and § *First*; `REVIEW.md` down to
  § *Whether work earns a review*; the ask halves, above the first divider, of
  two 2026-10-04 briefs as format models; filename listings of `docs/reviews/`
  and `docs/roadmap/`, and path greps over `docs/reviews/` that name prior
  verdicts without reading them; and its auto-loaded cross-session memory index.
  Its orchestrator read the `docs/SESSIONS.md` index tail (entries through
  2026-10-16, including the authoring runs' one-paragraph summaries) and the
  2026-10-16 session record's close section, and passed this writer nothing
  evaluative beyond the pointer list. What this writer suspects is in the sibling.

## What the work is

Landing commit (diff it; review the path at HEAD):

- `ebb358b` (2026-10-03) — templates: the reviews README's trigger list carries
  REVIEW's classes (200/100 C9)

Delta path: `docs/build/templates/docs/reviews/README.md`, § *When to write one*.
The previous commit on the file, `77fc609` (same day, 160/590's delta), changed
the opening and closing paragraphs; it is a non-goal here.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether a child, holding only this file, decides correctly whether a piece of
work earns a review. Read the section at HEAD and diff `ebb358b`. Read the file's
header comment and test the delta against every promise and prohibition it
states. The commit message gives a count of the copies of "what earns a review"
in atelier and says which had drifted: find every copy yourself, list them with
paths, and compare them class by class in a table — the count is a claim to
test. Parse the list as a child would: which bullets does the "in a product repo,
also" qualifier govern, and what does a child that is not a product repo (a
doctrine repo, an infrastructure repo, a records repo) read? Then drive cases:
a one-line change to a CI gate; a prose edit to a child's own `CLAUDE.md`; a new
dependency vendored; a records-only session log; a public README edit; a deploy
to an already-public site; a rename of a function nobody calls yet. For each,
the template's answer and `REVIEW.md`'s answer, side by side.

**Non-goals:** the opening and closing paragraphs (160/590's subject); the
calibration in `REVIEW.md` § *Whether work earns a review at all* (ruled
doctrine). Both are read only for consistency with the delta.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Is a restated list the right shape for this file, given what its header says
   the file is for? Are the two "product-repo additions" additions to the parent,
   or classes the parent already holds under another name?
2. **Correctness & quality.** Term-by-term agreement with the parent's wording of
   each class (V4, V5); the list's grammar and nesting as rendered; the routine
   examples in the paragraph after the list against the classes in it.
3. **Completeness / harvest.** Every surface that states the trigger — `REVIEW.md`,
   `skills/review-brief/SKILL.md` (frontmatter and § *First*), `ECONOMICS.md`,
   `README.md`, other templates — and whether any still disagrees. How does this
   change reach children created before it (V3)? Is a `CHANGELOG.md` entry, a
   stamp bump, or a create-repo note owed?
4. **Security & privacy** — mandatory. Design altitude: does the list still route
   security-relevant work (a guard, a secret path, a credential or trust-surface
   change, a silent-failure check) into review in every child shape? Code
   altitude: none (prose). `/security-review` is discharged by grounds — a landed
   prose delta; the session's pending diff is other passes' drafts — say so.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- the floor on both planes at HEAD (`python3 tools/floor.py --plane hook --root
  <root> --tools <root>/tools`, then `--plane ci --root <root>`), exit codes read
  explicitly
- `python3 tools/stampscan.py --warn --root . .` and `python3 tools/blockscan.py
  --check --warn --root .`
- the copy census in *Scope*, with the grep you used recorded so it re-runs

## House rules for this run

- Name your own worktree in the verdict. Run **no git command that writes** there;
  read-only git (`log`, `show`, `diff`, `blame`) is fine. Probes, scratch
  children and checkouts of older commits go in a private clone under your
  scratchpad, named by your prefix.
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
  --also-exclude $Q/610-rule-4-cold-pass-queued-template-review-triggers.md \
  --also-exclude docs/reviews/2026-10-16-1550-reviews-template-triggers-cold.deferred.md \
  --also-exclude docs/roadmap/200-anti-slop-invariant-registry-promote-rec \
  <pattern>
```

`--include-barred` only with disclosure in the verdict. The delta and the doctrine
it must agree with are never barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, findings with
stable IDs (prefix `TG`: `TG1`, `TG2`, …) and severities (MAJOR / MODERATE /
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

- **Reviewer:** a fresh `claude-fable-5-1` subagent (Fable, the principal-named
  review tier), spawned 2026-10-17 UTC by a Fable orchestrator that authored none
  of the work and none of the brief, and that holds the `.deferred.md` sibling
  outside the tree until this verdict is committed. The orchestrator forms no
  finding and writes no severity; every finding and severity below is this
  reviewer's. The reviewer-plus-orchestrator shape is disclosed here as rule 4
  requires. Neither this session nor its orchestrator started or instructed the
  2026-10-03 authoring run.
- **Worktree:** `/Users/mike/worktrees/atelier-review-1017`, branch
  `review-1017`, HEAD `64adf98` (verified `8acfff1` is an ancestor). No git
  write was run; only this file was edited.
- **Read:** the delta file at HEAD in full and `git show ebb358b` for that path;
  the diffs of `77fc609`, `5722bd8` and `4c17f59` on the same path (history of
  the list); `REVIEW.md` in full; `skills/review-brief/SKILL.md` lines 1–60;
  `ECONOMICS.md` lines 286–375; `AUTONOMY.md` lines 145–170; `PROPAGATION.md`
  lines 40–70, 200–215, 290–305, 816–855; `PRINCIPLES.md` § 6;
  `REPO-STANDARD.md` lines 225–281; `skills/create-repo/SKILL.md` (grep plus
  lines 120–175); `skills/queue-run/SKILL.md` lines 62–81; the templates
  `CLAUDE.md` (header), `CONTRIBUTING.md` § *Review*, `docs/ROADMAP.md`,
  `docs/decisions/README.md`;
  `docs/decisions/2026-07-19-0100-review-trigger-is-commitment-not-artefact.md`
  lines 40–75; `tools/test_templates.py` (the two template test classes);
  `tools/stampscan.py` docstring; `.stampscanignore`;
  `CHANGELOG.md` head and date greps; `.githooks/pre-commit`, `ci.yml` and
  `floor.py --help/--list` for the re-run invocations.
- ⚠️ **Exposure, disclosed.** (1) The landing commit's message body was read via
  `git show --stat` at the start, before this reviewer registered that the
  orchestrator's bar lists message bodies; the brief itself sends the reviewer to
  the message for the copy count, so the count and the author's "only the
  template had drifted" claim were met as claims to test, which is how they are
  treated below. (2) One hand grep over `docs/roadmap/` for the class vocabulary,
  run before the `coldsweep` census, printed three matching lines from the barred
  commissioning item under `200-anti-slop-…/100-…`; the lines restate what the
  commit message already said (four classes added, two additions labelled). The
  item was not opened; every later sweep used `coldsweep` with the brief's
  exclusions. (3) The message body of `4c17f59` (2026-07-19, the fork-to-pointer
  conversion) was read as history of the file; it is a prior delta's landing
  commit, not this one's. No prior verdict, `SESSIONS.md`, `docs/sessions/`,
  `ROADMAP-DONE.md`, the queue pointer or the sibling was opened. No wide sweep
  (`--include-barred`) was run.

### Lens 1 — approach and assumptions

Load-bearing assumptions, named first by this reviewer:

- A1: a child holding only this file should be able to decide whether work earns
  a review without opening atelier (the header's "thin floor").
- A2: the template may restate the parent's trigger classes.
- A3: the four added classes are exactly the parent's, and nothing else in the
  parent's calibration is load-bearing for the decision.
- A4: the three pre-existing bullets (user-visible behaviour, vendored code,
  load-bearing assumption) are "product-repo additions" that widen the parent.
- A5: every other copy of the trigger agrees with the parent, so only the
  template needed the sweep.

A2 is false on the file's own terms: its header says *"Do NOT restate atelier's
trigger list here"*, and ADR 2026-07-19-0100 decision 3 converted this file to
*"the one commitment question plus a thin floor; calibration is explicitly the
parent's call"*. The delta restates the list and leaves the header and the ADR
standing (TG1). A3 is half true: the "earns" classes were imported; the
"self-verifying" counterweight that makes the calibration decidable was not
(TG4). A4 is not what the text says: only one bullet carries the label (TG3),
and the third bullet is lens-1 material, not a trigger. A5 is false on one term
(TG2). A1 is the right goal and the delta serves it in spirit — a child now sees
the four classes where it decides — but the shape chosen (an unstamped
restatement in a file that forbids one) re-creates the exact hazard the header
records.

### Lens 2 — correctness and quality

**The copy census** (the commit message counts six copies; the count is a
claim, so every copy was found). Command, from the worktree root, exit 0, 33 hits
over 630 files, 407 barred files excluded:

```sh
Q=docs/roadmap/160-doctrine-review-owed
python3 tools/coldsweep.py --root /Users/mike/worktrees/atelier-review-1017 \
  --also-exclude $Q/610-rule-4-cold-pass-queued-template-review-triggers.md \
  --also-exclude docs/reviews/2026-10-16-1550-reviews-template-triggers-cold.deferred.md \
  --also-exclude docs/roadmap/200-anti-slop-invariant-registry-promote-rec \
  -i 'silent-failure (surface|mode)|first-of-kind or structural|forecloses alternatives|irreversible or public|bundled third-party|behaviour a user sees|earns? (the full ceremony|a review)'
```

Surfaces that state *which classes* earn a review (class-list copies):

| # | Surface | first-of-kind | silent-failure | doctrine | irreversible/public | self-verifying half |
|---|---|---|---|---|---|---|
| 1 | `REVIEW.md` § *Whether work earns a review at all* (canonical) | "first-of-kind or structural work" | "a silent-failure mode" | "doctrine text" | "irreversible or public **actions**" | yes |
| 2 | `ECONOMICS.md` § *Match the ceremony to the risk* | "…structural tooling" | "mode — a gate that can report green while not actually checking" | "doctrine text, because a wrong rule propagates…" | "irreversible or public-facing **actions**" | yes, with examples |
| 3 | `skills/review-brief/SKILL.md` frontmatter | "structural/first-of-kind work" | "a silent-failure surface" | "doctrine" | "anything irreversible or public" | n/a (one line) |
| 4 | `skills/review-brief/SKILL.md` § *First* | as 1 | "surface (a check whose green exit is read as 'safe')" | "doctrine text" | "anything irreversible or public" | yes |
| 5 | `docs/build/templates/docs/reviews/README.md` (the delta) | as 1 | as 4 | as 2 | "anything irreversible or public" | **no** — three routine examples instead |

Pointer-only surfaces (state the trigger sentence, no classes):
`docs/build/templates/CONTRIBUTING.md` § *Review*; `README.md` line 51. A
second, differently-shaped list sits inside `REVIEW.md` § *Review the design*
(captured feature, ratified design, structural decision; doctrine, ADRs, roadmap
direction, architecture note). The review-*line* trigger for design records
(`templates/docs/ROADMAP.md` lines 13–16, `templates/docs/decisions/README.md`)
is a different rule and agrees with § *Review the design*. The tier-escalation
rule (`ECONOMICS.md` line 302, `AUTONOMY.md` line 154, `skills/queue-run` line
73) reuses the class vocabulary for a different decision and is not a copy.
So: five class-list copies, two pointers, one sibling list — the "six" is
reachable only by one choice of what counts, and the message's "only the child
template had drifted" fails on the irreversible/public term (copies 3, 4 and 5
all drop "actions"; copies 1 and 2 keep it — TG2).

**Grammar as rendered.** Bullets 1–5 are the parent's classes. Bullet 6 opens
"and, in a product repo, also: behaviour a user sees…;" — the qualifier lives
inside that bullet, so as rendered it governs bullet 6 only; bullets 7 (bundled
third-party code) and 8 (a load-bearing assumption) read as unqualified. The
"and" signals a closing item, then two more follow. A child that is not a
product repo therefore has two readings, and the commit message's "two
product-repo additions labelled as additions" matches neither (TG3).

**The routine examples against the list.** The paragraph after the list keeps
"a config tweak" as routine while the list now carries "a silent-failure
surface: a check whose green exit is read as 'safe'". A CI-gate edit is both.
The parent resolves this with its self-verifying discriminator (already-reviewed
machinery, exercised end-to-end); the template never states it (TG4).

**Case drive** (template answer vs `REVIEW.md` + `ECONOMICS.md` answer):

| Case | Template | Parent | Agree? |
|---|---|---|---|
| one-line change to a CI gate | both "config tweak → routine" and "silent-failure surface → review"; undecidable | review, unless it wires already-reviewed machinery its floor exercises (self-verifying) | no — template lacks the discriminator |
| prose edit to a child's own `CLAUDE.md` | "doctrine text" → review, with no by-function test, so every line or only the stamped block | review iff doctrine by function (rule 3) | partly — TG8 |
| a new dependency vendored | review if bullet 7 is unqualified; none if the product-repo qualifier reaches it | no named class; lens 4 only once a review exists | template wider, but ambiguous — TG3 |
| records-only session log | routine (named) | self-verifying (named in ECONOMICS) | yes |
| public README edit (a typo, in a public repo) | "anything … public" → review; "a typo" → routine; contradiction | "public **actions**" → a typo is not one; routine | no — TG2 |
| deploy to an already-public site | "anything … public" → review | a public action → review, unless a reviewed pipeline deploying reviewed code (self-verifying) | partly — same gap as case 1 |
| rename of a function nobody calls yet | no class fires → routine | not a commitment → routine | yes |

### Lens 3 — completeness and harvest

- Surfaces still disagreeing after the sweep: copies 3 and 4 (the skill) on
  "actions" (TG2) — the sweep stopped at the template because the author judged
  the skill clean on a term the skill had already compressed away.
- **Reach to children created before the delta (V3):** none mechanical. The
  pin-bump drift check reviews the `CLAUDE.md` doctrine block's wording
  (`PROPAGATION.md` lines 44–60, 297); `tools/pins.py` reads pins only; nothing
  re-syncs a child's seeded `docs/reviews/README.md`. A pre-existing child meets
  this fix only if a session reads the `templates:` subject in its
  `log <PIN>..origin/main` output and edits its copy by hand. Pre-existing
  structural gap, not the delta's, recorded as TG6.
- **Records owed:** `CHANGELOG.md` carries entries dated 2026-09-20 and
  2026-10-05 and nothing between — neither 2026-10-03 template change (C8, C9)
  is logged; ADR 2026-07-19-0100 decision 3 is reversed without an addendum (TG5).
  No stamp bump applies: there is no stamp to bump — `stampscan` verifies exactly
  one block tree-wide (`templates/CLAUDE.md`), and the delta added none (TG1).
- `tools/test_templates.py` `ReviewsTemplateTest` pins the header marker, the
  commitment question, the prose-is-not-routine line and the placeholder — none
  of the four classes. Not a defect of the delta (the test pins invariants, not
  prose, by design) but it means nothing mechanical holds the list to the parent.

### Lens 4 — security and privacy (mandatory)

- **`/security-review`: discharged by grounds.** The delta is a landed prose
  change to a Markdown template; the scanner excludes Markdown, so its pass would
  be definitionally empty, and the session's pending diff is other reviewers'
  draft verdicts. Not run.
- **Design altitude, by hand against the OWASP Top 10 and ASVS headings:** the
  list routes a *guard* change (A05 security misconfiguration, A09 logging and
  monitoring failures) via "silent-failure surface" in every child shape — good.
  A secret-path, credential, auth or trust-surface change (A01 broken access
  control, A02 cryptographic failures, A07 identification and authentication
  failures) has no named class in *any* copy, parent included; it reaches review
  only if it is also irreversible, public or first-of-kind, or reaches the
  principal via the always-confirm floor (a confirmation, not a review). Vendored
  code (A06 vulnerable and outdated components) is the one supply-chain class
  named, and only in the template, where its reach is ambiguous (TG3). Recorded
  as TG7 at note severity: parent calibration is a non-goal here, and the gap is
  the parent's, not the delta's.
- **Code altitude:** none (prose). **Privacy:** the delta carries no personal,
  estate or instance detail; the file stays public-safe.

### Findings

**TG1 — MAJOR.** The delta restates the parent's trigger list in a file whose
header forbids exactly that, and the restatement is unstamped. The header (lines
5–8) says *"Do NOT restate atelier's trigger list here: an unmarked local copy
is how this file drifted from its parent once already"*; ADR
2026-07-19-0100 decision 3 made this file "the one commitment question plus a
thin floor". Lines 41–44 now carry the parent's four classes, with no
`stamp:begin source=docs/method/REVIEW.md …` pair, no region marker in
`REVIEW.md` for them to point at (`REVIEW.md` has none; the only canonical region
in the tree is `PROPAGATION.md`'s `floor`), and no test pinning the classes.
`stampscan --warn` at HEAD verifies one block tree-wide and cannot see this one.
The file now contradicts its own header (V5) and is the unmarked-copy shape V4
and `PROPAGATION.md` § *One statement, stamped copies* reject — re-created by the
commit that set out to cure drift. *Counsel:* the principal's call between (a)
restoring the decided shape — drop lines 41–44, keep the commitment question and
the pointer to § *Whether work earns a review at all*, which already carries the
classes; the "missing" classes were absent by ADR 0100's decision, not by drift;
or (b) keeping the list and making it mechanical — give `REVIEW.md` a
`trigger:begin/end` region whose lines the template copies verbatim (stampscan
compares line-literally, so a bulletised paraphrase would read as drift), wrap
the copy in a `stamp:begin … region=trigger` pair, rewrite the header to say a
stamped restatement is permitted, and append an addendum to ADR 0100. (a) is one
hunk; (b) is the commit's intent carried through. Either way the header and the
body must agree.

**TG2 — MODERATE.** "anything irreversible or public" (line 44) drops the
parent's "actions" (`REVIEW.md` line 447 "irreversible or public actions";
`ECONOMICS.md` line 366 "irreversible or public-facing actions"). In a public
child every file is public, so the class reads as "every edit" — contradicting
the file's own "a typo … doesn't need one" (line 51) and collapsing the list.
The same drop sits in `skills/review-brief/SKILL.md` line 3 and line 31, so the
commit message's claim that only the template had drifted is false on this term
(V1, V3). *Counsel:* "an irreversible or public action — publishing, deploying,
deleting" in all three copies; the skill is the source the template copied.

**TG3 — MODERATE.** The product-repo qualifier governs one bullet as rendered,
not the "two additions" the commit message says it labels, and the list's "and"
sits two bullets before its end. Reading A (qualifier reaches bullets 6–8): a
doctrine, infrastructure or records repo loses the vendored-code and
load-bearing-assumption triggers; vendored code is a supply-chain surface in any
repo. Reading B (bullet 6 only): "bundled third-party code" is an unlabelled
widening and the message's count is wrong. Bullet 8, "a load-bearing assumption
worth challenging", is the brief's lens-1 field (this file's own *Format* section
lists it) presented as a trigger — it is neither a parent class nor a labelled
addition. *Counsel:* one labelled bullet with a nested sub-list for whatever is
product-only, vendored code kept universal, and bullet 8 either dropped or
re-nouned as what it is (a brief field, not a trigger).

**TG4 — MODERATE.** The delta imports the "earns" half of the parent's
calibration and none of the "self-verifying" half (`REVIEW.md` lines 448–450;
`ECONOMICS.md` lines 367–371: wiring an already-reviewed tool into a gate, a
refactor its suite fully covers). The routine examples keep "a config tweak",
which now collides head-on with "a silent-failure surface" on the commonest
child case — a one-line CI-gate change is both — and the deploy case has the
same hole. A child cannot resolve either from this file; it must open the parent,
which the header's "thin floor (enough to act on without opening atelier)"
exists to avoid. *Counsel:* one sentence after the list — work whose tests and
dogfooding exercise it end-to-end over already-reviewed machinery is
self-verifying; there the floor is the review — and drop "a config tweak" from
the routine examples, or qualify it ("a config tweak to a reviewed gate").

**TG5 — minor.** Records owed and not written: no `CHANGELOG.md` line for either
2026-10-03 template change (the file jumps from 2026-09-20 to 2026-10-05), and
no addendum on ADR 2026-07-19-0100, whose decision 3 the delta reverses
(`RECORD.md`: everything after acceptance is appended). *Counsel:* a *Changed*
entry naming both template commits and the seeded file children should
re-sync, and an ADR addendum once TG1 is decided.

**TG6 — note.** V3 reach: nothing mechanical carries a template edit to a child
created before it — the pin-bump drift check reviews the `CLAUDE.md` block, and
`tools/pins.py` reads pins only. The fix reaches pre-existing children by hand.
Pre-existing gap, named so the "propagates by template into the whole fleet"
framing is read at its true strength. *Counsel:* a board item for a seeded-file
drift report (the child's `docs/reviews/README.md` against the template at its
pin), beside `pins.py`.

**TG7 — note.** No copy of the trigger list, the parent included, names a
security class (a credential path, an auth or trust-surface change). Such work
earns a review only when it is also silent-failure, irreversible, public or
first-of-kind; otherwise it meets the always-confirm floor, which confirms but
does not review. Parent calibration is a non-goal here; recorded as counsel for
the parent, not a defect of the delta.

**TG8 — note.** "doctrine text" lands in children without rule 3's by-function
definition (any rule that governs future agent behaviour, in prose, schema,
validator, gate, template or skill). A child reads either every line of its
`CLAUDE.md` as doctrine (over-ceremony) or only the stamped block (under). Six
words would settle it: "doctrine text — any rule that governs future sessions".

**Overall: PASS-WITH-FINDINGS — 1 MAJOR · 3 MODERATE · 1 minor · 3 note.**

The delta does what its subject says — the four parent classes are now on the
page a child reads — and does it in the one shape the page forbids, without the
counterweight that makes the classes decidable. All findings are on doctrine by
function (a template that stamps behaviour into other repos): recorded, nothing
applied; the decisions are the principal's.

### Standing checklist V1–V7

- **V1** — the commit's "six copies" and "only the template had drifted" were
  re-counted and re-compared: five class-list copies plus two pointers, and the
  skill drifts the same way on one term (TG2). The brief's "two product-repo
  additions, labelled" was read against the rendered grammar (TG3).
- **V2** — no recorded "live-proven" claim is in scope; the commit's implicit
  claim (the other copies agree) was re-driven (TG2). Scanners re-run in the
  ledger below.
- **V3** — mirror sites swept: `REVIEW.md`, `ECONOMICS.md`, the skill (two
  copies), the other templates, `README.md`; the skill still disagrees (TG2);
  reach to existing children is by hand (TG6).
- **V4** — the restated list is an unstamped copy; no region exists for it to
  stamp against (TG1).
- **V5** — the file contradicts its own header (TG1), its own routine examples
  (TG4) and, in a public child, its own typo exemption (TG2).
- **V6** — lens 4 run by hand against OWASP; `/security-review` discharged
  with grounds; TG7.
- **V7** — provenance stated in the brief (above the divider) and repeated in
  this verdict, including the orchestrator shape.

### Re-run ledger (all from the worktree root, under `nice -n 10`, foreground)

| Check | Command | Result |
|---|---|---|
| floor, hook plane | `python3 tools/floor.py --plane hook --root <root> --tools <root>/tools` | **not run** — the orchestrator's load instruction for this pass (machine load 60.9 / 113.7 / 86.7 at 2026-10-17 10:54 UTC from other sessions' test runs; the floor runs 16 whole-tree scanners) |
| floor, CI plane | `python3 tools/floor.py --plane ci --root <root>` | **not run** — same grounds |
| floor plan | `python3 tools/floor.py --list --plane hook` / `--plane ci` | 16 scanners listed on each plane, none disabled |
| stampscan | `python3 tools/stampscan.py --warn --root . .` | exit 0 — clean; 1 stamped block verified (`templates/CLAUDE.md:18`, identical to `PROPAGATION.md` region `floor`, 93 lines); 175 files suppressed by `.stampscanignore`; ran 3 s |
| blockscan | `python3 tools/blockscan.py --check --warn --root .` | exit 0 — clean; 55 unmapped headings, advisory; ran under 1 s |
| copy census | the `coldsweep` command in lens 2 | exit 0 — 33 hits / 630 files, 407 barred files excluded |
| Python suite, Node suite | — | **not run** — the orchestrator's instruction for this pass; nothing in the delta is code |
| `/security-review` | — | discharged by grounds (lens 4) |

### Follow-up checklist

- [ ] Principal rules TG1 (a) or (b); the header and body of the template agree
      afterwards, whichever way.
- [ ] TG2: "actions" restored in the template and both skill copies.
- [ ] TG3: the product-repo qualifier's reach made unambiguous; bullet 8 decided.
- [ ] TG4: the self-verifying sentence added, or "a config tweak" qualified.
- [ ] TG5: `CHANGELOG.md` entry for the two 2026-10-03 template commits; ADR
      2026-07-19-0100 addendum once TG1 is decided.
- [ ] TG6: board item for a seeded-file drift report beside `pins.py`.
- [ ] TG7, TG8: counsel for the parent, for the principal to take or leave.
- [ ] The floor on both planes re-run at HEAD by the applier once machine load
      allows; this pass could not.
- [ ] Phase 2: reconcile against the sibling once released.
