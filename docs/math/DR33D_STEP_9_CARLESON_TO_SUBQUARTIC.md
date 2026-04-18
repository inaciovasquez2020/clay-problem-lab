# DR33D Step 9 — Carleson-to-Subquartic Implication

## Objective
Formulate the precise implication from shell-weighted Carleson control to the subquartic bridge.

## Carleson input
Assume
\[
\mathfrak C_T(E)
:=
\sup_{I\subset[0,T]}
\frac{1}{|I|}
\sum_j \int_I 2^{-j}E_j(t)\,dt
\le C_T.
\]

## Target implication
Seek \(\theta\in(0,1)\) and \(C>0\) such that
\[
\mathfrak C_T(E)\le C_T
\Longrightarrow
\int_0^T\left(\sum_j 2^{-j}E_j(t)^{1/2}\right)^2dt
\le
C\int_0^T\sum_j E_j(t)^{1+\theta}\,dt.
\]

## Equivalent bridge form
It is enough to prove
\[
\mathfrak C_T(E)\le C_T
\Longrightarrow
\left(\sum_j 2^{-j}E_j(t)^{1/2}\right)^2
\le
C\sum_j E_j(t)^{1+\theta}
\quad\text{for a.e. }t.
\]

## Status
OPEN — implication not yet derived.
