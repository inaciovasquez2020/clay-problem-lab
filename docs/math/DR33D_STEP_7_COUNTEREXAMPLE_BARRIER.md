# DR33D Step 7 — Counterexample Barrier for the Subquartic Bridge

## Objective
Record the obstruction showing that \(L^1\)- and \(L^2\)-type shell control alone do not force the Step 6 bridge.

## Shell profile
For \(N\ge 1\), define
\[
E_j^{(N)} :=
\begin{cases}
2^{2j}, & 0\le j\le N,\\
0, & j>N.
\end{cases}
\]

## Weighted square-root accumulation
Then
\[
\sum_j 2^{-j}\bigl(E_j^{(N)}\bigr)^{1/2}
=
\sum_{j=0}^N 2^{-j}2^j
=
N+1.
\]
Hence
\[
\left(\sum_j 2^{-j}\bigl(E_j^{(N)}\bigr)^{1/2}\right)^2
=
(N+1)^2.
\]

## \(L^1\)-type shell sum
One has
\[
\sum_j 2^{-2j}E_j^{(N)}
=
\sum_{j=0}^N 1
=
N+1.
\]

## \(L^2\)-type shell sum
One has
\[
\sum_j 2^{-4j}\bigl(E_j^{(N)}\bigr)^2
=
\sum_{j=0}^N 1
=
N+1.
\]

## Subquartic target
If Step 6 were forced from these weighted \(L^1\)- and \(L^2\)-type controls alone, then for some fixed \(\theta\in(0,1)\), \(C>0\),
\[
(N+1)^2
\le
C\sum_{j=0}^N 2^{2(1+\theta)j}.
\]

## Barrier statement
The shell profile above shows that the bridge mechanism depends on a new structural invariant, not merely on separate weighted \(L^1\)- and weighted \(L^2\)-type summability data.

## Conclusion
Weighted one-shell and two-shell size controls do not by themselves encode the cross-shell decay geometry required for the DR33D subquartic bridge.

## Status
LOCKED BARRIER — new invariant still required.
