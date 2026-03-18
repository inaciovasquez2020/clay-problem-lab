# Mellin Strip Width

## Conditional Input

Assume
f \in \mathcal A_B

and
g(u)=f(e^u)e^{u/2}
has Fourier support in [-B,B].

## Paley-Wiener Upgrade

Then for every finite B,
g extends to an entire function of exponential type B.

## Strip Bound

For every \sigma > 0,
there exists C(B,\sigma) such that
|g(u+iv)| \le C(B,\sigma)e^{B|v|}
for all |v| \le \sigma.

## Pullback

Since
f(e^u)=e^{-u/2}g(u),

we obtain
|f(e^u e^{iv})| \le C(B,\sigma)e^{-u/2}e^{B|v|}.

## Target Constant

Define
\sigma(B) = 1

as the first fixed admissible strip width.

## Use

\sigma(B) > 0 supplies the contour-shift parameter needed for tail decay.
