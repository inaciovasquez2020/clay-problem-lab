# DR33D Step 27 — Tail-Sum Reduction Under Monotonicity (Corrected)

## Statement

Let \(0<\theta<1\). Assume
\[
E_{j+1}\le E_j \quad\text{for all }j,
\qquad
E_j=0 \quad\text{for all }j<j_0.
\]

Define
\[
S:=\sum_{j\in\mathbb Z}E_j^{1+\theta},\qquad
A:=\sum_{j\in\mathbb Z}2^{-j}E_j^{1/2}.
\]

## Exact tail identity

For \(j\ge j_0\),
\[
\sum_{m\le j}2^{-m}E_m^{1/2}
=
2^{-j}\sum_{n=0}^{j-j_0}2^{n}E_{j-n}^{1/2}.
\]

Under monotonicity \(E_{j-n}\ge E_j\),
\[
\sum_{m\le j}2^{-m}E_m^{1/2}
\ge
2^{-j}E_j^{1/2}\sum_{n=0}^{j-j_0}2^{n}
\asymp
E_j^{1/2}.
\]

## Consequence

The previously claimed upper bound
\[
\sum_{m\le j}2^{-m}E_m^{1/2}\le C\,2^{-j}E_j^{1/2}
\]
does not follow from monotonicity.

## Replacement reduction

For
\[
q=2(1+\theta),\qquad p=\frac{q}{q-1},
\]
one has
\[
A
=
\sum_{j\ge j_0}2^{-j}E_j^{1/2}
\le
\left(\sum_{j\ge j_0}2^{-pj}\right)^{1/p}
\left(\sum_{j\ge j_0}E_j^{q/2}\right)^{1/q}.
\]

## Logical role

This corrects the Step 27 reduction and replaces the invalid pointwise reduction by a valid weighted Hölder bound.

## Status

CORRECTED REDUCTION — prior pointwise reduction invalid; replaced by Hölder-based bound.
