from pathlib import Path

from qa_scripts.collection_runner import CollectionResult, format_results, run_collection


def test_collection_runner_reports_named_results():
    results = run_collection(Path(__file__).with_name("collection.json"))
    assert all(result.passed for result in results)
    output = format_results(results)
    assert "PASS - Get user" in output
    assert "PASS - Missing user" in output


def test_collection_runner_handles_malformed_collection_items(tmp_path):
    collection = tmp_path / "bad_collection.json"
    collection.write_text('{"items": [{"name": "Bad row", "operation": "get_user"}]}', encoding="utf-8")
    assert run_collection(collection) == [
        CollectionResult("Bad row", False, 0, 0, ("missing required field: expect_status",))
    ]


def test_collection_runner_reports_unknown_operation_with_fallback_name(tmp_path):
    collection = tmp_path / "unknown_operation.json"
    collection.write_text('{"items": [{"operation": "delete_user", "expect_status": 204}]}', encoding="utf-8")
    assert run_collection(collection) == [
        CollectionResult("delete_user", False, 204, 0, ("unknown operation: delete_user",))
    ]


def test_collection_runner_reports_non_integer_expected_status(tmp_path):
    collection = tmp_path / "bad_status.json"
    collection.write_text(
        '{"items": [{"name": "Bad status", "operation": "get_user", "expect_status": "two hundred"}]}',
        encoding="utf-8",
    )
    assert run_collection(collection) == [
        CollectionResult("Bad status", False, 0, 0, ("expect_status must be an integer",))
    ]
