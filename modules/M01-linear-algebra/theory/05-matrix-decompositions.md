---
module: M01
title: "Linear Algebra for ML"
artifact: theory-section
section: "05 — Matrix Decompositions (QR, LU, Cholesky)"
calibration: "MIT 18.06 (Strang), Lectures 4–6, 17, 23"
formalism_density: 0.4
status: draft
learner_id: L001
prereq: "theory/04-singular-value-decomposition.md"
---

# Section 5 — Matrix Decompositions: QR, LU, Cholesky

## Pre-reading map — what we're about to build

SVD (Section 4) was the *theoretical* champion — every matrix, perfect geometry.
But it's also relatively expensive. In day-to-day numerical work — solving linear
systems, fitting regressions, sampling from Gaussians — we reach for three cheaper,
more specialized factorizations. They're the practical workhorses your libraries
call under the hood thousands of times a second.

The unifying idea: **factor a matrix into pieces whose shapes make the hard problem
easy.** A triangular matrix is trivial to solve (just substitute one variable at a
time). An orthogonal matrix is trivial to invert (transpose it). So every
decomposition here is a trade: spend some work *up front* to express `A` as a
product of easy pieces, then cash in repeatedly. The route:

```
LU   = L · U      (lower × upper triangular)   — Gaussian elimination, frozen
QR   = Q · R      (orthogonal × upper tri.)    — Gram–Schmidt, frozen → stable least squares
Chol = L · Lᵀ     (triangular "square root")   — for symmetric positive-definite matrices
                                                 → Gaussian-process sampling
```

Three factorizations, three ML payoffs: stable regression (QR), and sampling from
multivariate Gaussians (Cholesky), with LU as the foundational solver underneath.

---

## 1. LU decomposition — Gaussian elimination, frozen into a product

**Bridge.** You already know how to solve a linear system: eliminate variables one
at a time, row by row, until the matrix is triangular, then back-substitute. That
procedure — **Gaussian elimination** — is something you *do*. LU decomposition is
the realization that the whole procedure can be *recorded* as a single product of
two matrices, so you never have to redo the elimination when only the right-hand
side changes.

**Definition.** For a square matrix `A`,

```
A  =  L U
```

`L` — a **lower-triangular** matrix (nonzeros on and below the diagonal) with `1`s
on its diagonal; it records the elimination multipliers — *what you subtracted from
what*. `U` — an **upper-triangular** matrix (nonzeros on and above the diagonal);
it's the row-echelon result of elimination — *what the matrix became*.

Why bother? Solving `Ax = b` becomes two trivial triangular solves:
`Ly = b` (forward substitution), then `Ux = y` (back substitution). And crucially,
if you have *many* right-hand sides `b₁, b₂, ...` (common in simulation and
optimization), you factor `A` **once** and reuse `L, U` for each — the expensive
part is paid a single time.

In practice we use **partial pivoting** (swapping rows for numerical stability),
giving `PA = LU` where `P` is a permutation matrix. SciPy's `lu` returns exactly
this.

```python
import numpy as np
from scipy.linalg import lu, solve_triangular

A = np.array([[2.0, 1.0, 1.0],
              [4.0, 3.0, 3.0],
              [8.0, 7.0, 9.0]])
b = np.array([4.0, 10.0, 24.0])

P, L, U = lu(A)
print("L lower-triangular?", np.allclose(L, np.tril(L)))
print("U upper-triangular?", np.allclose(U, np.triu(U)))
print("PA = LU ?", np.allclose(P @ A, L @ U))

# Solve via the two triangular solves (the whole point of LU):
y = solve_triangular(L, P.T @ b, lower=True)
x = solve_triangular(U, y, lower=False)
print("solution x:", np.round(x, 4), " check Ax=b:", np.allclose(A @ x, b))
```

---

## 2. QR decomposition — Gram–Schmidt, frozen into a product

**Bridge.** Recall projection from Section 2: you can strip the part of one vector
that lies along another, leaving a perpendicular remainder. Do that systematically
to a whole set of columns — subtract from each column everything that overlaps with
the previous ones — and you **orthogonalize** them. That procedure is
**Gram–Schmidt**, and QR decomposition is Gram–Schmidt frozen into a product.

**Definition.** For an `m×n` matrix `A` (think: a tall data matrix),

```
A  =  Q R
```

`Q` — an `m×n` matrix with **orthonormal columns** (mutually perpendicular, each
unit length; `QᵀQ = I`). These are the orthogonalized, normalized versions of `A`'s
columns. `R` — an `n×n` **upper-triangular** matrix recording the overlaps that
Gram–Schmidt subtracted out — *how to rebuild the original columns from the clean
orthonormal ones*.

**Why ML cares: numerically stable least squares.** Back in Section 2 we solved
regression via the normal equations `AᵀA x = Aᵀb` — and flagged that forming `AᵀA`
*squares the conditioning*, amplifying floating-point error. QR sidesteps this
entirely. Substitute `A = QR` into the least-squares problem and the orthogonal `Q`
cancels cleanly (because `QᵀQ = I`), leaving a triangular system:

```
R x  =  Qᵀ b
```

No `AᵀA`, no squared conditioning — just one stable triangular solve. This is what
`np.linalg.lstsq` and most regression code actually do.

```python
rng = np.random.default_rng(0)

# Fit y ≈ 3·t + 2 with noise, via QR instead of normal equations.
t = np.linspace(0, 5, 30)
y = 3.0 * t + 2.0 + rng.normal(scale=0.3, size=t.size)
A = np.column_stack([t, np.ones_like(t)])      # design matrix, columns [t, 1]

Q, R = np.linalg.qr(A)
print("Q orthonormal columns? QᵀQ≈I:", np.allclose(Q.T @ Q, np.eye(2)))
print("R upper-triangular?", np.allclose(R, np.triu(R)))

# Solve R x = Qᵀ y  (one triangular back-substitution)
from scipy.linalg import solve_triangular
x = solve_triangular(R, Q.T @ y, lower=False)
print("fitted [slope, intercept]:", np.round(x, 3))   # ≈ [3, 2]
```

---

## 3. Cholesky decomposition — the square root of a matrix

**Bridge.** Some matrices are special: **symmetric positive-definite (SPD)** —
symmetric (`A = Aᵀ`) *and* with all-positive eigenvalues (from Section 3),
equivalently `xᵀAx > 0` for every nonzero `x`. Covariance matrices are SPD. Kernel
matrices are SPD. For these well-behaved matrices, there's a decomposition twice as
fast as LU and beautifully simple: Cholesky finds a triangular **square root**.

**Definition.** For a symmetric positive-definite matrix `A`,

```
A  =  L Lᵀ
```

`L` — a **lower-triangular** matrix with positive diagonal entries. It's as close
as a matrix gets to a square root: multiply `L` by its own transpose and you
recover `A`. (Compare to a positive number `a = (√a)²`; Cholesky is the matrix
version, with the transpose playing the role of "the other copy.")

Operationally: **Cholesky exists if and only if the matrix is SPD**, so attempting
it doubles as a *test* — if `np.linalg.cholesky` throws, your matrix isn't positive
definite (a common, useful sanity check on covariance estimates). And it's the
*fast* path: roughly half the cost of LU, because it exploits the symmetry.

**The killer app: sampling from a multivariate Gaussian.** You know how to draw
standard normal noise `z ~ N(0, I)` — independent unit-variance numbers. But you
often need correlated samples `x ~ N(μ, Σ)` with a specified covariance `Σ` (in
Gaussian processes, Bayesian models, diffusion-adjacent methods). The recipe:

```
x  =  μ + L z        where  Σ = L Lᵀ  (Cholesky)
```

The triangular `L` "colors" the white noise — it stretches and correlates the
independent `z` so the result has exactly covariance `Σ`. One line of linear
algebra turns a random-number generator into a sampler for *any* Gaussian.

```python
rng = np.random.default_rng(42)

mu  = np.array([1.0, -2.0])
Sigma = np.array([[2.0, 0.8],          # SPD covariance: positive diag, symmetric
                  [0.8, 1.0]])

L = np.linalg.cholesky(Sigma)          # Σ = L Lᵀ ; raises if Σ isn't SPD
print("Σ = L Lᵀ ?", np.allclose(Sigma, L @ L.T))

# Draw 10000 correlated samples: x = μ + L z, z ~ N(0, I)
z = rng.normal(size=(2, 10000))
x = mu[:, None] + L @ z

print("empirical mean      :", np.round(x.mean(axis=1), 2))           # ≈ [1, -2]
print("empirical covariance:\n", np.round(np.cov(x), 2))              # ≈ Σ
```

The empirical covariance of the samples reproduces the `Σ` we asked for — the
Cholesky factor did all the work of injecting the right correlations.

---

## 4. Choosing the right decomposition — a field guide

**Bridge.** You now have four decompositions (SVD from Section 4, plus these
three). They're not interchangeable; each is the right tool for a shape of problem.
A quick mental routing table:

```
Question you're asking                          Reach for
──────────────────────────────────────────────  ──────────────
Solve Ax=b, square A, many right-hand sides     LU       (cheap, reusable)
Least squares / regression, stably              QR       (no squared conditioning)
Sample a Gaussian / invert an SPD matrix fast   Cholesky (2× faster, SPD only)
Rank, compression, pseudoinverse, ANY shape     SVD      (most robust, most costly)
```

Rule of thumb on cost vs. generality: **Cholesky < LU < QR < SVD**. The cheaper
ones demand more of the matrix (Cholesky needs SPD); the pricier ones ask nothing
and tell you everything. Pick the cheapest decomposition whose assumptions your
matrix actually satisfies.

```python
# The same SPD system, solved three ways — all agree, costs differ.
A = np.array([[4.0, 2.0],
              [2.0, 3.0]])          # SPD
b = np.array([2.0, 1.0])

x_solve = np.linalg.solve(A, b)                 # general (LU under the hood)
L = np.linalg.cholesky(A)                        # Cholesky path
import scipy.linalg as sla
y = sla.solve_triangular(L, b, lower=True)
x_chol = sla.solve_triangular(L.T, y, lower=False)

print("LU/solve :", np.round(x_solve, 4))
print("Cholesky :", np.round(x_chol, 4))
print("agree?", np.allclose(x_solve, x_chol))
```

---

## 5. Where this lives in ML

- **QR for linear regression.** The numerically stable workhorse behind
  least-squares fitting — `np.linalg.lstsq` and statistical packages use QR (or
  SVD) precisely to dodge the squared-conditioning trap of the normal equations.
- **Cholesky in Gaussian processes.** GP regression needs to sample from and invert
  the kernel covariance matrix `K`. Cholesky `K = LLᵀ` is the standard route: sample
  via `μ + Lz`, and solve `K⁻¹y` through two triangular solves. The `O(n³)` Cholesky
  is the GP's computational bottleneck — and the reason GPs struggle to scale.
- **Cholesky as a positive-definiteness check.** Training can drift a covariance or
  preconditioner matrix out of SPD; a failed Cholesky is the cheapest detector.
- **LU under the hood.** Nearly every general linear solve (`np.linalg.solve`,
  matrix inverses, many optimizers' inner steps) is LU with partial pivoting.
- **Cholesky in Bayesian / second-order methods.** Sampling posteriors, applying
  preconditioners, and natural-gradient steps all lean on the SPD square root.

---

## Section recap

- A **decomposition** factors `A` into easy pieces (triangular = easy to solve,
  orthogonal = easy to invert), trading up-front work for cheap repeated use.
- **LU** (`A = LU`): Gaussian elimination frozen into lower × upper triangular;
  the general-purpose solver, great for many right-hand sides.
- **QR** (`A = QR`): Gram–Schmidt frozen into orthonormal × upper-triangular;
  gives **numerically stable least squares** via `Rx = Qᵀb`, no squared conditioning.
- **Cholesky** (`A = LLᵀ`): the triangular **square root** of a symmetric
  positive-definite matrix; the engine for **sampling multivariate Gaussians**
  (`x = μ + Lz`) and an SPD test for free.
- Routing by cost/generality: **Cholesky < LU < QR < SVD** — pick the cheapest one
  your matrix qualifies for.

**Explain out loud:** Without notes, explain why we fit regressions with QR instead
of the normal equations from Section 2, and how Cholesky turns a plain random-number
generator into a sampler for any Gaussian. If you can narrate "Q cancels because
it's orthogonal" and "L colors white noise," you own this section.

---

## Memory tier update — Section 5

**CARRY (memorize):**
- The three forms: `LU` (general solve), `QR` (stable least squares), `LLᵀ`
  (Cholesky, SPD square root).
- Cholesky needs symmetric positive-definite; a failed Cholesky = not SPD.
- Gaussian sampling: `x = μ + Lz` with `Σ = LLᵀ`.

**RECONSTRUCT (re-derive):**
- QR least squares `Rx = Qᵀb` from substituting `A = QR` and cancelling `QᵀQ = I`.
- Why `x = μ + Lz` has covariance `Σ` (push the covariance through: `Cov(Lz)=LLᵀ`).

**LOOKUP (know it exists):**
- LU with partial pivoting `PA = LU` mechanics.
- Exact flop counts / the cost-ordering proof for each decomposition.

---

## Cross-modal — try it in the wild

**Try this in Hermes:** Build a 2-D covariance matrix with strong correlation,
Cholesky-factor it, and draw 5,000 samples via `μ + Lz`. Compute the empirical
covariance and compare to your target `Σ`. Then deliberately make the matrix
*not* positive-definite and watch `np.linalg.cholesky` refuse — feel why the test
works.

**Try this in Claude:** Ask Claude to walk through a minimal Gaussian-process
regression and point to the exact lines where Cholesky is used — both for sampling
and for solving the kernel system. Have it connect each line back to Section 5's
`A = LLᵀ`.

**Reflection prompt:** Every decomposition here is the same wisdom: *do the hard
reshaping once, then the repeated work is cheap.* You've made this trade in code a
thousand times — caching, indexing, precomputation. Write a journal line connecting
"factor the matrix once, solve many times" to a precomputation pattern from your own
engineering work. The instinct is already in your hands; now it has a name.

---

## Module M01 closing note

That closes the core decompositions of M01. You walked the full arc: a **universe**
(vector spaces), a **map** (linear transformations), **geometry** (inner products),
the matrix's **grain** (eigendecomposition), the **universal** factorization (SVD),
and the **practical** workhorses (LU/QR/Cholesky). Every one of them reappears in
the modules ahead — covariance and PCA in probability (M03), Hessians and curvature
in optimization, low-rank structure throughout deep learning. The fire's well lit.
Carry the kindling forward.
