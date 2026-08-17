# Cold pass — the apex: authority absolute, rulings conditioned

**Pass type:** doctrine cold pass (REVIEW.md rule 4 — the delta rewrites the
apex section that governs how the principal's word binds, plus its five
restatements and the child-facing floor block; self-authored doctrine by
function, in the authoring session's wording, carrying a ruling quoted from
the principal).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04). Checked
at selection: a session that cannot honour the bar stops rather than takes.
**Status:** BRIEF WRITTEN, REVIEW NOT RUN. The next cold session that passes
rule 4's criterion and the tier bar takes it — see *Spawn provenance*.

## Spawn provenance

- **Author of the work under review:** the session that landed the delta on
  2026-08-15 (wt: `authority-absolute-0815`; Fable tier per the commit
  trailers on `38add7c` and `c782e14`).
- **Who wrote this brief:** an atelier session Mike opened 2026-08-17 for the
  fleet board-split rollout, and then asked, mid-session: *"Are there any
  briefs that need to be written?"* and *"If so please write them for a cold
  review."* That session authored no part of this delta, was neither started
  nor instructed by the authoring session, and has not edited any file this
  delta touches. It wrote this brief from the two commits and the queue
  pointer only; it did **not** open the intent record
  (`docs/sessions/2026-08-15-1129-authority-absolute.md`) or the board item
  the pointer names.
- ⚠️ **Two disclosures the taker should weigh, both about the brief-writer,
  not the delta.**
  1. **It read the `SESSIONS.md` index entry for this delta** — early in the
     session, as a range grep over recent entries, before this brief was
     commissioned. That entry summarises the ruling and the surfaces. It is
     rule-2 barred material and it was read; it is the reason the intent
     record itself was left unopened, and it is why the seeded questions in
     the sibling are deliberately thin. Treat them as a floor, not a fence.
  2. **It is not on the Fable tier** — it is Opus. Brief-writing has been done
     at Fable in this repo's prior split passes (2026-08-15, 1024 UTC). The
     tier bar in REVIEW rule 4 is stated for the *reviewer*, and this is not
     the review; but the taker should satisfy itself that a brief written off
     the named tier is acceptable, and say so either way in its verdict. If
     it judges otherwise, the correct outcome is to rewrite the brief, not to
     run the review on a brief it does not trust.
- **Who takes the review:** the next cold session meeting rule 4's single
  criterion — a session the author neither started nor instructed — on the
  Fable tier. The taker repeats its own provenance in the verdict: how it was
  spawned, and its non-involvement with both the authoring session and this
  brief-writing session.
- **Orchestration shape:** the deferred material sits in the sibling
  `2026-08-17-0622-authority-absolute-cold.deferred.md` (rule 1's split).
  Recommended: run under an orchestrator that holds the sibling's bytes and
  releases them only after the reviewer's findings are durably written. A
  taker working by hand opens the sibling as a deliberate second act after its
  findings are committed, and says so in the verdict. Fold in and delete when
  the verdict lands.
- **Adjacent passes, not this one.** The Laws-removal cold pass
  (`2026-08-15-1031-laws-removal-apex-cold.md`) reviews the *removal* that
  emptied the apex section this delta then rewrote, and its LR findings are a
  prior verdict — barred until reconcile. The board-store pass
  (`2026-08-15-1030-…`) touches none of these surfaces.

## What the work is

Two commits on `main`, merged as `81d7d04`. Reviewed at HEAD.

**`38add7c` — the authority correction.** The apex section *The principal's
authority is conditioned on being informed* is retitled *The principal's
authority is absolute; his rulings are conditioned on being informed* and
rewritten. The removed claim: that authority is *"not exercisable
uninformed"*. The replacement: the authority is absolute and never decays, the
agent can never overrule the principal in any situation including one where it
believes him uninformed, and what being informed conditions is the **ruling** —
challengeable on the briefing, and still challengeable by an independent review
session even when informed; a challenge is raised *to* the principal by
re-briefing, never by declining to obey. Restatements aligned in the same
commit: `RECORD.md`, `AUTONOMY.md`, `CONCURRENCY.md`, `REVIEW.md` rule 3, the
child floor block in `PROPAGATION.md`, and the byte-identical
`docs/build/templates/CLAUDE.md` stamp. The sharpest single change outside the
apex is in REVIEW rule 3: *"An approval given without that account is not a
decision the doctrine recognises"* became *"stands as the principal's word but
is open to challenge — on the briefing, never on his authority."*

**`c782e14` — the dilemma line returns.** *"Surface a genuine dilemma; never
silently resolve it"* — dropped with the Laws — is restored as an in-practice
bullet under `00-APEX.md` § *Honesty is absolute*, and to the child floor block,
the templates stamp (53 lines, stampscan identical) and the session-onramp
skill, under the **honesty** bullet rather than the Laws bullet it used to ride.

The commit messages state the ruling in the principal's terms and claim
`stampscan` identity between `PROPAGATION.md`'s floor block and the template
stamp. Both are the author's claims and are in scope as such.

## Scope

Widest the work admits. This delta changes **what the agent may do when it
believes the principal is wrong**, so the reviewable question is not only
whether the words are accurate but what they license and forbid at the moment
of use. In scope: whether "absolute and never decays" and "challengeable by
re-briefing" compose into a rule an agent can actually follow under pressure,
or leave a gap where an agent that disagrees has no sanctioned action; whether
the REVIEW rule 3 softening — from *not recognised* to *stands, open to
challenge* — is what the principal ruled or the author's reading of it, and
what it now permits that it previously forbade; whether the five restatements
say the same thing as the apex or five slightly different things; whether the
always-confirm floor and the ADR-acceptance path still work under the new
wording; whether the honesty framing carries the dilemma line as well as the
removed Laws framing did, or whether something the Laws caveat was doing is
now unowned; and what a session reading only the **child floor block** — which
is all most children get — will believe about its authority to refuse.

**Non-goals, and neither fences the risk:** the reviewer does not decide any
finding — findings are the principal's to rule on (rule 3), and this delta is
his own ruling being recorded, so counsel is welcome but must be labelled.
And the *substance* of the ruling is not under review; the account of it is.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself
   first. Is the authority/ruling split a real distinction or a restatement
   that dissolves at the point of use — what, concretely, does an agent DO
   when it holds a ruling it believes uninformed and re-briefing has already
   failed once? Does "never decayed by it" bound the number of times an agent
   may re-brief, and if not, is repeated re-briefing distinguishable from
   declining to obey? Does the doctrine anywhere say what happens when the
   principal declines to be re-briefed?
2. **Correctness & quality.** Read all seven surfaces at HEAD side by side
   with both diffs. Do the apex, `RECORD`, `AUTONOMY`, `CONCURRENCY`,
   `REVIEW` rule 3, the `PROPAGATION` floor block and the templates stamp
   agree — not merely avoid contradicting? Verify the byte-identity claim by
   running `stampscan` rather than reading it. Check whether any surface still
   carries the old "not exercisable uninformed" logic under other words,
   including skills, `docs/build/`, and the ADR corpus.
3. **Completeness / harvest.** Every surface that stated the old rule, and
   every surface that *relies* on it: the always-confirm floor list, the
   ADR acceptance path, the autonomy grant, the review-independence rules,
   the session-onramp skill, `CHANGELOG.md`. Does a CHANGELOG entry exist for
   both commits? Children inherit the floor block only at their next pin bump
   — is the resulting window stated anywhere a child session would see it?
   Does the restored dilemma line duplicate anything already in the honesty
   section under another name?
4. **Security & privacy** — mandatory. atelier is PUBLIC. The delta quotes
   the principal at length and describes a governance relationship; check that
   nothing in the seven surfaces or the queue pointer joins a private repo's
   name to its posture, or carries personal context. Consider separately
   whether *this* change alters the safety posture: the always-confirm floor
   is the mechanism that stops irreversible action, and this delta touches how
   its stops may be challenged. If the lens has no surface beyond the public
   -tree check, discharge it in one explicit line with grounds. The house
   security scanner reads the session's pending diff whatever path it is aimed
   at (board item `160-…/190`); this is a landed-delta review, so state the
   reach case that applied rather than assuming one.

## Re-run obligation

Re-run, do not read: `stampscan` at HEAD, to test the byte-identity claim
between the `PROPAGATION.md` floor block and `docs/build/templates/CLAUDE.md`
— and note that `stampscan`'s verdicts are themselves under a standing finding
(board `115/030`: its verdicts are inverted against the doctrine it enforces),
so read its output against the files, not only its exit code. Run the full
suite and the floor on both planes at HEAD; lift the invocations from
[`.githooks/pre-commit`](../../.githooks/pre-commit) and
`.github/workflows/ci.yml` rather than guessing them. Grep the tree for the
old wording and for the removed *"not a decision the doctrine recognises"*
formulation. Check at least one real child's `CLAUDE.md` for which version of
the floor block it currently carries, and say which.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`,
every prior verdict in `docs/reviews/` (the Laws-removal pass especially), the
intent record for this delta, and the board item
`160-…/200-apex-authority-absolute-rulings-conditioned.md`, which carries the
ruling verbatim and the author's account. The sibling `.deferred.md` holds
those references and the brief-writer's seeded questions; open it after your
findings are committed. Reconcile after, never anchor before. A taker whose own
session onramp has already read the `SESSIONS.md` tail discloses that in the
verdict, as this brief-writer has.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `AA`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then open the sibling; append a
reconcile section; fold the sibling in below it and delete the sibling;
finalise. Update the queue pointer
(`docs/roadmap/160-doctrine-review-owed/210-rule-4-cold-pass-queued-authority-absolute.md`)
and rebuild the index in the same commit.
