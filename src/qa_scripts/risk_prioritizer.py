from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FeatureRisk:
    feature: str
    customer_impact: int
    change_frequency: int
    defect_history: int

    def __post_init__(self) -> None:
        for field_name, value in (
            ("customer_impact", self.customer_impact),
            ("change_frequency", self.change_frequency),
            ("defect_history", self.defect_history),
        ):
            if type(value) is not int or not 1 <= value <= 5:
                raise ValueError(f"{field_name} must be an integer between 1 and 5")

    @property
    def score(self) -> int:
        return self.customer_impact * 3 + self.change_frequency * 2 + self.defect_history


def prioritize(features: list[FeatureRisk]) -> tuple[FeatureRisk, ...]:
    return tuple(sorted(features, key=lambda item: (-item.score, item.feature)))
