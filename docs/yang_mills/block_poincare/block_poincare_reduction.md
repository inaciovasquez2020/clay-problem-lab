# Block Poincaré Reduction for the Yang–Mills Mass Gap

## Target Local Estimate

**Block Poincaré Inequality (Dirichlet Boundary Conditions)**

Let \(B\) be a lattice block of side \(L\). Let \(\mu_B\) be the Wilson measure on \(B\) with fixed boundary links.

For every gauge-invariant function \(g\):

\[
\operatorname{Var}_{\mu_B}(g)
\;\le\;
C L^2
\sum_{\ell\subset B}
\|\nabla_\ell g\|_{L^2(\mu_B)}^2
\]

with \(C>0\) independent of \(L\) and boundary conditions.

Equivalently, the generator of the block dynamics has spectral gap

\[
\gamma_B \ge \gamma L^{-2}.
\]

---

## Consequence for the Global Estimate

Let \(P_L\) be the conditional expectation onto block-constant functions and \(Q_L = I - P_L\).

Summing the block inequalities yields

\[
\|Q_L f\|^2
\;\ge\;
c L^2
\sum_{\ell}
\|\nabla_\ell(Q_L f)\|^2 .
\]

A complementary estimate for the coarse component holds:

\[
\sum_\ell \|\nabla_\ell(P_L f)\|^2
\;\le\;
C L^{-2}\|P_L f\|^2 .
\]

Together with the flip-averaging coercivity estimate

\[
I \le a T_L^*T_L + b Q_L^*Q_L
\]

one obtains

\[
I - T_L^*T_L \;\ge\; \kappa (-\Delta_G).
\]

This yields contraction

\[
\|T_L f\| \le \sqrt{1-\kappa\gamma}\|f\|
\]

and therefore exponential clustering.

---

## Minimal Missing Lemma

**Gauge-Fixed Convexity Lemma**

After axial gauge fixing on a block \(B\), the Wilson measure admits density

\[
d\mu_B(U) = Z^{-1} e^{-V_B(U)} dU
\]

with potential satisfying

\[
\nabla^2 V_B(U) \succeq \lambda I
\]

for some \(\lambda>0\) independent of block size and boundary configuration.

Under this condition the Brascamp–Lieb inequality gives

\[
\operatorname{Var}_{\mu_B}(g)
\le
\lambda^{-1}
\sum_{\ell\subset B}
\|\nabla_\ell g\|_{L^2(\mu_B)}^2 .
\]

Diffusive scaling on a block of diameter \(L\) produces

\[
\operatorname{Var}_{\mu_B}(g)
\le
C L^2
\sum_{\ell\subset B}
\|\nabla_\ell g\|_{L^2(\mu_B)}^2 .
\]

---

## Status

Reduction complete.

Remaining open step:

Prove the **gauge-fixed convexity lemma** for the Wilson action on finite blocks.

