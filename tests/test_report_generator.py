
import tempfile
import unittest

from src.password_auditor import audit_password
from src.report_generator import generate_report


class TestReportGenerator(unittest.TestCase):

    def test_report_is_created(self):
        result = audit_password("Weak123")

        with tempfile.TemporaryDirectory() as temp_dir:
            report_path = generate_report(result, temp_dir)

            self.assertTrue(report_path.exists())
            self.assertGreater(report_path.stat().st_size, 0)

    def test_report_does_not_contain_password(self):
        test_password = "Weak123"
        result = audit_password(test_password)

        with tempfile.TemporaryDirectory() as temp_dir:
            report_path = generate_report(result, temp_dir)
            report_content = report_path.read_text(encoding="utf-8")

            self.assertNotIn(test_password, report_content)

    def test_report_contains_compliance_status(self):
        result = audit_password("Weak123")

        with tempfile.TemporaryDirectory() as temp_dir:
            report_path = generate_report(result, temp_dir)
            report_content = report_path.read_text(encoding="utf-8")

            self.assertIn("NON-COMPLIANT", report_content)


if __name__ == "__main__":
    unittest.main()
