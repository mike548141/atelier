# 2026-07-23 · 0149 UTC · SA1–SA9 ruled and applied — secrets/access cycle closed (Fable, wt: sa-rulings-apply)

**Ask:** continuation of "work through the open decisions one by one" — after
QR1–QR9 closed, the SA set (secrets/access cold pass, PASS 0M/4m/4L/1n,
2026-07-22 1021) was the next decision set owed to Mike.

**Rulings.** Presented plain-language with context and likely impacts
(AskUserQuestion, two batches). Mike: accept-all as counselled; SA4 as
**name the break-glass class** (not out-of-scope); SA9 as the **repo-wide
artefact sweep**.

**Application.** By a session that authored neither the SECRETS.md delta
(`caa85fe`) nor the 1021 verdict; claim `7f83142` on `main` first, worktree
`sa-rulings-apply`. Delta `f8350ee` + stamps `86bad85`. Sweep scope call:
immutable records (sessions, reviews, CHANGELOG history, ADRs) untouched;
vendor feature names keep vendor spelling ("artifact attestations").
**Terminal application** — the pass carried no MAJOR, so the cycle closes on
this landing with no further pointer (the `87af9f9` shape).

**Mid-run provenance check.** Mike flagged a possibly-competing parallel
session mid-application; verified against origin before continuing — the
parallel session's landings were VP1–VP8 + D1–D5 (disjoint sets), SECRETS.md
untouched since `caa85fe`, the SA verdict unstamped, this session's claim the
newest commit. Mike then confirmed the flag was a mis-paste and the other
session is staying clear.

**Proofs at the applied state:** tool suite 330 OK · instruments 139 OK ·
secretscan/leakscan/linkscan/reviewscan/sizescan all exit 0. Item harvested
to ROADMAP-DONE; CHANGELOG closed.
