from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SRC_ROOT = REPO_ROOT / "src"


def repo_path(*parts: str) -> Path:
    """Resolve a path from the repository root."""
    return REPO_ROOT.joinpath(*parts)


def ensure_src_on_path() -> None:
    """Allow direct script execution without requiring package installation first."""
    src = str(SRC_ROOT)
    if src not in sys.path:
        sys.path.insert(0, src)
