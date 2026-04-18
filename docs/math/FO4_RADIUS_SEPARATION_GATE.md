# Conditional: FO4 radius-separation gate

## Gate statement

\[
\mathrm{PreserveObstructionClass}
:=
\bigl(R>\delta_{\mathrm{sep}}\bigr).
\]

## Consequence

Only if
\[
R>\delta_{\mathrm{sep}}
\]
is certified may one assert
\[
[T_R(z)]\neq 0 \iff [z]\neq 0.
\]

## Failure mode

If
\[
R\le \delta_{\mathrm{sep}},
\]
then the separation obstruction remains active and preservation is not certified.

## Truthfulness rule

Do not claim preservation of the obstruction class or Double Dime admissibility before this gate is certified.
