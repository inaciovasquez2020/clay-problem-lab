# RA1n Terminal Admissibility Weak-Orthogonality Theorem

Status: CONDITIONAL STRUCTURAL THEOREM

## Target

Prove

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
\forall \zeta\in W_{\mathrm{term}}^\perp,
\qquad
\langle \chi,\zeta\rangle_{L^2}=0.
\]

## Weak Terminal Orthogonality Hypothesis

Assume terminal admissibility includes the weak annihilation condition

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
\mathcal W_{\mathrm{term}}(\chi)=0,
\]

where

\[
\mathcal W_{\mathrm{term}}(\chi)
:=
\sup_{\substack{\zeta\in W_{\mathrm{term}}^\perp\\ \|\zeta\|_2=1}}
|\langle \chi,\zeta\rangle_{L^2}|.
\]

## Theorem

If

\[
\mathcal A_{\mathrm{term}}(\chi),
\]

then

\[
\forall \zeta\in W_{\mathrm{term}}^\perp,
\qquad
\langle \chi,\zeta\rangle_{L^2}=0.
\]

## Proof

Assume

\[
\mathcal A_{\mathrm{term}}(\chi).
\]

Then

\[
\mathcal W_{\mathrm{term}}(\chi)=0.
\]

Let

\[
\zeta\in W_{\mathrm{term}}^\perp.
\]

If \(\zeta=0\), then

\[
\langle \chi,\zeta\rangle_{L^2}=0.
\]

If \(\zeta\neq0\), define

\[
\widehat \zeta:=\frac{\zeta}{\|\zeta\|_2}.
\]

Then

\[
\widehat \zeta\in W_{\mathrm{term}}^\perp,
\qquad
\|\widehat \zeta\|_2=1.
\]

Therefore

\[
|\langle \chi,\widehat\zeta\rangle_{L^2}|
\le
\mathcal W_{\mathrm{term}}(\chi)
=
0.
\]

Thus

\[
\langle \chi,\widehat\zeta\rangle_{L^2}=0.
\]

Multiplying by \(\|\zeta\|_2\) gives

\[
\langle \chi,\zeta\rangle_{L^2}=0.
\]

## Consequence

By `RA1N_TERMINAL_ADMISSIBILITY_ANNIHILATOR_SATURATION_THEOREM.md`,

\[
\forall \zeta\in W_{\mathrm{term}}^\perp,
\quad
\langle \chi,\zeta\rangle_{L^2}=0
\Longrightarrow
(I-\Pi_W)\chi=0.
\]

## Remaining Non-Conditional Obligation

Prove the weak terminal orthogonality hypothesis from the actual admissibility rule:

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
\mathcal W_{\mathrm{term}}(\chi)=0.
\]
