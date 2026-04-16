# Conditional: RA1n GoodBounds lemmas

## Local lemma

\[
\mathrm{LocalGoodBound} :=
\exists \alpha<3,\ \exists C_0>0,\ \forall |\xi|\le 1,\quad
|\widehat G(\xi)| \le C_0 |\xi|^{-\alpha}.
\]

## Tail lemma

\[
\mathrm{TailGoodBound} :=
\exists \varepsilon>0,\ \exists C_\infty>0,\ \forall |\xi|\ge 1,\quad
|\widehat G(\xi)| \le C_\infty (1+|\xi|)^{-3-\varepsilon}.
\]

## Assembly lemma

\[
\mathrm{GoodBounds} := \mathrm{LocalGoodBound} \wedge \mathrm{TailGoodBound}.
\]

## Certification consequence

\[
\mathrm{GoodBounds} \Longrightarrow L^1\text{-integrable} \Longrightarrow C=1.
\]

## Truthfulness rule

Do not claim GoodBounds, \(L^1\)-integrable, or \(C=1\) before both component lemmas are established for the actual \(\widehat G\).
