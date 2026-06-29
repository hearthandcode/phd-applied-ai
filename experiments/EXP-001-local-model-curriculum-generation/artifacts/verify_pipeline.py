#!/usr/bin/env python3
"""
Layered verification pipeline (Chain-of-Verification, local models) — distinct from MoA.

  GENERATE (already done) -> draft
  VERIFY LAYER:
    - code        (DETERMINISTIC: execute every python block)
    - math        (model: check equations/definitions/derivations vs MIT 18.06)
    - consistency (model: do examples match their own definitions? dims correct?)
    - flow        (model: do concepts/examples build without unexplained leaps?)
  REVISE (model: draft + all findings -> corrected draft)
  RE-VERIFY code on the corrected draft to confirm the fix.

Usage: python3 verify_pipeline.py <draft.md>
"""
import re, sys, json, time, subprocess, tempfile, pathlib, urllib.request

DESKTOP = "http://100.91.68.54:11434"
VERIFIER_MODEL = "deepseek-r1:14b"   # fast reasoning model for verification + revision
OUTDIR = pathlib.Path(__file__).parent / "comparison"

def call(model, prompt, endpoint=DESKTOP, timeout=1200):
    body = json.dumps({"model": model, "prompt": prompt, "stream": False,
                       "options": {"num_ctx": 8192}}).encode()
    req = urllib.request.Request(endpoint + "/api/generate", data=body,
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        d = json.loads(r.read())
    resp = d.get("response", "")
    return resp.split("</think>", 1)[1].strip() if "</think>" in resp else resp.strip()

def verify_code(text):
    blocks = re.findall(r"```python\n(.*?)```", text, re.DOTALL)
    findings = []
    for i, code in enumerate(blocks, 1):
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
            f.write(code); path = f.name
        r = subprocess.run([sys.executable, path], capture_output=True, text=True, timeout=30)
        if r.returncode != 0:
            err = r.stderr.strip().splitlines()[-1] if r.stderr.strip() else "non-zero exit"
            findings.append(f"CODE BLOCK {i} FAILS: {err}")
    return findings, len(blocks)

ASPECTS = {
    "math": "You are a MATHEMATICS verifier. Check EVERY equation, definition, and derivation in the "
            "curriculum section below for correctness against standard linear algebra (MIT 18.06). Flag "
            "incomplete definitions (e.g. a vector space defined by closure alone, omitting the 8 axioms). "
            "Output a numbered list of concrete errors with location + correction. If none, output exactly 'NONE'.",
    "consistency": "You are a CONSISTENCY verifier. Check that every example and cross-reference is internally "
            "consistent: does a matrix claimed to represent a map have the correct dimensions and entries? Do "
            "examples match the definitions they illustrate? Output a numbered list of inconsistencies with "
            "location + correction. If none, output exactly 'NONE'.",
    "flow": "You are a PEDAGOGICAL-FLOW verifier. Check that concepts build on each other without unexplained "
            "leaps, that each worked example follows logically, and that nothing is used before it is introduced. "
            "Output a numbered list of flow gaps. If none, output exactly 'NONE'.",
}

def log(m):
    print(m, flush=True)
    with open(OUTDIR / "verify.log", "a") as f: f.write(m + "\n")

def run(draft_path):
    draft = pathlib.Path(draft_path).read_text()
    name = pathlib.Path(draft_path).stem
    log(f"=== verify pipeline on {name} | {time.strftime('%H:%M:%S')} ===")

    code_findings, nblocks = verify_code(draft)
    log(f"[code] {len(code_findings)}/{nblocks} blocks broken: {code_findings}")

    aspect_findings = {"code (deterministic)": code_findings or ["NONE"]}
    for asp, instr in ASPECTS.items():
        log(f"[{asp}] verifying ...")
        out = call(VERIFIER_MODEL, f"{instr}\n\n=== SECTION ===\n{draft}")
        aspect_findings[asp] = [out]
        log(f"[{asp}] -> {out[:200].replace(chr(10),' ')}")

    # assemble findings report
    report = f"# Verification report — {name}\n\n"
    for asp, items in aspect_findings.items():
        report += f"## {asp}\n" + "\n".join(f"- {x}" for x in items) + "\n\n"
    (OUTDIR / f"{name}__VERIFY-REPORT.md").write_text(report)

    # revise
    findings_text = "\n".join(f"[{asp}] " + " | ".join(items) for asp, items in aspect_findings.items())
    rev_prompt = ("You are a REVISER. Below is a curriculum-section draft and verifier findings (code "
                  "execution, math, consistency, flow). Produce a corrected version that fixes ALL identified "
                  "issues while preserving the structure and pedagogical style. CRITICAL: every python code "
                  "block must run correctly (fix any dimension mismatches), every definition must be complete "
                  "and correct, and every example must be internally consistent. Output ONLY the corrected "
                  f"Markdown document.\n\n=== FINDINGS ===\n{findings_text}\n\n=== DRAFT ===\n{draft}")
    log("[revise] producing corrected draft ...")
    corrected = call(VERIFIER_MODEL, rev_prompt, timeout=1800)
    (OUTDIR / f"{name}__VERIFIED.md").write_text(corrected)

    # re-verify code on corrected
    code2, n2 = verify_code(corrected)
    log(f"[re-verify code] {len(code2)}/{n2} broken after revision: {code2}")
    log(f"=== done {time.strftime('%H:%M:%S')} | code fixed: {len(code_findings)}->{len(code2)} ===")

if __name__ == "__main__":
    run(sys.argv[1])
