#!/usr/bin/env python3
"""
Local-model M01 curriculum generation for the frontier-vs-local comparison (T24 x T13).

Generates an M01 section using the local two-node Ollama farm, in two configs:
  - single: phi4-reasoning:plus alone (desktop GPU)
  - moa:    Mixture-of-Agents — proposers [phi4-reasoning:plus (desktop),
            qwen3:30b-a3b (laptop), deepseek-r1:14b (desktop)] -> aggregator (phi4-reasoning:plus)

Outputs + a timing log are written to OUTDIR for comparison against the frontier baselines
(canonical theory/foundations + claude-generate/).

Usage:
  python3 gen_m01_local.py <section_key> [single|moa|both]
Section keys defined in SECTIONS below.
"""
import json, sys, time, urllib.request, pathlib

DESKTOP = "http://100.91.68.54:11434"   # aeternus GPU: phi4-reasoning:plus, deepseek-r1:14b
LAPTOP  = "http://localhost:11434"       # xanastros CPU: qwen3:30b-a3b
OUTDIR  = pathlib.Path(__file__).parent / "comparison"
OUTDIR.mkdir(exist_ok=True)

# Section specs (mirror the baseline frontmatter; artifact = foundations-primer | theory-section)
SECTIONS = {
    "found-01-primer": {
        "artifact": "foundations-primer", "calibration": "MIT 18.06 (Strang)",
        "section": "01 — Primer", "formalism_density": 0.4,
        "topic": "A ground-floor primer that warms up working memory before the formal "
                 "linear-algebra theory: vectors as objects, vector spaces and closure, basis & "
                 "dimension, linear maps, matrices as the spreadsheet form of a map, and rank-nullity.",
    },
    "found-04-linind": {
        "artifact": "foundations-primer", "calibration": "MIT 18.06 (Strang)",
        "section": "04 — Linear Independence & Basis", "formalism_density": 0.5,
        "topic": "Linear independence, spanning sets, basis, and dimension — why a basis must be "
                 "both spanning and independent, built from intuition to formal definition.",
    },
    "theory-03-eigen": {
        "artifact": "theory-section", "calibration": "MIT 18.06 (Strang), Lectures 21-24",
        "section": "03 — Eigendecomposition", "formalism_density": 0.7,
        "topic": "Eigenvalues, eigenvectors, diagonalization, the eigendecomposition A = Q Λ Q^-1, "
                 "when it exists, and its meaning for ML (PCA, spectral methods, stability).",
    },
    "theory-04-svd": {
        "artifact": "theory-section", "calibration": "MIT 18.06 (Strang), Lectures 29-30",
        "section": "04 — Singular Value Decomposition", "formalism_density": 0.7,
        "topic": "The SVD A = U Σ V^T, geometric meaning, relation to eigendecomposition, "
                 "low-rank approximation (Eckart-Young), and ML uses (PCA, compression, pseudoinverse).",
    },
}

DESIGN_RULES = """\
You are generating one section of a doctoral-level self-study linear-algebra module (M01) for a
single learner. Follow the Hearth & Code curriculum design rules EXACTLY — these baselines are
calibrated to {calibration}:

LEARNER PROFILE (L001): an experienced programmer with ADHD; working memory is precious and must be
protected. Tone: direct, warm, vivid; start from a programmer's existing intuitions; never make the
reader hold an unexplained symbol across a page break.

REQUIRED STRUCTURE & RULES:
1. YAML frontmatter: module: M01, title: "Linear Algebra for ML", artifact: {artifact},
   section: "{section}", calibration: "{calibration}", formalism_density: {formalism_density},
   status: draft, learner_id: L001
2. CONCEPTUAL BRIDGE FIRST: before any formal definition, give an intuitive bridge in plain language
   (a second, denser bridge pass for the hardest part). THEN state the formal definition.
3. START FROM COMFORT: anchor new ideas in things a programmer already knows (spreadsheets, arrays, loops).
4. CONCRETE WORKED EXAMPLE: include at least one fully worked numerical example with explicit steps.
5. SYMBOL DISCIPLINE: every symbol is defined in the sentence it appears; provide a symbol reference
   table if multiple new symbols are introduced.
6. ML PAYOFF: a section explaining why this matters for machine learning, with concrete examples.
7. TIERED MEMORY SUMMARY: a "CARRY (memorize, max 7) / RECONSTRUCT (re-derive) / LOOKUP (never memorize)" summary.
8. COMPUTATIONAL EXERCISE: at least one small NumPy/SymPy exercise the learner can run.
9. ACCURACY IS NON-NEGOTIABLE: every definition, theorem, and derivation must be mathematically
   correct and verifiable against {calibration}. Do NOT invent theorems or misstate conditions.
   If a result has preconditions (e.g. diagonalizability), state them precisely.
10. End with an "explain-out-loud check" prompt.

TOPIC TO COVER:
{topic}

Write the complete section now as a single Markdown document (including the YAML frontmatter).
Output ONLY the Markdown document.
"""

# phi4-reasoning:plus is slow (spills + heavy thinking) → generous timeout.
TIMEOUTS = {"phi4-reasoning:plus": 2400, "qwen3:30b-a3b": 1500, "deepseek-r1:14b": 1200}

def build_prompt(spec):
    return DESIGN_RULES.format(**spec)

def call_ollama(endpoint, model, prompt, timeout=None):
    if timeout is None:
        timeout = TIMEOUTS.get(model, 1200)
    body = json.dumps({"model": model, "prompt": prompt, "stream": False,
                       "options": {"num_ctx": 8192}}).encode()
    req = urllib.request.Request(endpoint + "/api/generate", data=body,
                                 headers={"Content-Type": "application/json"})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as r:
        d = json.loads(r.read())
    dt = time.time() - t0
    resp = d.get("response", "")
    # strip <think> blocks for the saved artifact (keep raw separately)
    clean = resp.split("</think>", 1)[1] if "</think>" in resp else resp
    return {"raw": resp, "clean": clean.strip(), "wall_s": round(dt, 1),
            "eval_count": d.get("eval_count", 0),
            "tok_s": round(d.get("eval_count", 0) / (d.get("eval_duration", 1) / 1e9), 1)}

def log(msg):
    print(msg, flush=True)
    with open(OUTDIR / "run.log", "a") as f:
        f.write(msg + "\n")

MODEL_EP = {"phi4-reasoning:plus": DESKTOP, "deepseek-r1:14b": DESKTOP, "qwen3:30b-a3b": LAPTOP}

def gen_single(key, spec, model="phi4-reasoning:plus"):
    ep = MODEL_EP[model]
    tag = model.replace(":", "_").replace("/", "_")
    log(f"[{key}] SINGLE {model} @ {ep} ...")
    r = call_ollama(ep, model, build_prompt(spec))
    (OUTDIR / f"{key}__single-{tag}.md").write_text(r["clean"])
    log(f"[{key}] single {model} done: {r['wall_s']}s, {r['eval_count']} tok, {r['tok_s']} tok/s")
    return r

def gen_moa(key, spec):
    prompt = build_prompt(spec)
    proposers = [("phi4-reasoning:plus", DESKTOP), ("qwen3:30b-a3b", LAPTOP),
                 ("deepseek-r1:14b", DESKTOP)]
    drafts = []
    for model, ep in proposers:
        log(f"[{key}] MoA proposer {model} @ {ep} ...")
        r = call_ollama(ep, model, prompt)
        (OUTDIR / f"{key}__moa-proposer-{model.replace(':','_').replace('/','_')}.md").write_text(r["clean"])
        log(f"[{key}]   {model}: {r['wall_s']}s, {r['tok_s']} tok/s")
        drafts.append((model, r["clean"]))
    agg = ("You are the aggregator in a Mixture-of-Agents pipeline. Below are independent drafts of "
           "the SAME curriculum section from different models. Synthesize the single best version: keep "
           "the clearest explanations, MERGE the strongest worked examples, and CRITICALLY CORRECT any "
           "mathematical error, imprecise condition, or hallucinated claim you find in any draft. The "
           "final document must follow the same design rules and be mathematically correct.\n\n"
           "ORIGINAL TASK:\n" + prompt + "\n\n")
    for i, (m, d) in enumerate(drafts, 1):
        agg += f"\n===== DRAFT {i} (from {m}) =====\n{d}\n"
    agg += "\nNow output ONLY the final synthesized Markdown document."
    log(f"[{key}] MoA aggregator phi4-reasoning:plus ...")
    r = call_ollama(DESKTOP, "phi4-reasoning:plus", agg, timeout=1200)
    (OUTDIR / f"{key}__moa-final.md").write_text(r["clean"])
    log(f"[{key}] MoA final done: {r['wall_s']}s, {r['eval_count']} tok")
    return r

if __name__ == "__main__":
    key = sys.argv[1] if len(sys.argv) > 1 else "found-01-primer"
    mode = sys.argv[2] if len(sys.argv) > 2 else "both"
    # optional 3rd arg = single-model override (for fast validation), e.g. deepseek-r1:14b
    single_model = sys.argv[3] if len(sys.argv) > 3 else "phi4-reasoning:plus"
    spec = SECTIONS[key]
    log(f"=== {key} | mode={mode} | single={single_model} | {time.strftime('%H:%M:%S')} ===")
    if mode in ("single", "both"):
        gen_single(key, spec, single_model)
    if mode in ("moa", "both"):
        gen_moa(key, spec)
    log(f"=== {key} complete {time.strftime('%H:%M:%S')} ===")
