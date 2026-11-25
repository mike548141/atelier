#!/usr/bin/env python3
"""A reference review queue that keeps ccfleet's seal contract (man ccfleet,
THE QUEUE INTERFACE). Every name in it, and in any state it is given, is
fictional. It is small on purpose: the tests drive ccfleet against it, and an
adopter can read in one sitting what stops an unplanned paid pass.

The contract it keeps: until this run's ranking is sealed, `ranked`, `next`
and `take` refuse (exit 1), so a pass started by hand (`ccfleet pass`) meets
the same gate as a drain's. A run is its --by id: the seal is keyed by it, so
a session with another id holds no seal. ccfleet never calls `seal`; the
`/atelier:review run` skill does, with the ranking its plan made.

State is one JSON file, named by $REVIEW_QUEUE_STATE:
  routes   {name: {"open": bool, "lapses_utc": "YYYY-MM-DDTHH:MM" or null}}
  reviews  [{repo, item, brief, title, fits (route names, cheapest first),
             briefed_by (the session id that wrote the brief)}]
  owed     [{repo, item, title, why}]   owed reviews with no brief yet
  claims   {"repo:item": {by, brief, ...}}   done  ["repo:item", ...]
  ended    {"repo:item": {what `update` recorded}}
  seal     null, or what `seal` wrote
$REVIEW_QUEUE_NOW (YYYY-MM-DDTHH:MM, UTC) stands in for the clock.

Commands, the shape ccfleet.example.json calls:
  evidence [--fetch]          JSON array of the briefed, unrun reviews (read-only)
  owed [--fetch]              JSON array of the owed, unbriefed ones (read-only)
  seal --by ID --ranking FILE [--words TEXT]
                              FILE: JSON array of {repo, item, route, why,
                              why_not_cheaper (when not the best route)}
  ranked --by ID              exit 0 only while ID's seal holds
  next --skip-file PATH --by ID
                              the next sealed review not in PATH, tab-separated
  take REPO:ITEM --by ID --brief PATH [--set K=V ...]
  release REPO:ITEM --by ID
  update REPO:ITEM --by ID --set K=V ...
"""
import argparse
import datetime as dt
import fcntl
import json
import os
import sys


def now():
    t = os.environ.get("REVIEW_QUEUE_NOW")
    return (dt.datetime.strptime(t, "%Y-%m-%dT%H:%M") if t else
            dt.datetime.now(dt.timezone.utc).replace(tzinfo=None))


def lapse(route):
    t = (route or {}).get("lapses_utc")
    return dt.datetime.strptime(t, "%Y-%m-%dT%H:%M") if t else None


def key(repo, item):
    return f"{repo}:{item}"


def refuse(msg):
    print(f"refused: {msg}", file=sys.stderr)
    sys.exit(1)


def sealed_for(state, by):
    """Why `by` holds no seal now, or "" when it does."""
    s = state.get("seal")
    if not s:
        return "no ranking is sealed"
    if s["by"] != by:
        return f"the sealed ranking is run {s['by']}'s, not {by}'s"
    if s.get("expires") and now() >= dt.datetime.strptime(s["expires"], "%Y-%m-%dT%H:%M"):
        return f"the seal lapsed at {s['expires']}"
    return ""


def ready(state):
    gone = set(state.get("claims", {})) | set(state.get("done", []))
    return [r for r in state.get("reviews", []) if key(r["repo"], r["item"]) not in gone]


def seal(state, by, ranking, words):
    """The seal's own rules (skills/review/run.md, The seal's own rules)."""
    routes = state.get("routes", {})
    open_routes = [n for n, r in routes.items() if r.get("open")]
    if len(open_routes) > 1 and any(lapse(routes[n]) is None for n in open_routes):
        refuse("two budgets are open and a lapse time is unknown")
    ranked = {key(e.get("repo"), e.get("item")): e for e in ranking}
    for r in ready(state):
        k = key(r["repo"], r["item"])
        e = ranked.get(k)
        if e is None:
            refuse(f"{k} is ready and missing from the ranking")
        if not str(e.get("why") or "").strip():
            refuse(f"{k} is unreasoned")
        if not routes.get(e.get("route"), {}).get("open"):
            refuse(f"{k} is on a closed route ({e.get('route')})")
        fits = [f for f in r.get("fits") or ["local"] if routes.get(f, {}).get("open")]
        if e["route"] not in (r.get("fits") or ["local"]):
            refuse(f"{k} does not fit route {e['route']}")
        if fits and e["route"] != fits[0] and not str(e.get("why_not_cheaper") or "").strip():
            refuse(f"{k} is on {e['route']}, later than {fits[0]}, without saying why")
        if r.get("briefed_by") == by:
            refuse(f"{k}: this session ({by}) wrote its brief, so it may not run it")
    lapses = [lapse(routes[e["route"]]) for e in ranking if lapse(routes.get(e["route"]))]
    state["seal"] = {"by": by, "words": words, "at": now().strftime("%Y-%m-%dT%H:%M"),
                     "order": [[e["repo"], e["item"], e["route"]] for e in ranking],
                     "expires": min(lapses).strftime("%Y-%m-%dT%H:%M") if lapses else None}


def next_pick(state, by, skip_file):
    why = sealed_for(state, by)
    if why:
        refuse(why)
    try:
        with open(skip_file, encoding="utf-8") as f:
            skip = {tuple(l.rstrip("\n").split("\t")[:2]) for l in f if l.strip()}
    except OSError:
        skip = set()
    rows = {(r["repo"], r["item"]): r for r in ready(state)}
    order = [(repo, item) for repo, item, _ in state["seal"]["order"]]
    # A review briefed after the seal runs last, until it is planned and sealed.
    order += [k for k in rows if k not in order]
    for k in order:
        if k in rows and k not in skip:
            print("\t".join([k[0], k[1], rows[k]["brief"]]))
            return


def sets(pairs):
    out = {}
    for p in pairs or []:
        k, _, v = p.partition("=")
        out[k] = v
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(prog="review_queue_reference")
    ap.add_argument("cmd", choices=["evidence", "owed", "seal", "ranked", "next", "take", "release", "update"])
    ap.add_argument("target", nargs="?")
    ap.add_argument("--by")
    ap.add_argument("--brief")
    ap.add_argument("--ranking")
    ap.add_argument("--words", default="none given")
    ap.add_argument("--skip-file")
    ap.add_argument("--set", action="append", dest="sets")
    ap.add_argument("--fetch", action="store_true")
    a = ap.parse_args(argv)
    path = os.environ.get("REVIEW_QUEUE_STATE")
    if not path:
        refuse("set REVIEW_QUEUE_STATE to the state file")
    with open(path + ".lock", "w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        with open(path, encoding="utf-8") as f:
            state = json.load(f)
        if a.cmd == "evidence":
            print(json.dumps([{k: r.get(k) for k in ("repo", "item", "brief", "title", "fits", "briefed_by")}
                              for r in ready(state)]))
            return 0
        if a.cmd == "owed":
            print(json.dumps(state.get("owed", [])))
            return 0
        if a.cmd in ("seal", "ranked", "next", "take", "release", "update") and not a.by:
            refuse(f"{a.cmd} needs --by")
        if a.cmd == "seal":
            with open(a.ranking, encoding="utf-8") as f:
                seal(state, a.by, json.load(f), a.words)
        elif a.cmd == "ranked":
            why = sealed_for(state, a.by)
            if why:
                refuse(why)
            return 0
        elif a.cmd == "next":
            next_pick(state, a.by, a.skip_file)
            return 0
        else:
            k = a.target or ""
            claims = state.setdefault("claims", {})
            if a.cmd == "take":
                why = sealed_for(state, a.by)
                if why:
                    refuse(why)
                if k in claims or k in state.get("done", []):
                    refuse(f"{k} is held or done")
                if not any(key(r["repo"], r["item"]) == k for r in state.get("reviews", [])):
                    refuse(f"{k} is not in the queue")
                claims[k] = {"by": a.by, "brief": a.brief, **sets(a.sets)}
            elif a.cmd == "update":
                # ccfleet's `ended` runs after a release too: what it records
                # is kept per item, and on the claim while one is held.
                state.setdefault("ended", {}).setdefault(k, {}).update(sets(a.sets))
                if claims.get(k, {}).get("by") == a.by:
                    claims[k].update(sets(a.sets))
            elif k not in claims or claims[k]["by"] != a.by:
                refuse(f"{k} is not held by {a.by}")
            else:
                del claims[k]
                state.setdefault("done", []).append(k)
        tmp = path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=1)
        os.replace(tmp, path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
