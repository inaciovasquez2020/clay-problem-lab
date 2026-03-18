# Mellin Paley-Wiener Step

## Conditional Statement

Assume
f \in \mathcal A_B.

Set
g(u) = f(e^u)e^{u/2}.

Then
\widehat{g}(t) = M_f\!\left(\tfrac12+it\right)
vanishes for |t| > B.

## Consequence

g is Fourier-bandlimited to [-B,B].

## Target Bound

For every \sigma > 0,
there exists C_\sigma(B) such that
|g(u+iv)| \le C_\sigma(B) e^{B|v|}
for all |v| < \sigma.

## Pullback Form

|f(e^u)| \le C_\sigma(B) e^{-u/2} e^{B|v|}.

## Required Upgrade

Choose v = \sigma and transfer back to x = e^u
to obtain exponential tail decay in u.
