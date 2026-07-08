from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Defect:
    id: str
    title: str
    severity: str
    steps: tuple[str, ...]
    expected: str
    actual: str
    root_cause_prompt: str


SAMPLE_DEFECT = Defect(
    id="BUG-1042",
    title="Checkout total does not include tax after coupon removal",
    severity="High",
    steps=("Add item to cart", "Apply coupon", "Remove coupon", "Proceed to checkout"),
    expected="Tax is recalculated after coupon removal.",
    actual="Checkout shows stale tax value.",
    root_cause_prompt="Review cart state invalidation after coupon mutation.",
)


def render(defect: Defect = SAMPLE_DEFECT) -> str:
    steps = "\n".join(f"{index}. {step}" for index, step in enumerate(defect.steps, start=1))
    return (
        f"# {defect.id} - {defect.title}\n\n"
        f"**Severity:** {defect.severity}\n\n"
        f"## Steps to Reproduce\n{steps}\n\n"
        f"## Expected\n{defect.expected}\n\n"
        f"## Actual\n{defect.actual}\n\n"
        f"## RCA Prompt\n{defect.root_cause_prompt}\n"
    )
