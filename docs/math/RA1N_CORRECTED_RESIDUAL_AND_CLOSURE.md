# RA1n corrected residual and closure surface

## Corrected residual symbol

The formula
\[
r_k(\xi,\eta,\zeta)
=
\psi_k(\xi)\left[\frac{\xi\cdot\eta}{|\xi|^2}+\frac{\xi\cdot\zeta}{|\xi|^2}-1\right]\mathbf 1_{\{\xi=\eta+\zeta\}}
\]
is identically zero on \(\{\xi=\eta+\zeta\}\), since
\[
\frac{\xi\cdot\eta}{|\xi|^2}+\frac{\xi\cdot\zeta}{|\xi|^2}
=
\frac{\xi\cdot(\eta+\zeta)}{|\xi|^2}
=
\frac{\xi\cdot\xi}{|\xi|^2}
=
1.
\]

Hence the canonical residual is
\[
r_k=\widehat G_k-P_k\widehat G_k.
\]

## Corrected defect form

\[
\Phi_k^{\mathrm{defect}}(u,v,w)
:=
\int_{\xi=\eta+\zeta}
r_k(\xi,\eta,\zeta)\,
\bigl(\widehat u(\eta)\otimes \widehat v(\zeta)\bigr):\overline{\widehat w(\xi)}
\,d\eta\,d\zeta.
\]

\[
\mathcal I_{k,m,n}^{\mathrm{defect}}
:=
\int_{\xi=\eta+\zeta}
r_k(\xi,\eta,\zeta)\,
\bigl(\widehat u_m(\eta)\otimes \widehat u_n(\zeta)\bigr):\overline{\widehat u_k(\xi)}
\,d\eta\,d\zeta.
\]

## Canonical remaining obligations

\[
|r_k(\xi,\eta,\zeta)|
\le
C\,2^{-\alpha k}\,\mathfrak m_k(\xi,\eta,\zeta)
\qquad
(\alpha>0).
\]

\[
|\mathcal I_{k,m,n}^{\mathrm{defect}}|
\le
C\,2^{-\sigma(|k-m|+|k-n|)}\,2^k\,E_k^{1/2}E_m^{1/2}E_n^{1/2}
\qquad
(\sigma>0).
\]

\[
\sum_{m,n}
2^{-\sigma(|k-m|+|k-n|)}
E_m^{1/2}E_n^{1/2}
\le
C\,E_k^{\theta+\frac12}
\qquad
(\theta\in(0,1)).
\]

Under these three items,
\[
|\Phi_k^{\mathrm{defect}}|
\le
C\,2^kE_k^{1+\theta},
\]
hence
\[
\sum_{k\le K}|\Phi_k^{\mathrm{defect}}|
\le
C\sum_{k\le K}2^kE_k^{1+\theta}.
\]

## Status

Conditional.

RA1n is not closed by the zero-symbol formula.

The remaining frontier is the exponent-drop shell-sum theorem together with the corrected residual-symbol gain for
\[
r_k=\widehat G_k-P_k\widehat G_k.
\]
