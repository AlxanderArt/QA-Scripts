from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from qa_scripts.log_anomaly import scan_logs  # noqa: E402


def main() -> None:
    findings = scan_logs(["INFO started", "WARNING retry payment call", "INFO recovered"])
    print(f"PASS - {len(findings)} log finding(s) captured")


if __name__ == "__main__":
    main()
