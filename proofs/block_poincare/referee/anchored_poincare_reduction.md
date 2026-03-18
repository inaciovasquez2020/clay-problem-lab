# Anchored Poincaré Reduction on the Block Graph

## Anchoring
Fix a distinguished block \(B_0\) and impose
\[
m_{B_0}=0.
\]

## Target inequality
Prove
\[
\sum_B |B|\,|m_B|^2
\le
C_{\mathrm{anch}}
\sum_{(B,B')\in E(\mathcal B_L)} |m_B-m_{B'}|^2,
\]
with
\[
C_{\mathrm{anch}}<\infty
\]
independent of volume.

## Path expansion
For each block \(B\), choose a shortest path
\[
B_0 \to B.
\]
Then
\[
m_B=\sum_{e\in \gamma(B_0,B)} \delta_e m,
\qquad
\delta_e m := m_{B'}-m_B.
\]

## Cauchy estimate
\[
|m_B|^2
\le
|\gamma(B_0,B)|
\sum_{e\in \gamma(B_0,B)} |\delta_e m|^2.
\]

## Summation target
Prove edge multiplicity bound
\[
\sum_{B:\, e\in \gamma(B_0,B)} |\gamma(B_0,B)| \le C
\]
under the chosen normalization regime.

## Consequence
Anchored control yields a volume-independent replacement for \(C_{\mathrm{bg}}\).

## Status
Absolute coercivity constant reduced to anchored path-count bound.
