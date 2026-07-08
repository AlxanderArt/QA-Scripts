from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class VisualDiffResult:
    changed_pixels: int
    total_pixels: int
    diff_ratio: float
    passed: bool


def compare_pixel_buffers(baseline: list[int], candidate: list[int], *, threshold: float = 0.01) -> VisualDiffResult:
    if len(baseline) != len(candidate):
        raise ValueError("baseline and candidate must have the same pixel count")
    if not baseline:
        raise ValueError("pixel buffers cannot be empty")
    changed = sum(1 for expected, actual in zip(baseline, candidate, strict=True) if expected != actual)
    ratio = changed / len(baseline)
    return VisualDiffResult(changed, len(baseline), round(ratio, 4), ratio <= threshold)
