# DR33D Step 25B — Monotone+Cutoff+Size Control

## Statement

Let \(0<\theta<1\). Given \(M>0\), determine whether there exists \(C=C(\theta,j_0,M)<\infty\) such that every nonnegative sequence \((E_j)\) satisfying
\[
E_{j+1}\le E_j,
\qquad
E_j=0\ \text{for }j<j_0,
\qquad
\sum_{j\in\mathbb Z}E_j^{1+\theta}\le M
\]
obeys
\[
\left(\sum_{j\in\mathbb Z}2^{-j}E_j^{1/2}\right)^2
\le
C\sum_{j\in\mathbb Z}E_j^{1+\theta}.
\]

## Candidate extra invariant

A uniform lower size bound
\[
\sum_{j\in\mathbb Z}E_j^{1+\theta}\ge m>0
\]
would remove the pure power-gap obstruction
\[
S^{1/(1+\theta)}\le m^{-\theta/(1+\theta)}S.
\]

## Status

SURVIVING OPEN FRONTIER — requires one extra size/control invariant beyond monotone cutoff.
