"""Offline installer checks using actual Git repositories and isolated user roots."""
import contextlib
import importlib.util
import io
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("harness_install", ROOT / "harness/maintenance/install.py")
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)


class InstallerChecks(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="econfinharness-check-")
        self.base = Path(self.temporary.name).resolve()
        self.origin = self.base / "upstream repository"
        self.origin.mkdir()
        self.user = self.base / "isolated user"
        self.user.mkdir()
        self.prefix = self.user / ".local/share/econfinharness"
        self.bin = self.user / ".local/bin"
        self.write("harness/VERSION", "1.0.0\n")
        self.write("README.md", "Fixture project\n")
        self.write(".gitignore", "local.txt\n")
        self.write("harness/skills/example/SKILL.md", "---\nname: example\ndescription: Fixture\n---\n")
        self.write("harness/agents/reviewer.md", "Fixture reviewer\n")
        self.write("harness/orchestration/README.md", "Shared guidance\n")
        self.write(".codex/config.toml", '[agents.reviewer]\nconfig_file = "../harness/agents/codex/reviewer.toml"\n')
        source = self.origin / "harness/maintenance/install.py"
        source.parent.mkdir(parents=True)
        shutil.copy2(ROOT / "harness/maintenance/install.py", source)
        source.chmod(0o755)
        self.git(self.origin, "init", "-b", "main")
        self.git(self.origin, "config", "user.name", "Installer Check")
        self.git(self.origin, "config", "user.email", "installer-check@example.invalid")
        self.commit("Initial fixture")

    def tearDown(self):
        self.temporary.cleanup()

    def git(self, root, *args):
        result = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout.strip()

    def write(self, relative, text):
        path = self.origin / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)

    def commit(self, message):
        self.git(self.origin, "add", "--all")
        self.git(self.origin, "commit", "-m", message)

    def cli(self, *args):
        out, error = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(error):
            code = installer.main([*args, "--prefix", str(self.prefix)], user_directory=self.user)
        return code, out.getvalue(), error.getvalue()

    def install(self, *args):
        result = self.cli("install", "--repo", str(self.origin), *args)
        self.assertEqual(result[0], 0, result[2])
        return result

    def head(self):
        return self.git(self.prefix, "rev-parse", "HEAD")

    def test_global_install_and_executable_command_from_another_directory(self):
        self.install()
        for relative in (".agents/skills/example", ".claude/skills/example", ".claude/agents/reviewer.md"):
            self.assertTrue((self.user / relative).is_symlink(), relative)
        self.assertFalse((self.user / ".codex/config.toml").exists())
        self.assertEqual((self.user / ".agents/skills/example/../../orchestration/README.md").read_text(),
                         "Shared guidance\n")
        command = subprocess.run([str(self.bin / "econfinharness"), "status"], cwd=self.base,
                                 capture_output=True, text=True)
        self.assertEqual(command.returncode, 0, command.stderr)
        self.assertEqual(json.loads(command.stdout)["version"], "1.0.0")
        self.assertTrue(json.loads(command.stdout)["clean"])

    def test_project_install_preserves_project_instructions_and_other_skills(self):
        project = self.base / "research project"
        project.mkdir()
        (project / "AGENTS.md").write_text("User rules\n")
        other = project / ".agents/skills/other/SKILL.md"
        other.parent.mkdir(parents=True)
        other.write_text("User skill\n")
        self.install("--project", str(project), "--tool", "codex")
        self.assertTrue((project / "harness").is_symlink())
        self.assertTrue((project / ".codex/config.toml").is_symlink())
        self.assertEqual((project / "AGENTS.md").read_text(), "User rules\n")
        self.assertEqual(other.read_text(), "User skill\n")
        self.assertFalse((self.user / ".agents").exists())
        self.assertFalse((project / ".claude").exists())

    def test_repeated_install_and_update_are_idempotent(self):
        self.install()
        state = installer.read_state(self.prefix)
        self.install()
        self.assertEqual(installer.read_state(self.prefix), state)
        result = self.cli("update")
        self.assertEqual(result[0], 0, result[2])
        self.assertFalse(json.JSONDecoder().raw_decode(result[1])[0]["updated"])

    def test_collision_preflight_never_overwrites_host_files(self):
        existing = self.user / ".claude/skills/example"
        existing.mkdir(parents=True)
        (existing / "SKILL.md").write_text("Personal version\n")
        result = self.cli("install", "--repo", str(self.origin))
        self.assertEqual(result[0], 1)
        self.assertIn("Existing file or link", result[2])
        self.assertFalse((self.user / ".agents").exists())
        self.assertFalse((self.bin / "econfinharness").exists())
        self.assertEqual((existing / "SKILL.md").read_text(), "Personal version\n")

    def test_skip_existing_policy_survives_update(self):
        existing = self.user / ".claude/skills/example"
        existing.mkdir(parents=True)
        self.install("--skip-existing")
        (self.user / ".agents/skills/example").unlink()
        self.install()
        self.assertTrue((self.user / ".agents/skills/example").is_symlink())
        self.write("harness/VERSION", "1.0.1\n")
        self.commit("Update fixture")
        result = self.cli("update")
        self.assertEqual(result[0], 0, result[2])
        self.assertFalse(existing.is_symlink())
        self.assertIn(str(existing), installer.read_state(self.prefix)["skipped"])

    def test_installing_another_host_keeps_previously_registered_hosts(self):
        self.install("--tool", "codex")
        self.install("--tool", "claude")
        self.assertEqual(installer.read_state(self.prefix)["targets"][0]["tools"], ["claude", "codex"])
        self.assertTrue((self.user / ".agents/skills/example").is_symlink())
        self.assertTrue((self.user / ".claude/skills/example").is_symlink())

    def test_installed_command_retains_custom_prefix_during_reinstall(self):
        self.install()
        other_user = self.base / "another-isolated-user"
        out, error = io.StringIO(), io.StringIO()
        with patch.object(installer, "__file__", str(self.prefix / "harness/maintenance/install.py")):
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(error):
                code = installer.main(["install", "--repo", str(self.origin)], user_directory=other_user)
        self.assertEqual(code, 0, error.getvalue())
        self.assertEqual(json.JSONDecoder().raw_decode(out.getvalue())[0]["prefix"], str(self.prefix))
        self.assertFalse((other_user / ".local/share/econfinharness").exists())

    def test_fast_forward_refreshes_added_and_removed_skills(self):
        self.install()
        shutil.rmtree(self.origin / "harness/skills/example")
        self.write("harness/skills/new-skill/SKILL.md", "New skill\n")
        self.write("harness/VERSION", "1.1.0\n")
        self.commit("Replace fixture skill")
        result = self.cli("update")
        self.assertEqual(result[0], 0, result[2])
        self.assertEqual(self.head(), self.git(self.origin, "rev-parse", "HEAD"))
        for relative in (".agents/skills", ".claude/skills"):
            self.assertFalse((self.user / relative / "example").is_symlink())
            self.assertTrue((self.user / relative / "new-skill").is_symlink())

    def rename_fixture_skill(self):
        (self.origin / "harness/skills/example").rename(self.origin / "harness/skills/example-efh")
        self.write("harness/skills/example-efh/SKILL.md", "---\nname: example-efh\ndescription: Fixture\n---\n")
        self.commit("Namespace fixture skill")

    def test_namespace_upgrade_retires_owned_links_and_preserves_other_projects_skills(self):
        personal = self.user / ".agents/skills/example"
        personal.mkdir(parents=True)
        (personal / "SKILL.md").write_text("Another project's skill\n")
        self.install("--skip-existing")
        self.rename_fixture_skill()
        result = self.cli("update")
        self.assertEqual(result[0], 0, result[2])
        for relative in (".agents/skills", ".claude/skills"):
            self.assertTrue((self.user / relative / "example-efh").is_symlink())
        self.assertFalse((self.user / ".claude/skills/example").is_symlink())
        self.assertEqual((personal / "SKILL.md").read_text(), "Another project's skill\n")

    def test_install_migrates_legacy_links_without_a_registry_and_preserves_local_records(self):
        self.install()
        installer.state_path(self.prefix).unlink()
        self.rename_fixture_skill()
        self.git(self.prefix, "fetch", "origin", "main")
        self.git(self.prefix, "merge", "--ff-only", "FETCH_HEAD")
        record = self.prefix / "harness/skills/example/manifest.json"
        record.parent.mkdir(parents=True)
        record.write_text('{"historical": true}\n')
        with (self.prefix / ".git/info/exclude").open("a") as stream:
            stream.write("\nharness/skills/example/manifest.json\n")
        self.install()
        for relative in (".agents/skills", ".claude/skills"):
            self.assertFalse((self.user / relative / "example").is_symlink())
            self.assertTrue((self.user / relative / "example-efh").is_symlink())
        self.assertEqual(record.read_text(), '{"historical": true}\n')

    def test_legacy_migration_preserves_an_unrelated_symlink_at_the_old_name(self):
        self.install()
        installer.state_path(self.prefix).unlink()
        personal = self.base / "other-project-skill"
        personal.mkdir()
        old = self.user / ".agents/skills/example"
        old.unlink()
        old.symlink_to(personal)
        self.rename_fixture_skill()
        self.git(self.prefix, "fetch", "origin", "main")
        self.git(self.prefix, "merge", "--ff-only", "FETCH_HEAD")
        self.install()
        self.assertEqual(old.resolve(), personal)
        self.assertTrue((self.user / ".agents/skills/example-efh").is_symlink())

    def test_new_skill_collision_is_detected_before_checkout_changes(self):
        self.install()
        previous = self.head()
        personal = self.user / ".agents/skills/new-skill"
        personal.mkdir()
        self.write("harness/skills/new-skill/SKILL.md", "Remote skill\n")
        self.commit("Add colliding skill")
        result = self.cli("update")
        self.assertEqual(result[0], 1)
        self.assertIn("Existing file or link", result[2])
        self.assertEqual(self.head(), previous)
        self.assertFalse(personal.is_symlink())

    def test_dirty_and_untracked_checkout_files_prevent_updates(self):
        self.install()
        previous = self.head()
        for relative in ("README.md", "new-local-file.txt"):
            with self.subTest(relative=relative):
                path = self.prefix / relative
                original = path.read_bytes() if path.exists() else None
                path.write_text("Local work\n")
                result = self.cli("update")
                self.assertEqual(result[0], 1)
                self.assertIn("Local changes", result[2])
                self.assertEqual(path.read_text(), "Local work\n")
                self.assertEqual(self.head(), previous)
                if original is None:
                    path.unlink()
                else:
                    path.write_bytes(original)

    def test_local_commits_cannot_be_rebased_or_reset_by_update(self):
        self.install()
        self.git(self.prefix, "config", "user.name", "Local Check")
        self.git(self.prefix, "config", "user.email", "local@example.invalid")
        (self.prefix / "README.md").write_text("Committed local work\n")
        self.git(self.prefix, "commit", "-am", "Local change")
        previous = self.head()
        result = self.cli("update")
        self.assertEqual(result[0], 1)
        self.assertIn("ahead of or diverge", result[2])
        self.assertEqual(self.head(), previous)

    def test_ignored_local_files_are_not_overwritten_by_upstream(self):
        self.install()
        previous = self.head()
        path = self.prefix / "local.txt"
        path.write_text("Private local input\n")
        self.write("local.txt", "Upstream file\n")
        self.git(self.origin, "add", "--force", "local.txt")
        self.git(self.origin, "commit", "-m", "Add previously ignored path")
        result = self.cli("update")
        self.assertEqual(result[0], 1)
        self.assertEqual(path.read_text(), "Private local input\n")
        self.assertEqual(self.head(), previous)

    def test_changed_origin_or_branch_refuses_update(self):
        self.install()
        previous = self.head()
        self.git(self.prefix, "remote", "set-url", "origin", str(self.base / "different"))
        self.assertIn("Origin differs", self.cli("update")[2])
        self.git(self.prefix, "remote", "set-url", "origin", str(self.origin))
        self.git(self.prefix, "checkout", "-b", "local-work")
        self.assertIn("Expected branch", self.cli("update")[2])
        self.assertEqual(self.head(), previous)

    def test_failed_fetch_preserves_installed_revision(self):
        self.install()
        previous = self.head()
        self.origin.rename(self.base / "offline")
        result = self.cli("update")
        self.assertEqual(result[0], 1)
        self.assertEqual(self.head(), previous)

    def test_failed_clone_leaves_no_partial_checkout_or_host_links(self):
        result = self.cli("install", "--repo", str(self.base / "missing"))
        self.assertEqual(result[0], 1)
        self.assertFalse(self.prefix.exists())
        self.assertFalse((self.user / ".agents").exists())

    def test_existing_non_repository_prefix_is_preserved(self):
        self.prefix.mkdir(parents=True)
        important = self.prefix / "important.txt"
        important.write_text("Keep me\n")
        result = self.cli("install", "--repo", str(self.origin))
        self.assertEqual(result[0], 1)
        self.assertEqual(important.read_text(), "Keep me\n")

    def test_symlinked_host_parent_is_not_used_to_modify_another_directory(self):
        outside = self.base / "outside"
        outside.mkdir()
        (self.user / ".agents").mkdir()
        (self.user / ".agents/skills").symlink_to(outside)
        result = self.cli("install", "--repo", str(self.origin))
        self.assertEqual(result[0], 1)
        self.assertIn("symlinked parent", result[2])
        self.assertEqual(list(outside.iterdir()), [])

    def test_project_config_collision_is_preserved(self):
        project = self.base / "project"
        (project / ".codex").mkdir(parents=True)
        config = project / ".codex/config.toml"
        config.write_text('model = "personal-choice"\n')
        result = self.cli("install", "--repo", str(self.origin), "--project", str(project))
        self.assertEqual(result[0], 1)
        self.assertFalse((project / "harness").exists())
        self.assertEqual(config.read_text(), 'model = "personal-choice"\n')

    def test_project_resource_root_collision_cannot_be_skipped(self):
        project = self.base / "project"
        (project / "harness").mkdir(parents=True)
        (project / "harness/user.txt").write_text("User resources\n")
        result = self.cli("install", "--repo", str(self.origin), "--project", str(project), "--skip-existing")
        self.assertEqual(result[0], 1)
        self.assertFalse((project / ".codex").exists())
        self.assertEqual((project / "harness/user.txt").read_text(), "User resources\n")

    def test_project_config_can_be_skipped_without_changing_user_settings(self):
        project = self.base / "project"
        (project / ".codex").mkdir(parents=True)
        config = project / ".codex/config.toml"
        config.write_text('model = "personal-choice"\n')
        self.install("--project", str(project), "--skip-existing")
        self.assertTrue((project / ".agents/skills/example").is_symlink())
        self.assertEqual(config.read_text(), 'model = "personal-choice"\n')
        self.assertIn(str(config), installer.read_state(self.prefix)["skipped"])

    def test_missing_links_are_reported_and_install_can_repair_them(self):
        self.install()
        (self.user / ".agents/skills/example").unlink()
        result = self.cli("status")
        self.assertEqual(result[0], 1)
        self.assertTrue(json.loads(result[1])["missing_or_changed_links"])
        self.install()
        self.assertEqual(self.cli("status")[0], 0)

    def test_bootstrap_uses_local_copy_and_propagates_cli_errors(self):
        result = subprocess.run(["bash", str(ROOT / "install.sh"), "--help"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("install,update,status", result.stdout)
        failed = subprocess.run(["bash", str(ROOT / "install.sh"), "unknown"], capture_output=True, text=True)
        self.assertNotEqual(failed.returncode, 0)

    def test_downloaded_and_piped_bootstrap_and_failed_download(self):
        bootstrap = self.base / "downloaded-install.sh"
        source_url = "https://raw.githubusercontent.com/Si1entPe661e/EconFinHarness/main/harness/maintenance/install.py"
        script = (ROOT / "install.sh").read_text().replace(
            source_url, (ROOT / "harness/maintenance/install.py").as_uri())
        bootstrap.write_text(script)
        downloaded = subprocess.run(["bash", str(bootstrap), "--help"], capture_output=True, text=True)
        self.assertEqual(downloaded.returncode, 0, downloaded.stderr)
        piped = subprocess.run(["bash", "-s", "--", "--help"], input=script, capture_output=True, text=True)
        self.assertEqual(piped.returncode, 0, piped.stderr)
        bootstrap.write_text(script.replace((ROOT / "harness/maintenance/install.py").as_uri(),
                                            (self.base / "missing-installer.py").as_uri()))
        failed = subprocess.run(["bash", str(bootstrap), "install"], capture_output=True, text=True)
        self.assertNotEqual(failed.returncode, 0)
        self.assertNotIn('"prefix"', failed.stdout)

    def test_standalone_script_at_a_shallow_path_can_report_status(self):
        self.install()
        with patch.object(installer, "__file__", "/install.py"):
            result = self.cli("status")
        self.assertEqual(result[0], 0, result[2])

    def test_installation_lock_rejects_concurrent_mutation(self):
        with installer.installation_lock(self.prefix):
            result = self.cli("install", "--repo", str(self.origin))
        self.assertEqual(result[0], 1)
        self.assertIn("Another installation", result[2])


if __name__ == "__main__":
    unittest.main()
