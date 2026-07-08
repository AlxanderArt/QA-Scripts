# Risk-Based Test Prioritization

## What this demonstrates

Prioritize test execution based on impact, change frequency, and defect history.

## When a company would use it

Use this when QA/SDET teams need a focused automation signal beyond basic pass/fail tests. It helps expose release risk earlier and makes the result readable in CI.

## Local command

```bash
python scripts/17_risk_based_prioritization/prioritize_risks.py
pytest scripts/17_risk_based_prioritization -q
```

## Expected output

The standalone command prints deterministic synthetic output and exits successfully when the demo check passes.

## Production version

A production version would connect to the application under test, CI artifacts, logs, monitoring data, or schema registry while preserving the same validated core logic.
