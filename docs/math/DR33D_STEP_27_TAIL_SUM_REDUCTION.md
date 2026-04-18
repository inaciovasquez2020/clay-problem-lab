# DR33D Step 27 — Tail-Sum Reduction Under Monotonicity

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

## Reduction

For \(j\ge j_0\),
\[
\sum_{m\le j}2^{-m}E_m^{1/2}
=
\sum_{n=0}^{j-j_0}2^{-(j-n)}E_{j-n}^{1/2}
\le
2^{-j}\sum_{n\ge0}2^{n}E_j^{1/2}
=
C\,2^{-j}E_j^{1/2},
\]
where monotonicity \(E_{j-n}\ge E_j\) is used.

Hence
\[
A
=
\sum_{j\ge j_0}2^{-j}E_j^{1/2}
\le
C\sup_{j\ge j_0}\left(2^{-j}E_j^{1/2}\right).
\]

## Consequence

Thus Step 25 reduces to bounding
\[
\sup_{j\ge j_0}\left(2^{-j}E_j^{1/2}\right)^2
\le
C\sum_j E_j^{1+\theta}.
\]

Equivalently,
\[
E_j \le C\,2^{2j}\sum_k E_k^{1+\theta}
\quad\text{uniformly in }j.
\]

## Logical role

This converts the global invariant into a pointwise tail-growth condition under monotonicity.

## Status

REDUCTION LOCK — Step 25 is equivalent to a uniform pointwise growth bound under monotone cutoff.
