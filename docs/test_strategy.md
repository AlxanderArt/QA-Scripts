# Test Strategy

This repository demonstrates a layered QA strategy and a maintainable script architecture. Reusable logic lives under `src/qa_scripts/`; numbered script folders act as thin examples/entry points with local README files.

1. API contract tests validate payload shape, negative paths, duplicate protection, and resettable synthetic state.
2. Collection runner checks emulate Postman/Newman workflows without GUI dependency.
3. UI smoke tests show Page Object Model design.
4. Playwright smoke testing proves a real Chromium browser can execute in CI, while cross-browser regression planning maps critical flows across Chromium, Firefox, and WebKit.
5. BDD/ATDD acceptance tests tie automation to product language, acceptance criteria, and acceptance-test-driven development practices.
6. SQL validation catches data quality and integrity issues.
7. CI quality gate prevents releases when pass rate or severity thresholds fail.
8. Defect reporting creates RCA-ready issue documentation.
9. AI-assisted generation demonstrates deterministic test-idea expansion.
10. Mock services isolate third-party behavior for reliable integration tests.
