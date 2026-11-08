
import unittest

from src.password_auditor import PasswordPolicy, audit_password


class TestPasswordAuditor(unittest.TestCase):

    def test_strong_password_passes(self):
        result = audit_password("Tr!angleRiver92")
        self.assertTrue(result["compliant"])

    def test_short_password_fails(self):
        result = audit_password("Ab1!")
        self.assertFalse(result["checks"]["minimum_length"])

    def test_missing_uppercase_fails(self):
        result = audit_password("triangle!river92")
        self.assertFalse(result["checks"]["uppercase"])

    def test_missing_lowercase_fails(self):
        result = audit_password("TRIANGLE!RIVER92")
        self.assertFalse(result["checks"]["lowercase"])

    def test_missing_digit_fails(self):
        result = audit_password("Triangle!River")
        self.assertFalse(result["checks"]["digit"])

    def test_missing_special_character_fails(self):
        result = audit_password("TriangleRiver92")
        self.assertFalse(result["checks"]["special_character"])

    def test_repeated_characters_detected(self):
        result = audit_password("Abcdef!1111Xyz")
        self.assertIn(
            "Excessive repeated characters",
            result["weak_patterns"]
        )

    def test_ascending_sequence_detected(self):
        result = audit_password("Abcdef!123456Xyz")
        self.assertIn(
            "Sequential character pattern",
            result["weak_patterns"]
        )

    def test_descending_sequence_detected(self):
        result = audit_password("Abcdef!987654Xyz")
        self.assertIn(
            "Sequential character pattern",
            result["weak_patterns"]
        )

    def test_keyboard_pattern_detected(self):
        result = audit_password("Abcdef!qwertyXyz")
        self.assertIn(
            "Sequential character pattern",
            result["weak_patterns"]
        )

    def test_common_weak_word_detected(self):
        result = audit_password("Welcome!River92")
        self.assertIn(
            "Common weak password pattern",
            result["weak_patterns"]
        )

    def test_common_password_pattern_detected(self):
        result = audit_password("Password!2026")
        self.assertIn(
            "Common weak password pattern",
            result["weak_patterns"]
        )

    def test_custom_policy(self):
        policy = PasswordPolicy(
            min_length=8,
            require_special=False
        )
        result = audit_password("Triangle92", policy)
        self.assertTrue(result["compliant"])

    def test_non_string_input_rejected(self):
        with self.assertRaises(TypeError):
            audit_password(123456)

    def test_negative_minimum_length_rejected(self):
        with self.assertRaises(ValueError):
            PasswordPolicy(min_length=-1)

    def test_zero_minimum_length_rejected(self):
        with self.assertRaises(ValueError):
            PasswordPolicy(min_length=0)

    def test_invalid_repeat_threshold_rejected(self):
        with self.assertRaises(ValueError):
            PasswordPolicy(max_repeated_chars=0)

    def test_non_boolean_policy_setting_rejected(self):
        with self.assertRaises(ValueError):
            PasswordPolicy(require_digit="yes")


if __name__ == "__main__":
    unittest.main()
