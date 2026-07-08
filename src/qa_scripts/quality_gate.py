from __future__ import annotations

from dataclasses import dataclass
from typing import Any

MIN_PASS_RATE = 0.95
MAX_CRITICAL_DEFECTS = 0


@dataclass(frozen=True)
class GateResult:
    pass_rate: float
    critical_defects: int
    passed: bool
    reason: str

    def as_dict(self) -> dict[str, Any]:
        return {
            "pass_rate": round(self.pass_rate, 4),
            "critical_defects": self.critical_defects,
            "passed": self.passed,
            "reason": self.reason,
        }


def evaluate(results: dict[str, Any]) -> GateResult:
    passed_count = int(results.get("passed", 0))
    failed_count = int(results.get("failed", 0))
    critical_defects = int(results.get("critical_defects", 0))
    if min(passed_count, failed_count, critical_defects) < 0:
        return GateResult(0.0, max(critical_defects, 0), False, "result counts cannot be negative")
    total = passed_count + failed_count
    if total <= 0:
        return GateResult(0.0, critical_defects, False, "no test results supplied")
    pass_rate = passed_count / total
    if critical_defects > MAX_CRITICAL_DEFECTS:
        return GateResult(pass_rate, critical_defects, False, "critical defects exceed threshold")
    if pass_rate < MIN_PASS_RATE:
        return GateResult(pass_rate, critical_defects, False, "pass rate below threshold")
    return GateResult(pass_rate, critical_defects, True, "quality gate passed")
