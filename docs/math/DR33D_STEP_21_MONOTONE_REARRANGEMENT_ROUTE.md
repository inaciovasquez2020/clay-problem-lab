# DR33D Step 21 — Monotone Rearrangement Structure on Shell Energies

## Statement

Let \(0<\theta<1\). Assume the shell sequence is nonincreasing:
\[
E_{j+1}\le E_j\qquad\text{for all }j.
\]
Define
\[
A:=\sum_j 2^{-j}E_j^{1/2}.
\]
Seek a constant \(C<\infty\) such that
\[
A^2
=
\left(\sum_j 2^{-j}E_j^{1/2}\right)^2
\le
C\sum_j E_j^{1+\theta}.
\]

## Rearrangement form

Under monotonicity, each tail satisfies
\[
\sum_{m\le j}2^{-m}E_m^{1/2}
\le
C_\theta\,E_j^{\theta/2}
\]
for a suitable dyadic summation constant \(C_\theta\), sufficient to imply
\[
\left(\sum_j 2^{-j}E_j^{1/2}\right)^2
\le
C\sum_j E_j^{1+\theta}.
\]

## Logical role

This enforces a monotone rearrangement structure converting cross-shell accumulation into a one-parameter tail regime.

## Status

OPEN ROUTE — the stated tail estimate under monotonicity remains unproved.
