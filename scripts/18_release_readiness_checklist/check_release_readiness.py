from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from qa_scripts.release_readiness import ReadinessCheck, evaluate_readiness  # noqa: E402


def main() -> None:
    result = evaluate_readiness([
        ReadinessCheck("tests", True, "qa"),
        ReadinessCheck("rollback plan", True, "release-manager"),
    ])
    print("PASS - release ready" if result.ready else f"FAIL - blockers: {result.blockers}")
    raise SystemExit(0 if result.ready else 1)


if __name__ == "__main__":
    main()
