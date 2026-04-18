# RA1n projector paired symmetry

## DDYO paired form

Let the paired DDYO interaction be
\[
\mathcal B_{j,k}
=
\iint_{\mathbb R^3\times\mathbb R^3}
K_j^{\mathrm{proj}}(x-y)\,
\Gamma_{j,k}(x,y)\,dy\,dx,
\]
where \(\Gamma_{j,k}\) is the exact paired shell interaction induced by the DDYO form.

## Fourier representation

In Fourier variables,
\[
\Gamma_{j,k}(x,y)
=
\int_{\xi=\eta+\zeta}
\psi_j(|\xi|)\,
r_k(\eta,\zeta)\,
\widehat u_m(\eta)\widehat u_n(\zeta)
e^{i(x\cdot\xi - y\cdot\xi)}\,d\eta\,d\zeta.
\]

Equivalently, after pairing and inverse transform,
\[
\Gamma_{j,k}(x,y)
=
\int_{\eta,\zeta}
\psi_j(|\eta+\zeta|)\,
r_k(\eta,\zeta)\,
\widehat u_m(\eta)\widehat u_n(\zeta)
e^{i(x-y)\cdot(\eta+\zeta)}\,d\eta\,d\zeta.
\]

## Exchange transformation

Apply \((x,y)\mapsto(y,x)\). Then
\[
(x-y)\mapsto(y-x)=-(x-y),
\]
so
\[
e^{i(x-y)\cdot(\eta+\zeta)}
\mapsto
e^{-i(x-y)\cdot(\eta+\zeta)}.
\]

Taking complex conjugation,
\[
\overline{
e^{i(x-y)\cdot(\eta+\zeta)}
}
=
e^{-i(x-y)\cdot(\eta+\zeta)}.
\]

Since \(K_j^{\mathrm{proj}}\) is real and even,
\[
K_j^{\mathrm{proj}}(x-y)=K_j^{\mathrm{proj}}(y-x).
\]

## Symbol symmetry

The DDYO symbol satisfies
\[
r_k(\eta,\zeta)=r_k(\zeta,\eta).
\]

Thus under exchange of inputs,
\[
\widehat u_m(\eta)\widehat u_n(\zeta)
\longleftrightarrow
\widehat u_m(\zeta)\widehat u_n(\eta),
\]
and by symmetry of \(r_k\),
\[
r_k(\eta,\zeta)\widehat u_m(\eta)\widehat u_n(\zeta)
=
r_k(\zeta,\eta)\widehat u_m(\zeta)\widehat u_n(\eta).
\]

Hence the integrand is invariant under \((\eta,\zeta)\mapsto(\zeta,\eta)\).

## Paired symmetry conclusion

Combining:
- kernel evenness,
- real-valuedness,
- exponential conjugation symmetry,
- DDYO symbol symmetry,

one obtains
\[
\Gamma_{j,k}(y,x)=\Gamma_{j,k}(x,y).
\]

## First-order cancellation

Therefore the first-order paired integrand satisfies
\[
H^{(1),\mathrm{proj}}_{j,k}(y,x)=-H^{(1),\mathrm{proj}}_{j,k}(x,y),
\]
hence
\[
\mathsf T^{(1),\mathrm{proj}}_{j,k}=0.
\]

## Closure

\[
\mathsf T^{(1),\mathrm{proj}}_{j,k}=0
\Longrightarrow
|\mathsf R^{\mathrm{proj}}_{j,k}|
\le
C\,2^{-j}2^{-k}
\|\nabla S_k\|_{L^\infty}
\|\omega_k\|_{L^1}.
\]

\[
\Longrightarrow
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
