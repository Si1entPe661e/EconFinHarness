#!/usr/bin/env python3
"""Compatibility entry for existing-material queries.

Usage: python3 harness_build/cli/fhb.py search [query] [filters]
       python3 harness_build/cli/fhb.py status

This entry does not regenerate cards, notes, method summaries or the index.
"""
import sys
import fh_common as C

def status():
    for name, directory in (("Code cards", C.RECIPES),
                            ("Paper notes", C.BUILD / "papers/notes")):
        print(f"{name}: {len(list(directory.glob('*.json')))}")
    print(f"Method materials: {len(list(C.PARADIGMS.glob('*/recommendations.md')))}")
    print(f"Existing index: {'available' if (C.INDEX / 'fh_index.sqlite').exists() else 'unavailable'}")
    return 0

def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if args[0] == "status":
        return status()
    if args[0] == "search":
        import fh_index
        return fh_index.main(args[1:])
    print("Historical construction commands are retired from this entry. Existing results remain available; read AGENTS.md for current working practice.")
    return 2

if __name__ == "__main__":
    sys.exit(main() or 0)
