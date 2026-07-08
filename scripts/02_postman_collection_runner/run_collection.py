import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import _bootstrap  # noqa: F401,E402
from apps.demo_api import demo_api

OPERATIONS = {"get_user": demo_api.get_user, "create_user": demo_api.create_user}

def run_collection(path: Path):
    collection = json.loads(path.read_text())
    results = []
    for item in collection["items"]:
        response = OPERATIONS[item["operation"]](*item.get("args", []))
        passed = response["status"] == item["expect_status"]
        for key in item.get("expect_keys", []):
            passed = passed and key in response["body"]
        if "expect_error" in item:
            passed = passed and response["body"].get("error") == item["expect_error"]
        results.append({"name": item["name"], "passed": passed})
    return results

if __name__ == "__main__":
    results = run_collection(Path(__file__).with_name("collection.json"))
    for result in results:
        print(f"{'PASS' if result['passed'] else 'FAIL'} - {result['name']}")
    raise SystemExit(0 if all(r["passed"] for r in results) else 1)
