# RA1n Terminal Admissibility Annihilator-Saturation Theorem

Status: CONDITIONAL STRUCTURAL THEOREM

## Target

Prove

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
(I-\Pi_W)\chi=0.
\]

## Objects

Let

\[
W_{\mathrm{term}}
=
\operatorname{span}\{\phi_1,\psi_1,\dots,\psi_m\}
\subset L^2.
\]

Let

\[
\Pi_W:L^2\to W_{\mathrm{term}}
\]

be the orthogonal projection.

Then

\[
L^2
=
W_{\mathrm{term}}
\oplus
W_{\mathrm{term}}^\perp.
\]

## Annihilator-Saturation Hypothesis

Assume terminal admissibility annihilates every orthogonal test mode:

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
\forall \zeta\in W_{\mathrm{term}}^\perp,
\qquad
\langle \chi,\zeta\rangle_{L^2}=0.
\]

## Theorem

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
(I-\Pi_W)\chi=0.
\]

## Proof

Assume

\[
\mathcal A_{\mathrm{term}}(\chi).
\]

Set

\[
r:=(I-\Pi_W)\chi.
\]

Since \(\Pi_W\) is the orthogonal projection onto \(W_{\mathrm{term}}\),

\[
r\in W_{\mathrm{term}}^\perp.
\]

By the annihilator-saturation hypothesis, taking

\[
\zeta=r
\]

gives

\[
\langle \chi,r\rangle_{L^2}=0.
\]

Now decompose

\[
\chi=\Pi_W\chi+r.
\]

Since

\[
\Pi_W\chi\in W_{\mathrm{term}}
\quad
\text{and}
\quad
r\in W_{\mathrm{term}}^\perp,
\]

we have

\[
\langle \Pi_W\chi,r\rangle_{L^2}=0.
\]

Therefore

\[
0
=
\langle \chi,r\rangle_{L^2}
=
\langle \Pi_W\chi+r,r\rangle_{L^2}
=
\|r\|_2^2.
\]

Hence

\[
r=0.
\]

Thus

\[
(I-\Pi_W)\chi=0.
\]

## Consequence

By `RA1N_TERMINAL_ADMISSIBILITY_FINITE_COORDINATE_THEOREM.md`,

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
(I-\Pi_W)\chi=0
\]

implies

\[
\chi
=
a(\chi)\phi_1
+
\sum_{j=1}^m c_j(\chi)\psi_j.
\]

## Remaining Non-Conditional Obligation

Prove annihilator saturation from the actual RA1n terminal admissibility rule:

\[
\mathcal A_{\mathrm{term}}(\chi)
\Longrightarrow
\forall \zeta\in W_{\mathrm{term}}^\perp,
\qquad
\langle \chi,\zeta\rangle_{L^2}=0.
\]
