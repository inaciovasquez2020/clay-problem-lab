# DDYO Mollified Symmetric Commutator Bound

## Target estimate

For a smooth positive dyadic family \((\widetilde P_j)_j\),
prove
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

## Kernel form

With
\[
\widetilde P_j f(x)=\int K_j(x-y)f(y)\,dy,
\]
write
\[
[\widetilde P_j,S_{\sim j}\!\cdot\nabla]g(x)
=
\int K_j(x-y)\bigl(S_{\sim j}(x)-S_{\sim j}(y)\bigr)\cdot \nabla g(y)\,dy.
\]

## Weakest sufficient bound

It is sufficient to prove
\[
\|[\widetilde P_j,S_{\sim j}\!\cdot\nabla]g\|_{L^1}
\le
C\,\|\nabla S_{\sim j}\|_{L^\infty}\,\|g\|_{L^1}
\]
with a dyadic gain strong enough after multiplication by \(2^{2j}\) and summation to yield one global \(\varepsilon<1\).

## Required new ingredient

A Coifman--Meyer / Constantin--E--Titi type commutator estimate at the exact DDYO critical weights.

## Consequence

Combined with mollified skew cancellation and lower-order projector replacement,
this closes continuum DDYO high-high absorbability.
