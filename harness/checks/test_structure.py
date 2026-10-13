"""Structural checks for progressive loading, preserved records and shared roles."""
import hashlib
import importlib.util
import json
import re
import tempfile
import unittest
from pathlib import Path
from urllib.parse import unquote, urlparse

from harness.maintenance.sync_roles import ROOT, expected_config, expected_role, role_source


class StructureChecks(unittest.TestCase):
    def test_skill_frontmatter_uses_supported_top_level_fields(self):
        allowed={"name","description","license","allowed-tools","metadata"}
        for path in (ROOT/"harness/skills").glob("*/SKILL.md"):
            front=path.read_text().split("---",2)[1]
            keys=set(re.findall(r"(?m)^([a-z][a-z0-9-]*):",front))
            self.assertFalse(keys-allowed,(path.parent.name,sorted(keys-allowed)))

    def test_published_skill_ids_have_the_project_suffix(self):
        skills=list((ROOT/"harness/skills").glob("*/SKILL.md"))
        self.assertTrue(skills)
        for path in skills:
            self.assertRegex(path.parent.name,r"^[a-z0-9]+(?:-[a-z0-9]+)*-efh$")
            self.assertLess(len(path.parent.name),64)
            self.assertFalse((path.parent.parent/path.parent.name.removesuffix("-efh")/"SKILL.md").exists())
        for path in (ROOT/"harness/agents").glob("*.md"):
            metadata,_=role_source(path)
            for skill in metadata["skills"]:
                self.assertTrue(skill.endswith("-efh"),(path.name,skill))

    def test_tool_entrypoints_remain_relative_shared_symlinks(self):
        expected={".agents/skills":"harness/skills",".claude/skills":"harness/skills",
                  ".claude/agents":"harness/agents"}
        for link,target in expected.items():
            path=ROOT/link
            self.assertTrue(path.is_symlink(),link)
            self.assertFalse(path.readlink().is_absolute(),link)
            self.assertEqual(path.resolve(),(ROOT/target).resolve(),link)

    def test_every_route_resolves_to_focused_roles_and_skills(self):
        routes=json.loads((ROOT/"harness/orchestration/routes.json").read_text())
        for capability,route in routes.items():
            self.assertTrue((ROOT/"harness/agents"/(route["role"]+".md")).is_file(),capability)
            self.assertLessEqual(len(route["skills"]),3)
            for skill in route["skills"]:
                self.assertTrue((ROOT/"harness/skills"/skill/"SKILL.md").is_file(),capability)

    def test_evidence_review_can_deliver_owned_artifacts_without_editing_sources(self):
        text=(ROOT/"harness/agents/evidence-reviewer.md").read_text()
        self.assertIn("assigned review artifacts",text)
        self.assertNotIn("Remain read-only.",text)

    def test_skill_entrypoints_are_bounded_and_have_identity(self):
        for p in (ROOT/"harness/skills").glob("*/SKILL.md"):
            text=p.read_text()
            self.assertTrue(text.startswith("---\n"),str(p))
            front=text.split("---",2)[1]
            self.assertRegex(front,r"(?m)^name: "+re.escape(p.parent.name)+r"$")
            self.assertRegex(front,r"(?m)^description: .+")
            self.assertLessEqual(len(text.split()),750,str(p))

    def test_recorded_research_sections_are_preserved_exactly(self):
        records=json.loads((ROOT/"harness/checks/fixtures/research_record_hashes.json").read_text())
        for path,record in records.items():
            p=ROOT/path
            self.assertEqual(hashlib.sha256(p.read_bytes()).hexdigest(),record["sha256"],path)
            skill=(ROOT/record["source_skill"]).read_text()
            self.assertIn("references/research-records.md",skill)

    def test_shared_roles_and_codex_registration_stay_synchronized(self):
        for path in (ROOT/"harness/agents").glob("*.md"):
            meta,body=role_source(path)
            self.assertLessEqual(len(body.split()),400,str(path))
            self.assertEqual((ROOT/"harness/agents/codex"/(path.stem+".toml")).read_text(),expected_role(path))
        config=(ROOT/".codex/config.toml").read_text()
        self.assertEqual(config,expected_config(config))

    def test_general_and_split_document_links_resolve(self):
        paths=list((ROOT/"harness/orchestration").glob("*.md"))
        paths+=list((ROOT/"harness/workflows").glob("*.md"))
        paths+=list((ROOT/"harness/skills").rglob("*.md"))
        paths+=list((ROOT/"harness/presets").glob("*.md"))
        paths+=list((ROOT/"harness/maintenance").glob("*.md"))
        paths+=list((ROOT/"harness/examples").glob("*/README.md"))
        paths+=[ROOT/"README.md",ROOT/"harness/README.md",ROOT/"harness/skill-composition.md"]
        for path in paths:
            # Markdown links only; inline-code paths and optional local corpus pointers are not links.
            for target in re.findall(r"\]\(([^)]+)\)",path.read_text()):
                if urlparse(target).scheme or target.startswith("#"):continue
                target=unquote(target.split("#",1)[0].strip("<>"))
                self.assertTrue((path.parent/target).resolve().exists(),f"{path.relative_to(ROOT)} -> {target}")

    def test_role_sync_preserves_settings_outside_managed_block(self):
        source='unrelated = "preserved"\n# >>> fh-managed >>>\nold\n# <<< fh-managed <<<\n# custom trailing comment\n'
        result=expected_config(source)
        self.assertTrue(result.startswith('unrelated = "preserved"\n'))
        self.assertTrue(result.endswith('# custom trailing comment\n'))
        self.assertEqual(expected_config(result),result)

    def test_general_demo_can_resume_and_preserves_stale_evidence(self):
        path=ROOT/"harness/examples/general/run_demo.py"
        spec=importlib.util.spec_from_file_location("general_demo",path)
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        with tempfile.TemporaryDirectory() as d:
            first=module.run(Path(d));second=module.run(Path(d))
            self.assertEqual(first["operations-report"]["tasks"][0]["attempts"],2)
            self.assertEqual(second["operations-report"]["tasks"][0]["attempts"],2)
            self.assertEqual(second["document-editing"]["evidence"][0]["freshness"],"stale")
            self.assertTrue(all(second[k]["execution"]=="succeeded" for k in
                                ("project-management","operations-report","document-editing")))


if __name__=="__main__":
    unittest.main()
