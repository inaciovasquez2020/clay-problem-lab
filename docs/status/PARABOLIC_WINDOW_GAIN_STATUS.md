# Parabolic Window Gain Status

## Classification
- Route: SiMSVE / DDYO
- Layer: terminal wall
- Type: coercivity / decay gain beyond critical scaling
- Status: OPEN
- Role: single canonical obstruction

## Canonical statement

Let
\[
\mathcal A_\ell(t):=
2^{2\ell}
\left(
\int_{t-2^{-2\ell}}^{t} E_\ell(s)\,ds
\right)^{1/2}.
\]

The remaining theorem-level object is:

\[
\mathcal A_\ell(t)
\le
C\,2^{-\sigma\ell}
+
C\,2^{-\sigma\ell}
\Big(
\sup_{m\le \ell+O(1)} \mathcal A_m(t)
\Big)^\theta
\]
for some \(\sigma>0\), \(\theta\in(0,1)\).

## Consequence if proved

If the Parabolic Window Gain Lemma is proved, then the present bootstrap route closes and yields dyadic window decay
\[
\mathcal A_\ell(t)\lesssim 2^{-\sigma_*\ell}.
\]

## Truthfulness lock

- All auxiliary objects have been reduced away in the current route.
- The parabolic window gain is the unique remaining theorem-level input.
- No full solve is claimed.
