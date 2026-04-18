# RA1n Qk/Dini Reduction

## Status
Conditional.

## Definitions

Let
\[
E_k(t):=\|u_k(t)\|_{L_x^2}^2,
\qquad
\mathcal M_k(t):=\sup_{|j-k|\le C_0}E_j(t),
\qquad
Q_k(t):=\frac{\mathcal M_k(t)}{E_k(t)}.
\]

Assume the shell energy identity has the form
\[
D^+E_k(t)=\mathcal N_k(t)-\mathcal D_k(t),
\]
with bounds
\[
\mathcal N_k(t)\ge -\,b_k\,\mathcal M_k(t),
\qquad
\mathcal D_k(t)\le a_k\,E_k(t).
\]
Then
\[
D^+E_k(t)\ge -a_kE_k(t)-b_k\mathcal M_k(t).
\]

For the local shell supremum,
\[
\mathcal M_k(t)=\sup_{|j-k|\le C_0}E_j(t),
\]
the upper Dini derivative satisfies
\[
D^+\mathcal M_k(t)\le \sup_{|j-k|\le C_0}D^+E_j(t).
\]
Hence if
\[
D^+E_j(t)\le \alpha_k\,\mathcal M_k(t)+\beta_k\,E_k(t)
\qquad (|j-k|\le C_0),
\]
then
\[
D^+\mathcal M_k(t)\le \alpha_k\mathcal M_k(t)+\beta_kE_k(t).
\]

## Qk inequality

Using the Dini quotient rule,
\[
D^+Q_k(t)
\le
\frac{D^+\mathcal M_k(t)}{E_k(t)}
-
\frac{\mathcal M_k(t)}{E_k(t)^2}D_+E_k(t).
\]
Substituting the preceding bounds gives
\[
D^+Q_k(t)
\le
\beta_k+(\alpha_k+a_k)Q_k(t)+b_kQ_k(t)^2.
\]

If moreover
\[
\beta_k+b_k\le \mu,
\qquad
\alpha_k+a_k\le -\mu
\]
uniformly in \(k\), then for every \(Q_k\ge 1\),
\[
D^+Q_k(t)
\le
\mu-\mu Q_k(t)
=
-\mu\bigl(Q_k(t)-1\bigr).
\]

## Dini-sup Lyapunov functional

Define
\[
L(t):=\sup_k(Q_k(t)-1)\ge 0.
\]
Then
\[
D^+L(t)\le -\mu L(t)\le 0.
\]
Therefore
\[
L(t)\le e^{-\mu t}L(0),
\qquad
Q_k(t)\le 1+L(0)\quad\forall k,t.
\]
Equivalently,
\[
\mathcal M_k(t)\le (1+L(0))E_k(t).
\]

## Consequence for RA1n

Thus shell comparability holds with
\[
A:=1+L(0).
\]
Substituting into the conditional RA1n closure yields
\[
\sum_{m,n\sim k}
\left|
\int_{\xi=\eta+\zeta}
r_k(\eta,\zeta)
\bigl(\widehat u_m(\eta)\otimes\widehat u_n(\zeta)\bigr):
\overline{\widehat u_k(\xi)}
\,d\eta\,d\zeta
\right|
\le
C'(A,C_0)\,2^{\beta k}E_k(t)^{3/2}.
\]

## Remaining gap

The remaining open input is a shell-energy identity and uniform coefficients
\[
a_k,\ b_k,\ \alpha_k,\ \beta_k,\ \mu
\]
for the actual DDYO/Navier--Stokes shell dynamics satisfying the displayed hypotheses.
