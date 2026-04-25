# RA1n Corrected Scale-Normalized Coercivity

Status: CONDITIONAL.

Canonical residual:

r_k(ξ) = \widehat G_k(ξ) − P_k \widehat G_k(ξ).

The unscaled uniform shell coercivity claim

∫_{A_k} |∇_ξ r_k(ξ)|² w_k(ξ) dξ ≥ c ∫_{A_k} |r_k(ξ)|² w_k(ξ) dξ

with c independent of k is false on dyadic annuli of radius 2^k unless the derivative is scale-normalized or the shell diameter is uniformly bounded.

Corrected RA1n target:

∫_{A_k} |2^k ∇_ξ r_k(ξ)|² w_k(ξ) dξ ≥ c ∫_{A_k} |r_k(ξ)|² w_k(ξ) dξ.

Equivalent unscaled form:

∫_{A_k} |∇_ξ r_k(ξ)|² w_k(ξ) dξ ≥ c 2^{-2k} ∫_{A_k} |r_k(ξ)|² w_k(ξ) dξ.

Weakest sufficient assumptions:

1. r_k ∈ H¹(A_k,w_k).
2. r_k ⟂_{L²(w_k)} N_k, where N_k is the shell null-mode space killed by I − P_k.
3. 0 < m ≤ w_k(ξ) ≤ M < ∞ on A_k, uniformly in k.
4. ||∇w_k||_{L∞(A_k)} ≤ C_w 2^{-k}.
5. The normalized shell spectral gap is positive.

Conclusion:

RA1n closes only if the downstream shell-product gain uses the normalized derivative D_k := 2^k∇_ξ, or equivalently carries the factor 2^{2k} multiplying the unscaled derivative energy.
