from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from qa_scripts.contract_drift import detect_contract_drift  # noqa: E402


def main() -> None:
    drift = detect_contract_drift({"id": "integer", "email": "string"}, {"id": "integer", "email": "string"})
    print("PASS - no contract drift" if not drift else f"FAIL - {drift}")
    raise SystemExit(0 if not drift else 1)


if __name__ == "__main__":
    main()
