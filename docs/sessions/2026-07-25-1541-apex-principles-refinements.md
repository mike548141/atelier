# 2026-07-25 · coda · Apex + principles refinements and two raw notes (inline Opus, on `main`, no worktree)

The **apex/principles/economics cluster** the 0645 sibling entry
(`sessions/2026-07-25-0645-doctrine-design-captures.md`) explicitly left
unclaimed — six commits on `main` (2026-07-24, 14:42→15:41 UTC), small-commit-
push, doc/doctrine only (no code, tests untouched). Each doctrine edit is
self-authored ⇒ `⏳` review-owed, queued for a non-author, none spawned
(independence). Opened with a `ccrepo` run + a weekly-usage-limit-timezone
question — informational, no doctrine.

## Applied refinements

- **economics: `preferred`, not `welcome`** (`6ecfce0`) — ECONOMICS.md's
  cheaper-model rule read as mere tolerance; Mike's intent is *first choice* —
  same outcome for less spend wins whenever the cheapest-that-does-the-work test
  passes, stopping deliberately short of *required* to leave latitude for the
  unforeseen. Swept the other docs: `welcome` was the lone soft-modal spot; the
  canonical "cheapest that genuinely does the work" phrasing elsewhere already
  carries directive strength (no drift). No `⏳` (wording alignment, not new
  doctrine).
- **apex: the principal's authority is rooted in accountability** (`4af5f3b`, `⏳`)
  — `00-APEX.md`'s informed-principal section stated the *condition* on the
  authority but never its *source*. Added the grounding: RASCI *Accountable* —
  the principal funds the work, the world attributes the product to him, the
  liabilities (privacy, copyright/IP, licence/contract) fall on him; the reserved
  decisions are his *because their consequences are*.
- **apex: a supreme humanity law added to the Laws** — Mike's direction to adapt
  Asimov's Zeroth Law. Numbering was genuinely ambiguous in his ask ("the same
  way Asimov did" vs "move down one place"); surfaced via a decision prompt with
  rendered previews. Mike first ruled **renumber (move-down-one)** — applied
  `572dddd` (new law = First, old three → 2/3/4, off-by-one-against-records cost
  flagged before applying) — then **changed his mind** to the Asimov-faithful
  **unnumbered Zeroth above the Three Laws** — applied `672e838`. Final form:
  "Three Laws" title/language kept, original three keep 1–3 *and* their original
  wording, humanity law sits above as an unnumbered **Zeroth**, read first.
  Numbers 1/2/3 keep their historical meaning ⇒ the off-by-one cost is **void**.
  `README.md` + `method/README.md` swept to match. Two commits, one `⏳` (the
  final state); decision history preserved in the roadmap pointer.
- **principles: "Design the way out before the way in"** (`e29c49a`, `⏳`) — new
  PRINCIPLES §1 resilience principle paired with "Build the way back before the
  way forward": that gives a *destructive action* its restore path first; this
  gives an *adopted dependency* its exit path first (fallback / export /
  swappable seam / degraded mode) — adopt only once the exit exists. Grounded in
  atelier's own zero-dep tooling (limit case) + browser-fetch (documented
  exception); cross-linked to REACH.

## Two raw Mike notes captured (`9ff507b`)

- *The Laws are a ladder that needs a world-model to work* — captured
  **verbatim** with the Laws-as-they-stood, the reference URL Mike flagged
  (pointer only, not fetched/interpreted), and the session/transcript id + UTC
  capture time; a dated pointer notes the Laws were later restructured to the
  Zeroth form. Do-not-interpret until Mike expands.
- *Define complex vs complicated* in the glossary — Mike's later action with a
  seed distinction (Cynefin-style: complicated = knowable/decomposable; complex =
  emergent/interdependent), not to encode until the glossary ratify pass.

Also logged (low-priority): **tools/ vs instruments/ naming** — both read as
"tools"; recommend `tools/` → `checks/`, keep `instruments/`; not a swap. Mike's
call, deferred.

## Open for Mike / carried forward

- 🎯 **Zeroth subordination clause** (apex micro-choice) — the original three are
  left in their *original wording* (no explicit "unless this conflicts with the
  Zeroth Law" clause); precedence rides on position + section prose. If Mike
  wants the fully Asimov-faithful subordination clauses, it's a small edit.
  Flagged open in the apex `⏳` roadmap entry.
- **Review debt**: 3 new `⏳` (accountability, Zeroth, way-out) atop the pre-
  existing RECORD floor-at-head `⏳`; child apex-floor propagation still gated on
  the apex review.

## Floor at head

sizescan `--check` exit 0 (cold-content gate green; ROADMAP size-advisory only —
expected hot-path fulsomeness, no un-harvested `[x]`), linkscan clean, leakscan
clean, secretscan clean on every commit (pre-commit hook). No code touched.
