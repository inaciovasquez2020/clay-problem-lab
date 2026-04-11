# DDYO RA1n Annular Potential Estimate

## Target lemma

Let \(f_k\in L^1(\mathbb R^3)\) satisfy
\[
\operatorname{supp}\widehat{f_k}\subset\{\xi\in\mathbb R^3:c\,2^k\le |\xi|\le C\,2^k\}.
\]

Define
\[
\widehat{H_{k,m}}(\xi):=\frac{-\,i\,\xi_m}{|\xi|^2}\,\widehat{f_k}(\xi),
\qquad m=1,2,3.
\]

Then
\[
f_k=\nabla\!\cdot H_k
\]
and
\[
\|H_k\|_{L^1}\le C\,2^{-k}\|f_k\|_{L^1}.
\]

## RA1n consequence

Applied to
\[
f_k=e^{(j)}_{ab}(D)\omega_k,
\]
this yields
\[
e^{(j)}_{ab}(D)\omega_k=\nabla\!\cdot H^{ab}_{j,k},
\qquad
\|H^{ab}_{j,k}\|_{L^1}\le C\,2^{-k}\|\omega_k\|_{L^1}.
\]

Combined with
\[
\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
\]
it implies
\[
\left|
\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
\right|
\le
C\,2^{-j}2^{-k}\|\omega_k\|_{L^1}.
\]

## Status

Open reduction target.
