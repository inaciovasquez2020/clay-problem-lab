# RA1n Transversality Witness Lemma

Status: PROVED ABSTRACTLY

## Statement

Let

\[
g\neq0,
\qquad
h:=\frac{\overline g}{\|g\|_2}.
\]

Let

\[
V_{\mathrm{RA1n}}\subset L^2
\]

be a closed subspace.

Assume there exists a bounded linear functional

\[
\Lambda:L^2\to\mathbb C
\]

such that

\[
\Lambda(F)=0
\qquad
\forall F\in V_{\mathrm{RA1n}},
\]

and

\[
\Lambda(h)\neq0.
\]

Then

\[
h\notin V_{\mathrm{RA1n}}.
\]

## Proof

Assume for contradiction that

\[
h\in V_{\mathrm{RA1n}}.
\]

Since \(\Lambda\) annihilates \(V_{\mathrm{RA1n}}\),

\[
\Lambda(h)=0,
\]

contradicting

\[
\Lambda(h)\neq0.
\]

Therefore

\[
h\notin V_{\mathrm{RA1n}}.
\]

## Consequence

By `RA1N_ANGLE_GAP_LEMMA.md`, there exists \(\epsilon>0\) such that

\[
\left|\int Fg\right|
\le
(1-\epsilon)\|F\|_2\|g\|_2
\qquad
\forall F\in V_{\mathrm{RA1n}}.
\]

## Terminal Form

\[
\exists\Lambda\in (L^2)^*
:
\Lambda|_{V_{\mathrm{RA1n}}}=0
\ \text{and}\
\Lambda\left(\frac{\overline g}{\|g\|_2}\right)\neq0
\Longrightarrow
\text{Angle-Gap}.
\]
