# Problem

## Setup

Let `(X,Y)` be a binary model with `Y in {0,1}`, minority class `Y=0`, `X in R^d`, class priors `pi_0 in (0,1)` and `pi_1=1-pi_0`, and class-conditional densities `f_0,f_1` with distributions `F_0,F_1`. Let `C` be the measurable binary classifiers `g:R^d->{0,1}`. For a measurable set `A`, write
`M(A)=pi_0F_0(A)+pi_1F_1(A)`.

Fix `0<b<=1/pi_0` and define
`C_b={g in C: P(g(X)=0)<=b pi_0}` and
`L(g)=1-P(g(X)=0,Y=0)`.
Let
`r(x)=f_0(x)/f_1(x)` when `f_1(x)>0`, with `r(x)=+infinity` when `f_1(x)=0<f_0(x)` and `r(x)=0` when `f_0(x)=f_1(x)=0`. For `gamma>=0`, set `A_gamma={x:r(x)>gamma}`. Assume there is a threshold `gamma*` such that
`M(A_gamma*)=b pi_0` and `M({x:r(x)=gamma*})=0`.

## Task

Prove that the classifier `g_b` defined by `g_b(x)=0` for `x in A_gamma*` and `g_b(x)=1` otherwise minimizes `L(g)` over `C_b`. Moreover, prove that this same rule is a classical Bayes classifier for the class-prior weights
`pi'_0=1/(1+gamma*)` and `pi'_1=gamma*/(1+gamma*)`, whose likelihood-ratio threshold satisfies `pi'_1/pi'_0=gamma*` (with equality-boundary decisions immaterial because the boundary has zero probability).
