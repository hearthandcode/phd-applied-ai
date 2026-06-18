---
module: M01
title: "Linear Algebra for ML"
artifact: theory-section
section: "04 — Singular Value Decomposition"
calibration: "MIT 18.06 (Strang), Lectures 29–30"
formalism_density: 0.4
status: draft
learner_id: L001
prereq: "theory/03-eigendecomposition.md"
---

# Section 4 — Singular Value Decomposition

## Pre-reading map — what we're about to build

Section 3 gave us a gorgeous tool — eigendecomposition — with one cruel
restriction: **it only works on square matrices**, and really shines only on
symmetric ones. But the matrices in ML are mostly *not* square. A data matrix is
`samples × features`. A weight matrix maps `768` dims to `3072`. An image is
`height × width`. Eigendecomposition simply can't touch these.

The **Singular Value Decomposition (SVD)** removes the restriction entirely.
**Every matrix — any shape, any size, square or not, invertible or not — has an
SVD.** It is the most universal, most numerically trustworthy decomposition in the
subject, and it's the secret engine behind PCA, LoRA, recommender systems, and the
pseudoinverse. The route:

```
the SVD theorem   A = U Σ Vᵀ        (every matrix = rotate → scale → rotate)
        │
        ▼
geometric reading: three honest operations, not just symbols
        │
        ▼
link to eigendecomposition: U from AAᵀ, V from AᵀA, σ = √eigenvalues
        │
        ▼
truncated SVD → best low-rank approximation → LoRA, recommenders, pseudoinverse
```

If you only deeply learn one decomposition for ML, make it this one.

---

## 1. The SVD theorem

**Bridge.** Eigendecomposition said "in the right coordinates, a matrix is pure
stretching." SVD says something even more universal: **any** linear map, no matter
how weird its shape, is secretly just *rotate the input, stretch along clean axes,
then rotate the output*. Three simple moves. The matrix's apparent complexity is an
illusion created by viewing those three moves in awkward coordinates.

**Definition.** For any real `m×n` matrix `A`, the SVD is

```
A  =  U Σ Vᵀ
```

`A` — an `m×n` matrix (any shape). `V` — an `n×n` **orthogonal** matrix; its
columns are the **right singular vectors** (a clean set of perpendicular input
axes). `Σ` — an `m×n` **diagonal** matrix of **singular values**
`σ₁ ≥ σ₂ ≥ ... ≥ 0` (Greek "sigma"; the stretch factors, always real and
non-negative, sorted big-to-small). `U` — an `m×m` **orthogonal** matrix; its
columns are the **left singular vectors** (a clean set of perpendicular output
axes).

Orthogonal matrices are pure rotations/reflections — they preserve all lengths and
angles. So the *only* thing that actually distorts space is `Σ`, the diagonal
stretcher. Everything else just spins.

---

## 2. Geometric interpretation — three honest operations

**Bridge.** Don't let `UΣVᵀ` sit there as inert symbols. Read it right-to-left as
a pipeline that processes a vector `x`:

```
        Vᵀ              Σ               U
x ──rotate input──▶ ──scale axes──▶ ──rotate output──▶  Ax
   (no distortion)    (the ONLY        (no distortion)
                       distortion)
```

1. **`Vᵀ` rotates** your input vector into a clean coordinate system — the one
   where `A`'s action becomes simple. No stretching yet, just reorienting.
2. **`Σ` stretches** each of those clean axes by its singular value `σᵢ`. This is
   the entire substance of what `A` does. A big `σ₁` means axis 1 gets amplified a
   lot; a tiny `σₙ` means axis `n` gets nearly flattened.
3. **`U` rotates** the stretched result into the output space's orientation.

The famous picture: SVD says **a matrix maps the unit sphere to an ellipsoid.** The
singular values are the lengths of the ellipsoid's semi-axes; `U`'s columns point
along those axes. The largest `σ` is the longest the matrix can ever stretch any
unit vector — that's the matrix's **operator norm**, and it's exactly the quantity
spectral normalization caps.

```
   unit circle (input)        ──A──▶        ellipse (output)
        ○                                      ╱‾‾╲
       ╱ ╲                                    │    │  ← σ₁ long axis
      │   │                                    ╲__╱   ← σ₂ short axis
       ╲ ╱
        ○
```

```python
import numpy as np

A = np.array([[3.0, 0.0],
              [0.0, 1.0],
              [0.0, 0.0]])         # 3×2 — NOT square; eigendecomp can't touch it

U, s, Vt = np.linalg.svd(A)        # s is the 1-D array of singular values
print("singular values:", s)       # [3. 1.] — the stretch factors

# reconstruct: build the m×n Σ, then U Σ Vᵀ
Sigma = np.zeros_like(A)
np.fill_diagonal(Sigma, s)
print("reconstruct A = U Σ Vᵀ ?", np.allclose(A, U @ Sigma @ Vt))   # True
print("U orthogonal? UᵀU≈I:", np.allclose(U.T @ U, np.eye(3)))
print("V orthogonal? VᵀV≈I:", np.allclose(Vt @ Vt.T, np.eye(2)))
```

---

## 3. The bridge back to eigendecomposition

**Bridge.** SVD isn't disconnected from Section 3 — it's eigendecomposition
applied cleverly to the two *symmetric* matrices you can always build from `A`.
Recall from Section 3 that `AAᵀ` and `AᵀA` are always symmetric (and positive
semidefinite), so the Spectral Theorem applies to them with real eigenvalues and
orthogonal eigenvectors. SVD harvests exactly those.

```
columns of U  =  eigenvectors of  A Aᵀ   (m×m, symmetric)
columns of V  =  eigenvectors of  Aᵀ A   (n×n, symmetric)
σᵢ            =  √(eigenvalue of either)   ← singular values are square roots
```

Why square roots? Because `AᵀA = (UΣVᵀ)ᵀ(UΣVᵀ) = VΣᵀUᵀUΣVᵀ = V(ΣᵀΣ)Vᵀ`. That last
form *is* an eigendecomposition of `AᵀA` with eigenvalues `σᵢ²` on the diagonal. So
the eigenvalues of `AᵀA` are the *squares* of the singular values — take the square
root to get back to `σ`. This is also why SVD is numerically safer than forming
`AᵀA` directly (Section 2's least-squares warning): SVD never squares your numbers,
so it never squares your conditioning problems.

```python
A = np.array([[2.0, 0.0],
              [1.0, 1.0],
              [0.0, 2.0]])

U, s, Vt = np.linalg.svd(A)

# Verify σ² are the eigenvalues of AᵀA:
eig_AtA = np.sort(np.linalg.eigvalsh(A.T @ A))[::-1]
print("σ²        :", np.round(s**2, 4))
print("eig(AᵀA)  :", np.round(eig_AtA, 4))     # match!
```

---

## 4. Low-rank approximation — the SVD's killer app

**Bridge.** Here's where SVD earns its keep in ML. The singular values come sorted
**largest first**, and they often decay fast — `σ₁` huge, `σ₂` smaller, and a long
tail of near-zero ones. The tiny singular values contribute almost nothing to the
matrix. So: *throw them away.* Keep only the top `k`, and you get the **best
possible rank-`k` approximation** of `A`.

**Truncated SVD.** Keep the top `k` singular values and their vectors:

```
A  ≈  Aₖ  =  Uₖ Σₖ Vₖᵀ        (only the k biggest σ's)
```

`Uₖ` — first `k` columns of `U`. `Σₖ` — top-left `k×k` block of `Σ`. `Vₖ` — first
`k` columns of `V`. This `Aₖ` is provably the closest rank-`k` matrix to `A` (the
**Eckart–Young theorem** — the error is exactly the size of the singular values you
dropped). Operationally: **you've compressed the matrix to its most important
directions, paying a known, controllable price in accuracy.**

Storage drops from `m·n` numbers to `k·(m + n + 1)` — a massive saving when `k` is
small. That ratio is the whole economic argument behind LoRA and matrix
factorization.

```python
rng = np.random.default_rng(3)

# Build a 50×50 "image-like" matrix with structure (low effective rank).
x = np.linspace(0, 1, 50)
img = np.outer(np.sin(6*x), np.cos(4*x)) + 0.1*rng.normal(size=(50, 50))

U, s, Vt = np.linalg.svd(img)

def reconstruct(k):
    return U[:, :k] @ np.diag(s[:k]) @ Vt[:k, :]

full_storage = img.size
for k in [1, 3, 5, 50]:
    approx = reconstruct(k)
    err = np.linalg.norm(img - approx) / np.linalg.norm(img)
    stored = k * (img.shape[0] + img.shape[1] + 1)
    print(f"k={k:2d}  rel.error={err:5.2%}  stored={stored:5d}/{full_storage}  "
          f"({stored/full_storage:4.0%} of original)")
```

Watch the relative error plummet as `k` grows: a handful of singular values often
captures the vast majority of the matrix. The dropped tail was mostly the noise we
sprinkled in. **Compression and denoising are the same act** — keep the strong
directions, discard the weak.

---

## 5. The pseudoinverse — solving the unsolvable

**Bridge.** Not every matrix has an inverse — non-square ones can't, and singular
ones won't. But we still want to "undo" a matrix as best we can, for least squares
and beyond. SVD hands us the **Moore–Penrose pseudoinverse**, written `A⁺`, by the
obvious trick: invert what's invertible (the nonzero `σ`'s), leave the rest alone.

```
A⁺  =  V Σ⁺ Uᵀ        where Σ⁺ inverts each nonzero σᵢ → 1/σᵢ
```

The least-squares solution from Section 2 — `min ‖Ax − b‖` — is simply
`x = A⁺b`, and computing it through SVD is the numerically *robust* way (no
`AᵀA` to blow up the conditioning). When the system is underdetermined, `A⁺b`
even hands you the *smallest-norm* solution for free.

```python
A = np.array([[1.0, 1.0],
              [1.0, 2.0],
              [1.0, 3.0]])
b = np.array([1.0, 2.0, 2.0])

x_pinv  = np.linalg.pinv(A) @ b              # via SVD pseudoinverse
x_lstsq, *_ = np.linalg.lstsq(A, b, rcond=None)
print("pseudoinverse solution:", np.round(x_pinv, 4))
print("lstsq solution        :", np.round(x_lstsq, 4))   # identical
```

---

## 6. Where this lives in ML

- **LoRA (Low-Rank Adaptation).** Fine-tuning a giant weight matrix `W` is
  expensive. LoRA freezes `W` and learns a *low-rank* update `ΔW = BA` (with `B`,
  `A` skinny). That's Section 4's truncated-SVD idea turned into a training
  strategy: the meaningful change to a layer lives in a few directions, so only
  learn those. SVD is the theoretical justification that low rank can carry the
  signal.
- **Matrix factorization for recommendations.** A `users × items` ratings matrix
  is mostly empty and approximately low-rank (tastes cluster). Truncated SVD (or
  its learned cousins) factors it into `users × k` and `k × items` latent factors —
  the `k` hidden "genres." Filling in the product predicts missing ratings.
- **PCA, robustly.** PCA is the SVD of the centered data matrix; the right singular
  vectors *are* the principal components, and `σᵢ²/(n−1)` are the variances. This is
  the numerically preferred route to PCA (vs. eigendecomposing the covariance).
- **Pseudoinverse / stable least squares.** SVD gives the conditioning-safe
  solution to regression and the minimum-norm answer for underdetermined systems.
- **Operator norm & spectral normalization.** `σ₁` is the most a layer can amplify
  any input; capping it stabilizes GAN and deep-net training.

---

## Section recap

- **Every** matrix has an SVD: `A = UΣVᵀ`, with `U`, `V` orthogonal (rotations)
  and `Σ` diagonal of non-negative **singular values** (the only real stretching).
- Geometrically a matrix is **rotate → scale → rotate**; it maps the unit sphere to
  an ellipsoid whose semi-axis lengths are the singular values.
- SVD connects to eigendecomposition: `U` = eigenvectors of `AAᵀ`, `V` =
  eigenvectors of `AᵀA`, and `σᵢ = √(eigenvalue)`.
- **Truncated SVD** (`Aₖ = UₖΣₖVₖᵀ`) is the provably best rank-`k` approximation
  (Eckart–Young) — the foundation of compression, denoising, LoRA, and recommenders.
- The **pseudoinverse** `A⁺ = VΣ⁺Uᵀ` inverts what's invertible and gives robust
  least-squares solutions.

**Explain out loud:** Without notes, explain why "compressing an image with
truncated SVD" and "LoRA fine-tuning a weight matrix" are the same mathematical
move. If you can say "the useful information lives in the top few singular
directions," you've got it.

---

## Memory tier update — Section 4

**CARRY (memorize):**
- `A = UΣVᵀ`: U, V rotate (orthogonal); Σ is the diagonal stretch.
- Singular values are sorted big→small; truncating keeps the top `k`.
- SVD works on *any* matrix — that's its whole reason to exist over eigendecomp.

**RECONSTRUCT (re-derive):**
- `σᵢ = √(eigenvalue of AᵀA)` from `AᵀA = V(ΣᵀΣ)Vᵀ`.
- Truncated reconstruction `Uₖ Σₖ Vₖᵀ` and its storage savings.

**LOOKUP (know it exists):**
- Pseudoinverse formula `VΣ⁺Uᵀ` (use `np.linalg.pinv`).
- Eckart–Young exact error bound; thin vs. full SVD conventions.

---

## Cross-modal — try it in the wild

**Try this in Hermes:** Take any grayscale image, run `np.linalg.svd`, and
reconstruct it at `k = 5, 20, 50` singular values. Plot the relative error vs `k`.
At what `k` does the image become recognizable? That elbow is the image's
"effective rank" — its true information content.

**Try this in Claude:** Ask Claude to explain how LoRA's `ΔW = BA` decomposition
maps onto truncated SVD, and to show the parameter-count savings for a real layer
size (say `4096 × 4096` with rank `8`). Have it connect "rank-8 update" back to
"keep the top 8 singular directions."

**Reflection prompt:** SVD says every transformation — however tangled it looks — is
secretly *rotate, stretch, rotate*. Write a journal line about a system in your own
life or work that felt hopelessly complicated until you found the coordinate change
that made it three simple steps.
