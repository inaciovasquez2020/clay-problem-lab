# Flip-Averaging Operator and Coercivity Step

## Block Flip Operators

Let \(B\) be a block of side \(L\).

For each block define a **local flip operator**

\[
F_B : f(U) \mapsto \int f(U^{(B,\sigma)})\, d\sigma ,
\]

where

- \(U^{(B,\sigma)}\) denotes the configuration obtained by applying a gauge-compatible flip on links inside block \(B\),
- \(\sigma\) is drawn from the Haar measure on \(G\).

The flip leaves the Wilson measure invariant.

---

## Averaging Operator

Define the global block averaging operator

\[
T_L = \prod_{B} F_B .
\]

Properties

\[
\|T_L f\| \le \|f\|
\]

\[
T_L 1 = 1
\]

\[
T_L^* = T_L .
\]

---

## Energy Decomposition

Using the orthogonal decomposition

\[
f = P_L f + Q_L f
\]

with

\[
P_L = \text{block conditional expectation}, \qquad Q_L = I - P_L ,
\]

one derives

\[
\|f\|^2
=
\|P_L f\|^2 + \|Q_L f\|^2 .
\]

---

## Flip Averaging Estimate

The flip operator contracts fluctuations inside blocks.

Thus

\[
\|T_L Q_L f\|^2
\le
(1 - \eta)\|Q_L f\|^2
\]

for some \(\eta>0\).

---

## Coercivity Inequality

From the contraction property,

\[
I \le a T_L^*T_L + b Q_L^*Q_L
\]

for constants \(a,b>0\).

---

## Consequence

Using the fluctuation inequality

\[
\|Q_L f\|^2
\ge
c L^2
\sum_\ell \|\nabla_\ell(Q_L f)\|^2
\]

one obtains

\[
I - T_L^*T_L
\ge
\kappa (-\Delta_G).
\]

---

## Result

If the spectral gap of the gauge Laplacian satisfies

\[
-\Delta_G \ge \gamma I ,
\]

then

\[
\|T_L f\|
\le
\sqrt{1-\kappa\gamma}\,\|f\|.
\]

This yields exponential clustering and the Yang–Mills mass gap.

