from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from qa_scripts.quality_gate import evaluate  # noqa: E402

if __name__ == "__main__":
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("reports/sample_outputs/test-results.json")
    result = evaluate(json.loads(path.read_text(encoding="utf-8")))
    print(json.dumps(result.as_dict(), indent=2))
    raise SystemExit(0 if result.passed else 1)
