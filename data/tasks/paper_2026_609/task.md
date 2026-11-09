# Problem

## Setup

Let X be a nonempty Borel subset of R^d, with its Euclidean subspace topology, and let Y be a nonempty compact subset of R. On a probability space with law P, let Z_n=(X_n,Y_n) take values in X times Y. Set G_0 to be the trivial sigma-algebra and G_n=sigma(Z_1,...,Z_n) for n>=1.

Fix measurable versions of the conditional probability kernels

P_n(x,A)=P(Y_{n+1} in A | X_{n+1}=x,G_n),

for Borel A subset Y, with P_0(x,A)=P(Y_1 in A | X_1=x). Thus these versions are defined for every x, and their dependence on the history is G_n-measurable. Define their CDFs by

F_n(x,t)=P_n(x,Y intersect (-infinity,t]),  t in R,

and define Delta_k(x,t)=F_k(x,t)-F_{k-1}(x,t).

Assume that, for every t in Y, the family of functions x↦F_n(x,t), n>=0, is almost surely equicontinuous. Assume also that, for every fixed x in X and t in R, the signed drift series is almost surely convergent and its tails satisfy

sum_{k>n} E[Delta_k(x,t)|G_{k-1}] -> 0 almost surely.

The first assertion below asks for a limiting random probability kernel. Denote its CDF by tilde F(x,t).

Fix an integer m>=1, a deterministic finite grid (x_i,t_i) in X times R, i=1,...,m, and a deterministic gamma in (0,1]. Write

bold F_n=(F_n(x_i,t_i))_{i=1}^m,
bold tilde F=(tilde F(x_i,t_i))_{i=1}^m,
Delta_k=bold F_k-bold F_{k-1},
b_{k,i}=E[Delta_{k,i}|G_{k-1}].

For this grid, assume each t_i is a continuity point of the function t↦E[tilde F(x_i,t)]. Assume the following for every i:

(a) The two sequences

n^{gamma/2} sum_{k>n} b_{k,i},
 n^{gamma/2} sup_{k>=n}|b_{k,i}|

converge almost surely to zero. Each sequence is dominated in L1: its absolute values, for all n>=1, are bounded almost surely by a single nonnegative integrable random variable, which may depend on i and on the sequence.

(b) n^gamma sum_{k>=n} b_{k,i}^2 -> 0 almost surely.

(c) E[sup_{k>=1} k^{gamma/2}|Delta_{k,i}|]<infinity.

(d) sum_{k>=1} k^{2gamma} E[Delta_{k,i}^4]<infinity.

Define

R_n=n^gamma sum_{k>n} Delta_k Delta_k^T,
U_n=(n^{gamma+1}/gamma) E[Delta_{n+1}Delta_{n+1}^T|G_n],
V_n=(1/n) sum_{k=1}^n (k^{gamma+1}/gamma) Delta_k Delta_k^T.

Assume U_n converges almost surely, entrywise, to a finite symmetric positive-definite random matrix V. The quantity U_n is the exact conditional expectation under P; V_n is computed from the observed predictive increments.

For conditional probability kernels, almost-sure weak convergence means weak convergence of their probability measures for almost every outcome. All matrix limits below mean entrywise almost-sure convergence. For a positive-definite matrix A, A^{-1/2} denotes its symmetric positive-definite inverse square root.

## Credible sets

Fix alpha in (0,1). Let z_{1-alpha/2} be the standard normal (1-alpha/2)-quantile, and let q_{m,1-alpha} be the (1-alpha)-quantile of ||G||_2 for G distributed as N_m(0,I_m). For positive-definite A, let c_{1-alpha}(A) be the exact (1-alpha)-quantile of

max_{1<=j<=m} |H_j|/sqrt(A_jj),  H distributed as N_m(0,A).

For either choice A_n=U_n or A_n=V_n, whenever A_n is positive definite define

E_n(A_n)={theta in R^m: n^gamma (theta-bold F_n)^T A_n^{-1}(theta-bold F_n)<=q_{m,1-alpha}^2},

I_{n,j}(A_n)=[F_{n,j}-z_{1-alpha/2}sqrt(A_{n,jj}/n^gamma), F_{n,j}+z_{1-alpha/2}sqrt(A_{n,jj}/n^gamma)],

B_n(A_n)={theta in R^m: |theta_j-F_{n,j}|<=c_{1-alpha}(A_n)sqrt(A_{n,jj}/n^gamma) for every j}.

Here F_{n,j} is coordinate j of bold F_n. At indices where A_n is not positive definite, set the studentized vector below to zero and take these sets to be their full ambient spaces. These conventions only define the quantities at such indices.

## Task

Prove the following integrated theorem.

1. There exists a random probability kernel with CDF tilde F(x,t), supported on Y, such that on a probability-one event P_n(x,·) converges weakly to this kernel for every x in X.

2. Under the additional finite-grid assumptions, the series defining R_n are finite almost surely, R_n->V and V_n->V almost surely, and

Law(n^{gamma/2}(bold F_n-bold tilde F)|G_n) => N_m(0,V) almost surely.

3. Both U_n and V_n are eventually positive definite almost surely. For either choice A_n=U_n or A_n=V_n,

Law(n^{gamma/2} A_n^{-1/2}(bold tilde F-bold F_n)|G_n) => N_m(0,I_m) almost surely.

4. For each fixed alpha in (0,1) and either covariance choice, almost surely,

P(bold tilde F in E_n(A_n)|G_n) -> 1-alpha,
P(tilde F(x_j,t_j) in I_{n,j}(A_n)|G_n) -> 1-alpha for every j,
P(bold tilde F in B_n(A_n)|G_n) -> 1-alpha.

The coordinate projections of E_n(A_n) also give credible intervals: their conditional coverage has limit inferior at least 1-alpha. This last assertion does not claim exact nominal marginal calibration of ellipsoid projections when m>1.
