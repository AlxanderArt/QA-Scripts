from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

BUDGETS: Mapping[str, float] = {
    "p95_ms": 500.0,
    "error_rate": 0.01,
    "bundle_kb": 350.0,
}


@dataclass(frozen=True)
class BudgetViolation:
    metric: str
    actual: float | None
    limit: float
    reason: str


@dataclass(frozen=True)
class PerformanceBudgetResult:
    passed: bool
    violations: tuple[BudgetViolation, ...]


def evaluate_budget(metrics: Mapping[str, object], budgets: Mapping[str, float] = BUDGETS) -> PerformanceBudgetResult:
    violations: list[BudgetViolation] = []
    for metric, limit in budgets.items():
        if metric not in metrics:
            violations.append(BudgetViolation(metric, None, limit, "missing required metric"))
            continue
        raw_actual = metrics[metric]
        if isinstance(raw_actual, bool) or not isinstance(raw_actual, int | float):
            violations.append(BudgetViolation(metric, None, limit, "metric must be numeric"))
            continue
        actual = float(raw_actual)
        if actual > limit:
            violations.append(BudgetViolation(metric, actual, limit, "budget exceeded"))
    return PerformanceBudgetResult(not violations, tuple(violations))
