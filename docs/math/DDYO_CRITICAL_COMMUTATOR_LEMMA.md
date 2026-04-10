# DDYO Critical Commutator Lemma

## Terminal new ingredient

For a smooth positive dyadic family \((\widetilde P_j)_j\) with even real symbol and kernels \(K_j\),
prove the shellwise bound
\[
2^{2j}\left|
\int \mathcal H'(\omega_j)\cdot [\widetilde P_j,S_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx
\right|
\le
\varepsilon_j\bigl(\mathcal D_j[u]+\lambda\mathcal C_j[u]\bigr)
+
C_j\bigl(\Phi_j[u]+\lambda R_j^{\mathrm{cont}}[u]\bigr),
\]
with
\[
\sum_j \varepsilon_j < 1,
\qquad
\sum_j C_j\bigl(\Phi_j[u]+\lambda R_j^{\mathrm{cont}}[u]\bigr)
\lesssim
\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u].
\]

## Weakest sufficient local estimate

It is sufficient to establish
\[
\|[\widetilde P_j,S_{\sim j}\!\cdot\nabla]g\|_{L^1}
\le
C\,2^{-2j}\,\alpha_j\,\|g\|_{L^1},
\]
where
\[
\sum_j \alpha_j \lesssim \varepsilon\,\lambda^{-1}\bigl(\mathcal D[u]+\lambda\mathcal C_{\mathrm{DDYO}}[u]\bigr)
+
C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr).
\]

## Kernel reduction

Using
\[
[\widetilde P_j,S_{\sim j}\!\cdot\nabla]g(x)
=
\int K_j(x-y)\bigl(S_{\sim j}(x)-S_{\sim j}(y)\bigr)\cdot\nabla g(y)\,dy,
\]
the terminal task is to extract the exact dyadic gain needed for the weighted summation.

## Consequence

This lemma, together with mollified skew cancellation and lower-order projector replacement, yields
\[
\left|
\sum_j 2^{2j}\!\int \mathcal H'(\omega_j)\cdot [\widetilde P_j,S_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx
\right|
\le
\varepsilon\bigl(\mathcal D[u]+\lambda\mathcal C_{\mathrm{DDYO}}[u]\bigr)
+
C_\varepsilon\bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\bigr),
\qquad 0<\varepsilon<1.
\]
