---
module: M01
title: "Linear Algebra for ML"
artifact: theory-section
section: "03 — Eigendecomposition"
calibration: "MIT 18.06 (Strang), Lectures 21–25"
formalism_density: 0.4
status: draft
learner_id: L001
prereq: "theory/02-inner-products.md"
---

# Section 3 — Eigendecomposition

## Pre-reading map — what we're about to build

Up to now a matrix has been a *machine that moves the whole space around*. Feed it
a vector, it stretches, rotates, shears — generally scrambles directions into new
directions. This section asks a deceptively simple question:

> **Are there any directions the matrix refuses to twist — directions it only
> stretches or shrinks, never rotates?**

Those special directions are **eigenvectors**, and the amount of stretch along
each is its **eigenvalue**. Finding them is **eigendecomposition**, and it turns a
confusing tangle of a matrix into the cleanest possible story: "along *these* axes,
I'm just multiplication by a number." The route:

```
eigenvalue equation  Av = λv     (the directions that stay pure)
        │
        ▼
characteristic polynomial  det(A − λI) = 0   (how to FIND the λ's)
        │
        ▼
diagonalization  A = P D P⁻¹     (rebuild A from its pure directions)
        │
        ▼
symmetric case (real λ, orthogonal v)  ──▶  PCA, covariance, stability
```

The payoff at the bottom: PCA, the stability of RNN gradients, and spectral
normalization are all *the same theorem* applied to different matrices.

---

## 1. The eigenvalue equation

**Bridge.** Imagine pushing every point of a rubber sheet through a
transformation. Most arrows you draw on the sheet end up pointing somewhere new —
the transformation rotated them. But a few special arrows come out pointing the
*exact same way*, just longer or shorter. Those arrows found the transformation's
"grain," like the grain in a plank of wood. Push along the grain and you only
stretch; push across it and you twist. Eigenvectors are the grain of a matrix.

**Definition.** A nonzero vector `v` is an **eigenvector** of a square matrix `A`
if applying `A` only scales it:

```
A v  =  λ v
```

`A` — a square `n×n` matrix (the transformation). `v` — the eigenvector (the
direction that survives unrotated), `v ≠ 0`. `λ` — the **eigenvalue** (Greek
"lambda"), the scalar telling you *how much* `v` gets stretched (`λ>1`),
shrunk (`0<λ<1`), flipped (`λ<0`), or annihilated (`λ=0`).

Operationally: **`Av = λv` says "for this one direction, the whole matrix collapses
to a single multiplication."** All the shearing and rotating the matrix does to
other vectors simply doesn't happen to `v`.

```
generic vector w:          eigenvector v:
   w ──A──▶ Aw                v ──A──▶ λv
   (rotated, rescaled)        (same line, just rescaled)

      Aw                          λv
      ╱                           │
     ╱                            │   still on v's line!
    ●──── w                       ●──── v
```

```python
import numpy as np

A = np.array([[2.0, 0.0],
              [0.0, 3.0]])      # already diagonal: x-axis & y-axis are the grain

v1 = np.array([1.0, 0.0])       # along x
v2 = np.array([0.0, 1.0])       # along y

print("A v1 =", A @ v1, " → stretched by", 2.0)   # [2,0] = 2·v1
print("A v2 =", A @ v2, " → stretched by", 3.0)   # [0,3] = 3·v2

w = np.array([1.0, 1.0])        # NOT an eigenvector
print("A w  =", A @ w, " → [2,3], a different direction (got twisted)")
```

---

## 2. Finding eigenvalues — the characteristic polynomial

**Bridge.** Fine, eigenvectors are the grain. But how do you *find* them when the
matrix isn't conveniently diagonal? Rearrange the defining equation and a clean
algebraic test pops out.

Start from `Av = λv`. Move everything to one side: `Av − λv = 0`, i.e.
`(A − λI)v = 0`, where `I` is the **identity matrix** (the do-nothing
transformation). We need a *nonzero* `v` that this matrix sends to zero — meaning
`A − λI` must be **singular** (it crushes some direction to nothing). A matrix is
singular exactly when its **determinant** is zero:

```
det(A − λI)  =  0        ← the CHARACTERISTIC EQUATION
```

`det` — the determinant, a single number that's zero precisely when the matrix
collapses some dimension. Expanding `det(A − λI)` gives a degree-`n` polynomial in
`λ` — the **characteristic polynomial** — and its roots are the eigenvalues.

**Multiplicities.** A root can repeat. Two counts matter:
- **Algebraic multiplicity** — how many times `λ` appears as a root of the
  polynomial.
- **Geometric multiplicity** — how many genuinely independent eigenvectors `λ`
  actually has (the dimension of its eigenspace, `null(A − λI)`).

Geometric ≤ algebraic, always. When they're equal for every eigenvalue, the matrix
is **diagonalizable** (next section). When geometric falls short, the matrix is
**defective** — it has a repeated stretch factor but not enough independent
directions to go with it, and the clean story breaks down.

```python
A = np.array([[2.0, 1.0],
              [1.0, 2.0]])

# Characteristic polynomial det(A − λI) = (2−λ)² − 1 = λ² − 4λ + 3 = (λ−1)(λ−3)
eigvals, eigvecs = np.linalg.eig(A)
print("eigenvalues :", np.sort(eigvals))          # [1. 3.]
print("eigenvectors (columns):\n", eigvecs)
# λ=3 → direction [1,1]/√2 ; λ=1 → direction [1,−1]/√2
```

---

## 3. Diagonalization — A = P D P⁻¹

**Bridge.** Here's the eureka. If a matrix has a full set of `n` independent
eigenvectors, you can *change coordinates* so the matrix becomes pure stretching.
In the eigenvector coordinate system, `A` has no rotation, no shear — just a
number on each axis. That change of coordinates is diagonalization.

**Definition.** Stack the eigenvectors as the columns of a matrix `P`, and put the
eigenvalues on the diagonal of a matrix `D`. Then

```
A  =  P D P⁻¹
```

`P` — columns are the eigenvectors (the new axes, the "grain" coordinate system).
`D` — diagonal matrix of eigenvalues (pure stretch factors). `P⁻¹` — the inverse,
which translates *into* the eigenvector coordinates.

Read right to left, it's a three-act play: **`P⁻¹`** rewrites your vector in the
grain coordinates → **`D`** stretches each grain axis by its eigenvalue → **`P`**
translates back to the original coordinates. The matrix's whole behavior, told as
"go to the nice coordinates, stretch, come back."

**Why this is a superpower:** powers become trivial. `A² = PDP⁻¹PDP⁻¹ = PD²P⁻¹`,
and in general `Aᵏ = PDᵏP⁻¹`. Raising a *diagonal* matrix to a power just raises
each entry to that power. This is why eigenvalues govern long-run behavior — apply
`A` a thousand times and the eigenvalue closest to... well, that's the RNN story
below.

```python
A = np.array([[2.0, 1.0],
              [1.0, 2.0]])

eigvals, P = np.linalg.eig(A)
D = np.diag(eigvals)

A_reconstructed = P @ D @ np.linalg.inv(P)
print("reconstruction matches A?", np.allclose(A, A_reconstructed))   # True

# Powers the easy way:
A_cubed_fast = P @ np.diag(eigvals**3) @ np.linalg.inv(P)
print("A³ via eigen == A@A@A ?", np.allclose(A_cubed_fast, A @ A @ A))  # True
```

---

## 4. Symmetric matrices — the best-behaved case in all of ML

**Bridge.** Most matrices that matter in machine learning are **symmetric**
(`A = Aᵀ`): covariance matrices, Gram matrices, Hessians, kernel matrices. Nature
hands us symmetry constantly, and symmetry comes with a gift — the **Spectral
Theorem** — that makes everything clean.

**Spectral Theorem.** If `A` is real and symmetric, then:
1. **All its eigenvalues are real.** No imaginary stretch factors — every
   direction's behavior is an honest real number.
2. **Its eigenvectors are orthogonal.** The grain directions are mutually
   perpendicular (recall Section 2: zero cross-talk).

Because the eigenvectors are orthogonal, we can normalize them to unit length and
`P` becomes an **orthogonal matrix** `Q` (with `Q⁻¹ = Qᵀ` — the inverse is just the
transpose, free of charge). Diagonalization upgrades to:

```
A  =  Q D Qᵀ          ← spectral decomposition (orthogonal eigenvectors)
```

This is the cleanest decomposition in linear algebra: a symmetric matrix is *just*
a set of perpendicular axes, each with a real stretch factor. No defective
nonsense, no complex numbers. When you can arrange to work with symmetric matrices,
you should — and ML quietly does this everywhere.

```python
rng = np.random.default_rng(1)
M = rng.normal(size=(4, 4))
A = M @ M.T                      # M Mᵀ is ALWAYS symmetric & positive semidefinite

eigvals, Q = np.linalg.eigh(A)   # eigh: the symmetric-matrix solver — use it!
print("eigenvalues real & ≥ 0?", np.all(eigvals >= -1e-9))     # True
print("eigenvectors orthogonal? QᵀQ ≈ I:", np.allclose(Q.T @ Q, np.eye(4)))  # True
print("reconstruction A = Q D Qᵀ ?", np.allclose(A, Q @ np.diag(eigvals) @ Q.T))
```

---

## 5. Worked example — eigendecomposition of a covariance matrix (the seed of PCA)

**Bridge.** Let's make it concrete with the matrix ML cares about most: a
**covariance matrix**. Its eigenvectors point along the directions of greatest
*spread* in your data, and its eigenvalues say *how much* spread lives along each.
That sentence is the entire idea of Principal Component Analysis — we're deriving
PCA without naming it yet.

```python
rng = np.random.default_rng(7)

# Make 2-D data stretched mostly along the [1,1] diagonal.
n = 500
base = rng.normal(size=(n, 1)) * 3.0           # big spread
data = base @ np.array([[1.0, 1.0]]) + rng.normal(size=(n, 2)) * 0.4
data -= data.mean(axis=0)                       # center it

cov = (data.T @ data) / (n - 1)                 # 2×2 covariance matrix (symmetric)
eigvals, eigvecs = np.linalg.eigh(cov)

# eigh returns ascending; flip so the biggest-variance direction is first.
order = np.argsort(eigvals)[::-1]
eigvals, eigvecs = eigvals[order], eigvecs[:, order]

print("variance along each principal axis:", np.round(eigvals, 3))
print("top principal direction          :", np.round(eigvecs[:, 0], 3))
# → roughly ±[0.707, 0.707], the [1,1] diagonal we built in. PCA found it.
```

The top eigenvector recovered the `[1,1]` direction we deliberately stretched the
data along, and the top eigenvalue is far larger than the second — most of the
variance lives on one axis. **That is PCA.** Keep the top-`k` eigenvectors and
you've compressed the data to its most informative directions.

---

## 6. Where this lives in ML

- **PCA / dimensionality reduction.** PCA *is* eigendecomposition of the
  covariance matrix (Section 5). Top eigenvectors = principal components; their
  eigenvalues = variance explained. (In practice we usually compute it via the
  SVD of the data matrix — Section 4 — for numerical reasons, but the math is
  identical.)
- **RNN gradient stability.** Backpropagation through time repeatedly multiplies
  by a recurrent weight matrix `W`. From `Aᵏ = PDᵏP⁻¹`: if `W`'s largest eigenvalue
  magnitude (its **spectral radius**) exceeds 1, gradients *explode*; below 1, they
  *vanish*. The eigenvalues literally predict whether your RNN can learn long
  dependencies.
- **Spectral normalization** (GANs, stable training) divides weights by their
  largest singular value (closely related to the top eigenvalue) to cap how much a
  layer can stretch any input — directly controlling the `λ` that governs
  amplification.
- **Hessian eigenvalues** describe loss-surface curvature: large positive
  eigenvalues = steep sharp directions, near-zero = flat valleys. This shapes how
  optimizers behave and underlies second-order methods.

---

## Section recap

- An **eigenvector** is a direction a matrix only scales, never rotates:
  `Av = λv`. The **eigenvalue** `λ` is the stretch factor.
- Find eigenvalues by solving `det(A − λI) = 0`, the **characteristic equation**.
- **Algebraic** vs **geometric multiplicity**: when they match for all `λ`, the
  matrix **diagonalizes** as `A = PDP⁻¹` (eigenvectors in `P`, eigenvalues in `D`).
- Diagonalization makes powers trivial: `Aᵏ = PDᵏP⁻¹` — the source of long-run
  stability results.
- **Symmetric** matrices (the ML common case) get the **Spectral Theorem**: real
  eigenvalues, orthogonal eigenvectors, `A = QDQᵀ`.
- Eigendecomposition of a **covariance matrix** is **PCA**.

**Explain out loud:** Without notes, explain why an RNN's gradients explode or
vanish based on the eigenvalues of its recurrent matrix. If you can connect
`Aᵏ = PDᵏP⁻¹` to "gradients multiply the same matrix many times," you've grokked
the load-bearing idea.

---

## Memory tier update — Section 3

**CARRY (memorize):**
- `Av = λv` — the eigenvalue equation, and what it *means* (scale, don't rotate).
- Symmetric ⇒ real eigenvalues + orthogonal eigenvectors (use `np.linalg.eigh`).
- PCA = eigendecomposition of the covariance matrix.

**RECONSTRUCT (re-derive):**
- `det(A − λI) = 0` from `(A − λI)v = 0` needing a nonzero solution.
- `Aᵏ = PDᵏP⁻¹` from substituting `A = PDP⁻¹` and cancelling.

**LOOKUP (know it exists):**
- Exact definitions of algebraic vs geometric multiplicity / defective matrices.
- The spectral-radius threshold details for specific RNN architectures.

---

## Cross-modal — try it in the wild

**Try this in Hermes:** Generate a small 2-D dataset stretched along a diagonal,
compute its covariance matrix, and eigendecompose it. Predict the top eigenvector
*before* you run the code, then check. Were you right about which direction holds
the most variance?

**Try this in Claude:** Ask Claude to show you, in a few lines of PyTorch, an RNN
whose recurrent weight matrix has spectral radius > 1, and watch the gradient norms
grow across timesteps. Have it connect the explosion back to `Aᵏ = PDᵏP⁻¹` —
make the eigenvalue the protagonist of the explanation.

**Reflection prompt:** "Eigenvectors are the directions a transformation refuses to
twist." That sentence took mathematicians centuries to crystallize. Write a journal
line about a time you found the "grain" of a hard problem — the framing where the
twisting stopped and it became simple multiplication.
