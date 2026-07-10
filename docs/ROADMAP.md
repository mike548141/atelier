# atelier ROADMAP

Lean and read every session. Completed detail moves to `ROADMAP-DONE.md` once
this grows.

## The hard problem — propagation (raised by Mike 2026-07-10)

*"How do we learn this lesson once — keep all sessions and repos up to date as
the house doctrine changes? Child repos like faves need to feed off the house
doctrine repo."* This is the load-bearing architecture question for atelier and
is in the first Fable review's scope.

- [ ] **Design the propagation mechanism.** How a doctrine change in atelier
      reaches every child repo and every session, without a manual sync
      nightmare or a second diverging source of truth. Candidate shapes to weigh
      (Fable to pressure-test): child repos *reference* atelier (a pointer in
      each CLAUDE.md that says "the doctrine lives in atelier; read it there")
      vs *vendored copy* + a drift-check that flags staleness vs a session-start
      hook that pulls latest. Whatever wins must respect DRY (one source) and be
      observable (a repo can tell when it's behind).
- [ ] **Repo-boundary guidance** — Claude should *direct* whether a new piece of
      work is its own repo or a component of an existing one (Mike: "you should
      direct more"). E.g. rich EPL work = own repo vs component vs monorepo
      folder. A short decision guide in `build/`, and the standing behaviour to
      advise proactively rather than wait to be told.

## Now — method/ layer standing up

- [x] Scaffold; `00-APEX`, `AUTONOMY`, `STORAGE`, `CONCURRENCY`, `TOOLBOX`.
- [x] Autonomy widened to standing commit+push+PR for all work (2026-07-10).
- [ ] **Extract `PRINCIPLES.md` spine** from ros — the named principles +
      precedence ladder + situation tests, generalised out of tiki examples.
      Leave the tiki bearings + review case-law in ros. (Stub in place.)
- [ ] **Extract `MODEL-ECONOMICS.md`** general shape from ros; keep the
      estate-specific model/pool numbers machine-local. (Stub in place.)
- [ ] Write **session + doc-as-code discipline** and the
      **review-with-a-more-capable-model** practice into `method/`.

## Next — build/ layer + inheritance

- [ ] Extract the `create-repo` standard into `docs/build/` as the readable
      source; move `templates/` alongside.
- [ ] **Rewire `create-repo` to inherit from atelier** — the core fix: new repos
      inherit doctrine, not empty templates.

## Then — the machine-local instance (not in this repo)

- [ ] Capture the concrete **toolbox manifest** machine-local (`~/.claude/`):
      installed/approved tools, auth scopes, venv paths, connected services —
      so sessions stop rediscovering. Doctrine is `method/TOOLBOX.md`; the
      inventory itself never enters this shareable repo.

## North star — work from any device, anywhere (Mike 2026-07-10)

Two distinct goals, kept distinct on purpose:

- [ ] **Personal context travels with the *person*, not the device.** Mike's
      personal context (`~/.claude`) should be reachable from any of his devices
      (iPhone, MacBook, and their successors) — synced to *him*, not pinned to
      one machine. This does NOT weaken the rule that personal context never
      enters a *shareable repo*: it travels with Mike privately; it still never
      lands in atelier or any repo handed to a peer. (Design: where does the
      personal store live so it's on every device but never in a shared repo?
      Fable to weigh.)
- [ ] **Resume any project from any device.** The end state: pick up work on any
      repo/idea with Claude from any device, anywhere. Depends on the
      propagation + portable-context threads above.

## Session archive (Mike wondering, 2026-07-10)

- [ ] Decide whether to **archive every session** (chat, cowork, CLI, VS Code)
      for detail-on-demand — a kept-if-needed record, not regularly referenced.
      SESSIONS.md stays the human *index*; this would be the raw *detail* store.
      Feasibility: Claude Code already writes local transcripts
      (`~/.claude/projects/**/*.jsonl`); the work is collecting + backing them
      up (iCloud/NAS) and deciding retention/search. Design question for the
      review: worth the storage + privacy handling, or index-only enough?

## Sharing (private-first)

- [ ] Decide owner/visibility and push (deferred — Mike's call).
- [ ] Share with CEL/EPL peers; harden in real use.
- [ ] Decide public release + packaging (readable repo vs Claude Code
      plugin/skills bundle) once the layers are populated. Reuse the ros
      `PUBLISHING.md` pattern (extract public subset, scrub, fresh export).

## Open questions

- Does ros keep its own `PRINCIPLES.md`/`MODEL-ECONOMICS.md` as the canonical
  copy and atelier hold the general spine, or does atelier become canonical and
  ros reference it? (Resolve when extracting — avoid two diverging sources.)
- Naming/identity for the shared package when it goes to peers.
