# DDYO Counterexample: zero shell mean is not sufficient for cancellation

## Counterexample field

Let
\[
u(x,y,z)=(0,0,\sin x).
\]

Then
\[
\nabla\cdot u = 0,
\]
so \(u\) is incompressible.

Its strain tensor is
\[
S=\frac{\nabla u+(\nabla u)^{\mathsf T}}{2},
\]
with only nonzero entries
\[
S_{13}=S_{31}=\frac12\cos x.
\]

Its vorticity is
\[
\omega=\nabla\times u=(0,-\cos x,0).
\]

Both \(S_{13}\) and \(\omega_2\) are single-shell trigonometric modes with zero torus mean:
\[
\int_{\mathbb T^3} S_{13}\,dx=0,
\qquad
\int_{\mathbb T^3} \omega_2\,dx=0.
\]

However their same-shell pairing is nonzero:
\[
\int_{\mathbb T^3} S_{13}\,\omega_2\,dx
=
-\frac12\int_{\mathbb T^3}\cos^2 x\,dx
\neq 0.
\]

## Consequence

Zero shell mean alone does not force cancellation of same-shell pairings.

Therefore any Claim 5 route that uses only
\[
\int S_k=0,
\qquad
\int \omega_k=0
\]
without an additional dipole / Taylor / kernel cancellation mechanism is false.
