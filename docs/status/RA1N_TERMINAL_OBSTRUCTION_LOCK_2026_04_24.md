# RA1n terminal obstruction lock

Status: OPEN.

## Canonical terminal obstruction

RA1n remains the terminal theorem-level obstruction for DDYO high-high absorbability.

The missing theorem is the first-moment shell-product / direct-symbol-derivative estimate controlling the canonical annular remainder

```text
r_k(ξ) = \widehat G_k(ξ) - P_k \widehat G_k(ξ)
Correction to proposed closure proof
The proposed RA1n proof is not yet a theorem-level closure.
The following steps are still assumptions unless proved from repository definitions:
P_k \widehat G_k(ξ) = \widehat G_k(0) is not automatically compatible with a dyadic annular symbol supported on |ξ| ~ 2^k.
∫ r_k(ξ) dξ = 0 does not follow merely from subtracting the value at the origin.
r_k(0)=0 is not enough to obtain the stated dyadic first-moment bound without an explicit support, normalization, and derivative estimate.
The bound
|∂_{ξ_ℓ} r_k^{a,b}(ξ)| ≤ C · 2^{-k} · W_k(ξ)
is the analytic core and must be proved, not assumed.
The shell factor 2^{-j} must be derived from the exact definition of shell_product_first_moment, not inserted as a scaling heuristic.
The integration-by-parts / dual-form transfer must be justified with the precise function spaces and boundary/support conditions.
Required theorem-level input
A valid RA1n closure must prove, from explicit definitions, a theorem of the form:
|shell_product_first_moment_{j,k}^{a,b,ℓ}(r_k, ω_k)|
  ≤ C_RA1n · 2^{-j} · 2^{-k} · ||ω_k||_{L^1}
uniformly for all permitted dyadic interactions |j-k| ≤ C.
Locked boundary
No unconditional Navier--Stokes or DDYO continuum closure is claimed in this repository from the present RA1n layer.
Current repository action
This file does not solve RA1n. It locks the terminal obstruction and records why the proposed closure proof remains conditional.
