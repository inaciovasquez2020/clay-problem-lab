# RA1n Terminal Frontier Chain

Status: CONDITIONAL FRONTIER CHAIN

Full_RA1n_status: CONDITIONAL

## Chain

\[
\text{unary normalized derivative closure}
\]

plus

\[
\text{Weighted Affine-Transfer Cancellation Lemma}
\]

plus either

\[
F\in g^\perp
\]

or

\[
g\equiv 0
\]

implies

\[
\text{full RA1n promotion}.
\]

## Terminal dependency

The active terminal dependency is

\[
F\in g^\perp.
\]

This means

\[
\int
(\xi_{\mathrm{out}}-\eta-\xi_{k,\omega})^\beta
\sigma_{k,\omega}(\eta)
F(\eta)
J_{k,\omega}(\eta)
\,d\eta
=
0
\qquad(|\beta|=1).
\]

## Exact surface parametrization

\[
\Phi_{\xi_{\mathrm{out}}}(\eta)
=
(\xi_{\mathrm{out}}-\eta,\eta).
\]

## Counterexample guard

If

\[
g(\eta)
=
(\xi_{\mathrm{out}}-\eta-\xi_{k,\omega})^\beta
\sigma_{k,\omega}(\eta)
J_{k,\omega}(\eta)
\not\equiv0,
\]

then

\[
F(\eta)=\frac{\overline g(\eta)}{\|g\|_2}
\]

violates the weighted FM-1 transfer requirement.

## Status rule

The RA1n chain may be promoted only after one of the following is proved:

1. \(F\in g^\perp\) follows from the RA1n packet construction.
2. \(g\equiv0\) follows from exact antisymmetry of \(\sigma_{k,\omega}\).
3. Admissible RA1n packet inputs are explicitly restricted to \(g^\perp\).

Until then, full RA1n promotion remains CONDITIONAL.
