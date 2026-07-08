from pathlib import Path
DEFECT = {"id": "BUG-1042", "title": "Checkout total does not include tax after coupon removal", "severity": "High", "steps": ["Add item to cart", "Apply coupon", "Remove coupon", "Proceed to checkout"], "expected": "Tax is recalculated after coupon removal.", "actual": "Checkout shows stale tax value.", "root_cause_prompt": "Review cart state invalidation after coupon mutation."}

def render(defect=DEFECT):
    steps = "\n".join(f"{i+1}. {step}" for i, step in enumerate(defect["steps"]))
    return f"# {defect['id']} - {defect['title']}\n\n**Severity:** {defect['severity']}\n\n## Steps to Reproduce\n{steps}\n\n## Expected\n{defect['expected']}\n\n## Actual\n{defect['actual']}\n\n## RCA Prompt\n{defect['root_cause_prompt']}\n"

if __name__ == "__main__":
    out = Path("reports/generated/defect-BUG-1042.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render())
    print(out)
