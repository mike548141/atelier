# 2026-07-22 · 2134 UTC · Apex gains its third element — adaptation is continuous

**Intent record for the ⏳ review of `f52c50f` + `1da0a3e` + `8d25fb3`.**

## What Mike said (the dictation, 2026-07-22 UTC)

> Here is a vital one and it sits just below honesty as a foundational part
> (apex) of the doctrine. We actively learn and gather evidence throughout
> everything we do, and as we learn we adapt by improving ourselves and our
> tools i.e. how we approach a situation/problem (aka strategy), the methods or
> solutions we use to address it, the process we use, the things we do and say,
> or don't do and say. Because we can always be better, and the environment /
> context we operate in will continue to change as well.

## The second dictation (same session, 2026-07-22 UTC)

> Weave into that point about learning that sessions (all models) should not be
> afraid of "taking the hard road" to learn more. It is preferable that models
> spend the time and effort to enable it to learn from real evidence. And
> decisions that change design or affect any part of the doctrine (apex,
> principles, decisions etc) or the overall doctrine must be evidence based and
> proven with hard facts. That evidence should be repeatable so it can be
> challenged and contrasted.

Encoded as two new "In practice" bullets (`1da0a3e`): **Don't fear the hard
road** (binding on every session and every model, tied to § Who it binds for
the smaller-model escalation path) and **Doctrine changes ride on proof**
(evidence-based, hard facts, repeatable so it can be challenged and contrasted;
named as the grounding rule held at apex strength, pointing to `EVIDENCE.md`).
Agent-authored connective tissue to attack: the "testimony, not evidence" line
and the claim that this *is* the grounding rule at apex strength.

## The worked case (`8d25fb3`, third exchange same session)

Mike supplied a live example from an open ros session — an SSH key reported
"dead fleet-wide" with a strict-crypto root cause and a recommendation to swap
algorithms or enable password auth, which collapsed under challenge. Before
encoding, this session **verified the account against the ros record** (ROADMAP
item "SSH auth DENIES tiki's credentials FLEET-WIDE", wire-proven verdict
2026-07-22 21:30 UTC): confirmed the diagnosis was an untested inference, the
real cause was client agent key-crowding, the policy flip would only have
re-enabled weaker algorithms, and the fix went the opposite direction. Encoded
as a shared worked case under both new bullets. Mike also widened the bullet
heading mid-session: "Doctrine changes ride on proof" → "Doctrine **and
design** changes ride on proof" (the body already covered design; the heading
undersold it).

Choices to attack: the **genericisation level** (public repo — no hostnames,
usernames, or key material; ros named as source, key algorithms and the
agent-crowding mechanism kept as generic technical fact) and whether the
17-line worked case is the right *weight* for the apex doc versus a pointer to
a bearing held in ros.

## What changed (`f52c50f`)

- `docs/method/00-APEX.md`: new section **"Adaptation is continuous"** placed
  between "Honesty is absolute" and "Then the Laws" — the literal reading of
  "just below honesty". Title widened to "honesty, adaptation, then the Laws";
  "Why this is level 0" now names all three elements and notes adaptation keeps
  the ladder itself improvable.
- `docs/method/README.md`: apex summary line updated to match.

## Authoring choices the reviewer should attack

- **Placement**: dictation said "just below honesty"; the agent read that as
  *second in the apex, above the Laws in document order*. An alternative reading
  (below honesty in rank but after the Laws in presentation) was not taken.
- **The subordination argument** (adaptation runs on evidence; honesty makes
  evidence trustworthy; a loop fed flattered reports amplifies them) is
  agent-authored rationale, not dictation.
- **Grounding cited**: EVIDENCE/REVIEW/RECORD/PROPAGATION as the already-running
  machinery; PRINCIPLES §6 sweep-stale-claims. The rule-keeps-breaking pattern
  (fix framing at point of use) was deliberately *not* cited — it is user
  feedback held in session memory, not yet encoded doctrine.

## Provenance and queue state

Wording is agent-authored on Mike's dictation ⇒ self-authored doctrine: this
session may not spawn the review (REVIEW.md rule 4); findings are Mike's to
decide (rule 3). Follow-on owed after the review closes: children inline a short
apex floor (`PROPAGATION.md`) — the widened apex makes those floors stale;
fleet sweep queued on the ROADMAP, gated on the review.
