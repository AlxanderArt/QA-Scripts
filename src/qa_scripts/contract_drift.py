from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ContractDrift:
    field: str
    expected_type: str
    actual_type: str


def detect_contract_drift(expected: dict[str, str], actual: dict[str, str]) -> tuple[ContractDrift, ...]:
    drift: list[ContractDrift] = []
    for field, expected_type in sorted(expected.items()):
        actual_type = actual.get(field, "missing")
        if actual_type != expected_type:
            drift.append(ContractDrift(field, expected_type, actual_type))
    for field, actual_type in sorted(actual.items()):
        if field not in expected:
            drift.append(ContractDrift(field, "unexpected", actual_type))
    return tuple(drift)
