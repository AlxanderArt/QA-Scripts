from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "src"))

from qa_scripts.test_data_factory import build_user_batch  # noqa: E402


def main() -> None:
    users = build_user_batch(2, role="admin")
    print(users)


if __name__ == "__main__":
    main()
