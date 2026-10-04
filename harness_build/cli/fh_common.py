"""Small path, JSON and Markdown helpers for reading existing research materials."""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
HARNESS = ROOT / "harness"
BUILD = ROOT / "harness_build"
PAPER = ROOT / "Paper"
PARADIGMS = HARNESS / "paradigms"
SKILLS = HARNESS / "skills"
AGENTS = HARNESS / "agents"
WORKFLOWS = HARNESS / "workflows"
PRESETS = HARNESS / "presets"
RECIPES = BUILD / "recipes/accepted"
INDEX = BUILD / "index"

def read_json(path):
    return json.loads(pathlib.Path(path).read_text(encoding="utf-8"))

def rel(path):
    try:
        return str(pathlib.Path(path).resolve().relative_to(ROOT))
    except ValueError:
        return str(path)

def parse_frontmatter(text: str):
    """Return (frontmatter dict, body) for a Markdown file with a leading YAML block (flat key: value only,
    lists as comma-separated strings or '- item' blocks). No YAML dependency."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    block, body = text[4:end], text[end + 5:]
    fm, key = {}, None
    for line in block.splitlines():
        if not line.strip():
            continue
        if line.startswith("  - ") and key is not None:
            fm.setdefault(key, [])
            if isinstance(fm[key], str):
                fm[key] = [fm[key]] if fm[key] else []
            fm[key].append(line[4:].strip())
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1]
            fm[key] = val
    return fm, body


def dump_frontmatter(fm: dict) -> str:
    lines = ["---"]
    for k, v in fm.items():
        if isinstance(v, list):
            lines.append(f"{k}:")
            for item in v:
                lines.append(f"  - {item}")
        elif isinstance(v, bool):
            lines.append(f"{k}: {'true' if v else 'false'}")
        elif v is None:
            continue
        else:
            s = str(v)
            if any(ch in s for ch in ":#") or s != s.strip():
                s = '"' + s.replace('"', '\\"') + '"'
            lines.append(f"{k}: {s}")
    lines.append("---")
    return "\n".join(lines) + "\n"
