# RA1n Terminal Residual-Zero Theorem

Status: OPEN.

## Object

Let

\[
V_{\mathrm{RA1n}}=\operatorname{span}\{\phi_1\}.
\]

Let

\[
\Pi_V:L^2\to V_{\mathrm{RA1n}}
\]

be the \(L^2\)-orthogonal projection.

For

\[
F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\]

define the terminal residual

\[
R(F):=(I-\Pi_V)F.
\]

## Target Theorem

\[
\boxed{
R(F)=0
\qquad
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}.
}
\]

Equivalently,

\[
\boxed{
\|(I-\Pi_V)F\|_2=0
\qquad
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}.
}
\]

## Consequence

\[
R(F)=0
\Longrightarrow
F=\Pi_VF
\Longrightarrow
F\in V_{\mathrm{RA1n}}
\Longrightarrow
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
\subset
V_{\mathrm{RA1n}}.
\]

## Weakest Missing Lemma

\[
\boxed{
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\qquad
\langle F,\psi\rangle_{L^2}=0
\quad
\forall \psi\in V_{\mathrm{RA1n}}^\perp.
}
\]

## Failure Witness

Terminal packet exhaustion fails if there exist

\[
F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\qquad
\psi\in V_{\mathrm{RA1n}}^\perp,
\]

such that

\[
\langle F,\psi\rangle_{L^2}\neq 0.
\]
