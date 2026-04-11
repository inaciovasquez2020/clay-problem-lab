# DDYO RA1n Shell-Product Kernel Estimate (Conditional)

## Conditional theorem

Assume:
\[
\varphi\in C_c^\infty(\mathbb R^3),
\qquad
\operatorname{supp}\varphi\subset\left\{\tfrac12\le |\xi|\le 2\right\},
\qquad
|j-k|\le C_0,
\]
and
\[
|\partial_\xi^\alpha r_k(\xi)|
\le C_\alpha\,2^{-k(1+|\alpha|)}
\]
for every multi-index \(\alpha\) and every
\[
\xi\in\operatorname{supp}\bigl(\varphi(2^{-k}\cdot)\bigr).
\]

Define
\[
m_{j,k}(\xi):=\varphi(2^{-j}\xi)\varphi(2^{-k}\xi)r_k(\xi),
\qquad
K_{j,k}:=\mathcal F^{-1}[m_{j,k}].
\]

Then for every \(N\ge 0\) there exists \(C_N<\infty\) such that
\[
\int_{\mathbb R^3}(1+|x|)^N|K_{j,k}(x)|\,dx\le C_N\,2^{-k}.
\]

## Proof

Set
\[
\widetilde m_{j,k}(\eta):=m_{j,k}(2^k\eta)
=\varphi(2^{k-j}\eta)\varphi(\eta)\,r_k(2^k\eta).
\]

For every multi-index \(\alpha\),
\[
\partial_\eta^\alpha \widetilde m_{j,k}(\eta)
=
\sum_{\beta+\gamma+\delta=\alpha}
c_{\beta,\gamma,\delta}\,
\partial^\beta\!\bigl[\varphi(2^{k-j}\eta)\bigr]\,
\partial^\gamma\varphi(\eta)\,
2^{k|\delta|}\bigl(\partial^\delta r_k\bigr)(2^k\eta).
\]

Since \(|j-k|\le C_0\),
\[
\sup_\eta \left|\partial^\beta\!\bigl[\varphi(2^{k-j}\eta)\bigr]\right|
\le C_\beta,
\]
while the symbol assumption gives
\[
2^{k|\delta|}\left|(\partial^\delta r_k)(2^k\eta)\right|
\le C_\delta\,2^{-k}.
\]

Hence, for every integer \(M\ge 0\),
\[
\|\widetilde m_{j,k}\|_{C^M(\mathbb R^3)}\le C_M\,2^{-k}.
\]

Also,
\[
\operatorname{supp}\widetilde m_{j,k}
\subset
\{\eta:c_1\le |\eta|\le c_2\}
\]
for constants \(0<c_1<c_2<\infty\) depending only on \(\varphi\) and \(C_0\).

Let
\[
\widetilde H_{j,k}:=\mathcal F^{-1}[\widetilde m_{j,k}].
\]
Because \(\widetilde m_{j,k}\) is smooth and compactly supported, \(\widetilde H_{j,k}\) is Schwartz. Moreover, its Schwartz seminorms are bounded by \(C_M2^{-k}\). Therefore, for every \(N\ge 0\),
\[
\int_{\mathbb R^3}(1+|y|)^N|\widetilde H_{j,k}(y)|\,dy\le C_N\,2^{-k}.
\]

Now
\[
K_{j,k}(x)=2^{3k}\widetilde H_{j,k}(2^k x),
\]
so with the change of variables \(y=2^k x\),
\[
\int_{\mathbb R^3}(1+|x|)^N|K_{j,k}(x)|\,dx
=
\int_{\mathbb R^3}(1+2^{-k}|y|)^N|\widetilde H_{j,k}(y)|\,dy.
\]

For \(k\ge 0\),
\[
(1+2^{-k}|y|)^N\le (1+|y|)^N,
\]
hence
\[
\int_{\mathbb R^3}(1+|x|)^N|K_{j,k}(x)|\,dx
\le
\int_{\mathbb R^3}(1+|y|)^N|\widetilde H_{j,k}(y)|\,dy
\le
C_N\,2^{-k}.
\]

This proves the conditional theorem.

## Scope note

This proves the shell-product kernel estimate only under the stated symbol-derivative hypothesis on \(r_k\).

It does not by itself certify unconditional DDYO closure from the current repository state.
