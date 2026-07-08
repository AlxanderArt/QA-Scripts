from __future__ import annotations

from dataclasses import asdict, dataclass

REQUIREMENT = "Users can reset a forgotten password using a verified email address."
HEURISTICS = ("happy_path", "invalid_input", "expired_token", "rate_limit", "audit_logging", "accessibility")


@dataclass(frozen=True)
class TestCase:
    id: str
    heuristic: str
    requirement: str
    expected: str
    priority: str


def generate(requirement: str = REQUIREMENT, heuristics: tuple[str, ...] = HEURISTICS) -> list[dict[str, str]]:
    cases = [
        TestCase(
            id=f"TC-{index:03d}",
            heuristic=heuristic,
            requirement=requirement,
            expected=f"Validate {heuristic.replace('_', ' ')} behavior.",
            priority="P0" if heuristic in {"happy_path", "expired_token", "rate_limit"} else "P1",
        )
        for index, heuristic in enumerate(heuristics, start=1)
    ]
    return [asdict(case) for case in cases]
