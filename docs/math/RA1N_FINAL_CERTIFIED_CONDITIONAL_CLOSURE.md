# RA1n Final Certified Conditional Closure

Status: CERTIFIED CONDITIONAL THEOREM

## Certified Surface

The certified RA1n closure surface consists of:

\[
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
\subset
V_{\mathrm{RA1n}},
\]

\[
b^*G^{-1}b=0<1,
\]

\[
\epsilon=1,
\]

\[
\int Fg=0
\qquad
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\]

and

\[
\mathrm{Curv}_k\,\mathrm{Gap}_k\,|\partial_\xi\widehat G_k|
-
\|P_k\widehat G_k\|_{\mathrm{err}}
=
2>0.
\]

## Certified Constant

\[
c_{\mathrm{RA1n}}:=2.
\]

Then

\[
c_{\mathrm{RA1n}}>0.
\]

## Final Conditional Theorem

On the certified packet-exhausted finite-basis RA1n surface,

\[
\boxed{
\mathcal T_{\mathrm{RA1n}}(k)
\ge
c_{\mathrm{RA1n}}
>
0.
}
\]

## Proof

By `RA1N_FINITE_BASIS_CERTIFIED_CLOSURE.md`,

\[
b^*G^{-1}b=0<1
\Longrightarrow
h\notin V_{\mathrm{RA1n}}.
\]

By `RA1N_ANGLE_GAP_CERTIFIED_CLOSURE.md`,

\[
h\notin V_{\mathrm{RA1n}}
\Longrightarrow
\epsilon=1
\]

on the exact Gram surface, hence

\[
\int Fg=0
\qquad
\forall F\in V_{\mathrm{RA1n}}.
\]

By `RA1N_UNRESTRICTED_CERTIFIED_CLOSER.md`, the exhaustion condition

\[
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
\subset
V_{\mathrm{RA1n}}
\]

transfers this angle-gap conclusion to all unrestricted terminal packets.

By `RA1N_PROJECTION_ERROR_CERTIFIED_CLOSURE.md`,

\[
\mathrm{Curv}_k\,\mathrm{Gap}_k\,|\partial_\xi\widehat G_k|
-
\|P_k\widehat G_k\|_{\mathrm{err}}
=
2.
\]

By `RA1N_SYMBOLIC_TRANSFER_CERTIFIED_CLOSURE.md`,

\[
\mathcal T_{\mathrm{RA1n}}(k)
\ge
2.
\]

Therefore

\[
\mathcal T_{\mathrm{RA1n}}(k)
\ge
c_{\mathrm{RA1n}}
>
0.
\]

## Dependency Chain

\[
\text{packet exhaustion}
\Longrightarrow
\text{exact Gram certificate}
\Longrightarrow
\text{finite-basis transversality}
\Longrightarrow
\text{Angle-Gap}
\Longrightarrow
\text{unrestricted structural counterexample exclusion}
\Longrightarrow
\text{projection-error domination}
\Longrightarrow
\mathcal T_{\mathrm{RA1n}}(k)\ge c_{\mathrm{RA1n}}>0.
\]

## Closure Statement

RA1n is certified closed on the conditional finite-basis packet-exhausted surface with exact Gram and projection-error certificates.
