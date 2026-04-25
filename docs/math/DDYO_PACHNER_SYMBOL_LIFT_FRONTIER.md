# DDYO Pachner Symbol Lift Frontier

## Status
CONDITIONAL

## Purpose
This document records the weakest sufficient missing bridge from verified discrete Pachner outbound data to the original DDYO symbol package.

## Verified discrete input
The following discrete facts are treated as upstream verified inputs only:
- rank_F2(F6) = 5
- rank_F2(F7) = 25

These facts do not by themselves imply any analytic DDYO symbol bounds.

## Canonical missing bridge
The missing object is an explicit map
\[
\Phi_{6,7} : (F_6,F_7,V_{\mathrm{out}},E_{\mathrm{out}}) \longmapsto
\mathcal S_{\mathrm{DDYO}}^{\mathrm{orig}}
=
\Bigl(
\sigma_{\mathrm{eff}}(\xi,\eta),
\kappa_{\mathrm{rank\_defect}}(\xi,\eta),
D_j(\xi,\eta),
\kappa^{\mathrm{DDYO}}(\xi),
\chi_{\mathrm{out}}(\zeta)
\Bigr).
\]

## Required output conditions
The map \(\Phi_{6,7}\) must produce explicit formulas satisfying:

\[
0<\underline{\sigma}\le \sigma_{\mathrm{eff}}(\xi,\eta)\le \overline{\sigma}<\infty,
\]

\[
0<\underline{\kappa}_{\mathrm{rank}}
\le
|\kappa_{\mathrm{rank\_defect}}(\xi,\eta)|,
\]

\[
0<\underline{D}\le D_j(\xi,\eta)\le \overline{D}<\infty
\qquad (j\ge k+1),
\]

\[
0<\underline{\kappa}\le \kappa^{\mathrm{DDYO}}(\xi)\le \overline{\kappa}<\infty,
\]

\[
\chi_{\mathrm{out}}(\zeta)\equiv 1
\quad\text{for}\quad
2^{k-C-2}\le |\zeta|\le 2^{k-C}.
\]

## Weakest sufficient closure lemma
The theorem closes only after proving

\[
\inf_{(\xi,\eta)\in\Gamma_{\mathrm{term}}^{\sharp}}
\left|
\partial_{\theta}^{2}
\left[
\chi_{\mathrm{out}}(\xi+\eta)\,
\frac{\xi\cdot\eta}{|\xi||\eta|}\,
\frac{\kappa_{\mathrm{rank\_defect}}(\xi,\eta)}{3+\sigma_{\mathrm{eff}}(\xi,\eta)}
\sum_{j\ge k+1}2^{d(k-j)}D_j(\xi,\eta)
\right]
\right|
>0.
\]

## Non-implication lock
The following implication is NOT established in this repository state:

\[
\operatorname{rank}_{\mathbf F_2}(F_6)=5,\quad \operatorname{rank}_{\mathbf F_2}(F_7)=25
\;\centernot\Longrightarrow\;
a_{\mathrm{curv}}>0.
\]

## Missing data
To define \(\Phi_{6,7}\) explicitly, the repository must contain the outbound enumeration data:
- \(V_{\mathrm{out}}\)
- \(E_{\mathrm{out}}\)
- the coordinate assignment \(X_\gamma\) for each outbound generator

## Finish condition
Add explicit outbound sets and coordinate assignments, define \(\Phi_{6,7}\) as code and math, and prove that the induced original DDYO symbols satisfy the transverse non-degeneracy inequality above.


## Non-cancellation lock
Assume
\[
\inf_{(\xi,\eta)\in\Gamma_{\mathrm{term}}^{\sharp}} |X_{\gamma}(\xi,\eta)| \ge \varepsilon_{\gamma} > 0.
\]
Then the positive-definite replacement
\[
\sigma_{\mathrm{eff}}(\xi,\eta) := |X_{\gamma}(\xi,\eta)|^2
\]
obeys
\[
\sigma_{\mathrm{lower}} = \varepsilon_{\gamma}^2 > 0.
\]



## Piecewise sigma_lower rule

The terminal bridge rule is locked by the condition
\[
\inf_{(\xi,\eta)\in\Gamma_{\mathrm{term}}^{\sharp}} |X_{\gamma}(\xi,\eta)| \ge \varepsilon_{\gamma}>0.
\]

On the terminal patch,
\[
\sigma_{\mathrm{lower}}=\varepsilon_{\gamma}^{2}.
\]
