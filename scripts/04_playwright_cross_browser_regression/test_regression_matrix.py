import importlib.util
from pathlib import Path
module_path = Path(__file__).with_name("regression_matrix.py")
spec = importlib.util.spec_from_file_location("regression_matrix", module_path)
regression_matrix = importlib.util.module_from_spec(spec)
spec.loader.exec_module(regression_matrix)

def test_cross_browser_matrix_covers_all_critical_flows():
    matrix = regression_matrix.build_matrix()
    assert len(matrix) == 9
    assert {case["browser"] for case in matrix} == {"chromium", "firefox", "webkit"}
    assert {case["flow"] for case in matrix} == {"login", "search", "checkout"}
    assert any(case["priority"] == "P0" for case in matrix)
