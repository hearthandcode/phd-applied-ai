#!/usr/bin/env python3
"""
Curriculum at a Glance Generator
================================
Generates a human-readable markdown dashboard from the sync layer JSON.
Outputs to curriculum-at-a-glance.md for quick reference.
"""

import json
import subprocess
import sys
from pathlib import Path

SYNC_LAYER_SCRIPT = Path(__file__).parent / "sync-layer.py"
OUTPUT_FILE = Path("/workspace/phd/curriculum-at-a-glance.md")


def run_sync_layer() -> dict:
    """Run sync-layer.py and return parsed JSON."""
    result = subprocess.run([sys.executable, str(SYNC_LAYER_SCRIPT)], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running sync-layer.py: {result.stderr}", file=sys.stderr)
        sys.exit(1)
    return json.loads(result.stdout)


def format_hours(hours: float) -> str:
    """Format hours for display."""
    if hours >= 1000:
        return f"{hours/1000:.1f}k"
    return f"{hours:.1f}"


def generate_markdown(data: dict) -> str:
    """Generate markdown from sync layer data."""
    lines = []
    
    # Header
    lines.append("# Curriculum at a Glance")
    lines.append("")
    lines.append(f"*Generated: {data['generated_at']}*")
    lines.append("")
    
    # Overall summary
    ov = data["overall"]
    lines.append("## Overall Progress")
    lines.append("")
    lines.append(f"- **Par hours:** {format_hours(ov['total_par_hours'])} | **Actual:** {format_hours(ov['total_actual_hours'])}")
    lines.append(f"- **Modules:** {ov['modules_complete']}/{ov['total_modules']} complete · {ov['modules_in_progress']} in progress · {ov['total_modules'] - ov['modules_started']} not started")
    lines.append(f"- **Completion:** {ov['completion_pct']}%")
    lines.append("")
    
    # Next action
    if data["next_action"]:
        na = data["next_action"]
        lines.append("## Next Action")
        lines.append("")
        lines.append(f"> Continue **{na['module']}** — {na['title']}")
        lines.append(f"> {na['actual_hours']:.1f}/{na['par_hours']:.0f} hrs · {na['remaining_hours']:.1f} hrs remaining to par · competency level {na['competency']}")
        lines.append("")
    
    # Phase breakdown
    lines.append("## By Phase")
    lines.append("")
    
    for phase_num in range(6):
        phase_key = str(phase_num)
        if phase_key not in data["phases"]:
            continue
        p = data["phases"][phase_key]
        lines.append(f"### Phase {phase_num} — {p['name']}")
        lines.append("")
        lines.append(f"*{p['short_name']} · {p['module_count']} modules · {format_hours(p['par_hours'])} par hrs*")
        lines.append("")
        lines.append("| Module | Title | Par | Actual | Comp | Status |")
        lines.append("|--------|-------|-----|--------|------|--------|")
        
        for mid in sorted(p["modules"]):
            m = data["modules"].get(mid, {})
            if not m:
                continue
            comp = m.get("competency", 0)
            status = m.get("status", "not started")
            # Add visual indicator
            if comp >= 3:
                status_disp = "✅ complete"
            elif m.get("actual_hours", 0) > 0:
                status_disp = "🔄 in-progress"
            else:
                status_disp = "⏳ not started"
            
            lines.append(f"| {mid} | {m.get('title', '')} | {m.get('par_hours', 0):.0f} | {m.get('actual_hours', 0):.1f} | {comp} | {status_disp} |")
        
        lines.append(f"| **Phase total** | | {p['par_hours']:.0f} | {p['actual_hours']:.1f} | — | {p['complete']}/{p['started']} complete |")
        lines.append("")
    
    # Research Questions
    lines.append("## Research Questions Progress")
    lines.append("")
    
    for rq_id in ["RQ1", "RQ2", "RQ3", "RQ4", "RQ5"]:
        rq = data["research_questions"][rq_id]
        lines.append(f"### {rq_id} — {rq['title']}")
        lines.append("")
        lines.append(f"*{rq['actual_hours']:.1f}/{rq['par_hours']:.0f} hrs · {rq['started']}/{rq['total']} started · {rq['complete']} complete*")
        lines.append("")
        
        for mid in rq["modules"]:
            m = data["modules"].get(mid, {})
            if not m:
                continue
            comp = m.get("competency", 0)
            if comp >= 3:
                badge = "✅"
            elif m.get("actual_hours", 0) > 0:
                badge = "🔄"
            else:
                badge = "⏳"
            lines.append(f"- {badge} **{mid}** {m.get('title', '')} — {m.get('actual_hours', 0):.1f}/{m.get('par_hours', 0):.0f} hrs · comp {comp}")
        lines.append("")
    
    # Active modules detail
    if data["active_modules"]:
        lines.append("## Active Modules Detail")
        lines.append("")
        
        for mid in sorted(data["active_modules"]):
            m = data["modules"][mid]
            audit = m.get("audit", {})
            lines.append(f"### {mid} — {m['title']} (Phase {m['phase']})")
            lines.append("")
            lines.append(f"- **Progress:** {m['actual_hours']:.1f}/{m['par_hours']:.0f} hrs ({((m['actual_hours']/m['par_hours'])*100):.0f}% of par)")
            lines.append(f"- **Competency:** {m['competency']}/5 · Status: {m['status']}")
            lines.append(f"- **Sessions:** {audit.get('session_count', 0)} · Last updated: {audit.get('last_updated', 'unknown')}")
            lines.append(f"- **Prerequisites:** {', '.join(m.get('prerequisites', [])) or 'none'}")
            lines.append("")
    
    # Recent sessions
    if data["recent_sessions"]:
        lines.append("## Recent Sessions")
        lines.append("")
        lines.append("| Date | Session ID | Module | Hours | Energy | Focus |")
        lines.append("|------|------------|--------|-------|--------|-------|")
        for s in data["recent_sessions"]:
            lines.append(f"| {s['date']} | {s['session_id']} | {s['module']} | {s['hours']:.1f} | {s['energy']} | {s['focus']} |")
        lines.append("")
    
    # Footer
    lines.append("---")
    lines.append("")
    lines.append(f"*Total sessions logged: {data['total_sessions']}*")
    lines.append("*Run `python3 sync-layer.py` to refresh the data source.*")
    
    return "\n".join(lines)


def main():
    data = run_sync_layer()
    markdown = generate_markdown(data)
    OUTPUT_FILE.write_text(markdown)
    print(f"Generated {OUTPUT_FILE}")


if __name__ == "__main__":
    main()