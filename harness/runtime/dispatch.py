"""Explicit capability routing; packets contain pointers rather than source dumps."""
import json
import hashlib
from pathlib import Path

HARNESS = Path(__file__).resolve().parents[1]


def route(capability):
    catalog = json.loads((HARNESS / "orchestration/routes.json").read_text())
    if capability not in catalog:
        raise ValueError("Unknown capability: " + capability)
    return catalog[capability]


def context_fingerprints(task):
    """Capability instructions are inputs too, even outside a project workspace."""
    selected = route(task.get("capability", "implementation"))
    paths = [HARNESS / "agents" / (selected["role"] + ".md")]
    paths += [HARNESS / "skills" / s / "SKILL.md" for s in dict.fromkeys(selected["skills"] + task["skills"])]
    if any(not p.is_file() for p in paths):
        raise ValueError("Missing role or skill entrypoint in the selected capability.")
    result = {str(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    result["selected_route"] = hashlib.sha256(json.dumps(selected, sort_keys=True).encode()).hexdigest()
    return result


def make_packet(task, signature, token, root):
    selected = route(task.get("capability", "implementation"))
    skills = list(dict.fromkeys(selected["skills"] + task["skills"]))
    if len(skills) > 3:
        raise ValueError("Split this handoff; initial context needs more than three skills.")
    for skill in skills:
        if not (HARNESS / "skills" / skill / "SKILL.md").is_file():
            raise ValueError("Unknown skill: " + skill)
    packet = {"task": task["id"], "attempt_token": token, "input_signature": signature,
            "workspace": str(root), "role": selected["role"],
            "role_path": str(HARNESS / "agents" / (selected["role"] + ".md")),
            "skill_paths": [str(HARNESS / "skills" / s / "SKILL.md") for s in skills],
            "instruction": task["instruction"], "context": task.get("context", ""),
            "inputs": task["inputs"], "read_on_demand": task["references"],
            "owns_outputs": task["outputs"], "checks": task["checks"],
            "return_contract": {"artifacts": "paths actually produced", "checks": "actual commands and outcomes",
                                "evidence": "source/result pointers; distinguish inference and open claims",
                                "unresolved": "missing inputs, conflicts, or failed checks"},
            "coordination": "You are not alone in this workspace. Own only the declared outputs; preserve others' edits.",
            "host_instruction": "Use an available native agent tool only when authorized. Prefer fresh task context; do not copy the full parent conversation. One agent can execute serially. This packet does not spawn an agent or authorize external actions."}
    if len(json.dumps(packet,ensure_ascii=False))>32000:
        raise ValueError("Split the task: the complete dispatch packet exceeds 32,000 characters.")
    return packet
