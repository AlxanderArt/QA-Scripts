# QA Scripts

[![QA Scripts CI](https://github.com/AlxanderArt/QA-Scripts/actions/workflows/qa-ci.yml/badge.svg)](https://github.com/AlxanderArt/QA-Scripts/actions/workflows/qa-ci.yml)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![QA/SDET](https://img.shields.io/badge/QA%2FSDET-Automation-green)
![Playwright](https://img.shields.io/badge/Playwright-real%20browser%20smoke-45ba4b)

A practical QA/SDET automation portfolio repository with 10 runnable scripts covering API testing, Postman-style collection execution, Selenium/POM structure, Playwright real-browser smoke plus regression planning, BDD/ATDD acceptance criteria, SQL validation, CI quality gates, defect lifecycle reporting, deterministic AI-assisted test generation, and service virtualization.

**Positioning:** QA Automation / SDET / AI-assisted Quality Engineering.  
**No secrets. No paid APIs. All demo data is synthetic.**

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium
make verify
```

## Design standard

The numbered folders are recruiter-friendly script examples. Shared, reusable logic lives in `src/qa_scripts/` so the repo demonstrates maintainable SDET architecture instead of one-off scripts. CI runs linting, type-checking, all pytest tests, real Playwright browser smoke, JUnit/HTML report generation, and standalone CLI-style scripts.

## The 10 QA scripts

| # | Script | Demonstrates | Command |
|---|---|---|---|
| 01 | API Contract Tests | pytest, API contracts, positive/negative paths | `pytest scripts/01_api_contract_tests -q` |
| 02 | Postman Collection Runner | Postman/Newman-style API checks in Python | `python scripts/02_postman_collection_runner/run_collection.py` |
| 03 | Selenium POM Smoke | Page Object Model, locator strategy, smoke assertions | `pytest scripts/03_selenium_pom_smoke -q` |
| 04 | Playwright Regression | Real Chromium smoke + cross-browser regression case modeling | `pytest scripts/04_playwright_cross_browser_regression -q` |
| 05 | BDD/ATDD Acceptance Tests | Gherkin scenarios, acceptance criteria validation | `pytest scripts/05_bdd_acceptance_tests -q` |
| 06 | SQL Data Validation | SQLite validation, integrity checks | `python scripts/06_sql_data_validation/sql_validation.py` |
| 07 | CI Quality Gate | Test result aggregation and pass/fail gate | `python scripts/07_ci_quality_gate/quality_gate.py reports/sample_outputs/test-results.json` |
| 08 | Defect Lifecycle Reporter | Bug triage, severity, RCA-ready Markdown reports | `python scripts/08_defect_lifecycle_reporter/defect_reporter.py` |
| 09 | AI-Assisted Test Case Generator | Deterministic AI-QE style test ideas, no API keys | `python scripts/09_ai_assisted_test_case_generator/generate_test_cases.py` |
| 10 | Mock Service Virtualization | Service stubs/mocks for integration testing | `pytest scripts/10_mock_service_virtualization -q` |

## Portfolio coverage

See [`docs/recruiter_map.md`](docs/recruiter_map.md) and [`docs/test_strategy.md`](docs/test_strategy.md).

## Full verification workflow

```bash
ruff check .
mypy src apps scripts
pytest -q
pytest -q --junitxml=reports/generated/junit.xml --html=reports/generated/report.html --self-contained-html
python scripts/02_postman_collection_runner/run_collection.py
python scripts/06_sql_data_validation/sql_validation.py
python scripts/07_ci_quality_gate/quality_gate.py reports/sample_outputs/test-results.json
python scripts/08_defect_lifecycle_reporter/defect_reporter.py
python scripts/09_ai_assisted_test_case_generator/generate_test_cases.py
```

Or run the same local gate through Make:

```bash
make verify
```

Generated files, caches, virtual environments, and local environment files are ignored by git.
