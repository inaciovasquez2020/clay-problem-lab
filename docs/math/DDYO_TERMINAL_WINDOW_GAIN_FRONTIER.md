# Conditional: DDYO terminal window-gain frontier

## Canonical shell coefficient

Define
\[
\mathcal A_\ell(t):=
2^{2\ell}
\left(
\int_{t-2^{-2\ell}}^{t}E_\ell(s)\,ds
\right)^{1/2}.
\]

This is the shellwise coefficient that enters the DDYO \(L^2\to L^\infty\) bootstrap.

## Non-frontier deletion

The previously introduced low-shell quantity
\[
\mathcal R_K(t):=
2^{-K}\int_{t-2^{-2K}}^{t}\sum_{\ell\le K}2^{-\ell}E_\ell(s)\,ds
\]
is not a terminal frontier object, because
\[
\mathcal R_K(t)\le \mathcal D_K(t).
\]

Hence \(\mathcal R_K\) must be removed from the canonical missing-object surface.

## Terminal open problem

\[
\boxed{
\text{Open Problem.}
\quad
\exists\,\sigma>0,\ C<\infty
\text{ such that }
\mathcal A_\ell(t)\le C\,2^{-\sigma\ell}
\quad
\forall\,\ell\ge 0,\ t\ge 0.
}
\]

Equivalently,
\[
\boxed{
\sup_{\ell,t}
2^{(2+\sigma)\ell}
\left(
\int_{t-2^{-2\ell}}^{t}E_\ell(s)\,ds
\right)^{1/2}
<\infty.
}
\]

## Conditional closure surface

Assume the DDYO shell forcing estimate
\[
\|F_\ell(s)\|_{L^2}\lesssim 2^\ell E_\ell(s)^{1/2}\Phi(s),
\qquad
\Phi(s):=\sup_{m\ge 0}2^{m/2}U_m(s).
\]

If the terminal window-gain bound holds with sufficiently small constant, then the DDYO shell bootstrap closes.

## Canonical consequence for the repo

- Delete \(\mathcal R_K\) as a frontier object.
- Delete the false split into two independent tail objects.
- Replace both by the single terminal frontier \(\mathcal A_\ell(t)\).
