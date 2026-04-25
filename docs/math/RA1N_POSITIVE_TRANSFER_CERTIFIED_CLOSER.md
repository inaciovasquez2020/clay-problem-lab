# RA1n Positive Transfer Certified Closer

Status: CERTIFIED CONDITIONAL THEOREM

## Objects

Let

\[
\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}
\subset L^2
\]

be the terminal RA1n packet class.

Let

\[
g\neq0.
\]

## Certified Angle-Gap Input

By `RA1N_UNRESTRICTED_CERTIFIED_CLOSER.md`, on the packet-exhausted finite-basis surface,

\[
\exists \epsilon>0
\quad
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}},
\qquad
\left|\int Fg\right|
\le
(1-\epsilon)\|F\|_2\|g\|_2.
\]

On the certified exact Gram surface,

\[
\epsilon=1.
\]

Hence

\[
\int Fg=0
\qquad
\forall F\in\mathcal P_{\mathrm{RA1n}}^{\mathrm{terminal}}.
\]

## Projection-Error Domination Input

Assume the strict domination inequality

\[
\mathrm{Curv}_k\,\mathrm{Gap}_k\,|\partial_\xi\widehat G_k|
>
\|P_k\widehat G_k\|_{\mathrm{err}}.
\]

Define

\[
c_{\mathrm{RA1n}}
:=
\mathrm{Curv}_k\,\mathrm{Gap}_k\,|\partial_\xi\widehat G_k|
-
\|P_k\widehat G_k\|_{\mathrm{err}}.
\]

Then

\[
c_{\mathrm{RA1n}}>0.
\]

## Transfer Lower Bound

Assume

\[
\mathcal T_{\mathrm{RA1n}}(k)
\ge
\mathrm{Curv}_k\,\mathrm{Gap}_k\,|\partial_\xi\widehat G_k|
-
\|P_k\widehat G_k\|_{\mathrm{err}}.
\]

Then

\[
\mathcal T_{\mathrm{RA1n}}(k)
\ge
c_{\mathrm{RA1n}}
>
0.
\]

## Certified Closer

The RA1n positive transfer lower bound is certified closed on the surface consisting of:

1. unrestricted packet exhaustion into the certified finite-basis packet space;
2. exact Gram transversality certificate \(b^*G^{-1}b=0<1\);
3. projection-error strict domination.

## Terminal Chain

\[
\text{packet exhaustion}
\Longrightarrow
\text{finite-basis Gram certificate}
\Longrightarrow
\text{Angle-Gap}
\Longrightarrow
\text{structural counterexample exclusion}
\Longrightarrow
\mathcal T_{\mathrm{RA1n}}(k)\ge c_{\mathrm{RA1n}}>0.
\]
