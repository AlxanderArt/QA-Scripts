"""Legacy compatibility helper for direct script execution.

The improved portfolio now keeps reusable code in `src/qa_scripts`. This file is
kept so earlier examples that imported `scripts._bootstrap` do not break.
"""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
for candidate in (SRC_ROOT, REPO_ROOT):
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))
