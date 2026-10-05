---
name: review-brief
description: Write a peer-review brief and run an independent review of work before it is trusted — atelier's enforcement half. Use when work earns a review — the trigger is commitment, not artefact: a design others will build to, a decision that forecloses alternatives, or a diff that ships (structural/first-of-kind work, doctrine, a silent-failure surface, anything irreversible or public) — when the user asks to review a design/diff/branch "properly", or to draft the brief a fresh session will run cold.
---

<!--
  STAMPED COPY, NOT A SECOND SOURCE. The canonical trigger, calibration and
  lifecycle live in docs/method/REVIEW.md (bundled with this plugin). This
  skill compresses them for the point of use; narrowing-free — it may compress
  the parent, never contradict it. (2026-07-19 cold-pass F3: this file was an
  unmarked copy still carrying the artefact-grammar trigger the parent had
  retired — the same drift class as the reviews template, one sweep later.)
-->

# Atelier — the peer-review lifecycle

A doctrine that is *read* is not a doctrine that is *complied with*. Documents
inform; the review is what enforces. The work makes the claim; the review earns
the right to believe it. Full doctrine: `docs/method/REVIEW.md`, bundled with
this plugin under the plugin's own install directory (and `ECONOMICS.md`
beside it for which reviewer, and whether work earns a review at all).

## First: does the work even earn a review?

**The trigger is commitment, not artefact** — ask *what will come to rest on
this once it is trusted*; the question parses the same holding a paragraph, a
plan, or a patch. Ceremony is *spend* — apply it in proportion to the cost of
being wrong, not uniformly. **Earns the full ceremony:** a design others will
build to or a decision that forecloses alternatives, first-of-kind or
structural work, a silent-failure surface (a check whose green exit is read as
"safe"), doctrine text, anything irreversible or public. **Self-verifying**
(tests + dogfooding over already-reviewed machinery): most routine, mechanical
changes. If it doesn't earn one, say so and stop — don't manufacture ceremony.

## Independence is the core, not capability

The builder is the worst-placed judge of its own work — it shares every blind
spot that made it. So the reviewer must have **fresh context**: a separate
session, even the *same model*, delivers most of the value (independence +
different blind spots + fresh context). A more capable tier is a *multiplier* on
top, deployed where stakes are highest — not a precondition. **Run the review
cold**, not in the window that built the work.

## Writing the brief (the ask, on top)

A good brief is falsifiable and attackable. Include:

1. **Subject under review** — point at the exact thing: the commits / files /
   branch if it's built, the design record or decision if it isn't; include
   anything machine-local that no other review will catch.
2. **Why it earns a review** — name the worst failure mode (e.g. a false negative
   that manufactures confidence).
3. **Scope, and the four lenses — run all four.** Scope is the whole
   commitment, never just the artefact in hand: intent, decisions,
   assumptions, design, docs, code, test code, real-world behaviour
   (exercised live where possible; an impossibility claim states its
   grounds). Non-goals are the only legitimate narrowing, and the narrowing
   is itself reviewable. The lenses organise that scope, never bound it:
   - **Approach & assumptions** (most important): *is this the right problem,
     solved the right way?* Attack the load-bearing assumptions **by name**.
   - **Correctness & quality**: does it do what it claims; honest about done vs
     stubbed; any overclaim or silent scope-cut.
   - **Completeness / harvest**: what it should have covered and didn't; what it
     duplicated or ignored.
   - **Security & privacy** — a must on every review, never a specialist
     add-on: design-altitude exposure, over-collection and
     privacy-by-design-weakness, through code-altitude injection, XSS,
     authn/authz and secret handling; *likely* vectors checked against open
     catalogues (OWASP Top 10 / ASVS), not recalled. Where the harness ships
     a security scanner (Claude Code's `/security-review`), aim it at the
     in-scope diff where it can reach one — the floor under the lens, never a
     discharge of it; where it can't reach the work, or the work has no
     surface, one explicit line with grounds. A clean pass over a file class
     the scanner's own exclusions bar (markdown, for `/security-review`) is
     definitionally empty — weigh it as nothing. Never run it over a brief
     carrying deferred material before findings are committed.
4. **Load-bearing assumptions to attack** — list them as falsifiable claims. The
   reviewer must *damage each with a probe or confirm it by re-driving* — not
   reason about it.
5. **Re-run every "live-proven" claim in scope.** A recorded proof is a claim that
   can be stale by the commit that recorded it. The reviewer re-runs the work's
   asserted proofs; a proof that no longer reproduces is a finding. A proof you
   have not re-run is not one you can close on.

## Running it and landing the verdict

Reproduce the floor first (build, tests, any selftests). Work the lenses and the
assumptions. **Run the standing checklist unasked** (`REVIEW.md` § *The
standing checklist*; a brief need not list it): V1 no claim stronger than its
evidence · V2 re-run every recorded proof in scope · V3 a changed rule swept to
every mirror site · V4 one fact, one home · V5 no internal contradiction ·
V6 security & privacy · V7 a rule-4 pass states its spawn provenance. A line
with nothing to bite on is discharged in one line with grounds. Land findings
numbered, each with a counselled fix where you can.
Close with a verdict (**PASS**, **PASS-WITH-FINDINGS** or **FAIL**, the house's
usual verdict words) appended below a divider in the brief, so the brief and its
verdict live together as the record. **Who applies a finding depends on what was
reviewed** (`REVIEW.md` rules 3 and 4):
- **Ordinary code:** the author may apply a finding, re-drive it the same
  session, and record `[fixed]`, `[backlog]` or `[rejected: grounds]`. A finding
  fixed but not re-driven is not closed.
- **Self-authored doctrine** (judged by function, not file type, so a skill,
  template, schema or gate counts): **the author applies nothing on its own.**
  It records the verdict verbatim. The findings are the principal's to decide,
  after he has the plain-language account the apex requires. And the review
  itself must come from a cold *spawn*, never from the author's own session
  (rule 4).

**Deferred material lives in its own file** — `<slug>.deferred.md`, never a
section below a divider in the brief. Reading is atomic: a deferred section is
consumed by the act of reading the brief it sits in, which made the old rule
unfollowable rather than merely unfollowed. Open the sibling file only once
your own findings are durably written, then fold it into the brief below the
verdict and delete it — split for the duration, one file at rest.
`reviewscan` reds a brief that carries a deferred section with no verdict —
keyed on `deferred`/`seeded` heading vocabulary, so use those words for the
section name; a renamed section escapes the net (the doctrine names this
limit).
