# DDYO Solve Requirements

## Missing parts to have a solve

### 1. Zeroth-moment shell-product identity
For all dyadic indices with \(|j-k|\le C\) and all tensor indices \(a,b\),
\[
\int G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx=0.
\]

### 2. First-moment shell-product control
For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
\[
\left|
\int x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
\right|
\le
C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
\]

### 3. Shell-product Hardy gain
For all dyadic indices with \(|j-k|\le C\) and all tensor indices \(a,b\),
\[
\bigl\|G_j\cdot e^{(j)}_{ab}(D)\omega_k\bigr\|_{H^1}
\le
C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
\]

### 4. Deviatoric coercivity / absorption
For all dyadic indices with \(|j-k|\le C\),
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

### 5. Claim 5 / paired remainder closure
For all dyadic indices with \(|j-k|\le C\),
\[
|\mathsf R_{j,k}|
\le
C\,2^{-j}2^{-k}\,
\|\nabla S_k\|_{L^\infty}\,
\|\omega_k\|_{L^1}.
\]

### 6. Final DDYO continuum closure
High-high absorbability closes, hence the DDYO continuum argument closes.

## Minimal dependency statement

The sole real missing object is Item 2, or any equivalent estimate strong enough to imply Item 4.

## Status

Computationally closed.
Formally open at the shell-product moment frontier.


## Current weakest sufficient test for the remaining gradient input

A currently recorded weakest sufficient finished-math input is the finalized
test FsT:

\[
\mathrm{FsT}:=\left\{\,G_j(x)=2^{2j}\Gamma(2^j x)\ \text{for some }\Gamma,\quad
\nabla\!\bigl(x_\ell\Gamma\bigr)\in L^\infty(\mathbb R^3)\,\right\}.
\]

This yields
\[
\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
\]
and therefore removes the remaining RA1n gradient obstruction.

Reference:
`docs/math/DDYO_FST_FINALIZED_TEST.md`

Status: Conditional.


## Canonical combined gradient-test reference

The combined canonical reference for the currently recorded gradient tests is:

`docs/math/DDYO_COMBINED_GRADIENT_TESTS.md`

Status: Conditional.

