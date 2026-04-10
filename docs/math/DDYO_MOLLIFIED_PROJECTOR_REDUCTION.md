# DDYO Mollified Projector Reduction

## New ingredient

Construct a smooth positive dyadic family \((\widetilde P_j)_j\) with symbol
\[
\widetilde m_j(\xi)=\rho(2^{-j}\xi),
\]
where \(\rho\in C_c^\infty(\mathbb R^3)\), \(\rho\ge 0\), and \(\rho\) is supported in a fixed dyadic annulus.

## Target reduction

For every smooth scalar or vector field \(f\),
\[
[P_j,f]-[\widetilde P_j,f]
\]
is lower-order in the sense that
\[
\left\|([P_j,f]-[\widetilde P_j,f])g\right\|_{L^1}
\le
C\,2^{-j}\|\nabla f\|_{L^\infty}\|g\|_{L^1}
\]
up to an admissible summable dyadic remainder.

## Consequence

If this reduction holds, the continuum DDYO symmetric commutator pairing frontier reduces to the mollified identity/bound pair:
\[
\sum_j 2^{2j}\!\int \mathcal H'(\omega_j)\cdot [\widetilde P_j,\Omega_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx = 0,
\]
and
\[
\left|
\sum_j 2^{2j}\!\int \mathcal H'(\omega_j)\cdot [\widetilde P_j,S_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx
\right|
\le
\varepsilon\bigl(\mathcal D[u]+\lambda\mathcal C_{\mathrm{DDYO}}[u]\bigr)
+
C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr).
\]

## Status

This is the next structural reduction.
