# Conditional: RA1n certification checklist

## Required objects

- terminal_symbol_registered
- ghat_formula_explicit  
  Source: `docs/math/RA1N_GHAT_FORMULA.md`
- local_bound_proved  
  Source: `docs/math/RA1N_GHAT_LOCAL_BOUND_PROOF.md`
- tail_bound_proved  
  Source: `docs/math/RA1N_GHAT_TAIL_BOUND_PROOF.md`
- goodbounds_assembled  
  Source: `docs/status/RA1N_GOODBOUNDS_GATE.md`
- registry_gate_satisfied  
  Source: `ClayProblemLab/RA1nL1Registry.lean`

## Gate logic

Set `allCertified = true` only if every required object above is present and verified.

See also:
- `docs/status/RA1N_GOODBOUNDS_GATE.md`
- `docs/status/RA1N_ALLCERTIFIED_FRONTIER.md`

## Upgrade rule

Do not claim CANONICAL before:
- the exact \(\widehat G(\xi)\) formula is explicit,
- the local bound is proved,
- the tail bound is proved,
- GoodBounds is assembled,
- the registry gate is satisfied.

## Status

Conditional.
