# DR33D Step 26 — Monotone Geometric Test Family

## Test family

Let \(0<\theta<1\), \(j_0\in\mathbb Z\), and \(\alpha>0\). Define
\[
E_j^{(\alpha,j_0)}
:=
\begin{cases}
0,& j<j_0,\\
2^{-\alpha (j-j_0)},& j\ge j_0.
\end{cases}
\]
Then
\[
E_{j+1}^{(\alpha,j_0)}\le E_j^{(\alpha,j_0)}
\qquad\text{for all }j,
\]
and
\[
E_j^{(\alpha,j_0)}=0\qquad\text{for all }j<j_0.
\]

## Invariant computation

Set
\[
\mathfrak I\!\left(E^{(\alpha,j_0)}\right)
:=
\left(\sum_{j\in\mathbb Z}2^{-j}\left(E_j^{(\alpha,j_0)}\right)^{1/2}\right)^2.
\]
Then
\[
\sum_{j\in\mathbb Z}2^{-j}\left(E_j^{(\alpha,j_0)}\right)^{1/2}
=
2^{-j_0}\sum_{n\ge0}2^{-n}2^{-\alpha n/2}
=
\frac{2^{-j_0}}{1-2^{-(1+\alpha/2)}},
\]
hence
\[
\mathfrak I\!\left(E^{(\alpha,j_0)}\right)
=
\frac{2^{-2j_0}}{\left(1-2^{-(1+\alpha/2)}\right)^2}.
\]

## Subquartic norm computation

Also
\[
\sum_{j\in\mathbb Z}\left(E_j^{(\alpha,j_0)}\right)^{1+\theta}
=
\sum_{n\ge0}2^{-\alpha(1+\theta)n}
=
\frac{1}{1-2^{-\alpha(1+\theta)}}.
\]

## Ratio

Therefore
\[
R(\alpha,j_0,\theta)
:=
\frac{
\mathfrak I\!\left(E^{(\alpha,j_0)}\right)
}{
\sum_j \left(E_j^{(\alpha,j_0)}\right)^{1+\theta}
}
=
2^{-2j_0}
\frac{1-2^{-\alpha(1+\theta)}}{\left(1-2^{-(1+\alpha/2)}\right)^2}.
\]

## Consequence

For every fixed \(j_0\), \(\theta\), and \(\alpha>0\),
\[
R(\alpha,j_0,\theta)<\infty.
\]
Thus this monotone geometric family does not produce a counterexample to Step 25.

## Status

NEGATIVE TEST — standard geometric monotone cutoff family does not refute the Step 25 frontier.
