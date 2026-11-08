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
      `[~]` **TOP-UP CLAIMED 2026-11-01-1335** (wt: atelier-160-950-1335; cold pass: a Fable 5.1
      reviewer under an Opus 5.5 headless orchestrator, session 4610c607,
      itself started by session c87c4ee0; both are rule-4 off-tier
      orchestrators that hold the context partition, form no finding and
      write no severity; neither authored the delta, the original brief, the
      API harness or the top-up brief, nor was started or instructed by
      session 8e498ef1, 5070f22b, f7b25adb or 29af7e91). Runs under the
      principal's 2026-11-02 drain approval for Fable work. The 2026-10-29
      hold on running the top-ups is lifted by the principal for this drain,
      2026-11-02, verbatim: *"lift it and any others where I said to do it
      later"*.
      🎯 **TOP-UP PASS RAN 2026-11-01-1404 — PASS-WITH-FINDINGS, 1 MAJOR · 2
      MODERATE · 3 minor · 8 notes** (original plus top-up, QS1–QS11 and
      QU1–QU3; verdict and reconcile in the top-up brief, the deferred
      sibling folded below them). **TOP-UP SUFFICES**, the reviewer's answer
      to the principal's 2026-10-28 ask: every sandbox limit under a finding
      was re-driven on the laptop and each attribution held (four delta files
      green, full suite 2032 OK, floor green with the real term list, signing
      works). No severity changed, no API finding refuted. **QS1 (MAJOR)
      stands, now on real `git commit`s at the real gate:** a scope spelt by
      case or Unicode normalisation differently from git lets a staged
      live-shaped secret through the hook; CI reds only after the push, which
      detects but does not prevent. New notes: QU1 the per-guard test copies
      do not pin the exact-file positional; QU2 warn-only ci-plane findings
      outside the delta (this pointer's own glyph, cleared by this flip);
      QU3, formed at reconcile, `test_pins.py`'s 60 s wall-clock bound makes
      the full suite load-sensitive.
      *Owed to the principal (rule 3), all recorded, none applied:* a ruling
      on each finding, QS1 first, then QS2–QS11 and QU1–QU3; plus one ask
      the drain put here rather than asking: (a) accept TOP-UP SUFFICES, or
      still order a full laptop re-run (his 2026-10-28 default for degraded
      passes; the reviewer recommends the top-up suffices).
      *Routing:* code fixes in `tools/` here (QS1, QS4 with QU1, QS9, QU3);
      QS11's narrower truth on the `115/360` record; QU2's other two
      findings belong to the `970` pointer and the 2026-10-03 exception
      register's record.
      💬 **Mike's answer, 2026-11-08 (to options session 722ac2e2 offered in
      its ruling round; an answer, not a ruling):** *"Fix it + take advice"* —
      the offered option read: fix QS1 the way the reviewer counselled (let
      git resolve the positional), apply the reviewer's counsel on the other
      13 findings (QS2–QS11, QU1–QU3, QU3 being the 60 s wall-clock bound in
      `test_pins.py`), and accept **TOP-UP SUFFICES** with no full laptop
      re-run. The application is to queue a Fable re-check, which waits for
      his approval as usual (a MAJOR stood in the pass).
      ✅ **APPLIED 2026-11-09** by queue run 722ac2e2 (a Sonnet worker, read by
      the orchestrator before landing), per Mike's answer above: QS1/QS2 —
      `tools/report.py` `resolve_staged_scope` lets git resolve each staged
      positional as a literal root-anchored pathspec and refuses (exit 2) one
      git does not know, so a case or Unicode variant can no longer pass a
      staged secret; QS3–QS11, QU1 and QU3 (the `test_pins.py` bound is now a
      600 s hang guard) as counselled; QS11's narrower truth is on the
      `115/360` record. Fail-before shown for every code finding; full suite
      2402 OK. Probed before landing: every declared `scope` path in the five
      children that declare one is tracked, so none goes red. **Two calls for
      him:** the reader also reaches five other scanners (`datescan`,
      `sizescan`, `spellscan`, `reviewscan`, `wrapscan`), which now refuse an
      unknown scope too; and a declared scope directory that exists but holds
      no tracked file now blocks the commit (exit 2). QU2's other two
      findings stay with the `970` pointer and the exception register. A
      MAJOR stood, so the application's cold pass is queued as `160/1070`.
