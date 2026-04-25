# RA1n Transfer Split Definitions

Status: OPEN.

## Purpose

This file defines the canonical split needed to prove the RA1n Transfer Decomposition Lemma.

## Definitions

Define the main transfer term

\[
M_k
\]

to be the curvature-gap contribution in the RA1n transfer identity.

Define the error transfer term

\[
E_k
\]

to be the projection-error contribution in the RA1n transfer identity.

The target identity is

\[
\boxed{
\mathcal T_{\mathrm{RA1n}}(k)=M_k-E_k.
}
\]

## Required Bounds

\[
\boxed{
M_k\ge
\mathrm{Curv}_k\mathrm{Gap}_k|\partial_\xi\widehat G_k|.
}
\]

\[
\boxed{
E_k\le
\|P_k\widehat G_k\|_{\mathrm{err}}.
}
\]

## Consequence

If the split identity and both bounds hold, then

\[
\boxed{
\mathcal T_{\mathrm{RA1n}}(k)
\ge
\mathrm{Curv}_k\mathrm{Gap}_k|\partial_\xi\widehat G_k|
-
\|P_k\widehat G_k\|_{\mathrm{err}}.
}
\]

## Weakest Missing Ingredient

An explicit formula for \(M_k\) and \(E_k\) in terms of the existing RA1n terminal symbolic objects.
