# Conditional: RA1n Ghat local bound frontier

## Target
Prove local integrability near the origin for the actual Fourier kernel Ghat.

## Required statement
There exist alpha and C0 such that
- alpha < 3
- C0 > 0
- for all xi with |xi| <= 1,
  |Ghat(xi)| <= C0 * |xi|^(-alpha)

## Role in closure
This is the local half of GoodBounds.
Combined with the tail bound, it yields L1_integrable.

## Truthfulness rule
Do not claim GoodBounds or L1_integrable before this local estimate is proved for the actual Ghat.
