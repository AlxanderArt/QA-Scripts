from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from qa_scripts.flaky_test_detector import analyze_history  # noqa: E402


def main() -> None:
    signals = analyze_history({"test_checkout": [True, False, True, False], "test_login": [True, True, True]})
    flaky = [signal.test_name for signal in signals if signal.flaky]
    print(f"PASS - flaky tests detected: {flaky}")


if __name__ == "__main__":
    main()
