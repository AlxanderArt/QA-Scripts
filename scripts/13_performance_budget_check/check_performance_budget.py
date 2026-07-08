from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from qa_scripts.performance_budget import evaluate_budget  # noqa: E402


def main() -> None:
    result = evaluate_budget({"p95_ms": 320.0, "error_rate": 0.0, "bundle_kb": 280.0})
    print("PASS - performance budget" if result.passed else f"FAIL - {result.violations}")
    raise SystemExit(0 if result.passed else 1)


if __name__ == "__main__":
    main()
