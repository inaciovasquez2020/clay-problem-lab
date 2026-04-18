# DR33D Step 29 — Exact Power-Gap Obstruction Lemma

## Statement

Let \(0<\theta<1\). Define
\[
S:=\sum_{j\in\mathbb Z}E_j^{1+\theta}.
\]
There does not exist a universal constant \(C=C(\theta,j_0)<\infty\) such that
\[
S^{1/(1+\theta)}\le C\,S
\]
for all nonnegative sequences \((E_j)\) with
\[
E_{j+1}\le E_j,\qquad E_j=0\ \text{for }j<j_0.
\]

## Counterexample family

Fix \(j_0\in\mathbb Z\). For \(a\in(0,1)\), define
\[
E^{(a)}_j:=
\begin{cases}
a,& j=j_0,\\
0,& j\neq j_0.
\end{cases}
\]
Then
\[
E^{(a)}_{j+1}\le E^{(a)}_j,
\qquad
E^{(a)}_j=0\ \text{for }j<j_0,
\]
and
\[
S(a)=a^{1+\theta}.
\]
Hence
\[
S(a)^{1/(1+\theta)}=a,
\qquad
\frac{S(a)^{1/(1+\theta)}}{S(a)}=a^{-\theta}\to\infty
\quad(a\downarrow0).
\]

## Consequence

The Step 28 bound
\[
A^2\le C(\theta,j_0)\,S^{1/(1+\theta)}
\]
cannot be upgraded to
\[
A^2\le C'(\theta,j_0)\,S
\]
by monotonicity plus lower-shell cutoff alone.

## Status

LOCKED OBSTRUCTION — Step 28 stops exactly at the power gap \(S^{1/(1+\theta)}\not\Rightarrow S\).
