from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from qa_scripts.accessibility_audit import audit_login_markup, sample_accessible_login  # noqa: E402


def main() -> None:
    report = audit_login_markup(sample_accessible_login())
    print("PASS - accessibility audit" if report.passed else f"FAIL - {report.issues}")
    raise SystemExit(0 if report.passed else 1)


if __name__ == "__main__":
    main()
