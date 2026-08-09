# 2026-08-09 · 0848 UTC · A mechanical floor under COMMUNICATION.md

**Session:** Opus, inline on `main` (read-first sweep clean; no parallel session
evidence at start).
**Trigger:** a trust failure, stated by Mike, not a feature request.
**Landed:** `753adb6`, `e61adc4`, plus the records commit that carries this file.

## What Mike said

Kept verbatim, because the paraphrase risk here is the whole subject:

> In all repos you are continuously failing to communicate to a level that lacks
> honesty, lacks transparency, lacks verification that allows falsehoods, I am
> talking over many days and many many session. This is actively diminishing my
> trust in claude and your work

He then named the failure modes to look for — reference IDs without definition,
acronyms and abbreviations, long sentences, incomprehensible prose, lack of
context — pointed at the session transcripts as the evidence, and set the
direction himself: *"adding rulings and principles to doctrine are being
ignored. Deterministic hard walls like policy-as-code."*

So the design decision was his and arrived with the request. The work was to
measure honestly, then build the wall.

## What the measurement found

6,704 assistant replies of 200+ characters, across 1,094 session transcripts in
18 repos, 2026-07 to 2026-08. Replies under 200 characters were excluded as
acknowledgements, not prose.

| Defect | Share of replies | Rule already existed? |
|---|---|---|
| Bracketed aside over 25 chars | 67.2% | yes — doctrine since 2026-07-15 |
| Uncommon acronym, unexpanded | 55.5% | yes — plain-over-jargon |
| Sentence over 35 words | 36.8% | yes — plain-over-jargon |
| Bare reference code | 17.4% | yes — the same clause |

The number that settles the argument: of every reference code's **first use in
a session, 86% arrived with no gloss at all** — 1,457 bare against 236 glossed.
And the trend went the wrong way. Reference-code density rose from 4.04 to 7.23
per thousand words between July and August, while the rule against it sat in
`COMMUNICATION.md`, written down and unbroken.

Mike's read was right, and it was right on the strong form of the claim: not
"sometimes sloppy" but "the written rule is not a control".

## The root cause, and it was already documented

`COMMUNICATION.md`'s own enforcement clause said it: *"write-time discipline is
the **only** control."* Every other rule this estate cares about has a scanner
behind it. This one had a principle and a confession, and the confession had
been read as a closed question rather than an open one.

That is `floor.py`'s opening bug one surface over — a policy nobody could reach,
assumed to be working because it was written down.

## What was built

`tools/plainscan.py` — four rules, each carrying its ground, because a threshold
fitted to the current measurement is a photograph of the defect with a number
under it:

| Rule | Fires on | Ground |
|---|---|---|
| P1 | a code (`F1`, `C5`) used with nothing saying what it points at | **published** — digital.govt.nz: expand on first use |
| P2 | an acronym never expanded, absent from `GLOSSARY.md` | **published** — same clause |
| P3 | a sentence over the word limit | **house call** — see below |
| P4 | a bracketed aside over the char limit, mid-sentence | house doctrine, dated 2026-07-15 |

**P3's ground is honestly weak and is written up that way.** Two plain-language
authorities were checked for a numeric sentence cap — digital.govt.nz and
digital.gov — and **neither publishes one**; both say "one idea per sentence"
and stop. So the default is declared, not derived, and is flagged in the module
docstring, the README, the registry entry and the roadmap as Mike's to rule on.

**Two planes, one engine.** `scan_text()` takes a string. The repo plane is the
CLI in the floor registry. The reply plane is `tools/hooks/plain-reply.py`, a
Claude Code `Stop` hook reading `last_assistant_message` and returning
`{"decision": "block"}` so an unreadable reply is rewritten before Mike reads
it. The rules are not reimplemented per plane — that is the vendored-policy
shape ADR 0008 exists to end.

The reply plane **fails open**, alone among this estate's gates. Stated as a
trade, not an accident: `secretscan` failing open burns a credential for good,
while this failing open lets one clumsy reply through, and a linter that can
wedge a live session is worse than the defect it catches. It also gives up
after two blocked rewrites of one turn and says so visibly in the transcript
rather than looping.

## Honest notes

- **Warn-only, and that is a real limit on what landed.** The scanner reports
  and cannot block. atelier's own docs return ~7,900 findings; a blocking form
  would red every commit in the estate on day one and teach everyone
  `--no-verify`. `wrapscan` and `spellscan` landed the same way. But it means
  **nothing is yet prevented** on the repo plane — the wall is built and not
  yet switched on.
- **The Stop hook is not installed.** It needs a `settings.json` entry in
  `~/.claude/`, which changes every session in every repo. Left undone
  deliberately; it is Mike's call. Until he makes it, the reply plane — the one
  where every defect above was measured — is still unguarded. This session
  therefore fixed the *diagnosis* and built the *instrument*; it did not fix
  the problem Mike raised.
- **The corpus is the agent's own output, and the scanner was written by the
  agent that wrote the corpus.** Self-marking. The rules and thresholds want a
  cold pass, which is why the doctrine change carries a ⏳ pointer.
- **This session's own replies would have failed the gate**, repeatedly and
  including while writing about the gate. Not run against them retrospectively;
  saying so rather than leaving it unsaid.
- **The review pointer is one commit late.** The doctrine change landed in
  `753adb6` and the ⏳ pointer follows in the records commit, against this
  file's own landing-equals-queuing rule.
- **Two tests earned their keep by failing first.** The gloss rule read
  "F1 is open" as a definition (bare "is" removed), and the H1–H6 heading
  collision was checked against the corpus and left standing — all 45 uses of
  "H1" there are finding IDs, so exempting the shape would blind the rule to
  spare a rare collision. The `--limit` cap was added after the scanner
  printed 7,379 findings into its own first pre-commit run, reproducing the
  scroll-past failure it exists to catch.
- **Verification run:** 1,257 Python tests green, 207 instrument tests green,
  full floor green at both commits.

## What is still open

Filed under the policy-as-code programme, § *All doctrine directive first,
enforced second* — this is an instance of its part (a), found by measurement
before the census that should have found it. Four open items there: the two
house numbers, the hook install, the backlog scope, and the general lesson —
treat "the rule declares itself unenforced" as a census search key.
