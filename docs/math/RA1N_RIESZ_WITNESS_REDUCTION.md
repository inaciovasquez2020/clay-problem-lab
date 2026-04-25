# RA1n Riesz Witness Reduction

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

The following are equivalent:

\[
h\notin V_{\mathrm{RA1n}}
\]

and

\[
\exists w\in V_{\mathrm{RA1n}}^\perp
\quad
\langle h,w\rangle_{L^2}\neq0.
\]

## Proof: Witness Implies Transversality

Assume

\[
w\in V_{\mathrm{RA1n}}^\perp,
\qquad
\langle h,w\rangle_{L^2}\neq0.
\]

If

\[
h\in V_{\mathrm{RA1n}},
\]

then, since \(w\in V_{\mathrm{RA1n}}^\perp\),

\[
\langle h,w\rangle_{L^2}=0,
\]

contradiction.

Hence

\[
h\notin V_{\mathrm{RA1n}}.
\]

## Proof: Transversality Gives Witness

Assume

\[
h\notin V_{\mathrm{RA1n}}.
\]

Let

\[
\Pi_V:L^2\to V_{\mathrm{RA1n}}
\]

be the orthogonal projection and define

\[
w:=(I-\Pi_V)h.
\]

Then

\[
w\in V_{\mathrm{RA1n}}^\perp.
\]

Since \(h\notin V_{\mathrm{RA1n}}\),

\[
w\neq0.
\]

Moreover,

\[
\langle h,w\rangle_{L^2}
=
\langle \Pi_Vh+w,w\rangle_{L^2}
=
\|w\|_2^2
\neq0.
\]

Therefore

\[
\exists w\in V_{\mathrm{RA1n}}^\perp
\quad
\langle h,w\rangle_{L^2}\neq0.
\]

## Functional Form

Define

\[
\Lambda_w(F):=\langle F,w\rangle_{L^2}.
\]

Then

\[
\Lambda_w(F)=0
\qquad
\forall F\in V_{\mathrm{RA1n}},
\]

and

\[
\Lambda_w(h)=\langle h,w\rangle_{L^2}\neq0.
\]

Thus `RA1N_TRANSVERSALITY_WITNESS_LEMMA.md` applies.

## Terminal Form

\[
\exists w\in V_{\mathrm{RA1n}}^\perp
:
\left\langle
\frac{\overline g}{\|g\|_2},
w
\right\rangle_{L^2}
\neq0
\Longrightarrow
\text{Angle-Gap}.
\]
