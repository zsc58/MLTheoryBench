# Problem

## Setup

Let P be the probability law of (X,R,D,Y), where X takes values in a measurable covariate space mathcal X contained in R^m, R,D belong to {0,1}, and Y is real-valued. The observed data are iid copies of
\[
Z=(X,R,RD,RDY).
\]
Here R=1 denotes the source population and R=0 the target population; Y is observed only when RD=1. Use P also for the induced law of Z. Write P_X for the pooled covariate marginal and P_S,P_T for the covariate laws conditional on R=1 and R=0, respectively. For an integrable random variable Q, define
\[
E_S[Q]=E[Q\mid R=1],\qquad E_T[Q]=E[Q\mid R=0].
\]

Fix a measurable predictor f:mathcal X->R and a measurable loss ell:R x R->[0,infinity), and write L=ell(f(X),Y). Define the finite target risk and nuisance functions by
\[
\psi=E_T[L],\quad \rho=P(R=0),\quad g(x)=P(R=0\mid X=x),
\]
\[
\mu(x)=E[L\mid X=x,R=1,D=1],\quad
\pi(x)=P(R=1,D=1\mid X=x),\quad
\pi_S(x)=P(D=1\mid X=x,R=1).
\]
Assume 0<rho<1, Y is conditionally independent of D given (X,R=1), the conditional law of Y given X is the same in the source and target populations, pi_S(X)>epsilon almost surely for some epsilon>0, and P_T is absolutely continuous with respect to P_S with dP_T/dP_S<=C on the covariate space for some finite C. Take measurable versions of the conditional functions; the conditional means and the moments below are well-defined.

For an evaluation sample Z_1,...,Z_n, let hat g, hat pi, hat mu be measurable real-valued nuisance estimates trained only on an independent auxiliary sample of n iid pooled observations. Define
\[
\hat\rho=\frac1n\sum_{i=1}^n1\{R_i=0\},
\]
and, when hatrho>0 and hat pi(X_i) is nonzero for every i with R_iD_i=1, define
\[
\hat\psi=\frac{1}{n\hat\rho}\sum_{i=1}^n
\left[R_iD_i\frac{\hat g(X_i)}{\hat\pi(X_i)}\{L_i-\hat\mu(X_i)\}
+(1-R_i)\hat\mu(X_i)\right].
\]
Set hat psi=0 on all other samples. Here L_i=ell(f(X_i),Y_i), and a contribution multiplied by R_iD_i is defined to be zero without evaluating its loss or ratio when R_iD_i=0.

Define the score
\[
\varphi(Z;P)=\frac{RD}{\pi(X)}\frac{g(X)}{\rho}\{L-\mu(X)\}
+\frac{1-R}{\rho}\{\mu(X)-\psi\},
\]
with the same convention that the first contribution is zero when RD=0.

All L2 norms below are with respect to P_X:
\[
\|h\|_2=\left(\int h(x)^2\,dP_X(x)\right)^{1/2}.
\]
Suppose, as n tends to infinity, that
\[
\|\hat\mu-\mu\|_2=o_p(1),\quad
\|\hat\pi-\pi\|_2=o_p(1),\quad
\|\hat g-g\|_2=o_p(1),
\]
there is a constant epsilon'>0 such that
\[
P\!\left(\inf_{x\in\mathcal X}\hat\pi(x)\ge\epsilon'/2,
\ \hat\rho\ge\rho/2\right)\to1,\qquad
P\!\left(\hat g(x)\in(0,1)\ \text{for all }x\in\mathcal X\right)\to1,
\]
for some finite M,
\[
E[(L-\mu(X))^2\mid X,R=1,D=1]\le M,\qquad
E[(\mu(X)-\psi)^2]\le M,
\]
\[
\|\hat\mu-\mu\|_2
\big(\|\hat\pi-\pi\|_2+\|\hat g-g\|_2\big)=o_p(n^{-1/2}),
\]
and E[varphi(Z;P)^2]<infinity. The conditional moment inequality holds almost surely. Probabilities and stochastic convergence involving fitted quantities include auxiliary-sample randomness; all displayed events and random quantities are measurable.

## Task

Prove that
\[
\hat\psi-\psi=\frac1n\sum_{i=1}^n\varphi(Z_i;P)+o_p(n^{-1/2}),
\]
and consequently
\[
\sqrt n\,(\hat\psi-\psi)\ \Rightarrow\
N\!\left(0,\operatorname{Var}_P\{\varphi(Z;P)\}\right).
\]
