# Conditional: RA1n GoodBounds frontier

## Target
Assemble the local and tail bounds into GoodBounds for the actual Fourier kernel Ghat.

## Required statement
There exist alpha, eps, C0, Cinf such that
- alpha < 3
- eps > 0
- C0 > 0
- Cinf > 0
- for all xi with |xi| <= 1,
  |Ghat(xi)| <= C0 * |xi|^(-alpha)
- for all xi with |xi| >= 1,
  |Ghat(xi)| <= Cinf * (1 + |xi|)^(-3-eps)

## Registry consequence
GoodBounds -> L1_integrable -> C = 1.

## Truthfulness rule
Do not claim GoodBounds, L1_integrable, or C = 1 before both local and tail estimates are proved for the actual Ghat.
