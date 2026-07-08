# QA Scripts

[![QA Scripts CI](https://github.com/AlxanderArt/QA-Scripts/actions/workflows/qa-ci.yml/badge.svg)](https://github.com/AlxanderArt/QA-Scripts/actions/workflows/qa-ci.yml)
![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![QA/SDET](https://img.shields.io/badge/QA%2FSDET-Automation-green)
![Playwright](https://img.shields.io/badge/Playwright-real%20browser%20smoke-45ba4b)

A practical QA/SDET automation portfolio repository with 20 runnable scripts across two waves. Wave One covers API testing, Postman-style collection execution, Selenium/POM structure, Playwright real-browser smoke plus regression planning, BDD/ATDD acceptance criteria, SQL validation, CI quality gates, defect lifecycle reporting, deterministic AI-assisted test generation, and service virtualization. Wave Two expands into accessibility, visual regression, performance budgets, observability, flake analysis, test data, risk prioritization, release readiness, contract drift, and synthetic monitoring.

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

## Tell me about this project

I built **QA Scripts** to demonstrate my ability to create maintainable QA automation, not just isolated test cases.

The project has 20 runnable QA/SDET examples across two waves. Wave One includes API contract tests, a Postman-style collection runner, SQL validation, a CI quality gate, a defect reporter, mock service virtualization, deterministic AI-assisted test-case generation, and a real Playwright Chromium smoke test. Wave Two extends the portfolio into accessibility auditing, visual regression snapshot checks, performance-budget validation, log anomaly scanning, flaky-test detection, deterministic test-data generation, risk-based test prioritization, release-readiness checks, contract-drift detection, and synthetic monitoring probes.

One thing I focused on was making it feel like a real automation framework. The reusable logic lives under `src/qa_scripts`, while the numbered script folders stay easy to understand for reviewers. I also added CI through GitHub Actions, with linting, type checking, pytest, JUnit XML, HTML reports, standalone script execution, and uploaded artifacts.

From a QA workflow perspective, the repo shows how I think through automation: define the risk, validate expected and negative paths, make failures readable, keep test data synthetic and repeatable, and enforce release confidence through a quality gate.

## Design standard

The numbered folders are recruiter-friendly script examples. Shared, reusable logic lives in `src/qa_scripts/` so the repo demonstrates maintainable SDET architecture instead of one-off scripts. CI runs linting, type-checking, all pytest tests, real Playwright browser smoke, JUnit/HTML report generation, and standalone CLI-style scripts.

## Wave One: the first 10 QA scripts

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


## Wave Two: 10 additional QA/SDET scripts

| # | Script | Demonstrates | Command |
|---|---|---|---|
| 11 | Accessibility Audit | Labels, roles, live-region checks | `python scripts/11_accessibility_audit/audit_accessibility.py` |
| 12 | Visual Regression Snapshot | Synthetic pixel diff and thresholding | `python scripts/12_visual_regression_snapshot/compare_visual_snapshot.py` |
| 13 | Performance Budget Check | Latency, error-rate, and bundle budgets | `python scripts/13_performance_budget_check/check_performance_budget.py` |
| 14 | Log Anomaly Scanner | Observability signal detection | `python scripts/14_log_anomaly_scanner/scan_logs.py` |
| 15 | Flaky Test Detector | Historical pass/fail instability analysis | `python scripts/15_flaky_test_detector/detect_flakes.py` |
| 16 | Test Data Factory | Deterministic synthetic test data | `python scripts/16_test_data_factory/generate_test_data.py` |
| 17 | Risk-Based Prioritization | Test execution priority by feature risk | `python scripts/17_risk_based_prioritization/prioritize_risks.py` |
| 18 | Release Readiness Checklist | Go/no-go release blocker analysis | `python scripts/18_release_readiness_checklist/check_release_readiness.py` |
| 19 | Contract Drift Detector | Expected vs actual schema drift | `python scripts/19_contract_drift_detector/detect_contract_drift.py` |
| 20 | Synthetic Monitoring Probe | Status/latency health checks | `python scripts/20_synthetic_monitoring_probe/run_synthetic_monitor.py` |

## Portfolio coverage

See [`docs/recruiter_map.md`](docs/recruiter_map.md), [`docs/test_strategy.md`](docs/test_strategy.md), and [`docs/wave_two_test_strategy.md`](docs/wave_two_test_strategy.md).

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
```

Or run the same local gate through Make:

```bash
make verify
```

Generated files, caches, virtual environments, and local environment files are ignored by git.
