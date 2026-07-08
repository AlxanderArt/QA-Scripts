from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from qa_scripts.risk_prioritizer import FeatureRisk, prioritize  # noqa: E402


def main() -> None:
    ordered = prioritize([
        FeatureRisk("profile", 2, 2, 1),
        FeatureRisk("checkout", 5, 4, 3),
    ])
    print(f"PASS - top risk: {ordered[0].feature}")


if __name__ == "__main__":
    main()
