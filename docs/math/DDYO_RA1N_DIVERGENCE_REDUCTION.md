# DDYO RA1n Divergence Reduction

## Reduction lemma

Assume that for each dyadic-frequency function \(f_k\) with
\[
\operatorname{supp}\widehat{f_k}\subset\{\xi\in\mathbb R^3:c\,2^k\le |\xi|\le C\,2^k\},
\]
there exists a vector field \(H_k=(H_{k,1},H_{k,2},H_{k,3})\) such that
\[
f_k=\nabla\!\cdot H_k
\]
and
\[
\|H_k\|_{L^1}\le C\,2^{-k}\|f_k\|_{L^1}.
\]

Apply this with
\[
f_k=e^{(j)}_{ab}(D)\omega_k.
\]

Then there exists \(H^{ab}_{j,k}\) such that
\[
e^{(j)}_{ab}(D)\omega_k=\nabla\!\cdot H^{ab}_{j,k}
\]
and
\[
\|H^{ab}_{j,k}\|_{L^1}\le C\,2^{-k}\|\omega_k\|_{L^1}.
\]

Hence
\[
\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
=
-\int_{\mathbb R^3}\partial_m\!\bigl(x_\ell G_j(x)\bigr)\,H^{ab}_{j,k,m}(x)\,dx
\]
and therefore
\[
\left|
\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
\right|
\le
\|\nabla(x_\ell G_j)\|_{L^\infty}\,\|H^{ab}_{j,k}\|_{L^1}.
\]

Consequently, if
\[
\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
\]
then
\[
\left|
\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
\right|
\le
C\,2^{-j}2^{-k}\|\omega_k\|_{L^1}.
\]

## Status

This reduces RA1n to the annular divergence-potential estimate together with the bound
\[
\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
\]
