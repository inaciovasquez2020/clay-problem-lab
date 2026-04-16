# Conditional: Parabolic Window Gain Lemma

Let
\[
\mathcal A_\ell(t):=
2^{2\ell}
\left(
\int_{t-2^{-2\ell}}^{t} E_\ell(s)\,ds
\right)^{1/2},
\qquad
E_\ell(s):=\|u_\ell(s)\|_{L_x^2}^2.
\]

## Final missing object

A full closure of the current SiMSVE / DDYO route is reduced to the following single theorem-level input.

### Parabolic Window Gain Lemma
There exist constants \(\sigma>0\), \(\theta\in(0,1)\), \(C>0\) such that for every dyadic shell \(\ell\) and every time \(t\),
\[
\mathcal A_\ell(t)
\le
C\,2^{-\sigma\ell}
+
C\,2^{-\sigma\ell}
\Big(
\sup_{m\le \ell+O(1)} \mathcal A_m(t)
\Big)^\theta.
\]

If this holds, then the bootstrap closes and yields
\[
\mathcal A_\ell(t)\lesssim 2^{-\sigma_*\ell}
\]
for some \(\sigma_*>0\), uniformly in \(\ell,t\).

## Equivalent weakest sufficient DDYO form

It is enough to prove that the shellwise DDYO remainder \(R_\ell\) on
\[
I_\ell(t):=[t-2^{-2\ell},t]
\]
satisfies
\[
\|R_\ell\|_{L_t^2L_x^2(I_\ell(t)\times\mathbb R^3)}
\lesssim
2^{(2-\sigma)\ell}
\Big(
\sup_{m\le \ell+O(1)} \mathcal A_m(t)
\Big)^\theta
\]
for some \(\sigma>0\), \(\theta\in(0,1)\).

## Status

This lemma is the single canonical obstruction remaining in the current route.
No unconditional proof is claimed here.
