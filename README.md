# QA Scripts

A practical QA/SDET automation portfolio repository with 10 runnable scripts covering API testing, Postman-style collection execution, Selenium/POM structure, Playwright-style regression planning, BDD acceptance criteria, SQL validation, CI quality gates, defect lifecycle reporting, deterministic AI-assisted test generation, and service virtualization.

**Positioning:** QA Automation / SDET / AI-assisted Quality Engineering.  
**No secrets. No paid APIs. All demo data is synthetic.**

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
ruff check .
pytest -q
```

## Design standard

The numbered folders are recruiter-friendly script examples. Shared, reusable logic lives in `src/qa_scripts/` so the repo demonstrates maintainable SDET architecture instead of one-off scripts. CI runs linting, all pytest tests, and the standalone CLI-style scripts.

## The 10 QA scripts

| # | Script | Demonstrates | Command |
|---|---|---|---|
| 01 | API Contract Tests | pytest, API contracts, positive/negative paths | `pytest scripts/01_api_contract_tests -q` |
| 02 | Postman Collection Runner | Postman/Newman-style API checks in Python | `python scripts/02_postman_collection_runner/run_collection.py` |
| 03 | Selenium POM Smoke | Page Object Model, locator strategy, smoke assertions | `pytest scripts/03_selenium_pom_smoke -q` |
| 04 | Playwright Regression | Cross-browser regression case modeling | `pytest scripts/04_playwright_cross_browser_regression -q` |
| 05 | BDD Acceptance Tests | Gherkin scenarios, acceptance criteria validation | `pytest scripts/05_bdd_acceptance_tests -q` |
| 06 | SQL Data Validation | SQLite validation, integrity checks | `python scripts/06_sql_data_validation/sql_validation.py` |
| 07 | CI Quality Gate | Test result aggregation and pass/fail gate | `python scripts/07_ci_quality_gate/quality_gate.py reports/sample_outputs/test-results.json` |
| 08 | Defect Lifecycle Reporter | Bug triage, severity, RCA-ready Markdown reports | `python scripts/08_defect_lifecycle_reporter/defect_reporter.py` |
| 09 | AI-Assisted Test Case Generator | Deterministic AI-QE style test ideas, no API keys | `python scripts/09_ai_assisted_test_case_generator/generate_test_cases.py` |
| 10 | Mock Service Virtualization | Service stubs/mocks for integration testing | `pytest scripts/10_mock_service_virtualization -q` |

## Portfolio coverage

See [`docs/recruiter_map.md`](docs/recruiter_map.md) and [`docs/test_strategy.md`](docs/test_strategy.md).
