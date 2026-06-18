---
module: M01
title: "Linear Algebra for ML"
artifact: foundations-primer
section: "04 — Independence, Basis, Dimension"
calibration: "MIT 18.06 (Strang) — foundations supplement"
formalism_density: 0.4
status: draft
learner_id: L001
prereq: "foundations/03-vector-spaces-deep.md"
---

# Section 04 — Independence, Basis, Dimension

> Section 03 ended on the one fundamental operation: the **linear combination**.
> This file uses it to build the three ideas that let you *name* every point in a
> space with the fewest possible numbers: **independence** (no redundancy),
> **basis** (a minimal naming alphabet), and **dimension** (the size of that
> alphabet). Then: how to re-name the same vector in a different alphabet — **change
> of basis** — which is half of what neural networks do all day.

---

## 1. Linear independence — "no direction is a shortcut through the others"

**Bridge.** Suppose someone hands you three directions to navigate a space. If one
of them is just "go a bit north and a bit east" — i.e. it's reachable by combining
the other two — then it's **redundant**. It adds no new reach. A set of vectors is
**linearly independent** when *none* of them is a shortcut built from the others:
every vector contributes a genuinely new direction.

**Definition (the clean test).** Vectors `v₁, …, vₖ` are **linearly independent**
if the *only* way to write the zero vector as a linear combination

```
α₁v₁ + α₂v₂ + … + αₖvₖ  =  0
```

is the boring one where **every `αᵢ = 0`**. If some *nonzero* choice of scalars also
hits `0`, the vectors are **dependent** — and that nonzero relation is literally the
recipe showing one vector is a combination of the rest.

**Inline symbols.** `αᵢ ∈ F` — the scalar weights. `0` — the zero vector. The phrase
"only the trivial solution" means "all weights forced to zero."

**The one-liner to carry:**
> Independent = no vector is a linear combination of the others = the only way to
> mix them down to zero is to use nothing at all.

---

## 2. Span + independence = basis

**Bridge.** Two separate jobs a set of vectors might do:
- **Span**: their linear combinations *reach every point* in the space (full
  coverage — nothing is missed).
- **Independent**: they have *no redundancy* (nothing is wasted).

A set that does *both* — reaches everything **and** wastes nothing — is a **basis**.
It's the Goldilocks set: just enough vectors to name the whole space, not one more.

**Definition.** A **basis** of a vector space `V` is a set of vectors that is
1. **spanning** — every `v ∈ V` is *some* linear combination of them, and
2. **linearly independent** — that combination is **unique** (no redundancy).

The magic consequence of "both at once": **every vector has exactly one address.**
Spanning guarantees an address exists; independence guarantees it's unique. Those
addresses — the scalar weights — are the vector's **coordinates** in that basis.

**Example to anchor it.** In `ℝ³`, the standard basis is
`e₁ = (1,0,0), e₂ = (0,1,0), e₃ = (0,0,1)`. Any vector `(x, y, z)` is uniquely
`x·e₁ + y·e₂ + z·e₃`. The coordinates *are* the entries — which is exactly why the
standard basis feels invisible. Other bases re-shuffle those addresses.

---

## 3. Dimension — the size of the alphabet

**Bridge.** Here's a quietly profound fact: *every* basis of a given space has the
**same number of vectors**. You cannot describe `ℝ³` with two basis vectors (they'd
fail to span — a plane can't cover a volume) nor do you need four (the fourth would
be redundant). That fixed count is the space's **dimension** — the length of the
minimal alphabet needed to name any point.

**Definition.** `dim V` ("dimension of V") = the number of vectors in any basis of
`V`. It's well-defined precisely because all bases have equal size.

> Dimension = how many independent coordinates you need to pin down a point =
> the size of the naming alphabet.

**Why ML cares (a lot).** Dimension is *the* currency of representation:
- An embedding in `ℝ⁷⁶⁸` has 768 independent coordinates — 768 dials to describe one
  token. That number is a modeling choice about how much room meaning gets.
- "Intrinsic dimension" — the idea that real data secretly lives on a low-dimensional
  surface inside a high-dimensional space — is the entire premise of dimensionality
  reduction (PCA, autoencoders). Fewer *real* directions than ambient coordinates.
- **Rank** (you'll meet it next section) is just "the dimension of the space a matrix
  can actually reach." Same idea, applied to a map.

---

## 4. Change of basis — the same vector, a new address

**Bridge.** A vector is a *thing in the world* — an arrow, a data point — and it
doesn't change when you describe it differently. But its **coordinates** absolutely
do, depending on which basis (which alphabet) you read it in. Change of basis is the
translation rule between two coordinate systems for the *same* underlying vectors.
This is not bookkeeping trivia — it's the move behind PCA ("re-describe the data in
the directions of greatest variance"), behind every rotation, and behind what each
layer of a network does to its inputs.

**The mechanics (light).** Suppose `B` is a matrix whose **columns are your new
basis vectors**, written in the old (standard) coordinates. Then:

- To go **from new coordinates `c` → old coordinates `x`**: `x = B c`. (You're
  literally taking the linear combination of new-basis vectors with weights `c`.)
- To go **from old `x` → new `c`**: invert it, `c = B⁻¹ x`.

So `B` and `B⁻¹` are the two-way dictionary. The vector `x` never moved; you just
asked "what are your weights in *this* alphabet instead?"

**Inline symbols.** `B` — change-of-basis matrix (new basis as columns, in old
coords). `c` — coordinates of a vector in the new basis. `x` — same vector's
coordinates in the old/standard basis.

---

## 5. Python: independence via rank, and a basis change

We'll do two computational things. First, **check independence** the way real code
does — via **rank** (the number of genuinely independent directions; full theory next
section, but we can use it now). Second, **change basis** on a concrete vector and
confirm the vector itself is unchanged — only its coordinates differ.

```python
import numpy as np

# --- 1. Independence check via rank -------------------------------------
# Stack vectors as columns; rank = number of independent directions.
def independent(*vecs):
    M = np.column_stack(vecs)
    r = np.linalg.matrix_rank(M)
    return r == len(vecs), r

a = np.array([1., 0., 0.])
b = np.array([0., 1., 0.])
c = np.array([1., 1., 0.])           # c = a + b  → redundant!

print("a, b independent? ", independent(a, b))          # (True, 2)
print("a, b, c independent?", independent(a, b, c))      # (False, 2) — c is a shortcut
# The nonzero relation a + b - c = 0 is the witness to dependence:
print("a + b - c =", a + b - c)                          # [0 0 0]

# --- 2. Change of basis -------------------------------------------------
# New basis vectors (in standard coords) as COLUMNS of B.
B = np.array([[1., 1.],
              [0., 2.]])             # new basis: u1=(1,0), u2=(1,2)
B_inv = np.linalg.inv(B)

x = np.array([3., 4.])               # a vector, in STANDARD coordinates
c_new = B_inv @ x                    # its coordinates in the NEW basis
print("\nx in standard coords :", x)
print("x in new-basis coords :", np.round(c_new, 3))

# Reconstruct: take the linear combination of new-basis vectors with weights c_new
x_back = B @ c_new
print("rebuilt from new coords:", np.round(x_back, 3), " same vector?",
      np.allclose(x_back, x))         # True — the vector never moved
```

Two lessons land here. The rank check shows `c = a + b` collapses the rank from 3 to
2 — the redundancy is *visible* as a missing dimension. And the basis change shows the
same physical vector `(3, 4)` wearing two different coordinate outfits, with `B` and
`B⁻¹` as the dressing room. PCA, you'll later see, is nothing but a *clever* choice of
`B`.

---

## Section recap

- **Linear independence** = no vector is a combination of the others = the only way
  to mix them to `0` is all-zero weights.
- A **basis** does both jobs at once: **spans** (reaches everything) and is
  **independent** (no redundancy) → every vector gets a *unique* address.
- **Dimension** = the size of any basis (all bases tie). It's the count of
  independent coordinates — the currency of representation in ML.
- **Change of basis**: the vector is fixed; its coordinates depend on the alphabet.
  `x = Bc` (new→old), `c = B⁻¹x` (old→new). PCA is a smart basis choice.

**Explain out loud:** Without notes — *"Independent means ___. A basis is the set
that ___ and ___, so every vector has ___. Dimension is ___. And changing basis
keeps ___ fixed while ___ changes."*

---

## Memory tier update — Section 04

**🔥 CARRY (memorize):**
- Independent = only the all-zero combination gives `0`.
- Basis = spanning **and** independent → unique coordinates.
- Dimension = size of any basis (all bases equal size).

**🔧 RECONSTRUCT (re-derive when needed):**
- Why every basis has the same size (over-spanning → redundancy; under-spanning →
  gaps).
- Change-of-basis formulas `x = Bc`, `c = B⁻¹x` — rebuild from "columns of B are the
  new basis."

**📖 LOOKUP (reference, never memorize):**
- `np.linalg.matrix_rank` tolerance behavior and SVD-based rank computation.
- Coordinate-vector / matrix-of-a-linear-map formalism details.

---

## Cross-modal — try it in the wild

**Try this in Hermes:** Generate a random `5×5` matrix, confirm its columns are
independent (rank 5), then overwrite the last column with the sum of the first two
and watch the rank drop to 4. Print the nonzero relation that witnesses the
dependence. Then pick a non-standard basis and round-trip a vector through `B⁻¹`
and `B`, asserting it returns unchanged.

**Try this in Claude:** Ask Claude to explain PCA *purely* as a change of basis —
"which `B` does PCA choose, and why those directions?" — without yet invoking
eigenvalues. See if you can predict the answer (variance-maximizing directions)
before reading it.

**Reflection prompt:** "Find the minimal set that covers everything without
redundancy" is a problem you've solved in code — deduplicating a dependency set,
choosing a minimal spanning set of feature flags. Journal one line connecting a
"minimal non-redundant cover" from your engineering to the idea of a basis.
