- [ ] 🔑 **The fifth instance is not a report — it is a GUARD, and that is the
      version of this that cannot be double-checked.** Found 2026-08-23 in
      docker-heap, from a completely different direction to the other four, which
      is the best evidence available that the pattern is real rather than one
      session's bad luck.
  - [ ] **What happened.** The ZFS dataset-split tool is meant to exist
        byte-identically in three places: `tools/media-split.sh` in docker-heap,
        `How to and Scripts/zfs-dataset-split.sh` in homenetwork, and
        `~claude/media-split.sh` on the TrueNAS host. It did not, and the drift
        was **two-directional** — each copy held something the other lacked, so
        neither was simply stale. The doc half was harmless. The other half was
        not: the two copies used **different internal names** — a different
        `WORK_ROOT`, a different container-name prefix, and a different filename
        for the copy the tool self-extracts into its worker container.
  - [ ] 🛑 **Why that is the same defect wired to something that acts.** The tool
        has a guard, `restart_consumers`, whose entire job is to restart the
        containers that consume a folder **without restarting the tool's own
        long-running jobs**. It exists because the tool had already restarted its
        own verification container once, costing two hours of hashing. The guard
        excludes its own work by matching two strings: the container name prefix,
        **and** the script name in the container's command — deliberately both,
        because either alone had already failed once.
        **Given a job started from the other copy, that guard matches neither
        string.** It does not error. It reports nothing to exclude, and then
        restarts a live 366 GB transfer.
  - [ ] **The sentence, which is `370`'s own with one noun changed:**
        *a verification that cannot display the passing state is not a
        verification* → **a guard that cannot recognise the state it exists to
        detect is not a guard.** In both cases the instrument's blind spot is
        exactly the condition it was built for, and in both cases it fails by
        being quiet.
  - [ ] ⚠️ **And it is worse than the four report cases, in one specific way.** A
        report is addressed to a person, so a person can corroborate it against
        the artefacts — which is what `010` recommends and what saved the 348 GB
        deletion. **A guard's whole purpose is to fire when nobody is looking.**
        There is no moment at which someone reads its output and thinks to check.
        So for guards the artefact-corroboration rule has nothing to attach to,
        and the prevention has to be structural instead.
  - [ ] 🎯 **The candidate rule, and it is cheap.** Where a guard identifies its
        own work by a **convention rather than a fact** — a name prefix, a path, a
        marker string — that convention is a **shared invariant**, and it must be
        stated where the guard lives rather than in a playbook beside it. A rule
        that lives only in the playbook is a rule the next copy does not carry.
        The instance was fixed by writing *filenames may vary, internal names must
        not* into the header of the file itself, above the code that depends on it.
  - [ ] 🔎 **The general shape, if it is worth generalising:** duplicating a file
        duplicates its **data** and silently forks its **conventions**. Anything
        that keeps two copies of an executable in step needs to say which parts
        are allowed to differ. Sits beside `360` — *name what you launch* — which
        is the same problem approached from the launch side rather than the
        recognition side.
