# 2026-07-25 · 06:45 UTC · Doctrine + design captures — first-principles, cross-repo learning, solve-once, ccarchive encryption

**Model:** Opus. **Nature:** conversational capture session (no builds) — Mike
articulated several principles/directions and asked them noted for later. The
substance lives in the ROADMAP items below (this record points, does not
duplicate — *one fact, one home*). Continuation of the same conversation as the
2026-07-23-0959 queue run, but distinct work on a distinct day.

## Captured (all ROADMAP-only, `method/RECORD.md` stub-don't-fabricate)

All five are **captures / design directions**, not doctrine — content grounded in
Mike's words, actual doctrine NOT written or fabricated. Each lands its own
review when it moves from capture to doctrine/build.

1. **Elevate the first-principles doctrine to atelier** (`6835ce1`, enriched
   `e97c377`) — kāinga holds a first-principles/evaluation doctrine a prior
   session judged worthy of elevation ("governs how any repo evaluates, not just
   kāinga"); Mike agrees. Aligned meaning locked via the Musk/SpaceX example
   (decompose to raw-material cost, bypass industry markup, build from
   fundamentals); the rigour is in *"the parts you know are true"* (telling a real
   fundamental from a smuggled convention). External example illustrates; kāinga's
   own practice is the atelier-grounding. A future session locates + understands
   the kāinga doctrine before designing where it lands in `method/`.
2. **Cross-repo learning: atelier distils domain-diverse children** (`50fa4b7`) —
   the **up-flow** (child learnings → atelier, embed what generalises) as the
   complement to PROPAGATION's **down-flow**, plus **lateral** (child ↔ child).
   Engine = deliberate domain diversity at different constraint-walls: faves (no
   wall / pure software), tiki (hardware wall / networking), kāinga (research
   frontier), docker-heap + others as they mature.
3. **Solve once, reuse the building block** (`58776c4`) — in-repo (tiki's one
   wire-protocol module, many consumers) and cross-repo (intelligence/case-law as
   building blocks). Unifying claim: code primitives and knowledge primitives obey
   the same solve-once law → reframes atelier as the fleet's **shared library for
   knowledge**. Already-held twin: *one fact, one home* (EVIDENCE §9).
4. **ccarchive: encryption at rest, secure-by-default** (`b5e8d26`) — design pass.
   Direction: encrypted-by-default with a loud plaintext opt-out; ccrepo +
   cctranscript gain live-decrypt beside live-decompress. Raises the bar on the
   2026-07-23 "iCloud ADP E2E answers it" ruling (ADP covers only the iCloud copy;
   tool-native = confidential everywhere). Open questions named not pre-decided:
   key management as the crux (keys in the person-home, never atelier), overhead
   is key-access not decrypt, the **solve-once reuse** of the person-context
   age-capsule key infra (D1–D5), and the zero-dep-vs-crypto-dependency call as
   the one Mike-decision at the design pass.

The first three + the ccarchive item form a **coherent seam** (evaluation method
→ how knowledge flows → how it's reused → a concrete instance) a future session
can build out together.

## State at close

Floor green at head; tree clean; 0/0 sync; single worktree. No decisions blocking
— every capture is note-for-later whose downstream decisions need the design/
doctrine work first to be informed (never an under-contextualised ask). Not
mine, not claimed: the 2026-07-24 apex/principles commits (`4af5f3b` accountability,
`572dddd`/`672e838` Zeroth-law, `e29c49a` design-the-way-out, `9ff507b` raw notes,
`6ecfce0` economics wording) are a parallel session's work.
