# RA1n Terminal Generator Finite-Grammar Exclusion Theorem

Status: CONDITIONAL STRUCTURAL THEOREM

## Target

Prove

\[
\neg\exists \chi
\quad
\chi\in\mathcal G_{\mathrm{terminal}}
\quad
\chi\notin
\operatorname{span}\{\phi_1,\psi_1,\dots,\psi_m\}.
\]

Equivalently,

\[
\mathcal G_{\mathrm{terminal}}
\subset
\operatorname{span}\{\phi_1,\psi_1,\dots,\psi_m\}.
\]

## Terminal Generator Admissibility Functional

Let

\[
\mathcal A_{\mathrm{term}}(\chi)
\]

be the RA1n terminal generator admissibility predicate.

Assume

\[
\chi\in\mathcal G_{\mathrm{terminal}}
\Longleftrightarrow
\mathcal A_{\mathrm{term}}(\chi).
\]

## Finite-Grammar Exhaustion Hypothesis

Assume the admissibility predicate factors through the finite terminal coordinates:

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
\chi
=
a(\chi)\phi_1
+
\sum_{j=1}^m c_j(\chi)\psi_j
\]

for some

\[
a(\chi),c_1(\chi),\dots,c_m(\chi)\in\mathbb C.
\]

## Theorem

\[
\mathcal G_{\mathrm{terminal}}
\subset
\operatorname{span}\{\phi_1,\psi_1,\dots,\psi_m\}.
\]

Equivalently,

\[
\neg\exists \chi
\quad
\chi\in\mathcal G_{\mathrm{terminal}}
\quad
\chi\notin
\operatorname{span}\{\phi_1,\psi_1,\dots,\psi_m\}.
\]

## Proof

Let

\[
\chi\in\mathcal G_{\mathrm{terminal}}.
\]

By generator admissibility,

\[
\mathcal A_{\mathrm{term}}(\chi).
\]

By finite-grammar exhaustion,

\[
\chi
=
a(\chi)\phi_1
+
\sum_{j=1}^m c_j(\chi)\psi_j.
\]

Therefore

\[
\chi\in
\operatorname{span}\{\phi_1,\psi_1,\dots,\psi_m\}.
\]

Thus

\[
\mathcal G_{\mathrm{terminal}}
\subset
\operatorname{span}\{\phi_1,\psi_1,\dots,\psi_m\}.
\]

Hence no terminal generator lies outside the finite grammar.

## Consequence

By `RA1N_TERMINAL_GRAMMAR_FINITE_RESIDUAL_THEOREM.md`,

\[
\mathcal G_{\mathrm{terminal}}
\subset
\operatorname{span}\{\phi_1,\psi_1,\dots,\psi_m\}
\]

implies the finite residual expansion

\[
(I-\Pi_V)F
=
\sum_{j=1}^m c_j(F)\psi_j
\qquad
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}.
\]

## Remaining Non-Conditional Obligation

Prove the finite-grammar exhaustion hypothesis from the actual RA1n admissibility predicate:

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
\chi
=
a(\chi)\phi_1
+
\sum_{j=1}^m c_j(\chi)\psi_j.
\]
