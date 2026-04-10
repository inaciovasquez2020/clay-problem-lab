# DDYO Second Gain Route

## Structural elimination

For incompressible \(u\),
\[
S := \frac{\nabla u + (\nabla u)^{\mathsf T}}{2}
\]
satisfies
\[
\nabla \cdot S
=
\frac12 \Delta u,
\]
hence, in general,
\[
\nabla \cdot S \neq 0.
\]

Therefore the second effective dyadic gain cannot be obtained from a divergence-free strain-shell identity.

## Weakest admissible replacement

The remaining \(2^{-k}\) gain must be extracted from one of the following equivalent shellwise mechanisms:

### Route A: pairing-level almost-orthogonality
Prove directly
\[
\left|
\int \mathcal H'(\omega_j)\cdot
[\widetilde P_j,S_k\!\cdot\nabla]\omega_k\,dx
\right|
\le
C\,2^{-j}2^{-k}\,
\|\nabla S_k\|_{L^\infty}\,
\|\omega_k\|_{L^1}\,
\|\mathcal H'(\omega_j)\|_{L^\infty},
\qquad |j-k|\le C.
\]

### Route B: double-commutator factorization
Prove a representation
\[
[\widetilde P_j,S_k\!\cdot\nabla]\omega_k
=
\sum_{|j-k|\le C}
[\widetilde P_j,[Q_k,S_k]]\,\nabla\omega_k
+
\text{lower-order},
\]
with
\[
\|[\widetilde P_j,[Q_k,S_k]]g\|_{L^1}
\le
C\,2^{-j}2^{-k}\,
\|\nabla S_k\|_{L^\infty}\,
\|g\|_{L^1}.
\]

### Route C: first-order cancellation in the paired trace
Using
\[
S_k(x)-S_k(y)
=
(x-y)\cdot \int_0^1 \nabla S_k(y+\theta(x-y))\,d\theta,
\]
prove that the first-order contribution vanishes after pairing with \(\mathcal H'(\omega_j)\), leaving only a remainder with net gain
\[
2^{-j}2^{-k}.
\]

## Consequence

Any one of Routes A--C is sufficient to close
\[
\sum_j 2^{2j}\!\int \mathcal H'(\omega_j)\cdot
[\widetilde P_j,S_{\sim j}\!\cdot\nabla]\omega_{\sim j}\,dx
\]
with one global \(\varepsilon<1\).

## Status

The incompressibility branch is closed off.
The remaining frontier is a pairing-level or multiplier-level second-order cancellation.
