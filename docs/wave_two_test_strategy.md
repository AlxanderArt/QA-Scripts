# Wave Two Test Strategy

Wave Two extends QA Scripts beyond baseline automation into senior SDET release signals. See the root [`README.md`](../README.md#wave-two-10-additional-qasdet-scripts) for the runnable command table.

| Area | Risk covered |
|---|---|
| Accessibility audit | Users blocked by missing labels, roles, and live status feedback |
| Visual regression | Unexpected UI snapshot drift |
| Performance budget | Latency, error-rate, and bundle-size release regression |
| Log anomaly scanning | Runtime errors, retries, timeouts, and exceptions |
| Flaky test detection | Unstable automation that can hide real defects |
| Test data factory | Non-repeatable setup data and environment pollution |
| Risk prioritization | Low-value test ordering during constrained regression windows |
| Release readiness | Missing go/no-go ownership or rollback readiness |
| Contract drift | Consumer-breaking schema mismatches |
| Synthetic monitoring | Post-deploy status and latency regression |

All examples use deterministic data and local-only execution so they are safe for public portfolio review.
