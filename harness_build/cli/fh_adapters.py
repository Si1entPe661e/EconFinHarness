"""Copy source roles and skills to Claude Code and Codex without rebuilding research materials."""
import argparse
import json
import pathlib
import re
import sys

import fh_common as C

BEGIN = "# >>> fh-managed (harness_build/cli/fh_adapters.py) >>>"
END = "# <<< fh-managed <<<"

def role_sources():
    roles = {}
    for directory in (C.AGENTS, C.BUILD / "agents"):
        for path in sorted(directory.glob("*.md")):
            fm, body = C.parse_frontmatter(path.read_text(encoding="utf-8"))
            if fm.get("name"):
                roles[fm["name"]] = {"path": path, "fm": fm, "body": body}
    return roles

def skill_sources():
    skills = {}
    for directory in (C.SKILLS, C.BUILD / "skills"):
        for path in sorted(directory.glob("*/SKILL.md")):
            skills[path.parent.name] = path.parent
    return skills

def header(path):
    return f"<!-- Generated from {C.rel(path)} by fh sync-adapters. Edit the source. -->\n\n"

def claude_role(source):
    fm = source["fm"]
    selected = {k: fm[k] for k in ("name", "description", "tools", "model", "effort") if fm.get(k)}
    if fm.get("skills"):
        selected["skills"] = fm["skills"] if isinstance(fm["skills"], list) else [s.strip() for s in fm["skills"].split(",")]
    return C.dump_frontmatter(selected) + "\n" + header(source["path"]) + source["body"].lstrip()

def codex_role(name, source):
    fm = source["fm"]
    instructions = f"Role: {name}. Follow AGENTS.md; use existing research materials directly.\n\n" + source["body"].strip()
    lines = [f"# Generated from {C.rel(source['path'])}. Edit the source."]
    if fm.get("codex_model"):
        lines.append("model = " + json.dumps(fm["codex_model"]))
    if fm.get("effort"):
        lines.append("model_reasoning_effort = " + json.dumps(fm["effort"]))
    lines.extend(['sandbox_mode = "workspace-write"', 'developer_instructions = ' + json.dumps(instructions, ensure_ascii=False)])
    return "\n".join(lines) + "\n"

def config_block(roles, old):
    lines = [BEGIN, "# Generated role descriptions; edit source roles and sync again."]
    # Keep the feature setting previously owned by this generated block.
    match = re.search(r"(?m)^multi_agent\s*=\s*(true|false)\s*$", old)
    if match and not re.search(r"(?m)^\[features\]\s*$", unmanaged_config(old)):
        lines.extend(["[features]", f"multi_agent = {match.group(1)}"])
    for name, source in sorted(roles.items()):
        lines.extend(["", f"[agents.{name.replace('-', '_')}]",
                      "description = " + json.dumps(source["fm"].get("description", ""), ensure_ascii=False),
                      "config_file = " + json.dumps(f"agents/{name}.toml")])
    lines.extend(["", END])
    return "\n".join(lines) + "\n"

def unmanaged_config(old):
    pattern = re.compile(re.escape(BEGIN) + r"[\s\S]*?" + re.escape(END) + r"\n?")
    return pattern.sub("", old)

def merge_codex_config(old, block):
    pattern = re.compile(re.escape(BEGIN) + r"[\s\S]*?" + re.escape(END) + r"\n?")
    found = list(pattern.finditer(old))
    if not found:
        return old + ("\n" if old and not old.endswith("\n") else "") + block
    # Replace every historical managed block with one; preserve all other text.
    before = old[:found[0].start()]
    after = pattern.sub("", old[found[0].end():])
    return before + block + after

def outputs(hosts=("claude", "codex")):
    roles, skills = role_sources(), skill_sources()
    generated = {}
    for host in hosts:
        if host == "claude":
            for name, source in roles.items():
                generated[pathlib.Path(f".claude/agents/{name}.md")] = claude_role(source).encode()
        else:
            for name, source in roles.items():
                generated[pathlib.Path(f".codex/agents/{name}.toml")] = codex_role(name, source).encode()
            path = C.ROOT / ".codex/config.toml"
            old = path.read_text(encoding="utf-8") if path.exists() else ""
            generated[pathlib.Path(".codex/config.toml")] = merge_codex_config(old, config_block(roles, old)).encode()
        for name, directory in skills.items():
            target = pathlib.Path(".claude/skills" if host == "claude" else ".agents/skills") / name
            for source in sorted(directory.rglob("*")):
                relative = source.relative_to(directory)
                if not source.is_file() or any(part.startswith(".") for part in relative.parts):
                    continue
                # Historical bookkeeping and evidence metadata are read from their
                # source location; host instructions need just guides and templates.
                if relative.name in {"manifest.json", "evidence.json", "reported_evidence.json"}:
                    continue
                generated[target / relative] = source.read_bytes()
    return generated

def sync(hosts=("claude", "codex"), destination=None, quiet=False):
    base = pathlib.Path(destination) if destination else C.ROOT
    generated = outputs(hosts)
    for relative, data in generated.items():
        path = base / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or path.read_bytes() != data:
            path.write_bytes(data)
    # Retire unchanged copies of the old administrative templates. Keep any
    # user-edited template where it is, and preserve retired copies as history.
    old_templates = C.BUILD / "legacy/harness/skills"
    for host in hosts:
        folder = pathlib.Path(".claude/skills" if host == "claude" else ".agents/skills")
        for source in old_templates.glob("*/templates/*.json"):
            relative = folder / source.relative_to(old_templates)
            path = base / relative
            if relative in generated or not path.is_file() or path.read_bytes() != source.read_bytes():
                continue
            archived = base / "harness_build/legacy/host-copies" / relative
            if archived.exists() and archived.read_bytes() != path.read_bytes():
                continue
            archived.parent.mkdir(parents=True, exist_ok=True)
            path.rename(archived)
    if not quiet:
        print(f"Copied {len(generated)} role, skill and template files to {base}.")
    return 0

def main(argv=None):
    ap = argparse.ArgumentParser(prog="fh sync-adapters", description=__doc__)
    ap.add_argument("--host", choices=["claude", "codex", "all"], default="all")
    ap.add_argument("--output-dir", help="write a preview copy outside the live host folders")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args(argv)
    return sync(("claude", "codex") if a.host == "all" else (a.host,), a.output_dir, a.quiet)

if __name__ == "__main__":
    sys.exit(main() or 0)
