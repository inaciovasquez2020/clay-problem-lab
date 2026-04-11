# DDYO RA1n Multiplier Kernel Route

## Annular multiplier route

For
\[
q_{k,m}(\xi):=\frac{-\,i\,\xi_m}{|\xi|^2}\,\chi_k(\xi),
\]
with \(\chi_k\) supported in
\[
\{\xi\in\mathbb R^3:c\,2^k\le |\xi|\le C\,2^k\},
\]
the desired annular potential estimate follows from the kernel bound
\[
\|\mathcal F^{-1}q_{k,m}\|_{L^1}\le C\,2^{-k}.
\]

Indeed, defining
\[
H_{k,m}:=\mathcal F^{-1}\!\bigl(q_{k,m}\widehat{f_k}\bigr),
\]
one gets
\[
\|H_{k,m}\|_{L^1}
\le
\|\mathcal F^{-1}q_{k,m}\|_{L^1}\,\|f_k\|_{L^1}
\le
C\,2^{-k}\|f_k\|_{L^1}.
\]

## Scaling reduction

Write
\[
q_{k,m}(\xi)=2^{-k}Q_m(2^{-k}\xi),
\qquad
Q_m(\eta):=\frac{-\,i\,\eta_m}{|\eta|^2}\,\chi(\eta),
\]
where \(\chi\) is supported in a fixed annulus.

Then
\[
\mathcal F^{-1}q_{k,m}(x)=2^{-k}2^{3k}K_m(2^k x),
\qquad
K_m:=\mathcal F^{-1}Q_m,
\]
hence
\[
\|\mathcal F^{-1}q_{k,m}\|_{L^1}=2^{-k}\|K_m\|_{L^1}.
\]

Therefore the annular potential estimate reduces to the fixed-scale bound
\[
\|K_m\|_{L^1}<\infty.
\]

## Remaining local task

Prove
\[
Q_m\in \mathcal S(\mathbb R^3),
\]
equivalently that the annular cutoff removes the origin singularity and yields an \(L^1\) Schwartz kernel at unit scale.

## Status

Open reduction target.
