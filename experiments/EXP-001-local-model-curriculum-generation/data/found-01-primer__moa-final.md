```yaml
module: M01
title: "Linear Algebra for ML"
artifact: foundations-primer
section: "01 — Primer"
calibration: "MIT 18.06 (Strang)"
formalism_density: 0.4
status: draft
learner_id: L001
```

# Linear Algebra Primer

In this primer we’ll bridge your intuition from spreadsheets and arrays in programming with the formal definitions of vectors, vector spaces, matrices, and linear maps.

## Vectors as Objects

Think of a **vector** as a one-dimensional array or a “row” of numbers. For instance, when you work with data in Python (using NumPy), a vector might be an array like:

  • `[height, weight, age]`  
  • `np.array([175, 70, 32])`

Formally, a vector is an ordered list of elements that represents a point or direction in some space. In linear algebra we denote vectors with bold lowercase letters (e.g., **v**, **u**).

## Vector Spaces and Closure

Imagine a spreadsheet where every row obeys two simple rules:
  
1. **Closure under addition**: If you take any two rows, adding them together gives another valid row.
2. **Closure under scalar multiplication**: Multiplying any entry by a number (a real scalar) produces yet another valid row.

A **vector space** is the collection of all such vectors that satisfy these rules. For example, in ℝ² (the 2-dimensional space), every vector has the form `[x, y]` and if you add or scale any two such vectors, the result remains a vector in ℝ².

## Basis & Dimension

A **basis** is the “building block” set of vectors that can be combined (via addition and scaling) to represent any vector in the space. Think of it as choosing the minimal number of independent directions needed to rebuild every row in your spreadsheet.

For instance, the standard basis for ℝ² is:

  • e₁ = [1, 0]  
  • e₂ = [0, 1]

Any vector `[a, b]` can be written as a combination: a·[1, 0] + b·[0, 1]. The number of vectors in the basis is called the **dimension**. Here, ℝ² has dimension 2.

## Linear Maps as Functions

A **linear map** (or linear transformation) is simply a function between vector spaces that preserves both addition and scalar multiplication. Consider the example:

  • f(x, y) = [y, x]

This swaps the components of any 2D vector while preserving linearity. In machine learning models such as neural networks or linear regression, you often apply linear maps to transform data.

## Matrices as Spreadsheets

In your programming experience you’re already comfortable with arrays and tables. In linear algebra, a **matrix** is a rectangular array of numbers organized in rows and columns (e.g., an m×n matrix). A key fact is that matrices represent linear maps: for instance, given a basis {e₁, e₂} in ℝ², the matrix

  • A = [T(e₁) T(e₂)]  
    where each column represents how the transformation acts on one of the basis vectors.

Thus, if you have an input vector **v** in ℝ², then A · **v** gives you the transformed output vector. Matrices are everywhere: from transforming features to building layers in neural networks.

## Rank-Nullity Theorem

Every linear map has two essential spaces:

1. **Rank (Column Space)** – This is the set of all possible outputs; its dimension tells us how many independent directions are preserved by the transformation.
2. **Nullity (Kernel)** – These are the inputs that get mapped to zero.

The Rank-Nullity Theorem states that for a linear map T: ℝⁿ → ℝᵐ:

  • rank(T) + nullity(T) = n

This theorem is a “data compression” rule in machine learning. It tells us how much information from the input is preserved (rank) versus lost (nullity).

## ML Payoff

- **Feature Representation**: Each data point is a vector, and matrices act as transformations that can rotate or scale these feature vectors.
- **Linear Models**: Methods like linear regression apply linear maps to predict outcomes based on input features.
- **Dimensionality Reduction**: Techniques such as Principal Component Analysis (PCA) find a new basis with maximal rank, effectively compressing data while preserving essential information.

## Computational Example

Below is an example in Python using NumPy that demonstrates how to create vectors, matrices, and apply them:

```python
import numpy as np

# Create a vector in R^3
v = np.array([2, 5, -1])
print("Vector v:", v)

# Define a matrix (linear map) acting on R^3 -> R^3
A = np.array([[1, 0, 0],
              [0, -1, 0],
              [0, 0, 2]])

# Apply the linear transformation A to vector v
result = A @ v
print("Transformed Vector (A @ v):", result)
```

In this example, each column of A tells you how one of the standard basis vectors is transformed. The output shows how A maps the input vector **v**.

## Tiered Memory Summary

| Tier         | What to Remember                                         |
|--------------|----------------------------------------------------------|
| **CARRY**    | 1. Vector = ordered list (like a spreadsheet row)      |
|              | 2. Basis = minimal set that spans the space             |
|              | 3. Matrix = representation of a linear map              |
|              | 4. Rank-nullity theorem: rank + nullity = input dimension |
| **RECONSTRUCT** | 1. How to form a matrix from T(eᵢ) for basis vectors    |
|              | 2. Solving A·v = 0 (finding the null space)             |
| **LOOKUP**   | 1. Detailed properties of specific operations           |

## Explain-Out-Loud Check

Take a moment to explain, out loud: “What’s the difference between a vector and a matrix?” Reflect on how vectors represent single data points or directions, whereas matrices act as functions that transform one vector into another. If you find any part unclear, review that section until it feels intuitive.

Happy learning!
```