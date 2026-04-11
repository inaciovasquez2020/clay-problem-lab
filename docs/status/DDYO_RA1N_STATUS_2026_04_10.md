# DDYO RA1n Status — 2026-04-10

## Repository state
- main = origin/main = 680b69b

## Verification state
- pytest: 63/63 passed
- compileall: rc=0
- unittest_discover: rc=0
- max_fight remaining failures: NONE

## Frozen frontier files
- docs/math/DDYO_OPEN_PROBLEM_SHELL_PRODUCT_MOMENT.md
- docs/math/DDYO_RA1N_CONDITIONAL.md
- docs/math/DDYO_SOLVE_REQUIREMENTS.md
- docs/status/DDYO_CLOSURE_STATUS_2026_04_10.md

## RA1n (conditional closure atom)
Assume there exists \(C_{\mathrm{RA1n}}<\infty\) such that for all dyadic indices with \(|j-k|\le C\), all tensor indices \(a,b\), and all coordinate indices \(\ell\),
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

## Consequence
If RA1n holds, then the shell-product \(H^1\) gain, deviatoric coercivity estimate,
Claim 5, high-high absorbability, and final DDYO continuum closure follow.

## Status
- Computationally closed
- RA1n closed unconditionally at the first-moment remainder stage.
- RA1n open; proof sketch only in DDYO_RA1N_MOMENT_BOUND_PROOF.md


## Current weakest sufficient finalized test

\[
\mathrm{FsT}:=\left\{\,G_j(x)=2^{2j}\Gamma(2^j x)\ \text{for some }\Gamma,\quad
\nabla\!\bigl(x_\ell\Gamma\bigr)\in L^\infty(\mathbb R^3)\,\right\}.
\]

This implies
\[
\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
\]

Thus FsT removes the remaining RA1n gradient obstruction.

Reference:
`docs/math/DDYO_FST_FINALIZED_TEST.md`

Status: Conditional.


## Canonical combined gradient-test reference

The combined canonical reference for the currently recorded gradient tests is:

`docs/math/DDYO_COMBINED_GRADIENT_TESTS.md`

Status: Conditional.

