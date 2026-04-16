# Conditional: renormalized flux route

Assume
\[
\widetilde{\mathrm{Flux}}_\ell
\lesssim
E_\ell^{1+\theta}
\Bigl(\sum_{m\le \ell}2^{m}E_m\Bigr)^{\frac{1-\theta}{2}},
\qquad \theta\in(0,1).
\]

Define
\[
D_\ell:=2^\ell E_\ell,
\qquad
S_\ell:=\sum_{m\le \ell}2^mE_m=\sum_{m\le \ell}D_m.
\]

Set
\[
\widetilde{\mathcal F}_K(t):=
\sum_{\ell\le K}2^{-2\ell}\int_{t-2^{-2K}}^{t}\widetilde{\mathrm{Flux}}_\ell(s)\,ds.
\]

Define
\[
\mathcal D_K(t):=
\int_{t-2^{-2K}}^{t}\sum_{\ell\le K}2^\ell E_\ell(s)\,ds,
\qquad
\mathcal Q_K(t):=
\int_{t-2^{-2K}}^{t}\sum_{\ell\le K}2^{-\ell}E_\ell(s)^2\,ds.
\]

Using
\[
\Bigl(\sum_{\ell\le K} a_\ell\Bigr)^{\frac{2}{1+\theta}}
\le
(K+1)^{\frac{1-\theta}{1+\theta}}
\sum_{\ell\le K} a_\ell^{\frac{2}{1+\theta}},
\]
with \(a_\ell=2^{-2\ell}E_\ell^{1+\theta}\), one gets
\[
\widetilde{\mathcal F}_K(t)
\lesssim
(K+1)^{\frac{1-\theta}{2}}
2^{K\frac{\theta-3}{2}}
\mathcal D_K(t)^{\frac{1-\theta}{2}}
\mathcal Q_K(t)^{\frac{1+\theta}{2}}.
\]

Hence, if
\[
\sup_{K,t}\mathcal D_K(t)\le D_0,
\qquad
\sup_{K,t}2^{-2K}\mathcal Q_K(t)\le \eta_0,
\]
then
\[
\sup_{K,t}\widetilde{\mathcal F}_K(t)
\lesssim_\theta
D_0^{\frac{1-\theta}{2}}\eta_0^{\frac{1+\theta}{2}}.
\]

Therefore, whenever
\[
D_0^{\frac{1-\theta}{2}}\eta_0^{\frac{1+\theta}{2}}
\le c\,\varepsilon_0,
\]
the \(\widetilde{\mathcal F}\)-smallness criterion closes.

Weakest remaining object:
\[
\widetilde{\mathrm{Flux}}_\ell
\lesssim
E_\ell^{1+\theta}
\Bigl(\sum_{m\le \ell}2^mE_m\Bigr)^{\frac{1-\theta}{2}}.
\]

No separate uniform summation lemma is needed; the \((K+1)^{\frac{1-\theta}{2}}\) loss is absorbed by \(2^{K(\theta-1)}\).
