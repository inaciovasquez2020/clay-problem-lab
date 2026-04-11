# DDYO RA1n: verified first-moment decay for r_k

## Setup

Assume
\[
\widehat G_k(\xi)=\varphi(2^{-k}\xi)|\xi|^{-4},
\qquad
\varphi\in C_c^\infty(\mathbb R^3),
\qquad
\operatorname{supp}\varphi\subset\{\eta:c_0\le |\eta|\le C_0\}.
\]

Fix \(\xi_k\) with \(|\xi_k|\sim 2^k\), define
\[
P_k f(\xi)=f(\xi_k)+\nabla f(\xi_k)\cdot(\xi-\xi_k),
\qquad
r_k(\xi)=\widehat G_k(\xi)-P_k\widehat G_k(\xi).
\]

## Verified bound

For every multi-index \(\alpha\),
\[
|\partial_\xi^\alpha r_k(\xi)|
\le
C_\alpha\,2^{-k(4+|\alpha|)}
\le
C_\alpha\,2^{-k(2+|\alpha|)}
\]
on \(\operatorname{supp}\varphi(2^{-k}\cdot)\).

## Proof

For every multi-index \(\beta\),
\[
\partial_\xi^\beta \widehat G_k(\xi)
=
\sum_{\gamma+\delta=\beta}
c_{\gamma,\delta}\,
\partial^\gamma(\varphi(2^{-k}\xi))\,
\partial^\delta(|\xi|^{-4}),
\]
hence on the dyadic shell \(|\xi|\sim 2^k\),
\[
|\partial_\xi^\beta \widehat G_k(\xi)|
\le
C_\beta\,2^{-k(4+|\beta|)}.
\]

Differentiated Taylor remainder gives
\[
\partial^\alpha r_k(\xi)
=
\sum_{|\beta|=2}
(\xi-\xi_k)^\beta
\int_0^1 (1-t)\,
\partial^{\alpha+\beta}\widehat G_k(\xi_k+t(\xi-\xi_k))\,dt.
\]
Since \(|\xi-\xi_k|\lesssim 2^k\) on one shell,
\[
|\partial^\alpha r_k(\xi)|
\le
C\,2^{2k}\sup_{y\sim 2^k}|\partial^{\alpha+2}\widehat G_k(y)|
\le
C_\alpha\,2^{-k(4+|\alpha|)}.
\]

## Consequence

The required \(2^{-k}\) gain is available a fortiori. Any remaining RA1n obstruction is no longer at the \(r_k\) first-moment stage.
