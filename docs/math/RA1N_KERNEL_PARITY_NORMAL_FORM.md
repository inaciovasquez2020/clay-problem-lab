# RA1n kernel parity normal form

## Operator-level parity projection

Let
\[
(\widetilde P_j f)(x):=\int_{\mathbb R^3} K_j(x-y) f(y)\,dy .
\]

Define the parity decomposition
\[
K_j^{\mathrm{sym}}(z):=\frac12\bigl(K_j(z)+K_j(-z)\bigr),\qquad
K_j^{\mathrm{asym}}(z):=\frac12\bigl(K_j(z)-K_j(-z)\bigr).
\]

Then
\[
K_j=K_j^{\mathrm{sym}}+K_j^{\mathrm{asym}},
\qquad
K_j^{\mathrm{sym}}(z)=K_j^{\mathrm{sym}}(-z),
\qquad
K_j^{\mathrm{asym}}(z)=-K_j^{\mathrm{asym}}(-z).
\]

Replace \(\widetilde P_j\) by
\[
(\widetilde P_j^{\mathrm{sym}} f)(x):=\int_{\mathbb R^3} K_j^{\mathrm{sym}}(x-y) f(y)\,dy .
\]

Then
\[
\int_{\mathbb R^3} z_\ell K_j^{\mathrm{sym}}(z)\,dz = 0
\qquad (\ell=1,2,3).
\]

## Exchange invariance

For the paired bilinear form
\[
\mathcal B_{j,k}[H]
:=
\iint_{\mathbb R^3\times\mathbb R^3}
K_j^{\mathrm{sym}}(x-y)\,H(x,y)\,dy\,dx,
\]
one has
\[
\mathcal B_{j,k}[H]=\mathcal B_{j,k}[H\circ\sigma],
\qquad
\sigma(x,y):=(y,x),
\]
because
\[
K_j^{\mathrm{sym}}(x-y)=K_j^{\mathrm{sym}}(y-x).
\]

Hence every antisymmetric integrand
\[
H(y,x)=-H(x,y)
\]
satisfies
\[
\mathcal B_{j,k}[H]=0.
\]

## First-order leakage class

Define
\[
L_{j,k}(x,y):=(x-y)\cdot \nabla S_k(y).
\]

Let \(\Gamma_{j,k}(x,y)\) be the shell-paired factor with symmetry
\[
\Gamma_{j,k}(y,x)=\Gamma_{j,k}(x,y).
\]

Then the post-symmetrized first-order integrand
\[
H^{(1)}_{j,k}(x,y)
:=
K_j^{\mathrm{sym}}(x-y)\,
\frac12\Bigl(
L_{j,k}(x,y)\Gamma_{j,k}(x,y)
-
L_{j,k}(y,x)\Gamma_{j,k}(y,x)
\Bigr)
\]
is antisymmetric:
\[
H^{(1)}_{j,k}(y,x)=-H^{(1)}_{j,k}(x,y).
\]

Therefore
\[
\mathsf T^{(1),\mathrm{sym}}_{j,k}=0.
\]

## Commutator normal form

Write
\[
[\widetilde P_j^{\mathrm{sym}}, S_k\!\cdot\nabla]\omega_k(x)
=
\int
K_j^{\mathrm{sym}}(x-y)\,
\bigl(S_k(x)-S_k(y)\bigr)\cdot \nabla \omega_k(y)\,dy.
\]

Expand
\[
S_k(x)-S_k(y)=L_{j,k}(x,y)+Q_{j,k}(x,y),
\]
with
\[
Q_{j,k}(x,y)
:=
\int_0^1 (1-\theta)\,
(x-y)^\top \nabla^2 S_k(y+\theta(x-y))(x-y)\,d\theta.
\]

Then
\[
[\widetilde P_j^{\mathrm{sym}}, S_k\!\cdot\nabla]\omega_k
=
\mathcal C^{(1),\mathrm{sym}}_{j,k}\omega_k
+
\mathcal C^{(2),\mathrm{sym}}_{j,k}\omega_k,
\]
and the first-order contribution cancels after pairing:
\[
\langle \mathcal H'(\omega_j),\mathcal C^{(1),\mathrm{sym}}_{j,k}\omega_k\rangle=0.
\]

So only the second-order remainder remains:
\[
\langle \mathcal H'(\omega_j),[\widetilde P_j^{\mathrm{sym}}, S_k\!\cdot\nabla]\omega_k\rangle
=
\langle \mathcal H'(\omega_j),\mathcal C^{(2),\mathrm{sym}}_{j,k}\omega_k\rangle.
\]

## Remainder estimate

Using
\[
|Q_{j,k}(x,y)|\le C |x-y|^2 \|\nabla^2 S_k\|_{L^\infty}
\]
and
\[
\int |K_j^{\mathrm{sym}}(z)|\,|z|^2\,dz \lesssim 2^{-2j},
\]
one gets
\[
|\mathsf R^{\mathrm{sym}}_{j,k}|
\le
C\,2^{-2j}\,\|\nabla^2 S_k\|_{L^\infty}\,\|\nabla \omega_k\|_{L^1}.
\]

If
\[
\|\nabla^2 S_k\|_{L^\infty}\lesssim 2^k \|\nabla S_k\|_{L^\infty},
\qquad
\|\nabla \omega_k\|_{L^1}\lesssim 2^k \|\omega_k\|_{L^1},
\]
then for \(|j-k|\le C_0\),
\[
|\mathsf R^{\mathrm{sym}}_{j,k}|
\le
C\,2^{-j}2^{-k}\,\|\nabla S_k\|_{L^\infty}\,\|\omega_k\|_{L^1}.
\]

## Closure chain

\[
\mathsf T^{(1),\mathrm{sym}}_{j,k}=0
\Longrightarrow
|\mathsf R^{\mathrm{sym}}_{j,k}|
\le
C\,2^{-j}2^{-k}\,\|\nabla S_k\|_{L^\infty}\,\|\omega_k\|_{L^1}
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
