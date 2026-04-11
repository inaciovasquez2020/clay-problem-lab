# DDYO RA1n Gradient Bound

## Target lemma

For the dyadic kernel factor \(G_j\),
\[
\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
\]

## RA1n consequence

If
\[
e^{(j)}_{ab}(D)\omega_k=\nabla\!\cdot H^{ab}_{j,k}
\qquad\text{and}\qquad
\|H^{ab}_{j,k}\|_{L^1}\le C\,2^{-k}\|\omega_k\|_{L^1},
\]
then
\[
\left|
\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
\right|
=
\left|
\int_{\mathbb R^3}\partial_m(x_\ell G_j)(x)\,H^{ab}_{j,k,m}(x)\,dx
\right|
\le
C\,2^{-j}2^{-k}\|\omega_k\|_{L^1}.
\]

## Status

Open reduction target.
