# Weighted Mellin Transfer Gap

## Exact Remaining Lemma

Let
g(u)=e^{u/2}f(e^u).

Assume
\[
f \in L^2((0,\infty),e^{-x}dx)
\]
and
\[
M_f\!\left(\tfrac12+it\right)=0
\quad\text{for } |t|>B.
\]

Then the required statement is:

\[
\widehat{g}(\xi)=0
\quad\text{for } |\xi|>B
\]
together with a norm comparison
\[
\|g\|_{L^2(\mathbb R)} \le C \|f\|_{L^2((0,\infty),e^{-x}dx)}.
\]

## Obstruction

The logarithmic pullback gives
\[
\|g\|_{L^2(\mathbb R)}^2
=
\int_0^\infty |f(x)|^2 dx,
\]
not
\[
\int_0^\infty |f(x)|^2 e^{-x}dx.
\]

## Required Upgrade

Prove a weighted embedding:
\[
\int_0^\infty |f(x)|^2 dx
\le
C_B
\int_0^\infty |f(x)|^2 e^{-x}dx
\]
for the admissible Mellin-bandlimited class.

## Consequence

Weighted embedding
⇒ exact Mellin–Fourier transfer
⇒ Paley–Wiener
⇒ contour shift
⇒ AKCL closure.
