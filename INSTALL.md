# Install, update and uninstall from a terminal

Requirements: macOS, Linux or WSL; Bash, Git, Python 3.9+ and symlink support. The downloaded bootstrap also uses curl. No Python packages, model API key, administrator access or running coordination service are required.

## Global installation

Download the bootstrap and run it:

```bash
curl -fsSLo /tmp/econfinharness-install.sh https://raw.githubusercontent.com/Si1entPe661e/EconFinHarness/main/install.sh
bash /tmp/econfinharness-install.sh install
```

The equivalent one-line bootstrap is:

```bash
curl -fsSL https://raw.githubusercontent.com/Si1entPe661e/EconFinHarness/main/install.sh | bash -s -- install
```

By default the installer clones `main` to `~/.local/share/econfinharness`, links skills into `~/.agents/skills` for Codex and `~/.claude/skills` for Claude Code, links Claude roles into `~/.claude/agents`, and installs `~/.local/bin/econfinharness`. It leaves global Codex settings, `AGENTS.md`, `CLAUDE.md` and shell startup files untouched. Codex named-role configurations remain project scoped.

All EconFinHarness skill names end in `-efh`, for example `did-efh` and `project-status-efh`. Other projects can keep their own `did` or `project-status` skills.

If `~/.local/bin` is not on your command search path, enable it for the current terminal:

```bash
export PATH="$HOME/.local/bin:$PATH"
econfinharness status
```

You can also invoke `~/.local/bin/econfinharness` directly. The script prints the actual checkout and command paths. Open a new Codex or Claude Code session after installation or updates. For resources named `harness/...` in a guide, use the installed checkout as the resource root; keep analysis inputs and outputs in your working project.

Host discovery locations follow [official Codex guidance](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills) and [Claude Code skill documentation](https://code.claude.com/docs/en/skills). Global installation registers filesystem skills and Claude roles; it does not install a plugin or launch an agent.

## Update and inspect

```bash
econfinharness update
econfinharness status
```

`update` fetches the recorded branch and uses Git's fast-forward merge with ignored-file protection. It refuses a dirty checkout, untracked files, an unexpected branch or origin, or local commits ahead of or diverging from the remote. It never resets, rebases, stashes, force-pulls or deletes local work. Network failure leaves the installed revision intact. New skills are checked for host-path conflicts before the checkout changes; removed skills lose only their installer-owned obsolete symlinks.

`status` prints JSON with the installed version, commit, branch, target scopes, local-change status, skipped entries and missing or changed links. A missing link gives a nonzero exit code. Running `install` again with the same prefix repairs missing links. Installation records live inside the checkout's Git metadata, so they do not dirty the repository. Concurrent installers for a prefix are rejected.

Updating a pre-0.5.0 installation replaces this project's unqualified skill links with the new `-efh` links. An `install` against an already updated checkout also recognizes legacy manual links pointing to that exact checkout, even without an installation record. It removes only retired skill symlinks owned by that checkout; another project's files or links at the old names and historical local records remain intact. No generic skill aliases are published.

Installations made before the installer moved to the repository root link their command to `harness/maintenance/install.py`, which no longer exists, so their `econfinharness update` stops without changing files. Update them once through the bootstrap, adding `--prefix` for a custom location:

```bash
curl -fsSL https://raw.githubusercontent.com/Si1entPe661e/EconFinHarness/main/install.sh | bash -s -- update
```

This fast-forwards the checkout and retargets the command to the root `install.py`.

## Uninstall

```bash
econfinharness uninstall
econfinharness uninstall --tool codex
econfinharness uninstall --project /path/to/existing/project
econfinharness uninstall --remove-checkout
```

`uninstall` removes the host links and the `econfinharness` command that this checkout installed. It removes a link only while it still points to the file or directory the installer linked, so replaced entries and other projects' skills stay. `--tool` removes one host and `--project` one project installation; the command stays while any installation remains. The managed checkout is kept unless you add `--remove-checkout`, which requires removing every host and project and refuses a checkout with local changes, untracked files or commits not on the remote. Pass `--prefix` for a custom location when running a separately downloaded script.

## Options and existing files

Run from a clone, or pass the same options to the downloaded bootstrap:

```bash
# Only one host; default is both.
bash install.sh install --tool codex
bash install.sh install --tool claude

# Keep existing skills or host files; report skipped entries explicitly.
bash install.sh install --skip-existing

# Customize the shared checkout and command locations.
bash install.sh install --prefix ~/opt/econfinharness --bin-dir ~/bin
~/bin/econfinharness update

# Use only this project's skills and roles, backed by the same shared checkout.
bash install.sh install --project /path/to/existing/project
```

Existing files and conflicting symlinks are never overwritten. By default, a conflict stops before host links are written. `--skip-existing` preserves those entries and records the choice for subsequent updates. Previously installed hosts remain registered when you add another host. A skipped command path means you should invoke `python3 /path/to/checkout/install.py update --prefix /path/to/checkout` directly.

Project installation links `harness/`, individual host skills, Claude roles and `.codex/config.toml`. Existing project instructions and unrelated skills remain intact. An existing Codex configuration can be skipped, leaving named roles under the user's configuration; the installer does not merge TOML or enable features in existing settings. A conflicting project `harness/` directory cannot be skipped because installed role and guide paths depend on that resource root; use global installation instead.

`--repo` and `--branch` on `install` select a fork or a branch. An existing installation's origin and branch must match; use a separate prefix to switch sources. The command installed in a custom prefix remembers its checkout through its symlink target. When using a separately downloaded script for updates, pass `--prefix` for a nondefault installation.
