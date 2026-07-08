from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from qa_scripts.synthetic_monitor import MonitorCheck, evaluate_monitor  # noqa: E402


def main() -> None:
    result = evaluate_monitor(MonitorCheck("login health", 200, 180))
    print("PASS - synthetic monitor" if result.healthy else f"FAIL - {result.reason}")
    raise SystemExit(0 if result.healthy else 1)


if __name__ == "__main__":
    main()
