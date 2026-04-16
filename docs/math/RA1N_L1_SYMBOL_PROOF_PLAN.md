# Conditional: RA1n L1 symbol proof plan

## Remaining target
Prove GoodBounds for the actual Fourier kernel Ghat.

## Required inputs
1. Exact formula for Ghat(xi).
2. Local singularity analysis near xi = 0.
3. Tail decay analysis as |xi| -> infinity.

## Required outputs
- alpha < 3
- eps > 0
- C0 > 0
- Cinf > 0
- proof that
  |Ghat(xi)| <= C0 * |xi|^(-alpha) for |xi| <= 1
- proof that
  |Ghat(xi)| <= Cinf * (1 + |xi|)^(-3-eps) for |xi| >= 1

## Registry consequence
GoodBounds -> L1_integrable -> C = 1.

## Truthfulness rule
Do not claim CANONICAL before GoodBounds is proved for the actual symbol.
