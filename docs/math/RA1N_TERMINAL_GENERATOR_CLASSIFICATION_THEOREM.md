# RA1n Terminal Generator Classification Theorem

Status: OPEN TERMINAL STRUCTURAL THEOREM

## Target

\[
\mathcal G_{\mathrm{terminal}}=\{\phi_1\}
\quad
\text{up to scalar closure.}
\]

Equivalently,

\[
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\qquad
F=a(F)\phi_1
\quad
\text{for some }a(F)\in\mathbb C.
\]

## Required Structural Content

The terminal packet construction must prove all three statements:

\[
\phi_1\in\mathcal G_{\mathrm{terminal}},
\]

\[
\forall \psi\in V_{\mathrm{RA1n}}^\perp,
\qquad
\psi\notin\mathcal G_{\mathrm{terminal}},
\]

and

\[
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
=
\{a\phi_1:a\in\mathbb C\}.
\]

## Failure Witness

If there exists

\[
\psi\in V_{\mathrm{RA1n}}^\perp,
\qquad
\psi\neq0,
\qquad
\psi\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\]

then

\[
(I-\Pi_V)\psi=\psi\neq0,
\]

and terminal packet exhaustion fails.

## Terminal Missing Lemma

\[
\boxed{
\neg\exists\psi\in V_{\mathrm{RA1n}}^\perp
\quad
\psi\neq0
\quad
\psi\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}.
}
\]

## Halt Condition

No further RA1n theorem-level progress is possible without a structural rule excluding transverse terminal generators.
