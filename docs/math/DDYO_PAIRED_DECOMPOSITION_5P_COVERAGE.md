# DDYO Paired Decomposition 5% Coverage

## Coverage tranche

This note decomposes the terminal paired lemma into five explicit subclaims covering the next structural 5% of the continuum closure.

## Terminal target

For \(|j-k|\le C\),
\[
\int \mathcal H'_\tau(\omega_j)\cdot [\widetilde P_j,S_k\!\cdot\nabla]\omega_k\,dx
=
\mathsf I^{\mathrm{sym}}_{j,k}+\mathsf R_{j,k},
\]
with
\[
\mathsf I^{\mathrm{sym}}_{j,k}
=
\int \Gamma_{j,k}(x):\operatorname{Sym}\nabla S_k(x)\,dx,
\qquad
|\mathsf R_{j,k}|
\le
C\,2^{-j}2^{-k}\,
\|\nabla S_k\|_{L^\infty}\,
\|\omega_k\|_{L^1}.
\]

## Five subclaims

### Claim 1: paired commutator expansion
Expand
\[
\int \mathcal H'_\tau(\omega_j)\cdot \widetilde P_j(S_k\!\cdot\nabla\omega_k)\,dx
-
\int \mathcal H'_\tau(\omega_j)\cdot S_k\!\cdot\nabla(\widetilde P_j\omega_k)\,dx
\]
into kernel form with \(K_j(x-y)\).

### Claim 2: symmetrization in \((x,y)\)
Rewrite the kernel pairing as a sum of terms symmetric and antisymmetric under
\[
(x,y)\leftrightarrow(y,x).
\]

### Claim 3: antisymmetric cancellation
Prove the antisymmetric contribution cancels exactly after pairing with
\[
\mathcal H'_\tau(\omega_j)=\frac{\omega_j}{\sqrt{|\omega_j|^2+\tau^2}}.
\]

### Claim 4: symmetric-gradient extraction
Show the remaining top-order term can be written as
\[
\mathsf I^{\mathrm{sym}}_{j,k}
=
\int \Gamma_{j,k}:\operatorname{Sym}\nabla S_k\,dx.
\]

### Claim 5: dyadic remainder gain
Prove the remainder satisfies
\[
|\mathsf R_{j,k}|
\le
C\,2^{-j}2^{-k}\,
\|\nabla S_k\|_{L^\infty}\,
\|\omega_k\|_{L^1},
\]
up to summable lower-order terms.

## Weakest sufficient outcome

Any proof of Claims 1--5 yields the paired decomposition lemma and advances the continuum DDYO closure by the next structural tranche.

## Status

This is a coverage document only.
It does not claim the paired decomposition lemma is proved.
