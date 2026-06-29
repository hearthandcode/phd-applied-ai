---
type: experiment-analysis
exp_id: EXP-001
section: "foundations/01-primer"
created: 2026-06-29
updated: 2026-06-29
status: in-progress
---

# EXP-001 — Gap Analysis (M01 foundations/01-primer)

Comparison of local generation strategies against the frontier baseline for the M01 foundations
primer. **Correctness is graded deterministically where possible (code execution); rigor/pedagogy/
profile-fit are model-/reviewer-judged.**

## Deterministic results (code execution — hallucination-free)

| Condition | Code blocks | Broken | Note |
|---|---|---|---|
| baseline (canonical `foundations/01-primer`) | 0 runnable python in primer | — | primer is prose; theory files hold code |
| single phi4-reasoning:plus | 1 | **0 ✅** | correct (R³ map example) |
| single deepseek-r1:14b (run A) | 1 | **1 ❌** | `ValueError: matmul size 2≠3` (2×3 matrix × len-2 vector) |
| MoA proposer phi4-reasoning:plus | 1 | 0 ✅ | |
| MoA proposer deepseek-r1:14b (run B) | 1 | **0 ✅** | *same model, different run — clean this time* |
| MoA proposer qwen3:30b-a3b | 1 | **1 ❌** | broken |
| **MoA final (aggregated)** | 1 | **0 ✅** | clean |
| **CoVe (verify→revise on deepseek run A)** | 1 | **0 ✅** | **1→0: reviser fixed the matmul error** |

**Headline deterministic finding:** correctness is **probabilistic per run** — deepseek-r1:14b produced
broken code in run A and clean code in run B *with identical inputs*. No single generation can be
trusted; verification is mandatory, not optional. phi4-reasoning:plus was clean in both its runs
(higher reliability, consistent with its benchmark lead).

## Quality grades (0–5; baseline = reference ceiling)

| Condition | Correctness | Rigor | Pedagogy | Profile-fit | Overall |
|---|---|---|---|---|---|
| **baseline (canonical)** | 5 | 5 | 5 | 5 | reference |
| single deepseek-r1:14b | 2 | 3 | 4 | 3 | broken code + false matrix↔map claim + closure-only def |
| single phi4-reasoning:plus | 4* | 4 | 2 | 2 | *correct content BUT **thinking/planning leaks into the document** ("Possibly I'll include…", "We need a worked example: I can take…"); 4366 words, bloated, needs heavy post-processing |
| **MoA final** | 4 | 3 | 3.5 | 3 | **B+ draft**: clean code, **no false matrix↔map claim**, correct rank-nullity; but closure-only vector-space def (omits 8 axioms), thinner (913 w), no symbol table, generic voice ("Happy learning!") |
| **CoVe (verify→revise on deepseek run A)** | **5** | **4.5** | 4 | 3 | **Repaired all 3 errors**: code 1→0 (deterministic), 8 axioms added, matrix↔map claim corrected (3×2). Started from the *worst* draft (broken+false) and ended *correct*. 1238→1413 w. Residual: voice/profile-fit still below baseline. |

### The decisive result (CoVe verifier catches, in its own words)
- **math verifier:** "omits several necessary axioms beyond closure" → reviser **added all 8 axioms**.
- **consistency verifier:** caught *both* errors precisely — (1) "multiplies a 2×3 matrix by a vector of
  length 2 ... change `x` to `[1, 2, 3]`"; (2) "the matrix A should be 3×2 to represent a linear map
  from R²→R³" (the false matrix↔map claim). → reviser corrected both.
- **code (deterministic):** 1 broken → **0 after revision**, re-executed to confirm.
- **flow verifier:** NONE (structure was sound).

\* phi4 correctness is on its *content*; its *output hygiene* is poor (thinking leakage) — a separate,
fixable problem (better stop-tokens / a strip pass / using phi4 as verifier not generator).

## Key qualitative findings

- **F-A (output hygiene):** phi4-reasoning:plus does not cleanly separate reasoning from output via
  `</think>`; its planning prose contaminates the document. → It is better deployed as a **verifier/
  aggregator** (where its rigor helps and a final synthesis pass produces clean prose) than as a raw
  **generator**. The faster, cleaner-output models (deepseek, qwen3:30b) are the better drafters.
- **F-B (MoA as normalizer + corrector):** the MoA aggregation step produced the cleanest, most
  presentable output of all conditions *and* avoided deepseek's two worst errors (broken code, false
  matrix↔map claim). MoA's benefit is therefore twofold: error-reduction *and* format normalization.
- **F-C (residual gaps even in MoA):** MoA still (1) reduced the vector-space definition to closure,
  omitting the 8 axioms; (2) ran thinner than the baseline (fewer/lighter worked examples, no symbol
  table); (3) lacked the baseline's distinctive ADHD-aware voice. These are **enrichment** gaps, not
  correctness errors — addressable by a verification/enrichment pass + a few-shot style exemplar.
- **F-D (the verification thesis, confirmed deterministically):** per-run correctness variance proves
  no single generation is trustworthy. The cheapest reliable guarantee is **executable** (run the
  code). This is the central design principle for the pipeline and for AI-generated curriculum generally.

## Implications

1. **Generator vs verifier split:** use deepseek-r1:14b / qwen3:30b-a3b as fast *generators* (clean
   output), phi4-reasoning:plus as a *verifier/aggregator* (rigor where it counts, clean synthesis).
2. **MoA is a good default** for a correct, clean first draft — but does not reach baseline rigor/voice
   alone; pair it with (3).
3. **Layered verification + enrichment is required** to close the residual gaps: deterministic code +
   SymPy checks, a completeness verifier (e.g. "are all required axioms present?"), and a profile-fit/
   voice pass anchored by a baseline few-shot exemplar.
4. Feeds `METHODOLOGY.md`: elevate Phase-3 Verification to an explicit layered stage; update Model
   Routing to the generator/verifier split above.

## Bottom line

**Local models + layered verification = trustworthy curriculum content.** No single local generation
is reliable (per-run correctness variance is real), but the pipeline **generate → layered-verify →
revise** took the *worst* draft (broken code + a false mathematical claim + an incomplete definition)
and produced a *correct, more complete* one — with the deterministic code check as a hallucination-free
backstop. The residual gap to the frontier baseline is no longer **correctness** (closed) but **voice/
richness** (profile-fit, worked-example density), which is an *enrichment* problem solvable with a
few-shot style exemplar + a completeness/voice verifier. This validates committing to the local
generate→verify→revise pipeline for curriculum generation, with a thin frontier seam for the residual.
