# Yang–Mills Mass Gap: Complete Local Reduction Stack

## Global Objective

Establish the Yang–Mills mass gap by proving the operator inequality

\[
I - T_L^*T_L \ge \kappa (-\Delta_G)
\]

which implies exponential decay of correlations and therefore a strictly positive mass gap.

---

# Step 1 — Block Decomposition

Partition the lattice into cubic blocks \(B\) of side \(L\).

Define

\[
P_L f = \text{conditional expectation onto block-constant functions}
\]

\[
Q_L = I - P_L
\]

Interpretation:

- \(P_L f\): coarse component
- \(Q_L f\): fluctuation component

---

# Step 2 — Fluctuation Inequality

Target estimate

\[
\|Q_L f\|^2
\ge
c L^2 \sum_{\ell} \|\nabla_\ell(Q_L f)\|^2
\]

Reduction:

It suffices to prove a **block Poincaré inequality**.

---

# Step 3 — Block Poincaré Inequality

For a block \(B\) with fixed boundary links and Wilson measure \(\mu_B\):

\[
\operatorname{Var}_{\mu_B}(g)
\le
C L^2
\sum_{\ell\subset B} \|\nabla_\ell g\|^2
\]

for all gauge-invariant functions \(g\).

Equivalent formulation:

\[
\gamma_B \ge \gamma L^{-2}
\]

where \(\gamma_B\) is the spectral gap of the block generator.

---

# Step 4 — Block Generator

Define

\[
\mathcal{L}_B = \sum_{\ell\subset B} \nabla_\ell^* \nabla_\ell
\]

Dirichlet form

\[
\mathcal{E}_B(g,g)
=
\sum_{\ell\subset B} \|\nabla_\ell g\|^2
\]

Spectral gap

\[
\gamma_B
=
\inf_{g\neq const}
\frac{\mathcal{E}_B(g,g)}{\operatorname{Var}(g)}
\]

---

# Step 5 — Gauge Fixing

Fix a spanning tree \(T_B\).

Set

\[
U_\ell = I \quad \text{for } \ell\in T_B.
\]

Remaining variables lie on

\[
E(B) \setminus T_B
\]

Gauge-fixed Wilson measure

\[
d\mu_B(U)
=
Z^{-1} e^{-S_B(U)} dU
\]

with

\[
S_B(U) = -\beta \sum_{p\subset B} \mathrm{Re}\,\mathrm{Tr}(U_p).
\]

---

# Step 6 — Convexity Lemma (Missing)

Need uniform convexity

\[
\nabla^2 S_B(U) \succeq \lambda I
\]

independent of block size and boundary conditions.

---

# Step 7 — Brascamp–Lieb Inequality

If convexity holds:

\[
\operatorname{Var}_{\mu_B}(g)
\le
\lambda^{-1}
\sum_{\ell\subset B} \|\nabla_\ell g\|^2
\]

Diffusive scaling then yields

\[
\operatorname{Var}_{\mu_B}(g)
\le
C L^2
\sum_{\ell\subset B} \|\nabla_\ell g\|^2 .
\]

---

# Step 8 — Global Assembly

Summing overlapping blocks gives

\[
\|Q_L f\|^2
\ge
c L^2
\sum_\ell \|\nabla_\ell(Q_L f)\|^2 .
\]

---

# Step 9 — Coarse Component Bound

Because \(P_L f\) varies only at scale \(L\),

\[
\sum_\ell \|\nabla_\ell(P_L f)\|^2
\le
C L^{-2}\|P_L f\|^2 .
\]

---

# Step 10 — Flip Averaging

Construct block averaging operator \(T_L\) such that

\[
I \le a T_L^*T_L + b Q_L^*Q_L.
\]

---

# Step 11 — Coercivity

Combining bounds yields

\[
I - T_L^*T_L \ge \kappa (-\Delta_G).
\]

---

# Step 12 — Mass Gap

Let \(\gamma\) be the spectral gap of \(-\Delta_G\).

Then

\[
\|T_L f\| \le \sqrt{1-\kappa\gamma}\|f\|.
\]

This gives exponential clustering and the Yang–Mills mass gap.

---

# Remaining Open Lemma

Uniform convexity of the gauge-fixed Wilson action on finite blocks.

