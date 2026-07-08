# Log Anomaly Scanner

## What this demonstrates

Observability-oriented scan for errors, timeouts, retries, and exceptions.

## When a company would use it

Use this when QA/SDET teams need a focused automation signal beyond basic pass/fail tests. It helps expose release risk earlier and makes the result readable in CI.

## Local command

```bash
python scripts/14_log_anomaly_scanner/scan_logs.py
pytest scripts/14_log_anomaly_scanner -q
```

## Expected output

The standalone command prints deterministic synthetic output and exits successfully when the demo check passes.

## Production version

A production version would connect to the application under test, CI artifacts, logs, monitoring data, or schema registry while preserving the same validated core logic.
