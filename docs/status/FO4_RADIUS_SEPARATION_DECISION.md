# Conditional: FO4 radius-separation decision

## Extracted values

\[
R = R_EXTRACTED_VALUE,\qquad
\delta_{\mathrm{sep}} = DELTA_SEP_EXTRACTED_VALUE
\]

## Decision

Exactly one must be certified:

\[
R > \delta_{\mathrm{sep}}
\quad\text{or}\quad
R \le \delta_{\mathrm{sep}}.
\]

## Registry gate

- If \(R > \delta_{\mathrm{sep}}\): enable obstruction preservation.
- If \(R \le \delta_{\mathrm{sep}}\): keep separation obstruction active.

## Status

Conditional.
