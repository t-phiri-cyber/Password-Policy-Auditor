
from getpass import getpass

from src.password_auditor import audit_password
from src.report_generator import generate_report


def main():
    print("=" * 45)
    print("       PASSWORD POLICY AUDITOR")
    print("=" * 45)
    print("Local password security assessment tool")
    print("Use synthetic test passwords only.")
    print()

    password = getpass("Enter a synthetic test password: ")

    try:
        result = audit_password(password)

        print("\nAUDIT RESULTS")
        print("-" * 45)

        for rule, passed in result["checks"].items():
            status = "PASS" if passed else "FAIL"
            print(f"{rule.replace('_', ' ').title()}: {status}")

        print("\nWEAK PATTERNS")
        print("-" * 45)

        if result["weak_patterns"]:
            for pattern in result["weak_patterns"]:
                print(f"- {pattern}")
        else:
            print("No weak patterns detected.")

        print("\nOVERALL RESULT")
        print("-" * 45)

        if result["compliant"]:
            print("COMPLIANT")
        else:
            print("NON-COMPLIANT")

        report_path = generate_report(result)

        print(f"\nReport saved to: {report_path}")

    except (TypeError, ValueError) as error:
        print(f"Audit error: {error}")

    finally:
        password = None


if __name__ == "__main__":
    main()
