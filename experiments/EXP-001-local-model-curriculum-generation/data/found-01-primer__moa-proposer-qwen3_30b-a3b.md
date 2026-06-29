```markdown
---
module: M01
title: "Linear Algebra for ML"
artifact: foundations-primer
section: "01 — Primer"
calibration: "MIT 18.06 (Strang)"
formalism_density: 0.4
status: draft
learner_id: L001
---

# 01 — Primer: Vectors, Spaces, and Maps (The Programmer's Warmup)

> **Conceptual Bridge First**  
> *You know spreadsheets: rows of numbers representing data. Linear algebra is just spreadsheets where rows can be *combined* to create new rows. A vector is a spreadsheet row. A vector space is a collection of rows that *always* stays within the spreadsheet when you combine rows. A basis is the *smallest set of columns* you need to rebuild *any* row in the spreadsheet.*

## 1. Vectors: Your Spreadsheet Rows
**Programmer Anchor:** Think of a vector as a row in your data table (e.g., `[height, weight, age]`). In code, this is a 1D array like `np.array([175, 70, 32])`.

**Formal Definition:**  
A **vector** $\vec{v}$ is an ordered list of numbers. For example, in $\mathbb{R}^3$ (3D space), $\vec{v} = \begin{bmatrix} 2 \\ 5 \\ -1 \end{bmatrix}$.  
*We write vectors as column matrices (stacked numbers) but think of them as rows in your code.*

> **Second Bridge Pass (for Vector Spaces):**  
> Your spreadsheet *only* has rows (vectors) that follow two rules:  
> 1. **Add them**: `[1,2] + [3,4] = [4,6]` (just add corresponding numbers)  
> 2. **Scale them**: `2 * [1,2] = [2,4]` (multiply every number by 2)  
> *If every possible combination of rows (like `a*[1,2] + b*[3,4]`) *stays* in your spreadsheet, you’ve got a vector space.*

---

## 2. Vector Spaces & Closure
**Formal Definition:**  
A **vector space** $V$ over $\mathbb{R}$ is a set of vectors where:  
- **Closure under addition**: If $\vec{u}, \vec{v} \in V$, then $\vec{u} + \vec{v} \in V$.  
- **Closure under scalar multiplication**: If $\vec{v} \in V$ and $c \in \mathbb{R}$, then $c\vec{v} \in V$.  

**Concrete Worked Example**  
Let $V = \left\{ \begin{bmatrix} x \\ y \end{bmatrix} \;\middle|\; x + y = 0 \right\}$ (all 2D vectors where the two numbers sum to zero).  
- **Check closure under addition**:  
  $\vec{u} = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$, $\vec{v} = \begin{bmatrix} 2 \\ -2 \end{bmatrix}$ → $\vec{u} + \vec{v} = \begin{bmatrix} 3 \\ -3 \end{bmatrix}$.  
  $3 + (-3) = 0$ → $\vec{u} + \vec{v} \in V$.  
- **Check closure under scalar multiplication**:  
  $c = 3$, $\vec{v} = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$ → $c\vec{v} = \begin{bmatrix} 3 \\ -3 \end{bmatrix}$.  
  $3 + (-3) = 0$ → $c\vec{v} \in V$.  
✅ *This is a vector space.*

---

## 3. Bases & Dimension
**Programmer Anchor:** A **basis** is like the *minimal columns* in your spreadsheet that let you rebuild *every row* using just addition and scaling (like `SUMPRODUCT` in Excel).

**Formal Definition:**  
A **basis** $B$ for a vector space $V$ is a set of vectors:  
- **Spanning**: Every $\vec{v} \in V$ can be written as $\vec{v} = c_1\vec{b}_1 + c_2\vec{b}_2 + \cdots + c_n\vec{b}_n$ (a linear combination).  
- **Linearly independent**: No basis vector can be written as a combination of the others (e.g., `[1,0]` isn’t a combination of `[0,1]`).  

**Dimension** $\dim(V)$ is the number of vectors in $B$.

**Concrete Example**  
Basis for $\mathbb{R}^2$: $B = \left\{ \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \begin{bmatrix} 0 \\ 1 \end{bmatrix} \right\}$.  
- **Why it spans**: Any vector $\begin{bmatrix} a \\ b \end{bmatrix} = a \begin{bmatrix} 1 \\ 0 \end{bmatrix} + b \begin{bmatrix} 0 \\ 1 \end{bmatrix}$.  
- **Why independent**: You can’t get `[1,0]` from `[0,1]` (no scalar $c$ satisfies $c \cdot [0,1] = [1,0]$).  
✅ $\dim(\mathbb{R}^2) = 2$.

---

## 4. Linear Maps & Matrices
**Programmer Anchor:** A **linear map** is a *spreadsheet transformation* (e.g., "scale height by 2, add weight"). Its **matrix** is the *spreadsheet of how it acts on basis vectors*.

**Formal Definition:**  
A **linear map** $T: \mathbb{R}^n \to \mathbb{R}^m$ satisfies:  
1. $T(\vec{u} + \vec{v}) = T(\vec{u}) + T(\vec{v})$  
2. $T(c\vec{u}) = cT(\vec{u})$  

The **matrix** $A$ representing $T$ is built by:  
$A = \begin{bmatrix} T(\vec{e}_1) & T(\vec{e}_2) & \cdots & T(\vec{e}_n) \end{bmatrix}$  
where $\vec{e}_i$ are standard basis vectors (e.g., $\vec{e}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$).

**Concrete Example**  
Let $T$ scale $x$-coordinate by 2 and $y$-coordinate by 3:  
- $T(\vec{e}_1) = T\left(\begin{bmatrix} 1 \\ 0 \end{bmatrix}\right) = \begin{bmatrix} 2 \\ 0 \end{bmatrix}$  
- $T(\vec{e}_2) = T\left(\begin{bmatrix} 0 \\ 1 \end{bmatrix}\right) = \begin{bmatrix} 0 \\ 3 \end{bmatrix}$  
→ $A = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix}$.  
Now apply to $\vec{v} = \begin{bmatrix} 4 \\ 5 \end{bmatrix}$:  
$A\vec{v} = \begin{bmatrix} 2 & 0 \\ 0 & 3 \end{bmatrix} \begin{bmatrix} 4 \\ 5 \end{bmatrix} = \begin{bmatrix} 8 \\ 15 \end{bmatrix}$  
*Matches: $T(\vec{v}) = [2\cdot4, 3\cdot5] = [8,15]$.*

---

## 5. Rank-Nullity Theorem (The "Info Compression" Rule)
**Why It Matters:** How much *information* gets preserved when you apply a linear map? Rank is preserved info, nullity is lost info.

**Formal Statement:**  
For a linear map $T: \mathbb{R}^n \to \mathbb{R}^m$ represented by matrix $A$:  
$$\text{rank}(A) + \text{nullity}(A) = n$$  
- **Rank** $\text{rank}(A)$: Dimension of the *output space* (how many independent directions $T$ can create).  
- **Nullity** $\text{nullity}(A)$: Dimension of the *null space* (vectors $\vec{v}$ where $A\vec{v} = \vec{0}$).

**Concrete Example**  
$A = \begin{bmatrix} 1 & 2 \\ 2 & 4 \end{bmatrix}$ (scales $x$ by 1, $y$ by 2).  
- **Null space**: $A\vec{v} = \vec{0}$ → $\begin{bmatrix} v_1 + 2v_2 \\ 2v_1 + 4v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$ → $v_1 = -2v_2$.  
  Basis for null space: $\begin{bmatrix} -2 \\ 1 \end{bmatrix}$ → $\text{nullity}(A) = 1$.  
- **Rank**: $A$ has only 1 independent column (columns are scalar multiples) → $\text{rank}(A) = 1$.  
- **Check**: $\text{rank}(A) + \text{nullity}(A) = 1 + 1 = 2 = n$ (since $A$ is $2 \times 2$).

---

## ML Payoff: Why This Matters
- **Feature Vectors**: Every data point (e.g., image pixels, user stats) is a vector in $\mathbb{R}^d$ (where $d$ is features).  
- **Linear Maps = Model Layers**: A neural network layer is a linear map $A$ (matrix) applied to input vectors.  
- **Rank-Nullity = Model Capacity**:  
  - High **rank** (e.g., $A$ has full column rank): Model *preserves all input information* (good for complex tasks).  
  - High **nullity** (e.g., $A$ has redundant columns): Model *collapses input* (e.g., dimensionality reduction like PCA).  
*Example*: PCA finds a basis (matrix $A$) that maximizes $\text{rank}(A)$ for the most important features.

---

## Tiered Memory Summary
| Tier         | What to Remember (Max 7)                                                                 |
|--------------|----------------------------------------------------------------------------------------|
| **CARRY**    | 1. Vector = spreadsheet row (ordered list) <br> 2. Vector space = closed under +/× <br> 3. Basis = minimal spanning set <br> 4. Matrix = linear map spreadsheet <br> 5. Rank = preserved info <br> 6. Rank-nullity: rank + nullity = input dim <br> 7. Null space = input vectors mapped to 0 |
| **RECONSTRUCT** | 1. How to build a matrix from $T(\vec{e}_i)$ <br> 2. How to compute null space (solve $A\vec{v}=0$) |
| **LOOKUP**   | 1. Exact rank-nullity formula <br> 2. Linear independence test (determinant of basis matrix) |

---

## Computational Exercise (Run in NumPy)
```python
import numpy as np

# Define a vector space in R^2: V = { [x, y] | x + y = 0 }
# Check if [1, -1] and [2, -2] form a basis for V
v1 = np.array([1, -1])
v2 = np.array([2, -2])

# Are they linearly independent? (If not, they don't span)
# Check determinant of [v1, v2] (as columns)
M = np.column_stack((v1, v2))
det = np.linalg.det(M)
print(f"Determinant: {det:.2f}")  # Should be near 0

# What's the null space of A = [[1, 2], [2, 4]]?
A = np.array([[1, 2], [2, 4]])
null_space = np.linalg.null_space(A)  # Returns basis for null space
print("Null space basis:\n", null_space)
```
**Expected Output**:  
`Determinant: 0.00`  
`Null space basis: [[-0.89442719] [ 0.4472136 ]]`  
*Note: This matches our example ([-2,1] scaled to unit vector).*

---

## Explain-Out-Loud Check
*Explain to yourself why the determinant being zero proves [1,-1] and [2,-2] are *not* a basis for $V$ (using your programmer intuition about spreadsheets). Then, describe in one sentence how rank-nullity affects a machine learning model's ability to learn from data.*
```