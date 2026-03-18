# AKCL Gap Closed Conditionally by Exact Paley–Wiener Transfer

## Input Chain

1. Mellin–Fourier isometry  
2. Exact Fourier Paley–Wiener theorem  
3. Entire extension of
   g(u)=e^{u/2}f(e^u)
4. Contour shift
5. Tail decay
6. Uniform tail domination
7. Core lower bound
8. Localized coercivity

## Derived Statement

If
\[
M_f\!\left(\tfrac12+it\right)
\]
is compactly supported in \([-B,B]\),
then
\[
g(u)=e^{u/2}f(e^u)
\]
is entire of exponential type \(B\).

Hence contour shift is valid, so
\[
|f(x)| \le C_\eta x^{-(1/2+\eta)}.
\]

Therefore
\[
\varepsilon_B(L) \le C(B)e^{-L}L^{-2\eta-1}\to 0.
\]

Combined with
\[
E[f]\ge c_0\int_{\mathrm{Core}(L)}|f|^2w,
\]
this yields
\[
E[f]\ge \frac{c_0}{1+\varepsilon_B(L)}\|f\|_{L^2(w)}^2.
\]

Passing to large \(L\),
\[
E[f]\ge c_0\|f\|_{L^2(w)}^2.
\]

## Conclusion

AKCL holds on the Mellin-bandlimited admissible class.

## Status

Conditional on exact transfer of Fourier Paley–Wiener regularity through the weighted Mellin correspondence.
