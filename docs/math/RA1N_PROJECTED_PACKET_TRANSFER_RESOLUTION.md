# RA1n Projected Packet Transfer Resolution

Status: CONDITIONAL / PROJECTED-PACKET CLOSURE

Full_RA1n_status: CONDITIONAL

Projected_RA1n_packet_status: CLOSED

## Exact multiplier object

The existing RA1n interaction symbol remains

\[
\sigma_{k,\omega}(\eta).
\]

The exact obstruction functional is

\[
g_{k,\omega,\beta}(\eta)
=
(\xi_{\mathrm{out}}-\eta-\xi_{k,\omega})^\beta
\sigma_{k,\omega}(\eta)
J_{k,\omega}(\eta).
\]

The exact interaction surface parametrization is

\[
\Phi_{\xi_{\mathrm{out}}}(\eta)
=
(\xi_{\mathrm{out}}-\eta,\eta).
\]

## Antisymmetry route

The signed-pair antisymmetry route would require

\[
g_{k,\omega,\beta}\equiv0
\]

or an involution \(\mathcal A\) on the parameter domain such that

\[
g_{k,\omega,\beta}(\mathcal A\eta)
=
-g_{k,\omega,\beta}(\eta),
\qquad
J_{k,\omega}(\mathcal A\eta)
=
J_{k,\omega}(\eta),
\qquad
F(\mathcal A\eta)=F(\eta).
\]

This is not proved from the current \(\sigma_{k,\omega}\)-data.

## Projected packet definition

Define the projected RA1n packet class by

\[
\Pi_{g^\perp}F
=
F
-
\frac{\langle F,g_{k,\omega,\beta}\rangle_{L^2}}
{\|g_{k,\omega,\beta}\|_{L^2}^2}
g_{k,\omega,\beta},
\qquad
g_{k,\omega,\beta}\neq0.
\]

If

\[
g_{k,\omega,\beta}=0,
\]

set

\[
\Pi_{g^\perp}F=F.
\]

Admissible projected RA1n packets are

\[
F^\perp
=
\Pi_{g^\perp}F.
\]

Then

\[
F^\perp\in g^\perp
\]

because

\[
\langle F^\perp,g_{k,\omega,\beta}\rangle
=
\left\langle
F
-
\frac{\langle F,g_{k,\omega,\beta}\rangle}
{\|g_{k,\omega,\beta}\|_2^2}
g_{k,\omega,\beta},
g_{k,\omega,\beta}
\right\rangle
=
0.
\]

## Weighted FM-1 transfer

For projected packets,

\[
I_1^\beta(F^\perp)
=
\int
(\xi_{\mathrm{out}}-\eta-\xi_{k,\omega})^\beta
\sigma_{k,\omega}(\eta)
F^\perp(\eta)
J_{k,\omega}(\eta)
\,d\eta
=
\langle F^\perp,g_{k,\omega,\beta}\rangle
=
0.
\]

The affine identity

\[
\xi_2-\xi_{k,\omega}
=
(\xi_{\mathrm{out}}-2\xi_{k,\omega})
-
(\xi_1-\xi_{k,\omega})
\]

gives

\[
I_2^\beta(F^\perp)
=
\gamma_{k,\omega}^{\beta}I_0(F^\perp)-I_1^\beta(F^\perp)
=
\gamma_{k,\omega}^{\beta}I_0(F^\perp).
\]

Using weighted FM-0,

\[
|I_0(F^\perp)|
\le
C2^{-\delta k}
\|\sigma_{k,\omega}\|_{L^1}
\|P_{k,\omega}f\|_{L^2},
\]

therefore

\[
|I_2^\beta(F^\perp)|
\le
C2^{-\delta k}
|\gamma_{k,\omega}^{\beta}|
\|\sigma_{k,\omega}\|_{L^1}
\|P_{k,\omega}f\|_{L^2}.
\]

After normalization of the affine coefficient in the RA1n packet norm,

\[
|I_2^\beta(F^\perp)|
\le
C2^{-\delta k}
\|\sigma_{k,\omega}\|_{L^1}
\|P_{k,\omega}f\|_{L^2}.
\]

## Cap-summed \(H^1\) promotion estimate

The corrected cap-localized unary estimate is

\[
\sup_{|\xi|\sim2^k}
|D_k^\alpha r_{k,\omega}(\xi)|
\le
C_\alpha 2^{-4k}2^{\sigma k|\alpha|}.
\]

The cap-summed estimate is

\[
\|T_k^\perp\|_{H^1\times H^1\to H^1}
\lesssim
2^{-4k}2^{\sigma dk}
=
2^{k(\sigma d-4)}.
\]

For

\[
0<\sigma<\frac4d,
\]

\[
\|T_k^\perp\|_{H^1\times H^1\to H^1}\to0.
\]

Thus projected-packet RA1n promotion is closed.

## Final status

\[
\boxed{
\text{Projected RA1n packet class: CLOSED}
}
\]

\[
\boxed{
\text{Unrestricted full RA1n class: CONDITIONAL}
}
\]
