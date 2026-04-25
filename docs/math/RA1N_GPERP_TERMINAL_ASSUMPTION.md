# RA1n \(g^\perp\) Terminal Assumption

Status: TERMINAL FRONTIER / CONDITIONAL

Full_RA1n_status: CONDITIONAL

## Non-provability from current data

The statement

\[
F\in g^\perp
\]

is not derivable from the current RA1n packet construction unless an additional structural constraint is imposed on admissible packets or on the interaction symbol.

The obstruction is the theorem-level guard

\[
g(\eta)
=
(\xi_{\mathrm{out}}-\eta-\xi_{k,\omega})^\beta
\sigma_{k,\omega}(\eta)
J_{k,\omega}(\eta).
\]

If

\[
g\not\equiv0,
\]

then

\[
F(\eta)=\frac{\overline g(\eta)}{\|g\|_2}
\]

is an admissible \(L^2\)-packet Fourier input and gives

\[
\int g(\eta)F(\eta)\,d\eta
=
\|g\|_2
\ne0.
\]

Therefore arbitrary admissible RA1n packet inputs do not satisfy \(F\in g^\perp\).

## Weakest sufficient terminal assumption

Restrict admissible RA1n packet inputs by

\[
\boxed{
F\in g^\perp
}
\]

meaning

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

Equivalently,

\[
I_1^\beta(F)=0.
\]

## Conditional closure rule

If

\[
F\in g^\perp
\]

and the weighted FM-0 estimate holds,

\[
|I_0(F)|
\le
C2^{-\delta k}
\|\sigma_{k,\omega}\|_{L^1}
\|P_{k,\omega}f\|_{L^2},
\]

then

\[
\left|
\gamma_{k,\omega}^\beta I_0(F)-I_1^\beta(F)
\right|
\le
C2^{-\delta k}
\|\sigma_{k,\omega}\|_{L^1}
\|P_{k,\omega}f\|_{L^2}.
\]

Hence

\[
F\in g^\perp
+
\text{weighted FM-0}
\Longrightarrow
\text{Weighted Affine-Transfer Cancellation}.
\]

## Exact antisymmetry alternative

The stronger route is

\[
g\equiv0.
\]

This requires the exact antisymmetry condition

\[
(\xi_{\mathrm{out}}-\eta-\xi_{k,\omega})^\beta
\sigma_{k,\omega}(\eta)
J_{k,\omega}(\eta)
\equiv0
\]

or an equivalent signed-pair cancellation on the parametrized surface.

Without this exact antisymmetry, \(g\equiv0\) is not proved.

## Final status

Full RA1n promotion remains CONDITIONAL until either:

1. \(F\in g^\perp\) is proved from the RA1n packet construction;
2. admissible RA1n packets are explicitly restricted to \(g^\perp\); or
3. \(g\equiv0\) is proved from exact antisymmetry of \(\sigma_{k,\omega}\).
