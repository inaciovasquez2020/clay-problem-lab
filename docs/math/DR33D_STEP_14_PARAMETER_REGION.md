# DR33D Step 14 — Admissible Parameter Region

## Objective
Record the exact parameter inequalities required by the current candidate routes.

## Parameters
Let
\[
\alpha>0,\qquad \beta>0,\qquad \theta\in(0,1).
\]

## Candidate invariant route
The Step 8 candidate seeks
\[
\left(\sum_j 2^{-j}E_j(t)^{1/2}\right)^2
\le
C\sum_j 2^{-\beta j}E_j(t)^{1+\theta}.
\]

## Renormalized route
The Step 10 candidate seeks
\[
\left(\sum_j 2^{-j+\alpha j/2}F_j(t)^{1/2}\right)^2
\le
C\sum_j F_j(t)^{1+\theta},
\qquad
F_j(t):=2^{-\alpha j}E_j(t).
\]

## Pullback identity
Substituting \(F_j(t)=2^{-\alpha j}E_j(t)\) gives
\[
\sum_j F_j(t)^{1+\theta}
=
\sum_j 2^{-\alpha(1+\theta)j}E_j(t)^{1+\theta}.
\]

## Parameter identification
Hence the renormalized route matches the invariant route exactly when
\[
\beta=\alpha(1+\theta).
\]

## Hölder-side restriction
The Step 11 weighted Hölder prefactor is finite only if
\[
\alpha<2.
\]

## Admissible candidate region
The currently admissible parameter region is therefore
\[
\theta\in(0,1),\qquad
\alpha\in(0,2),\qquad
\beta=\alpha(1+\theta).
\]

## Status
LOCKED REGION — candidate parameter geometry only, not a proof.
