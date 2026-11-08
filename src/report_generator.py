
from datetime import datetime, timezone
from pathlib import Path


def generate_report(result: dict, output_dir: str = "reports") -> Path:
    """
    Generate a text compliance report.
    Password values are never included in the report.
    """

    report_folder = Path(output_dir)
    report_folder.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc)
    filename = timestamp.strftime("password_audit_%Y%m%d_%H%M%S.txt")
    report_path = report_folder / filename

    status = "COMPLIANT" if result["compliant"] else "NON-COMPLIANT"

    lines = [
        "PASSWORD POLICY AUDIT REPORT",
        "=" * 40,
        f"Generated: {timestamp.strftime('%Y-%m-%d %H:%M:%S UTC')}",
        f"Overall result: {status}",
        "",
        "POLICY CHECKS",
        "-" * 40,
    ]

    for rule, passed in result["checks"].items():
        outcome = "PASS" if passed else "FAIL"
        lines.append(f"{rule.replace('_', ' ').title()}: {outcome}")

    lines.extend(["", "FAILED REQUIREMENTS", "-" * 40])

    if result["failed_checks"]:
        for failure in result["failed_checks"]:
            lines.append(f"- {failure.replace('_', ' ').title()}")
    else:
        lines.append("None")

    lines.extend(["", "WEAK PATTERNS DETECTED", "-" * 40])

    if result["weak_patterns"]:
        for pattern in result["weak_patterns"]:
            lines.append(f"- {pattern}")
    else:
        lines.append("None")

    lines.extend([
        "",
        "SECURITY NOTE",
        "-" * 40,
        "This report contains audit results only.",
        "No password values are stored in this report.",
        "Use synthetic test passwords only.",
    ])

    report_path.write_text("\n".join(lines), encoding="utf-8")

    return report_path
