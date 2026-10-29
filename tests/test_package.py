from pathlib import Path
import importlib.util
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / ".agents/skills/mathforge"
SPEC = importlib.util.spec_from_file_location("package_validator", PACKAGE / "scripts/validate_package.py")
assert SPEC is not None and SPEC.loader is not None
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class PackageIntegrityTest(unittest.TestCase):
    def test_committed_package_is_valid(self):
        self.assertEqual(VALIDATOR.validate(PACKAGE), [])

    def test_changed_mathematical_artifact_is_detected(self):
        with tempfile.TemporaryDirectory(prefix="mafs-package-test-") as temporary:
            copy = Path(temporary) / "mathforge"
            shutil.copytree(PACKAGE, copy)
            target = copy / "references/solution-contract.md"
            target.write_text(target.read_text() + "\nUnexpected alteration.\n")
            failures = VALIDATOR.validate(copy)
            self.assertIn("Manifest mismatch: references/solution-contract.md", failures)


if __name__ == "__main__":
    unittest.main()
