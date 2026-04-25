# Exact DDYO Symbol Curvature Lemma

## Status
OPEN

Exact Symbol Curvature Lemma for terminal_high_high_resonance_curvature_gain


## Canonical Missing Object

There exist absolute constants
\[
\varepsilon_0>0,\qquad c_0>0,
\]
and a retained admissible witness class \(\mathcal A_{\mathrm{ret}}\) such that for every retained witness triple
\[
(\xi,\eta,k)\in \mathcal A_{\mathrm{ret}},
\]
one has
\[
\big|F_k(\xi,\eta)-F_k\big(\xi,\eta_{\parallel}(\xi,\eta)\big)\big|\ge c_0
\]
whenever the retained admissibility conditions hold and the transverse separation satisfies
\[
|\eta-\eta_{\parallel}(\xi,\eta)|\ge \varepsilon_0.
\]

Equivalently, the exact renormalized transverse curvature quantity
\[
r_k^{\mathrm{trans}}(\xi,\eta)
:=F_k(\xi,\eta)-F_k\big(\xi,\eta_{\parallel}(\xi,\eta)\big)
\]
admits a uniform positive lower bound on the retained admissible class:
\[
\inf_{(\xi,\eta,k)\in\mathcal A_{\mathrm{ret}}}
\big|r_k^{\mathrm{trans}}(\xi,\eta)\big|>0.
\]

## Immediate Closure Consequence

If the Exact Symbol Curvature Lemma holds, then
\[
\lambda_{\mathrm{search}} > 0,
\]
so the frontier object `terminal_high_high_resonance_curvature_gain` is no longer certified at zero score, and the OPEN gate closes.

## Retained Admissible Class Interface

The retained admissible class \(\mathcal A_{\mathrm{ret}}\) must be specified by explicit inequalities in repository-native variables only:

1. shell constraint:
\[
\chi_k(\xi+\eta)>0;
\]
2. nondegenerate propagator regime;
3. admissible patch restriction;
4. positive-curvature witness retention rule;
5. exclusion of structurally trivial zero-score cases.

Each condition must be encoded as an executable predicate.

## Smallest Sufficient Proof Decomposition

### Lemma A. Parallel Baseline Exactness
For every admissible \((\xi,\eta,k)\), the parallel projection baseline satisfies
\[
F_k\big(\xi,\eta_{\parallel}(\xi,\eta)\big)=B_k(\xi,\eta)
\]
for an explicit closed-form baseline \(B_k\).

### Lemma B. First Transverse Variation Nonvanishing
There exists an explicit transverse direction \(v_\perp\) and a retained admissible region such that
\[
\partial_{v_\perp} F_k(\xi,\eta)\neq 0.
\]

### Lemma C. Quantitative Curvature Lower Bound
There exists \(c_0>0\) such that on \(\mathcal A_{\mathrm{ret}}\),
\[
\big|F_k(\xi,\eta)-F_k(\xi,\eta_{\parallel})\big|\ge c_0.
\]

### Lemma D. Search Positivity Transfer
If Lemma C holds, then the repository search functional satisfies
\[
\lambda_{\mathrm{search}}\ge c_1 c_0>0
\]
for an explicit transfer constant \(c_1>0\) determined by the current simulator normalization.

## Repository-Native Finish Condition

Replace the locked OPEN statement by the following verified statement:

**Status: COMPLETE**

For the retained admissible class used by `terminal_high_high_resonance_curvature_gain_sim.py`, the exact DDYO symbol curvature is uniformly positive away from the parallel baseline. Consequently, `best_score > 0`, `lambda_search > 0`, `local_gain_found = true`, and the exact-symbol gate closes.

## Weakest Sufficient Mathematical Obligation

Produce an explicit formula or rigorous lower estimate for
\[
F_k(\xi,\eta)-F_k\big(\xi,\eta_{\parallel}(\xi,\eta)\big)
\]
on the retained admissible class that is strictly positive uniformly in the certified search region.

## Halting Condition

No further theorem-level progress is possible without a new invariant, estimate, or exact formula proving the positive lower bound above.
