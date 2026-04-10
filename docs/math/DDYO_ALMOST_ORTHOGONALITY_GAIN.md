# DDYO Almost-Orthogonality Gain

## Remaining shellwise ingredient

After the kernel first-moment estimate
\[
\int |K_j(z)|\,|z|\,dz \lesssim 2^{-j},
\]
the remaining task is to extract one further effective \(2^{-j}\) from shell localization / almost-orthogonality.

## Terminal shellwise target

For
\[
B_j[u]
:=
2^{2j}\!\int \mathcal H'(\omega_j)\cdot
[\widetilde P_j,S_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx,
\]
prove a decomposition
\[
B_j[u]=\sum_{|k-j|\le C} B_{j,k}[u]
\]
with
\[
|B_{j,k}[u]|
\le
2^{-(j+k)}\,a_{j,k},
\]
where
\[
\sum_{j}\sum_{|k-j|\le C} a_{j,k}
\le
\varepsilon\bigl(\mathcal D[u]+\lambda\mathcal C_{\mathrm{DDYO}}[u]\bigr)
+
C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr),
\qquad 0<\varepsilon<1.
\]

## Weakest sufficient mechanism

It is sufficient to prove:
\[
[\widetilde P_j,S_{\sim j}\!\cdot\nabla]\omega_{\sim j}
=
\sum_{|k-j|\le C} T_{j,k}(\nabla S_k,\omega_k),
\]
with
\[
\|T_{j,k}(\nabla S_k,\omega_k)\|_{L^1}
\le
C\,2^{-j}2^{-k}\,\|\nabla S_k\|_{L^\infty}\,\|\omega_k\|_{L^1}.
\]

## Consequence

This produces the second effective \(2^{-j}\), closes
\[
\sum_j B_j[u],
\]
and therefore completes the DDYO continuum high-high absorbability step.
