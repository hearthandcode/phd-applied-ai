---
module: M01-linear-algebra
type: assessment-items
source: Strang "Introduction to Linear Algebra" 5th ed. + MIT 18.06 OCW problem sets
status: DRAFT — review against source material before finalizing
pre-registration-status: NOT YET PRE-REGISTERED
---

# M01 Assessment Items

> **Pre-registration rule:** This file must be committed to git before beginning any M01 study session. The commit hash serves as timestamp evidence that questions preceded study. Do not modify Layer 1 items after study starts. Layer 2 and Layer 3 items may be refined before study begins but not after.

---

## Layer 1 — Standardized Recall (External sourced)

Source: Strang "Introduction to Linear Algebra" (5th ed.) and MIT 18.06 OCW.  
Scoring per item: 0 (absent or wrong), 1 (partial), 2 (correct with minor gaps), 3 (complete and correct).  
Max score: 30.

**L1-01.** State the definition of a vector space over a field F. List at least six of the eight axioms.

**L1-02.** What is the difference between a field and a ring? Give one example of each.

**L1-03.** Let A be an m×n matrix. Define the four fundamental subspaces of A. For each, state its ambient space (Rⁿ or Rᵐ) and its dimension in terms of rank(A).

**L1-04.** State the rank-nullity theorem. What is its geometric interpretation for a linear map T: Rⁿ → Rᵐ?

**L1-05.** Define linear independence for a set of vectors {v₁, ..., vₖ}. What is the relationship between linear independence and the definition of a basis?

**L1-06.** Describe the algorithm for Gaussian elimination. What does row reduction preserve about the solution set of Ax = b, and why?

**L1-07.** Define the projection of vector b onto the column space of matrix A. Write the formula for the projection matrix P in terms of A.

**L1-08.** State the spectral theorem for real symmetric matrices. What does it guarantee about their eigenvalues and eigenvectors?

**L1-09.** State the SVD theorem: every matrix A ∈ Rᵐˣⁿ can be written as A = UΣVᵀ. What are U, Σ, V, and what properties do each have?

**L1-10.** Define a symmetric positive definite matrix. Give two equivalent conditions for a matrix to be positive definite.

---

## Layer 2 — Integration Probes (Custom)

Scored qualitatively after module completion. Target: evidence of structural understanding — prior knowledge rearranged around new concepts, not just new facts added.

Scoring scale (unless noted): 0 = no structural connection | 1 = connection named but not explained | 2 = structural explanation present | 3 = explanation with novel framing or generalization.

**L2-01 (Spatial/relational).** Draw or describe in your own words the relationship between the null space and the column space of A. Why are they orthogonal complements, and what does that mean geometrically?

**L2-02 (Cascade trace).** Why does the definition of a vector space require a field of scalars rather than just any set? What specific algebraic property would fail without the field's multiplicative inverses?

**L2-03 (Surprise capture).** What concept or result in M01 most changed something you thought you already understood from previous math exposure? Describe what changed and why it changed.  
*Scoring: qualitative only — note whether the change is structural (prior concept rearranged) vs. additive (new fact attached to existing structure).*

**L2-04 (Novel application).** Describe a matrix factorization problem that arises naturally in machine learning. Which M01 concepts does it use, and why are those concepts necessary rather than incidental? Do not use an example from any study material.

**L2-05 (Structural explanation).** Eigendecomposition applies only to square matrices; SVD applies to any matrix. Explain in your own words why this is the case — what is it about the geometry of eigendecomposition that requires squareness?

**L2-06 (Meta-cognitive).** After completing M01, which concept can you explain fluently and which can you only reproduce mechanically? Describe the difference in how they feel cognitively.  
*Scoring: qualitative only — this feeds the RQ2 knowledge integration analysis.*

---

## Layer 3 — Cascade Pre-Registration

> **Instructions:** Before beginning any M01 study session, write your predictions below and commit this file to git. The commit hash is your pre-registration timestamp. Predictions will be scored against M02 and M03 assessments — not before. Do not modify predictions after committing.

**Pre-registration date:** _______ *(fill in before committing)*  
**Git commit hash:** _______ *(fill in after committing)*

### Prediction task

List 5–8 M01 concepts you predict will reappear as prerequisites in M02 (Multivariate Calculus for ML) or M03 (Probability and Statistics for ML). For each, write one sentence explaining why you expect it to be needed.

1. ___
2. ___
3. ___
4. ___
5. ___
6. ___
7. ___
8. ___

### Scoring rubric *(fill in after M02/M03 completion)*

For each prediction: **CORRECT** (concept appeared as predicted) | **PARTIAL** (concept appeared but for different reasons) | **INCORRECT** (concept not needed) | **UNEXPECTED** (concept appeared but wasn't predicted).

| # | Prediction | Status | Notes |
|---|-----------|--------|-------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |

**Accuracy score:** ___/8 *(CORRECT + PARTIAL × 0.5)*
