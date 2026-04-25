# RA1n Canonical Formula Selection Gate

Status: OPEN.

Correction to the previous exact-formula gap:

The repository does contain candidate formulas for r_k. The remaining obstruction is not total absence of r_k, but non-unique competing residual surfaces.

Candidate unary RA1n formula:

\widehat G_k(ξ)=φ(2^{-k}ξ)|ξ|^{-4}.

P_k f(ξ)=f(ξ_k)+∇f(ξ_k)·(ξ−ξ_k).

r_k(ξ)=\widehat G_k(ξ)−P_k\widehat G_k(ξ).

Competing surfaces appearing in the repository include:

1. Unary residuals r_k(ξ).
2. Binary residuals r_k(ξ,η), r_k(η,ζ).
3. Ternary residuals r_k(ξ,η,ζ).
4. Transverse high-high residuals attached to ξ ∥ η.
5. Conditional symbolic residuals of the form (1−P_k(ξ))\widehat G(ξ)ψ_k(ξ).

Weakest sufficient gate:

Declare exactly one source-backed RA1n residual as canonical for the first-moment shell-product theorem, and mark every other residual surface as either:

- auxiliary,
- conditional,
- transverse high-high route,
- sampled surrogate,
- or noncanonical.

The admissible canonical choice is:

\widehat G_k(ξ)=φ(2^{-k}ξ)|ξ|^{-4},

P_k f(ξ)=f(ξ_k)+∇f(ξ_k)·(ξ−ξ_k),

r_k(ξ)=\widehat G_k(ξ)−P_k\widehat G_k(ξ).

After this gate is locked, the next theorem is the normalized derivative estimate:

sup_{|ξ|~2^k} |(2^k∇_ξ)^α r_k(ξ)| ≤ C_α.

No RA1n closure claim is admissible before canonical formula selection.
