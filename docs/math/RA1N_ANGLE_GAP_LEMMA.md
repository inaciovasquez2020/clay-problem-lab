# RA1n Angle-Gap Lemma

Status: CONDITIONAL

## Statement

Let

\[
g\neq 0,
\qquad
h:=\frac{\overline g}{\|g\|_2}.
\]

Assume

\[
V_{\mathrm{RA1n}}\subset L^2
\]

is a closed subspace and

\[
h\notin V_{\mathrm{RA1n}}.
\]

Let

\[
\Pi_V:L^2\to V_{\mathrm{RA1n}}
\]

be the orthogonal projection and define

\[
\alpha:=\|\Pi_Vh\|_2.
\]

Then

\[
\alpha<1.
\]

Set

\[
\epsilon:=1-\alpha>0.
\]

Then for every

\[
F\in V_{\mathrm{RA1n}},
\]

one has

\[
\left|\int F(\eta)g(\eta)\,d\eta\right|
\le
(1-\epsilon)\|F\|_2\|g\|_2.
\]

## Proof

Since \(h\notin V_{\mathrm{RA1n}}\) and \(\|h\|_2=1\),

\[
\alpha=\|\Pi_Vh\|_2<1.
\]

Thus

\[
\epsilon=1-\alpha>0.
\]

For every \(F\in V_{\mathrm{RA1n}}\),

\[
|\langle F,h\rangle_{L^2}|
=
|\langle F,\Pi_Vh\rangle_{L^2}|
\le
\|F\|_2\|\Pi_Vh\|_2
=
\alpha\|F\|_2.
\]

Since

\[
h=\frac{\overline g}{\|g\|_2},
\]

we have

\[
\langle F,h\rangle_{L^2}
=
\int F(\eta)\overline{h(\eta)}\,d\eta
=
\frac{1}{\|g\|_2}
\int F(\eta)g(\eta)\,d\eta.
\]

Therefore

\[
\left|
\int F(\eta)g(\eta)\,d\eta
\right|
=
\|g\|_2|\langle F,h\rangle_{L^2}|
\le
\alpha\|F\|_2\|g\|_2
=
(1-\epsilon)\|F\|_2\|g\|_2.
\]

## Conditional Closure

\[
h=\frac{\overline g}{\|g\|_2}\notin V_{\mathrm{RA1n}}
\Longrightarrow
\exists\epsilon>0\ \forall F\in V_{\mathrm{RA1n}},
\quad
\left|\int Fg\right|
\le
(1-\epsilon)\|F\|_2\|g\|_2.
\]

## Transversality Witness Source

The hypothesis

\[
h
otin V_{\mathrm{RA1n}}
\]

follows from `RA1N_TRANSVERSALITY_WITNESS_LEMMA.md` once there exists a bounded linear functional annihilating \(V_{\mathrm{RA1n}}\) but not annihilating \(h=\overline g/\|g\|_2\).
