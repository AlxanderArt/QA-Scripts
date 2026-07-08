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

verify: lint type test reports standalone

clean:
	rm -rf .pytest_cache .ruff_cache .mypy_cache reports/generated
	find . -type d -name __pycache__ -prune -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
