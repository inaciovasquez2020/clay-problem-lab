# Conditional: RA1n Ghat tail bound proof

## Target

Prove that there exist \(\varepsilon>0\) and \(C_\infty>0\) such that
\[
|\widehat G(\xi)| \le C_\infty (1+|\xi|)^{-3-\varepsilon}
\qquad\text{for } |\xi|\ge 1.
\]

## Role

This is the tail half of GoodBounds.

## Dependency

This proof must use the exact formula stated in `docs/math/RA1N_GHAT_FORMULA.md`.

## Truthfulness rule

Do not claim GoodBounds or \(L^1\)-integrable before this tail estimate is proved for the actual \(\widehat G\).
