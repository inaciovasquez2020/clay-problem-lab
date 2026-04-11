# DDYO Counterexample: strain shell is not divergence-free

## Counterexample field

Let
\[
u(x,y,z)=(\sin y,\sin z,\sin x).
\]

Then
\[
\nabla\cdot u
=
\partial_x(\sin y)+\partial_y(\sin z)+\partial_z(\sin x)=0,
\]
so \(u\) is incompressible.

Define
\[
S=\frac{\nabla u+(\nabla u)^{\mathsf T}}{2}.
\]

For incompressible \(u\),
\[
\nabla\cdot S=\frac12 \Delta u.
\]

For this \(u\),
\[
\Delta u=(-\sin y,-\sin z,-\sin x),
\]
hence
\[
\nabla\cdot S
=
-\frac12(\sin y,\sin z,\sin x)\neq 0.
\]

## Consequence

This is an explicit counterexample to any route that attempts to obtain the second gain by assuming the strain field \(S_k\) is divergence-free.
