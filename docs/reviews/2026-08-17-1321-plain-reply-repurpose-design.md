# Design review — can `plain-reply.py` be usefully repurposed as a data-gathering instrument?

**Pass type:** design review (REVIEW.md § *Review the design, not only the
build*) — a build/no-build question the principal put to the Fable tier. Not a
rule-4 doctrine pass: the hook is nobody's self-authored doctrine and no rule
is under review; the decision stays the principal's.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04). Checked
at selection.
**Status:** RUNNING — taken 2026-08-17 1321 UTC (wt: `cold-run-0817-1321`).

## The commission — the principal's words, verbatim

> "Do a fable review to see if it can be usefully repurposed e.g. to gather
> data/stats on plain speak to find the root cause when its not plain.
> Otherwise we will destroy the hook per your recommendation."

(Ruled 2026-08-17, second sitting, 1045 UTC; recorded at board item
`docs/roadmap/290-ruling-round-2026-08-17-the-cold-run-find/070-cmf1-fable-repurpose-review-else-destroy.md`,
which is the commission and is **not** barred — read it whole. It restates the
context the principal was given before ruling and the two outcomes it funds.)

## Spawn provenance

- **Author of the work under review:** the session that built the reply gate
  (landed 2026-08-09, `c374959`, per `git log`) and the session that unwired it
  on the principal's 2026-08-15 ruling. Neither is this
  session.
- **Who wrote this brief:** an atelier session Mike opened 2026-08-17 at 1321
  UTC on the **Fable** tier under his standing cold-session instruction (*do
  any reviews and any Fable-dependent work; write any briefs required*). This
  brief is scope-and-process only; the question is the principal's, above, and
  the brief-writer adds no attack questions of its own. The brief-writer is the
  orchestrator of this pass; it forms no finding and writes no severity.
- ⚠️ **Disclosure.** The brief-writer read the `docs/SESSIONS.md` tail and the
  2026-08-17 0955 session record at onramp — the record that carries the
  ruling and the principal's context for it in the orchestrating session's
  words. The reviewer read none of that.
- **Who reviews:** a Fable reviewer subagent spawned by the orchestrator, which
  authored no part of the hook, `plainscan`, the CHANGELOG or the doctrine
  clause, and was not started or instructed by any authoring session.
- **Orchestration shape:** the three prior verdicts the commission names —
  the communication-floor pass (`CMF`), the reply-gate unwiring pass (`RG`) and
  the board-generator pass (for `BG14`) — live under `docs/reviews/`, which
  `tools/coldsweep.py` bars by default; they are released by the orchestrator
  after the reviewer's phase-1 verdict is durably written, for reconcile only.

## Delta under review (the principal's list)

- `tools/hooks/plain-reply.py`
- `tools/plainscan.py` § the reply plane
- `tools/README.md` § `plainscan.py` (the two-planes section and the install
  stanza)
- `docs/method/COMMUNICATION.md` § *Some of it is enforceable*

## What the review must weigh (from the commission)

1. Whether a **record-only Stop hook** — run `plainscan` over the last
   assistant message, log findings + rule + context to a machine-local store,
   never block — would produce data that finds *root causes* of unplain prose,
   or only counts of it.
2. Whether the existing **`cctranscript` instruments** already reach the same
   data from transcripts without a hook. **Run the instruments' `--help` first**
   (`instruments/cctranscript --help`, and its man page under
   `instruments/man/`), and probe them against a real local transcript if one
   is reachable, before proposing any hook.
3. The **threat surface** the earlier passes named as `CMF6` — a machine-wide,
   fail-open hook running branch-tracking code from a public repo — as it
   applies to a *logging-only* variant. Consider what a logging hook writes,
   where, and who can read it (atelier is PUBLIC; the store must be
   machine-local and never travel into a repo).
4. The **private-layout path** the earlier passes named as `BG14`: the hook
   carries a hard-coded estate-layout fallback path. Say what it is, whether
   it belongs in a public tree, and what a repurposed hook would do about it.

Also in scope, because a design review's earliest finding is the cheapest:
whether the *question itself* is well posed — is "root cause when it's not
plain" a property a per-reply hook can observe at all, or does it need the
prompt/context that only a transcript carries? And whether "usefully
repurposed" has a cheaper answer than either build or destroy (a `plainscan`
mode over `cctranscript` output; a report; nothing).

## Re-run obligation

- `python3 tools/plainscan.py --help` and `python3 tools/hooks/plain-reply.py
  --help` (or read the argparse); run `plainscan` over a method doc to see the
  finding shape the hook would log.
- `instruments/cctranscript --help`; if a local transcript directory exists
  under `~/.claude/projects/`, run the instrument's search/stat modes against
  it and say what data it already yields on prose plainness — this is the
  control the commission asks for.
- The hook's tests, if any (`tools/test_*plain*`), the full Python and node
  suites, and the floor on both planes at HEAD (invocations lifted from
  `.githooks/pre-commit` and `.github/workflows/ci.yml`).
- Confirm the current wiring state: is the hook installed anywhere the repo
  can see (`.claude/settings*.json`, `tools/README.md` install stanza)? Say
  what you found, not what the docs claim.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the prior verdicts named in the commission are held by the orchestrator under rule 1's split, released after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`,
every prior verdict in `docs/reviews/` (the `CMF`, `RG` and `BG` passes
especially, which the commission names for reconcile). Sweep the tree with
`python3 tools/coldsweep.py`; if you use `--include-barred`, disclose it. The
board item `290-…/070` is the commission and is open to you. Board items
elsewhere that discuss the hook (`grep`-able as `plain-reply`) are the
authors' framing — read them after your findings if at all, and say so.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
the load-bearing assumptions named first, the answer to each of the four
weighings, findings with stable IDs (prefix `RP` — `PR` was already taken by a 2026-08-02 pass) and severities (MAJOR /
MODERATE / minor / note) where a finding is warranted, a **verdict line —
REPURPOSE (with the design, sized) or DESTROY — with grounds**, and a
follow-up checklist naming which of the item's two funded outcomes it
triggers. Then, on release, append a reconcile section against the three
prior verdicts. The decision is the principal's; record, apply nothing.
