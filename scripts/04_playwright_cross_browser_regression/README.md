# 04 Playwright Cross-Browser Regression Suite

This example now includes two layers:

1. **Real Playwright Chromium smoke** — launches a real browser against synthetic in-memory HTML, fills a login form, and asserts the status text.
2. **Regression matrix planning** — models Chromium/Firefox/WebKit coverage for login/search/checkout flows.

## Run

```bash
python -m playwright install chromium
pytest scripts/04_playwright_cross_browser_regression -q
```

## Why this matters

A real SDET suite should prove browser automation can execute in CI, while also documenting the planned cross-browser regression matrix a company would expand for production.
