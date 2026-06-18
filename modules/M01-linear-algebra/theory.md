---
type: module-theory-toc
schema_version: "1.0"
module_id: M01
module_title: "Linear Algebra for ML"
phase: 0
status: draft
learner_id: L001
calibration_target: "MIT 18.06 (Gilbert Strang)"
formalism_density: 0.4
---

# M01: Linear Algebra for ML

Calibration target: MIT 18.06 (Gilbert Strang) — doctoral depth with ML emphasis.

---

## How to Use This Module

Read the foundations primer first — it primes your working memory. Then read theory sections in order.

| Section | Core Idea | ML Application |
|---------|-----------|----------------|
| [01 Vector spaces](./theory/01-vector-spaces.md) | Add, scale, subspaces, rank-nullity | Parameter spaces, LoRA |
| [02 Inner products](./theory/02-inner-products.md) | Direction, angle, projection | Attention scores, cosine sim |
| [03 Eigendecomposition](./theory/03-eigendecomposition.md) | Fixed directions of symmetric maps | PCA, gradient stability |
| [04 SVD](./theory/04-singular-value-decomposition.md) | Rotate -> scale -> rotate | Low-rank approx, LoRA |
| [05 Matrix decompositions](./theory/05-matrix-decompositions.md) | QR, LU, Cholesky | GP solvers |
| [06 Spectral analysis](./theory/06-spectral-analysis.md) | Matrix exponentials, condition | RNN flow, Hessian |
| [07 Attention mechanisms](./theory/07-attention-mechanisms.md) | QKV as linear algebra | Transformers |
| [08 NN weight matrices](./theory/08-nn-weight-matrices.md) | Geometry of learned maps | Weight decay |
| [09 Open problems](./theory/09-open-problems.md) | Limits, frontiers | Research directions |
| [10 Connections](./theory/10-connections.md) | Links to other modules | Integration |
| [11 Summary](./theory/11-summary.md) | Memory tiers, checklist | Review |

---

## Foundations (Primer)

| # | File | When to Read |
|---|------|-------------|
| 01 | [Foundations primer](./foundations/01-primer.md) | Start here |
| 02 | [Fields and number systems](./foundations/02-fields-number-systems.md) | Before theory Section 1 |
| 03 | [Vector spaces deep](./foundations/03-vector-spaces-deep.md) | Before theory Section 1 |
| 04 | [Independence, basis](./foundations/04-linear-independence-basis.md) | Before theory Section 1 |
| 05 | [Four subspaces](./foundations/05-four-subspaces.md) | Before theory Section 1 |
| 06 | [Dot product and geometry](./foundations/06-dot-product-geometry.md) | Before theory Section 2 |

---

## Exercises

Computational exercises for each section. Python/NumPy only.

> Exercises directory: exercises/

## Project

Apply linear algebra to the H&C platform.

> See: project/README.md

## Assessment

Track your mastery progression.

> See: assessment/

---

*Last updated: 2026-06-18*
