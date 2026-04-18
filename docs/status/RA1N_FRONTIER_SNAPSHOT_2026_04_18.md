# RA1n Frontier Snapshot — 2026-04-18

## Locked chain

The following theorem-level route is now locked in-repo:

1. Kernel parity normal form:
   - `docs/math/RA1N_KERNEL_PARITY_NORMAL_FORM.md`
   - first-order cancellation route installed
   - paired antisymmetry class isolated

2. Projector-consistent kernel:
   - `docs/math/RA1N_PROJECTOR_CONSISTENT_KERNEL.md`
   - radial/real/even/self-adjoint projector kernel locked
   - divergence-free preservation locked
   - Fourier commutator form locked
   - DDYO symbol compatibility locked

3. Projector paired symmetry:
   - `docs/math/RA1N_PROJECTOR_PAIRED_SYMMETRY.md`
   - exact paired exchange symmetry route locked
   - final symmetry assumption removed at document level

## Installed closure chain

\[
\Gamma_{j,k}(y,x)=\Gamma_{j,k}(x,y)
\Longrightarrow
\mathsf T^{(1),\mathrm{proj}}_{j,k}=0
\Longrightarrow
|\mathsf R^{\mathrm{proj}}_{j,k}|
\le
C\,2^{-j}2^{-k}\|\nabla S_k\|_{L^\infty}\|\omega_k\|_{L^1}
\]
\[
\Longrightarrow
\text{paired commutator closure}
\Longrightarrow
\text{Claim 5}
\Longrightarrow
\text{shell-product }H^1\text{ gain}
\Longrightarrow
\text{deviatoric coercivity}
\Longrightarrow
\text{final DDYO continuum closure.}
\]

## Remaining status

Status: Conditional.

Reason:
the route is now fully locked as the canonical projector-based closure path, but the repo still needs a single canonical status document asserting that the RA1n frontier has been reduced from an open theorem object to a conditional closure route based on the projector-paired-symmetry chain.

## Canonical frontier statement

The former terminal object
\[
\mathsf T^{(1)}_{j,k}=0
\]
has been reduced to the projector-based exchange-symmetry route and is no longer tracked as a free-standing unconstrained leakage object.

The remaining repo-level task is status normalization:
record that RA1n is now a conditional closure package whose remaining gap is verification/promotion, not discovery of a new missing theorem statement.

