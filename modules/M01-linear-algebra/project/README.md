---
type: project-readme
schema_version: "1.0"
module_id: M01
module_title: "Linear Algebra for ML"
language: Python
created: 2026-06-13
updated: 2026-06-13
status: generated
---

# M01: Linear Algebra for ML — Implementation Project

**Language:** Python (NumPy for verification only; core algorithm must be implemented from scratch)
**Estimated time:** 16–20 hours
**Skills demonstrated:** SVD derivation, numerical linear algebra, image compression pipeline

---

## Problem statement

Implement Singular Value Decomposition (SVD) from scratch in Python — without using `numpy.linalg.svd` or any other library SVD routine — and apply it to image compression.

The SVD is the central matrix factorization in applied machine learning. Implementing it from scratch forces engagement with the underlying numerical algorithms (power iteration, QR iteration) that production libraries abstract away. Verifying your implementation against `numpy.linalg.svd` closes the loop between theory and ground truth.

---

## Deliverables

### 1. Core SVD implementation (`svd_scratch.py`)

Implement a function with signature:

```python
def svd_scratch(A: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Compute the thin SVD of matrix A.

    Returns:
        U: Left singular vectors, shape (m, r)
        s: Singular values (1D array), shape (r,), sorted descending
        Vt: Right singular vectors transposed, shape (r, n)
        where r = rank(A)
    """
```

**Required approach:** Use eigendecomposition of $A^\top A$ to obtain right singular vectors $V$ and singular values $\sigma_i = \sqrt{\lambda_i}$, then compute left singular vectors $u_i = (1/\sigma_i) A v_i$. You may use `numpy.linalg.eigh` (symmetric eigenvalue solver) but not `svd`. Handle near-zero singular values robustly (define a threshold for rank truncation).

### 2. Verification suite (`verify_svd.py`)

Write a test suite that:
- Runs your implementation against `numpy.linalg.svd` on at least five randomly generated matrices: square, tall, wide, rank-deficient, and near-singular.
- Reports the Frobenius-norm reconstruction error $\|A - U \Sigma V^\top\|_F$ for both implementations.
- Verifies orthogonality: $\|U^\top U - I\|_F < \epsilon$ and $\|V^\top V - I\|_F < \epsilon$ for a threshold $\epsilon$ you define and justify.
- Times both implementations on a $500 \times 500$ random matrix.

### 3. Image compression application (`compress_image.py`)

Apply your SVD to compress a grayscale image:
- Load a real grayscale image (any public-domain image, minimum $256 \times 256$ pixels).
- Compute the SVD of the image matrix.
- Reconstruct the image using only the top $k$ singular values for $k \in \{5, 20, 50, 100\}$.
- Display the reconstructed images side by side with their PSNR (Peak Signal-to-Noise Ratio) and compression ratio $r = mn / (k(m+n+1))$.
- Produce a plot of the singular value spectrum (log scale) to show the rapid decay that makes compression possible.

### 4. Written analysis (`analysis.md`)

A short technical writeup (400–600 words) covering:
- Why the eigendecomposition of $A^\top A$ yields the right singular vectors of $A$
- The numerical limitations of your implementation compared to `numpy.linalg.svd` (which uses a divide-and-conquer algorithm)
- At what rank $k$ the image becomes visually indistinguishable from the original, and why this corresponds to the "knee" in the singular value spectrum
- One failure mode you encountered and how you diagnosed it

---

## Done state

This project is complete when:
1. `svd_scratch.py` produces results matching `numpy.linalg.svd` to within Frobenius error $< 10^{-8}$ on full-rank matrices (numerical precision, not algorithmic error).
2. `verify_svd.py` passes all five matrix test cases with the orthogonality check passing at $\epsilon = 10^{-10}$.
3. `compress_image.py` produces a 2×2 or 1×4 plot showing reconstructions at $k \in \{5, 20, 50, 100\}$ with correct PSNR values.
4. `analysis.md` explains the connection between $A^\top A$ eigendecomposition and SVD accurately, in your own words.

---

## Evaluation criteria

| Criterion | Weight | What "good" looks like |
|---|---|---|
| **Correctness** | 35% | Frobenius reconstruction error $< 10^{-8}$; singular values match numpy to 8+ significant figures; orthogonality check passes |
| **Robustness** | 25% | Handles rank-deficient and near-singular matrices without crashing or producing NaN; threshold for zero singular values is explicit and justified |
| **Analysis depth** | 25% | Written analysis correctly traces the eigendecomposition derivation, quantifies numerical differences vs. numpy, and explains the singular value spectrum decay |
| **Code quality** | 15% | Functions are documented; variable names match mathematical notation from theory.md; no unexplained magic constants |

---

## Setup

```bash
pip install numpy matplotlib pillow
```

No other dependencies required. Python 3.10+ recommended.

---

## Suggested approach

1. Read the SVD proof sketch in `theory.md` (§ Singular value decomposition) before writing any code.
2. Implement on a $3 \times 2$ matrix first — small enough to check by hand.
3. Add the rank-deficient case only after the full-rank case is correct.
4. Use a real image (e.g., from the USC SIPI Image Database, which is public domain) for the compression task.
