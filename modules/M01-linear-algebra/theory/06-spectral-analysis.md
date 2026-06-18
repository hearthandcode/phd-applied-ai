---
module: M01
formalism_density: 0.4
status: draft
learner_id: L001
title: "Spectral Analysis and Matrix Functions"
calibration: "MIT 18.06 (Strang) — spectral theory with ML emphasis"
---

# Section 6 — Spectral Analysis and Matrix Functions

## 6.0 Bridge: eigenvalues aren't just numbers — they're the controls

Back in Section 4 you learned to factor a matrix into its eigenvectors and
eigenvalues. It probably felt like an algebra trick: find the directions a
matrix doesn't rotate (the eigenvectors), and the stretch factor along each
(the eigenvalues). True, but underwhelming. Here's the eureka that turns that
trick into a superpower:

**Eigenvalues control dynamics.** Whenever you apply a matrix over and over —
which is *exactly* what happens in an iterative optimizer, a recurrent network
unrolled through time, or a Markov chain — the eigenvalues decide whether things
blow up, die out, or settle. The matrix is the rule of the game; the eigenvalues
are the dial that says "fast / slow / stable / chaotic."

Think of it kinesthetically. You have a vector. You push it through the matrix.
Push again. Again. If every eigenvalue has magnitude less than 1, the vector
shrinks toward zero no matter where it started — the system *forgets*. If some
eigenvalue has magnitude greater than 1, the component along that eigenvector
*grows* and eventually dominates everything — the system *explodes*. That single
sentence is the seed of vanishing and exploding gradients, of why some learning
rates diverge, and of why power iteration finds the top eigenvector for free.

This section is about reading those dials. We'll meet four of them: the
**matrix exponential** (continuous-time dynamics), the **condition number**
(sensitivity to noise), the **spectral radius** (will my iteration converge?),
and **Gershgorin disks** (where are the eigenvalues hiding, without computing
them?).

---

## 6.1 The matrix exponential: turning algebra into motion

### Conceptual bridge

You know the scalar exponential. If money grows at continuous rate $a$, then
after time $t$ you have $e^{at}$ times what you started with. The differential
equation $\frac{dx}{dt} = a x$ has solution $x(t) = e^{at}x(0)$. One number $a$
governs the whole future.

Now imagine many quantities that grow and feed into *each other* — populations
of predators and prey, voltages in a circuit, hidden activations in an RNN. The
rate of change of the whole vector $x$ is a *matrix* times $x$:

$$\frac{dx}{dt} = A x$$

Here $A$ (an $n \times n$ matrix) says "how each coordinate's rate of change
depends on all the coordinates." By beautiful analogy, the solution is

$$x(t) = e^{At}\, x(0)$$

where $e^{At}$ — the **matrix exponential** ($n\times n$ matrix-valued) — is the
single object that propagates the whole system forward in time.

### The definition

The matrix exponential is defined by the *same* power series as the scalar one,
just with a matrix plugged in:

$$e^{A} \;=\; I + A + \frac{A^2}{2!} + \frac{A^3}{3!} + \cdots \;=\; \sum_{k=0}^{\infty} \frac{A^k}{k!}$$

- $I$ — the identity matrix ($n\times n$, ones on the diagonal).
- $A^k$ — $A$ multiplied by itself $k$ times.
- $k!$ — factorial, the scalar $1\cdot 2 \cdots k$.

This series *always converges* for any square matrix, just like the scalar one
always converges. The result is another $n\times n$ matrix.

### Why eigenvalues make this easy

Computing an infinite sum of matrix powers sounds brutal. The eigendecomposition
rescues us. If $A = V \Lambda V^{-1}$ (eigenvectors in the columns of $V$,
eigenvalues on the diagonal of $\Lambda$), then $A^k = V \Lambda^k V^{-1}$ —
the messy middle telescopes. Substituting into the series:

$$e^{A} = V\, e^{\Lambda}\, V^{-1}, \qquad e^{\Lambda} = \mathrm{diag}(e^{\lambda_1}, \dots, e^{\lambda_n})$$

So **you exponentiate a matrix by exponentiating its eigenvalues** — scalar
operations along the diagonal. Combined with $x(t)=e^{At}x(0)$, this says the
$i$-th eigen-component evolves as $e^{\lambda_i t}$. Real negative $\lambda_i$:
that mode decays. Positive: grows. Imaginary part: it oscillates. There is your
dial.

### Worked example (ML-grounded numbers)

Take a tiny 2-state linear system, the kind that models a leaky integrator in a
linearized RNN cell:

$$A = \begin{bmatrix} -0.5 & 1 \\ 0 & -2 \end{bmatrix}$$

Its eigenvalues are the diagonal (it's triangular): $\lambda_1 = -0.5$,
$\lambda_2 = -2$. Both negative, so $e^{At}x(0) \to 0$: the hidden state decays.
The slow mode ($-0.5$) sets the timescale — the state's "memory" lasts roughly
$1/0.5 = 2$ time units. The fast mode ($-2$) is gone in about $0.5$ units. This
is *literally* how you reason about how many timesteps an RNN remembers.

```python
import numpy as np
from scipy.linalg import expm

A = np.array([[-0.5, 1.0],
              [ 0.0, -2.0]])

# Eigenvalues set the timescales
eigvals = np.linalg.eigvals(A)
print("eigenvalues:", eigvals)          # [-0.5 -2. ] -> both decay

# Propagate an initial hidden state forward in time
x0 = np.array([1.0, 1.0])
for t in [0.0, 0.5, 1.0, 2.0, 4.0]:
    xt = expm(A * t) @ x0
    print(f"t={t:>3}:  x(t) = {xt.round(4)},  ||x|| = {np.linalg.norm(xt):.4f}")
# Watch the norm shrink — the slow -0.5 mode dominates the tail.
```

Try changing the $-0.5$ to $+0.3$. One positive eigenvalue and the norm now
*grows* without bound — that's an exploding hidden state in continuous time.

> **Try this in Hermes:** "Walk me through why $A^k = V\Lambda^k V^{-1}$ makes the
> exponential series collapse to $V e^\Lambda V^{-1}$. Make me do one term."
> **Try this in Claude:** "Show me a 2×2 matrix with complex eigenvalues and
> explain how the imaginary part turns $e^{At}$ into rotation + decay (a spiral)."

---

## 6.2 Condition number: how much does noise get amplified?

### Conceptual bridge

Imagine solving $Ax = b$ — find the inputs $x$ that produce output $b$. Now jiggle
$b$ a tiny bit, say by measurement noise. Does $x$ jiggle a tiny bit too, or does
it lurch wildly? A matrix that turns small input wiggles into huge output wiggles
is **ill-conditioned** — solving with it is like balancing a pencil on its tip.
A matrix where small stays small is **well-conditioned** — solid ground.

The condition number puts a number on this fragility. It's the single most
important "is my linear algebra going to betray me numerically?" diagnostic.

### The definition

Using the singular values from Section 5 (the SVD's stretch factors,
$\sigma_{\max} \ge \cdots \ge \sigma_{\min} \ge 0$):

$$\kappa(A) \;=\; \frac{\sigma_{\max}}{\sigma_{\min}}$$

- $\sigma_{\max}$ — the largest singular value (the most stretch any direction
  gets).
- $\sigma_{\min}$ — the smallest singular value (the least stretch — the
  "weakest" direction).

The ratio asks: *how lopsided is the stretching?* If $\kappa = 1$, the matrix
stretches every direction equally (a scaled rotation) — perfectly conditioned.
If $\kappa = 10^{8}$, one direction is squashed a hundred-million times harder
than another, and you'll lose about 8 digits of precision solving with it.

Rule of thumb: **you lose roughly $\log_{10}\kappa$ digits of accuracy.** With
float64's ~16 digits, a $\kappa$ near $10^{16}$ means your answer is numerical
mush.

### Worked example (ML-grounded)

This is the silent killer behind "my normal equations gave garbage." In linear
regression you might solve $X^\top X\, w = X^\top y$. But forming $X^\top X$
*squares the condition number*: $\kappa(X^\top X) = \kappa(X)^2$. If your feature
matrix has $\kappa(X)=10^4$ (very ordinary with unscaled features), then
$\kappa(X^\top X)=10^8$ — you've thrown away half your precision before you even
start. This is the concrete reason ML practitioners standardize features and
prefer QR/SVD-based solvers over the normal equations.

```python
import numpy as np

# Features on wildly different scales -> ill-conditioned design matrix
n = 200
age      = np.random.uniform(20, 60, n)            # ~tens
income   = np.random.uniform(20_000, 200_000, n)   # ~hundred-thousands
X = np.column_stack([np.ones(n), age, income])

kappa_X   = np.linalg.cond(X)
kappa_XtX = np.linalg.cond(X.T @ X)
print(f"kappa(X)      = {kappa_X:.2e}")
print(f"kappa(X^T X)  = {kappa_XtX:.2e}   (~ kappa(X)^2)")

# Standardizing collapses the condition number
Xs = (X - X.mean(0)) / np.where(X.std(0) == 0, 1, X.std(0))
Xs[:, 0] = 1.0
print(f"kappa(standardized X) = {np.linalg.cond(Xs):.2e}   <-- much friendlier")
```

> **Try this in Hermes:** "Quiz me: if $\kappa(X)=10^6$ and I use float32
> (~7 digits), what happens when I solve the normal equations? Why?"
> **Try this in Claude:** "Explain geometrically why squashing one direction
> (small $\sigma_{\min}$) makes $Ax=b$ sensitive to noise in $b$."

---

## 6.3 Spectral radius: will my iteration converge?

### Conceptual bridge

Many algorithms are just "do the same update forever until it stops moving":
gradient descent, power iteration, fixed-point solvers, PageRank, value iteration
in RL. Each step often looks like $x_{k+1} = M x_k$ (plus maybe a constant). Apply
$M$ enough times and you've applied $M^k$. The question "does this converge or
diverge?" becomes "does $M^k$ shrink to zero or blow up?"

We saw in the bridge that the *largest-magnitude eigenvalue* decides this. Give
it a name.

### The definition

$$\rho(A) \;=\; \max_i |\lambda_i|$$

the **spectral radius** — the magnitude of the biggest eigenvalue (using $|\cdot|$
for complex modulus). The clean theorem:

$$A^k \to 0 \;\text{ as } k\to\infty \iff \rho(A) < 1$$

If the spectral radius is below 1, repeated application contracts everything to
zero — the iteration converges. If it's above 1, some component grows
geometrically — divergence. If it's exactly 1, you're on the knife's edge
(oscillation or drift).

**Spectral radius vs. condition number — don't confuse them.** Condition number
is about *one-shot* sensitivity (solving $Ax=b$ once). Spectral radius is about
*repeated* application (iterating). Different questions, different dials.

### Worked example (ML-grounded)

Gradient descent on a quadratic loss $\frac{1}{2}x^\top H x$ updates as
$x_{k+1} = (I - \eta H)x_k$, where $\eta$ is the learning rate and $H$ is the
Hessian. The iteration matrix is $M = I - \eta H$. It converges iff
$\rho(M) < 1$, which works out to needing $\eta < 2/\lambda_{\max}(H)$. Set the
learning rate above that and gradient descent *diverges* — not because your code
is wrong, but because the spectral radius crossed 1. This is the math behind
"my loss went to NaN when I bumped the learning rate."

```python
import numpy as np

# A quadratic with curvature 1 along one axis, 10 along the other
H = np.array([[1.0, 0.0],
              [0.0, 10.0]])
lam_max = np.linalg.eigvalsh(H).max()     # = 10
eta_critical = 2.0 / lam_max              # = 0.2

for eta in [0.05, 0.19, 0.21]:
    M = np.eye(2) - eta * H
    rho = max(abs(np.linalg.eigvals(M)))
    verdict = "converges" if rho < 1 else "DIVERGES"
    print(f"eta={eta:<5}  spectral radius rho(M)={rho:.3f}  -> {verdict}")
# eta just above 0.2 pushes rho past 1 and GD blows up.
```

> **Try this in Hermes:** "Derive $\eta < 2/\lambda_{\max}$ from $\rho(I-\eta H)<1$.
> Make me handle the smallest eigenvalue too — why doesn't it set the limit?"
> **Try this in Claude:** "Connect spectral radius < 1 to why power iteration
> converges to the *top* eigenvector. What role does the eigenvalue *gap* play in
> convergence speed?"

---

## 6.4 Gershgorin disks: locating eigenvalues without computing them

### Conceptual bridge

Computing eigenvalues exactly is expensive ($O(n^3)$) and for a billion-parameter
model, impossible. But sometimes you don't need exact values — you just need to
know "are they all negative?" (stable system) or "could any have magnitude > 1?"
(might diverge). Gershgorin's theorem gives you cheap *bounding boxes* — actually
bounding *disks* — for where every eigenvalue must live, read straight off the
matrix entries with zero heavy computation.

The intuition: a matrix's eigenvalues are "anchored" near its diagonal entries.
The off-diagonal entries in each row say how far an eigenvalue can wander from its
anchor. Strong diagonal, weak off-diagonals → eigenvalues pinned near the
diagonal. This is why **diagonal dominance** keeps systems stable.

### The theorem

For each row $i$, form the **Gershgorin disk**: center at the diagonal entry
$a_{ii}$, radius equal to the sum of the absolute off-diagonal entries in that
row,

$$R_i = \sum_{j \ne i} |a_{ij}|.$$

Then **every eigenvalue of $A$ lies inside the union of these disks**
$\{ z : |z - a_{ii}| \le R_i \}$. No eigenvalue can escape all the disks.

- $a_{ii}$ — the $i$-th diagonal entry (the disk's center on the complex plane).
- $R_i$ — the row's off-diagonal absolute sum (the disk's radius).

Corollary you'll actually use: if $|a_{ii}| > R_i$ for every row (**strict
diagonal dominance**), no disk reaches the origin, so $0$ is not an eigenvalue —
the matrix is invertible. Same idea bounds stability and convergence for free.

### Worked example

```python
import numpy as np

A = np.array([[ 6.0, 1.0, 0.5],
              [ 0.5, 4.0, 1.0],
              [ 1.0, 0.0, 2.0]])

centers = np.diag(A)
radii   = np.abs(A).sum(axis=1) - np.abs(centers)   # row off-diagonal sums
for i, (c, r) in enumerate(zip(centers, radii)):
    print(f"row {i}: disk centered at {c:.1f}, radius {r:.1f} -> [{c-r:.1f}, {c+r:.1f}]")

print("\nactual eigenvalues:", np.linalg.eigvals(A).round(3))
# Every eigenvalue lands inside one of the predicted disks — for free, no eig solve.
```

You'll see the true eigenvalues all sit inside the predicted intervals. We learned
the *neighborhood* eigenvalues live in without ever running the $O(n^3)$ solver —
exactly the kind of cheap guarantee you want when the matrix is enormous.

> **Try this in Hermes:** "Give me a 3×3 matrix and have me compute its Gershgorin
> disks by hand, then check against `np.linalg.eigvals`."
> **Try this in Claude:** "How does Gershgorin justify the claim that strictly
> diagonally dominant matrices are invertible? Walk the logic."

---

## 6.5 Connections to ML — the through-line

Everything above is one idea wearing four hats: **the spectrum of a matrix
governs how a repeated or sensitive process behaves.**

- **Vanishing / exploding gradients in RNNs.** Backpropagation through time
  multiplies by (roughly) the same recurrent Jacobian at every step. The gradient
  scales like $\rho(\text{Jacobian})^{T}$ over $T$ timesteps. $\rho < 1$ →
  gradients vanish (no long-range learning); $\rho > 1$ → they explode (NaNs).
  This is *literally* §6.3 applied to backprop, and it's why LSTMs/GRUs and
  gradient clipping exist.

- **Hessian curvature and optimization.** The Hessian's eigenvalues are the
  curvature of the loss surface. Its condition number $\kappa(H)$ determines how
  slowly gradient descent zig-zags through narrow ravines — and it's exactly the
  ratio that second-order and adaptive methods try to fix.

- **Adaptive learning rates.** Adam, RMSProp, and friends are, in spirit,
  per-coordinate attempts to *precondition* the problem — to flatten the
  eigenvalue spread so the effective condition number drops and you can take
  bigger, safer steps. Newton's method does this exactly via $H^{-1}$.

- **The stable learning-rate ceiling** $\eta < 2/\lambda_{\max}(H)$ comes straight
  from §6.3 — the largest Hessian eigenvalue sets the speed limit.

The thread: when you next see a training run diverge, ask "what crossed a
spectral threshold?" — that instinct is doctoral-level fluency, and it's the same
instinct whether you're staring at an RNN, an optimizer, or an H&C mastery-update
loop that won't stabilize.

---

## 6.6 Section recap

**Explain out loud (no notes):**
1. "The matrix exponential solves $\dot x = Ax$ because…" — and why eigenvalues
   make it computable.
2. "The condition number is $\sigma_{\max}/\sigma_{\min}$, and it matters because…"
   — connect it to losing digits and to the normal-equations trap.
3. "An iteration $x_{k+1}=Mx_k$ converges iff…" — and how that sets the
   learning-rate ceiling.
4. "Without computing eigenvalues, I can bound them by…" — describe a Gershgorin
   disk in one breath.

If any of those stalls, re-read that subsection's bridge — the bridge is the
load-bearing idea; the formula is just bookkeeping.

### Memory tiers for THIS section

**CARRY (memorize — these are reflexes):**
- $e^{A} = \sum_k A^k/k!$ and $\dot x = Ax \Rightarrow x(t)=e^{At}x(0)$
- $\kappa(A) = \sigma_{\max}/\sigma_{\min}$
- $\rho(A) = \max_i|\lambda_i|$; iteration converges iff $\rho < 1$
- "Eigenvalues control dynamics, convergence, and stability" (the one-liner)

**RECONSTRUCT (re-derive when needed):**
- $e^{A} = V e^{\Lambda} V^{-1}$ from the eigendecomposition
- $\eta < 2/\lambda_{\max}(H)$ from $\rho(I-\eta H) < 1$
- $\kappa(X^\top X) = \kappa(X)^2$ and why standardizing helps
- Gershgorin disk: center $a_{ii}$, radius $\sum_{j\ne i}|a_{ij}|$

**LOOKUP (know it exists, search when needed):**
- `scipy.linalg.expm` algorithm details (scaling-and-squaring)
- Exact float-digit loss tables, complex-eigenvalue spiral formulas
- Refinements of Gershgorin (Brauer ovals, second-disk theorems)

> **Closing interaction prompt —**
> **Try this in Hermes:** "Give me one matrix and have me report all four
> diagnostics — $e^A$, $\kappa$, $\rho$, Gershgorin disks — and say what each
> predicts about its behavior."
> **Try this in Claude:** "Take my toy RNN recurrent matrix and tell me, from its
> spectrum alone, whether gradients will vanish or explode over 50 timesteps."
