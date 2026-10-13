"""Generate Codex roles from shared Markdown; preserve unrelated project settings."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def role_source(path):
    _, front, body = path.read_text().split("---", 2)
    metadata = {}
    for key in ("name", "description", "effort"):
        match = re.search(r"^" + key + r": (.+)$", front, re.M)
        if not match:
            raise ValueError(f"Missing {key}: {path}")
        metadata[key] = match[1]
    skills=re.search(r"(?m)^skills:\n((?:  - .+\n)+)",front)
    metadata["skills"]=re.findall(r"  - (.+)",skills[1]) if skills else []
    return metadata, body.strip()


def expected_role(path):
    metadata, body = role_source(path)
    instructions = "Role: " + metadata["name"] + ". Follow AGENTS.md and use only the capabilities needed for the task.\n\n" + body
    if metadata["skills"]:
        instructions += "\n\nInitial capability: " + ", ".join("harness/skills/"+s+"/SKILL.md" for s in metadata["skills"]) + ". Read only these entrypoints initially; supporting references load on demand."
    return (f"# Generated from harness/agents/{path.name}. Edit the source.\n"
            f'model_reasoning_effort = {json.dumps(metadata["effort"])}\n'
            'sandbox_mode = "workspace-write"\n'
            f'developer_instructions = {json.dumps(instructions)}\n')


def expected_config(current):
    entries = ['# Role configurations are maintained under harness/agents/codex/.',
               '[features]', 'multi_agent = true', '']
    for path in sorted((ROOT / "harness/agents").glob("*.md")):
        meta, _ = role_source(path)
        entries.extend([f'[agents.{meta["name"].replace("-", "_")}]',
                        f'description = {json.dumps(meta["description"])}',
                        f'config_file = "../harness/agents/codex/{path.stem}.toml"', ''])
    block = '# >>> fh-managed >>>\n' + '\n'.join(entries) + '# <<< fh-managed <<<'
    pattern = r"# >>> fh-managed >>>.*?# <<< fh-managed <<<"
    if re.search(pattern, current, re.S):
        return re.sub(pattern, lambda _: block, current, flags=re.S)
    return current.rstrip() + '\n\n' + block + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--config", action="store_true", help="Also synchronize the managed .codex/config.toml block.")
    args = parser.parse_args()
    changed = []
    for path in sorted((ROOT / "harness/agents").glob("*.md")):
        target = ROOT / "harness/agents/codex" / (path.stem + ".toml")
        expected = expected_role(path)
        if not target.exists() or target.read_text() != expected:
            changed.append(str(target.relative_to(ROOT)))
            if args.write: target.write_text(expected)
    if args.config:
        path = ROOT / ".codex/config.toml"
        expected = expected_config(path.read_text())
        if path.read_text() != expected:
            changed.append(".codex/config.toml")
            if args.write: path.write_text(expected)
    print(json.dumps({"mode": "write" if args.write else "check", "changed": changed}, indent=2))
    if changed and not args.write: raise SystemExit(1)


if __name__ == "__main__":
    main()
