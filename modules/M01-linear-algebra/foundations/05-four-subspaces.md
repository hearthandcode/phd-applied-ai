---
module: M01
title: "Linear Algebra for ML"
artifact: foundations-primer
section: "05 — The Four Fundamental Subspaces"
calibration: "MIT 18.06 (Strang), Lecture 10 — the big picture"
formalism_density: 0.4
status: draft
learner_id: L001
prereq: "foundations/04-linear-independence-basis.md"
---

# Section 05 — The Four Fundamental Subspaces

> This is Strang's "big picture" — the lecture he says is the heart of 18.06. Every
> matrix `A` (an `m×n` table, also a linear map) quietly defines **four** subspaces:
> two about what it can *reach* and *destroy* on the way out, two about the same
> from the *input* side. Section 04 gave you subspaces, basis, and dimension; this
> file uses all three to map the complete anatomy of a matrix.

---

## 1. Setup — one matrix, two viewpoints

**Bridge.** A matrix `A` of shape `m×n` ("m rows, n columns") is a linear map that
eats an `n`-vector and produces an `m`-vector: `A : ℝⁿ → ℝᵐ`. There are two honest
ways to read `A`:
- **By columns:** `Ax` is a linear combination of `A`'s columns, weighted by the
  entries of `x`. (Column view → tells you what `A` can *output*.)
- **By rows:** each output entry is a dot product of a row of `A` with `x`. (Row view
  → tells you about the *inputs*.)

Each viewpoint spawns two subspaces — one "alive" space and one "destroyed" space.
Four in total. We'll take them one at a time, then assemble the grand picture.

**Inline symbols.** `A` — the `m×n` matrix/map. `Aᵀ` — its **transpose** (flip rows
↔ columns), shape `n×m`. `C(·)` — "column space of." `N(·)` — "null space of."
`rank A = r` — the number of independent directions `A` reaches.

---

## 2. Column space `C(A)` — what the map can reach

**Bridge.** Push every possible input `x` through `A` and collect *all* the outputs
you can ever produce. That collection is the **column space** — the reachable
territory of the map. It's called the column space because every output `Ax` is a
linear combination of `A`'s columns, so the reachable set is exactly the **span of
the columns**.

**Definition.** `C(A) = { Ax : x ∈ ℝⁿ } = span of the columns of A`. It lives in the
output space `ℝᵐ`. Its dimension is the **rank** `r` — the number of *independent*
columns.

> `C(A)` answers: *"What outputs are even possible?"* If `b` isn't in `C(A)`, then
> `Ax = b` has **no** solution — you're asking the map for something it can't reach.
> This is exactly why least squares exists (project `b` onto `C(A)`).

---

## 3. Null space `N(A)` — what the map destroys

**Bridge.** Some inputs get crushed to nothing: `Ax = 0`. The set of all such inputs
is the **null space** — the directions the map *annihilates*, the information it
throws away. It's the "kernel" from the primer's symbol card.

**Definition.** `N(A) = { x ∈ ℝⁿ : Ax = 0 }`. It lives in the input space `ℝⁿ`. Its
dimension is the **nullity** `n − r`.

> `N(A)` answers: *"What inputs map to zero — i.e., what does the map forget?"* If
> `N(A)` contains more than just `0`, the map is **not injective**: distinct inputs
> can collide to the same output (add any null-space vector and the output is
> unchanged). That's lost information — the heart of why some systems can't be
> uniquely inverted.

---

## 4. Row space `C(Aᵀ)` — the other view

**Bridge.** Flip to the rows. The **row space** is the span of `A`'s rows — or
equivalently, the column space of the transpose `Aᵀ`. Here's the beautiful part: the
row space lives in the *input* space `ℝⁿ`, and it's exactly the set of input
directions the map treats as "meaningful" — the orthogonal complement of the
directions it destroys.

**Definition.** `C(Aᵀ) = span of the rows of A`, living in `ℝⁿ`. Remarkably, its
dimension is **also `r`** — the same rank as the column space.

> The number of independent columns equals the number of independent rows. Always.
> This is the single most surprising free lunch in linear algebra — "row rank =
> column rank." It's why we can just say *"the rank,"* singular.

---

## 5. Left null space `N(Aᵀ)` — the dual destruction

**Bridge.** Apply the null-space idea to the transpose: which output-side directions
`y` get crushed when you map *backwards* through `Aᵀ`? Equivalently, `yᵀA = 0` — the
combinations of rows that cancel to zero. These are the directions in the **output**
space `ℝᵐ` that the map can *never reach*; they're orthogonal to everything `A`
produces.

**Definition.** `N(Aᵀ) = { y ∈ ℝᵐ : Aᵀy = 0 }`, living in `ℝᵐ`. Its dimension is
`m − r`.

> `N(Aᵀ)` answers: *"What output directions are forever unreachable?"* It's the
> leftover of `ℝᵐ` after you carve out the column space — the residual space where
> least-squares errors live.

---

## 6. The Fundamental Theorem — how the four fit together

**Bridge.** Now the assembly. The four subspaces aren't a random list — they tile the
input and output spaces *perfectly*, in orthogonal pairs, with rank `r` as the hinge.

**On the input side `ℝⁿ`:** the row space (dim `r`) and the null space (dim `n − r`)
are **orthogonal complements** — every input splits uniquely into a "meaningful"
part (row space) and a "destroyed" part (null space):

```
dim C(Aᵀ)  +  dim N(A)   =   r   +   (n − r)   =   n      (the input space ℝⁿ)
```

**On the output side `ℝᵐ`:** the column space (dim `r`) and the left null space (dim
`m − r`) are **orthogonal complements** — every output direction is either reachable
or forever-unreachable:

```
dim C(A)   +  dim N(Aᵀ)  =   r   +   (m − r)   =   m      (the output space ℝᵐ)
```

**The crown jewel:** `dim C(A) = dim C(Aᵀ) = r`. Column rank = row rank. This is the
rank–nullity law from the primer, now seen whole: nothing is lost, only **sorted**
into "kept" and "crushed," on both sides of the map.

---

## 7. Python: compute bases for all four subspaces

We'll take a deliberately rank-deficient matrix and extract bases for all four
subspaces, then verify the dimension arithmetic of the fundamental theorem. SciPy's
`null_space` and SVD do the heavy lifting.

```python
import numpy as np
from scipy.linalg import null_space, orth

# A 3×4 matrix, deliberately rank 2 (row 3 = row1 + row2).
A = np.array([[1., 2., 0., 1.],
              [0., 1., 1., 0.],
              [1., 3., 1., 1.]])      # = row0 + row1  → dependent
m, n = A.shape
r = np.linalg.matrix_rank(A)
print(f"shape m×n = {m}×{n},  rank r = {r}\n")

# 1. Column space C(A) ⊂ ℝᵐ : orthonormal basis for the reachable outputs
col = orth(A)
print("C(A) basis (cols), dim =", col.shape[1])

# 2. Null space N(A) ⊂ ℝⁿ : inputs crushed to zero
nul = null_space(A)
print("N(A) basis (cols), dim =", nul.shape[1])
print("   check A @ null ≈ 0:", np.allclose(A @ nul, 0))

# 3. Row space C(Aᵀ) ⊂ ℝⁿ : orthonormal basis for meaningful inputs
row = orth(A.T)
print("C(Aᵀ) basis, dim     =", row.shape[1])

# 4. Left null space N(Aᵀ) ⊂ ℝᵐ : unreachable output directions
lnul = null_space(A.T)
print("N(Aᵀ) basis, dim     =", lnul.shape[1])
print("   check Aᵀ @ lnull ≈ 0:", np.allclose(A.T @ lnul, 0))

# --- The Fundamental Theorem, verified numerically ---
print("\nFUNDAMENTAL THEOREM")
print(f"  input  ℝⁿ:  dim C(Aᵀ) + dim N(A)  = {row.shape[1]} + {nul.shape[1]} = {n}  (= n)")
print(f"  output ℝᵐ:  dim C(A)  + dim N(Aᵀ) = {col.shape[1]} + {lnul.shape[1]} = {m}  (= m)")
print(f"  row rank == col rank == r :", row.shape[1] == col.shape[1] == r)

# Orthogonality: row space ⊥ null space (every meaningful input ⊥ every crushed one)
print("  C(Aᵀ) ⊥ N(A)?  ", np.allclose(row.T @ nul, 0))
```

Watch what the output proves: the rank is `2`, the null space has dimension
`n − r = 2`, the left null space has dimension `m − r = 1`, and the two pairs sum to
`n` and `m` exactly. The final check confirms the row space and null space are
genuinely perpendicular — the input space `ℝ⁴` cleanly split into "kept" and
"crushed" halves.

---

## Section recap

- Every matrix `A` (`m×n`) defines **four subspaces**:
  - `C(A)` — column space, what it can **reach** (in `ℝᵐ`, dim `r`).
  - `N(A)` — null space, what it **destroys** (in `ℝⁿ`, dim `n − r`).
  - `C(Aᵀ)` — row space, the **meaningful inputs** (in `ℝⁿ`, dim `r`).
  - `N(Aᵀ)` — left null space, the **unreachable outputs** (in `ℝᵐ`, dim `m − r`).
- **Fundamental theorem:** `dim C(A) = dim C(Aᵀ) = r` (row rank = column rank), and
  the dimensions add to `n` (input side) and `m` (output side). Orthogonal pairs.
- Nothing is lost — only **sorted** into kept vs. crushed.

**Explain out loud:** Without notes — *"The four subspaces are ___, ___, ___, ___.
Two live in the input space and two in the output. The fundamental theorem says ___,
and the dimensions add to ___ on each side."*

---

## Memory tier update — Section 05

**🔥 CARRY (memorize):**
- The four: `C(A)` reach, `N(A)` destroy, `C(Aᵀ)` row/meaningful, `N(Aᵀ)` unreachable.
- Row rank = column rank = `r` (the hinge).
- Dimensions add: `r + (n−r) = n` (input), `r + (m−r) = m` (output).

**🔧 RECONSTRUCT (re-derive when needed):**
- Which space each subspace lives in (`ℝⁿ` vs `ℝᵐ`) — derive from "input side vs
  output side."
- Why row space ⊥ null space (a meaningful input direction can't also be crushed).

**📖 LOOKUP (reference, never memorize):**
- `scipy.linalg.null_space` / `orth` and their SVD-based internals.
- RREF-based hand methods for extracting each basis.

---

## Cross-modal — try it in the wild

**Try this in Hermes:** Build a random `4×6` matrix, force it to rank 3 (make 3
columns combinations of the others), and compute the dimensions of all four
subspaces. Verify they sum to `6` and `4`. Then confirm `C(A) ⊥ N(Aᵀ)` numerically —
feel the output space splitting in two.

**Try this in Claude:** Ask Claude to connect the four subspaces to **least squares**:
"if `b` isn't in `C(A)`, where does the error vector live, and which subspace does
the projection land in?" The answer ties `N(Aᵀ)` directly to the residual — a
preview of the next foundations file.

**Reflection prompt:** "What can this function reach, and what does it throw away?"
is a question you ask of code constantly — a lossy compression, a hash, a projection
in a serializer. Journal one line linking a lossy transform from your engineering to
the column-space/null-space split: what it keeps vs. what it crushes.
