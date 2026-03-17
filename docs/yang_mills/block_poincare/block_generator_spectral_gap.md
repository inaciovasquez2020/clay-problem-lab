# Block Generator and Spectral Gap Formulation

## Block Configuration Space

Let \(B\subset \mathbb{Z}^d\) be a cubic block of side \(L\).

Let
\[
\Omega_B = G^{E(B)}
\]
be the space of link variables on edges inside \(B\), where \(G = SU(N)\).

Boundary links are fixed.

The Wilson measure on the block is

\[
d\mu_B(U)
=
Z_B^{-1}
\exp\!\Big(
\beta \sum_{p\subset B} \mathrm{Re}\,\mathrm{Tr}(U_p)
\Big)
dU .
\]

---

## Block Generator

Define the block Glauber generator

\[
\mathcal{L}_B
=
\sum_{\ell\subset B} \nabla_\ell^* \nabla_\ell .
\]

The Dirichlet form is

\[
\mathcal{E}_B(g,g)
=
\sum_{\ell\subset B}
\|\nabla_\ell g\|_{L^2(\mu_B)}^2 .
\]

---

## Spectral Gap Formulation

The block Poincaré inequality is equivalent to

\[
\operatorname{Var}_{\mu_B}(g)
\le
\gamma_B^{-1}\,
\mathcal{E}_B(g,g)
\]

where

\[
\gamma_B
=
\inf_{g\neq const}
\frac{\mathcal{E}_B(g,g)}{\operatorname{Var}_{\mu_B}(g)} .
\]

---

## Target Scaling

We require

\[
\gamma_B
\ge
\gamma L^{-2}
\]

with \(\gamma>0\) independent of \(L\).

---

## Reduction

If the block spectral gap bound holds then

\[
\operatorname{Var}_{\mu_B}(g)
\le
C L^2
\sum_{\ell\subset B}
\|\nabla_\ell g\|^2 .
\]

Summation over overlapping blocks yields the global fluctuation inequality.

---

## Remaining Lemma

Uniform spectral gap for the Wilson block generator under Dirichlet boundary conditions.

