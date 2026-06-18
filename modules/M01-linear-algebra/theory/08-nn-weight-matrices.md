---
module: M01
formalism_density: 0.4
status: draft
learner_id: L001
title: "Neural Network Weight Matrices: Structure and Geometry"
calibration: "MIT 18.06 (Strang) — weight geometry, ML emphasis"
---

# Section 8 — Neural Network Weight Matrices: Structure and Geometry

## 8.0 Bridge: a neural network is a composition of linear maps

Strip away the marketing and a neural network is almost embarrassingly simple
linear algebra. Each layer takes a vector, multiplies it by a matrix, adds a
shift, and then bends it with a single nonlinear squish. Stack those layers and
you've composed a bunch of linear maps with little kinks between them.

Here's the eureka worth holding onto: **without the nonlinearities, a deep network
collapses.** A composition of linear maps is *itself* just one linear map —
$W_3(W_2(W_1 x)) = (W_3 W_2 W_1)x$, a single matrix. Ten layers would equal one.
So the entire expressive power of depth lives in the tiny nonlinear kinks
(ReLU, GELU, …) wedged between the matrices. The matrices do the heavy
geometric lifting; the nonlinearities are what stop it all from telescoping into
a single boring transformation.

Which means: if you understand what a weight matrix *does to space* — how it
stretches, rotates, and squashes — you understand the substance of what a network
computes. This section reads weight matrices the way Section 5 taught you to read
any matrix: through rank, singular values, and spectral norm. The difference is
these matrices were *learned*, and their geometry tells you what the network
learned.

---

## 8.1 Each layer as an affine map

### Conceptual bridge

A pure linear map ($Wx$) always fixes the origin — feed in zero, get out zero. But
networks need to shift things around freely, not just stretch through the origin.
The fix is to add a constant vector after the multiply. That "linear map plus a
shift" is called an **affine map**, and it's the actual unit of computation in a
dense layer.

Think of it kinesthetically: $W$ stretches and rotates the input space; $b$ then
slides the whole result over. Stretch, then slide. Then the nonlinearity bends.

### The definition

A single layer (before the nonlinearity) computes:

$$h = Wx + b$$

- $x$ — the layer's input vector (dimension $d_{\text{in}}$).
- $W$ — the **weight matrix** ($d_{\text{out}} \times d_{\text{in}}$), the learned
  linear transformation.
- $b$ — the **bias vector** ($d_{\text{out}}$), the learned shift (translation).
- $h$ — the **pre-activation** output ($d_{\text{out}}$), which then goes through a
  nonlinearity $\sigma$ to give the layer's output $\sigma(h)$.

A full network is $f(x) = \sigma_L(W_L \,\sigma_{L-1}(\cdots \sigma_1(W_1 x + b_1)\cdots) + b_L)$ —
affine maps and nonlinearities, alternating, all the way down.

### Worked example (shapes, ML-grounded)

A classifier mapping a 784-pixel MNIST image to a 128-unit hidden layer to 10
class logits:

- Layer 1: $W_1$ is $128\times 784$, $b_1$ is $128$. Input $x$ is $784$.
  $h_1 = W_1 x + b_1$ is $128$; output $\sigma(h_1)$ (ReLU) is $128$.
- Layer 2: $W_2$ is $10\times 128$, $b_2$ is $10$. Output is the 10 logits.

The first weight matrix has $128\times 784 \approx 100\text{k}$ parameters — those
are 100k learned numbers describing one linear transformation of pixel space. The
geometry of *that one matrix* is what we'll dissect next.

> **Try this in Hermes:** "Quiz me: for a layer mapping dimension 512 → 256, what
> are the shapes of $W$, $b$, $x$, and $h$? How many learned parameters?"
> **Try this in Claude:** "Prove to me that stacking two linear layers with no
> nonlinearity is equivalent to a single linear layer. Where exactly does depth
> 'die'?"

---

## 8.2 Spectral norm and Lipschitz continuity

### Conceptual bridge

Here's a stability question that matters enormously in practice: if I nudge the
input a little, how much can the output move? A layer that can turn a tiny input
change into a giant output change is *jumpy* — fragile to noise, vulnerable to
adversarial examples, prone to exploding gradients. A layer with a bounded
"amplification factor" is *smooth* and well-behaved.

That maximum amplification factor of a matrix has a name you already met in
Section 5: the largest singular value. Reframed as "the most this matrix can
stretch any direction," it's called the **spectral norm**, and it's the single
number that controls a layer's worst-case sensitivity.

### The definitions

The **spectral norm** of $W$ is

$$\|W\|_2 = \sigma_{\max}(W) = \max_{x \ne 0} \frac{\|Wx\|}{\|x\|}$$

- $\sigma_{\max}(W)$ — the largest singular value of $W$ (top stretch factor from
  its SVD).
- The right-hand expression literally reads "the biggest output-length-to-
  input-length ratio over all inputs" — the worst-case amplification.

A function $f$ is **$L$-Lipschitz** if it never amplifies distances by more than
$L$:

$$\|f(x) - f(y)\| \le L\,\|x - y\| \quad \text{for all } x, y.$$

For a linear map $f(x)=Wx$, the smallest such $L$ is *exactly* $\|W\|_2$. And
because most nonlinearities (ReLU, sigmoid, tanh) are themselves 1-Lipschitz
(they never stretch distances), the Lipschitz constant of a *whole network* is at
most the **product of the layers' spectral norms**:

$$L_{\text{net}} \le \prod_{\ell} \|W_\ell\|_2.$$

That product is the master dial for network smoothness. If each layer's spectral
norm sits above 1, the product explodes with depth (jumpy network, exploding
gradients); keep them near 1 and the network stays controlled. This is the
mathematical heart of **spectral normalization** in GANs and of certified
adversarial robustness.

### Worked example

```python
import numpy as np

W = np.array([[2.0, 0.0],
              [0.0, 0.5]])     # stretches x-axis 2x, squashes y-axis to 0.5x

spectral_norm = np.linalg.norm(W, 2)          # largest singular value
print("spectral norm ||W||_2 =", spectral_norm)   # 2.0 -> worst-case amplification

# Verify empirically: hunt for the direction that gets amplified most
ratios = []
for theta in np.linspace(0, np.pi, 1000):
    x = np.array([np.cos(theta), np.sin(theta)])  # unit vectors all around
    ratios.append(np.linalg.norm(W @ x))          # output length (input length=1)
print("max observed amplification:", max(ratios).round(4))  # ~2.0, matches
```

The empirical max amplification matches the spectral norm — the matrix can stretch
some direction (here, the x-axis) by exactly $2\times$, and never more. That "never
more" is the Lipschitz guarantee in your hands.

> **Try this in Hermes:** "Have me compute, by hand, the Lipschitz upper bound of a
> 3-layer net with spectral norms 1.2, 0.8, and 1.5. Is it stable?"
> **Try this in Claude:** "Explain how spectral normalization in GANs uses
> $\|W\|_2$ to stop the discriminator from becoming too jumpy."

---

## 8.3 Low-rank structure in trained networks

### Conceptual bridge

Here's something surprising and deeply useful. A weight matrix might be, say,
$512\times 512$ — full rank in principle, 512 independent directions of stretch.
But when you train a network and then look at the singular values of its learned
weights, you usually find that *most of them are tiny*. A handful of directions
carry almost all the action; the rest barely stretch anything. The matrix is
**effectively low-rank** even though it's technically full-rank.

The picture from Section 5: SVD writes $W$ as a sum of rank-1 pieces, each scaled
by a singular value. If singular value #50 onward are near zero, then those 460+
pieces contribute almost nothing — you could throw them away and barely change the
network. *That* is why pruning, low-rank compression, and LoRA work.

### The structure

From the SVD $W = U\Sigma V^\top$, with singular values
$\sigma_1 \ge \sigma_2 \ge \cdots \ge 0$:

$$W = \sum_{i=1}^{r} \sigma_i\, u_i v_i^\top$$

- $u_i, v_i$ — the $i$-th left/right singular vectors (rank-1 building blocks).
- $\sigma_i$ — how much the $i$-th block contributes.
- **Effective rank** — the number of singular values that are non-negligible
  (above some threshold). Trained weights tend to have effective rank far below
  their dimension.

Keep only the top $k$ terms and you get the **best rank-$k$ approximation** of $W$
(the Eckart–Young theorem from Section 5). If $k \ll d$, you've compressed
$d\times d = d^2$ numbers down to $k(2d+1)$ — a huge saving when $k$ is small.

This is the entire premise of **LoRA** (Low-Rank Adaptation): instead of
fine-tuning a giant weight matrix $W$, you freeze it and learn a tiny low-rank
*update* $\Delta W = AB$ where $A$ is $d\times k$ and $B$ is $k\times d$ with
$k$ tiny (say 8). You're betting that the *change* a network needs to adapt to a
new task is low-rank — and empirically, it is.

### Worked example — analyze a "trained" weight matrix

```python
import numpy as np

# Simulate a trained matrix that is secretly near low-rank:
# a strong rank-3 signal plus a little full-rank noise.
np.random.seed(1)
d = 64
A = np.random.randn(d, 3)
B = np.random.randn(3, d)
W = A @ B + 0.01 * np.random.randn(d, d)   # effective rank ~ 3

# Full numerical rank vs. effective rank
print("numpy rank (full):", np.linalg.matrix_rank(W))   # likely 64
U, S, Vt = np.linalg.svd(W)
print("top 6 singular values:", S[:6].round(3))
print("tail singular values: ", S[6:9].round(4), "...")  # tiny -> negligible

# Energy captured by the top-k components (sum of squared singular values)
energy = np.cumsum(S**2) / np.sum(S**2)
for k in [1, 2, 3, 5, 10]:
    print(f"top-{k:>2} components capture {energy[k-1]*100:5.1f}% of the energy")

# Best rank-3 approximation -- compress 64x64 down to 3 directions
W_k = (U[:, :3] * S[:3]) @ Vt[:3]
rel_err = np.linalg.norm(W - W_k) / np.linalg.norm(W)
print(f"\nrank-3 reconstruction relative error: {rel_err:.4f}  (tiny -> safe to prune)")

# ---- plot the singular value spectrum (the 'scree' that reveals low rank) ----
import matplotlib
matplotlib.use("Agg")          # headless: write a file, don't pop a window
import matplotlib.pyplot as plt
plt.figure(figsize=(6, 4))
plt.semilogy(range(1, d + 1), S, marker="o", ms=3)
plt.xlabel("singular value index"); plt.ylabel("magnitude (log)")
plt.title("Singular value spectrum: a cliff = effective low rank")
plt.tight_layout(); plt.savefig("weight_spectrum.png", dpi=120)
print("saved weight_spectrum.png  -- look for the cliff after index 3")
```

The "cliff" in the log-scale plot is the visual signature of low rank: a few big
singular values, then a plunge to near-zero. When you see that cliff in a real
trained layer, you've found a layer that's begging to be compressed.

> **Try this in Hermes:** "Walk me through why keeping the top-$k$ singular triplets
> is provably the *best* rank-$k$ approximation (Eckart–Young). One sentence of
> intuition, then the statement."
> **Try this in Claude:** "Explain LoRA to me in terms of the low-rank update
> $\Delta W = AB$ — why is the *update* low-rank even when $W$ isn't?"

---

## 8.4 Connections to ML — weight geometry in practice

The three diagnostics above (affine structure, spectral norm, low rank) aren't
academic — they're the lens behind everyday training tricks:

- **Weight decay as spectral regularization.** Adding $\lambda\|W\|_F^2$ to the
  loss (L2 / weight decay) penalizes the *sum of squared singular values*
  ($\|W\|_F^2 = \sum_i \sigma_i^2$). So weight decay literally pushes singular
  values down — shrinking the spectral norm, smoothing the network, and nudging
  it toward lower effective rank. The "keep weights small" folklore is, in the
  SVD basis, "keep the stretch factors small."

- **Initialization as scaling (Xavier/Glorot, He).** When you initialize $W$, you
  want each layer to roughly *preserve* the variance of its activations — neither
  amplifying (toward explosion) nor shrinking (toward vanishing) as signals pass
  through. That's a spectral-norm-near-1 condition. Xavier scales the random init
  by $\sqrt{1/d_{\text{in}}}$ (for tanh-ish nets), He by $\sqrt{2/d_{\text{in}}}$
  (for ReLU, which kills half the signal and so needs the extra factor of 2). Both
  are just choosing the random matrix's scale so its singular values cluster near
  1 — keeping the forward/backward signal at a stable amplitude through depth.
  This is §8.2's Lipschitz product, applied at birth.

- **Pruning and compression.** §8.3's low-rank cliff is why you can delete a large
  fraction of weights (magnitude pruning) or factor layers into thin products
  (low-rank factorization, LoRA) with little accuracy loss. The network was using
  far fewer effective directions than it had parameters.

The unifying thesis: **the singular value spectrum of a weight matrix is its
fingerprint.** Spread-out spectrum = full-capacity, jumpy, big. Concentrated
spectrum with a cliff = smooth, compressible, well-regularized. Every trick above
is, secretly, spectrum-shaping. For H&C, this is the same math you'd use to keep a
learned learner-model compact enough to run cheaply per student.

---

## 8.5 Section recap

**Explain out loud (no notes):**
1. "A layer computes $h = Wx + b$, which is an *affine* map because…" — and why
   networks would collapse without nonlinearities.
2. "The spectral norm $\|W\|_2$ is the largest singular value, and it controls…"
   — connect it to Lipschitz / sensitivity / exploding gradients.
3. "Trained weights are often effectively low-rank, which means I can…" — name two
   things this enables.
4. "Weight decay shrinks the spectrum because…" and "He vs. Xavier init differ
   because…"

If the spectral-norm-to-Lipschitz link is fuzzy, that's the structural keystone —
reread §8.2.

### Memory tiers for THIS section

**CARRY (memorize):**
- $h = Wx + b$ (affine = linear + shift); composition of linear maps = one linear
  map (so nonlinearities are essential)
- $\|W\|_2 = \sigma_{\max}(W)$ = worst-case amplification = Lipschitz constant of
  the linear map
- "Trained weight matrices are usually effectively low-rank"

**RECONSTRUCT (re-derive):**
- $L_{\text{net}} \le \prod_\ell \|W_\ell\|_2$ (product of spectral norms)
- $\|W\|_F^2 = \sum_i \sigma_i^2$, so weight decay shrinks singular values
- Best rank-$k$ approx = top-$k$ SVD triplets (Eckart–Young)
- He's extra factor of 2 vs. Xavier (ReLU kills half the signal)

**LOOKUP (know it exists):**
- Exact Xavier/He variance formulas per activation
- Power-iteration trick for fast spectral-norm estimation in spectral norm layers
- LoRA rank/alpha hyperparameter conventions

> **Closing interaction prompt —**
> **Try this in Hermes:** "Give me a random weight matrix; have me report its rank,
> spectral norm, and top-5 singular values, then say whether it's compressible."
> **Try this in Claude:** "Take a real pretrained layer (e.g. a `nn.Linear` from a
> small model), plot its singular value spectrum, and tell me how aggressively I
> could prune or LoRA-adapt it based on the cliff."
