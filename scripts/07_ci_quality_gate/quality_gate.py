import json
import sys
from pathlib import Path
MIN_PASS_RATE = 0.95
MAX_CRITICAL_DEFECTS = 0

def evaluate(results):
    total = results["passed"] + results["failed"]
    pass_rate = results["passed"] / total if total else 0
    return {"pass_rate": pass_rate, "critical_defects": results.get("critical_defects", 0), "passed": pass_rate >= MIN_PASS_RATE and results.get("critical_defects", 0) <= MAX_CRITICAL_DEFECTS}

if __name__ == "__main__":
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("reports/sample_outputs/test-results.json")
    result = evaluate(json.loads(path.read_text()))
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["passed"] else 1)
