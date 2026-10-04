- [~] **ccarchive hardening — build the cold passes' counsel so an ordinary run
      can never overwrite or lose a good archived copy** (claimed 2026-10-04-2329,
      wt: atelier-ccarchive-1005)

      Mike, 2026-10-05, setting the run: *"work related to ccarchive - I want to
      be able to rely on it to protect my session transcript data as I expect it
      too"*. Put to him in plain words — the reviewers' fix set, one principle:
      trust the archived copy over the live file, write safely, skip-and-report
      a bad file instead of dying, check before restoring — his answer was
      *"If there are rulings related to ccarchive lets do them now in case it
      effects your work. After that I want you to build all of it"*.

      **Scope:** the follow-up checklists of the MC verdict
      ([`2026-10-03-0357-manifest-checkpoints-cold.md`](../../reviews/2026-10-03-0357-manifest-checkpoints-cold.md))
      and the HL verdict
      ([`2026-10-04-2215-ccarchive-heal-pulled-cold.md`](../../reviews/2026-10-04-2215-ccarchive-heal-pulled-cold.md)),
      together with `210/010`, `170`, `190` and `200`, which the same code
      change closes or touches. Two choices were put to Mike as options and
      answered (answers, not rulings in his own words): HL3 — a run whose
      manifest signature does not verify **stops and says so**, cleared
      deliberately with `--rekey`; `210/010`'s class — a memory note that
      shrinks **keeps both versions**, the old one as a dated copy beside the
      new, while transcripts keep the strict refusal.

      Rulings first: any other open ccarchive decision is walked with Mike
      before the build starts, so the build does not land on an unruled shape.
