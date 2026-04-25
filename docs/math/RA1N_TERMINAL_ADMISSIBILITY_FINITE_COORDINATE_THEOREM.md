# RA1n Terminal Admissibility Finite-Coordinate Theorem

Status: CONDITIONAL STRUCTURAL THEOREM

## Target

Prove

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
\chi
=
a(\chi)\phi_1
+
\sum_{j=1}^m c_j(\chi)\psi_j.
\]

## Objects

Let

\[
\Phi_{\mathrm{term}}
:
L^2
\to
\mathbb C^{m+1}
\]

be the terminal coordinate map

\[
\Phi_{\mathrm{term}}(\chi)
=
\left(
\langle \chi,\phi_1\rangle_{L^2},
\langle \chi,\psi_1\rangle_{L^2},
\dots,
\langle \chi,\psi_m\rangle_{L^2}
\right).
\]

Let

\[
W_{\mathrm{term}}
=
\operatorname{span}\{\phi_1,\psi_1,\dots,\psi_m\}.
\]

Let

\[
\Pi_W:L^2\to W_{\mathrm{term}}
\]

be the orthogonal projection.

## Finite-Coordinate Admissibility Hypothesis

Assume terminal admissibility is saturated by the finite coordinate projection:

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
\chi=\Pi_W\chi.
\]

Equivalently,

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
(I-\Pi_W)\chi=0.
\]

## Theorem

If

\[
\mathcal A_{\mathrm{term}}(\chi),
\]

then there exist coefficients

\[
a(\chi),c_1(\chi),\dots,c_m(\chi)\in\mathbb C
\]

such that

\[
\chi
=
a(\chi)\phi_1
+
\sum_{j=1}^m c_j(\chi)\psi_j.
\]

## Proof

Assume

\[
\mathcal A_{\mathrm{term}}(\chi).
\]

By finite-coordinate admissibility,

\[
\chi=\Pi_W\chi.
\]

Since

\[
\Pi_W\chi\in W_{\mathrm{term}},
\]

and

\[
W_{\mathrm{term}}
=
\operatorname{span}\{\phi_1,\psi_1,\dots,\psi_m\},
\]

there exist

\[
a(\chi),c_1(\chi),\dots,c_m(\chi)\in\mathbb C
\]

such that

\[
\Pi_W\chi
=
a(\chi)\phi_1
+
\sum_{j=1}^m c_j(\chi)\psi_j.
\]

Because

\[
\chi=\Pi_W\chi,
\]

we obtain

\[
\chi
=
a(\chi)\phi_1
+
\sum_{j=1}^m c_j(\chi)\psi_j.
\]

## Consequence

By `RA1N_TERMINAL_GENERATOR_FINITE_GRAMMAR_EXCLUSION_THEOREM.md`,

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
\chi
=
a(\chi)\phi_1
+
\sum_{j=1}^m c_j(\chi)\psi_j
\]

implies

\[
\mathcal G_{\mathrm{terminal}}
\subset
\operatorname{span}\{\phi_1,\psi_1,\dots,\psi_m\}.
\]

## Remaining Non-Conditional Obligation

Prove the finite-coordinate admissibility hypothesis from the actual RA1n terminal admissibility rule:

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
(I-\Pi_W)\chi=0.
\]
