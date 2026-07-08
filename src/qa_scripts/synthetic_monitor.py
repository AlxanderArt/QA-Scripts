from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MonitorCheck:
    name: str
    status_code: int
    latency_ms: int


@dataclass(frozen=True)
class MonitorResult:
    healthy: bool
    reason: str


def evaluate_monitor(check: MonitorCheck, *, max_latency_ms: int = 750) -> MonitorResult:
    if not 100 <= check.status_code <= 599:
        return MonitorResult(False, "invalid status code")
    if check.latency_ms < 0 or max_latency_ms < 0:
        return MonitorResult(False, "latency cannot be negative")
    if check.status_code >= 500:
        return MonitorResult(False, "server error")
    if check.status_code >= 400:
        return MonitorResult(False, "client error")
    if check.latency_ms > max_latency_ms:
        return MonitorResult(False, "latency budget exceeded")
    return MonitorResult(True, "synthetic monitor passed")
