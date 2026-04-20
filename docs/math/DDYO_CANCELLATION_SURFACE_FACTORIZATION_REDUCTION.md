# DDYO Cancellation Surface Factorization Reduction

## Status
CONDITIONAL

## Scope
This note records the corrected cancellation-surface reduction for the DDYO / RA1n coercivity track.
It is a sufficient reduction only.
It does **not** prove necessity.
It does **not** prove "weakest possible" without an additional division lemma.

## Setup
Let
\[
\omega=(\xi,\eta)\in \mathbb R^2\times \mathbb R^2.
\]

Fix shell parameters
\[
0<\lambda<\Lambda<\infty,\qquad B>0,\qquad C\ge 1.
\]

Define
\[
K_k:=
\Bigl\{
(\xi,\eta):
\lambda 2^k\le |\xi|\le \Lambda 2^k,\ 
\lambda 2^k\le |\eta|\le \Lambda 2^k,\ 
|\xi+\eta|\le B2^{k-C}
\Bigr\}.
\]

Define the cancellation-surface equation
\[
g_k(\xi,\eta):=\det(\xi,\eta)=\xi_1\eta_2-\xi_2\eta_1.
\]

Define
\[
C_k:=\{\omega\in K_k:g_k(\omega)=0\}.
\]

Let
\[
r_k:U_k\to\mathbb R
\]
be defined on an open set \(U_k\supset K_k\), and define
\[
Z_k:=\{\omega\in K_k:r_k(\omega)=0\}.
\]

## Explicit geometry of \(g_k\)
\[
\nabla g_k(\xi,\eta)=\bigl(\eta_2,-\eta_1,-\xi_2,\xi_1\bigr),
\qquad
|\nabla g_k(\xi,\eta)|^2=|\xi|^2+|\eta|^2.
\]

Hence on \(K_k\),
\[
\sqrt{2}\lambda\,2^k\le |\nabla g_k(\omega)|\le \sqrt{2}\Lambda\,2^k.
\]

## Correct sufficient reduction
Assume
\[
r_k(\omega)=g_k(\omega)\,b_k(\omega)\qquad(\omega\in U_k),
\]
with
\[
b_k\in C^2(U_k),
\qquad
m_b:=\inf_{\omega\in K_k}|b_k(\omega)|>0.
\]

This factorization is **sufficient** for the cancellation-surface package below.

## Immediate consequences
### (M1)
\[
r_k|_{C_k}=0.
\]

### (M2)
\[
Z_k=C_k.
\]

Proof:
\[
r_k(\omega)=0
\iff
g_k(\omega)b_k(\omega)=0
\iff
g_k(\omega)=0
\iff
\omega\in C_k,
\]
because \(|b_k(\omega)|\ge m_b>0\) on \(K_k\).

### (M3)
For \(\zeta\in C_k\),
\[
\nabla r_k(\zeta)=b_k(\zeta)\nabla g_k(\zeta),
\]
hence with
\[
\nu_k(\zeta):=\frac{\nabla g_k(\zeta)}{|\nabla g_k(\zeta)|},
\]
one has
\[
\partial_{\nu_k}r_k(\zeta)=b_k(\zeta)\,|\nabla g_k(\zeta)|.
\]

Therefore
\[
\inf_{\zeta\in C_k}|\partial_{\nu_k}r_k(\zeta)|
\ge
m_b\,\sqrt{2}\lambda\,2^k
>0.
\]

### (M4)
\[
r_k\in C^2(U_k).
\]

Moreover, for every \(\varepsilon_k>0\),
\[
M_k:=
\sup_{\omega\in N_{\varepsilon_k}(Z_k)\cap K_k}|D^2r_k(\omega)|<\infty
\]
by compactness.

### (M5)
Since
\[
Z_k=C_k,
\]
the set
\[
K_k\setminus N_{\varepsilon_k}(Z_k)=K_k\setminus N_{\varepsilon_k}(C_k)
\]
is compact, and \(g_k\neq 0\) there.

Define
\[
m_g(k,\varepsilon_k):=
\inf_{\omega\in K_k\setminus N_{\varepsilon_k}(C_k)}|g_k(\omega)|>0.
\]

Then
\[
\mu_k:=
\inf_{\omega\in K_k\setminus N_{\varepsilon_k}(Z_k)}|r_k(\omega)|
=
\inf_{\omega\in K_k\setminus N_{\varepsilon_k}(C_k)}|g_k(\omega)b_k(\omega)|
\ge
m_b\,m_g(k,\varepsilon_k)
>0.
\]

### (M6)
For every \(\rho>0\),
\[
Z_k=C_k\subset N_{\rho/2}(C_k).
\]

## Quotient extension
Define on \(K_k\setminus C_k\),
\[
a_k(\omega):=\frac{r_k(\omega)}{g_k(\omega)}.
\]

Then
\[
a_k(\omega)=b_k(\omega)\qquad(\omega\in K_k\setminus C_k),
\]
so \(a_k\) extends continuously to all of \(K_k\) by
\[
a_k=b_k\quad\text{on }K_k.
\]

Hence
\[
\inf_{\omega\in K_k}|a_k(\omega)|=m_b>0.
\]

## Certification region and corrected quantitative bounds
Define
\[
\Gamma_{\mathrm{cert}}(k,\rho):=
\{\omega\in K_k:\operatorname{dist}(\omega,C_k)\ge \rho\}.
\]

Since \(Z_k=C_k\), define
\[
\gamma_{k,\rho}:=
\inf_{\omega\in\Gamma_{\mathrm{cert}}(k,\rho)}
\frac{|g_k(\omega)|}{\operatorname{dist}(\omega,C_k)}.
\]

Because the function
\[
\omega\mapsto \frac{|g_k(\omega)|}{\operatorname{dist}(\omega,C_k)}
\]
is continuous and positive on the compact set \(\Gamma_{\mathrm{cert}}(k,\rho)\), one has
\[
\gamma_{k,\rho}>0.
\]

Define
\[
\widetilde{\alpha}_{k,\rho}:=m_b\,\gamma_{k,\rho}.
\]

Then
\[
\kappa_{\mathrm{adj}}(k,\rho):=
\inf_{\omega\in\Gamma_{\mathrm{cert}}(k,\rho)}
\frac{|r_k(\omega)|^2}{\operatorname{dist}(\omega,Z_k)^2}
=
\inf_{\omega\in\Gamma_{\mathrm{cert}}(k,\rho)}
|b_k(\omega)|^2
\frac{|g_k(\omega)|^2}{\operatorname{dist}(\omega,C_k)^2}
\ge
m_b^2\gamma_{k,\rho}^2
=
\widetilde{\alpha}_{k,\rho}^{\,2}.
\]

Also,
\[
\delta_{\mathrm{sep}}(k,\rho):=
\operatorname{dist}(\Gamma_{\mathrm{cert}}(k,\rho),Z_k)
=
\operatorname{dist}(\Gamma_{\mathrm{cert}}(k,\rho),C_k)
\ge \rho.
\]

Therefore
\[
c_{\mathrm{need}}(k,\rho):=
\inf_{\omega\in\Gamma_{\mathrm{cert}}(k,\rho)}|r_k(\omega)|^2
\ge
\widetilde{\alpha}_{k,\rho}^{\,2}\rho^2.
\]

Equivalently,
\[
c_{\mathrm{need}}(k,\rho)\ge
m_b^2
\Bigl(\inf_{\omega\in\Gamma_{\mathrm{cert}}(k,\rho)}|g_k(\omega)|\Bigr)^2.
\]

## Honest frontier statement
What is proved here is a **sufficient reduction**:
\[
r_k=g_k\,b_k,\quad b_k\in C^2(U_k),\quad \inf_{K_k}|b_k|>0
\Longrightarrow
\text{all of }(M1)\text{--}(M6)\text{ and the corrected certification bounds.}
\]

What is **not** proved here:
1. necessity of the factorization;
2. "weakest possible" status;
3. derivation of the factorization from the DDYO / RA1n symbol itself.

## Minimal additional lemmas still missing
### Division lemma
\[
\forall r\in C^2(U_k),\qquad r|_{C_k}=0
\Longrightarrow
\exists\,b\in C^1(U_k)\text{ such that }r=g_k\,b.
\]

### Nonvanishing transfer lemma
\[
r_k=g_k\,b_k,\quad
Z_k=C_k,\quad
\inf_{\zeta\in C_k}|\partial_{\nu_k}r_k(\zeta)|>0
\Longrightarrow
\inf_{\omega\in K_k}|b_k(\omega)|>0.
\]

### Repository finish condition
Replace `CONDITIONAL` by `PROVED` only after the actual DDYO / RA1n residual symbol is shown repository-natively to admit the factorization
\[
r_k=g_k\,b_k
\]
with an explicit lower bound
\[
\inf_{\omega\in K_k}|b_k(\omega)|>0
\]
on the certified shell region.
