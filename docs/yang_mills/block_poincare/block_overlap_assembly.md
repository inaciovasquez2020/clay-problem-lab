# Block Overlap Assembly and Global Fluctuation Inequality

## Block Cover

Partition the lattice into cubic blocks \(B_i\) of side \(L\).

Each link belongs to at most \(K(d)\) blocks, where \(K(d)\) depends only on dimension.

---

## Block Poincaré Inequality

For each block \(B_i\):

\[
\operatorname{Var}_{\mu_{B_i}}(g)
\le
C L^2
\sum_{\ell\subset B_i}
\|\nabla_\ell g\|^2 .
\]

---

## Fluctuation Projection

Define

\[
P_L f = \text{conditional expectation onto block-constant functions}
\]

\[
Q_L = I - P_L .
\]

Properties

\[
P_L^2 = P_L
\]

\[
Q_L^2 = Q_L
\]

\[
P_L Q_L = 0 .
\]

---

## Local Application

Apply the block inequality to

\[
g = Q_L f
\]

inside each block.

\[
\|Q_L f\|_{L^2(B_i)}^2
\le
C L^2
\sum_{\ell\subset B_i}
\|\nabla_\ell(Q_L f)\|^2 .
\]

---

## Global Summation

Sum over all blocks.

Because each link appears in at most \(K(d)\) blocks,

\[
\sum_i \sum_{\ell\subset B_i}
\|\nabla_\ell(Q_L f)\|^2
\le
K(d)
\sum_\ell
\|\nabla_\ell(Q_L f)\|^2 .
\]

Thus

\[
\|Q_L f\|^2
\le
C' L^2
\sum_\ell
\|\nabla_\ell(Q_L f)\|^2 .
\]

Rearranging

\[
\|Q_L f\|^2
\ge
c L^2
\sum_\ell
\|\nabla_\ell(Q_L f)\|^2 .
\]

---

## Result

Global fluctuation inequality established once the block Poincaré inequality holds.

