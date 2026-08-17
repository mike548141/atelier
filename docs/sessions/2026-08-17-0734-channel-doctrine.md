# 2026-08-17 · 0734 UTC · The channel becomes a concurrency primitive (Opus 5 1M, wt: channel-doctrine-0817)

**Mike's commission, verbatim:** *"In Faves repo the sessions have said they
essentially talk to each other (broadcast) to manage concurrency of sessions and
have been working to manage issues like working on a shared repo and file
subsets, claiming work, asking questions and making decisions, identifiers like
ADR numbers clashing, committing, sweeping each others work, single file doc
changes. So the claim the work the commit, and the post commit work. Sometimes
with up to 5 sessions running in parallel on one repo / Have a look through the
sessions of the last 4 days in tha repo / I think there are doctrine
improvements we can make based on that work. I like the idea of the concurrent
sessions talking to each to e.g. Saying Hi when a new session starts or resumes
or closes, inviting other sessions to share what they are working on, what
quetions, decisions, rulings they have made (or the principal has made), when an
identifier is minted like an ADR number, claiming not only work but subsets of
files they are modifying and more I am sure"*

He also handed over a live incident from one of those sessions mid-turn, and it
became law 3: *"I spent the session broadcasting 'a message reserves nothing,
only a pushed file does' — then collided on ADR 0082 with a fifth session. We
both politely renumbered to 0083. Also simultaneously. main went red twice in
five minutes. The rule now has a third clause: check after the push, not before.
0082 is left as a permanent hole, documented so nobody 'fixes' it."*

## The finding that shaped the whole extraction

Every coordination mechanism this repo's doctrine has works by **manufacturing a
git conflict** — the claim mutates a contested checkbox, record names collide
trivially, a push is rejected. Read against four days of five-session work in
the public child `faves`, that is a structural blind spot rather than a gap in
coverage: it cannot reach the class where **both parties are individually
correct and neither has written yet**, because no shared line exists to collide
on. `CONCURRENCY.md` did not contain the words *message*, *broadcast* or *peer
session*, and neither did any other method doc.

The child's own formulation is what the section rests on: *a file map is a claim
about your own writes; a collision is a fact about somebody else's.*

## Grounding, and why it is not testimony

The apex bars a doctrine change riding on testimony, and this one nearly did. A
parallel atelier session offered a summary of a four-round inter-session
exchange as evidence for the protocol primitives. Asked for the raw exchange
instead, it made the better move and **refused the relay** — relaying into
another window would have moved the problem, since the source would then die
with *that* window. It committed the transcript instead
([`2026-08-17-0343-cross-session-channel-transcript.md`](2026-08-17-0343-cross-session-channel-transcript.md)),
which is now cited by the section.

🔑 **A primary source that exists only in an agent's context is not a primary
source.** That generalises past this channel and is written into the section.

So the evidence base is: the child's committed session records (public,
re-readable), four board items handed up from it (`020/320`, `030/140`,
`115/130`, `200/090`), and that transcript. Nothing rests on either session's
recollection.

## What landed

- **`docs/method/CONCURRENCY.md` § The channel** — three laws (message is
  awareness, artefact is authority · the closing check runs after the push ·
  a repair is itself a claim and its tie-break must be deterministic, with the
  burned-identifier corollary), seven message classes, three message-*shape*
  rules, the re-run rule, the **cost clause**, the publication clause, and a
  what-it-is-not fence.
- **Four seam edits.** § The trigger gains an ask-your-peers cue — the only cue
  that turns the flipped prior into a fact rather than a posture — plus the
  index and mid-rebase blind spots the dirty-tree backstop cannot see.
  § Integration hygiene gains **absorption**: a rebase does not conflict on a
  shared *value* that independently matches, it silently no-ops. § Claiming work
  gains the file-set announcement and file-disjointness-not-item-disjointness.
  § Surviving an interrupted session gains the volatility of a peer message.
- **The floor clause**, three sentences in `PROPAGATION.md`'s canonical
  concurrency bullet, with `docs/build/templates/CLAUDE.md` re-stamped in the
  same commit — `tools/test_templates.py` asserts byte-identity, so that pair is
  mechanical, not remembered.

## Mike's three rulings, 2026-08-17

Put to him as one question set, with the impacts of each option stated first.

1. **Doctrine-layer work proceeds** — asked because a parallel session had
   measured that roughly three-quarters of the open board is guard, policy and
   review work and raised, unargued, whether this estate should be adding to
   that layer at all. It was relayed to him unargued for the same reason it was
   handed over: an approval given without that account is challengeable on the
   briefing.
2. **Method plus a floor clause**, not method alone. Read as *the clause is
   authored here and each child adopts it in its own session*, because work
   lands in the repo it changes (his 2026-08-09 ruling). Queued at `280/020`,
   not swept from here. He was told that reading before any work began.
3. **The CF3 finding stays untouched.** `030/140` is an open finding against the
   claiming rule's yield branch, the passage immediately adjacent to this write,
   and the fix is his to choose. Nothing here is written over it, and this
   sentence is the commit's own statement to that effect.

## Verified, not assumed

- **The floor edit reds no child's commits**, checked in the tool rather than
  inferred: `stampscan` is deliberately outside `floor.py`'s registry, the
  reusable floor workflow and the pre-commit hook, because its `source=` path
  exists only in atelier. Propagation is a *read* obligation at the next pin
  bump, with no machine behind it yet. That is recorded at `280/020` rather than
  implied.
- **`tools/test_templates.py` — 44 tests, green in the worktree**, `pwd`
  confirmed before believing it. An earlier full-suite run had gone to the
  primary checkout because this harness resets shell cwd between calls, which
  would have been a green run against a tree without the change — the exact trap
  the child repo documents.
- **The claim landed on `main` before the worktree existed** (`a502a7b`), and
  the first commit attempt was blocked by `linkscan` on a relative path one
  level short. Recorded because the hook's `BLOCKED by:` line named the right
  scanner immediately — the child spent two sessions misreading which `✗` had
  stopped them.

## After the landing — the channel corrected its own doctrine's artefact

Two peer corrections arrived after `b0f202d` merged, both verified here rather
than accepted, both landed as `bb7c08f`.

- 🔎 **An atelier peer filed `AA11` and it hit this very commit.** A rule-4 brief
  can order its reviewer into barred material when the delta's commit packages
  its own intent record — and `git show --stat b0f202d` carries **120 lines of
  this session's own account** alongside the doctrine, plus both board items and
  the `SESSIONS.md` entry. So `280/030`'s delta is now scoped to the three
  doctrine paths, deliberately **not** to the commit, with the intent record
  named as background the reviewer's deferral discipline governs. `pointerscan`
  stayed clean, so the fix cost none of the refs-only grammar. The same peer
  passed rule 4's criterion for this delta and **declined it on the tier bar**,
  being Opus rather than Fable; it stays untaken. Its own
  Opus-orchestrator/Fable-reviewer departure is unratified and with Mike — not
  cited here, and nothing above rests on it.
- **The first child's pin has a known trigger.** A `faves` session reported its
  bump to `19eb0e2` with the `docs/method/` diff empty at that moment, so this
  section's floor commit is exactly the next drift its check reports. On `020`,
  because "owed at the next pin bump" otherwise reads as done.

🔑 **The section's hardest rule proved itself on the section.** Both of those
came from a party *re-running* a claim rather than reasoning about it — the third
instance in the evidence base, and the first found *after* the doctrine landed,
against the doctrine's own artefact. The peer's third correction was checked and
**did not bite**: `grep` for `additionalContext`, `systemMessage` and `hook`
across `CONCURRENCY.md` returns nothing, so the section makes no claim about what
a hook renders to whom.

One thing declined on the section's own cost clause: a fourth `faves` session was
**not** messaged. Two live sessions there hold the disposition and one is
relaying; a cheap channel makes it cheap to be noisy, and coverage was already
met.

## What this session did *not* do

No CF3 edit. No child repo touched. No review spawned — self-authored doctrine,
so `280/030` carries the rule-4 `⏳` on the Fable tier for a session this one
neither started nor instructed.
