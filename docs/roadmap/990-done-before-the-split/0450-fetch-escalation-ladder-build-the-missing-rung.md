- [x] **Fetch escalation ladder — build the missing rungs + elevate to doctrine**
      — DONE 2026-07-12 (session 47): doctrine elevated (`method/REACH.md`,
      reviewed) and both build sub-items shipped (multi-engine rung 3,
      live-verified; explicit rung-4/5 port split). The full ladder is documented
      in `instruments/browser-fetch/README.md` (rungs 1 WebFetch/WebSearch ·
      2 curl · 3 `browser_fetch` standalone headless, now Chrome/Firefox/WebKit ·
      4 persistent dedicated profile `:9222` · 5 persistent everyday session
      `:9223` · 6 ask the operator). The **only residual is operator-gated**: a
      live rung-5 fetch needs the operator's everyday Chrome on `:9223`.
      Sub-items, for the record:
      - [x] **Other engines** — DONE 2026-07-12 (session 47). `browser_fetch`
            (rung 3) gains an `engine` param: `chromium` (default, real installed
            Chrome), `firefox` (Gecko), `webkit` (Safari's engine) — a second
            engine is a second way past anti-bot that keys on Chrome/headless
            specifically. Firefox + WebKit **live-verified** (each fetched
            example.com end-to-end through the server path). **Honest limit:**
            rungs 4/5 stay **Chrome-only by protocol** — CDP is Chrome's, and
            Playwright's `connect_over_cdp` speaks only CDP; Firefox/WebKit have
            no connect-to-running equivalent. Not a fillable stub — a real limit,
            documented in code + README.
      - [x] **Cleaner 4/5 split** — DONE 2026-07-12 (session 47). Made explicit
            two ways at once: `browser_fetch_persistent` gains a `rung` param
            (`4` dedicated / `5` everyday), each mapping to a **distinct port**
            (rung 4 → `:9222`, rung 5 → `:9223`) the operator binds to the
            matching profile — replacing the implicit "which profile is on
            `:9222`". Rung-specific not-reachable errors (rung 5's names the
            credential boundary and warns it's a deliberate escalation).
            Rung-4 live-proven on adoption (change is port-param, unit-covered);
            **rung-5 live fetch is owed-to-operator** by nature (needs the
            operator's everyday Chrome on `:9223` — can't be self-driven).
      - [x] **Elevate the credential boundary + ladder to `method/` doctrine**
            — DONE 2026-07-12 (session 47, Opus): `method/REACH.md` written,
            grounded in the browser-fetch README + this item. Both halves in one
            doc: the escalation ladder (engine-agnostic, cheapest-first) and the
            credential boundary as a purpose-of-storage test. Named for the
            instruments' third verb (*extend reach*, ADR 0006), indexed after
            ACCESS in the SECRETS/ACCESS family. **Review-owed** (cold
            fresh-context, session-40/44 pattern) — pre-seeded questions: does
            the ladder's generic shape stay honestly grounded without inventing
            rungs the instance doesn't have; is the two-halves-one-doc join
            argued or asserted; does the purpose-of-storage test cover the real
            estate cases without outlawing intended use. The rule as captured:
            - **Provisioned stores are the intended path** — credentials saved
              *so that* a repo/tool/agent can use them (keychain items the estate
              registry records, minted per-consumer API tokens, the SECRETS/
              ACCESS machinery). Agent use is what they exist for; in scope by
              design.
            - **Personal convenience stores are off-limits by default** — a
              browser profile's saved logins, the principal's password manager
              (here Apple Passwords; browsers hold little to nothing by his own
              practice): saved over years to ease the *principal's own* browsing,
              never provisioned for agent use, and far broader than any task
              needs. Riding an already-authenticated *session* is fine; the
              stored credentials that mint sessions are the line.
            - **The principal can grant across the line** — temporary or
              permanent, per credential, his explicit act; a grant moves that
              credential into the intended path (and belongs in the provisioned
              machinery, not ad-hoc).
            A shareable SECRETS/ACCESS-family boundary, currently stated only
            operationally in the browser-fetch README. The escalation principle
            (start cheapest, step down only when blocked) is likewise general.
