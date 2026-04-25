# RA1n Terminal Generator Normal-Form Theorem

Status: OPEN STRUCTURAL MECHANISM

## Target

Prove

\[
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\qquad
F=a(F)\phi_1
\quad
\text{for some }a(F)\in\mathbb C.
\]

Equivalently,

\[
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\qquad
(I-\Pi_V)F=0,
\]

where

\[
V_{\mathrm{RA1n}}=\operatorname{span}\{\phi_1\}.
\]

## Structural Normal-Form Mechanism

It suffices to prove that the terminal packet grammar has only the following production rules:

\[
\phi_1\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\]

and

\[
F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\ a\in\mathbb C
\Longrightarrow
aF\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}.
\]

No transverse generator is admissible:

\[
\neg\exists \psi\in V_{\mathrm{RA1n}}^\perp
\quad
\psi\neq0
\quad
\psi\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}.
\]

## Induction Theorem

If every terminal packet is generated from \(\phi_1\) by scalar multiplication only, then every terminal packet satisfies

\[
F=a(F)\phi_1.
\]

## Proof

Proceed by structural induction on terminal packet generation.

Base case:

\[
F=\phi_1=1\cdot\phi_1.
\]

Scalar step: if

\[
F=a(F)\phi_1,
\]

then for any \(b\in\mathbb C\),

\[
bF=b\,a(F)\phi_1.
\]

Set

\[
a(bF):=b\,a(F).
\]

Thus every generated terminal packet has the form

\[
F=a(F)\phi_1.
\]

Therefore

\[
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
\subset
\operatorname{span}\{\phi_1\}.
\]

Hence

\[
(I-\Pi_V)F=0
\qquad
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}.
\]

## Remaining Non-Wrapper Obligation

Prove that the actual terminal packet construction admits no production rule other than scalar multiplication of \(\phi_1\).

Equivalently, prove

\[
\mathcal G_{\mathrm{terminal}}
=
\{\phi_1\}
\]

up to scalar closure.
