#!/usr/bin/env python3
"""Install, update and uninstall EconFinHarness with Git and the Python standard library."""
import argparse
import fcntl
import json
import os
import shutil
import subprocess
import sys
import tempfile
from contextlib import contextmanager
from pathlib import Path


REPOSITORY = "https://github.com/Si1entPe661e/EconFinHarness.git"
STATE_NAME = "econfinharness-install.json"
# Installations made before the installer moved to the repository root link the command here.
LEGACY_COMMAND_SOURCE = "harness/maintenance/install.py"


class InstallError(Exception):
    """An installation cannot proceed without changing user-owned work."""


def git(root, *args, check=True):
    command = ["git"] + (["-C", str(root)] if root else []) + list(args)
    result = subprocess.run(command, capture_output=True, text=True)
    if check and result.returncode:
        raise InstallError(result.stderr.strip() or result.stdout.strip() or "Git command failed.")
    return result


def repository_identity(url):
    # Accept GitHub's HTTPS and SSH spellings without changing Git credentials.
    value = url.removesuffix("/").removesuffix(".git")
    for prefix in ("https://github.com/", "ssh://git@github.com/", "git@github.com:"):
        if value.startswith(prefix):
            return "github.com/" + value[len(prefix):].lower()
    return value


def validate_checkout(root, repository, branch):
    if not (root / ".git").exists():
        raise InstallError(f"Not a Git checkout: {root}. Choose an empty --prefix directory.")
    actual = Path(git(root, "rev-parse", "--show-toplevel").stdout.strip()).resolve()
    if actual != root:
        raise InstallError(f"Installation prefix must be the checkout root: {actual}")
    origin = git(root, "remote", "get-url", "origin").stdout.strip()
    if repository_identity(origin) != repository_identity(repository):
        raise InstallError("Origin differs from the installed repository; refusing to update it.")
    current = git(root, "symbolic-ref", "--quiet", "--short", "HEAD", check=False)
    if current.returncode or current.stdout.strip() != branch:
        raise InstallError(f"Expected branch {branch!r}; switch branches yourself before updating.")
    if git(root, "status", "--porcelain", "--untracked-files=all").stdout:
        raise InstallError("Local changes or untracked files exist. Commit or move them before updating.")
    for relative in ("harness/VERSION", "harness/skills"):
        if not (root / relative).exists():
            raise InstallError(f"Missing installation source: {relative}")


def state_path(root):
    directory = Path(git(root, "rev-parse", "--absolute-git-dir").stdout.strip())
    return directory / STATE_NAME


def read_state(root):
    path = state_path(root)
    if not path.exists():
        raise InstallError(f"No installation record at {root}. Run install with this --prefix first.")
    state = json.loads(path.read_text())
    if state.get("schema") != 1:
        raise InstallError("Unsupported installation record version.")
    return state


def save_state(root, state):
    path = state_path(root)
    with tempfile.NamedTemporaryFile(mode="w", dir=path.parent, delete=False) as stream:
        temporary = Path(stream.name)
        json.dump(state, stream, indent=2)
        stream.write("\n")
    try:
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


@contextmanager
def installation_lock(root):
    root.parent.mkdir(parents=True, exist_ok=True)
    with (root.parent / ("." + root.name + ".install.lock")).open("a") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise InstallError("Another installation or update is running for this prefix.") from exc
        try:
            yield
        finally:
            fcntl.flock(lock, fcntl.LOCK_UN)


def clone(root, repository, branch):
    if root.is_symlink() or (root.exists() and (not root.is_dir() or any(root.iterdir()))):
        raise InstallError(f"Refusing to replace an existing path: {root}")
    with tempfile.TemporaryDirectory(prefix=".econfinharness-clone-", dir=root.parent) as temp:
        staged = Path(temp) / "checkout"
        git(None, "clone", "--single-branch", "--branch", branch, "--", repository, str(staged))
        validate_checkout(staged, repository, branch)
        # A failed download never leaves a partial installation at the final path.
        os.replace(staged, root)


def target_links(root, target, inventory=None):
    base = Path(target["base"])
    tools = target["tools"]
    links = {}
    paths = inventory if inventory is not None else [
        p.relative_to(root).as_posix() for pattern in ("harness/skills/*/SKILL.md", "harness/agents/*.md")
        for p in root.glob(pattern)]
    skills = [root / p for p in paths if len(Path(p).parts) == 4
              and p.startswith("harness/skills/") and p.endswith("/SKILL.md")]
    roles = [root / p for p in paths if len(Path(p).parts) == 3
             and p.startswith("harness/agents/") and p.endswith(".md")]
    for tool in tools:
        directory = base / (".agents/skills" if tool == "codex" else ".claude/skills")
        for skill in sorted(skills):
            links[directory / skill.parent.name] = skill.parent
        if tool == "claude":
            for role in sorted(roles):
                links[base / ".claude/agents" / role.name] = role
    if target["scope"] == "project":
        links[base / "harness"] = root / "harness"
        if "codex" in tools:
            links[base / ".codex/config.toml"] = root / ".codex/config.toml"
    return links


def legacy_command(root, path):
    return path.is_symlink() and path.resolve() == (root / LEGACY_COMMAND_SOURCE).resolve()


def link_plan(root, targets, bin_directory, skip_existing, inventory=None):
    command = Path(bin_directory) / "econfinharness"
    desired = {command: root / "install.py"}
    for target in targets:
        desired.update(target_links(root, target, inventory))
    required = {Path(t["base"]) / "harness" for t in targets if t["scope"] == "project"}
    accepted, skipped, conflicts = {}, [], []
    for destination, source in desired.items():
        if os.path.lexists(destination):
            if (destination.resolve() == source.resolve()
                    or (destination == command and legacy_command(root, destination))):
                accepted[destination] = source
                continue
            reason = f"Existing file or link: {destination}"
        elif any(parent.is_symlink() for parent in destination.parents):
            reason = f"Destination has a symlinked parent: {destination}"
        else:
            accepted[destination] = source
            continue
        if skip_existing and destination not in required:
            skipped.append(str(destination))
        else:
            conflicts.append(reason)
    if conflicts:
        raise InstallError("\n".join(conflicts) + "\nKeep these files, choose another scope, or use --skip-existing.")
    return accepted, skipped


def retired_skill_source(source):
    return (source.parent.name == "skills" and source.parent.parent.name == "harness"
            and not (source / "SKILL.md").is_file())


def legacy_skill_links(root, targets):
    """Recognize retired links from manual installations by their source checkout."""
    retired = {}
    for target in targets:
        for destination, source in target_links(root, target).items():
            if source.parent != root / "harness/skills" or not source.name.endswith("-efh"):
                continue
            previous_source = source.with_name(source.name.removesuffix("-efh"))
            previous_link = destination.with_name(previous_source.name)
            if (previous_link.is_symlink() and previous_link.resolve() == previous_source.resolve()
                    and retired_skill_source(previous_source)):
                retired[str(previous_link)] = str(previous_source)
    return retired


def apply_links(links, old_links, root):
    created, replaced = [], []
    try:
        for destination, source in links.items():
            if os.path.lexists(destination):
                if destination.resolve() == source.resolve():
                    continue
                if not (destination.name == "econfinharness" and legacy_command(root, destination)):
                    raise InstallError(f"Destination changed during installation: {destination}")
                replaced.append((destination, os.readlink(destination)))
                destination.unlink()
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.symlink_to(source, target_is_directory=source.is_dir())
            created.append(destination)
    except BaseException:
        for destination in reversed(created):
            destination.unlink()
        for destination, previous in replaced:
            destination.symlink_to(previous)
        raise
    # Only obsolete symlinks whose resolved target is still ours may be removed.
    for destination, source in old_links.items():
        path = Path(destination)
        if path not in links and path.is_symlink() and path.resolve() == Path(source).resolve():
            if not Path(source).exists() or retired_skill_source(Path(source)):
                path.unlink()


def install(root, repository, branch, user_directory, bin_directory, tools, project, skip_existing):
    with installation_lock(root):
        if not (root / ".git").exists():
            clone(root, repository, branch)
        validate_checkout(root, repository, branch)
        if not (root / "install.py").is_file():
            raise InstallError("This checkout predates the root installer. Run 'bash install.sh update' first.")
        state = read_state(root) if state_path(root).exists() else {
            "schema": 1, "repository": repository, "branch": branch, "targets": [], "links": {}}
        target = {"scope": "project" if project else "user",
                  "base": str(project or user_directory), "tools": tools}
        previous = next((t for t in state["targets"]
                         if (t["scope"], t["base"]) == (target["scope"], target["base"])), None)
        target["tools"] = sorted(set(tools) | set(previous["tools"] if previous else []))
        targets = [t for t in state["targets"] if (t["scope"], t["base"]) != (target["scope"], target["base"])]
        targets.append(target)
        policy = skip_existing or state.get("skip_existing", False)
        links, skipped = link_plan(root, targets, bin_directory, policy)
        previous_links = {**state["links"], **legacy_skill_links(root, targets)}
        apply_links(links, previous_links, root)
        state.update(targets=targets, bin_directory=str(bin_directory), skip_existing=policy,
                     links={str(p): str(s) for p, s in links.items()}, skipped=skipped)
        save_state(root, state)
        return describe(root, state)


def update(root, skip_existing):
    with installation_lock(root):
        state = read_state(root)
        validate_checkout(root, state["repository"], state["branch"])
        git(root, "fetch", "--no-tags", "origin", state["branch"])
        revision = git(root, "rev-parse", "FETCH_HEAD^{commit}").stdout.strip()
        if git(root, "merge-base", "--is-ancestor", "HEAD", revision, check=False).returncode:
            raise InstallError("Local commits are ahead of or diverge from the remote. No checkout files changed.")
        previous = git(root, "rev-parse", "HEAD").stdout.strip()
        inventory = git(root, "ls-tree", "-r", "--name-only", revision).stdout.splitlines()
        required_paths = ["harness/VERSION", "install.py"]
        if any(t["scope"] == "project" and "codex" in t["tools"] for t in state["targets"]):
            required_paths.append(".codex/config.toml")
        for required in required_paths:
            if required not in inventory:
                raise InstallError(f"Incoming revision is missing {required}; no checkout files changed.")
        # Inspect the incoming tree before changing the checkout or live skill links.
        links, skipped = link_plan(root, state["targets"], state["bin_directory"],
                                   skip_existing or state.get("skip_existing", False), inventory)
        # Git also protects ignored local files when an upstream file collides.
        git(root, "-c", "merge.autostash=false", "merge", "--ff-only", "--no-overwrite-ignore", revision)
        previous_links = {**state["links"], **legacy_skill_links(root, state["targets"])}
        apply_links(links, previous_links, root)
        state.update(links={str(p): str(s) for p, s in links.items()}, skipped=skipped,
                     skip_existing=skip_existing or state.get("skip_existing", False))
        save_state(root, state)
        result = describe(root, state)
        result["updated"] = previous != revision
        return result


def uninstall(root, project, tools, remove_checkout):
    with installation_lock(root):
        state = read_state(root)

        def selected(target):
            return project is None or (target["scope"], target["base"]) == ("project", str(project))

        if project is not None and not any(selected(t) for t in state["targets"]):
            raise InstallError(f"No installation record for project {project}.")
        targets = [{**t, "tools": [tool for tool in t["tools"] if not selected(t) or tool not in tools]}
                   for t in state["targets"]]
        targets = [t for t in targets if t["tools"]]
        if remove_checkout:
            if targets:
                raise InstallError("--remove-checkout needs every host and project removed. Nothing was changed.")
            if git(root, "status", "--porcelain", "--untracked-files=all").stdout:
                raise InstallError("Local changes or untracked files exist. Nothing was changed.")
            ahead = git(root, "rev-list", "--count", "@{upstream}..HEAD", check=False)
            if ahead.returncode or ahead.stdout.strip() != "0":
                raise InstallError("Local commits are not on the remote. Nothing was changed.")
        command = Path(state["bin_directory"]) / "econfinharness"
        keep = {command: root / "install.py"} if targets else {}
        for target in targets:
            keep.update(target_links(root, target))
        removed = []
        for destination, source in {**state["links"], **legacy_skill_links(root, state["targets"])}.items():
            path = Path(destination)
            # Only symlinks that still point to what this checkout installed are removed.
            if path not in keep and path.is_symlink() and path.resolve() == Path(source).resolve():
                path.unlink()
                removed.append(destination)
        if targets:
            state.update(targets=targets, links={p: s for p, s in state["links"].items() if Path(p) in keep})
            save_state(root, state)
        else:
            state_path(root).unlink()
        if remove_checkout:
            shutil.rmtree(root)
        return {"prefix": str(root), "removed_links": removed, "targets": targets,
                "checkout_removed": remove_checkout, "command": str(command) if targets else None}


def describe(root, state):
    missing = [p for p, source in state["links"].items()
               if not Path(p).exists() or Path(p).resolve() != Path(source).resolve()]
    return {"prefix": str(root), "version": (root / "harness/VERSION").read_text().strip(),
            "commit": git(root, "rev-parse", "HEAD").stdout.strip(),
            "branch": git(root, "branch", "--show-current").stdout.strip(),
            "clean": not bool(git(root, "status", "--porcelain", "--untracked-files=all").stdout),
            "targets": state["targets"], "linked_paths": len(state["links"]),
            "missing_or_changed_links": missing, "skipped": state.get("skipped", []),
            "command": str(Path(state["bin_directory"]) / "econfinharness")}


def main(argv=None, user_directory=None):
    user_directory = Path(user_directory or Path.home()).resolve()
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for action in ("install", "update", "status", "uninstall"):
        command = subparsers.add_parser(action)
        command.add_argument("--prefix", type=Path, help="Managed checkout directory.")
        if action in ("install", "update"):
            command.add_argument("--skip-existing", action="store_true", help="Leave conflicting host files untouched.")
        if action == "install":
            command.add_argument("--repo", default=REPOSITORY, help="Git repository URL; defaults to the public GitHub repository.")
            command.add_argument("--branch", default="main")
            command.add_argument("--bin-dir", type=Path, help="Command directory; defaults to ~/.local/bin.")
        if action in ("install", "uninstall"):
            command.add_argument("--tool", choices=("codex", "claude", "both"), default="both")
            command.add_argument("--project", type=Path, help=(
                "Install for this project instead of all user projects." if action == "install"
                else "Remove only this project's installation."))
        if action == "uninstall":
            command.add_argument("--remove-checkout", action="store_true",
                                 help="Also delete the managed checkout when it has no local changes or commits.")
    args = parser.parse_args(argv)
    if not shutil.which("git"):
        parser.error("Git is required. Install it before running this script.")
    default = user_directory / ".local/share/econfinharness"
    local = Path(__file__).resolve().parent
    if (local / ".git").exists() and (local / "harness/VERSION").is_file():
        if args.command != "install" or state_path(local).exists():
            default = local
    root = (args.prefix or default).expanduser().absolute()
    if root.is_symlink():
        parser.error("The installation prefix must not be a symlink.")
    root = root.resolve()
    try:
        if args.command in ("install", "uninstall"):
            tools = ["codex", "claude"] if args.tool == "both" else [args.tool]
            project = args.project.expanduser().resolve() if args.project else None
        if args.command == "install":
            if args.branch.startswith("-"):
                raise InstallError("Branch names must not start with '-'.")
            if project and not project.is_dir():
                raise InstallError("--project must name an existing project directory.")
            bin_directory = (args.bin_dir or user_directory / ".local/bin").expanduser().absolute()
            result = install(root, args.repo, args.branch, user_directory, bin_directory,
                             tools, project, args.skip_existing)
        elif args.command == "update":
            result = update(root, args.skip_existing)
        elif args.command == "uninstall":
            result = uninstall(root, project, tools, args.remove_checkout)
        else:
            result = describe(root, read_state(root))
        print(json.dumps(result, indent=2))
        if args.command in ("install", "update"):
            print("Open a new Codex or Claude Code session to discover installed skills.")
            print("If the command is not on PATH, run it using the full 'command' path above.")
        elif args.command == "uninstall":
            print("Open a new Codex or Claude Code session so hosts stop listing removed skills.")
        return 0 if not result.get("missing_or_changed_links") else 1
    except (InstallError, OSError, ValueError) as exc:
        print(f"econfinharness: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
