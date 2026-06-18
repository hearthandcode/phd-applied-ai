---
module: M01
title: "Linear Algebra for ML"
artifact: theory-section
section: "11 — Module Summary"
calibration: "MIT 18.06 (Strang) — capstone synthesis"
formalism_density: 0.4
status: draft
learner_id: L001
prereq: "theory/10-connections.md"
---

# Section 11 — Module Summary

## Pre-reading map — what this file is for

This is the closing campfire. Not new material — a **consolidation pass** that does
three jobs: (1) lays out the seven intuitions of M01 as a single arc so you can see
the shape of what you learned; (2) sorts everything into CARRY / RECONSTRUCT / LOOKUP
one final time, at the *module* level; (3) gives you a revisit checklist so future-you
knows exactly which section to reopen when a concept goes fuzzy. Read it slowly. The
goal is that you can close the laptop and narrate M01 from memory.

---

## 1. The seven intuitions — the whole module as one arc

Each link in this chain *depends on the one before it*. That dependency is the lesson:
linear algebra is a ladder, and every rung was placed so the next one had something to
stand on.

```
1. VECTOR SPACE   →  a universe where add & scale never kick you out
        │             (field of scalars underneath; basis names every point)
        ▼
2. INNER PRODUCT  →  the measuring tool: length, angle, distance, projection
        │             (dot product turns algebra into geometry)
        ▼
3. EIGEN          →  a matrix's natural grain — directions it only stretches
        │             (Av = λv; diagonalizes the map in its own basis)
        ▼
4. SVD            →  the universal factorization: ANY matrix = rotate·stretch·rotate
        │             (A = UΣVᵀ; rank, compression, pseudoinverse all fall out)
        ▼
5. DECOMPOSITIONS →  practical workhorses: LU, QR, Cholesky
        │             (factor into easy pieces; do the hard work once)
        ▼
6. SPECTRAL / FOUR SUBSPACES → the anatomy: what a map reaches, destroys, sorts
        │             (row rank = col rank; nothing lost, only sorted)
        ▼
7. ML APPLICATIONS → it was all ML the whole time
                      (PCA, regression, covariance, backprop, attention)
```

**The single sentence for the whole module:**
> Linear algebra is the study of **add-and-scale universes** and the **maps between
> them** — and once you can measure (inner product), find the grain (eigen/SVD), and
> factor cheaply (decompositions), you have the skeleton of nearly all of ML.

---

## 2. What to CARRY — memorize forever (the 7-item campfire)

These never leave working memory. They're the load-bearing facts everything else
reconstructs *from*. If you forget these, you've lost the map.

1. **Vector space** = add & scale, closed (never kicked out). Basis = minimal naming
   alphabet; **dimension** = its size.
2. **Rank** = number of independent directions a matrix reaches = `dim C(A)` =
   `dim C(Aᵀ)` (row rank = column rank).
3. **Dot product** = alignment meter (`u·v = ‖u‖‖v‖cos θ`); zero = orthogonal.
   Projection = closest point on a subspace; least squares = projection.
4. **Eigendecomposition**: `Av = λv` — eigenvectors are directions the map only
   stretches; eigenvalues are the stretch factors. Symmetric → orthogonal
   eigenvectors (spectral theorem).
5. **SVD**: `A = UΣVᵀ` — *every* matrix factors into rotate · stretch · rotate.
   Singular values rank-order importance.
6. **The four subspaces**: column (reach), null (destroy), row (meaningful inputs),
   left-null (unreachable outputs). Dimensions add to `n` and `m`.
7. **The decompositions' jobs**: LU (general solve), QR (stable least squares),
   Cholesky (SPD square root → Gaussian sampling).

---

## 3. What to RECONSTRUCT — re-derive, don't memorize

These are *derivable* from the CARRY set. Don't burn memory on them — rebuild them
when needed. Two anchor equations regenerate almost everything:

> **Everything eigen reconstructs from `Av = λv`.**
> **Everything factorization reconstructs from `A = UΣVᵀ`.**

- The **eight vector-space axioms** → rebuild from "addition well-behaved (4) +
  scaling consistent (4)."
- **Why a basis is spanning + independent** → spanning gives existence of
  coordinates, independence gives uniqueness.
- **The spectral theorem** `Σ = QΛQᵀ` for symmetric matrices → special case of
  eigendecomposition with orthogonal eigenvectors.
- **PCA = SVD of centered data = eigendecomposition of covariance** → re-derive by
  writing `Σ ∝ XᵀX` and substituting `X = UΣVᵀ`.
- **Least-squares normal equations** `P = A(AᵀA)⁻¹Aᵀ` → rebuild from "drop a
  perpendicular onto `C(A)`."
- **QR least squares** `Rx = Qᵀb` → substitute `A = QR`, cancel `QᵀQ = I`.
- **Backprop** → chain rule = right-to-left products of transposed Jacobians.

---

## 4. What to LOOKUP — keep a reference open, never memorize

Memorizing these is wasted effort — they're stable, searchable, and rarely change.

- Exact **API signatures**: `np.linalg.{eig, eigh, svd, qr, matrix_rank, lstsq}`,
  `scipy.linalg.{lu, cholesky, null_space, orth, solve_triangular}`.
- **Specific algorithms**: how SVD/QR/Cholesky are *computed* (Householder, Golub–
  Kahan, etc.) — know they exist, let the library implement them.
- **Flop counts** and the cost-ordering proofs (Cholesky < LU < QR < SVD).
- Convention details: **sign/ordering** of singular vectors, eigenvalue ordering,
  PCA-vs-SVD conventions across libraries.
- Named model **embedding dimensionalities**, finite fields, exotic norms.

---

## 5. Learning progression checklist — which section to revisit when

A diagnostic, not a to-do list. When a concept goes fuzzy, this routes you to the
*exact* file to reopen. Self-check each row; reopen any you can't narrate aloud.

| If you can't confidently explain… | Revisit |
|---|---|
| What "add & scale, stay in the box" means | `foundations/01-primer.md`, `03-vector-spaces-deep.md` |
| Why `ℤ` isn't a field / why ML uses `ℝ` | `foundations/02-fields-number-systems.md` |
| Independence, basis, dimension, change of basis | `foundations/04-linear-independence-basis.md` |
| The four subspaces and row-rank = col-rank | `foundations/05-four-subspaces.md` |
| Dot product, projection, least squares geometry | `foundations/06-dot-product-geometry.md` |
| Linear maps & matrices as their spreadsheet form | `theory/01-vector-spaces.md` |
| Inner products, norms, orthogonality (formal) | `theory/02-inner-products.md` |
| `Av = λv`, diagonalization, spectral theorem | `theory/03-eigendecomposition.md` |
| `A = UΣVᵀ`, rank, compression, pseudoinverse | `theory/04-singular-value-decomposition.md` |
| LU / QR / Cholesky and when to use each | `theory/05-matrix-decompositions.md` |
| How M01 feeds M02/M03/M04/M21/M23 | `theory/10-connections.md` |

**Suggested revisit cadence:** skim the CARRY list weekly until it's automatic; reopen
any *single* fuzzy section rather than rereading the module; re-run one Python block
per session — typing the code reconsolidates the idea faster than rereading prose.

---

## 6. Where M01 goes next

You now hold the skeleton. The modules ahead add flesh:
- **M02 (Calculus)** turns the static Jacobian into *motion* — gradients that move.
- **M03 (Probability)** dresses covariance in eigen-geometry.
- **M04 (Statistics)** reveals regression and PCA as projection and SVD.
- **M21 (Neural Networks)** chains linear maps into learners.
- **M23 (Transformers)** stacks dot products and linear combinations into language.

None of those will feel *foreign*. That's the point of doing M01 first and doing it
well — you're not learning new math five times; you're recognizing the same skeleton
in new clothes.

---

## Section recap

- **Seven intuitions, one arc:** vector space → inner product → eigen → SVD →
  decompositions → spectral/four-subspaces → ML applications.
- **CARRY** the 7-item campfire (space, rank, dot/projection, eigen, SVD, four
  subspaces, the decompositions' jobs).
- **RECONSTRUCT** everything else from `Av = λv` and `A = UΣVᵀ`.
- **LOOKUP** APIs, algorithms, flop counts, conventions.
- Use the **revisit checklist** to reopen exactly one fuzzy section at a time.

**Explain out loud:** Close everything and narrate the seven-intuition arc from
"vector space" to "ML applications," saying *why each step needed the one before it*.
If the chain holds end to end, M01 is yours.

---

## Memory tier update — Section 11 (module-level)

**🔥 CARRY (memorize):**
- The seven-intuition arc as a single chain.
- The two anchor equations everything reconstructs from: `Av = λv`, `A = UΣVᵀ`.

**🔧 RECONSTRUCT (re-derive when needed):**
- Any individual derivation — they all descend from the two anchors plus "projection =
  drop a perpendicular."

**📖 LOOKUP (reference, never memorize):**
- The revisit-checklist table itself (it's a map, not memory work).
- All API/algorithm/convention specifics.

---

## Cross-modal — try it in the wild

**Try this in Hermes:** Write a single "M01 self-test" script that, for each CARRY
item, runs one tiny assertion proving you can produce it in code (e.g. `matrix_rank`
equals your hand count; `U @ diag(S) @ Vt` reconstructs `A`; a projection residual is
orthogonal). One green run = one piece of evidence the campfire is lit.

**Try this in Claude:** Ask Claude to quiz you on the seven intuitions in *random*
order — it states an ML scenario (e.g. "compressing an image," "decorrelating
features," "fitting a noisy line") and you name which M01 intuition powers it. Have it
score you and flag the one to revisit.

**Final reflection prompt:** You began M01 with "scattered-intermediate" linear
algebra and a programmer's instincts. Write a journal entry answering: *which of the
seven intuitions did I already half-own from coding, and which one genuinely rewired
how I see ML?* That contrast — what was familiar vs. what was new — is exactly the
RQ5 data this curriculum exists to capture. Name it while it's fresh.
