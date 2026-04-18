# DR33D Step 23 — Minimal Unifying Invariant (Sharp Frontier Object)

## Statement

Let \(0<\theta<1\). Define the cross-shell quadratic form
\[
\mathfrak I(E)
:=
\left(\sum_j 2^{-j}E_j^{1/2}\right)^2.
\]

The DR33D closure reduces to proving existence of a constant \(C<\infty\) such that
\[
\boxed{
\mathfrak I(E)
\le
C\sum_j E_j^{1+\theta}.
}
\]

## Equivalences

The following are equivalent realizations:

1. Cross-shell form:
\[
\sum_{j\le k}2^{-(j+k)}E_j^{1/2}E_k^{1/2}
\le
C\sum_j E_j^{1+\theta}.
\]

2. Square form:
\[
\left(\sum_j 2^{-j}E_j^{1/2}\right)^2
\le
C\sum_j E_j^{1+\theta}.
\]

3. Invariant domination:
\[
\mathfrak I(E)\lesssim \|E\|_{\ell^{1+\theta}}^{1+\theta}.
\]

## Logical role

This isolates the unique minimal invariant whose domination yields:

\[
F_K \;\Longrightarrow\; \sum_j E_j^{1+\theta}
\]

and therefore closes the RA1n frontier.

## Status

FINAL WALL — no known inequality achieves this domination without additional structural assumptions.
