# DDYO H-Prime Route Criterion

## Current truthful state

At the current continuum layer, the exact algebraic form of
\[
\mathcal H'(\omega_j)
\]
has not yet been frozen as a single explicit formula in the reduction chain.

Therefore the weakest sufficient next step is to declare the admissible \(\mathcal H\)-model and route criterion explicitly.

## Route criterion by algebraic form

### Case 1: \(L^1\)-type entropy
If
\[
\mathcal H(z)=|z|,
\qquad
\mathcal H'(z)=\frac{z}{|z|}
\quad \text{a.e. on } z\neq 0,
\]
then \(\mathcal H'\) is \(0\)-homogeneous and nonsmooth at \(z=0\).
The admissible closure route is pairing-level cancellation:
\[
\int \mathcal H'(\omega_j)\cdot
[\widetilde P_j,S_k\!\cdot\nabla]\omega_k\,dx.
\]
This is Route C.

### Case 2: regularized \(L^1\)-type entropy
If
\[
\mathcal H_\tau(z)=\sqrt{|z|^2+\tau^2},
\qquad
\mathcal H_\tau'(z)=\frac{z}{\sqrt{|z|^2+\tau^2}},
\]
then the derivative is smooth but still \(0\)-order in \(z\).
The admissible closure route remains pairing-level or mixed pairing/multiplier:
\[
\left|
\int \mathcal H_\tau'(\omega_j)\cdot
[\widetilde P_j,S_k\!\cdot\nabla]\omega_k\,dx
\right|.
\]
This is still Route C, with Route A auxiliary only.

### Case 3: quadratic energy
If
\[
\mathcal H(z)=\frac12 |z|^2,
\qquad
\mathcal H'(z)=z,
\]
then the pairing is linear in the shell variable and multiplier-level commutator analysis is admissible.
This opens Routes A/B.

## Weakest sufficient branch for DDYO

The DDYO critical residual is based on an \(L^1\)-type gradient/vorticity structure.
Therefore the natural continuum choice is
\[
\mathcal H(z)=|z|
\quad\text{or a smooth regularization}\quad
\mathcal H_\tau(z)=\sqrt{|z|^2+\tau^2}.
\]

Hence the mathematically admissible terminal branch is:

\[
\textbf{Route C (pairing-level cancellation) is primary.}
\]

## Terminal explicit target

Freeze
\[
\mathcal H_\tau(z)=\sqrt{|z|^2+\tau^2},
\qquad
\mathcal H_\tau'(z)=\frac{z}{\sqrt{|z|^2+\tau^2}},
\]
and prove
\[
\left|
\int \mathcal H_\tau'(\omega_j)\cdot
[\widetilde P_j,S_k\!\cdot\nabla]\omega_k\,dx
\right|
\le
C\,2^{-j}2^{-k}\,
\|\nabla S_k\|_{L^\infty}\,
\|\omega_k\|_{L^1},
\qquad |j-k|\le C,
\]
up to summable lower-order terms.

## Consequence

This freezes the correct algebraic branch and rules out pursuing the terminal gain as a purely absolute operator \(L^1\) bound in the non-quadratic DDYO state.
