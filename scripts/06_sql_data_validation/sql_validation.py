from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from qa_scripts.sql_validation import format_checks, run_validation  # noqa: E402

if __name__ == "__main__":
    checks = run_validation()
    print(format_checks(checks))
    raise SystemExit(0 if all(checks.values()) else 1)
