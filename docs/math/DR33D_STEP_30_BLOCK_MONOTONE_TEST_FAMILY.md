# DR33D Step 30 — Block-Monotone Test Family Beyond the Geometric Case

## Test family

Let \(0<\theta<1\), \(j_0\in\mathbb Z\), \(L\in\mathbb N\), and \(a>0\). Define
\[
E^{(a,L)}_j:=
\begin{cases}
a,& j_0\le j\le j_0+L,\\
0,& \text{otherwise}.
\end{cases}
\]

Then
\[
E^{(a,L)}_{j+1}\le E^{(a,L)}_j
\qquad\text{for all }j,
\qquad
E^{(a,L)}_j=0\qquad\text{for all }j<j_0.
\]

## Invariant computation

Define
\[
A(a,L):=\sum_{j\in\mathbb Z}2^{-j}\left(E^{(a,L)}_j\right)^{1/2}.
\]
Then
\[
A(a,L)
=
a^{1/2}\sum_{j=j_0}^{j_0+L}2^{-j}
=
a^{1/2}2^{-j_0}\sum_{n=0}^{L}2^{-n},
\]
so
\[
A(a,L)^2
=
a\,2^{-2j_0}\left(\sum_{n=0}^{L}2^{-n}\right)^2.
\]

## Subquartic norm

Also
\[
S(a,L):=\sum_j\left(E^{(a,L)}_j\right)^{1+\theta}
=
(L+1)a^{1+\theta}.
\]

## Ratio

Hence
\[
\frac{A(a,L)^2}{S(a,L)}
=
2^{-2j_0}\frac{\left(\sum_{n=0}^{L}2^{-n}\right)^2}{L+1}\,a^{-\theta}.
\]

## Consequence

For each fixed \(L\),
\[
\frac{A(a,L)^2}{S(a,L)}\to\infty
\qquad(a\downarrow0).
\]

Therefore Step 25 fails for the block-monotone cutoff family if no further size normalization is imposed.

## Status

LOCKED COUNTEREXAMPLE — monotone cutoff alone does not imply Step 25.
