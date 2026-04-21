# RA1n Terminal Region Factorization Route

Status: OPEN

Canonical residual:
\[
r_k(\xi,\eta)=\widehat G_k(\xi,\eta)-P_k\widehat G_k(\xi,\eta).
\]

Canonical compact terminal region:
\[
\Gamma_k^{\mathrm{term}}
:=
\Bigl\{
(\xi,\eta)\in\mathbb R^3\times\mathbb R^3:
2^{k-1}\le |\xi|\le 2^{k+1},\
2^{k-1}\le |\eta|\le 2^{k+1},\
|\xi+\eta|\le 2^{k+1},\
|\xi\wedge\eta|\ge \varepsilon 2^{2k}
\Bigr\}
\setminus \mathcal C_k,
\]
where \(\varepsilon>0\) is fixed and \(\mathcal C_k\) is the union of all currently known cancellation loci.

Exact next structural step:
define one explicit cancellation-surface equation
\[
g_k(\xi,\eta)=0
\]
such that
\[
Z_k:=\{(\xi,\eta):r_k(\xi,\eta)=0\}\subseteq \{(\xi,\eta):g_k(\xi,\eta)=0\}.
\]

Quotient:
\[
a_k(\xi,\eta):=\frac{r_k(\xi,\eta)}{g_k(\xi,\eta)}
\qquad\text{on }\{g_k\neq 0\}.
\]

Extension target:
extend \(a_k\) continuously to
\[
Z_k\cap \Gamma_k^{\mathrm{term}}.
\]

Required nonvanishing bounds:
\[
\inf_{(\xi,\eta)\in Z_k\cap \Gamma_k^{\mathrm{term}}}|a_k(\xi,\eta)|>0,
\qquad
\inf_{(\xi,\eta)\in Z_k\cap \Gamma_k^{\mathrm{term}}}\|\nabla g_k(\xi,\eta)\|>0.
\]

Target lower bound:
\[
|r_k(\xi,\eta)|
=
|a_k(\xi,\eta)|\,|g_k(\xi,\eta)|
\gtrsim
2^{-\alpha k}|\xi\wedge\eta|^2
\qquad\text{on }\Gamma_k^{\mathrm{term}}
\]
for some \(\alpha>0\).

Closure rule:
replace OPEN by PROVED only after the repository contains:
1. an explicit formula for \(g_k\);
2. a proof that \(Z_k\subseteq \{g_k=0\}\);
3. a continuous extension proof for \(a_k\) on \(Z_k\cap\Gamma_k^{\mathrm{term}}\);
4. the two strict positive infimum bounds above;
5. a repository-native derivation of the target lower bound for the canonical \(r_k\).

No-claim rule:
do not replace OPEN by PROVED before Items 1--5 are discharged.
