#!/usr/bin/env python3
"""Deterministic code verifier: extract python blocks from a markdown file and execute each."""
import re, sys, subprocess, tempfile, pathlib

def verify(md_path):
    text = pathlib.Path(md_path).read_text()
    blocks = re.findall(r"```python\n(.*?)```", text, re.DOTALL)
    print(f"Found {len(blocks)} python block(s) in {pathlib.Path(md_path).name}\n")
    issues = 0
    for i, code in enumerate(blocks, 1):
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
            f.write(code); path = f.name
        r = subprocess.run([sys.executable, path], capture_output=True, text=True, timeout=30)
        if r.returncode != 0:
            issues += 1
            err = r.stderr.strip().splitlines()[-1] if r.stderr.strip() else "non-zero exit"
            print(f"  ❌ BLOCK {i}: FAILS — {err}")
        else:
            print(f"  ✅ BLOCK {i}: runs clean")
            if r.stdout.strip():
                print("     output:", r.stdout.strip().replace(chr(10), " | ")[:120])
    print(f"\nVERDICT: {issues} broken / {len(blocks)} blocks")
    return issues

if __name__ == "__main__":
    verify(sys.argv[1])
