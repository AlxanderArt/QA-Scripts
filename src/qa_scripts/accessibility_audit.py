from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ElementCheck:
    selector: str
    passed: bool
    issue: str = ""


@dataclass(frozen=True)
class AccessibilityReport:
    passed: bool
    checks: tuple[ElementCheck, ...]

    @property
    def issues(self) -> tuple[str, ...]:
        return tuple(check.issue for check in self.checks if not check.passed)


def audit_login_markup(elements: dict[str, dict[str, str]]) -> AccessibilityReport:
    """Audit synthetic element metadata for common accessibility regressions."""
    checks = [
        ElementCheck("form", elements.get("form", {}).get("aria-label") == "Login form", "form needs aria-label"),
        ElementCheck("email", elements.get("email", {}).get("label") == "Email", "email input needs visible label"),
        ElementCheck("password", elements.get("password", {}).get("label") == "Password", "password input needs visible label"),
        ElementCheck("submit", elements.get("submit", {}).get("role") == "button", "submit needs button role"),
        ElementCheck("status", elements.get("status", {}).get("role") == "status", "status message needs live role"),
    ]
    return AccessibilityReport(all(check.passed for check in checks), tuple(checks))


def sample_accessible_login() -> dict[str, dict[str, str]]:
    return {
        "form": {"aria-label": "Login form"},
        "email": {"label": "Email"},
        "password": {"label": "Password"},
        "submit": {"role": "button"},
        "status": {"role": "status"},
    }
