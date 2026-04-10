# NAK spectral-gap lemma

## Minimal missing assumption

Let
\[
S=\frac{\nabla u+(\nabla u)^\top}{2},\qquad
\omega=\nabla\times u,\qquad
\widehat\omega=\frac{\omega}{|\omega|}.
\]

Write the ordered eigenvalues of \(S\) as
\[
\lambda_1(S)\ge \lambda_2(S)\ge \lambda_3(S).
\]

Assume there exists
\[
\kappa>0
\]
such that
\[
\lambda_1(S(x,t))-\lambda_2(S(x,t))\ge \kappa
\qquad
\text{for all }(x,t)\text{ with }|\omega(x,t)|>0.
\]

Then the principal eigendirection
\[
e_1(S(x,t))
\]
is smooth as a function of \(S(x,t)\), and for every \(s>\frac52\),
\[
\|\lambda_1(S)\|_{H^s}+\|e_1(S)\|_{H^s}\le C_{\kappa,s}\|S\|_{H^s}.
\]

## NAK quantities

Define
\[
A:=1-(\widehat\omega\cdot e_1(S))^2,
\]
\[
R_{\mathrm{NAK}}[u]:=\int_{\mathbb R^3} A\,|\omega|^{3/2}\,dx,
\]
\[
\mathcal C_{\mathrm{NAK}}[u]:=\int_{\mathbb R^3}\big|\nabla(\sqrt A\,|\omega|^{3/4})\big|^2\,dx.
\]

## Conditional closure form

Under the spectral-gap assumption,
\[
\frac{d}{dt}R_{\mathrm{NAK}}[u]+\mathcal C_{\mathrm{NAK}}[u]
\le
C_{\kappa,s}\big(\mathcal D[u]+\Phi[u]+R_{\mathrm{NAK}}[u]\big),
\]
and
\[
\Sigma_{\mathrm{NAK}}[u]
\le
\eta\big(\mathcal D[u]+\lambda \mathcal C_{\mathrm{NAK}}[u]\big)
+
C_{\kappa,s,\eta}\big(\Phi[u]+\lambda R_{\mathrm{NAK}}[u]\big),
\qquad
0\le \eta<1.
\]

## Status

The weakest sufficient new ingredient is a uniform spectral-gap lemma for the top strain eigenvalue on the vorticity support.
