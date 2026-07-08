BROWSERS = ["chromium", "firefox", "webkit"]
CRITICAL_FLOWS = ["login", "search", "checkout"]

def build_matrix():
    return [{"browser": browser, "flow": flow, "priority": "P0" if flow == "checkout" else "P1"} for browser in BROWSERS for flow in CRITICAL_FLOWS]
