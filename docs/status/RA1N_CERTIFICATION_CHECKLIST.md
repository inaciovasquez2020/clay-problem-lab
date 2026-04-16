# Conditional: RA1n certification checklist

## Required objects

- terminal_symbol_registered
- ghat_formula_explicit
- local_bound_proved
- tail_bound_proved
- goodbounds_assembled

## Gate logic

Set `allCertified = true` only if every required object above is present and verified.

See also: `docs/status/RA1N_GOODBOUNDS_GATE.md`.

## Upgrade rule

Do not claim CANONICAL before:
- the exact \(\widehat G(\xi)\) formula is explicit,
- the local bound is proved,
- the tail bound is proved,
- GoodBounds is assembled,
- the registry gate is satisfied.

## Status

Conditional.
