# Conditional: RA1n Ghat tail bound frontier

## Target
Prove tail integrability at infinity for the actual Fourier kernel Ghat.

## Required statement
There exist eps and Cinf such that
- eps > 0
- Cinf > 0
- for all xi with |xi| >= 1,
  |Ghat(xi)| <= Cinf * (1 + |xi|)^(-3-eps)

## Role in closure
This is the tail half of GoodBounds.
Combined with the local bound, it yields L1_integrable.

## Truthfulness rule
Do not claim GoodBounds or L1_integrable before this tail estimate is proved for the actual Ghat.
