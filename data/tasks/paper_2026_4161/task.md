# Problem

## Setup

Let d and k be positive integers, let n>=2 be an integer, and let p_0 be a probability density on R^d. Let W_t be standard d-dimensional Brownian motion independent of X_0~p_0, and consider

dX_t=sqrt(2)dW_t.

For t>0, write p_t for the positive smooth density of X_t and s_t=nabla log p_t for its score. Equivalently, at each fixed t>0, X_t has the same law as X_0+sqrt(2t)epsilon, where epsilon~N(0,I_d) is independent of X_0. Take n independent copies of this process.

Write boldsymbol{x}=(x^(1),...,x^(n)) in (R^d)^n. For a fixed linear map A:R^d->R^k, set B=A^T A, bar x=n^{-1}sum_i x^(i), and

Var_n^A(boldsymbol{x})=n^{-1}sum_i ||A(x^(i)-bar x)||^2.

Define

Z_A=integral_{(R^d)^n} Var_n^A(boldsymbol{u}) product_i p_0(u^(i)) d boldsymbol{u},

and assume 0<Z_A<infinity. The variance-weighted batch target is the probability density

pi_0^A(boldsymbol{x})=Z_A^{-1}Var_n^A(boldsymbol{x}) product_i p_0(x^(i)).

Let q_t^A denote the density at time t>0 of the batch process

boldsymbol{U}_t=boldsymbol{U}_0+sqrt(2)boldsymbol{W}_t,

where boldsymbol{U}_0 has density pi_0^A and boldsymbol{W}_t is standard nd-dimensional Brownian motion independent of boldsymbol{U}_0. Define s_t^{pi^A}=nabla_boldsymbol{x} log q_t^A.

For t>0 define

mu_t(x)=x+2t s_t(x),

J_t(x)=I_d+2t nabla s_t(x),

where (nabla s_t)_(ab)=partial_b(s_t)_a. For a differentiable d-by-d matrix field M, use column-wise divergence

[div M]_c=sum_{b=1}^d partial_b M_(bc).

Set

h_t^A(boldsymbol{x})=Var_n^A(mu_t(x^(1)),...,mu_t(x^(n)))+(n-1)n^{-2}sum_i [2t Tr(B)+4t^2 Tr(A(nabla s_t(x^(i)))A^T)].

Assume that s_t is three-times continuously differentiable in space for every t>0 and that h_t^A(boldsymbol{x})>0 for every t>0 and every batch boldsymbol{x}.

## Task

Prove that for every t>0 and every batch boldsymbol{x}, defining

g_t^{A,i}(boldsymbol{x})=(2/n)J_t(x^(i))^T B(mu_t(x^(i))-n^{-1}sum_j mu_t(x^(j)))+(n-1)n^{-2}4t^2 div(B nabla s_t(x^(i))),

the score of q_t^A is

s_t^{pi^A}(boldsymbol{x})=(s_t(x^(1)),...,s_t(x^(n)))+h_t^A(boldsymbol{x})^{-1}(g_t^{A,1}(boldsymbol{x}),...,g_t^{A,n}(boldsymbol{x})).

Consequently, prove that for every finite T>0 the reverse-time diffusion

dboldsymbol{Y}_r=2s_{T-r}^{pi^A}(boldsymbol{Y}_r)dr+sqrt(2)d overline{boldsymbol{W}}_r,  0<=r<T,

initialized with density q_T^A, has terminal density pi_0^A. Here overline{boldsymbol{W}} is standard nd-dimensional Brownian motion in the reverse-time filtration, the SDE is understood in the weak sense, and the terminal state is the continuous limit boldsymbol{Y}_T=lim_{r upward T}boldsymbol{Y}_r.
