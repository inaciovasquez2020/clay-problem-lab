# RA1n Conditional Closure Record

Status: CONDITIONAL

## Action 1 — Shell comparability installed as an explicit hypothesis

**Hypothesis SC\((A,C_0)\).** There exist constants \(A \ge 1\) and \(C_0 < \infty\) such that for every dyadic index \(k\) and every \(m,n\) satisfying
\[
|m-k| \le C_0,\qquad |n-k| \le C_0,
\]
one has
\[
E_m \le A\,E_k,\qquad E_n \le A\,E_k.
\]

## Action 2 — Conditional theorem

**Conditional Theorem (RA1n-coerc).** Assume SC\((A,C_0)\). Assume further that there exist \(\beta \in \mathbb R\) and \(C>0\) such that for all \(k\) and all \(m,n\) with \(|m-k|,|n-k|\le C_0\),
\[
\left|
\int_{\xi=\eta+\zeta}
r_k(\eta,\zeta)\,
(\widehat u_m(\eta)\otimes \widehat u_n(\zeta)):\overline{\widehat u_k(\xi)}
\,d\eta\,d\zeta
\right|
\le
C\,2^{\beta k}\,E_k^{1/2}E_m^{1/2}E_n^{1/2}.
\]
Then
\[
\sum_{\substack{m,n\\|m-k|\le C_0\\|n-k|\le C_0}}
\left|
\int_{\xi=\eta+\zeta}
r_k(\eta,\zeta)\,
(\widehat u_m(\eta)\otimes \widehat u_n(\zeta)):\overline{\widehat u_k(\xi)}
\,d\eta\,d\zeta
\right|
\le
C'\,A\,2^{\beta k}\,E_k^{3/2},
\]
where \(C' = C'(C_0)\).

Without SC\((A,C_0)\), one obtains only
\[
\sum_{\substack{m,n\\|m-k|\le C_0\\|n-k|\le C_0}}
\left|
\int_{\xi=\eta+\zeta}
r_k(\eta,\zeta)\,
(\widehat u_m(\eta)\otimes \widehat u_n(\zeta)):\overline{\widehat u_k(\xi)}
\,d\eta\,d\zeta
\right|
\le
C\,2^{\beta k}\,E_k^{1/2}
\sum_{\substack{m,n\\|m-k|\le C_0\\|n-k|\le C_0}}
E_m^{1/2}E_n^{1/2}.
\]

## Action 3 — Unconditional frontier

The unconditional frontier is exactly SC\((A,C_0)\).

## Action 4 — Norm test

Membership in \(\dot H^s\) or \(\dot B^0_{2,\infty}\) alone does not imply SC\((A,C_0)\).

## Action 5 — Monotone shell envelope

Define
\[
\mathcal M_k := \sup_{|j-k|\le C_0} E_j.
\]

Then:
\[
\mathcal M_k \ge E_j \quad \text{for all } |j-k|\le C_0,
\]
and
\[
\mathrm{SC}(A,C_0) \iff \mathcal M_k \le A\,E_k \quad \text{for all } k.
\]

Moreover,
\[
\sum_{\substack{m,n\\|m-k|\le C_0\\|n-k|\le C_0}}
E_m^{1/2}E_n^{1/2}
\le
N(C_0)\,\mathcal M_k,
\]
where \(N(C_0) = (2C_0+1)^2\). Hence
\[
\sum_{\substack{m,n\\|m-k|\le C_0\\|n-k|\le C_0}}
\left|
\int_{\xi=\eta+\zeta}
r_k(\eta,\zeta)\,
(\widehat u_m(\eta)\otimes \widehat u_n(\zeta)):\overline{\widehat u_k(\xi)}
\,d\eta\,d\zeta
\right|
\le
C\,N(C_0)\,2^{\beta k}\,E_k^{1/2}\mathcal M_k.
\]

Thus the exact closure alternative is:
\[
E_k^{1/2}\mathcal M_k \lesssim E_k^{1+\theta}
\]
for some \(\theta\in(0,1)\), equivalently
\[
\mathcal M_k \lesssim E_k^{1/2+\theta}.
\]
