# DDYO RA1n First-Moment Bound Proof

## Objective
Establish that the first moment of the shell-product interaction satisfies:
\[
\left| \int x_\ell \, G_j(x) \, e^{(j)}_{ab}(D) \omega_k(x) \, dx \right| \le C \, 2^{-j} 2^{-k} \|\omega_k\|_{L^1}
\]

## Proof: Bernstein Extraction via Fourier Derivative
1. **Fourier Representation**: Let K(x) = G_j(x)\,[e^{(j)}_{ab}(D)\omega_k](x). The first moment is:
   \[ M_{1,\ell} = \int x_\ell K(x) \, dx = i \left. \frac{\partial}{\partial \xi_\ell} \widehat{K}(\xi) \right|_{\xi=0} \]
2. **Symbol Decomposition**: The symbol of the product is the convolution of the symbols:
   \[ \widehat{K}(\xi) = \left( \hat{G}_j * \left[ \text{symb}(e^{(j)}_{ab}) \cdot \hat{\omega}_k \right] \right)(\xi) \]
3. **Derivative Application**: By the properties of convolution:
   \[ \partial_{\xi_\ell} \widehat{K}(0) = \int (\partial_{\xi_\ell} \hat{G}_j)(-\eta) \cdot \text{symb}(e^{(j)}_{ab})(\eta) \cdot \hat{\omega}_k(\eta) \, d\eta \]
4. **Scale Extraction**:
   - Since $\hat{G}_j(\xi) = \phi(2^{-j}\xi)$, we have $\partial_{\xi_\ell} \hat{G}_j \sim 2^{-j}$.
   - The operator $e^{(j)}_{ab}(D)$ contributes the claimed dyadic scale; the extra $2^{-k}$ factor is not justified here without an additional argument.
5. **Conclusion**: The ^{-j}$ factor is a direct consequence of the Bernstein inequality in frequency space. Combined with the ^{-k}$ gain from the dyadic commutator structure, the bound holds.


### Missing Lemma (Exact RA1n Reduction)

To justify the \(2^{-k}\) factor, it suffices to prove:
\[
\left\|
e^{(j)}_{ab}(D)\omega_k
\right\|_{L^1}
\le
C\,2^{-k}\|\omega_k\|_{L^1}.
\]

Equivalently, at the symbol level:
\[
|\mathrm{symb}(e^{(j)}_{ab})(\eta)|
\lesssim 2^{-k}
\quad \text{for } |\eta|\sim 2^k.
\]

This is the exact missing step converting the Bernstein \(2^{-j}\) gain
into the full \(2^{-j}2^{-k}\) RA1n bound.

## Status
- **Continuum Closure**: Not established by this file.
- **Status**: Proof sketch only; repository frontier remains conditional on RA1n.
