# DDYO / RA1n Conditional Closure

## Canonical data

Assume
\[
|F_k(\xi)| \le M_F,
\qquad
r_k(\xi) = (1-P_k(\xi))\,\widehat G(\xi)\,\psi_k(\xi),
\qquad
\sup_{\xi\in\mathbb R^3}\sum_k |\psi_k(\xi)| < \infty .
\]

Define
\[
a_k := M_F \int_{S_k} |\widehat G(\xi)|\,|\psi_k(\xi)|\,d\xi .
\]

If
\[
\widehat G \in L^1(\mathbb R^3),
\]
then
\[
\left|\int_{\mathbb R^3} F_k(\xi)\,r_k(\xi)\,d\xi\right|
\le a_k
\]
and
\[
\sum_k a_k
\le
M_F \int_{\mathbb R^3} |\widehat G(\xi)|\Bigl(\sum_k |\psi_k(\xi)|\Bigr)\,d\xi
< \infty .
\]

## Conditional closure statement

Conditional.

RA1n is closed provided the actual canonical symbol \(\widehat G\) in the RA1n line satisfies
\[
\widehat G \in L^1(\mathbb R^3).
\]

No unconditional closure is claimed in this repository state.
