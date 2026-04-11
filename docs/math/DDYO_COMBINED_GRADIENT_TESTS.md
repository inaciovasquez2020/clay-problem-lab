# DDYO Combined Gradient Tests

## Status

Conditional.

## Combined tests

### Test 1: weakest sufficient finished-math input

Reference:
`docs/math/DDYO_GJ_FINISHED_MATH_INPUT.md`

\[
G_j(x)=2^{2j}\Gamma(2^j x),
\qquad
\nabla\!\bigl(x_\ell\Gamma\bigr)\in L^\infty(\mathbb R^3).
\]

Consequence:
\[
\|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
\]

### Test 2: finalized test FsT

Reference:
`docs/math/DDYO_FST_FINALIZED_TEST.md`

\[
\mathrm{FsT}:=\left\{\,G_j(x)=2^{2j}\Gamma(2^j x)\ \text{for some }\Gamma,\quad
\nabla\!\bigl(x_\ell\Gamma\bigr)\in L^\infty(\mathbb R^3)\,\right\}.
\]

Consequence:
\[
\mathrm{FsT}\Longrightarrow \|\nabla(x_\ell G_j)\|_{L^\infty}\le C\,2^{-j}.
\]

## Consolidated conclusion

Both recorded tests reduce to the same sufficient structural input:
\[
G_j(x)=2^{2j}\Gamma(2^j x),
\qquad
\nabla\!\bigl(x_\ell\Gamma\bigr)\in L^\infty(\mathbb R^3).
\]

Hence both remove the remaining RA1n gradient obstruction.

## Final state

Conditional.
