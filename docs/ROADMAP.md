# atelier ROADMAP

Lean and read every session. Completed detail moves to `ROADMAP-DONE.md` once
this grows.

## Now — method/ layer standing up

- [x] Scaffold; `00-APEX`, `AUTONOMY`, `STORAGE`, `CONCURRENCY`, `TOOLBOX`.
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
