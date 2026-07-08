import json
REQUIREMENT = "Users can reset a forgotten password using a verified email address."
HEURISTICS = ["happy_path", "invalid_input", "expired_token", "rate_limit", "audit_logging", "accessibility"]

def generate(requirement=REQUIREMENT):
    return [{"id": f"TC-{i+1:03d}", "heuristic": h, "requirement": requirement, "expected": f"Validate {h.replace('_', ' ')} behavior."} for i, h in enumerate(HEURISTICS)]

if __name__ == "__main__":
    print(json.dumps(generate(), indent=2))
