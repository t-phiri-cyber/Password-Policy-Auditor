
import re
from dataclasses import dataclass


@dataclass
class PasswordPolicy:
    min_length: int = 12
    require_uppercase: bool = True
    require_lowercase: bool = True
    require_digit: bool = True
    require_special: bool = True
    max_repeated_chars: int = 3

    def __post_init__(self):
        if type(self.min_length) is not int or self.min_length < 1:
            raise ValueError("Minimum length must be a positive integer.")

        if (
            type(self.max_repeated_chars) is not int
            or self.max_repeated_chars < 1
        ):
            raise ValueError(
                "Maximum repeated characters must be a positive integer."
            )

        settings = (
            self.require_uppercase,
            self.require_lowercase,
            self.require_digit,
            self.require_special,
        )

        if not all(type(setting) is bool for setting in settings):
            raise ValueError("Policy requirements must be True or False.")


def audit_password(password: str, policy: PasswordPolicy = None) -> dict:
    """Audit a synthetic test password against a configurable policy."""

    if not isinstance(password, str):
        raise TypeError("Password must be a string.")

    if policy is None:
        policy = PasswordPolicy()

    if not isinstance(policy, PasswordPolicy):
        raise TypeError("Policy must be a PasswordPolicy instance.")

    checks = {
        "minimum_length": len(password) >= policy.min_length,
        "uppercase": not policy.require_uppercase or bool(
            re.search(r"[A-Z]", password)
        ),
        "lowercase": not policy.require_lowercase or bool(
            re.search(r"[a-z]", password)
        ),
        "digit": not policy.require_digit or bool(
            re.search(r"\d", password)
        ),
        "special_character": not policy.require_special or bool(
            re.search(r"[^A-Za-z0-9]", password)
        ),
    }

    weak_patterns = []

    repeated_pattern = (
        r"(.)\1{" + str(policy.max_repeated_chars) + r",}"
    )

    if re.search(repeated_pattern, password):
        weak_patterns.append("Excessive repeated characters")

    common_patterns = (
        "password", "letmein", "admin", "welcome", "qwerty"
    )

    if any(pattern in password.lower() for pattern in common_patterns):
        weak_patterns.append("Common weak password pattern")

    sequences = (
        "abcdefghijklmnopqrstuvwxyz",
        "123456", "234567", "345678", "456789",
        "987654", "876543", "765432", "654321",
        "qwerty", "asdfgh", "zxcvbn",
    )

    if any(sequence in password.lower() for sequence in sequences):
        weak_patterns.append("Sequential character pattern")

    failed_checks = [
        rule for rule, passed in checks.items() if not passed
    ]

    return {
        "compliant": all(checks.values()) and not weak_patterns,
        "checks": checks,
        "failed_checks": failed_checks,
        "weak_patterns": weak_patterns,
    }
