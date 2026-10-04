#!/usr/bin/env python3
"""Read and use existing EconFinHarness materials.

Usage: python3 tools/fh.py <command> [args]

  search [query] [--index PATH]  search an optional existing local index, read-only
  recipe <artid> [--specs|--json] read an existing code card
  exemplars <method> [--lang L]  show existing implementation examples
  skills list|show <id>         read an operation guide
  agents list|show <id>         read a role description
  workflows list|show <id>      read optional working steps
  presets list|show <id>        read a common task prompt (expand is an alias)
  sync-adapters [--host H]      copy current roles and skills to host configuration
  status                       show available materials

Ordinary tasks use instructions and files directly. Historical building and
process-management commands are not part of this interface.
"""
import argparse
import sys

import fh_common as C

def read_guide(kind, argv):
    ap = argparse.ArgumentParser(prog=f"fh {kind}")
    ap.add_argument("action", choices=["list", "show", "expand"], nargs="?", default="list")
    ap.add_argument("id", nargs="?")
    a = ap.parse_args(argv)
    directory = {"skills": C.SKILLS, "agents": C.AGENTS,
                 "workflows": C.WORKFLOWS, "presets": C.PRESETS}[kind]
    entries = {p.parent.name: p for p in directory.glob("*/SKILL.md")} if kind == "skills" else {
        p.stem: p for p in directory.glob("*.md") if p.name != "README.md"}
    if a.action == "list":
        for name, path in sorted(entries.items()):
            print(f"{name:<24} {C.rel(path)}")
        return 0
    if not a.id or a.id not in entries:
        ap.error(f"choose one of: {', '.join(sorted(entries))}")
    print(entries[a.id].read_text(encoding="utf-8"))
    return 0

def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd, rest = args[0], args[1:]
    if cmd == "search":
        import fh_index
        return fh_index.main(rest)
    if cmd in ("recipe", "exemplars"):
        import fh_cards
        fh_cards.main([cmd] + rest)
        return 0
    if cmd in ("skills", "agents", "workflows", "presets"):
        return read_guide(cmd, rest)
    if cmd == "sync-adapters":
        import fh_adapters
        return fh_adapters.main(rest)
    if cmd == "status":
        for name, directory, pattern in (
                ("Code cards", C.RECIPES, "*.json"),
                ("Paper notes", C.NOTES, "*.json"),
                ("Skills", C.SKILLS, "*/SKILL.md"),
                ("Roles", C.AGENTS, "*.md"),
                ("Method materials", C.PARADIGMS, "*/recommendations.md")):
            print(f"{name}: {len(list(directory.glob(pattern)))}")
        return 0
    print(f"Command {cmd!r} is not part of the current interface. Read AGENTS.md and use the task's files directly.")
    return 2

if __name__ == "__main__":
    sys.exit(main() or 0)
