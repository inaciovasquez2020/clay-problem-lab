# DDYO RA1n Fixed-Scale Schwartz Kernel

## Fixed-scale lemma

Let
\[
Q_m(\eta):=\frac{-\,i\,\eta_m}{|\eta|^2}\,\chi(\eta),
\]
where \(\chi\in C_c^\infty(\mathbb R^3)\) is supported in a fixed annulus
\[
\{\eta\in\mathbb R^3:c\le |\eta|\le C\}.
\]

Then
\[
Q_m\in C_c^\infty(\mathbb R^3).
\]

Consequently,
\[
K_m:=\mathcal F^{-1}Q_m\in \mathcal S(\mathbb R^3),
\]
and in particular
\[
\|K_m\|_{L^1}<\infty.
\]

## Kernel consequence

For
\[
q_{k,m}(\xi)=2^{-k}Q_m(2^{-k}\xi),
\]
one has
\[
\mathcal F^{-1}q_{k,m}(x)=2^{-k}2^{3k}K_m(2^k x)
\]
and therefore
\[
\|\mathcal F^{-1}q_{k,m}\|_{L^1}=2^{-k}\|K_m\|_{L^1}\le C\,2^{-k}.
\]

## RA1n consequence

This closes the annular potential estimate:
\[
\|H_k\|_{L^1}\le C\,2^{-k}\|f_k\|_{L^1}.
\]

Combined with
\[
\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
\]
it yields
\[
\left|
\int_{\mathbb R^3} x_\ell G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
\right|
\le
C\,2^{-j}2^{-k}\|\omega_k\|_{L^1}.
\]

## Status

Conditional on the gradient bound
\[
\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
\]
