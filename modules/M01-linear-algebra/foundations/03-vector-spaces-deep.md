---
module: M01
title: "Linear Algebra for ML"
artifact: foundations-primer
section: "03 — Vector Spaces from First Principles"
calibration: "MIT 18.06 (Strang) — foundations supplement"
formalism_density: 0.4
status: draft
learner_id: L001
prereq: "foundations/02-fields-number-systems.md"
---

# Section 03 — Vector Spaces from First Principles

> The primer gave you the one-line intuition: *a vector space is a universe where
> add & scale never kick you out.* Section 02 nailed down the **field** `F` — the
> numbers you scale by. Now we build the universe properly: `V` over `F`, the eight
> axioms (demystified), subspaces, and the single operation everything reduces to —
> the **linear combination**.

---

## 1. The setup: a space `V` standing on a field `F`

**Bridge.** Picture two ingredients. First, a field `F` (from Section 02) — your
numbers, almost always `ℝ`. Second, a set `V` ("vee") of *things you can add to each
other*. The things in `V` are **vectors** — but "vector" here means anything that
plays by the rules, not just arrows. Glue them with two operations: **add two
vectors** (`v + w`), and **scale a vector by a number from the field** (`α · v`,
where `α ∈ F`). A *vector space* is the pair `(V, F)` plus the promise that those
operations never throw you out of `V`.

**Inline symbols.** `V` — the space (the set of vectors). `F` — the field of scalars
underneath it. `v, w ∈ V` — vectors living in the space. `α, β ∈ F` — scalars.
`0` (bold) — the **zero vector**, the one vector that adds to nothing.

The phrase to keep: **"V over F."** A real vector space is "V over `ℝ`." Swap the
field and you get a complex vector space "V over `ℂ`" — same rules, different ground
(exactly the dial from Section 02).

---

## 2. The eight axioms — "rules that let us do algebra without coordinates"

**Bridge.** Don't memorize eight cryptic lines. Here's the honest framing: the
axioms are the *minimum promises* you need so that ordinary algebra — rearranging,
factoring, cancelling — works on vectors **even when you refuse to write down their
coordinates.** That's the whole superpower. Once these hold, you can manipulate
`αv + βw` like a high-school expression, and every step is guaranteed legal, whether
`v` is a 3-vector or a 768-dim embedding or a function.

The eight, grouped so they actually make sense:

**Addition behaves (4 rules):**
1. Commutative: `v + w = w + v`
2. Associative: `(u + v) + w = u + (v + w)`
3. Identity: there's a `0` with `v + 0 = v`
4. Inverse: every `v` has a `−v` with `v + (−v) = 0`

**Scaling behaves and plays well with addition (4 rules):**
5. Scalar identity: `1 · v = v`
6. Scalars compose: `α(βv) = (αβ)v`
7. Distribute over vector addition: `α(v + w) = αv + αw`
8. Distribute over scalar addition: `(α + β)v = αv + βv`

> **The one sentence:** these eight rules say *add and scale, in any order or
> grouping, and the algebra you already know still works — without ever needing
> coordinates.*

Rules 1–4 are "addition is a well-behaved group." Rules 5–8 are "scaling is
consistent with the field and threads cleanly through addition." Closure (the
operations stay in `V`) is assumed throughout — it's the primer's load-bearing wall.

---

## 3. Subspaces — self-contained neighborhoods

**Bridge.** Inside a big space, some subsets are *spaces in their own right* — they
have everything they need to be self-sufficient. Think of a flat plane passing
through the origin inside 3-D space: you can add any two vectors in the plane and
stay in the plane; scale any of them and stay in the plane. The plane is a
**subspace** — a self-contained neighborhood that never needs to borrow from the
rest of `V`.

**Definition (the 3-point test).** A subset `U ⊆ V` ("U is contained in V") is a
**subspace** if:
1. It contains the zero vector `0`.
2. It's **closed under addition**: `u₁, u₂ ∈ U ⟹ u₁ + u₂ ∈ U`.
3. It's **closed under scaling**: `u ∈ U, α ∈ F ⟹ αu ∈ U`.

That's the entire test. If a subset survives all three, it inherits the eight
axioms for free (it's sitting inside a space that already obeys them). The
non-negotiable is **passing through the origin** — any flat thing that misses `0`
fails test 1 and is *not* a subspace.

**Why ML cares.** The **column space** and **null space** you'll meet in the
four-subspaces section are subspaces. The set of all weight configurations a frozen
layer can output is (before the bias and nonlinearity) a subspace. "What can this
linear map reach?" is always answered by a subspace.

---

## 4. Linear combinations — the one operation underneath everything

**Bridge.** Everything in linear algebra — span, basis, dimension, rank, the whole
zoo — is built from **one** move: take some vectors, scale each, add the results. A
**linear combination** of `v₁, …, vₖ` is

```
α₁v₁ + α₂v₂ + … + αₖvₖ        (each αᵢ ∈ F)
```

That's it. Closure (axioms + subspace rules) guarantees the result is still a
vector in `V`. So a linear combination is just *"mix these vectors in some
proportions"* — and the proportions are the scalars.

**This is the operation.** When you later hear:
- **span** = the set of *all* linear combinations of some vectors,
- **subspace** = a set closed under linear combinations,
- **basis** = the smallest set whose linear combinations reach everything,
- **rank** = how many independent directions the combinations actually cover,

— every one of those is the phrase "linear combination" wearing a different hat.
Master this one move and the vocabulary stops being intimidating.

---

## 5. Python: a vector space you can hold in your hands

Let's make the axioms tangible by *implementing* a tiny vector space and checking
the rules numerically. We'll wrap `ℝⁿ`, the most common space, in a small class —
then verify closure, the axioms, and the subspace test.

```python
import numpy as np

class Vec:
    """A vector in ℝⁿ — the space V over the field ℝ.
    Only two operations are exposed: add (+) and scale (·)."""
    def __init__(self, data):
        self.data = np.asarray(data, dtype=float)

    def __add__(self, other):          # vector addition: stays in ℝⁿ (closure)
        return Vec(self.data + other.data)

    def scale(self, alpha):            # scalar multiplication by α ∈ ℝ
        return Vec(alpha * self.data)

    def __repr__(self):
        return f"Vec({self.data})"

# --- check a few of the eight axioms hold ---
rng = np.random.default_rng(0)
u, v, w = (Vec(rng.normal(size=3)) for _ in range(3))
a, b = rng.normal(), rng.normal()

zero = Vec([0, 0, 0])
lhs_distrib = (v + w).scale(a).data                 # a·(v + w)
rhs_distrib = (v.scale(a) + w.scale(a)).data        # a·v + a·w
print("commutative  v+w=w+v :", np.allclose((v + w).data, (w + v).data))
print("identity     v+0=v   :", np.allclose((v + zero).data, v.data))
print("distrib  a(v+w)=av+aw:", np.allclose(lhs_distrib, rhs_distrib))
print("scalars  a(bv)=(ab)v :", np.allclose(v.scale(b).scale(a).data,
                                             v.scale(a * b).data))

# --- a linear combination: the one fundamental operation ---
def lin_comb(coeffs, vecs):
    """α₁v₁ + … + αₖvₖ — mix vectors in given proportions."""
    out = Vec(np.zeros_like(vecs[0].data))
    for c, vec in zip(coeffs, vecs):
        out = out + vec.scale(c)
    return out

combo = lin_comb([2.0, -1.0, 0.5], [u, v, w])
print("\nlinear combination 2u - v + 0.5w =", combo)

# --- subspace test: is the xy-plane {(x, y, 0)} a subspace of ℝ³? ---
def in_xy_plane(vec):                 # the candidate neighborhood
    return np.isclose(vec.data[2], 0.0)

p = Vec([1, 2, 0]); q = Vec([-3, 4, 0])
print("\ncontains 0?           ", in_xy_plane(zero))                 # test 1
print("closed under +?        ", in_xy_plane(p + q))                 # test 2
print("closed under scaling?  ", in_xy_plane(p.scale(7.3)))         # test 3
# A plane that MISSES the origin, e.g. z = 1, fails test 1 → not a subspace.
print("z=1 plane contains 0?  ", in_xy_plane(Vec([0, 0, 1])))       # False
```

The class exposes exactly two doors — add and scale — and nothing you do through
them ever leaves `ℝ³`. That sealed-sandbox feeling *is* the vector space. The
subspace test at the end shows the xy-plane is self-contained, while the parallel
plane `z = 1` flunks on the very first rule because it skips the origin.

---

## Section recap

- A vector space is **`V` over `F`**: a set `V` of vectors plus a field `F` of
  scalars, closed under addition and scaling.
- The **eight axioms** say one thing: *ordinary algebra works on vectors without
  coordinates.* Four make addition well-behaved; four make scaling consistent.
- A **subspace** is a self-contained neighborhood — passes the 3-point test
  (contains `0`, closed under `+`, closed under scaling). Must pass through the
  origin.
- The **linear combination** `α₁v₁ + … + αₖvₖ` is the single operation everything
  else (span, basis, rank) is built from.

**Explain out loud:** Without notes, say — *"A vector space is `V` over `F` where
___. A subspace passes these three tests: ___. And the one operation underneath
span, basis, and rank is ___."*

---

## Memory tier update — Section 03

**🔥 CARRY (memorize):**
- Vector space = `V` over `F`, closed under add & scale.
- Subspace 3-point test: contains `0`, closed under `+`, closed under scaling.
- Linear combination `α₁v₁ + … + αₖvₖ` is *the* fundamental operation.

**🔧 RECONSTRUCT (re-derive when needed):**
- The eight axioms — rebuild from "addition is well-behaved (4) + scaling is
  consistent (4)."
- Why a subspace must contain the origin (set `α = 0` in closure-under-scaling).

**📖 LOOKUP (reference, never memorize):**
- Exotic examples of vector spaces (polynomials, functions, matrices as vectors).
- Formal proofs that the 3-point test implies all eight axioms.

---

## Cross-modal — try it in the wild

**Try this in Hermes:** Extend the `Vec` class to check *all eight* axioms in a loop
over random vectors and scalars, printing a ✅/❌ per axiom. Then write a
`is_subspace(test_fn, samples)` helper that runs the 3-point test on random samples
and try it on the xy-plane vs. the `z = 1` plane. Feel which test the off-origin
plane fails.

**Try this in Claude:** Ask Claude for a *surprising* example of a vector space —
the set of all polynomials of degree ≤ 2, or all 2×2 matrices — and have it walk
through how "add & scale stay in the set" still holds when the "vectors" aren't
arrows at all. This is where the abstraction earns its keep.

**Reflection prompt:** You've written closure checks before without naming them —
every time you validated that an operation kept data in a legal state (a reducer
that returns the same shape, a type that's closed under its own methods). Journal
one line linking a closure invariant from your code to the vector-space axioms.
