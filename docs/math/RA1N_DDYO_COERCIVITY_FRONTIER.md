# RA1n DDYO Coercivity Frontier

## Status
CONDITIONAL

## Structural layer
CLOSED

## Geometric layer
CLOSED

## Numerical layer
BENCHMARKED

## Corrected terminal geometry
\[
\Gamma_{\mathrm{term}}^{\sharp}
=
\left\{
(\xi,\eta):
\begin{array}{l}
2^{k-1}\le |\xi|,|\eta|\le 2^{k+1},\\
\bigl||\xi|-|\eta|\bigr|\le 2^{k-C-3},\\
2^{k-C-2}\le |\xi+\eta|\le 2^{k-C}
\end{array}
\right\}.
\]

## Terminal gap lemma
\[
1-\cos\alpha_{\xi,\eta}
=
1+\cos\theta_{\xi,\eta}
=
\frac{|\xi+\eta|^2-(|\xi|-|\eta|)^2}{2|\xi||\eta|}
\ge 3\cdot 2^{-2C-9}.
\]

## Coercivity template
\[
c_{\mathrm{RA1n}}
\ge
\delta \cdot \underline{\kappa}\cdot
\left(
\inf_{\Gamma_{\mathrm{term}}^{\sharp}}
|\partial_\theta^2 \mathfrak M_k^{\mathrm{DDYO}}|
\cdot
3\cdot 2^{-2C-9}
\right)^2.
\]

## Benchmarked packet data
\[
\min \gamma_a = 0.22426,\qquad
\max_{a}\sum_{b\neq a}|m_{ab}| = 0.00228,
\]
\[
\delta = 0.9898,\qquad
|m_{ab}|\le 26.3 e^{-10|a-b|},
\]
\[
c_{\mathrm{RA1n}}^{\mathrm{bench}} \approx 0.222.
\]

## Exact-symbol nondegeneracy package
\[
\mathcal S_{\mathrm{DDYO}}^{\mathrm{explicit}}
=
\left(
\sigma_{\mathrm{eff}}(\xi,\eta),
\kappa_{\mathrm{rank\_defect}}(\xi,\eta),
D_j(\xi,\eta),
\kappa^{\mathrm{DDYO}}(\xi)
\right)
\]
with bounds
\[
0<\underline{\sigma}\le \sigma_{\mathrm{eff}}(\xi,\eta)\le \overline{\sigma}<\infty,
\]
\[
0<\underline{\kappa}_{\mathrm{rank}}
\le
|\kappa_{\mathrm{rank\_defect}}(\xi,\eta)|,
\]
\[
0<\underline{D}\le D_j(\xi,\eta)\le \overline{D}<\infty,
\qquad j\ge k+1,
\]
\[
0<\underline{\kappa}\le \kappa^{\mathrm{DDYO}}(\xi)\le \overline{\kappa}<\infty,
\]
and
\[
\inf_{(\xi,\eta)\in\Gamma_{\mathrm{term}}^{\sharp}}
|d_\perp^2 r_k(\xi,\eta)|
\ge a_{\mathrm{curv}}>0.
\]

## Weakest sufficient closure lemma
\[
\inf_{\Gamma_{\mathrm{term}}^{\sharp}}
\left|
\partial_{\theta}^2
\left[
\chi_k(\xi+\eta)
\cdot
\frac{\xi\cdot\eta}{|\xi||\eta|}
\cdot
\frac{\kappa_{\mathrm{rank\_defect}}(\xi,\eta)}{3+\sigma_{\mathrm{eff}}(\xi,\eta)}
\cdot
\sum_{j\ge k+1}2^{d(k-j)}D_j(\xi,\eta)
\right]
\right|
>0.
\]

## Finish condition
Replace the symbolic package above by explicit formulas and derive the stated lower bound.


## Uniform non-cancellation hypothesis
Assume
\[
\inf_{(\xi,\eta)\in\Gamma_{\mathrm{term}}^{\sharp}} |X_{\gamma}(\xi,\eta)| \ge \varepsilon_{\gamma} > 0.
\]
Then, under the positive-definite replacement
\[
\sigma_{\mathrm{eff}}(\xi,\eta) := |X_{\gamma}(\xi,\eta)|^2,
\]
one has the certified lower bound
\[
\sigma_{\mathrm{lower}} = \varepsilon_{\gamma}^2 > 0.
\]


## Exact kappa_rank_defect formula lock
Source file:
`navier_stokes/experiments/core/terminal_high_high_resonance_curvature_gain_sim.py`

Canonical formula:
`kappa_rank_defect(xi: tuple[float, float, float], eta: tuple[float, float, float], ) -> float: l1, l2 = eigenvalue_pair_vieta(interaction_matrix(xi, eta)) if abs(l1) <= 1.0e-12: return 0.0 return l2 / l1 def D_j( xi: tuple[float, float, float], eta: tuple[float, float, float], j: int, ) -> float: zeta = add3(xi, eta) zeta_n2 = dot3(zeta, zeta) if zeta_n2 <= 1.0e-12: return 0.0 wedge = xi[0] * eta[1] - xi[1] * eta[0] return ((wedge * wedge) / (norm3(xi) * norm3(eta) * zeta_n2)) * chi_k(zeta, j) def F_k( xi: tuple[float, float, float], eta: tuple[float, float, float], k: int, ) -> float: zeta = add3(xi, eta) nxi = norm3(xi) neta = norm3(eta) if nxi <= 1.0e-12 or neta <= 1.0e-12: return 0.0 align = dot3(xi, eta) / (nxi * neta) sig = sigma_eff(k) prefactor = chi_k(zeta, k) * align * (kappa_rank_defect(xi, eta) / (3.0 + sig)) gaussian = math.exp(-dot3(zeta, zeta) / ((2.0 ** (2 * k)) * (sig ** 2))) tail = (1.0 / 7.0) * D_j(xi, eta, k + 1) return prefactor * gaussian * tail def run_generation(g: int, seed: int) -> tuple[float, float, float, float, int, dict]: rng = random.Random(seed + g) lambda_search = None best = -1.0 best_xi = 0.0 best_eta = 0.0 best_k = 0 best_log: dict = {} min_xi = 0.0 min_eta = 0.0 min_k = 0 min_log: dict = {} for _ in range(20000) = lambda_search, best, best_xi, best_eta, best_k, {`

