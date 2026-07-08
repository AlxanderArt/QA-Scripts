from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from qa_scripts.collection_runner import format_results, run_collection  # noqa: E402

if __name__ == "__main__":
    results = run_collection(Path(__file__).with_name("collection.json"))
    print(format_results(results))
    raise SystemExit(0 if all(result.passed for result in results) else 1)
