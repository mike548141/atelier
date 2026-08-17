# Cross-session channel — coordination git cannot carry (Mike commissioned 2026-08-17)

**Where this came from.** Four days of five-parallel-session work in the public
child `faves` (2026-08-13 to 2026-08-17), read at Mike's direction. Every
coordination mechanism this house already has works by **manufacturing a git
conflict** — a claim line mutated in place, a coordination-free record name, a
rebase that stops. The collisions that cost real time in that window were
precisely the ones that *cannot* produce a conflict: two sessions each holding a
correct map of their own files, a rebase **absorbing** a matching version
constant instead of conflicting on it, two identifiers allocated from two stale
views, and one session's entirely correct change making the repo's gates
stricter for everyone else.

What caught nearly all of them was a **live message channel between sessions**,
which `docs/method/CONCURRENCY.md` does not mention once — nor does any other
method doc. That is a missing primitive rather than a missing paragraph, and
this section is its extraction.

**The evidence is durable and non-circular**, which matters because the apex
bars a doctrine change riding on testimony:

- the child's own committed session records, public and re-readable;
- this repo's board items handed up from that child — `020/320`, `030/140`,
  `115/130`, `200/090`;
- a verbatim four-round inter-session exchange, kept as primary source at
  [`../../sessions/2026-08-17-0343-cross-session-channel-transcript.md`](../../sessions/2026-08-17-0343-cross-session-channel-transcript.md).

**Mike's rulings, 2026-08-17.** Doctrine-layer work proceeds despite roughly
three-quarters of the open board already being guard, policy and review work
(the capacity question was put to him unargued before he ruled). The rules bind
at **method plus a floor clause**, not method alone. And the open finding
against the claiming rule's yield branch (`030/140`) stays untouched — it is his
to rule, and nothing here is written over it.
