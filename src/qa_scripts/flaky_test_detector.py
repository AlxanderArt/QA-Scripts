from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FlakeSignal:
    test_name: str
    pass_rate: float
    transitions: int
    flaky: bool


def analyze_history(history: dict[str, list[bool]], *, min_transitions: int = 2) -> tuple[FlakeSignal, ...]:
    signals: list[FlakeSignal] = []
    for test_name, outcomes in sorted(history.items()):
        if not outcomes:
            signals.append(FlakeSignal(test_name, 0.0, 0, False))
            continue
        transitions = sum(1 for previous, current in zip(outcomes, outcomes[1:], strict=False) if previous != current)
        pass_rate = sum(outcomes) / len(outcomes)
        flaky = 0.0 < pass_rate < 1.0 and transitions >= min_transitions
        signals.append(FlakeSignal(test_name, round(pass_rate, 4), transitions, flaky))
    return tuple(signals)
