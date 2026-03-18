# Admissible Class for AKCL

## Definition

Let
w(x) = e^{-x}.

Define the Mellin transform
M_f(s) = \int_0^\infty f(x) x^{s-1} dx.

Define the admissible class
\mathcal{A}_B
=
\left\{
f \in L^2((0,\infty),w(x)dx)
:
M_f\!\left(\tfrac12+it\right)=0 \text{ for } |t|>B
\right\}.

## Structural Consequence

Bounded Mellin support implies controlled oscillation scale.

## Target Upgrade

Prove:
\forall f \in \mathcal{A}_B,\quad
\sum_{x\in \mathrm{Tail}(L)} |f(x)|^2 w(x)
\le
\varepsilon_B(L)
\sum_{x\in \mathrm{Core}(L)} |f(x)|^2 w(x)

with
\varepsilon_B(L)\to 0.
