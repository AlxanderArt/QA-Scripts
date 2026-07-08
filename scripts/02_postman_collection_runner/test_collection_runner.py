from pathlib import Path

from qa_scripts.collection_runner import format_results, run_collection


def test_collection_runner_reports_named_results():
    results = run_collection(Path(__file__).with_name("collection.json"))
    assert all(result.passed for result in results)
    output = format_results(results)
    assert "PASS - Get user" in output
    assert "PASS - Missing user" in output
