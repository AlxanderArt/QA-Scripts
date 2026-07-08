from __future__ import annotations

import json
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from qa_scripts import demo_api
from qa_scripts.demo_api import ApiResponse

Operation = Callable[..., ApiResponse]
OPERATIONS: dict[str, Operation] = {
    "get_user": demo_api.get_user,
    "create_user": demo_api.create_user,
}


@dataclass(frozen=True)
class CollectionResult:
    name: str
    passed: bool
    expected_status: int
    actual_status: int
    failures: tuple[str, ...] = ()


def _load_collection(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid collection JSON: {path}: {exc}") from exc


def run_collection(path: Path) -> list[CollectionResult]:
    demo_api.reset_users()
    collection = _load_collection(path)
    results: list[CollectionResult] = []
    for index, item in enumerate(collection.get("items", []), start=1):
        failures: list[str] = []
        operation_name = item.get("operation")
        item_name = str(item.get("name", operation_name or f"item {index}"))
        if "expect_status" not in item:
            results.append(CollectionResult(item_name, False, 0, 0, ("missing required field: expect_status",)))
            continue

        operation = OPERATIONS.get(operation_name)
        try:
            expected_status = int(item.get("expect_status", 0))
        except (TypeError, ValueError):
            results.append(CollectionResult(item_name, False, 0, 0, ("expect_status must be an integer",)))
            continue
        if operation is None:
            results.append(CollectionResult(item_name, False, expected_status, 0, (f"unknown operation: {operation_name}",)))
            continue

        response = operation(*item.get("args", []))
        actual_status = int(response["status"])
        if actual_status != expected_status:
            failures.append(f"status {actual_status} != expected {expected_status}")
        for key in item.get("expect_keys", []):
            if key not in response["body"]:
                failures.append(f"missing response key: {key}")
        if "expect_error" in item and response["body"].get("error") != item["expect_error"]:
            failures.append(f"error {response['body'].get('error')!r} != expected {item['expect_error']!r}")
        results.append(CollectionResult(item_name, not failures, expected_status, actual_status, tuple(failures)))
    return results


def format_results(results: list[CollectionResult]) -> str:
    lines = []
    for result in results:
        suffix = "" if result.passed else f" ({'; '.join(result.failures)})"
        lines.append(f"{'PASS' if result.passed else 'FAIL'} - {result.name}{suffix}")
    return "\n".join(lines)
