from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]


def repo_path(*parts: str) -> Path:
    """Resolve a path from the repository root."""
    return REPO_ROOT.joinpath(*parts)
