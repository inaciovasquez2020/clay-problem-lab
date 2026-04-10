# DDYO Dyadic Gain Extraction

## Next terminal reduction

Starting from
\[
[\widetilde P_j,S_{\sim j}\!\cdot\nabla]g(x)
=
\int K_j(x-y)\bigl(S_{\sim j}(x)-S_{\sim j}(y)\bigr)\cdot \nabla g(y)\,dy,
\]
extract the exact shellwise gain needed to offset the DDYO weight \(2^{2j}\).

## Weakest sufficient shellwise bound

It is sufficient to prove
\[
\|[\widetilde P_j,S_{\sim j}\!\cdot\nabla]g\|_{L^1}
\le
c_j\,2^{-2j}\|g\|_{L^1},
\]
with coefficients \(c_j\ge 0\) satisfying
\[
\sum_j c_j
\le
\varepsilon\,\lambda^{-1}\bigl(\mathcal D[u]+\lambda\mathcal C_{\mathrm{DDYO}}[u]\bigr)
+
C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr),
\qquad 0<\varepsilon<1.
\]

## Structural decomposition

Write
\[
S_{\sim j}(x)-S_{\sim j}(y)
=
(x-y)\cdot \int_0^1 \nabla S_{\sim j}(y+\theta(x-y))\,d\theta.
\]
Then
\[
[\widetilde P_j,S_{\sim j}\!\cdot\nabla]g(x)
=
\int K_j(x-y)(x-y)\cdot
\left(
\int_0^1 \nabla S_{\sim j}(y+\theta(x-y))\,d\theta
\right)\nabla g(y)\,dy.
\]

## Required kernel gain

The terminal estimate is to prove
\[
\int |K_j(z)|\,|z|\,dz \lesssim 2^{-j},
\]
and recover one additional effective \(2^{-j}\) from the shell localization / almost-orthogonality structure, yielding net \(2^{-2j}\).

## Consequence

This shellwise gain closes the weighted summation
\[
\sum_j 2^{2j}\!\int \mathcal H'(\omega_j)\cdot
[\widetilde P_j,S_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx
\]
with one global \(\varepsilon<1\), completing the DDYO continuum high-high absorbability step.
