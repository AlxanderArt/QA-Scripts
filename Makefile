.PHONY: install lint type test reports standalone verify playwright-install clean

install:
	python3 -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

playwright-install:
	python -m playwright install chromium

lint:
	ruff check .

type:
	mypy src apps scripts

test:
	pytest -q

reports:
	mkdir -p reports/generated
	pytest -q --junitxml=reports/generated/junit.xml --html=reports/generated/report.html --self-contained-html

standalone:
	python scripts/02_postman_collection_runner/run_collection.py
	python scripts/06_sql_data_validation/sql_validation.py
	python scripts/07_ci_quality_gate/quality_gate.py reports/sample_outputs/test-results.json
	python scripts/08_defect_lifecycle_reporter/defect_reporter.py
	python scripts/09_ai_assisted_test_case_generator/generate_test_cases.py
	python scripts/11_accessibility_audit/audit_accessibility.py
	python scripts/12_visual_regression_snapshot/compare_visual_snapshot.py
	python scripts/13_performance_budget_check/check_performance_budget.py
	python scripts/14_log_anomaly_scanner/scan_logs.py
	python scripts/15_flaky_test_detector/detect_flakes.py
	python scripts/16_test_data_factory/generate_test_data.py
	python scripts/17_risk_based_prioritization/prioritize_risks.py
	python scripts/18_release_readiness_checklist/check_release_readiness.py
	python scripts/19_contract_drift_detector/detect_contract_drift.py
	python scripts/20_synthetic_monitoring_probe/run_synthetic_monitor.py

verify: lint type test reports standalone

clean:
	rm -rf .pytest_cache .ruff_cache .mypy_cache reports/generated
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
