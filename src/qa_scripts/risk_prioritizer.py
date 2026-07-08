from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FeatureRisk:
    feature: str
    customer_impact: int
    change_frequency: int
    defect_history: int

    @property
    def score(self) -> int:
        return self.customer_impact * 3 + self.change_frequency * 2 + self.defect_history


def prioritize(features: list[FeatureRisk]) -> tuple[FeatureRisk, ...]:
    return tuple(sorted(features, key=lambda item: (-item.score, item.feature)))
