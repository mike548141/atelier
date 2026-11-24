#!/usr/bin/env python3
"""atelier-menu -- print every /atelier: command the plugin ships, as a table.

Why (board 450/010 row 14): the principal pressed Enter on `/atelier` and on
`/atelier:` expecting the list of the plugin's commands. Claude Code's picker
shows that list only while the prefix is being typed, and a plugin's skills are
always `/<plugin>:<name>`, so no plugin skill can answer a bare `/atelier`. This
script is the body of a user-level skill named `atelier` (linked into
`~/.claude/skills/atelier` by `instruments/install`) that does.

Every /atelier: command is subject, space, action (board 450/020): one skill
per subject, `skills/<subject>/SKILL.md`, and one file per action beside it,
`skills/<subject>/<action>.md`, whose front matter carries `action:`. A bare
subject shows its own menu, which is this script given the subject's name.

The menu is read at run time from the plugin's own front matter -- every
subject's action files, any skill with no action files, and any
`commands/*.md` -- never from a typed list, so a command added to the plugin
appears here with no edit.

  menu.py              the menu of every command, as a Markdown table
  menu.py SUBJECT      one subject's actions (a bare /atelier:SUBJECT)
  menu.py --root DIR   read the plugin at DIR (default: this file's repo)
  menu.py --selftest   prove it lists a fixture plugin and stays quiet on junk
"""
import argparse
import os
import re
import sys
import tempfile

PREFIX = "atelier"
FIRST_SENTENCE = re.compile(r"^(.+?[.!?])(\s|$)")


def front_matter(path):
    """Return the YAML front matter of a Markdown file as a flat dict.

    Only `key: value` lines are read; that is all the plugin's files use, and a
    full YAML parser would be a dependency for nothing."""
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        return {}
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        return {}
    out = {}
    for line in text[4:end].splitlines():
        m = re.match(r"^([A-Za-z][\w-]*):\s*(.*)$", line)
        if m:
            out[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return out


def short(desc):
    """The description's lead clause, so the table stays one line a row: the
    text before the first spaced dash, else its first sentence."""
    desc = " ".join(desc.split()).split(" — ")[0]
    m = FIRST_SENTENCE.match(desc)
    return m.group(1) if m else desc


def actions(skill_dir):
    """(action, description) for each action file of a subject skill: a
    Markdown file beside SKILL.md whose front matter names an `action`."""
    out = []
    for fn in sorted(os.listdir(skill_dir)):
        if fn.endswith(".md") and fn != "SKILL.md":
            fm = front_matter(os.path.join(skill_dir, fn))
            if fm.get("action"):
                out.append((fm["action"], short(fm.get("description", ""))))
    return out


def entries(root, subject=None):
    """Rows of (command after the prefix, what it does). With `subject`, only
    that subject's actions."""
    rows = []
    skills = os.path.join(root, "skills")
    if os.path.isdir(skills):
        for name in sorted(os.listdir(skills)):
            d = os.path.join(skills, name)
            fm = front_matter(os.path.join(d, "SKILL.md"))
            if not fm:
                continue
            s = fm.get("name") or name
            if subject is not None and s != subject:
                continue
            acts = actions(d)
            if acts:
                rows += [(f"{s} {a}", desc) for a, desc in acts]
            else:
                rows.append((s, short(fm.get("description", ""))))
    commands = os.path.join(root, "commands")
    if subject is None and os.path.isdir(commands):
        for fn in sorted(os.listdir(commands)):
            if fn.endswith(".md"):
                fm = front_matter(os.path.join(commands, fn))
                rows.append((fn[:-3], short(fm.get("description", ""))))
    return sorted(rows)


def subjects(root):
    return sorted({r[0].split(" ")[0] for r in entries(root)})


def render(rows, subject=None):
    if not rows:
        return "No /atelier: commands found -- is the plugin checkout where this skill points?\n"
    lines = ["| Command | What it does |", "|---|---|"]
    for name, desc in rows:
        lines.append(f"| `/{PREFIX}:{name}` | {desc.replace('|', '/')} |")
    lines.append("")
    if subject:
        lines.append(f"`/{PREFIX}:{subject}` on its own only shows this menu. "
                     f"To run one, type it with its action, as listed.")
    else:
        lines.append(f"Each command is a subject and an action. A subject on its own "
                     f"(such as `/{PREFIX}:{rows[0][0].split(' ')[0]}`) shows only its own menu.")
    return "\n".join(lines) + "\n"


def default_root():
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


def selftest():
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, "skills", "alpha"))
        os.makedirs(os.path.join(d, "skills", "gamma"))
        os.makedirs(os.path.join(d, "skills", "broken"))
        os.makedirs(os.path.join(d, "commands"))
        with open(os.path.join(d, "skills", "alpha", "SKILL.md"), "w") as f:
            f.write("---\nname: alpha\ndescription: Does A — in detail. Then more.\n---\nbody\n")
        with open(os.path.join(d, "skills", "gamma", "SKILL.md"), "w") as f:
            f.write("---\nname: gamma\ndescription: Router.\n---\nbody\n")
        with open(os.path.join(d, "skills", "gamma", "go.md"), "w") as f:
            f.write("---\naction: go\ndescription: Goes — fast.\n---\nbody\n")
        with open(os.path.join(d, "skills", "gamma", "notes.md"), "w") as f:
            f.write("a supporting file with no front matter\n")
        with open(os.path.join(d, "skills", "broken", "SKILL.md"), "w") as f:
            f.write("no front matter\n")
        with open(os.path.join(d, "commands", "beta.md"), "w") as f:
            f.write('---\ndescription: "Does B | safely."\n---\n')
        rows = entries(d)
        assert rows == [("alpha", "Does A"), ("beta", "Does B | safely."), ("gamma go", "Goes")], rows
        out = render(rows)
        assert "`/atelier:alpha` | Does A |" in out, out
        assert "`/atelier:gamma go` | Goes |" in out, out
        assert "Does B / safely." in out, out
        assert "broken" not in out and "notes" not in out and "Router" not in out, out
        assert entries(d, "gamma") == [("gamma go", "Goes")]
        assert "on its own only shows this menu" in render(entries(d, "gamma"), "gamma")
        assert entries(d, "nope") == []
        assert "No /atelier: commands" in render([])
    print("✓ atelier-menu selftest: lists subjects' actions and plain skills, one subject on its own, skips junk")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="Print every /atelier: command as a table.")
    ap.add_argument("subject", nargs="?", default=None, help="one subject's actions only")
    ap.add_argument("--root", default=None)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    if a.selftest:
        return selftest()
    root = a.root or default_root()
    if a.subject:
        rows = entries(root, a.subject)
        if rows:
            sys.stdout.write(render(rows, a.subject))
            return 0
        sys.stdout.write(f"There is no `/{PREFIX}:{a.subject}`. Every command:\n\n")
    sys.stdout.write(render(entries(root)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
