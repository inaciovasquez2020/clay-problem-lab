# Mellin Contour Shift Step

## Conditional Input

Assume
g(u)=f(e^u)e^{u/2}
extends holomorphically to
|\Im u| < \sigma

and satisfies
|g(u+iv)| \le C_\sigma(B)e^{B|v|}.

## Shift

For 0 < \eta < \sigma,
apply the inverse Fourier formula on the line \Im u = \eta.

Then
|g(u)| \le C_{\sigma,\eta}(B)e^{- \eta u}
for u \to +\infty.

## Pullback

Since
f(e^u)=e^{-u/2}g(u),

we obtain
|f(e^u)| \le C_{\sigma,\eta}(B)e^{-(1/2+\eta)u}.

Equivalently, with x=e^u,

|f(x)| \le C_{\sigma,\eta}(B)x^{-(1/2+\eta)}.

## Target

Use the weight
w(x)=e^{-x}
to deduce

\int_L^\infty |f(x)|^2 w(x)\,dx
\le
C_{\sigma,\eta}(B)e^{-L}L^{-1-2\eta}.
