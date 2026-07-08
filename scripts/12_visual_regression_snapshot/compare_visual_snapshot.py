from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from qa_scripts.visual_regression import compare_pixel_buffers  # noqa: E402


def main() -> None:
    result = compare_pixel_buffers([1, 1, 1, 1, 1], [1, 1, 1, 1, 2], threshold=0.25)
    print(f"PASS - visual diff ratio {result.diff_ratio}" if result.passed else "FAIL - visual diff exceeded")
    raise SystemExit(0 if result.passed else 1)


if __name__ == "__main__":
    main()
