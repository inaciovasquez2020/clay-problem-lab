# Conditional: RA1n Ghat local bound proof

## Target

Prove that there exist \(\alpha<3\) and \(C_0>0\) such that
\[
|\widehat G(\xi)| \le C_0 |\xi|^{-\alpha}
\qquad\text{for } |\xi|\le 1.
\]

## Role

This is the local half of GoodBounds.

## Dependency

This proof must use the exact formula stated in `docs/math/RA1N_GHAT_FORMULA.md`.

## Truthfulness rule

Do not claim GoodBounds or \(L^1\)-integrable before this local estimate is proved for the actual \(\widehat G\).
