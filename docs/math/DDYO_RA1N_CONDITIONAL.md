# DDYO RA1n (Conditional)

## Name
RA1n = Rigidity Atom 1n

## Conditional statement

Assume there exists a constant \(C_{\mathrm{RA1n}}<\infty\) such that for all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
\[
\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0,
\]
and
\[
\left|
\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
\right|
\le
C_{\mathrm{RA1n}}\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
\]

## Consequences

RA1n implies the shell-product \(H^1\) gain
\[
\bigl\|\,G_j\cdot e^{(j)}_{ab}(D)\omega_k\,\bigr\|_{H^1}
\le
C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
\]

Hence RA1n implies the deviatoric coercivity estimate
\[
\left|
\int G_j\cdot
\Bigl(\sum_{a,b}\partial_b S_k^a\,e^{(j)}_{ab}(D)\omega_k\Bigr)\,dx
\right|
\le
C\,2^{-j}2^{-k}\,
\|\nabla S_k\|_{L^\infty}\,
\|\omega_k\|_{L^1}.
\]

Hence RA1n implies Claim 5 / paired remainder closure
\[
|\mathsf R_{j,k}|
\le
C\,2^{-j}2^{-k}\,
\|\nabla S_k\|_{L^\infty}\,
\|\omega_k\|_{L^1}.
\]

Hence RA1n implies high-high absorbability closure and final DDYO continuum closure.

## Status

Conditional new mathematics.
No proof is claimed in this repository.
