# DR33D Step 17 — Candidate Cross-Shell Interaction Invariant

## Objective
Introduce a concrete invariant encoding off-diagonal shell interaction.

## Definition
For a nonnegative shell profile \(E=(E_j)_j\), define
\[
\mathfrak I_{\mathrm{cross}}(E)
:=
\sum_{j\le k} 2^{-(j+k)}E_j^{1/2}E_k^{1/2}.
\]

## Exact identity
One has
\[
\left(\sum_j 2^{-j}E_j^{1/2}\right)^2
=
\sum_j 2^{-2j}E_j
+
2\sum_{j<k}2^{-(j+k)}E_j^{1/2}E_k^{1/2}.
\]

Hence
\[
\left(\sum_j 2^{-j}E_j^{1/2}\right)^2
\le
2\,\mathfrak I_{\mathrm{cross}}(E).
\]

## Required domination
The remaining task is to prove or refute the existence of \(\theta\in(0,1)\), \(C>0\) such that
\[
\mathfrak I_{\mathrm{cross}}(E)
\le
C\sum_j E_j^{1+\theta}.
\]

## Logical role
This is the first concrete realization candidate for the Step 16 axiom schema.

## Status
CANDIDATE INVARIANT — domination by subquartic shell sum remains open.
