import importlib.util
from pathlib import Path
from types import ModuleType


def load_regression_matrix() -> ModuleType:
    module_path = Path(__file__).with_name("regression_matrix.py")
    spec = importlib.util.spec_from_file_location("regression_matrix", module_path)
    assert spec is not None
    assert spec.loader is not None
    regression_matrix = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(regression_matrix)
    return regression_matrix


def test_cross_browser_matrix_covers_all_critical_flows():
    regression_matrix = load_regression_matrix()
    matrix = regression_matrix.build_matrix()
    assert len(matrix) == 9
    assert {case["browser"] for case in matrix} == {"chromium", "firefox", "webkit"}
    assert {case["flow"] for case in matrix} == {"login", "search", "checkout"}
    assert any(case["priority"] == "P0" for case in matrix)
