from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ReadinessCheck:
    name: str
    passed: bool
    owner: str


@dataclass(frozen=True)
class ReadinessResult:
    ready: bool
    blockers: tuple[ReadinessCheck, ...]


def evaluate_readiness(checks: list[ReadinessCheck]) -> ReadinessResult:
    blockers = tuple(check for check in checks if not check.passed)
    return ReadinessResult(not blockers, blockers)
