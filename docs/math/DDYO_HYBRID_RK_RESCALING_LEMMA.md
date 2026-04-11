# DDYO Hybrid \(r_k\) Rescaling Lemma

## Target lemma

Assume the exact DDYO/RA1n remainder symbol in the repository admits the hybrid fixed-annulus form
\[
r_k(\xi)=2^{-k}\rho(2^{-k}\xi)
\qquad\text{for }|\xi|\sim 2^k,
\]
where
\[
\rho\in C^\infty(\{\eta\in\mathbb R^3:c\le |\eta|\le C\})
\]
is independent of \(k\).

Then for every multi-index \(\alpha\in\mathbb N^3\),
\[
\sup_{k\ge 0}\ \sup_{|\xi|\sim 2^k}
2^{k(1+|\alpha|)}
\left|\partial_\xi^\alpha r_k(\xi)\right|
<\infty.
\]

## Proof

For every multi-index \(\alpha\),
\[
\partial_\xi^\alpha r_k(\xi)
=
2^{-k}2^{-k|\alpha|}\,
(\partial^\alpha \rho)(2^{-k}\xi).
\]
Hence
\[
2^{k(1+|\alpha|)}
\left|\partial_\xi^\alpha r_k(\xi)\right|
=
\left|(\partial^\alpha \rho)(2^{-k}\xi)\right|.
\]
If \(|\xi|\sim 2^k\), then \(|2^{-k}\xi|\sim 1\), so \(2^{-k}\xi\) ranges in the fixed annulus
\[
\{\eta:c\le |\eta|\le C\}.
\]
Therefore
\[
\sup_{k\ge 0}\ \sup_{|\xi|\sim 2^k}
2^{k(1+|\alpha|)}
\left|\partial_\xi^\alpha r_k(\xi)\right|
\le
\sup_{c\le |\eta|\le C}
\left|(\partial^\alpha \rho)(\eta)\right|
<\infty.
\]
This proves the target estimate.

## Closure corollary

If the exact repository formula for \(r_k\) is verified to have the above hybrid fixed-annulus form, then:
\[
\text{symbol derivative bound}
\Longrightarrow
\text{annular fixed-scale kernel bound}
\Longrightarrow
\text{RA1n}
\Longrightarrow
\text{unconditional DDYO closure.}
\]

## Remaining exact verification task

Verify from the exact repository formula for \(r_k\) that there exists a \(k\)-independent
\[
\rho\in C^\infty(\{\eta:c\le |\eta|\le C\})
\]
such that
\[
r_k(\xi)=2^{-k}\rho(2^{-k}\xi)
\qquad\text{for }|\xi|\sim 2^k.
\]
