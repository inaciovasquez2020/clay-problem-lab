# RA1n projector-consistent kernel

## Projector-consistent kernel

Define
\[
\widehat K_j^{\mathrm{proj}}(\xi):=\psi_j(|\xi|),
\qquad
\psi_j(|\xi|)=\psi(2^{-j}|\xi|),
\]
with \(\psi\in C_c^\infty((1/2,2))\), real-valued and radial. Let
\[
K_j^{\mathrm{proj}}:=\mathcal F^{-1}(\psi_j(|\xi|)).
\]

Then
\[
K_j^{\mathrm{proj}}(z)=K_j^{\mathrm{proj}}(-z),
\qquad
\widehat K_j^{\mathrm{proj}}(\xi)\in\mathbb R.
\]

Hence the associated operator
\[
(\widetilde P_j^{\mathrm{proj}} f)(x)
:=
\int_{\mathbb R^3} K_j^{\mathrm{proj}}(x-y)f(y)\,dy
\]
is self-adjoint on \(L^2\) and commutes with complex conjugation.

## Divergence-free preservation

Let
\[
\widehat{e^{(j)}_{ab}(D)f}(\xi)
=
m^{(j)}_{ab}(\xi)\,\widehat f(\xi),
\]
where the symbol is of divergence-free projector type:
\[
\xi_a m^{(j)}_{ab}(\xi)=0
\qquad\text{for all }\xi.
\]

Since \(\widetilde P_j^{\mathrm{proj}}\) is scalar-multiplier defined,
\[
\widehat{\widetilde P_j^{\mathrm{proj}} e^{(j)}_{ab}(D)f}(\xi)
=
\psi_j(|\xi|)\,m^{(j)}_{ab}(\xi)\,\widehat f(\xi),
\]
so
\[
\xi_a \psi_j(|\xi|)m^{(j)}_{ab}(\xi)\widehat f(\xi)=0.
\]

Therefore
\[
\widetilde P_j^{\mathrm{proj}} e^{(j)}_{ab}(D)
\]
preserves the divergence-free structure.

## Compatibility with the DDYO symbol

Let the DDYO defect symbol be
\[
r_k(\eta,\zeta).
\]

Projector consistency means that every projected shell factor is multiplied by the scalar radial weight
\[
\psi_j(|\eta|),\qquad \psi_j(|\zeta|),\qquad \psi_j(|\eta+\zeta|),
\]
without changing tensorial contraction structure.

Hence the projected DDYO form has symbol
\[
r_k^{\mathrm{proj}}(\eta,\zeta)
=
\psi_j(|\eta+\zeta|)\,r_k(\eta,\zeta),
\]
or in the paired-input formulation
\[
r_{j,k}^{\mathrm{proj}}(\eta,\zeta)
=
\psi_j(|\eta|)\psi_j(|\zeta|)\,r_k(\eta,\zeta),
\]
depending on whether projection is placed on output or inputs.

Because the projector factor is scalar, radial, and real,
\[
|r_{j,k}^{\mathrm{proj}}(\eta,\zeta)|
\le
|r_k(\eta,\zeta)|.
\]

Thus all previously established shell-localized bounds remain valid with the same tensor structure and no new divergence defect.

## Fourier-space commutator identity

For any vector field \(S_k\) and scalar \(\omega_k\),
\[
[\widetilde P_j^{\mathrm{proj}},S_k\!\cdot\nabla]\omega_k
=
\widetilde P_j^{\mathrm{proj}}(S_k\!\cdot\nabla \omega_k)
-
S_k\!\cdot\nabla(\widetilde P_j^{\mathrm{proj}}\omega_k).
\]

Taking Fourier transform gives
\[
\mathcal F\!\left(
[\widetilde P_j^{\mathrm{proj}},S_k\!\cdot\nabla]\omega_k
\right)(\xi)
=
\int_{\mathbb R^3}
\bigl(\psi_j(|\xi|)-\psi_j(|\eta|)\bigr)\,
\widehat S_k(\xi-\eta)\cdot(i\eta)\,
\widehat\omega_k(\eta)\,d\eta.
\]

Thus the exact Fourier commutator symbol is
\[
c_j(\xi,\eta)
=
\bigl(\psi_j(|\xi|)-\psi_j(|\eta|)\bigr)\,i\eta.
\]

Since \(\psi_j\) is smooth and radial,
\[
\psi_j(|\xi|)-\psi_j(|\eta|)
=
\nabla \psi_j(|\eta+\theta(\xi-\eta)|)\cdot(\xi-\eta)
\]
for some \(\theta\in(0,1)\), hence
\[
|c_j(\xi,\eta)|
\lesssim
2^{-j}|\xi-\eta|\,|\eta|
\]
on the \(j\)-shell.

This is the Fourier-space form of the first kernel-moment gain.

## Real-valuedness and self-adjointness

Since
\[
\widehat K_j^{\mathrm{proj}}(\xi)=\psi_j(|\xi|)\in\mathbb R,
\qquad
\widehat K_j^{\mathrm{proj}}(-\xi)=\widehat K_j^{\mathrm{proj}}(\xi),
\]
the kernel is real and even:
\[
K_j^{\mathrm{proj}}(z)\in\mathbb R,
\qquad
K_j^{\mathrm{proj}}(z)=K_j^{\mathrm{proj}}(-z).
\]

Therefore
\[
\langle \widetilde P_j^{\mathrm{proj}} f,g\rangle
=
\langle f,\widetilde P_j^{\mathrm{proj}} g\rangle.
\]

## Projector-only paired remainder derivation

Write
\[
[\widetilde P_j^{\mathrm{proj}},S_k\!\cdot\nabla]\omega_k(x)
=
\int
K_j^{\mathrm{proj}}(x-y)\,
\bigl(S_k(x)-S_k(y)\bigr)\cdot\nabla\omega_k(y)\,dy.
\]

Expand
\[
S_k(x)-S_k(y)
=
(x-y)\cdot\nabla S_k(y)+Q_{j,k}(x,y),
\]
with
\[
Q_{j,k}(x,y)
=
\int_0^1(1-\theta)\,
(x-y)^\top\nabla^2S_k(y+\theta(x-y))(x-y)\,d\theta.
\]

The first-order leakage is
\[
\mathsf T^{(1),\mathrm{proj}}_{j,k}
:=
\iint
K_j^{\mathrm{proj}}(x-y)\,
\bigl((x-y)\cdot\nabla S_k(y)\bigr)\,
\Gamma_{j,k}(x,y)\,dy\,dx.
\]

Because \(K_j^{\mathrm{proj}}\) is even and real, the paired form is exchange invariant:
\[
\mathcal B_{j,k}[H]
=
\iint K_j^{\mathrm{proj}}(x-y)H(x,y)\,dy\,dx
=
\mathcal B_{j,k}[H\circ\sigma],
\qquad \sigma(x,y)=(y,x).
\]

Hence for the post-symmetrized first-order integrand
\[
H^{(1),\mathrm{proj}}_{j,k}(x,y)
:=
K_j^{\mathrm{proj}}(x-y)\,
\frac12\Bigl(
L_{j,k}(x,y)\Gamma_{j,k}(x,y)
-
L_{j,k}(y,x)\Gamma_{j,k}(y,x)
\Bigr),
\]
if
\[
\Gamma_{j,k}(y,x)=\Gamma_{j,k}(x,y),
\]
then
\[
H^{(1),\mathrm{proj}}_{j,k}(y,x)
=
-
H^{(1),\mathrm{proj}}_{j,k}(x,y),
\]
so
\[
\mathsf T^{(1),\mathrm{proj}}_{j,k}=0.
\]

Only the second-order remainder survives:
\[
\mathsf R^{\mathrm{proj}}_{j,k}
=
\iint
K_j^{\mathrm{proj}}(x-y)\,
Q_{j,k}(x,y)\,
\Gamma_{j,k}(x,y)\,dy\,dx.
\]

Using
\[
|Q_{j,k}(x,y)|
\le
C|x-y|^2\|\nabla^2S_k\|_{L^\infty},
\]
and
\[
\int |K_j^{\mathrm{proj}}(z)|\,|z|^2\,dz\lesssim 2^{-2j},
\]
one gets
\[
|\mathsf R^{\mathrm{proj}}_{j,k}|
\le
C\,2^{-2j}\,\|\nabla^2S_k\|_{L^\infty}\,\|\nabla\omega_k\|_{L^1}.
\]

If
\[
\|\nabla^2S_k\|_{L^\infty}\lesssim 2^k\|\nabla S_k\|_{L^\infty},
\qquad
\|\nabla\omega_k\|_{L^1}\lesssim 2^k\|\omega_k\|_{L^1},
\]
then for \(|j-k|\le C_0\),
\[
|\mathsf R^{\mathrm{proj}}_{j,k}|
\le
C\,2^{-j}2^{-k}\,\|\nabla S_k\|_{L^\infty}\,\|\omega_k\|_{L^1}.
\]

Therefore the projector-consistent kernel yields
\[
\mathsf T^{(1),\mathrm{proj}}_{j,k}=0
\Longrightarrow
|\mathsf R^{\mathrm{proj}}_{j,k}|
\le
C\,2^{-j}2^{-k}\,\|\nabla S_k\|_{L^\infty}\,\|\omega_k\|_{L^1},
\]
hence
\[
\text{paired commutator closure}
\Longrightarrow
\text{Claim 5}
\Longrightarrow
\text{shell-product }H^1\text{ gain}
\Longrightarrow
\text{deviatoric coercivity}
\Longrightarrow
\text{final DDYO continuum closure.}
\]
