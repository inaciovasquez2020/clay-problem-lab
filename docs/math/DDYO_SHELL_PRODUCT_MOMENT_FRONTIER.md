# DDYO Shell-Product Moment Frontier

## Weakest sufficient remaining lemma

For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
\[
\left|
\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
\right|
\le
C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
\]

Together with the zeroth-moment identity
\[
\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
\]
this is sufficient to recover the shell-product \(H^1\) gain and hence
\[
\left|
\int G_j\cdot
\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
\right|
\le
C\,2^{-j}2^{-k}\,
\|\nabla S_k\|_{L^\infty}\,
\|\omega_k\|_{L^1},
\qquad |j-k|\le C.
\]

## Equivalent absorption form

It is equivalently sufficient to prove that for every \(\varepsilon\in(0,1)\),
\[
\left|
\int G_j\cdot
\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
\right|
\le
\varepsilon\,\mathcal D_{j,k}[u]
+
C_\varepsilon\Bigl(\Phi[u]+\lambda R^{\mathrm{cont}}_{\mathrm{DDYO}}[u]\Bigr)_{j,k}.
\]

## Status

Computational verification is green.
The program remains formally open at the shell-product moment-control frontier.
No theorem-level closure is claimed here.
