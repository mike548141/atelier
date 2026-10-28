- [ ] 🎯 **Rule-4 cold pass queued: the staged-positional reader the three
      staged-diff guards share (`115/360`).** Guard code, doctrine by
      function: a clean `--staged` scan is read as "nothing barred was
      staged". So the authoring session (a Mike-opened Opus 5.5 queue run,
      session 8e498ef1, 2026-10-18, wt atelier-qr-115-360, which dispatched
      the Sonnet worker that wrote the code) queues this and does not take
      it.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/report.py` (`scope_staged`),
      `tools/leakscan.py`, `tools/secretscan.py`, `tools/conflictscan.py`
      and their four `tools/test_*.py` files, commit `692c04a` on `main`,
      2026-10-18. One question the author could not settle alone: whether
      any child's declared scope relied on the old exact-spelling match.
      *Intent record:*
      [`../115-guardrail-architecture-mike-commissioned/360-a-bare-dot-scope-makes-the-staged-plane-scan-nothing.md`](../115-guardrail-architecture-mike-commissioned/360-a-bare-dot-scope-makes-the-staged-plane-scan-nothing.md).
      📝 BRIEF WRITTEN 2026-10-26 by session 5070f22b (Opus 5.5):
      `docs/reviews/2026-10-26-0912-staged-positional-reader-cold.md`, with
      its `.deferred.md` sibling; this session may not run the pass. Written
      by an Opus 5.5 subagent of that headless brief-writing session, which
      authored none of the delta; review NOT run. The pass waits for a
      criterion-passing cold Fable session and the principal's explicit
      permission for Fable work.
      ✅ **PASS RAN 2026-10-28** (Fable 5.1 xhigh through the Claude Platform
      API on the principal's monthly credit, approved 2026-10-28;
      orchestrator session `f7b25adb`, which formed no finding).
      **PASS-WITH-FINDINGS — 1 MAJOR · 2 MODERATE · 3 minor · 5 notes**,
      in the brief with the folded sibling. **QS1 (MAJOR):** a committed
      scope whose spelling differs from git's by case or Unicode
      normalisation renders, passes every floor guard, and the boundary
      guards print clean over a staged live-shaped secret (reproduced on a
      probe repo); counsel at reconcile: let git resolve the positional
      (`git ls-files -z -- <normalised>`), which closes QS1 and QS2
      together. Answers the author's open question: no child on this
      machine changes behaviour. 🎯 **The principal's:** every finding;
      QS11 asks that the `115/360` record carry the narrower truth beside
      the ruling.
      ⏳ **TOP-UP BRIEF WRITTEN 2026-10-28** by session `29af7e91` (Opus 5.5,
      off-tier, forms no finding): the API pass could not run the checks
      under QS1, QS4 and QS9 (signing-broken git, lost suite summary, empty
      term list, no real commit, no `/security-review`, no `gh`).
      `docs/reviews/2026-10-28-1255-staged-positional-reader-topup-cold.md`,
      with its `.deferred.md` sibling; Fable on the laptop, checked at
      selection; ends with a TOP-UP SUFFICES or FULL RE-RUN verdict. Barred:
      `8e498ef1` and its workers, `5070f22b` and its subagents, `f7b25adb`
      (built the harness; may not orchestrate), `29af7e91`.
