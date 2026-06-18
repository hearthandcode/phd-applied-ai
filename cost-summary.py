#!/usr/bin/env python3
"""Generate a cost summary markdown from the CSV log."""
import csv, os
from collections import defaultdict

LOG = os.path.expanduser("~/devel/hearthandcode/internal/hearthandcode-hub/cost-tracking/usage.csv")

def generate():
    if not os.path.exists(LOG):
        return "# Cost Tracking\n\nNo cost data yet."
    modules = defaultdict(list)
    with open(LOG) as f:
        reader = csv.DictReader(f)
        for row in reader:
            modules[row["module"]].append(row)
    lines = ["# Cost Tracking\n", "| Module | Sections | Total Cost | Calls |", "|---|---|---|---|"]
    total = 0.0
    for mod in sorted(modules):
        rows = modules[mod]
        cost = sum(float(r["total_cost"]) for r in rows)
        total += cost
        secs = ", ".join(sorted(set(r["section"] for r in rows)))
        lines.append(f"| {mod} | {secs} | ${cost:.4f} | {len(rows)} |")
    lines.append(f"\n**Grand Total: ${total:.4f}**\n")
    return "\n".join(lines)

if __name__ == "__main__":
    print(generate())
