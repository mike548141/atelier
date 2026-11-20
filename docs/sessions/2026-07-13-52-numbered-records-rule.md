# 2026-07-13 · 52 — numbered records under concurrency (Fable)

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 75+1 -->
- [2026-07-13 · numbered records under concurrency (Fable)](2026-07-13-52-numbered-records-rule.md) — a child repo's parallel-session number collision (two sessions both allocated 03 from stale views; renumbered 03→05 on human read-through) named the gap CONCURRENCY's append-tail bullet didn't cover: a next-N counter collides *silently* — differently named files, same number, no merge conflict. Codified (`e93e731`) as the append-tail bullet's sibling, three rules and still no locking: **allocate late** (N picked at landing, fresh pull immediately before, pushed at once — the allocate-to-push gap is the entire window), **provisional until pushed** (a loss costs one rename, not a reference cascade), **first landed wins** (the loser renumbers, mechanically). New record series should prefer coordination-free identifiers; counters stay only where the running number carries meaning. Fleet delivery via the child block's Concurrency line (canonical + template together, drift test green); RECORD.md points at the rule from the `<date>-NN` spec. This very entry allocated 52 the new way.


Mike relayed an incident from a child repo the night before: a session-number
collision under parallel sessions — s7 took 03+04 while another session had
already used 03, resolved by renumbering 03→05 — and asked whether it could be
prevented from recurring, steering the fix into atelier ("I'm thinking a change
within atelier").

## Diagnosis

- `CONCURRENCY.md` already covered the *visible* half of concurrent
  record-writing: append-tail conflicts on `SESSIONS.md` are expected and
  trivial — git forces the merge, both entries survive.
- The incident is the **silent sibling**: a next-N counter is a shared resource
  git does not police. Two sessions allocating from their own stale views
  create *differently named* files carrying the same number, so no merge
  conflict fires and the duplicate lands until a human reads through.
- The root cause is **allocation at session open with the push hours later** —
  the whole gap is collision window. The same hazard sits under every next-N
  series in the record: session numbers, `<date>-NN` detail files, ADR/review
  `NNNN`.

## Codified (`e93e731`)

- **`method/CONCURRENCY.md`** — new integration-hygiene bullet beside its
  append-tail sibling. Three rules, still no locking (the existing KISS line
  holds): **allocate late** (pick N at landing, fresh pull immediately before,
  commit, push at once — the allocate-to-push gap is the entire window);
  **provisional until pushed** (never cite your own number elsewhere before the
  push lands, so a loss costs one rename, not a cascade); **first landed wins**
  (the loser renumbers, mechanically — the same rule rebase already imposes on
  content). Plus a design preference: new record series should use
  coordination-free identifiers (date + time, unique slug); keep a counter only
  where the running number carries meaning. Bearing: the ros incident.
- **`method/PROPAGATION.md` + stamped template** — the child block's
  Concurrency line gains the compressed form (allocate at landing; first landed
  wins), canonical and template moved together per the session-47 drift lesson;
  the restatement enumeration updated to match. Drift test green (54 tests).
- **`method/RECORD.md`** — one pointer at the `<date>-NN-slug` spec: NN is
  allocated at landing per CONCURRENCY, never at session open.

## Owed

- Children adopt via normal pin bumps — no fleet retrofit; ros (whose incident
  this was) picks it up at its next deliberate bump.
- New/changed doctrine ⇒ the usual cold-review sweep covers these sections;
  nothing else outstanding.

This entry allocated its own number the new way: 52 taken at landing, fresh
pull immediately before, pushed at once.
