# DR33D Step 24 — Failure on Arbitrary \(\ell^{1+\theta}\) without Lower-Shell Cutoff

## Statement

Let \(0<\theta<1\). There does not exist a universal constant \(C<\infty\) such that
\[
\left(\sum_{j\in\mathbb Z} 2^{-j}E_j^{1/2}\right)^2
\le
C\sum_{j\in\mathbb Z} E_j^{1+\theta}
\]
for all nonnegative sequences \(E=(E_j)_{j\in\mathbb Z}\in \ell^{1+\theta}(\mathbb Z)\).

## Counterexample

For each \(N\in\mathbb N\), define
\[
E^{(N)}_j :=
\begin{cases}
1,& j=-N,\\
0,& j\neq -N.
\end{cases}
\]
Then
\[
E^{(N)}\in \ell^{1+\theta}(\mathbb Z),
\qquad
\sum_j \left(E^{(N)}_j\right)^{1+\theta}=1,
\]
but
\[
\left(\sum_j 2^{-j}\left(E^{(N)}_j\right)^{1/2}\right)^2
=
\left(2^{N}\right)^2
=
2^{2N}.
\]
Hence the ratio
\[
\frac{\left(\sum_j 2^{-j}\left(E^{(N)}_j\right)^{1/2}\right)^2}
{\sum_j \left(E^{(N)}_j\right)^{1+\theta}}
=
2^{2N}
\to \infty
\qquad (N\to\infty).
\]
Therefore no universal \(C\) can exist.

## Consequence

Any realization of the Step 23 domination
\[
\mathfrak I(E)
=
\left(\sum_j 2^{-j}E_j^{1/2}\right)^2
\le
C\sum_j E_j^{1+\theta}
\]
requires at least one additional structural hypothesis.

## Minimal surviving hypothesis

A lower-shell cutoff
\[
E_j=0\qquad\text{for all }j<j_0
\]
is sufficient to eliminate this obstruction.

## Status

LOCKED IMPOSSIBILITY — Step 23 fails on arbitrary \(\ell^{1+\theta}\) without added structure.
