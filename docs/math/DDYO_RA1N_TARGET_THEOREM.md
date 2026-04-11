# DDYO RA1n Target Theorem

## Exact target

For all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
\[
\left|
\int_{\mathbb R^3} x_\ell\,G_j(x)\,e^{(j)}_{ab}(D)\omega_k(x)\,dx
\right|
\le
C\,2^{-j}2^{-k}\,\|\omega_k\|_{L^1}.
\]

## Role

This is Item 2 in `docs/math/DDYO_SOLVE_REQUIREMENTS.md`.

If proved together with the zeroth-moment identity, it yields the shell-product \(H^1\) gain, the deviatoric coercivity estimate, Claim 5 / paired remainder closure, and final DDYO continuum closure.

## Status

Closed at the annular first-moment remainder stage.
A theorem-level first-moment remainder proof is now recorded in this repository.


## Weakest sufficient finalized test

The weakest sufficient finalized test currently recorded for the remaining
gradient obstruction is:

\[
\mathrm{FsT}:=\left\{\,G_j(x)=2^{2j}\Gamma(2^j x)\ \text{for some }\Gamma,\quad
\nabla\!\bigl(x_\ell\Gamma\bigr)\in L^\infty(\mathbb R^3)\,\right\}.
\]

Under FsT one obtains
\[
\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j},
\]
which removes the remaining RA1n gradient obstruction.

Reference:
`docs/math/DDYO_FST_FINALIZED_TEST.md`

Status: Conditional.


## Canonical combined gradient-test reference

The combined canonical reference for the currently recorded gradient tests is:

`docs/math/DDYO_COMBINED_GRADIENT_TESTS.md`

Status: Conditional.

