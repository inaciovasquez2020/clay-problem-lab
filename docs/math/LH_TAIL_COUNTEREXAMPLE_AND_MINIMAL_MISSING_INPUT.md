# Conditional: LH tail counterexample and minimal missing input

Let
\[
D_\ell:=2^\ell E_\ell,
\qquad
S_\ell:=\sum_{m\le \ell}D_m.
\]

Define the upper-tail quantity
\[
T_\ell:=\sum_{m\ge \ell+4}2^{-m}D_m^{1/2}.
\]

The candidate bound
\[
T_\ell
\le
C\,2^{-\ell/2}S_\ell^{1/2}
\]
cannot hold from \((D_\ell,S_\ell)\) alone.

Counterexample: fix \(\ell\), set \(S_\ell=1\), and define
\[
D_m=
\begin{cases}
1,&m=\ell,\\
M^2\,2^{2N},&m=N,\\
0,&\text{otherwise},
\end{cases}
\qquad N\ge \ell+4.
\]

Then
\[
S_\ell=\sum_{m\le \ell}D_m=1,
\]
but
\[
T_\ell
=
\sum_{m\ge \ell+4}2^{-m}D_m^{1/2}
=
2^{-N}(M\,2^N)=M.
\]

Hence the bound would imply
\[
M\le C\,2^{-\ell/2}
\]
for all \(M>0\), contradiction.

Therefore no inequality controlling the \(LH\) tail by \((D_\ell,S_\ell)\) only is possible.

Minimal missing input:
\[
\exists\,U_\ell\ge 0\ \text{ such that }\ 
\sum_{m\ge \ell+4}2^{-m}D_m^{1/2}\le U_\ell
\quad\text{and}\quad
\widetilde{\mathrm{Flux}}_\ell^{LH}
\lesssim E_\ell\,2^{\ell/2}U_\ell.
\]

Closure condition:
\[
\sup_{K,t}
\sum_{\ell\le K}2^{-2\ell}\int_{t-2^{-2K}}^{t}E_\ell(s)\,2^{\ell/2}U_\ell(s)\,ds
\le \varepsilon_0.
\]
