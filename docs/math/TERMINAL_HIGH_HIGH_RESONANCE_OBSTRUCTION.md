# Conditional: Terminal High-High Resonance Obstruction

Let
\[
\mathcal A_\ell(t):=
2^{2\ell}
\left(
\int_{t-2^{-2\ell}}^{t} \|u_\ell(s)\|_{L_x^2}^2\,ds
\right)^{1/2},
\qquad
I_\ell(t):=[t-2^{-2\ell},t].
\]

## Canonical terminal object

The remaining theorem-level object is the estimate:
\[
\sum_{m:\,|m-\ell|\le C}
\Big\|
P_\ell \mathbb P\big((u_m\cdot\nabla)u_{m+O(1)}\big)
\Big\|_{L_t^2L_x^2(I_\ell(t)\times\mathbb R^3)}
\le
C\,2^{(2-\sigma)\ell}
\Big(
\sup_{k\le \ell+O(1)}\mathcal A_k(t)
\Big)^\theta
\]
for some \(\sigma>0\), \(\theta\in(0,1)\).

## Coherent transverse model

There exist divergence-free wave packets with transverse interaction
\[
\sin\angle(\eta,\zeta)\sim 1
\]
such that
\[
\Big\|
P_\ell \mathbb P\big((u_m\cdot\nabla)u_{m'}\big)
\Big\|_{L_t^2L_x^2(I_\ell(t))}
\gtrsim
2^{-\frac32\ell}\mathcal A_\ell(t)^2.
\]

Thus no sublinear exponent \(\theta<1\) is obtained from size estimates alone.

## Interpretation

The obstruction is a transverse high-high resonance that survives:
- Leray projection
- divergence-free constraints
- angular non-degeneracy

## Status

Single canonical obstruction.
No unconditional proof of the required inequality is known in this route.
