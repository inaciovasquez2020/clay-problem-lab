# Navier--Stokes Frontier Snapshot (2026-04-10)

## Verified sampled state
- DDYO wall sampled layer: 31/31 tests passing.
- Verified sampled DDYO components:
  - exact pair partition
  - single-shell advective cancellation
  - single-shell skew cancellation
  - positive strain contribution
  - full-shell strain dominance proxy
  - theta-active-set nonemptiness
  - localized active-tail proxy split
  - theta-tail monotonicity
- J2B sampled frontier now includes:
  - exact gradient-level stretch split into strain + skew
  - shear-shell skew vanishing test
  - product-rule bound
    \[
    \|\nabla(S\nabla\omega)\|_{L^1}
    \le
    \|\nabla S\|_{L^\infty}\|\nabla\omega\|_{L^1}
    +
    \|S\|_{L^\infty}\|\nabla^2\omega\|_{L^1}.
    \]

## DDYO commutator frontier
- sampled same-scale commutator split verified
- sampled same-scale commutator bound verified
- sampled rotation-part cancellation against h' verified
- sampled normalized commutator ratio integer-dilation stability verified

## DDYO commutator absorbability frontier
- sampled strain/rotation commutator split verified
- sampled strain commutator Kato--Ponce proxy bound verified
- sampled rotation commutator lower-order proxy verified
- sampled epsilon-proxy integer-dilation stability verified
- active wall: continuum commutator-absorbability lemma

## Exact skew-adjoint reduction frontier
- sampled exact pairing split into symmetric + rotational parts verified
- sampled rotational pairing vanishes before magnitude bounds
- sampled symmetric pairing recovers full pairing after cancellation
- active wall: continuum exact skew-adjoint reduction before norm estimates

## Symmetric commutator pairing frontier
- sampled commutator pairing split into symmetric + rotational parts verified
- sampled rotational commutator pairing lower-order proxy verified
- sampled symmetric commutator pairing epsilon-proxy verified
- sampled symmetric commutator pairing integer-dilation stability verified
- active wall: continuum symmetric commutator pairing absorbability lemma

## Truthful frontier
- sampled wall structure: verified
- continuum DDYO high-high absorbability: open
- continuum J2B exact residual closure: open
- full continuum solve / global regularity closure: open
