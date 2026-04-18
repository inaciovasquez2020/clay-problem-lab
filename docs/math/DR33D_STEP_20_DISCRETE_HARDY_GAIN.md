# DR33D Step 20 — Discrete Hardy-Type Inequality with Exponent Gain

## Statement

Let \(0<\theta<1\). Define
\[
a_j:=E_j^{1/2},\qquad
H_j:=\sum_{m\le j}2^{-m}a_m.
\]
Seek constants \(C<\infty\) and \(\varepsilon>0\) such that
\[
\sum_j H_j^{\,2+\varepsilon}
\le
C\sum_j E_j^{1+\theta}.
\]
Equivalently, since \(a_j=E_j^{1/2}\),
\[
\sum_j \left(\sum_{m\le j}2^{-m}E_m^{1/2}\right)^{2+\varepsilon}
\le
C\sum_j E_j^{1+\theta}.
\]

## Logical role

This is a discrete Hardy-type exponent-gain route: if true with some \(\varepsilon>0\), then the cross-shell accumulation gains integrability beyond quadratic scale and becomes a candidate realization of the Step 16 subquartic bridge.

## Status

OPEN ROUTE — exponent gain beyond quadratic remains unproved.
