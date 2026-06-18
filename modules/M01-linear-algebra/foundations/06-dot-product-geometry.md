---
module: M01
title: "Linear Algebra for ML"
artifact: foundations-primer
section: "06 — Dot Product, Norm, and Projection"
calibration: "MIT 18.06 (Strang), Lectures 14–16"
formalism_density: 0.4
status: draft
learner_id: L001
prereq: "foundations/05-four-subspaces.md"
---

# Section 06 — Dot Product, Norm, and Projection

> So far the space has been *flat* — we could add and scale, but we couldn't measure
> anything. No lengths, no angles, no "how close are these two vectors?" This file
> installs the **measuring tool**: the dot product. From it flows length (**norm**),
> distance (**metric**), alignment (**orthogonality**), and the workhorse operation
> of ML geometry — **projection**, which is what least-squares regression secretly
> is.

---

## 1. The dot product — "how much do these vectors align?"

**Bridge.** Give me two vectors. I want a single number answering: *do they point
the same way, opposite ways, or are they unrelated?* The **dot product** is that
number. Multiply matching entries and sum them up — and that humble arithmetic turns
out to encode the *angle* between the vectors. It's the one tool that converts
algebra (entries) into geometry (angles and lengths).

**Definition.** For `u, v ∈ ℝⁿ`, the **dot product** (a.k.a. inner product) is

```
u · v  =  u₁v₁ + u₂v₂ + … + uₙvₙ  =  Σᵢ uᵢ vᵢ        (a single scalar)
```

**Inline symbols.** `u · v` (or `⟨u, v⟩`) — the dot product, a number. The geometric
identity that makes it powerful:

```
u · v  =  ‖u‖ ‖v‖ cos θ
```

where `θ` is the angle between them and `‖·‖` is length (next section). Read it
operationally: the dot product is **large and positive** when vectors align, **zero**
when perpendicular, **negative** when opposed. It's an *alignment meter*.

> **Try it on intuition:** `u · v > 0` → "roughly same direction." `= 0` →
> "unrelated / perpendicular." `< 0` → "roughly opposed." That sign is the first
> thing ML cares about (cosine similarity is built on it).

---

## 2. From dot product to norm (length) to distance (metric)

**Bridge.** A vector dotted with *itself* can only measure one thing — its own
length, squared. (Same direction as itself, perfectly aligned.) So **length falls
out of the dot product for free**, and once you have length, "distance between two
points" is just "length of the difference."

**Norm (length).** The **norm** of `v` is

```
‖v‖  =  √(v · v)  =  √(v₁² + v₂² + … + vₙ²)
```

This is the Euclidean length — Pythagoras in `n` dimensions. `‖v‖` is read "norm of
v" or "length of v."

**Distance (metric).** The distance between two vectors is the norm of their gap:

```
dist(u, v)  =  ‖u − v‖
```

This is the **metric** — the function that says how far apart two points are. It's
the L2 distance you've used in k-NN, in clustering, in loss functions, a thousand
times.

> Chain to carry: **dot product → (dot with self) → norm/length → (norm of the
> difference) → distance.** Three ideas, one root.

---

## 3. Orthogonality — zero alignment

**Bridge.** The special case `u · v = 0` deserves its own name because it's
everywhere. It means the alignment meter reads *zero* — the vectors are
**perpendicular**, contributing nothing to each other's direction. In the
four-subspaces file, "orthogonal complement" was exactly this idea applied to whole
subspaces.

**Definition.** `u` and `v` are **orthogonal** iff `u · v = 0`. A set of vectors that
are mutually orthogonal *and* unit-length (`‖·‖ = 1`) is **orthonormal** — the
cleanest possible basis, because each coordinate is read off by a single dot product
with no interference between directions.

> Why ML loves orthogonality: orthogonal directions are *independent information* —
> no redundancy, no leakage. PCA hands you orthogonal axes on purpose. Orthonormal
> bases (the `Q` in QR) make least squares numerically stable. Perpendicular = clean.

---

## 4. Projection — onto a line, then onto a plane

**Bridge.** Here's the operation that earns this whole file. You have a vector `b`,
and a direction (or a subspace) you're allowed to live on. **Projection** finds the
point *on that allowed set* that's **closest** to `b` — the shadow `b` casts onto the
subspace. The leftover, `b − projection`, is perpendicular to the subspace (it's the
unavoidable error). That "closest point + perpendicular error" split is the entire
logic of least squares.

**Projection onto a line** (direction `a`). The shadow of `b` onto the line through
`a` is:

```
proj_a(b)  =  ( (a · b) / (a · a) ) · a
```

Read it: `(a·b)/(a·a)` is *how many copies of `a`* you need; multiply by `a` to land
on the line. The coefficient is the alignment, normalized by `a`'s own length.

**Projection onto a subspace** (columns of a matrix `A`). When the "allowed set" is
the column space `C(A)` (from Section 05!), the projection of `b` is:

```
p  =  A (AᵀA)⁻¹ Aᵀ b          and the projection matrix is  P = A(AᵀA)⁻¹Aᵀ
```

`P` is the operator that casts *any* `b` onto `C(A)`. The error `b − p` lands in the
left null space `N(Aᵀ)` — perpendicular to everything `A` can reach. **That `(AᵀA)⁻¹Aᵀ`
is the normal-equations solution of least squares.** Projection *is* regression.

---

## 5. Python: projection from scratch, and least squares in 2-D

We'll build the projection operator by hand, confirm the error is perpendicular, and
then fit a line to noisy data as a projection onto a column space — watching the
geometry and the regression be the *same computation*.

```python
import numpy as np

# --- 1. Projection onto a line through `a` -------------------------------
a = np.array([2., 1.])
b = np.array([1., 3.])

coeff = (a @ b) / (a @ a)            # how many copies of a we need
p = coeff * a                        # the shadow of b on the line
err = b - p                          # the leftover
print("projection of b onto line:", np.round(p, 3))
print("error ⊥ line?  a·err ≈ 0 :", np.isclose(a @ err, 0.0))   # True

# --- 2. Norm & distance fall out of the dot product ----------------------
print("\n‖b‖ = √(b·b):", np.sqrt(b @ b), " == np.linalg.norm:", np.linalg.norm(b))
print("dist(a,b) = ‖a-b‖:", np.linalg.norm(a - b))

# --- 3. Least squares in 2-D AS a projection onto a column space ---------
# Fit y ≈ slope·t + intercept to noisy data.
rng = np.random.default_rng(0)
t = np.linspace(0, 5, 20)
y = 2.0 * t + 1.0 + rng.normal(scale=0.4, size=t.size)   # true slope 2, intercept 1
A = np.column_stack([t, np.ones_like(t)])                # columns: [t, 1]

# Projection matrix onto C(A), then project y — the normal equations.
P = A @ np.linalg.inv(A.T @ A) @ A.T     # the projection operator onto C(A)
y_hat = P @ y                            # fitted values = projection of y
beta = np.linalg.inv(A.T @ A) @ A.T @ y  # [slope, intercept] = the regression coeffs
print("\nfitted [slope, intercept]:", np.round(beta, 3))     # ≈ [2, 1]

# The residual lives in the LEFT NULL SPACE — perpendicular to every column of A.
resid = y - y_hat
print("residual ⊥ columns of A?  Aᵀ·resid ≈ 0:", np.allclose(A.T @ resid, 0, atol=1e-9))
```

The punchline is the last check: the residual is perpendicular to the columns of `A`,
which means it sits in `N(Aᵀ)` from the four-subspaces file. Least squares didn't
"minimize a loss" by magic — it **dropped a perpendicular** onto the column space.
The closest reachable point *is* the projection. Geometry and regression were the
same act all along.

---

## Section recap

- The **dot product** `u · v = Σ uᵢvᵢ = ‖u‖‖v‖cos θ` is the alignment meter:
  positive = aligned, zero = perpendicular, negative = opposed.
- **Norm** `‖v‖ = √(v·v)` is length; **distance** `‖u − v‖` is the metric. Both fall
  out of the dot product.
- **Orthogonal** = dot product zero = independent, non-redundant directions.
  Orthonormal bases are the cleanest.
- **Projection** finds the closest point on an allowed subspace; the error is
  perpendicular. `P = A(AᵀA)⁻¹Aᵀ` projects onto `C(A)` — and *that is least squares*.

**Explain out loud:** Without notes — *"The dot product measures ___. Length is ___
and distance is ___. Orthogonal means ___. Projection finds ___, and least squares
is really just ___."*

---

## Memory tier update — Section 06

**🔥 CARRY (memorize):**
- Dot product = alignment; `u·v = ‖u‖‖v‖cos θ`; zero = perpendicular.
- Norm `‖v‖ = √(v·v)`; distance `‖u−v‖`.
- Projection = closest point on a subspace; error ⊥ subspace; least squares = projection.

**🔧 RECONSTRUCT (re-derive when needed):**
- Line projection `((a·b)/(a·a))a` — rebuild from "how many copies of `a`."
- Why the residual is orthogonal to `C(A)` (it lands in `N(Aᵀ)`).
- The normal-equations form `P = A(AᵀA)⁻¹Aᵀ`.

**📖 LOOKUP (reference, never memorize):**
- Other norms (L1, L∞, Frobenius) and when each is used.
- Numerically stable least squares via QR/SVD instead of `(AᵀA)⁻¹` (see theory/05).

---

## Cross-modal — try it in the wild

**Try this in Hermes:** Implement cosine similarity (`u·v / (‖u‖‖v‖)`) and test it on
three pairs of vectors — aligned, perpendicular, opposed — confirming the values land
near `+1`, `0`, `−1`. Then project a vector onto a 2-D plane (two columns) and verify
the residual is orthogonal to *both* columns.

**Try this in Claude:** Ask Claude why we *can't* just invert `A` to solve `Ax = b`
when `A` is tall (more equations than unknowns), and how projection rescues us. Have
it connect "no exact solution exists" to "`b` isn't in `C(A)`" from Section 05.

**Reflection prompt:** "Find the closest valid point to what I actually want" is a
pattern you've coded — snapping to a grid, clamping to a range, nearest-neighbor
lookup. Journal one line linking a "snap to the nearest legal value" move from your
work to projection onto a subspace.
