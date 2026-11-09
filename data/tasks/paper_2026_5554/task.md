# Problem

## Setup

Let integers m,n,p,r satisfy rank(X)=p<m and 3 <= r <= min(m,n), where X is in R^{p x m}, and let Y be in R^{p x n}. For W in R^{m x n}, set

L(W)=1/2 ||XW-Y||_F^2,    G_ls(W)=X^T(XW-Y).

For a rank-k matrix A=U_A Sigma_A V_A^T in compact singular value decomposition, with k positive singular values, write P(A)=U_A V_A^T for its compact polar factor. Define

M={W:XW=Y},  X^dagger=X^T(XX^T)^(-1),  P_perp=I_m-X^dagger X.

Thus P_perp is symmetric, idempotent, and has operator norm one. Fix eta>0.

For a rank-r matrix W with positive singular values sigma=(sigma_1,...,sigma_r), put

rho=||W||_F,    tilde sigma_i=sigma_i/rho,

R_pw(sigma)=-sum_{i ne j} log(sigma_i+sigma_j),    tilde R_pw(W)=R_pw(tilde sigma),

S_i=sum_{j ne i}(tilde sigma_i+tilde sigma_j)^(-1),    C=binom(r,2),    q_i=S_i-C tilde sigma_i.

For part 1, let W(t) be a differentiable curve in M on an interval, with constant rank r and simple ordered positive singular values

W=U_W diag(sigma_1,...,sigma_r)V_W^T,    sigma_1>...>sigma_r>0,

satisfying the ideal projected self-polar flow

dot W=-eta P_perp P(W).

For part 3, independently consider a differentiable curve W:[0,T] -> R^{m x n}, where T>0, and a driving-matrix path G:[0,T] -> R^{m x n}. Fix delta_M>0 and define

dist_F(W,M)=inf_{Z in M} ||W-Z||_F.

Assume throughout [0,T] that dist_F(W(t),M)<=delta_M, that W(t) and G(t) both have rank r, and that W(t) has ordered positive singular values satisfying

sigma_r(W(t))>=delta_W>0,    min_{i ne j}|sigma_i(W(t))-sigma_j(W(t))|>=Delta>0.

Assume also that the least positive singular value of G(t) is at least delta_G>0. The actual flow and the self-polar field evaluated at the same W(t) are

dot W=F=-eta P_perp P(G(t)),    F_0=-eta P_perp P(W(t)).

All these hypotheses are assumed on the given interval [0,T]. Define

delta_P(t)=||P(G(t))-P(W(t))||_F,    bar_delta_P=sup_{0 <= t <= T} delta_P(t),

sigma_min(t)=min_{1 <= i <= r} sigma_i(W(t)).

The quantities rho, tilde sigma_i, S_i, and q_i in part 3 are evaluated at this actual W(t). Derivatives at endpoints are understood one-sided.

## Task

Prove the following integrated theorem.

1. Along the ideal flow, with alpha_i=[U_W^T P_perp U_W]_{ii}=||P_perp u_i||_2^2, prove

dot sigma_i=-eta alpha_i,    0 <= alpha_i <= 1,

d||W||_F^2/dt=-2eta sum_i alpha_i sigma_i <=0,

and

d tilde R_pw(W)/dt=(2eta/rho) sum_i alpha_i q_i.

Here normalized spectral flattening at a time means d tilde R_pw(W)/dt<=0. Thus prove that it occurs exactly when sum_i alpha_i q_i<=0. Show also that unequal normalized singular values have strictly opposite q-ordering: tilde sigma_i>tilde sigma_k implies q_i<q_k.

2. For every c>0, among all positive rank-r spectra with ||sigma||_2=c, the minimum of R_pw is attained uniquely at sigma_1=...=sigma_r=c/sqrt(r), up to permutation; singular-vector frames are irrelevant. This variational statement includes repeated singular values and is independent of the trajectory assumptions and the constraint XW=Y.

3. For the actual flow, define alpha_i by the same formula as in part 1, using the singular vectors of the actual W(t). Prove that constants C_1,C_2>0 depending only on r,delta_W,Delta (and delta_G where needed) satisfy, for every i and all t in [0,T],

|dot sigma_i+eta alpha_i| <= C_1 eta bar_delta_P,

|d tilde R_pw(W)/dt-(2eta/rho) sum_i alpha_i q_i| <= C_2 eta bar_delta_P/sigma_min(t).

Moreover, prove

delta_P(t) <= 2 ||G(t)-W(t)||_F / min(delta_G,delta_W).

If P(G(t))=P(W(t)) throughout [0,T], prove that delta_P is identically zero and the displayed ideal spectral identities hold exactly for the actual flow.
