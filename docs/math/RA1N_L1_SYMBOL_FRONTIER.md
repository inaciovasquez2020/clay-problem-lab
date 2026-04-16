# Conditional: RA1n L1 symbol frontier

## Canonical remaining object
Prove that the actual RA1n terminal symbol Fourier kernel \hat G belongs to L^1(R^3).

### Weakest sufficient lemma
There exist constants alpha, eps, C with
- alpha < 3
- eps > 0
- C > 0

such that for all xi in R^3,
|Ghat(xi)| <= C * min(|xi|^{-alpha}, (1 + |xi|)^(-3-eps)).

### Required split
1. Local integrability near the origin:
   integral_{|xi|<=1} |Ghat(xi)| dxi < infinity

2. Tail integrability at infinity:
   integral_{|xi|>=1} |Ghat(xi)| dxi < infinity

### Exact remaining subproblems
1. Extract the concrete formula for Ghat from the RA1n terminal symbol.
2. Prove the local singularity exponent is strictly below 3.
3. Prove the decay exponent at infinity is strictly above 3.
4. Combine the two bounds into an L^1 proof on R^3.
5. Lift L^1_integrable to the registry flag C = 1.

### Closure trigger
If allCertified = true and C = 1, then the RA1n registry upgrades from CONDITIONAL to CANONICAL.

## Concrete symbol
Paste the exact formula for Ghat here.

## Local bound proof
Prove: there exist alpha < 3 and C0 > 0 such that
|Ghat(xi)| <= C0 |xi|^{-alpha} for |xi| <= 1.

## Tail bound proof
Prove: there exist eps > 0 and Cinf > 0 such that
|Ghat(xi)| <= Cinf (1 + |xi|)^(-3-eps) for |xi| >= 1.
