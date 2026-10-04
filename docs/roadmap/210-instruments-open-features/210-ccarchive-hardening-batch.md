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

      **The rulings walk, 2026-10-05, before any build.** Three further
      questions, and two of his answers are his own words, so they are
      rulings and quoted whole:

      - **Index repair — Mike's ruling, verbatim:** *"Yes fix it from the
        archive but it should be when we can tell that ccarchive has failed
        part way i.e. this is an error handling condition. We don't want
        someone able to add files (copy files to ccarchives destination) and
        then they get adopted as ccarchive data when they are not. The idea of
        signing the archives data and the manifest is integrity of the data as
        well as a manifest being more efficent to read than reading the data
        archived. So whatever you do needs a way to handle that, perhaps we fix
        it from the archive as you recommended but if there is data in the
        archive that is not signed then we compare it to the primary data
        (local /live copy) and if its identical (SHA hash etc) we can sign it
        and update the index as expected. If it is not identical to the priary
        data maybe there are other steps you can recommend before we fallback
        to erroring to the user to explain the situation"*. The rule built from
        it, played back and answered *"Yes, build that"*: a run keeps a private
        intent log beside the signing key, off the archive, of each mirror it
        is about to write; (1) after a run dies, the next run repairs the index
        only for mirrors that log says ccarchive wrote; (2) any other archive
        file the signed index does not vouch for is adopted only if its
        SHA-256 equals the live copy's; (3) anything else is moved to a
        not-trusted folder in the archive, never deleted and never adopted, the
        live copy is archived properly, and the run exits non-zero explaining
        what was set aside and why. This settles HL15 and HL6.
      - **Overlapping runs — Mike's ruling, verbatim** (a lock-free design was
        offered first): *"No that sounds worse than dealing with locks that get
        stuck. Let use the lock option but there needs to be a way to tell if a
        lock is stuck and to clear the stuck lock"*. So: a lock, a way to see
        whether it is stuck, and a way to clear a stuck one.
      - **Old versions — answer:** *"Any edit that isn't a pure addition"* —
        whenever a non-transcript document changes other than by appending,
        the previous mirror is kept as a dated copy. Widens the shrink-only
        answer above. Transcripts keep the strict refusal.
      - Also answered, off this item: encryption's crypto source is C′
        (`210/030`).
      - Not put to Mike, and why: the HL9/MC9 and HL4/MC2 severity splits are
        moot because every one of those findings is built; `210/200`'s
        evicted-file choice dissolves because a run will no longer read a
        mirror to replace it; `210/160`'s "session" definition is the
        builder's call, per its own text.

      **Mike's model of the data, verbatim (2026-10-05, mid-build):**
      *"ccarchive exists to keep my claude code session transcripts so that we
      can refer and learn from them over time. The way I see it ccarchive will
      deal with, 1. Data that is active for a while and then never changes
      again after. Most session transcripts will be like this where once I
      have finished with the session and closed it off I never change it
      again, and neither should anything else. On the rare occassion I do
      re-open a closed session to look something up, and its even rarier for
      me to pick up that session by giving it prompts etc... I do however do
      that regularly with sessions that have paused for a variety of reasons
      and I had not finished with the session yet e.g. out of claude budget,
      computer issues, internet connectivity issues, waiting for me to get
      back to a topic etc 2. Data like the memory file you mentioned where
      claude (or other software maybe) alters an existing file over time
      rather than starting new files like we do with session transcripts."*

      **How the build reads it** (stated back to him, open to correction):
      two classes. **Append-only records** (transcripts, subagent logs, prompt
      history, tool-result sidecars): the only legitimate change is growth at
      the end, however long after the last one. Any other change, a shrink or
      a rewrite in place, is an anomaly. The archived copy is never
      overwritten, the changed version is kept aside, and the run reports it.
      This **retires the old same-size-rewrite-replaces-the-mirror behaviour**
      (S4c in the HL verdict). **Living documents** (memory notes, metadata
      sidecars): any change that is not a pure addition keeps the previous
      version as a dated copy. Pure growth is checked without reading the
      mirror: the hash of the source's first recorded-length bytes must equal
      the signed index's hash.
