# Conditional: FO4 radius versus separation status

## Extracted simulation radius

\[
R=SIMULATED_RADIUS
\]

Source:
- `KERNEL_TRANSPORT_CONFIGURATION_SOURCE`

## Certified separation scale

\[
\delta_{\mathrm{sep}}=CERTIFIED_DELTA_SEP
\]

Source:
- `SEPARATION_OBSTRUCTION_SOURCE`

## Decision gate

Exactly one of the following must be asserted after extraction:

\[
R>\delta_{\mathrm{sep}}
\]

or

\[
R\le \delta_{\mathrm{sep}}.
\]

## Preservation gate

The preservation claim
\[
[T_R(z)]\neq 0 \iff [z]\neq 0
\]
may be used only under the certified inequality
\[
R>\delta_{\mathrm{sep}}.
\]

## Double Dime admissibility gate

Do not claim Double Dime admissibility unless the inequality
\[
R>\delta_{\mathrm{sep}}
\]
is proved from the extracted values.

## Status

Conditional.
