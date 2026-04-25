# RA1n Downstream Scale Compatibility

Status: CONDITIONAL.

The corrected RA1n coercivity scale is

D_k := 2^k∇_ξ.

Therefore the admissible derivative target is not an unscaled estimate for ∇_ξ r_k, but a scale-invariant estimate for D_k r_k.

Correct downstream form:

sup_{|ξ| ~ 2^k} |(2^k∇_ξ)^α r_k(ξ)| ≤ C_α.

Equivalent fixed-annulus form after ξ = 2^kη:

2^{k|α|}(∂^α r_k)(2^kη).

The downstream shell-product kernel route is compatible with the corrected RA1n scaling exactly when all symbol-derivative hypotheses on r_k occur in this normalized form.

Unscaled uniform coercivity

∫_{A_k} |∇_ξ r_k|² w_k dξ ≥ c ∫_{A_k} |r_k|² w_k dξ

with c independent of k is not an admissible RA1n target on dyadic annuli.

Weakest remaining theorem:

Derive the normalized bound

sup_{|ξ| ~ 2^k} |(2^k∇_ξ)^α r_k(ξ)| ≤ C_α

from the exact repository formula for

r_k(ξ) = \widehat G_k(ξ) − P_k \widehat G_k(ξ).

Once this is proved, the corrected scale-normalized coercivity and the shell-product kernel estimate are compatible.
