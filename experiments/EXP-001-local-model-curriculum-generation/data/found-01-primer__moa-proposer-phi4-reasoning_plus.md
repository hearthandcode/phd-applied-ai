<think>We are Phi. We need to generate one section for doctoral-level self-study module "M01" called "Linear Algebra for ML", artifact: foundations-primer, and then we have section "01 — Primer". It is calibrated against MIT 18.06 by Strang.

We are given instructions that the learner profile is L001: experienced programmer with ADHD; working memory is precious. Tone must be direct, warm, vivid. Start from a programmer's existing intuitions (spreadsheets, arrays, loops). Should never leave an unexplained symbol across a page break. We need to include many details: YAML front matter in the beginning exactly as specified.

We need required structure and rules:
- YAML front matter with these keys:
module: M01, title: "Linear Algebra for ML", artifact: foundations-primer,
section: "01 — Primer", calibration: "MIT 18.06 (Strang)", formalism_density: 0.4, status: draft, learner_id: L001.
- We then have conceptual bridge first (before any formal definition) - so we give an intuitive description in plain language (and a second denser pass for the hardest part).
- Then state the formal definitions.

We need to cover topics: vectors as objects, vector spaces and closure, basis & dimension, linear maps, matrices as the spreadsheet form of a map, and rank-nullity. 

Let's plan the document structure:
1. YAML front matter with the required keys.
2. A conceptual bridge for each topic:
   - For Vectors: Start from programmer intuitions (maybe spreadsheets arrays). "Vectors are like lists in Python or NumPy".
   - Provide intuitive explanation and then formal definition.

But instructions require to include a worked numerical example, symbol discipline with all symbols defined when they appear, etc.
I need to produce text that includes multiple sections:
- "Vectors as Objects" section: conceptual bridge, then definition. 
- "Vector Spaces & Closure": conceptual bridge, then definition of vector space (with conditions).
- "Basis and Dimension": conceptual bridge then formal definition with basis and dimension explained.
- "Linear Maps": explanation using arrays in programming; then provide formal definitions: linearity property: f(ax + by) = a f(x)+ b f(y). 
- "Matrices as the Spreadsheet Form of a Map": talk about matrices representation, rows/columns. Then show connection with linear maps.
- "Rank-Nullity": explanation with worked example.

I must include a concrete fully worked numerical example in some section (maybe a worked example for computing rank and nullity or similar).
I need to include a symbol reference table if multiple new symbols are introduced. So I'll list maybe the symbols that we define: like V, W for vector spaces, x, y for vectors, etc.

Then ML payoff: include a separate subsection explaining why this matters for machine learning with concrete examples (maybe using matrix multiplication or eigen decomposition) but at a basic level.

I need to include "TIERED MEMORY SUMMARY" with three parts: memorize max 7 items, re-derive and lookup. So I'll include instructions that are summarized as bullet points with labels "CARRY", "RECONSTRUCT", "LOOKUP".

Include "COMPUTATIONAL EXERCISE": at least one small exercise that the learner can run (NumPy/SymPy) with code snippet maybe in a Python code block.

Finally, end with an "explain-out-loud check" prompt, asking the reader to explain something out loud. It must be clear and direct.

I need to produce the complete section as a single markdown document.
The YAML front matter is at top of file, then the content in markdown style.

We need to follow all required structure exactly.

Let's plan step by step:

YAML header lines:
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

Now the content begins.

I can produce an outline:

Title of section: maybe "Primer" with a level 1 header "# Linear Algebra Primer". But instructions say to use plain markdown.

Let's structure the document as following sections:
- Introduction, then subsections for each topic. I'll try to produce headings in the following order:

1. "Vectors as Objects": Conceptual Bridge: Explain vectors like lists/arrays used in programming (spreadsheets columns). Then formal definition of a vector, maybe not fully rigorous but similar.

2. "Vector Spaces and Closure": conceptual bridge: explain that collection of objects must be closed under addition and scalar multiplication. Provide formal definition: V is a vector space if it has addition and scalar multiplication satisfying axioms.
   - Note: I'll mention closure properties explicitly.

3. "Basis & Dimension": conceptual bridge: relate basis to minimal spanning set in programming arrays with no redundancy, then define basis formally as a set of linearly independent vectors that span the vector space. Then dimension is the number of elements in any basis. Worked example maybe using R^2 coordinates.

4. "Linear Maps": conceptual bridge: explain transformation between data arrays (like applying functions to each element) but also more structured transformations. Then formal definition: A map T: V → W is linear if T(a * v + b * w) = a * T(v) + b * T(w), with a, b scalars. Provide some examples.

5. "Matrices as the Spreadsheet Form of a Map": conceptual bridge: explain that matrices are simply tables (like spreadsheets) representing linear maps in coordinates. Then formal definition: an m×n matrix A is an array where each element a_ij is defined. The product with vector x gives another vector y = A x.

6. "Rank-Nullity": conceptual bridge: talk about image and kernel of linear map, then rank-nullity theorem. Formal definitions: For T: V → W, the null space (kernel) is { v in V | T(v)=0} and the rank is dimension of range(T). The Rank-Nullity Theorem states that dim(V) = rank(T) + nullity(T).

I must include a worked example with explicit steps. I can produce one numerical example for computing basis or computing rank-nullity.

Maybe I'll pick an example: Consider linear map T: R^3 -> R^2 given by matrix A = [[1,2,3],[4,5,6]]. Then find rank of A and nullity. But let's check if that works with numbers? Alternatively, maybe choose a simpler example e.g. consider transformation T: R^2 → R^2 given by matrix [[2,0], [0, 3]] and compute its kernel, but then that trivial.

Alternatively, I can pick A = 
[[1, 2],
 [3,4],
 [5,6]]
Which is a 3x2 matrix. Its rank might be computed using row reduction, etc. But maybe simpler: Let's use a small 2x2 example for clarity and show steps clearly.

I want to choose an easily computed example. Maybe I'll pick T: R^2 -> R^2 with matrix A = [[1,2],[3,4]]. Then find nullity? Let me compute the kernel of that matrix if possible. But then determinant is (1*4 - 2*3) = 4-6 = -2 which is nonzero so rank=2 and nullity=0.

But then rank-nullity theorem yields dimension R^2 = 2, but maybe it's too trivial example since it has no interesting structure regarding kernel. Alternatively, I could pick a matrix that is singular. Perhaps A = [[1, 2], [2,4]]. Then the second row is twice first row, so the rank=1 and nullity=1. But then note the vector space dimension of R^2 is 2 (if we assume domain R^2). Alternatively, I can pick T: R^3 -> R^2 with matrix A = [[1,0,-1],[0,1,1]] maybe or simpler: 
I want to include a worked example that covers all steps. Perhaps I'll choose the matrix:
A = [ [1, 2],
      [2,4] ]
This is a 2x2 matrix. Let's see: That matrix represents T: R^2 -> R^2. Then find kernel: solve system:
1*x + 2*y = 0
2*x + 4*y = 0
The second equation is double the first, so only one independent equation. So nullity= dimension of solution space is 1, and basis for nullspace can be chosen as vector [ -2, 1 ] or similar. But let me check: if I set y=t then x=-2t. So a basis for kernel = {(-2,1)}. And the rank is 1 because there's only one pivot column.

Alternatively, maybe a simpler matrix might be better:
Let A = [ [2,4], [3,6] ] with rows multiples? But not as simple.

I can choose A = [ [1, 2], [2,4] ] then the rank is computed by noticing that row2=2*row1, so dimension of image is 1. Then nullity = (domain dimension) - rank = 2-1=1, and the kernel vector is something like [-2,1]. But I'll show detailed steps.

I should include a worked numerical example for each or at least one that covers rank-nullity.

Alternatively, I can choose an example from linear maps in R^3 -> R^2 as earlier. Maybe I'll use A = [ [1, 0, -1], [0, 1, 1] ] then compute its nullspace. But perhaps simpler is to stick with the 2x2 singular matrix.

I can choose a numerical example that goes step-by-step: "Worked Example: Determining Rank and Nullity of A = [[1,2],[2,4]]".

Steps:
- Write down the system for kernel.
- Solve first equation: x + 2y = 0 => x = -2y.
- Then second eq becomes 2(-2y) + 4y = -4y+4y=0. So solution is all vectors of form (-2t, t). Then basis for nullspace is {[-2,1]}. So dimension (nullity)=1.
- Rank: number of pivot columns, which are 1.

Then mention rank-nullity theorem: dim(R^2) = 2 equals 1 + 1. But wait, domain R^2 has dimension 2? Yes.
So that is an example.

I must include a symbol reference table if multiple new symbols are introduced. I'll have to list symbols: V for vector space, v for vector elements, etc. I can produce a small table after the theoretical parts. Let me check which symbols to include:
- In "Vectors as Objects": use symbol x and y.
- In "Vector Spaces and Closure": V is set of vectors, 0 (zero element), addition operation, scalar multiplication with scalar c from field F or R maybe.
- For linear maps: T, domain V, codomain W.
- Matrices: A, entry a_ij.
- Basis: B, dimension dim(V) etc.

I can include a table like:

Symbol | Description
---|---
V      | vector space (set of vectors)
x, y   | elements/vectors in V
0      | additive identity in V
+      | addition operation on vectors
c      | scalar in field F (commonly ℝ or ℂ)
•      | scalar multiplication
T      | linear map from V to W

I can add symbols for matrix A and its entries a_ij.

I'll produce a table maybe at the end of the section, after rank-nullity theorem. Or I can include it along with each new symbol introduction but must be careful not to break working memory constraints.

I should now produce text following instructions: "conceptual bridge first", then formal definitions.

Let's plan sections:

I'll produce one markdown document that includes:
- YAML front matter in triple dash style.
- Title of the section maybe as a heading level 1 with something like "# Section 01 — Primer" or similar. But I need to include an introduction paragraph.

The instructions require: "You are generating one section of a doctoral-level self-study linear-algebra module (M01) for a single learner." So that means we produce one markdown document with YAML front matter and then content.

Let's now produce the text:

I'll start with something like:
"Welcome to our primer on Linear Algebra for ML! In this module, we will build your intuition for vectors, vector spaces, basis, linear maps, matrices, and rank-nullity. We begin by connecting these concepts to familiar programming objects such as arrays in spreadsheets and loops."

Then I'll produce conceptual bridges:

For Vectors: "Before diving into formal definitions, think of a vector simply as an ordered list of numbers, much like the row in your favorite spreadsheet or array in Python. These lists can represent data points, coordinates, or even pixel intensities." Then mention that we're going to define what a vector is.

Then I'll produce: "Vectors as Objects" and then Conceptual Bridge:
- "Imagine your daily life dealing with arrays (ordered collections) where each element has an index, much like the rows/columns in an Excel sheet. In linear algebra, vectors are similar objects but they also have structure that allows us to combine them through addition and multiplication by numbers."

Then I'll produce formal definition: "A vector is an element of a set V called a vector space. A vector space over a field F (commonly the real numbers ℝ) is defined as follows:" Then list axioms: but wait, this might be too much detail for a primer? But instructions say: "cover vectors as objects." I'll give definition:

Definition: A vector is an element of a set V. But note that by itself, the concept of "vector" requires context (like what operations are defined on them). So I'll define it in terms of vector space.

Maybe I'll produce: "In this primer, we view vectors as objects that can be added together and scaled by numbers from a given field." Then formal definition:
"A set V is called a vector space over a field F if there exist two operations (vector addition and scalar multiplication) satisfying the following axioms: (list axioms)"

But since this is a primer, maybe I'll not list all 10 axioms in full detail. But instructions say "every definition must be mathematically correct and verifiable against MIT 18.06 (Strang)." So I need to include all required details? Possibly I can produce a truncated but complete set of axioms.

Let me recall the standard axioms for vector spaces:
1. Closure under addition: For all u, v in V, u + v is in V.
2. Commutativity of addition: u+v = v+u.
3. Associativity of addition: (u+v)+w = u+(v+w).
4. Existence of additive identity: there exists 0 in V such that u+0 = u for all u in V.
5. Existence of additive inverses: For each u, there exists -u in V so that u + (-u) = 0.
6. Closure under scalar multiplication: for any c in F and v in V, c*v is in V.
7. Distributivity of scalar sums: (a+b)v = av + bv for all a,b in F and v in V.
8. Distributivity of vector sums: a(u+v) = au + av for all a in F and u,v in V.
9. Associativity of scalar multiplication: a(bv) = (ab)v for all scalars a, b in F and v in V.
10. Identity element of scalar multiplication: 1*v = v.

That's the standard definition. I must include these axioms as formal definitions.

But we need to ensure "conceptual bridge first" before formal definitions, so I'll say:
"For every concept below, a conceptual story is provided to anchor your understanding."

Then move on to next topic: "Vector Spaces and Closure".
I can produce a conceptual narrative: "Imagine building a dynamic data structure in a programming language where you combine elements using addition and multiplication. The idea of closure means that no matter which two vectors (data points) you combine, their sum still belongs to the same family (set)."
Then state the formal definition as above.

Next: "Basis & Dimension". Conceptual Bridge: "Think of a basis as the 'minimal recipe' or the set of independent building blocks that can generate every vector in your space. It's similar to having an optimized, non-redundant array of functions that collectively span all the possible outputs you need." Then formal definition:
- A subset B of V is a basis if: (i) B is linearly independent; meaning that no element in B can be written as a combination of others. And (ii) B spans V, meaning every vector in V can be expressed uniquely as a linear combination of elements from B.
Then dimension is defined as the number of vectors in any basis.

I must include a worked example: For instance, consider R^2 represented by pairs (x, y). A standard basis for R^2 is { (1,0), (0,1) }. Then explain that these two vectors are linearly independent and span the space. That can be our numerical example.

Alternatively, I'll do a more complex worked numerical example focusing on rank-nullity: Perhaps choose a matrix from R^2 to R^2 as described earlier. But note that "Basis & Dimension" could use R^2 example. Alternatively, I might include a separate subsection "Rank-Nullity", which includes a worked example with the singular 2x2 matrix.

I need to produce at least one fully worked numerical example with explicit steps (preferably rank-nullity theorem). So I'll produce that as its own section maybe after "Matrices as the Spreadsheet Form of a Map".

Perhaps structure is: Vectors -> Vector Spaces and Closure -> Basis & Dimension -> Linear Maps -> Matrices as the Spreadsheet Form of a Map -> Rank-Nullity Theorem (with worked example) -> Symbol Reference Table -> ML Payoff -> Tiered Memory Summary -> Computational Exercise -> Explain Out Loud Check Prompt.

Plan sections:
Section 1: Vectors as Objects
- Conceptual Bridge: Use analogies with arrays, lists, spreadsheets.
- Formal Definition of a vector element in a vector space (or at least note that vectors are elements of a vector space).
Maybe I'll state: "In linear algebra, we often speak of vectors without specifying the underlying set. However, for clarity, we say that a vector is an element v belonging to some vector space V."

Section 2: Vector Spaces and Closure
- Conceptual Bridge: talk about closure under addition and scalar multiplication.
- Formal definition with axioms.

Section 3: Basis & Dimension
- Conceptual Bridge: relate basis to minimal building blocks in programming like a set of independent functions.
- Formal definition: Basis is linearly independent and spans the space.
- Provide example: For R^2, standard basis. Worked steps.

Section 4: Linear Maps
- Conceptual Bridge: Relate to functions in programming that transform data.
- Formal Definition: T: V → W is linear if for all vectors u,v and scalars a,b in F, T(a*u + b*v) = a*T(u)+b*T(v).
- Possibly mention kernel and image.

Section 5: Matrices as the Spreadsheet Form of a Map
- Conceptual Bridge: In spreadsheets or NumPy arrays, think of each matrix as a table where rows represent outputs. It's like mapping columns to rows.
- Formal definition: A matrix is an ordered array of numbers, typically denoted by A, with entries a_ij. The linear map T can be represented in coordinates relative to chosen bases.

Section 6: Rank-Nullity
- Conceptual Bridge: Think about when functions have redundant input data that collapse into the same output (like many indices giving same result). In ML, this is related to features redundancy.
- Formal definition: For a linear map T: V → W with V finite-dimensional,
   Null space N(T) = { v in V | T(v)=0 } has dimension nullity.
   Range or image R(T) = { T(v) for all v in V } has dimension rank.
   The Rank-Nullity Theorem states: dim(V) = rank(T) + nullity(T).

Include Worked Example:
Let A be the matrix representing a linear map T: R^2 → R^2 with
A = [ [1, 2],
      [2, 4] ]
Then find kernel and rank.
Steps:
- Write system: 1*x + 2*y=0, 2*x+4*y=0. Recognize that second equation is redundant because it's 2*(first eq). So the solution set for (x,y) is given by x=-2y, y arbitrary; basis = { (-2,1) }.
- Therefore nullity is 1.
- Since there is one pivot column, rank=1.
Then check: dimension of domain (2)= rank + nullity => 2=1+1.

I must include a symbol reference table:
I'll produce something like:

Symbol Reference Table:
Symbol | Description
---|---
V     | A vector space (set with operations defined)
v, u  | Vectors in the vector space
0     | Zero vector (additive identity)
a, b  | Scalars from field F (often ℝ or ℂ)
T: V → W | Linear map from vector space V to W.
Basis B | A set of linearly independent vectors spanning V.
dim(V)   | Dimension of V, number of elements in any basis.
A       | Matrix representing a linear map T.
a_ij    | The entry in the i-th row and j-th column of matrix A.
N(T) or ker(T)| Null space/kernel of T (set where T(v)=0).
R(T) or im(T)| Range/image of T.

I can produce that table at the end after rank-nullity theorem, or I could intersperse it after each section. But instructions say: "provide symbol reference table if multiple new symbols are introduced." Possibly I'll include one table near the end summarizing all symbols used in this module section.

Section ML Payoff:
- Explain why these matters for machine learning: For example, matrices and linear maps underlie many algorithms like neural networks (affine transformations) and dimensionality reduction techniques. In particular, understanding the rank-nullity theorem helps with feature selection and regularization.

I must produce Tiered Memory Summary with three parts: "CARRY" which are memorize max 7 items, "RECONSTRUCT" which are re-derive, "LOOKUP" which never memorize.
Maybe I'll produce something like:
Memory summary:
CARRY (memorize max 7):
1. A vector is an element of a vector space with defined addition and scalar multiplication.
2. A set V is a vector space if it satisfies closure under addition and scalar multiplication along with the ten axioms.
3. A basis is a minimal spanning set that is linearly independent, and its size equals the dimension.
4. A linear map T preserves linear combinations: T(a*u + b*v) = a*T(u)+b*T(v).
5. The matrix representation of a linear map in given bases.
6. Rank is the dimension of the image (range) of a linear map.
7. Nullity is the dimension of the kernel of a linear map.

RECONSTRUCT:
- Reconstruct the definitions of vector space axioms, basis, and linear maps from first principles.
LOOKUP:
- Do not memorize the specific proof details or advanced derivations; consult textbooks (e.g., Strang) for complete proofs.

I must include Computational Exercise with at least one small NumPy/SymPy exercise that learner can run:
Maybe I'll produce something like:

Example computational exercise: "Using Python and NumPy, compute the null space of a given 2x2 matrix representing a singular linear map. For example: 
import numpy as np
A = np.array([[1,2],[2,4]])
# Compute eigenvalues and eigenvectors using np.linalg.eig.
eigenvals, eigenvecs = np.linalg.eig(A)
print('Eigenvalues:', eigenvals)
print('Eigenvectors (columns):', eigenvecs)

Then instruct: "Examine the eigenvector corresponding to the zero eigenvalue to identify a basis for the null space."

I can include that as a code block in markdown.

Finally, End with an "explain-out-loud check" prompt. For example:
"At this point, explain out loud (or type) how you would verify the Rank-Nullity theorem for a linear map T: R^2 → R^2 using the matrix A = [[1, 2], [2,4]]."

I'll produce that at the end.

Ensure not to leave any unexplained symbol across page breaks. I must ensure every symbol is defined in the sentence it appears.

I need to follow Hearth & Code curriculum design rules exactly: "Tone direct, warm, vivid; start from a programmer's existing intuitions; never make reader hold an unexplained symbol across a page break." So I'll produce text that includes definitions and explanations in the same paragraphs as where they appear.

Let me now produce a final answer with YAML front matter then Markdown document content. The instructions say: "Output ONLY the Markdown document" so I must output markdown only.

I must include YAML front matter at top, and then content.

I'll produce the text with headings and code blocks.

I'll produce text in markdown style (plain text with markdown formatting).

Plan structure:

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

# Linear Algebra Primer

Welcome to the primer on linear algebra tailored for machine learning! In this module, we'll warm up your working memory with ideas that feel familiar from programming and spreadsheets, then gradually build formal mathematical structures. We start by exploring vectors as objects, vector spaces (and their closure properties), basis & dimension, linear maps, matrices as coordinate representations of these maps, and finally the rank-nullity theorem.

---

## 1. Vectors as Objects

Imagine a row in your favorite spreadsheet or an array in Python – that's essentially what we call a vector in programming. Just like each cell holds a number, a vector is an ordered list of numbers representing data points, coordinates, or even pixel intensities. In linear algebra, however, these objects come with extra structure: you can add two vectors and multiply them by scalars (numbers) while still remaining within the same collection.

Conceptual Bridge:
Think of your array as being "closed" under addition and multiplication by numbers. For example, if you have two arrays [1, 2] and [3, 4], their sum is [4, 6]. This idea of combining elements without leaving the set is at the heart of linear algebra.

Formal Definition:
A vector is defined as an element v (we write v ∈ V) belonging to a vector space V. Informally, V is a collection of such objects that supports two operations – addition and scalar multiplication – in a manner consistent with familiar arithmetic rules.

---

## 2. Vector Spaces and Closure

Conceptual Bridge:
In programming, you often work with dynamic lists or arrays where new elements are created by combining existing ones (think list comprehensions). Similarly, a vector space is designed so that any combination of its vectors (via addition and scaling) still lies within the same set. This property is known as closure.

Formal Definition:
A set V, together with two operations (vector addition “+” and scalar multiplication “·”), forms a vector space over a field F (typically the real numbers ℝ or complex numbers ℂ) if it satisfies the following axioms:

1. Closure under addition: For every u, v ∈ V, the sum u + v is also in V.
2. Commutativity of addition: u + v = v + u for all u, v ∈ V.
3. Associativity of addition: (u + v) + w = u + (v + w) for all u, v, w ∈ V.
4. Existence of an additive identity: There exists a vector 0 in V such that u + 0 = u for every u ∈ V.
5. Existence of additive inverses: For each u ∈ V, there exists a vector –u such that u + (–u) = 0.
6. Closure under scalar multiplication: For any scalar c ∈ F and any v ∈ V, the product c · v is in V.
7. Distributivity of scalar sums over vectors: For any scalars a, b ∈ F and v ∈ V, (a + b) · v = a · v + b · v.
8. Distributivity of vector sums over scalars: For any scalar c ∈ F and u, v ∈ V, c · (u + v) = c · u + c · v.
9. Associativity of scalar multiplication: For any scalars a, b ∈ F and any v ∈ V, a · (b · v) = (a · b) · v.
10. Identity element of scalar multiplication: There exists an identity scalar 1 in F such that 1 · v = v for every v ∈ V.

---

## 3. Basis & Dimension

Conceptual Bridge:
Imagine you’re optimizing your code by choosing a minimal set of independent functions that together can generate any desired output. In linear algebra, a basis serves as just that—a minimal and non-redundant set of vectors from which every vector in the space can be uniquely constructed.

Formal Definition:
A subset B ⊆ V is called a basis for V if it satisfies two properties:
- Spanning: Every vector v ∈ V can be expressed as a linear combination of elements of B.
- Linear Independence: No vector in B can be written as a linear combination of the others.

The dimension of V, denoted dim(V), is defined as the number of vectors in any basis for V.

Worked Example:
Consider the 2-dimensional real vector space ℝ². A common choice for a basis is
B = { (1, 0), (0, 1) }.
Verification Steps:
• Spanning: Any vector (x, y) ∈ ℝ² can be written as x*(1, 0) + y*(0, 1).
• Linear Independence: The equation a*(1, 0) + b*(0, 1) = (0, 0) implies a = 0 and b = 0.
Thus, B is indeed a basis for ℝ², so dim(ℝ²) = 2.

---

## 4. Linear Maps

Conceptual Bridge:
Think of a linear map as a function in your programming world that transforms data from one format to another while preserving the “linearity” structure—just like applying a consistent operation element-wise across an array. However, here the transformation respects both vector addition and scalar multiplication.

Formal Definition:
A function T: V → W between two vector spaces is called linear if for all vectors u, v ∈ V and for all scalars a, b ∈ F,
  T(a·u + b·v) = a·T(u) + b·T(v).

---

## 5. Matrices as the Spreadsheet Form of a Map

Conceptual Bridge:
In spreadsheets or programming libraries like NumPy, data is often stored in matrices—rectangular arrays where each cell holds a number. In linear algebra, a matrix represents a linear map when you choose bases for your domain and codomain.

Formal Definition:
An m×n matrix A is an ordered array of numbers written as
  A = [ a₍ᵢⱼ₎ ],
where i indexes the rows (1 ≤ i ≤ m) and j indexes the columns (1 ≤ j ≤ n). When you multiply a matrix A by a vector x ∈ ℝⁿ, you obtain another vector y ∈ ℝᵐ given by:
  y = A · x,
with each component computed as
  y₍ᵢ₎ = Σ (from j=1 to n) a₍ᵢⱼ₎ · xⱼ.

---

## 6. Rank-Nullity

Conceptual Bridge:
Consider what happens when two different inputs to a function yield the same output—a phenomenon seen in many machine learning models where redundant features may collapse into similar responses. In linear maps, this is formally captured by the kernel (null space) and image (range).

Formal Definitions:
For a linear map T: V → W with V finite-dimensional:
• The null space (or kernel), denoted N(T) or ker(T), is defined as
  N(T) = { v ∈ V | T(v) = 0 }.
• The rank of T, denoted rank(T), is the dimension of its image R(T) (the set of outputs T produces):
  R(T) = { T(v) | v ∈ V }.
The Rank-Nullity Theorem states that:
  dim(V) = rank(T) + nullity(T),
where nullity(T) is the dimension of N(T).

Worked Example (Rank-Nullity):
Let’s consider a linear map T: ℝ² → ℝ² represented by the matrix
  A = [ [1, 2],
       [2, 4] ].
To find the kernel of A, solve:
  1·x + 2·y = 0  (1)
  2·x + 4·y = 0  (2)
Notice that equation (2) is just 2 times equation (1), so they are equivalent. From (1):
  x = –2y.
Let y = t (a free parameter). Then every solution has the form:
  (x, y) = (–2t, t).
A basis for the kernel is { (-2, 1) }, so nullity(T) = 1.
Since the domain ℝ² has dimension 2 and we have one linearly independent equation, only one pivot exists. Thus, rank(A) = 1.
Verification via Rank-Nullity:
  dim(ℝ²) = 2 = rank(T) + nullity(T) = 1 + 1.

---

## Symbol Reference Table

Symbol | Description
---|---
V | A vector space (a set with operations of addition and scalar multiplication)
v, u | Vectors within the vector space V
0 | The zero vector (additive identity in V)
a, b | Scalars from a field F (commonly ℝ or ℂ)
T: V → W | A linear map (function) from vector space V to another vector space W
Basis B | A set of vectors that is both spanning and linearly independent; determines dim(V)
dim(V) | Dimension of the vector space V (number of vectors in any basis)
A | An m×n matrix representing a linear map T with respect to chosen bases
a₍ᵢⱼ₎ | The entry in the i-th row and j-th column of matrix A
N(T) or ker(T) | Null space (kernel) of T; set of all v ∈ V such that T(v)=0
R(T) or im(T) | Image (range) of T; set {T(v) | v ∈ V}

---

## Machine Learning Payoff

In machine learning, many models—from neural networks to regression algorithms—rely on linear transformations. Understanding matrices and linear maps helps in:
• Designing layers in neural networks where each layer applies an affine transformation.
• Analyzing feature spaces for redundancy (via the null space) or determining the effective number of features (via rank).
• Implementing dimensionality reduction techniques, such as Principal Component Analysis (PCA), which are deeply rooted in linear algebra concepts like eigenvalues and singular value decomposition.

---

## Tiered Memory Summary

CARRY (Memorize these 7 key ideas):
1. A vector is an element of a vector space with defined addition and scalar multiplication.
2. A vector space must satisfy closure under both operations along with the ten axioms.
3. A basis is a minimal set of vectors that spans the space without redundancy.
4. The dimension of a vector space is the number of vectors in any basis.
5. A linear map T preserves linear combinations: T(a·u + b·v) = a·T(u) + b·T(v).
6. A matrix represents a linear map with respect to chosen bases.
7. The Rank-Nullity Theorem states that dim(V) = rank(T) + nullity(T).

RECONSTRUCT:
- From the axioms, derive why every vector space has an additive identity and inverses.
- Explain how a basis guarantees both spanning and independence.
- Reconstruct the proof of the linearity property for T.

LOOKUP:
- Do not memorize the detailed proofs of advanced topics (e.g., eigenvalue decompositions); refer to textbooks like Strang’s “Introduction to Linear Algebra” when needed.

---

## Computational Exercise

Below is a simple Python exercise using NumPy that illustrates finding the null space of a matrix:

```python
import numpy as np

# Define a 2x2 singular matrix A representing a linear map T: R^2 -> R^2
A = np.array([[1, 2],
              [2, 4]])

# Compute eigenvalues and eigenvectors; the eigenvector corresponding to eigenvalue 0 gives a basis for the null space.
eigenvals, eigenvecs = np.linalg.eig(A)

print("Eigenvalues:", eigenvals)
print("Eigenvectors (each column is an eigenvector):")
print(eigenvecs)

# Identify the null space vector from the eigenvector corresponding to eigenvalue 0
null_vector = eigenvecs[:, np.isclose(eigenvals, 0)]
print("\nA basis for the null space of A is:")
print(null_vector)
```

Try running this code in your Python environment and observe how the matrix’s singularity reflects in its eigenstructure.

---

## Explain-Out-Loud Check Prompt

Now that you’ve worked through these concepts, pause and explain out loud (or type) how you would verify the Rank-Nullity Theorem for the linear map T: ℝ² → ℝ² represented by A = [ [1, 2], [2, 4] ]. Consider:
• How to find a basis for the null space.
• How to determine the rank of the matrix.
• How these add up to confirm that dim(ℝ²) equals rank(T) + nullity(T).

Good luck exploring the world of linear algebra—and remember, every vector and transformation has its own story waiting to be discovered in machine learning!

---