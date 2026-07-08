from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from qa_scripts.defect_reporter import SAMPLE_DEFECT, render  # noqa: E402

if __name__ == "__main__":
    out = Path("reports/generated") / f"defect-{SAMPLE_DEFECT.id}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(SAMPLE_DEFECT), encoding="utf-8")
    print(out)
