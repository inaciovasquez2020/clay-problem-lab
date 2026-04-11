# DDYO RA1n Reduction Chain

## Conditional reduction theorem

Assume the annular potential estimate:

For every dyadic-frequency function \(f_k\) with
\[
\operatorname{supp}\widehat{f_k}\subset\{\xi\in\mathbb R^3:c\,2^k\le|\xi|\le C\,2^k\},
\]
there exists \(H_k\) such that
\[
f_k=\nabla\!\cdot H_k
\qquad\text{and}\qquad
\|H_k\|_{L^1}\le C\,2^{-k}\|f_k\|_{L^1}.
\]

Assume also the gradient bound:
\[
\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
\]

Then for
\[
f_k=e^{(j)}_{ab}(D)\omega_k,
\]
one has
\[
\left|
\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
\right|
\le
C\,2^{-j}2^{-k}\|\omega_k\|_{L^1}.
\]

## Consequence

The RA1n first-moment estimate follows from the conjunction of:

1. `docs/math/DDYO_RA1N_ANNULAR_POTENTIAL_ESTIMATE.md`
2. `docs/math/DDYO_RA1N_GRADIENT_BOUND.md`

## Status

Open reduction target.
