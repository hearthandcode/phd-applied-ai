#!/usr/bin/env python3
"""
PhD Curriculum Sync Layer
=========================
Single source of truth for curriculum state across all views.
Reads SCORECARD.md, AUDIT_LOG.md, curriculum/overview.md, curriculum/phase-map.md,
curriculum/prerequisites.md, and modules/MXX/audit.md files.
Produces machine-readable JSON for dashboards, CLI tools, and automation.
"""

import re
import json
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional

PHD_ROOT = Path("/workspace/phd")

# Module-to-phase mapping (authoritative)
PHASE_MODULES = {
    0: list(range(1, 7)),    # M01-M06
    1: list(range(7, 19)),   # M07-M18
    2: list(range(19, 29)),  # M19-M28
    3: list(range(29, 43)),  # M29-M42
    4: list(range(43, 62)),  # M43-M61
    5: list(range(62, 68)),  # M62-M67
}

PHASE_NAMES = [
    "Mathematical Foundations",
    "CS Fundamentals",
    "ML Foundations",
    "Advanced AI",
    "Specialized Research",
    "Thesis and Defense",
]

PHASE_SHORT_NAMES = [
    "Foundations",
    "CS Fundamentals",
    "ML Foundations",
    "Advanced AI",
    "Specialized Research",
    "Thesis",
]

RESEARCH_QUESTIONS = {
    "RQ1": "Adaptive Competency Modeling",
    "RQ2": "Pedagogy & Generative AI",
    "RQ3": "Personality, Virtue & Motivation",
    "RQ4": "Ethics & Governance at Scale",
    "RQ5": "Neurodiversity & AI-Mediated Learning",
}

RQ_MODULES = {
    "RQ1": ["M45", "M43", "M51"],
    "RQ2": ["M49", "M44", "M47"],
    "RQ3": ["M53", "M54", "M52", "M50"],
    "RQ4": ["M55", "M56", "M41"],
    "RQ5": ["M61", "M58", "M52"],
}


def parse_scorecard(content: str) -> Dict[str, Dict]:
    """Parse SCORECARD.md into module dict."""
    modules = {}
    current_phase = -1
    for line in content.split("\n"):
        pm = re.match(r"## Phase (\d)", line)
        if pm:
            current_phase = int(pm.group(1))
        # Phase 0-4 format: 6 columns (Module, Title, Par, Actual, Competency, Status)
        m = re.match(r"\|\s*(M\d{2})\s*\|\s*(.+?)\s*\|\s*(\d+)\s*\|\s*([\d.]+)\s*\|\s*(\d+)\s*\|\s*(.+?)\s*\|", line)
        if m:
            mod_id = m.group(1)
            modules[mod_id] = {
                "id": mod_id,
                "title": m.group(2).strip(),
                "par_hours": float(m.group(3)),
                "actual_hours": float(m.group(4)),
                "competency": int(m.group(5)),
                "status": m.group(6).strip(),
                "phase": current_phase if current_phase >= 0 else None,
            }
            continue
        # Phase 5 format: 5 columns (Module, Title, Par, Actual, Status) - no Competency
        m5 = re.match(r"\|\s*(M\d{2})\s*\|\s*(.+?)\s*\|\s*(\d+)\s*\|\s*([\d.]+)\s*\|\s*(.+?)\s*\|", line)
        if m5 and current_phase == 5:
            mod_id = m5.group(1)
            modules[mod_id] = {
                "id": mod_id,
                "title": m5.group(2).strip(),
                "par_hours": float(m5.group(3)),
                "actual_hours": float(m5.group(4)),
                "competency": 0,  # Phase 5 doesn't track competency
                "status": m5.group(5).strip(),
                "phase": 5,
            }
    return modules


def parse_audit_log(content: str) -> List[Dict]:
    """Parse AUDIT_LOG.md session index."""
    entries = []
    in_table = False
    for line in content.split("\n"):
        if line.startswith("| Date | Session ID"):
            in_table = True
            continue
        if in_table and line.startswith("|") and not line.startswith("|---"):
            parts = [p.strip() for p in line.split("|")[1:-1]]
            if len(parts) >= 5 and parts[0] != "—" and parts[0] != "":
                try:
                    hours = float(parts[3]) if parts[3].replace(".", "").isdigit() else 0
                except:
                    hours = 0
                entries.append({
                    "date": parts[0],
                    "session_id": parts[1],
                    "module": parts[2],
                    "hours": hours,
                    "energy": parts[4],
                    "focus": parts[5] if len(parts) > 5 else "",
                    "competency_changes": parts[6] if len(parts) > 6 else "",
                    "notes": parts[7] if len(parts) > 7 else "",
                })
    return entries


def read_module_audit(module_id: str) -> Dict:
    """Read a module's audit.md for detailed session data."""
    try:
        # Find the module directory
        modules_dir = PHD_ROOT / "modules"
        for d in modules_dir.iterdir():
            if d.is_dir() and d.name.startswith(module_id):
                audit_path = d / "audit.md"
                if audit_path.exists():
                    content = audit_path.read_text()
                    # Extract frontmatter
                    session_match = re.search(r"total_sessions:\s*(\d+)", content)
                    last_updated_match = re.search(r"updated:\s*([\d-]+)", content)
                    return {
                        "session_count": int(session_match.group(1)) if session_match else 0,
                        "last_updated": last_updated_match.group(1) if last_updated_match else "unknown"
                    }
    except Exception:
        pass
    return {"session_count": 0, "last_updated": "unknown"}


def parse_curriculum_overview(content: str) -> Dict[str, Dict]:
    """Parse curriculum/overview.md for module status."""
    modules = {}
    current_phase = -1
    for line in content.split("\n"):
        pm = re.match(r"## Phase (\d)", line)
        if pm:
            current_phase = int(pm.group(1))
        # Phase 0-4 format: 5 columns (ID, Title, Status, Competency, Blog)
        m = re.match(r"\|\s*(M\d{2})\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(\d+)\s*\|\s*(.+?)\s*\|", line)
        if m and m.group(1).startswith("M"):
            mod_id = m.group(1)
            modules[mod_id] = {
                "status": m.group(3).strip(),
                "competency": int(m.group(4)) if m.group(4).isdigit() else 0,
                "blog": m.group(5).strip() if m.group(5).strip() != "—" else None,
            }
            continue
        # Phase 5 format: 4 columns (ID, Title, Status, Notes)
        m5 = re.match(r"\|\s*(M\d{2})\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|", line)
        if m5 and m5.group(1).startswith("M") and current_phase == 5:
            mod_id = m5.group(1)
            modules[mod_id] = {
                "status": m5.group(3).strip(),
                "competency": 0,
                "blog": None,
            }
    return modules


def parse_phase_map(content: str) -> Dict:
    """Parse curriculum/phase-map.md for visual map."""
    # Extract phase structure from markdown
    phases = {}
    current_phase = -1
    for line in content.split("\n"):
        if line.startswith("## Phase"):
            # Extract phase letter
            match = re.match(r"## Phase ([A-D])", line)
            if match:
                phase_letter = match.group(1)
                phases[phase_letter] = {"title": line.replace("## Phase ", "").strip(), "modules": []}
                current_phase = phase_letter
        elif current_phase and line.strip().startswith("- M"):
            modules_in_line = re.findall(r"(M\d+)", line)
            for mod in modules_in_line:
                phases[current_phase]["modules"].append(mod)
    return phases


def parse_prerequisites(content: str) -> Dict[str, List[str]]:
    """Parse curriculum/prerequisites.md for dependency graph."""
    deps = {}
    for line in content.split("\n"):
        m = re.match(r"\|\s*(M\d{2})\s*\|\s*.+?\s*\|\s*\d\s*\|\s*(.+?)\s*\|", line)
        if m:
            mod_id = m.group(1)
            prereq_str = m.group(2).strip()
            if prereq_str == "—" or prereq_str == "":
                deps[mod_id] = []
            else:
                deps[mod_id] = [p.strip() for p in prereq_str.split(",")]
    return deps


def build_sync_layer() -> Dict[str, Any]:
    """Build the complete sync layer data structure."""
    
    # Read all source files
    scorecard_content = (PHD_ROOT / "SCORECARD.md").read_text()
    audit_log_content = (PHD_ROOT / "AUDIT_LOG.md").read_text()
    curriculum_overview_content = (PHD_ROOT / "curriculum" / "overview.md").read_text()
    phase_map_content = (PHD_ROOT / "curriculum" / "phase-map.md").read_text()
    prerequisites_content = (PHD_ROOT / "curriculum" / "prerequisites.md").read_text()
    
    # Parse all sources
    scorecard_modules = parse_scorecard(scorecard_content)
    audit_entries = parse_audit_log(audit_log_content)
    curriculum_modules = parse_curriculum_overview(curriculum_overview_content)
    phase_map = parse_phase_map(phase_map_content)
    prerequisites = parse_prerequisites(prerequisites_content)
    
    # Merge module data
    all_modules = {}
    for mod_id in scorecard_modules:
        all_modules[mod_id] = scorecard_modules[mod_id].copy()
        if mod_id in curriculum_modules:
            all_modules[mod_id].update(curriculum_modules[mod_id])
        all_modules[mod_id]["prerequisites"] = prerequisites.get(mod_id, [])
        all_modules[mod_id]["audit"] = read_module_audit(mod_id)
    
    # Compute phase summaries
    phase_summaries = {}
    for phase_num in range(6):
        phase_mods = {mid: m for mid, m in all_modules.items() if m.get("phase") == phase_num}
        if not phase_mods:
            continue
        phase_summaries[phase_num] = {
            "name": PHASE_NAMES[phase_num],
            "short_name": PHASE_SHORT_NAMES[phase_num],
            "modules": list(phase_mods.keys()),
            "module_count": len(phase_mods),
            "par_hours": sum(m["par_hours"] for m in phase_mods.values()),
            "actual_hours": sum(m["actual_hours"] for m in phase_mods.values()),
            "started": sum(1 for m in phase_mods.values() if m["actual_hours"] > 0),
            "complete": sum(1 for m in phase_mods.values() if m["competency"] >= 3),
            "in_progress": sum(1 for m in phase_mods.values() if m["actual_hours"] > 0 and m["competency"] < 3),
        }
    
    # Overall totals
    total_actual = sum(m["actual_hours"] for m in all_modules.values())
    total_par = sum(m["par_hours"] for m in all_modules.values())
    started = sum(1 for m in all_modules.values() if m["actual_hours"] > 0)
    complete = sum(1 for m in all_modules.values() if m["competency"] >= 3)
    in_progress = started - complete
    
    # Active modules
    active = {mid: m for mid, m in all_modules.items() if m["actual_hours"] > 0 and m["competency"] < 3}
    
    # Next action recommendation
    next_action = None
    if active:
        next_mid = sorted(active.keys())[0]
        m = active[next_mid]
        remaining = m["par_hours"] - m["actual_hours"]
        next_action = {
            "module": next_mid,
            "title": m["title"],
            "actual_hours": m["actual_hours"],
            "par_hours": m["par_hours"],
            "remaining_hours": round(remaining, 1),
            "competency": m["competency"],
        }
    
    # Research question progress
    rq_progress = {}
    for rq_id, rq_title in RESEARCH_QUESTIONS.items():
        rq_mods = RQ_MODULES.get(rq_id, [])
        rq_modules_data = {mid: all_modules.get(mid, {}) for mid in rq_mods}
        rq_actual = sum(m.get("actual_hours", 0) for m in rq_modules_data.values())
        rq_par = sum(m.get("par_hours", 0) for m in rq_modules_data.values())
        rq_complete = sum(1 for m in rq_modules_data.values() if m.get("competency", 0) >= 3)
        rq_started = sum(1 for m in rq_modules_data.values() if m.get("actual_hours", 0) > 0)
        rq_progress[rq_id] = {
            "title": rq_title,
            "modules": rq_mods,
            "par_hours": rq_par,
            "actual_hours": round(rq_actual, 1),
            "started": rq_started,
            "complete": rq_complete,
            "total": len(rq_mods),
        }
    
    # Build output
    return {
        "generated_at": datetime.now().isoformat(),
        "phd_root": str(PHD_ROOT),
        "schema_version": "1.0",
        "overall": {
            "total_par_hours": total_par,
            "total_actual_hours": round(total_actual, 1),
            "modules_started": started,
            "modules_complete": complete,
            "modules_in_progress": in_progress,
            "total_modules": len(all_modules),
            "completion_pct": round((complete / len(all_modules)) * 100, 1) if all_modules else 0,
        },
        "phases": phase_summaries,
        "modules": all_modules,
        "active_modules": list(active.keys()),
        "next_action": next_action,
        "research_questions": rq_progress,
        "recent_sessions": audit_entries[-10:] if audit_entries else [],
        "total_sessions": len(audit_entries),
    }


def main():
    """Main entry point - output JSON to stdout."""
    data = build_sync_layer()
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()