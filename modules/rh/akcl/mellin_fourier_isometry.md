# Mellin–Fourier Isometry

## Logarithmic Change of Variables

Set
u = \log x

and
g(u) = e^{u/2} f(e^u).

## Transform Identity

Then
\[
M_f\!\left(\tfrac12+it\right)
=
\int_0^\infty f(x)x^{-1/2+it}\,dx
=
\int_{\mathbb R} g(u)e^{itu}\,du.
\]

Hence
\[
M_f\!\left(\tfrac12+it\right)
=
\widehat{g}(-t)
\]
up to Fourier normalization.

## Isometry

Therefore
\[
\int_{\mathbb R}\left|M_f\!\left(\tfrac12+it\right)\right|^2 dt
=
C \int_{\mathbb R}|g(u)|^2 du.
\]

Equivalently,
\[
\int_{\mathbb R}\left|M_f\!\left(\tfrac12+it\right)\right|^2 dt
=
C \int_0^\infty |f(x)|^2 dx.
\]

## Bandlimit Equivalence

If
\[
M_f\!\left(\tfrac12+it\right)=0
\quad\text{for }|t|>B,
\]
then
\[
\widehat{g}(\xi)=0
\quad\text{for }|\xi|>B.
\]

Thus
g is Fourier-bandlimited.

## Role

Mellin bandlimit
⇔
Fourier bandlimit in log-variable
⇒ exact Paley–Wiener transfer target.
