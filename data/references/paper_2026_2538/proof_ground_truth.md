# Reference Proof

## Proof Structure

1. Encode a classifier by its class-0 decision region and reduce the constrained loss minimization to maximizing its class-0 probability under a mixture-mass budget.
2. Use the likelihood-ratio ordering to show that the superlevel region at the capacity threshold maximizes this objective.
3. Use the assumed no-atom condition to attain the budget exactly.
4. Identify the same threshold with the Bayes likelihood-ratio threshold for normalized modified priors.

## Complete Proof

For a measurable classifier `g`, let `A_g={x:g(x)=0}`. Then
`P(g(X)=0,Y=0)=pi_0 F_0(A_g)` and `P(g(X)=0)=M(A_g)`, where
`M(A)=pi_0F_0(A)+pi_1F_1(A)`. Since `pi_0` is fixed,
`L(g)=1-pi_0F_0(A_g)` is minimized over `C_b` exactly when `F_0(A_g)` is maximized subject to `M(A_g)<=b pi_0`.

Write `r=f_0/f_1` on `{f_1>0}`, set `r=+infinity` on `{f_1=0<f_0}`, and set `r=0` where `f_0=f_1=0`. Let `A*=A_{gamma*}={r>gamma*}`. By assumption, `M(A*)=b pi_0` and `M({r=gamma*})=0`.

Take any feasible measurable region `A`, and put `B=A\\A*` and `C=A*\\A`. On `B` one has `f_0<=gamma* f_1`, while on `C` one has `f_0>gamma* f_1` (up to null sets). Therefore
`F_0(A)-F_0(A*) = integral_B f_0 - integral_C f_0 <= gamma* (F_1(A)-F_1(A*))`.
Feasibility and `M(A*)=b pi_0` give
`pi_0(F_0(A)-F_0(A*))+pi_1(F_1(A)-F_1(A*))<=0`, hence
`F_1(A)-F_1(A*) <= -(pi_0/pi_1)(F_0(A)-F_0(A*))`.
Combining the two inequalities yields
`(1+gamma* pi_0/pi_1)(F_0(A)-F_0(A*))<=0`, so `F_0(A)<=F_0(A*)`. (When `gamma*=0`, the first inequality already gives the same conclusion.) Thus the classifier `g_b=0` on `A*` and `1` elsewhere is optimal, and it attains the capacity exactly.

Define normalized modified class weights by
`pi'_0=1/(1+gamma*)` and `pi'_1=gamma*/(1+gamma*)`. The classical Bayes rule for these weights assigns class 0 precisely when `pi'_0 f_0>pi'_1 f_1`, equivalently when `r>pi'_1/pi'_0=gamma*`. Its possible equality set is null by the no-atom assumption, so it coincides with `g_b` almost surely. Hence the capacity-constrained optimum is exactly a Bayes classifier under the modified prior weights.
