# Axial Gauge Fixing on a Finite Block

## Block

Let \(B \subset \mathbb{Z}^d\) be a cube of side \(L\).

Edges inside the block are \(E(B)\).
Vertices are \(V(B)\).

Gauge group:
\[
G = SU(N)
\]

Configuration space:
\[
\Omega_B = G^{E(B)} .
\]

Boundary links are fixed.

---

## Gauge Transformations

For \(h : V(B) \to G\),

\[
(U_\ell) \mapsto (h_x U_\ell h_y^{-1})
\]

for link \(\ell = (x,y)\).

---

## Axial Gauge Choice

Fix a spanning tree \(T_B \subset E(B)\).

For all \(\ell \in T_B\),

\[
U_\ell = I .
\]

Remaining degrees of freedom lie on

\[
E(B) \setminus T_B .
\]

Number of remaining variables:

\[
|E(B)| - |V(B)| + 1
\]

which equals the number of independent plaquette cycles.

---

## Gauge-Fixed Measure

The Wilson action on the block is

\[
S_B(U)
=
-\beta \sum_{p \subset B} \mathrm{Re}\,\mathrm{Tr}(U_p).
\]

After axial gauge fixing,

\[
d\mu_B(U)
=
Z_B^{-1}
\exp(-S_B(U))
\, dU .
\]

Integration is only over edges in \(E(B)\setminus T_B\).

---

## Key Property

The Dirichlet form

\[
\sum_{\ell\subset B} \|\nabla_\ell g\|^2
\]

is invariant under gauge transformations.

Thus spectral gap estimates for the gauge-fixed generator transfer to gauge-invariant observables.

---

## Next Target

Prove convexity / spectral-gap estimate for the gauge-fixed potential \(S_B(U)\).

