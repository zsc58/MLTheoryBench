# Problem

## Setup

Let O be a bounded domain in R^d with smooth boundary, and let the set of modes be {1,...,m}, where m>=2. Let b_i:R^d->R^d, sigma:R^d->R^{d x d}, and f_i:R^d->[0,infinity) be continuously differentiable. The diffusion coefficient sigma is the same in every mode. Write a=sigma sigma^T and
\[
L_i\phi=b_i\cdot D\phi+\tfrac12\operatorname{tr}(aD^2\phi).
\]
Assume that a constant C_coef bounds the values and first derivatives of b_i, sigma, and f_i on O, uniformly in i. Assume also that, for some sigma_0>0,
\[
\xi^Ta(x)\xi\geq\sigma_0|\xi|^2
\quad(x\in O,\ \xi\in\mathbb R^d).
\]
Let r>0. The switching costs G_ij are constants satisfying G_ii=0, G_ij>0 for i!=j, and G_ij+G_jk>G_ik for pairwise distinct modes i,j,k.

Let V* be the classical switching value, characterized as the continuous viscosity solution on the closure of O of
\[
\max\left\{-L_iV_i^*-f_i+rV_i^*,\quad V_i^*-\min_{j\ne i}(V_j^*+G_{ij})\right\}=0
\quad\text{in }O,
\qquad V_i^*=0\quad\text{on }\partial O.
\]

An admissible randomized policy is a bounded Borel measurable state-feedback generator q=(q_ij):O->R^{m x m}, with q_ij>=0 for i!=j and q_ii=-sum_{j!=i}q_ij. Each policy is bounded, but no common numerical bound is imposed on the whole policy class. Starting from X_0=x and I_0=i, the state evolves until boundary exit according to
\[
dX_t=b_{I_t}(X_t)\,dt+\sigma(X_t)\,dW_t,
\]
where W is a d-dimensional Brownian motion and the conditional jump intensity from mode i to mode j is q_ij(X_t). Write
\[
\tau_O=\inf\{t\geq0:X_t\notin O\}.
\]
Define D(q|1)=q log q-q+1 for q>=0, with 0 log 0=0. For lambda>0 set
\[
J_i^\lambda(x;q)=\mathbb E_{i,x}^{q}\!\left[\int_0^{\tau_O}e^{-rt}\left(f_{I_t}(X_t)+\sum_{j\ne I_t}q_{I_tj}(X_t)G_{I_tj}+\lambda\sum_{j\ne I_t}D(q_{I_tj}(X_t)\mid1)\right)dt\right],
\qquad
V_i^\lambda(x)=\inf_q J_i^\lambda(x;q).
\]
The payoff at exit is zero.

## Task

Prove that for every lambda>0, V^lambda is the unique vector in C^2(O)^m intersect C(cl O)^m satisfying
\[
L_iV_i^\lambda+f_i-rV_i^\lambda+\lambda\sum_{j\ne i}\left(1-\exp\left(\frac{V_i^\lambda-V_j^\lambda-G_{ij}}{\lambda}\right)\right)=0
\quad\text{in }O,
\]
with V_i^lambda=0 on the boundary and
\[
0\leq V_i^\lambda\leq\frac{C_{\rm coef}+(m-1)\lambda}{r}.
\]
Prove that an optimal feedback policy has off-diagonal entries
\[
q_{ij}^\lambda(x)=\exp\left(\frac{V_i^\lambda(x)-V_j^\lambda(x)-G_{ij}}{\lambda}\right),
\qquad i\ne j,
\]
and diagonal entries equal to minus their row sums.

Moreover, prove that constants C_Lip and C, depending only on the fixed domain, coefficients, ellipticity bound, discount, number of modes, and switching costs, but not on lambda, can be chosen so that
\[
|DV_i^\lambda(x)|\leq C_{\rm Lip}
\quad\text{for every }\lambda>0,\ i,\ x\in O,
\]
and, for all sufficiently small lambda>0, uniformly in i and x,
\[
V_i^\lambda-C\lambda\log(1/\lambda)\leq V_i^*\leq V_i^\lambda.
\]
Also prove, for all sufficiently small lambda>0,
\[
\kappa(\lambda)V_i^\lambda-
\frac{(1-\kappa(\lambda))C_{\rm coef}+(m-1)\lambda}{r}
\leq V_i^*,
\]
where
\[
\kappa(\lambda)=\min_{i\ne j}\frac{G_{ij}}{G_{ij}+\lambda\log(C_{\rm up}/\lambda)},
\qquad C_{\rm up}=2C_{\rm coef}(1+C_{\rm Lip}).
\]
