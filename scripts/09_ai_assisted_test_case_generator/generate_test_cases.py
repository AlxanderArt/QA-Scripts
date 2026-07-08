from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from qa_scripts.test_case_generator import generate  # noqa: E402

if __name__ == "__main__":
    print(json.dumps(generate(), indent=2))
