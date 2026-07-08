from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LogFinding:
    line_number: int
    severity: str
    message: str


def scan_logs(lines: list[str]) -> tuple[LogFinding, ...]:
    findings: list[LogFinding] = []
    for index, line in enumerate(lines, start=1):
        normalized = line.lower()
        if "traceback" in normalized or "exception" in normalized:
            findings.append(LogFinding(index, "critical", line))
        elif "error" in normalized or "timeout" in normalized:
            findings.append(LogFinding(index, "high", line))
        elif "warning" in normalized or "retry" in normalized:
            findings.append(LogFinding(index, "medium", line))
    return tuple(findings)
