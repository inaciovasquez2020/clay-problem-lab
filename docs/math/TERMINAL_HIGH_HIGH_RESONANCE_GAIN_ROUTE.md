# Conditional: Terminal High-High Resonance Gain Route

## Status
OPEN.

## Frontier object
Construct a renormalized symbol \(r_k(\xi,\eta)\) for the transverse high-high interaction and prove a curvature-driven gain estimate sufficient to close the DDYO route.

## Dyadic interaction functional
For each cutoff \(K\),
\[
\mathcal R_K(t)
:=
\sum_{\ell\le K}
2^\ell
\sum_{|m-\ell|\le C}
\int_{\mathbb R^3}
|u_\ell(x,t)|\,|u_m(x,t)|\,|\nabla u_{\max\{\ell,m\}}(x,t)|
\,dx.
\]

## Target inequality
There exist constants \(C_0>0\) and \(\theta\in(0,1)\) such that
\[
\mathcal R_K(t)
\le
C_0\,
\mathcal E_K(t)^{1+\theta}\,
\mathcal D_K(t)^{\frac{1-\theta}{2}}
\]
for every smooth finite-energy solution segment and every dyadic cutoff \(K\).

## Renormalized symbol
Define
\[
r_k(\xi,\eta)
:=
m_k(\xi,\eta)
-
m_k(\xi,\eta)\big|_{\xi\parallel\eta}.
\]

## Minimal curvature requirement
A sufficient local gain condition is
\[
\partial_{\perp}^2 r_k(\xi,\eta)\big|_{\xi\parallel\eta}\neq 0.
\]

## Quantitative gain form
A sufficient shellwise estimate is
\[
|r_k(\xi,\eta)|
\gtrsim
2^{-\alpha k}|\xi\wedge\eta|^2
\]
for some \(\alpha>0\) on the localized transverse interaction region.

## Shellwise consequence
If the curvature gain implies
\[
\sum_{|m-\ell|\le C}
\int
|u_\ell|\,|u_m|\,|\nabla u_{\max\{\ell,m\}}|
\lesssim
2^{-(1+\alpha)\ell}
E_\ell^{1+\theta}
\Big(\sum_{j\le \ell}2^jE_j\Big)^{\frac{1-\theta}{2}},
\]
then summing over \(\ell\le K\) yields the target inequality.

## Classification
Single irreducible OPEN obstruction.

## No-claim rule
No unconditional proof is claimed here.


## Canonical target inequality

\[
|r_k(\xi,\eta)| \ge c\,2^{-\alpha k}|\xi\wedge\eta|^2
\]

## Closure consequence

\[
\mathcal R_K(t) \lesssim \mathcal E_K(t)^{1+\theta}\mathcal D_K(t)^{\frac{1-\theta}{2}}
\]
